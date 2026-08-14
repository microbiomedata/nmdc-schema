"""Guard against reintroducing `slot_usage` that restates an inherited value.

A ratchet, not a snapshot. It asserts the count does not grow, so a new redundant
assertion fails here rather than accumulating unnoticed. The exhaustive check that
a removal changed no meaning is `src/scripts/dump_induced_slots.py`, run before and
after and diffed; that one needs a baseline and so does not belong in the suite.
"""

from linkml_runtime import SchemaView

from src.scripts.report_redundant_slot_usage import find_redundancies

SCHEMA_FILE = "src/schema/nmdc.yaml"

# `PropertyAssertion.has_unit` asserts `required: false` over a baseline that is unset
# rather than asserted. It restates the default, so the report flags it, but it is kept
# on purpose: it documents the conditional requirement its description spells out, and
# it becomes a genuine relaxation rather than a restatement if `AttributeValue` ever
# requires `has_unit`. Removing it would be a silent loss of that marker.
EXPECTED = {("PropertyAssertion", "has_unit", "required")}


def test_no_unexpected_redundant_slot_usage():
    findings = find_redundancies(SchemaView(SCHEMA_FILE))
    actual = {(f.class_name, f.slot_name, f.metaslot) for f in findings}
    unexpected = actual - EXPECTED
    assert not unexpected, (
        f"{len(unexpected)} slot_usage assertion(s) restate a value the class already "
        f"inherits: {sorted(unexpected)}. Remove them, or add to EXPECTED with a reason. "
        f"See src/scripts/report_redundant_slot_usage.py."
    )


def test_expected_exception_is_still_present():
    """If this fails, EXPECTED is stale and should shrink rather than be ignored."""
    findings = find_redundancies(SchemaView(SCHEMA_FILE))
    actual = {(f.class_name, f.slot_name, f.metaslot) for f in findings}
    assert EXPECTED <= actual, (
        f"EXPECTED no longer occurs and should be pruned: {EXPECTED - actual}"
    )
