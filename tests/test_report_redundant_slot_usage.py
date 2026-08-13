"""Tests for src/scripts/report_redundant_slot_usage.py."""

from dataclasses import fields

from linkml_runtime import SchemaView
from linkml_runtime.linkml_model.meta import SlotDefinition

from src.scripts.report_redundant_slot_usage import (
    UNSET_MEANS_FALSE_METASLOTS,
    find_redundancies,
    format_tsv,
    summarize_value,
)

# Two global slots, and classes exercising the cases the report must tell apart.
# On `status`, which is globally required: Parent restates the global value, Child
# restates what Parent already says, Refiner narrows the range, and Relaxer drops
# the requirement. On `note`, which is globally unset: ExplicitFalse writes the
# false it already inherits. Redundant: Parent, Child, ExplicitFalse.
SCHEMA_YAML = """
id: https://example.org/test
name: test-schema
prefixes:
  linkml: https://w3id.org/linkml/
  test: https://example.org/test/
default_prefix: test
default_range: string
imports:
  - linkml:types
slots:
  status:
    range: string
    required: true
    description: A status.
  note:
    range: string
    description: A note, with `required` left unset so it defaults to false.
classes:
  Parent:
    slots:
      - status
    slot_usage:
      status:
        required: true
  Child:
    is_a: Parent
    slot_usage:
      status:
        required: true
  Refiner:
    is_a: Parent
    slot_usage:
      status:
        range: integer
  Relaxer:
    is_a: Parent
    slot_usage:
      status:
        required: false
  ExplicitFalse:
    slots:
      - note
    slot_usage:
      note:
        required: false
  Untouched:
    slots:
      - status
"""


def build_view(tmp_path) -> SchemaView:
    schema_file = tmp_path / "schema.yaml"
    schema_file.write_text(SCHEMA_YAML)
    return SchemaView(str(schema_file))


def test_flags_usage_restating_the_global_slot(tmp_path):
    """Parent asserts required: true, which the global slot already says."""
    findings = find_redundancies(build_view(tmp_path))
    parent = [f for f in findings if f.class_name == "Parent"]
    assert len(parent) == 1
    assert parent[0].slot_name == "status"
    assert parent[0].metaslot == "required"
    assert parent[0].baseline == "global slot"


def test_flags_usage_restating_an_inherited_value(tmp_path):
    """Child asserts required: true, which it already inherits from Parent."""
    findings = find_redundancies(build_view(tmp_path))
    child = [f for f in findings if f.class_name == "Child"]
    assert len(child) == 1
    assert child[0].metaslot == "required"
    assert child[0].baseline == "is_a Parent"


def test_does_not_flag_a_genuine_refinement(tmp_path):
    """Refiner narrows the range, so nothing about it is redundant."""
    findings = find_redundancies(build_view(tmp_path))
    assert [f for f in findings if f.class_name == "Refiner"] == []


def test_flags_required_false_over_an_unset_baseline(tmp_path):
    """ExplicitFalse writes required: false on a slot that is already optional.

    The baseline reads as None because LinkML has nothing to inherit, but unset
    means false, so the assertion leaves the induced slot unchanged.
    """
    findings = find_redundancies(build_view(tmp_path))
    explicit = [f for f in findings if f.class_name == "ExplicitFalse"]
    assert len(explicit) == 1
    assert explicit[0].slot_name == "note"
    assert explicit[0].metaslot == "required"
    assert explicit[0].value is False
    assert explicit[0].baseline == "global slot, unset so false"


def test_does_not_flag_dropping_an_inherited_requirement(tmp_path):
    """Relaxer sets required: false where Parent says true, which is a refinement."""
    findings = find_redundancies(build_view(tmp_path))
    assert [f for f in findings if f.class_name == "Relaxer"] == []


def test_unset_means_false_metaslots_are_real_booleans():
    """Guards the hand-maintained list against typos and metamodel renames."""
    boolean_metaslots = {
        f.name for f in fields(SlotDefinition) if "bool" in str(f.type)
    }
    assert UNSET_MEANS_FALSE_METASLOTS <= boolean_metaslots
    assert not UNSET_MEANS_FALSE_METASLOTS & {"inlined", "inlined_as_list"}


def test_ignores_classes_without_slot_usage(tmp_path):
    findings = find_redundancies(build_view(tmp_path))
    assert [f for f in findings if f.class_name == "Untouched"] == []


def test_tsv_rows_are_single_line_and_well_formed(tmp_path):
    """Multi-line reprs must not break the column count."""
    findings = find_redundancies(build_view(tmp_path))
    lines = format_tsv(findings).strip().split("\n")
    assert lines[0] == "class\tslot\tmetaslot\tvalue\tbaseline"
    for line in lines:
        assert len(line.split("\t")) == 5


class MultiLineRepr:
    """Stands in for LinkML objects such as Example, whose repr spans lines."""

    def __repr__(self) -> str:
        return "Example({\n  'a': 1,\n\t'b': 2\n})"


def test_summarize_value_collapses_real_newlines_and_tabs():
    """Object reprs carry genuine newlines and tabs, which would corrupt the TSV."""
    summarized = summarize_value(MultiLineRepr())
    assert "\n" not in summarized
    assert "\t" not in summarized
    assert summarized == "Example({ 'a': 1, 'b': 2 })"


def test_summarize_value_truncates():
    long_value = "x" * 300
    assert len(summarize_value(long_value)) == 100
    assert summarize_value(long_value).endswith("...")
