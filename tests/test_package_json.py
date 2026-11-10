"""Checks on package.json, which lets npm install the JSON artifacts from a release tag."""

import json
from pathlib import Path

from src.scripts.release import current_project_version, pep440_to_semver

REPO_ROOT = Path(__file__).resolve().parents[1]
PACKAGE = json.loads((REPO_ROOT / "package.json").read_text(encoding="utf-8"))


def test_package_is_private_and_has_no_scripts() -> None:
    # npm runs `prepare` on git dependencies, which would try to build this Python repo.
    assert PACKAGE["name"] == "nmdc-schema"
    assert PACKAGE["private"] is True
    assert "scripts" not in PACKAGE


def test_exports_point_at_packaged_files() -> None:
    for subpath, target in PACKAGE["exports"].items():
        assert subpath.startswith("./") and target.startswith("./")
        assert (REPO_ROOT / target).is_file(), target
        if target != "./package.json":
            assert target.removeprefix("./") in PACKAGE["files"], target


def test_version_matches_pyproject() -> None:
    assert PACKAGE["version"] == pep440_to_semver(current_project_version(REPO_ROOT))


def test_no_package_lock() -> None:
    assert not (REPO_ROOT / "package-lock.json").exists()
