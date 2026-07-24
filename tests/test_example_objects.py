"""Validate every structured ``examples: - object:`` in the schema against its slot's range class.

LinkML lets a slot carry example instances two ways: a scalar ``value:`` (a string) or a
structured ``object:`` (a nested instance of the slot's range class). This module checks the
``object:`` form. It walks the induced slots of every class (via ``SchemaView.class_induced_slots``,
so inherited slots, inline attributes, and ``slot_usage`` overrides are all covered, not only the
top-level slot definitions) and, for each object example, asserts three things:

1. The object validates against its slot's range class in closed mode (no unexpected properties,
   all required slots present).
2. The object asserts its class with ``type`` whenever the range class defines a ``type``
   designator slot. Wrapper classes such as ``QuantityValue`` require this, and asserting it keeps
   the examples faithful to how real instances are written.
3. The object carries ``has_raw_value`` whenever the range class defines that slot, so the example
   models the raw-plus-normalized shape that the attribute-value classes are built around.

Validation runs against ``src/schema/nmdc.yaml`` rather than the generated materialized artifact so
the check is independent of the build state.
"""

import json

import pytest
from jsonasobj2 import as_dict
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml_runtime import SchemaView

from tests import ROOT

SOURCE_SCHEMA = ROOT / "src" / "schema" / "nmdc.yaml"


@pytest.fixture(scope="module")
def schema_view():
    return SchemaView(str(SOURCE_SCHEMA))


@pytest.fixture(scope="module")
def object_validator():
    return Validator(
        str(SOURCE_SCHEMA),
        validation_plugins=[JsonschemaValidationPlugin(closed=True)],
    )


def _induced_slot_names(schema_view, class_name):
    """Names of every slot induced on ``class_name``; empty set if the class is unknown."""
    try:
        return {slot.name for slot in schema_view.class_induced_slots(class_name)}
    except (ValueError, KeyError):
        return set()


def _collect_object_examples(schema_view):
    """Yield ``(location, range_class, object_dict)`` for each ``examples: - object:`` in the schema.

    ``location`` is a human-readable ``ClassName.slot_name`` label for failure messages. Duplicate
    ``(range_class, object)`` pairs are collapsed so the same wrapper example reused across many
    slots is only reported once.
    """
    all_classes = set(schema_view.all_classes())
    seen = set()
    for class_name in sorted(all_classes):
        for slot in schema_view.class_induced_slots(class_name):
            for example in slot.examples or []:
                raw_object = getattr(example, "object", None)
                if raw_object is None:
                    continue
                object_dict = as_dict(raw_object)
                range_class = slot.range
                dedup_key = (range_class, json.dumps(object_dict, sort_keys=True, default=str))
                if dedup_key in seen:
                    continue
                seen.add(dedup_key)
                location = f"{class_name}.{slot.name}"
                yield location, range_class, object_dict


def test_object_examples_are_valid(schema_view, object_validator):
    """Every ``examples: - object:`` must validate against its range class and follow raw/type rules."""
    all_classes = set(schema_view.all_classes())
    failures = []

    for location, range_class, object_dict in _collect_object_examples(schema_view):
        if range_class not in all_classes:
            failures.append(
                f"{location}: object example given but slot range '{range_class}' is not a class"
            )
            continue

        range_slots = _induced_slot_names(schema_view, range_class)

        if "type" in range_slots and "type" not in object_dict:
            failures.append(
                f"{location}: {range_class} defines a 'type' designator but the example object "
                f"does not assert it"
            )

        if "has_raw_value" in range_slots and "has_raw_value" not in object_dict:
            failures.append(
                f"{location}: {range_class} defines 'has_raw_value' but the example object "
                f"omits it"
            )

        report = object_validator.validate(object_dict, target_class=range_class)
        for result in report.results:
            failures.append(f"{location}: invalid against {range_class}: {result.message}")

    assert not failures, "Object example problems:\n" + "\n".join(sorted(failures))


def test_example_form_matches_range(schema_view):
    """Each example must use the form its slot's range demands: ``object:`` XOR ``value:``.

    A slot whose range is an inlined class without an identifier is a *wrapper* slot: its
    instances are structured objects (``QuantityValue``, ``TextValue``, ``PropertyAssertion``,
    ...), so an example must be given as an ``object:``. Every other slot (scalar type, enum, or a
    class referenced by identifier) carries a plain scalar, so an example must be a ``value:``.
    ``SchemaView.is_inlined`` is exactly this predicate: it is true only for inlined,
    identifier-less class ranges. Slots without examples are unconstrained; examples are optional.

    This enforces the dichotomy with no tolerated exceptions: every wrapper example is an object
    and every non-wrapper example is a scalar.
    """
    all_classes = set(schema_view.all_classes())
    failures = []

    for class_name in sorted(all_classes):
        for slot in schema_view.class_induced_slots(class_name):
            examples = slot.examples or []
            if not examples:
                continue
            is_wrapper = slot.range in all_classes and schema_view.is_inlined(slot)
            for example in examples:
                has_object = getattr(example, "object", None) is not None
                has_value = getattr(example, "value", None) is not None
                location = f"{class_name}.{slot.name}"
                if is_wrapper and not has_object:
                    failures.append(
                        f"{location}: range '{slot.range}' is an inlined wrapper class, so the "
                        f"example must use 'object:', not 'value:'"
                    )
                elif not is_wrapper and not has_value:
                    failures.append(
                        f"{location}: range '{slot.range}' is scalar/enum/referenced, so the "
                        f"example must use 'value:', not 'object:'"
                    )

    assert not failures, "Example form mismatches:\n" + "\n".join(sorted(set(failures)))
