"""Check that every MIxS customization changes a slot that exists.

A yq update such as `.slots.foo.range |= "Protocol"` creates `foo` if no imported slot has
that name, which leaves an empty stub slot in src/schema/mixs.yaml. That happened to
`internal_standard` after it was dropped from the import list
(https://github.com/microbiomedata/nmdc-schema/issues/3500).
"""

import csv
import re

from tests import ROOT

IMPORT_LIST = ROOT / "assets" / "import_mixs_slots_regardless.tsv"
CUSTOMIZATIONS = ROOT / "assets" / "yq-for-mixs-customizations.txt"

SLOT_REFERENCE = re.compile(r"\.slots\.([A-Za-z0-9_]+)")
RENAME = re.compile(r"^'\.slots\.([A-Za-z0-9_]+) = \.slots\.[A-Za-z0-9_]+")


def active_lines() -> list[str]:
    """Return the customization lines the MIxS pipeline runs: those starting with a single quote."""
    return [
        line.rstrip("\n")
        for line in CUSTOMIZATIONS.read_text().splitlines()
        if line.startswith("'")
    ]


def known_slots() -> set[str]:
    """Return slots that exist when the customizations run: imported, or created by a rename.

    Files in assets/other_mixs_yaml_files/ other than the mixs_template.yaml recipient model are
    injected after the customizations run (makefiles/mixs.Makefile), so their slots don't count.
    The recipient model defines no slots.
    """
    with IMPORT_LIST.open() as fh:
        known = {row["slot"] for row in csv.DictReader(fh, delimiter="\t")}
    for line in active_lines():
        match = RENAME.match(line)
        if match:
            known.add(match.group(1))
    return known


def test_customizations_only_change_known_slots() -> None:
    known = known_slots()
    unknown = sorted(
        {name for line in active_lines() for name in SLOT_REFERENCE.findall(line)}
        - known
    )
    assert unknown == [], (
        f"These customizations target slots nothing imports: {unknown}"
    )


def test_slot_reference_finds_update_and_delete_targets() -> None:
    assert SLOT_REFERENCE.findall(
        "'.slots.internal_standard.range |= \"Protocol\"'"
    ) == ["internal_standard"]
    assert SLOT_REFERENCE.findall("'del(.slots.ph.structured_pattern)'") == ["ph"]
    assert RENAME.match(
        "'.slots.samp_collec_device = .slots.samp_collect_device | del(.slots.samp_collect_device)'"
    )
