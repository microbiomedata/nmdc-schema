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

PINNED_FILES = [
    *sorted((ROOT / ".github" / "workflows").glob("*.y*ml")),
    ROOT / "Dockerfile",
    ROOT / "DEVELOPMENT.md",
    ROOT / "CLAUDE.md",
]


class TestPoetryVersionPins(unittest.TestCase):

    def test_poetry_pins_agree(self):
        versions = {}
        for path in PINNED_FILES:
            for version in PIN.findall(path.read_text()):
                versions.setdefault(version, []).append(str(path.relative_to(ROOT)))
        self.assertTrue(versions, "found no poetry==X.Y.Z pins; did the install commands change?")
        self.assertEqual(
            len(versions), 1, f"poetry is pinned to more than one version: {versions}"
        )
