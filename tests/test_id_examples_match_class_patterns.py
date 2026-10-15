"""Every example on a class's id slot must match that class's id pattern.

linkml 1.12 copies slot examples into the generated JSON Schema, so an example on the base
id slot appears on every class. See https://github.com/microbiomedata/nmdc-schema/issues/3540.
"""

import re
from pathlib import Path

import pytest
from linkml_runtime import SchemaView

SCHEMA = Path(__file__).resolve().parent.parent / "src" / "schema" / "nmdc.yaml"


def _id_examples():
    sv = SchemaView(str(SCHEMA))
    for class_name in sorted(sv.all_classes()):
        if "id" not in sv.class_slots(class_name):
            continue
        slot = sv.induced_slot("id", class_name)
        for example in slot.examples or []:
            yield class_name, slot.pattern, example.value


ID_EXAMPLES = list(_id_examples())


def test_some_id_example_is_checked():
    # Guards against the parametrized test below passing because it collected nothing.
    assert ID_EXAMPLES


@pytest.mark.parametrize("class_name,pattern,value", ID_EXAMPLES)
def test_id_example_matches_class_pattern(class_name, pattern, value):
    assert pattern, f"{class_name}.id has an example but no pattern"
    assert re.search(pattern, value), f"{class_name}.id example {value!r} fails {pattern!r}"
