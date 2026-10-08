"""Check the method_for annotations that say which slot each method slot describes.

See https://github.com/microbiomedata/nmdc-schema/issues/3481.
"""

import re

from linkml_runtime import SchemaView

from tests import SCHEMA_FILE

METHOD_SLOT_NAME = re.compile(r"_(meth|method|methods|protocol)$")

# Method slots that describe a process or a sample as a whole, not how one other slot's
# value was measured, so they have no method_for annotation.
PROCESS_METHOD_SLOTS = {
    "add_recov_method",
    "dna_isolate_meth",
    "dna_lr_isolate_meth",
    "filter_method",
    "heat_sys_deliv_meth",
    "internal_standard_method",
    "rna_isolate_meth",
    "samp_collec_method",
    "samp_sort_meth",
    "separation_method",
    "seq_meth",
}


def method_for_pairs(view: SchemaView) -> dict[str, str]:
    """Return each slot with a method_for annotation and the slot it names."""
    pairs = {}
    for name, slot in view.all_slots().items():
        if slot.annotations and "method_for" in slot.annotations:
            pairs[name] = slot.annotations["method_for"].value
    return pairs


def test_method_for_names_a_slot_that_exists():
    view = SchemaView(SCHEMA_FILE)
    missing = {
        m: t for m, t in method_for_pairs(view).items() if t not in view.all_slots()
    }
    assert missing == {}


def test_every_method_slot_is_paired_or_listed_as_a_process():
    view = SchemaView(SCHEMA_FILE)
    pairs = method_for_pairs(view)
    unpaired = sorted(
        name
        for name in view.all_slots()
        if METHOD_SLOT_NAME.search(name)
        and name not in pairs
        and name not in PROCESS_METHOD_SLOTS
    )
    assert unpaired == [], (
        f"Add a method_for annotation or list these in PROCESS_METHOD_SLOTS: {unpaired}"
    )


def test_process_method_slots_have_no_method_for():
    view = SchemaView(SCHEMA_FILE)
    assert sorted(set(method_for_pairs(view)) & PROCESS_METHOD_SLOTS) == []


def test_every_class_with_a_method_slot_also_has_the_slot_it_describes():
    view = SchemaView(SCHEMA_FILE)
    problems = []
    for method, target in method_for_pairs(view).items():
        for class_name in view.all_classes():
            slots = view.class_slots(class_name)
            if method in slots and target not in slots:
                problems.append(f"{class_name}: {method} without {target}")
    assert problems == []
