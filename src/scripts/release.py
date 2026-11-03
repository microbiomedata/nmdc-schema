"""Release tooling for nmdc-schema.

    uv run python src/scripts/release.py bump --bump minor --bump rc
    uv run python src/scripts/release.py bump --bump stable --no-push
    uv run python src/scripts/release.py check-artifacts --tag v11.26.0-rc.1

`make release BUMP='minor rc'` calls the `bump` subcommand, and the publish
workflow calls `check-artifacts`. The version lives in pyproject.toml; every
other version string (tag, package.json, schema files) is derived from it.
"""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

import click
import yaml

# This file lives at src/scripts/release.py.
REPO_ROOT = Path(__file__).resolve().parents[2]

ALLOWED_BUMP_COMPONENTS = ("major", "minor", "patch", "rc", "stable")

# The only version shapes a release may have: X.Y.Z and X.Y.ZrcN (PEP 440).
RELEASE_VERSION_PATTERN = re.compile(r"^(?P<release>\d+\.\d+\.\d+)(?:rc(?P<rc>\d+))?$")

MIGRATORS_DIR = "nmdc_schema/migrators"

# Generated files that record the schema version.
VERSIONED_ARTIFACTS = (
    "nmdc_schema/nmdc.py",
    "nmdc_schema/nmdc_pydantic.py",
    "nmdc_schema/nmdc.schema.json",
    "nmdc_schema/nmdc_materialized_patterns.schema.json",
    "nmdc_schema/nmdc_materialized_patterns.json",
    "nmdc_schema/nmdc_materialized_patterns.yaml",
)

# The generated Python modules record the version as a top-level assignment.
PYTHON_VERSION_LINE = re.compile(r'^version = "(?P<version>[^"]*)"$', re.MULTILINE)

SCHEMA_SOURCE = "src/schema/nmdc.yaml"

# Every tracked file a release commit may change.
RELEASE_COMMIT_FILES = frozenset(
    VERSIONED_ARTIFACTS
    + (
        "nmdc_schema/gold-to-mixs.sssom.tsv",
        "package.json",
        "pyproject.toml",
        "uv.lock",
    )
)


class ReleaseError(Exception):
    """A release step failed. The message says what went wrong."""


def parse_release_version(version: str) -> re.Match[str]:
    """Match a release version, or raise ValueError for any other shape.

    >>> parse_release_version("11.26.0rc1")["release"]
    '11.26.0'
    """
    match = RELEASE_VERSION_PATTERN.match(version)
    if match is None:
        raise ValueError(f"{version!r} is not X.Y.Z or X.Y.ZrcN, the only version shapes a release may have")
    return match


def pep440_to_semver(version: str) -> str:
    """Convert a release version to the form used in tags and package.json.

    >>> pep440_to_semver("11.26.0rc1")
    '11.26.0-rc.1'
    >>> pep440_to_semver("11.26.0")
    '11.26.0'
    """
    match = parse_release_version(version)
    rc_number = match["rc"]
    return match["release"] if rc_number is None else f"{match['release']}-rc.{rc_number}"


def tag_for_version(version: str) -> str:
    """Return the git tag for a release version.

    >>> tag_for_version("11.26.0rc1")
    'v11.26.0-rc.1'
    """
    return "v" + pep440_to_semver(version)


def is_prerelease(version: str) -> bool:
    """Return True for a release candidate such as 11.26.0rc1."""
    return parse_release_version(version)["rc"] is not None


def validate_bump_components(components: list[str]) -> None:
    """Raise ReleaseError unless components is a non-empty list of supported `uv version --bump` values."""
    allowed = ", ".join(ALLOWED_BUMP_COMPONENTS)
    if not components:
        raise ReleaseError(f"BUMP is empty. Use one or more of: {allowed}. For example: BUMP='minor rc'.")
    unsupported = [component for component in components if component not in ALLOWED_BUMP_COMPONENTS]
    if unsupported:
        raise ReleaseError(f"Unsupported bump component(s): {', '.join(unsupported)}. Use one or more of: {allowed}.")


def migrator_glob(version: str) -> str:
    """Return the file-name pattern of migrators that reach this version's X.Y.Z.

    >>> migrator_glob("11.26.0rc2")
    'migrator_from_*_to_11_26_0.py'
    """
    release = parse_release_version(version)["release"]
    return f"migrator_from_*_to_{release.replace('.', '_')}.py"


def find_migrators(version: str, migrators_dir: Path) -> list[Path]:
    """Return the migrators in migrators_dir that reach this version (any rc suffix ignored)."""
    return sorted(migrators_dir.glob(migrator_glob(version)))


def read_artifact_version(path: Path) -> str:
    """Return the schema version recorded in a generated artifact."""
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".py":
        match = PYTHON_VERSION_LINE.search(text)
        if match is None:
            raise ValueError('no top-level `version = "..."` line')
        return match["version"]
    if path.suffix == ".json":
        return str(json.loads(text)["version"])
    if path.suffix == ".yaml":
        return str(yaml.safe_load(text)["version"])
    raise ValueError(f"no rule for reading the version from a {path.suffix} file")


def read_package_json_version(repo: Path) -> str:
    """Return the version in package.json."""
    return str(json.loads((repo / "package.json").read_text(encoding="utf-8"))["version"])


def check_release_artifacts(repo: Path, version: str, tag: str | None = None) -> list[str]:
    """Return every way the artifacts, package.json and tag disagree with version; empty means consistent."""
    try:
        semver = pep440_to_semver(version)
    except ValueError as error:
        return [str(error)]
    problems = []
    for relative in VERSIONED_ARTIFACTS:
        try:
            found = read_artifact_version(repo / relative)
        except (OSError, KeyError, ValueError, yaml.YAMLError) as error:
            problems.append(f"{relative}: could not read version ({error})")
            continue
        if found != version:
            problems.append(f"{relative} says {found}, expected {version}")
    try:
        package_version = read_package_json_version(repo)
    except (OSError, KeyError, ValueError) as error:
        problems.append(f"package.json: could not read version ({error})")
    else:
        if package_version != semver:
            problems.append(f"package.json says {package_version}, expected {semver}")
    if tag is not None and tag != f"v{semver}":
        problems.append(f"tag {tag} does not match pyproject.toml version {version} (expected v{semver})")
    return problems


def run(command: list[str], repo: Path, capture: bool = True) -> str:
    """Run a command in repo and return its stripped stdout ('' when not captured)."""
    result = subprocess.run(command, cwd=repo, check=True, text=True, capture_output=capture)
    return result.stdout.strip() if capture else ""


def command_failure(error: subprocess.CalledProcessError) -> str:
    """Describe a failed command, including its own error output when it was captured."""
    message = f"`{' '.join(str(part) for part in error.cmd)}` failed"
    stderr = (error.stderr or "").strip()
    return f"{message}:\n{stderr}" if stderr else f"{message}."


def current_project_version(repo: Path) -> str:
    """Return the version in pyproject.toml."""
    return run(["uv", "version", "--short"], repo)


def git(repo: Path, *args: str) -> str:
    """Run a git command in repo and return its stripped stdout."""
    return run(["git", *args], repo)


def fetch_origin_main(repo: Path) -> None:
    """Update origin/main. Tags aren't fetched: the tag checks ask origin directly, and a stale local
    copy of an old tag would make `git fetch --tags` fail."""
    try:
        git(repo, "fetch", "--no-tags", "origin", "main")
    except subprocess.CalledProcessError as error:
        raise ReleaseError(f"Could not fetch main from origin:\n{error.stderr.strip()}") from error


def bump_arguments(components: list[str]) -> list[str]:
    """Turn ['minor', 'rc'] into ['--bump', 'minor', '--bump', 'rc']."""
    return [argument for component in components for argument in ("--bump", component)]


def next_project_version(repo: Path, components: list[str]) -> str:
    """Return the version `uv version --bump` would produce, without writing anything."""
    try:
        return run(["uv", "version", *bump_arguments(components), "--dry-run", "--short", "--no-sync"], repo)
    except subprocess.CalledProcessError as error:
        raise ReleaseError(f"uv could not compute the next version: {error.stderr.strip()}") from error


def gh_is_authenticated(repo: Path) -> bool:
    """Return True if the GitHub CLI is installed and logged in."""
    try:
        result = subprocess.run(
            ["gh", "auth", "status", "--hostname", "github.com"], cwd=repo, capture_output=True, text=True
        )
    except FileNotFoundError:
        return False
    return result.returncode == 0


def check_preconditions(repo: Path, tag: str) -> list[str]:
    """Return every reason a release can't start from this checkout; empty means ready."""
    problems = []
    branch = git(repo, "rev-parse", "--abbrev-ref", "HEAD")
    if branch != "main":
        problems.append(f"You are on {branch!r}; releases are made from main.")
    if git(repo, "status", "--porcelain", "--untracked-files=no"):
        problems.append("Tracked files have uncommitted changes; commit or discard them first.")
    if git(repo, "rev-parse", "HEAD") != git(repo, "rev-parse", "origin/main"):
        problems.append("Local main is not level with origin/main; pull or push first.")
    if git(repo, "tag", "--list", tag):
        problems.append(f"Tag {tag} already exists locally.")
    if git(repo, "ls-remote", "--tags", "origin", f"refs/tags/{tag}"):
        problems.append(f"Tag {tag} already exists on origin.")
    return problems


def confirm_release(current: str, next_version: str, tag: str) -> bool:
    """Ask whether to go ahead. The default is no, and so is no input at all (e.g. stdin isn't a terminal)."""
    try:
        return click.confirm(f"Release {current} -> {next_version} as {tag}?", default=False)
    except click.Abort:
        return False


def check_lock_change(repo: Path) -> str | None:
    """Return a problem if uv.lock differs from HEAD by more than its one project-version line.

    An older uv than the one that last wrote the lock rewrites it in an older format.
    """
    numstat = git(repo, "diff", "--numstat", "HEAD", "--", "uv.lock")
    if numstat in ("", "1\t1\tuv.lock"):
        return None
    uv_version = run(["uv", "--version"], repo)
    return (
        "uv.lock changed beyond the project version, which usually means this uv "
        f"({uv_version}) is older than the one that last wrote the lock. "
        "Update it (`uv self update`) and try again."
    )


def set_package_json_version(repo: Path, semver: str) -> None:
    """Write semver into package.json, keeping key order and two-space indentation."""
    path = repo / "package.json"
    package = json.loads(path.read_text(encoding="utf-8"))
    package["version"] = semver
    path.write_text(json.dumps(package, indent=2) + "\n", encoding="utf-8")


def untracked_artifacts(repo: Path) -> list[str]:
    """Return files under nmdc_schema/ that git doesn't track and doesn't ignore.

    The publish workflow's diff can't see these, but the wheel would include them.
    """
    return git(repo, "ls-files", "--others", "--exclude-standard", "--", "nmdc_schema/").splitlines()


def commit_and_tag(repo: Path, changed: list[str], tag: str) -> None:
    """Commit changed as the release commit and add an annotated tag, saying exactly what exists on failure."""
    try:
        git(repo, "add", "--", *changed)
        git(repo, "commit", "-m", f"Release {tag}")
    except subprocess.CalledProcessError as error:
        raise ReleaseError(f"Creating the release commit failed. Nothing was committed.\n{command_failure(error)}") from error
    try:
        git(repo, "tag", "-a", tag, "-m", f"Release {tag}")
    except subprocess.CalledProcessError as error:
        raise ReleaseError(
            f"The release commit was made, but creating tag {tag} failed. Nothing was pushed.\n{command_failure(error)}"
        ) from error


def unexpected_release_changes(changed: list[str]) -> list[str]:
    """Return the changed paths a release commit must not contain."""
    return sorted(set(changed) - RELEASE_COMMIT_FILES)


def release(repo: Path, components: list[str], push: bool = True, assume_yes: bool = False) -> str:
    """Bump, build, check, commit, tag, push and create the GitHub release. Return the tag."""
    validate_bump_components(components)
    fetch_origin_main(repo)
    current = current_project_version(repo)
    next_version = next_project_version(repo, components)
    try:
        tag = tag_for_version(next_version)
    except ValueError as error:
        raise ReleaseError(str(error)) from error

    problems = check_preconditions(repo, tag)
    if push and not gh_is_authenticated(repo):
        problems.append("The GitHub CLI is not installed or not logged in; run `gh auth login` first.")
    if not find_migrators(next_version, repo / MIGRATORS_DIR):
        problems.append(
            f"No migrator matches {MIGRATORS_DIR}/{migrator_glob(next_version)}. Add one first (a no-op migrator is fine)."
        )
    if problems:
        raise ReleaseError(
            f"Not releasing {current} -> {next_version}:\n" + "\n".join(f"  - {problem}" for problem in problems)
        )
    if not assume_yes and not confirm_release(current, next_version, tag):
        raise ReleaseError("Not releasing. Nothing was changed.")

    try:
        run(["uv", "version", *bump_arguments(components), "--no-sync"], repo)
        lock_problem = check_lock_change(repo)
        if lock_problem:
            raise ReleaseError(f"{lock_problem} Nothing was committed.")
        set_package_json_version(repo, pep440_to_semver(next_version))
        run(["make", "set-version"], repo, capture=False)
        run(["make", "squeaky-clean", "all", "test"], repo, capture=False)
    except subprocess.CalledProcessError as error:
        raise ReleaseError(f"{command_failure(error)}\nNothing was committed.") from error
    problems = check_release_artifacts(repo, next_version)
    if problems:
        raise ReleaseError(
            "The build produced inconsistent versions. Nothing was committed.\n"
            + "\n".join(f"  - {problem}" for problem in problems)
        )

    try:
        git(repo, "checkout", "--", SCHEMA_SOURCE)
    except subprocess.CalledProcessError as error:
        raise ReleaseError(f"{command_failure(error)}\nNothing was committed.") from error
    changed = git(repo, "diff", "--name-only", "HEAD").splitlines()
    unexpected = unexpected_release_changes(changed) + untracked_artifacts(repo)
    if unexpected:
        raise ReleaseError(
            "The build changed or added files a release commit must not contain. Nothing was committed.\n"
            + "\n".join(f"  - {path}" for path in unexpected)
        )
    commit_and_tag(repo, changed, tag)

    if not push:
        click.echo(f"Committed and tagged {tag} locally. Nothing was pushed (--no-push).")
        return tag

    try:
        git(repo, "push", "--atomic", "origin", "main", tag)
    except subprocess.CalledProcessError as error:
        raise ReleaseError(
            f"The push was rejected, so nothing was pushed. The commit and tag {tag} exist only locally.\n"
            f"{error.stderr.strip()}"
        ) from error

    release_command = ["gh", "release", "create", tag, "--verify-tag", "--title", tag, "--generate-notes"]
    if is_prerelease(next_version):
        release_command.append("--prerelease")
    try:
        run(release_command, repo)
    except subprocess.CalledProcessError as error:
        raise ReleaseError(
            f"The commit and tag {tag} are pushed, but creating the GitHub release failed:\n"
            f"{error.stderr.strip()}\nCreate it with: {' '.join(release_command)}"
        ) from error
    click.echo(f"Released {tag}. The publish workflow is now running: gh run list --workflow pypi-publish.yaml")
    return tag


@click.group()
def cli() -> None:
    """Make nmdc-schema releases and check release artifacts."""


@cli.command()
@click.option(
    "--bump",
    "components",
    multiple=True,
    type=click.Choice(ALLOWED_BUMP_COMPONENTS),
    help="A `uv version --bump` component. Repeat for several, e.g. --bump minor --bump rc.",
)
@click.option("--no-push", is_flag=True, help="Stop after the local commit and tag.")
@click.option("--yes", is_flag=True, help="Don't ask for confirmation.")
def bump(components: tuple[str, ...], no_push: bool, yes: bool) -> None:
    """Make a release: bump the version, build, commit, tag, push and create the GitHub release."""
    try:
        release(REPO_ROOT, list(components), push=not no_push, assume_yes=yes)
    except ReleaseError as error:
        raise click.ClickException(str(error)) from error


@cli.command("check-artifacts")
@click.option("--version", help="Expected PEP 440 version. Defaults to the pyproject.toml version.")
@click.option("--tag", help="Also require this release tag to match the version.")
def check_artifacts(version: str | None, tag: str | None) -> None:
    """Check that the artifacts, package.json and (optionally) a tag agree on the version."""
    version = version or current_project_version(REPO_ROOT)
    problems = check_release_artifacts(REPO_ROOT, version, tag)
    if problems:
        raise click.ClickException(
            "Release artifacts are inconsistent:\n" + "\n".join(f"  - {problem}" for problem in problems)
        )
    click.echo(f"All versioned artifacts and package.json carry {version}" + (f", matching {tag}" if tag else ""))


if __name__ == "__main__":
    cli()
