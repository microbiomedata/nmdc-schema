"""Tests for src/scripts/report_asset_usage.py.

Builds a small git repository under ``tmp_path`` (``git add``-ed, not committed;
``git ls-files`` reads the index) so the detector's real path is exercised end to
end, rather than mocking ``tracked_assets``.
"""

import subprocess

import pytest

from src.scripts.report_asset_usage import (
    GENERIC_BASENAMES,
    ROOT_EXCLUDED_DIRS,
    _emit_text,
    _emit_tsv,
    find_asset_findings,
)

DEPRECATED_SCHEMA = """
classes: {}
slots:
  old_slot: {}
enums: {}
types: {}
subsets: {}
"""


def _write(path, text=""):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


@pytest.fixture
def repo(tmp_path):
    """A minimal git repo with a handful of tracked assets and one consumer file."""
    _write(tmp_path / "src/schema/deprecated.yaml", DEPRECATED_SCHEMA)

    # Referenced by full path.
    _write(tmp_path / "assets/misc/referenced.tsv", "data\n")
    _write(tmp_path / "Makefile", "target: assets/misc/referenced.tsv\n\techo built\n")

    # Referenced only by a distinctive bare filename (the Makefile-builds-a-path case).
    _write(tmp_path / "assets/misc/distinctive_name.tsv", "data\n")
    _write(tmp_path / "scripts/build.sh", "cat $DIR/distinctive_name.tsv\n")

    # A generic basename that collides with something unrelated; must not count.
    _write(tmp_path / "assets/one/README.md", "one\n")
    _write(tmp_path / "assets/two/README.md", "two\n")
    _write(tmp_path / "unrelated/README.md", "not about either asset\n")

    # Names a deprecated element, and nothing references it.
    _write(tmp_path / "assets/misc/old_mapping.tsv", "old_slot\tsomething\n")

    # Authored docs under src/docs/ must stay searchable (the root-`docs/`-only fix).
    _write(tmp_path / "assets/misc/documented.tsv", "data\n")
    _write(
        tmp_path / "src/docs/notes.md",
        "See assets/misc/documented.tsv for details.\n",
    )

    # A generated root docs/ tree must stay excluded even though it mentions a path.
    _write(
        tmp_path / "docs/generated.md",
        "See assets/misc/only_in_generated_docs.tsv.\n",
    )
    _write(tmp_path / "assets/misc/only_in_generated_docs.tsv", "data\n")

    # A duplicate basename that isn't in GENERIC_BASENAMES: the dynamic uniqueness
    # check, not the hardcoded denylist, must be what catches this.
    _write(tmp_path / "assets/a/data.csv", "a\n")
    _write(tmp_path / "assets/b/data.csv", "b\n")
    _write(tmp_path / "scripts/loads_data.py", "open('data.csv')\n")

    # An untracked asset naming another tracked asset by full path must not count:
    # only committed content is a consumer.
    _write(tmp_path / "assets/misc/only_named_untracked.tsv", "data\n")

    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    subprocess.run(["git", "add", "-A"], cwd=tmp_path, check=True)

    _write(
        tmp_path / "untracked_notes.md",
        "See assets/misc/only_named_untracked.tsv for context.\n",
    )
    return tmp_path


def _find(findings, path):
    matches = [f for f in findings if f.path == path]
    assert len(matches) == 1, f"expected exactly one finding for {path}"
    return matches[0]


def test_full_path_reference_is_found(repo):
    finding = _find(find_asset_findings(repo), "assets/misc/referenced.tsv")
    assert not finding.is_unreferenced
    assert "Makefile" in finding.referenced_by


def test_distinctive_basename_fallback_is_found(repo):
    finding = _find(find_asset_findings(repo), "assets/misc/distinctive_name.tsv")
    assert not finding.is_unreferenced
    assert "scripts/build.sh" in finding.referenced_by


def test_generic_basename_does_not_count_as_a_reference(repo):
    """A same-named unrelated file must not make README.md assets look consumed."""
    findings = find_asset_findings(repo)
    one = _find(findings, "assets/one/README.md")
    two = _find(findings, "assets/two/README.md")
    assert one.is_unreferenced
    assert two.is_unreferenced


def test_duplicate_basename_not_in_denylist_is_caught_dynamically(repo):
    """Two tracked assets sharing a basename must not trust the bare-name fallback,
    even though neither name is in GENERIC_BASENAMES."""
    findings = find_asset_findings(repo)
    a = _find(findings, "assets/a/data.csv")
    b = _find(findings, "assets/b/data.csv")
    assert a.is_unreferenced
    assert b.is_unreferenced


def test_untracked_file_is_not_a_consumer(repo):
    """Only committed content counts; an untracked file naming an asset must not."""
    finding = _find(find_asset_findings(repo), "assets/misc/only_named_untracked.tsv")
    assert finding.is_unreferenced


def test_deprecated_element_is_detected(repo):
    finding = _find(find_asset_findings(repo), "assets/misc/old_mapping.tsv")
    assert finding.is_unreferenced
    assert finding.deprecated_elements == ("old_slot",)


def test_authored_docs_under_src_docs_are_searched(repo):
    """src/docs/ is authored content, not the generated docs/ tree; must be searched."""
    finding = _find(find_asset_findings(repo), "assets/misc/documented.tsv")
    assert not finding.is_unreferenced
    assert "src/docs/notes.md" in finding.referenced_by


def test_generated_root_docs_tree_is_excluded(repo):
    """The generated root docs/ tree must not count as a reference source."""
    finding = _find(find_asset_findings(repo), "assets/misc/only_in_generated_docs.tsv")
    assert finding.is_unreferenced


def test_generic_basenames_are_a_real_collision_set(repo):
    """Guards GENERIC_BASENAMES against silently going stale or empty."""
    assert "README.md" in GENERIC_BASENAMES
    assert "docs" in ROOT_EXCLUDED_DIRS


def test_emit_text_lists_every_unreferenced_and_deprecated_asset(repo, capsys):
    findings = find_asset_findings(repo)
    _emit_text(findings)
    out = capsys.readouterr().out
    assert "assets/one/README.md" in out
    assert "old_slot" in out
    assert "assets/misc/referenced.tsv" not in out.split("Referenced nowhere")[1].split(
        "Naming an element"
    )[0]


def test_emit_tsv_has_one_row_per_asset_and_a_header(repo, capsys):
    findings = find_asset_findings(repo)
    _emit_tsv(findings)
    lines = capsys.readouterr().out.strip().split("\n")
    assert lines[0] == "asset\treferenced_by\tdeprecated_elements_named"
    assert len(lines) == 1 + len(findings)
