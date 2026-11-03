"""Tests for src/scripts/release.py."""

import json
import os
import subprocess
from pathlib import Path

import pytest
from click.testing import CliRunner

from src.scripts import release as release_module
from src.scripts.release import (
    MIGRATORS_DIR,
    RELEASE_COMMIT_FILES,
    VERSIONED_ARTIFACTS,
    ReleaseError,
    check_lock_change,
    check_preconditions,
    check_release_artifacts,
    cli,
    command_failure,
    commit_and_tag,
    confirm_release,
    current_project_version,
    fetch_origin_main,
    find_migrators,
    gh_is_authenticated,
    is_prerelease,
    migrator_glob,
    next_project_version,
    pep440_to_semver,
    read_artifact_version,
    set_package_json_version,
    tag_for_version,
    unexpected_release_changes,
    untracked_artifacts,
    validate_bump_components,
)

REPO_ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize(
    ("version", "expected"),
    [
        ("11.26.0", "11.26.0"),
        ("11.26.0rc1", "11.26.0-rc.1"),
        ("12.0.0rc12", "12.0.0-rc.12"),
    ],
)
def test_pep440_to_semver(version: str, expected: str) -> None:
    assert pep440_to_semver(version) == expected


@pytest.mark.parametrize("version", ["11.26", "11.26.0a1", "11.26.0.dev0", "11.26.0rc1.post1", "v11.26.0", ""])
def test_pep440_to_semver_rejects_other_shapes(version: str) -> None:
    with pytest.raises(ValueError, match=r"X\.Y\.Z or X\.Y\.ZrcN"):
        pep440_to_semver(version)


def test_tag_for_version() -> None:
    assert tag_for_version("11.26.0rc1") == "v11.26.0-rc.1"
    assert tag_for_version("11.26.0") == "v11.26.0"


def test_is_prerelease() -> None:
    assert is_prerelease("11.26.0rc1")
    assert not is_prerelease("11.26.0")


def test_validate_bump_components_accepts_supported() -> None:
    validate_bump_components(["minor", "rc"])
    validate_bump_components(["stable"])


def test_validate_bump_components_rejects_empty() -> None:
    with pytest.raises(ReleaseError, match="BUMP is empty"):
        validate_bump_components([])


@pytest.mark.parametrize("component", ["alpha", "beta", "post", "dev", "minr"])
def test_validate_bump_components_rejects_unsupported(component: str) -> None:
    with pytest.raises(ReleaseError, match=component):
        validate_bump_components(["minor", component])


def test_migrator_glob_ignores_rc_suffix() -> None:
    assert migrator_glob("11.26.0rc2") == "migrator_from_*_to_11_26_0.py"
    assert migrator_glob("11.26.0") == "migrator_from_*_to_11_26_0.py"


def test_find_migrators(tmp_path: Path) -> None:
    (tmp_path / "migrator_from_11_24_1_to_11_25_0.py").write_text("")
    (tmp_path / "migrator_from_11_25_0_to_11_26_0.py").write_text("")
    expected = ["migrator_from_11_25_0_to_11_26_0.py"]
    assert [path.name for path in find_migrators("11.26.0rc1", tmp_path)] == expected
    assert [path.name for path in find_migrators("11.26.0", tmp_path)] == expected
    # From 11.26.0rc1, BUMP=minor gives 11.27.0, which needs its own migrator.
    assert find_migrators("11.27.0", tmp_path) == []


def test_find_migrators_in_repository() -> None:
    names = [path.name for path in find_migrators("11.25.0", REPO_ROOT / MIGRATORS_DIR)]
    assert names == ["migrator_from_11_24_1_to_11_25_0.py"]


def write_fake_release(repo: Path, version: str, package_version: str) -> None:
    """Write the six versioned artifacts and package.json, the way a release build leaves them."""
    for relative in VERSIONED_ARTIFACTS:
        path = repo / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.suffix == ".py":
            path.write_text(f'metamodel_version = "1.7.0"\nversion = "{version}"\n')
        elif path.suffix == ".json":
            path.write_text(json.dumps({"id": "https://w3id.org/nmdc/nmdc", "version": version}))
        else:
            path.write_text(f"id: https://w3id.org/nmdc/nmdc\nversion: {version}\n")
    (repo / "package.json").write_text(json.dumps({"name": "nmdc-schema", "version": package_version}))


def test_check_passes_when_versions_agree(tmp_path: Path) -> None:
    write_fake_release(tmp_path, "11.26.0rc1", "11.26.0-rc.1")
    assert check_release_artifacts(tmp_path, "11.26.0rc1") == []
    assert check_release_artifacts(tmp_path, "11.26.0rc1", tag="v11.26.0-rc.1") == []


def test_check_reports_stale_artifact(tmp_path: Path) -> None:
    write_fake_release(tmp_path, "11.26.0rc1", "11.26.0-rc.1")
    (tmp_path / "nmdc_schema/nmdc_pydantic.py").write_text('version = "0.0.0"\n')
    assert check_release_artifacts(tmp_path, "11.26.0rc1") == [
        "nmdc_schema/nmdc_pydantic.py says 0.0.0, expected 11.26.0rc1"
    ]


def test_check_reports_package_json_mismatch(tmp_path: Path) -> None:
    write_fake_release(tmp_path, "11.26.0rc1", "11.26.0rc1")
    assert check_release_artifacts(tmp_path, "11.26.0rc1") == ["package.json says 11.26.0rc1, expected 11.26.0-rc.1"]


@pytest.mark.parametrize("tag", ["v11.26.0rc1", "v11.26", "11.26.0-rc.1"])
def test_check_reports_tag_mismatch(tmp_path: Path, tag: str) -> None:
    write_fake_release(tmp_path, "11.26.0rc1", "11.26.0-rc.1")
    problems = check_release_artifacts(tmp_path, "11.26.0rc1", tag=tag)
    assert len(problems) == 1
    assert f"tag {tag} does not match" in problems[0]
    assert "expected v11.26.0-rc.1" in problems[0]


def test_check_reports_missing_file_without_crashing(tmp_path: Path) -> None:
    write_fake_release(tmp_path, "11.26.0", "11.26.0")
    (tmp_path / "nmdc_schema/nmdc.schema.json").unlink()
    problems = check_release_artifacts(tmp_path, "11.26.0")
    assert len(problems) == 1
    assert problems[0].startswith("nmdc_schema/nmdc.schema.json: could not read version")


@pytest.mark.parametrize("version", ["11.26.0.dev0", "11.26"])
def test_check_reports_unsupported_version(tmp_path: Path, version: str) -> None:
    write_fake_release(tmp_path, version, version)
    problems = check_release_artifacts(tmp_path, version)
    assert len(problems) == 1
    assert "X.Y.Z or X.Y.ZrcN" in problems[0]


@pytest.mark.parametrize("relative", VERSIONED_ARTIFACTS)
def test_read_artifact_version_reads_real_files(relative: str) -> None:
    # The committed files say 0.0.0 before the first `make release`, and the release
    # version afterward. Either way, each parser must find a version string.
    assert read_artifact_version(REPO_ROOT / relative)


def test_repo_root_is_the_repository() -> None:
    assert release_module.REPO_ROOT == REPO_ROOT


def test_check_artifacts_command(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    fake_repo = tmp_path / "repo"
    write_fake_release(fake_repo, "11.26.0rc1", "11.26.0-rc.1")
    monkeypatch.setattr(release_module, "REPO_ROOT", fake_repo)
    monkeypatch.chdir(tmp_path)  # the working directory must not matter
    passing = CliRunner().invoke(cli, ["check-artifacts", "--version", "11.26.0rc1", "--tag", "v11.26.0-rc.1"])
    assert passing.exit_code == 0
    assert "carry 11.26.0rc1, matching v11.26.0-rc.1" in passing.stdout
    failing = CliRunner().invoke(cli, ["check-artifacts", "--version", "11.26.0rc1", "--tag", "v11.26.0rc1"])
    assert failing.exit_code == 1
    assert "tag v11.26.0rc1 does not match" in failing.stderr


def test_bump_command_rejects_unsupported_component() -> None:
    result = CliRunner().invoke(cli, ["bump", "--bump", "minor", "--bump", "alpha"])
    assert result.exit_code == 2
    assert "'alpha' is not one of" in result.stderr


def test_bump_command_reports_release_errors(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    result = CliRunner().invoke(cli, ["bump"])
    assert result.exit_code == 1
    assert "BUMP is empty" in result.stderr


def sh(repo: Path, *command: str) -> None:
    subprocess.run(command, cwd=repo, check=True, capture_output=True, text=True)


@pytest.fixture
def git_identity(monkeypatch: pytest.MonkeyPatch) -> None:
    """Make git usable in temp repos regardless of the developer's own config."""
    for name, value in {
        "GIT_AUTHOR_NAME": "Test",
        "GIT_AUTHOR_EMAIL": "test@example.org",
        "GIT_COMMITTER_NAME": "Test",
        "GIT_COMMITTER_EMAIL": "test@example.org",
        "GIT_CONFIG_GLOBAL": os.devnull,
        "GIT_CONFIG_NOSYSTEM": "1",
    }.items():
        monkeypatch.setenv(name, value)


@pytest.fixture
def clone(tmp_path: Path, git_identity: None) -> Path:
    """A clone of a bare 'origin', with one commit on main pushed."""
    origin = tmp_path / "origin.git"
    work = tmp_path / "work"
    sh(tmp_path, "git", "init", "--bare", "--initial-branch=main", str(origin))
    sh(tmp_path, "git", "clone", str(origin), str(work))
    sh(work, "git", "symbolic-ref", "HEAD", "refs/heads/main")
    (work / "README.md").write_text("demo\n")
    sh(work, "git", "add", "README.md")
    sh(work, "git", "commit", "-m", "start")
    sh(work, "git", "push", "-u", "origin", "main")
    return work


def test_preconditions_pass_on_clean_main(clone: Path) -> None:
    assert check_preconditions(clone, "v11.26.0") == []


def test_preconditions_reject_other_branch(clone: Path) -> None:
    sh(clone, "git", "switch", "-c", "feature")
    assert check_preconditions(clone, "v11.26.0") == ["You are on 'feature'; releases are made from main."]


def test_preconditions_reject_uncommitted_changes(clone: Path) -> None:
    (clone / "README.md").write_text("changed\n")
    (clone / "untracked.txt").write_text("fine\n")
    assert check_preconditions(clone, "v11.26.0") == [
        "Tracked files have uncommitted changes; commit or discard them first."
    ]


def test_preconditions_reject_unpushed_commit(clone: Path) -> None:
    sh(clone, "git", "commit", "--allow-empty", "-m", "local only")
    assert check_preconditions(clone, "v11.26.0") == ["Local main is not level with origin/main; pull or push first."]


def test_preconditions_reject_existing_local_tag(clone: Path) -> None:
    sh(clone, "git", "tag", "v11.26.0")
    assert check_preconditions(clone, "v11.26.0") == ["Tag v11.26.0 already exists locally."]


def test_preconditions_reject_existing_remote_tag(clone: Path) -> None:
    sh(clone, "git", "tag", "v11.26.0")
    sh(clone, "git", "push", "origin", "v11.26.0")
    sh(clone, "git", "tag", "-d", "v11.26.0")
    assert check_preconditions(clone, "v11.26.0") == ["Tag v11.26.0 already exists on origin."]


@pytest.fixture
def uv_project(tmp_path: Path) -> Path:
    (tmp_path / "pyproject.toml").write_text('[project]\nname = "demo"\nversion = "11.25.0"\nrequires-python = ">=3.10"\n')
    return tmp_path


def test_next_project_version(uv_project: Path) -> None:
    assert current_project_version(uv_project) == "11.25.0"
    assert next_project_version(uv_project, ["minor", "rc"]) == "11.26.0rc1"
    assert next_project_version(uv_project, ["patch"]) == "11.25.1"
    # A dry run must not write anything.
    assert current_project_version(uv_project) == "11.25.0"


def test_next_project_version_reports_uv_refusal(uv_project: Path) -> None:
    with pytest.raises(ReleaseError, match="didn't increase the version"):
        next_project_version(uv_project, ["rc"])


def test_gh_is_authenticated_without_gh(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("PATH", str(tmp_path))
    assert gh_is_authenticated(tmp_path) is False


@pytest.mark.parametrize(
    ("typed", "expected"),
    [("y\n", True), ("yes\n", True), (" YES \n", True), ("\n", False), ("n\n", False), ("", False)],
)
def test_confirm_release(typed: str, expected: bool) -> None:
    # An empty string means no input at all (EOF), as when stdin isn't a terminal.
    runner = CliRunner()
    with runner.isolation(input=typed) as (stdout, _stderr, _output):
        assert confirm_release("11.25.0", "11.26.0rc1", "v11.26.0-rc.1") is expected
    if typed:  # CliRunner only echoes the prompt when it reads input
        assert "Release 11.25.0 -> 11.26.0rc1 as v11.26.0-rc.1? [y/N]" in stdout.getvalue().decode()


def test_confirm_release_asks_again_after_unclear_reply() -> None:
    runner = CliRunner()
    with runner.isolation(input="sure\ny\n"):
        assert confirm_release("11.25.0", "11.26.0rc1", "v11.26.0-rc.1") is True


def test_set_package_json_version_keeps_other_keys(tmp_path: Path) -> None:
    (tmp_path / "package.json").write_text('{\n  "name": "nmdc-schema",\n  "version": "11.25.0",\n  "private": true\n}\n')
    set_package_json_version(tmp_path, "11.26.0-rc.1")
    assert (tmp_path / "package.json").read_text() == (
        '{\n  "name": "nmdc-schema",\n  "version": "11.26.0-rc.1",\n  "private": true\n}\n'
    )


def test_unexpected_release_changes() -> None:
    assert unexpected_release_changes(sorted(RELEASE_COMMIT_FILES)) == []
    assert unexpected_release_changes(["pyproject.toml", "src/docs/index.md", "src/schema/core.yaml"]) == [
        "src/docs/index.md",
        "src/schema/core.yaml",
    ]


def test_fetch_origin_main_ignores_conflicting_local_tag(clone: Path, tmp_path: Path) -> None:
    # An admin's clone can hold a stale copy of an old tag that origin has since moved.
    sh(clone, "git", "tag", "v1.0.0")
    sh(clone, "git", "push", "origin", "v1.0.0")
    other = tmp_path / "other"
    sh(tmp_path, "git", "clone", str(tmp_path / "origin.git"), str(other))
    sh(other, "git", "commit", "--allow-empty", "-m", "moved")
    sh(other, "git", "tag", "-f", "v1.0.0")
    sh(other, "git", "push", "origin", "main", "--force", "v1.0.0")
    fetch_origin_main(clone)
    assert subprocess.run(
        ["git", "rev-parse", "origin/main"], cwd=clone, capture_output=True, text=True, check=True
    ).stdout == subprocess.run(["git", "rev-parse", "HEAD"], cwd=other, capture_output=True, text=True, check=True).stdout


def test_fetch_origin_main_reports_unreachable_origin(clone: Path, tmp_path: Path) -> None:
    sh(clone, "git", "remote", "set-url", "origin", str(tmp_path / "missing.git"))
    with pytest.raises(ReleaseError, match="Could not fetch main from origin"):
        fetch_origin_main(clone)


LOCK = 'version = 1\nrevision = 5\n\n[[package]]\nname = "nmdc-schema"\nversion = "11.25.0"\nsource = {{ editable = "." }}\n'


@pytest.fixture
def locked_clone(clone: Path) -> Path:
    (clone / "uv.lock").write_text(LOCK.format())
    sh(clone, "git", "add", "uv.lock")
    sh(clone, "git", "commit", "-m", "lock")
    return clone


def test_check_lock_change_accepts_version_only(locked_clone: Path) -> None:
    (locked_clone / "uv.lock").write_text(LOCK.format().replace('"11.25.0"', '"11.26.0rc1"'))
    assert check_lock_change(locked_clone) is None


def test_check_lock_change_rejects_older_uv_rewrite(locked_clone: Path) -> None:
    rewritten = LOCK.format().replace('"11.25.0"', '"11.26.0rc1"').replace("revision = 5", "revision = 3")
    (locked_clone / "uv.lock").write_text(rewritten)
    message = check_lock_change(locked_clone)
    assert message is not None
    assert "uv.lock changed beyond the project version" in message
    assert "uv self update" in message


def test_command_failure_includes_tool_message() -> None:
    error = subprocess.CalledProcessError(2, ["uv", "version", "--bump", "minor"], stderr="error: network down\n")
    assert command_failure(error) == "`uv version --bump minor` failed:\nerror: network down"


def test_command_failure_without_captured_output() -> None:
    error = subprocess.CalledProcessError(2, ["make", "all"])
    assert command_failure(error) == "`make all` failed."


def test_commit_and_tag_reports_tag_failure_after_commit(clone: Path) -> None:
    # e.g. tag signing fails after commit signing worked; here the tag name is already taken.
    sh(clone, "git", "tag", "v11.26.0")
    (clone / "README.md").write_text("release\n")
    with pytest.raises(ReleaseError, match="release commit was made, but creating tag v11.26.0 failed") as raised:
        commit_and_tag(clone, ["README.md"], "v11.26.0")
    assert "already exists" in str(raised.value)


def test_commit_and_tag_reports_commit_failure(clone: Path) -> None:
    with pytest.raises(ReleaseError, match="Creating the release commit failed. Nothing was committed."):
        commit_and_tag(clone, ["no-such-file.txt"], "v11.26.0")


def test_commit_and_tag(clone: Path) -> None:
    (clone / "README.md").write_text("release\n")
    commit_and_tag(clone, ["README.md"], "v11.26.0")
    log = subprocess.run(["git", "log", "-1", "--format=%s %D"], cwd=clone, capture_output=True, text=True, check=True)
    assert log.stdout.startswith("Release v11.26.0 ")
    assert "tag: v11.26.0" in log.stdout


def test_untracked_artifacts(clone: Path) -> None:
    (clone / "nmdc_schema").mkdir()
    (clone / "nmdc_schema" / "new_artifact.json").write_text("{}")
    (clone / "elsewhere.txt").write_text("not an artifact")
    assert untracked_artifacts(clone) == ["nmdc_schema/new_artifact.json"]


def test_gh_is_authenticated_checks_github_com_only(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    # `gh auth status` fails when any configured host has a bad token; only github.com matters.
    fake_gh = tmp_path / "gh"
    fake_gh.write_text('#!/bin/sh\n[ "$*" = "auth status --hostname github.com" ]\n')
    fake_gh.chmod(0o755)
    monkeypatch.setenv("PATH", str(tmp_path))
    assert gh_is_authenticated(tmp_path) is True
