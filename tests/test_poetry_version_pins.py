"""Keep every pinned poetry version in the repository the same.

The poetry.lock content-hash depends on the poetry version, so CI, the Docker
image and the developer instructions have to install the same one. GitHub
Actions can't share one value across workflow files without a repository
variable, and Dependabot doesn't update versions written inside ``run:`` steps,
so this test is what keeps the copies from drifting apart. To change the
version, update every file listed in the failure message together. See
https://github.com/microbiomedata/nmdc-schema/issues/3460
"""

import re
import unittest

from tests import ROOT

PIN = re.compile(r"poetry==(\d+\.\d+\.\d+)")

WORKFLOWS = ROOT / ".github" / "workflows"

# Files that install or document poetry and so must each carry a pin. Removing a
# pin from one of these should fail the test, not leave that install unpinned.
EXPECTED_PIN_FILES = [
    WORKFLOWS / "check-links.yaml",
    WORKFLOWS / "deploy-docs.yaml",
    WORKFLOWS / "lint.yaml",
    WORKFLOWS / "main.yaml",
    WORKFLOWS / "pypi-publish.yaml",
    WORKFLOWS / "schema-pattern-lint.yml",
    WORKFLOWS / "test-pages-build.yaml",
    ROOT / "Dockerfile",
    ROOT / "DEVELOPMENT.md",
    ROOT / "CLAUDE.md",
]

# Also scan every workflow, so a pin added to a new workflow is checked too.
SCANNED_FILES = sorted(set(EXPECTED_PIN_FILES) | set(WORKFLOWS.glob("*.y*ml")))


class TestPoetryVersionPins(unittest.TestCase):

    def test_expected_files_are_pinned(self):
        unpinned = [
            str(path.relative_to(ROOT))
            for path in EXPECTED_PIN_FILES
            if not PIN.search(path.read_text())
        ]
        self.assertEqual(unpinned, [], f"no poetry==X.Y.Z pin found in: {unpinned}")

    def test_poetry_pins_agree(self):
        versions = {}
        for path in SCANNED_FILES:
            for version in PIN.findall(path.read_text()):
                versions.setdefault(version, []).append(str(path.relative_to(ROOT)))
        self.assertTrue(versions, "found no poetry==X.Y.Z pins; did the install commands change?")
        self.assertEqual(
            len(versions), 1, f"poetry is pinned to more than one version: {versions}"
        )
