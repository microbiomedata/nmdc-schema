"""Detect constraints declared on slots whose range makes them unreachable.

A slot declaring `pattern` or `minimum_value` on a class-ranged slot has its
constraint silently ignored by JsonschemaValidationPlugin — `pattern` only
applies to strings, and `minimum_value` only to numbers, but the slot value is
an object. Verified empirically in issue #3007.

This test is report-only: it prints a violation table and always passes.
Scope: top-level slot definitions in the materialized schema only
       (not per-class slot_usage overrides).

See: https://github.com/microbiomedata/nmdc-schema/issues/3009
Fast-fail follow-on: https://github.com/microbiomedata/nmdc-schema/issues/3010
"""
import unittest
from collections import defaultdict

from linkml_runtime import SchemaView

from tests import SCHEMA_FILE

_STRING_CONSTRAINTS = frozenset(
    [
        "pattern",
        "structured_pattern",
        "equals_string",
        "equals_string_in",
        "string_serialization",
    ]
)
_NUMERIC_CONSTRAINTS = frozenset(
    [
        "minimum_value",
        "maximum_value",
        "equals_number",
    ]
)
_ENUM_CONSTRAINTS = frozenset(["permissible_values"])
_ALL_CHECKED = _STRING_CONSTRAINTS | _NUMERIC_CONSTRAINTS | _ENUM_CONSTRAINTS

# LinkML built-in type names whose ultimate ancestor is string-compatible.
# Derived user types (e.g. decimal_degree, external_identifier) are handled
# by walking the type_ancestors chain.
_STRING_BASE_TYPES = frozenset(
    [
        "string",
        "uriorcurie",
        "anyuri",
        "curie",
        "ncname",
        "date",
        "datetime",
        "time",
        "dateOrDatetime",
    ]
)
_NUMERIC_BASE_TYPES = frozenset(["integer", "float", "double", "decimal"])


def _range_kind(sv: SchemaView, range_name: str) -> str:
    """Classify a range name as 'string', 'numeric', 'boolean', 'enum', or 'class'."""
    if sv.get_class(range_name) is not None:
        return "class"
    if sv.get_enum(range_name) is not None:
        return "enum"
    if sv.get_type(range_name) is not None:
        ancestors = set(sv.type_ancestors(range_name))
        if ancestors & _NUMERIC_BASE_TYPES:
            return "numeric"
        if "boolean" in ancestors:
            return "boolean"
        if ancestors & _STRING_BASE_TYPES:
            return "string"
        return "string"  # fallback for derived types not in the explicit list
    return "unknown"


class TestSlotConstraintRangeCompatibility(unittest.TestCase):
    """Report constraints that are incompatible with their slot's range.

    Always passes — report-only mode until triage is complete (#3009).
    """

    def test_report_incompatible_constraints(self) -> None:
        sv = SchemaView(str(SCHEMA_FILE))

        violations: list[dict] = []
        for slot_name, slot_def in sv.schema.slots.items():
            range_name = slot_def.range
            if range_name is None:
                continue
            kind = _range_kind(sv, range_name)

            for constraint in _ALL_CHECKED:
                val = getattr(slot_def, constraint, None)
                if val is None or (isinstance(val, (list, dict)) and len(val) == 0):
                    continue
                compatible = (
                    (constraint in _STRING_CONSTRAINTS and kind == "string")
                    or (constraint in _NUMERIC_CONSTRAINTS and kind == "numeric")
                    or (constraint in _ENUM_CONSTRAINTS and kind == "enum")
                )
                if not compatible:
                    violations.append(
                        {
                            "slot": slot_name,
                            "range": range_name,
                            "range_kind": kind,
                            "constraint": constraint,
                        }
                    )

        if violations:
            by_group: dict[tuple, list[str]] = defaultdict(list)
            for v in violations:
                by_group[(v["range_kind"], v["range"], v["constraint"])].append(
                    v["slot"]
                )

            print(f"\n{'=' * 72}")
            print(f"SLOT CONSTRAINT / RANGE INCOMPATIBILITIES  ({len(violations)} total)")
            print(f"{'=' * 72}")
            print(f"{'Range kind':<12} {'Range':<36} {'Constraint':<26} Count")
            print("-" * 90)
            for (kind, rng, constraint), slots in sorted(by_group.items()):
                print(f"{kind:<12} {rng:<36} {constraint:<26} {len(slots)}")
            print(f"{'=' * 72}")
            print("report-only mode — see #3009 for context, #3010 for fast-fail follow-on")
