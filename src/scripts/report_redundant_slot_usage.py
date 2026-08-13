"""Report `slot_usage` assertions that restate a value the class already inherits.

A `slot_usage` is meant to refine a slot for one class. When it asserts a value
the class would inherit anyway, it adds nothing: the induced slot is the same
either way. Those assertions still cost maintenance, because a later change
upstream silently stops reaching every class that restated the old value.

The comparison is against what the class actually inherits, which is the parent's
induced slot when the class has a parent, and the global slot definition
otherwise. That distinction matters: a `slot_usage` restoring the global value
after a parent narrowed it is a real refinement, not a redundancy.

This script reports them. It does not edit the schema, because some restatements
are deliberate (see the note on re-declaring `range: uriorcurie` in
`src/docs/maintaining-the-schema.md`), so a human decides what to remove.

Usage:

    poetry run python src/scripts/report_redundant_slot_usage.py \
        --schema-file src/schema/nmdc.yaml

    # machine-readable, for diffing between releases
    poetry run python src/scripts/report_redundant_slot_usage.py \
        --schema-file src/schema/nmdc.yaml --output-format tsv

Or via make:

    make assets/redundant-slot-usage.txt
"""

from dataclasses import fields
from typing import Any, List, NamedTuple, Optional

import click
from linkml_runtime import SchemaView
from linkml_runtime.linkml_model.meta import SlotDefinition
from linkml_runtime.utils.schemaview import OrderedBy

# Populated by the loader or carried as bookkeeping rather than authored in the
# `slot_usage` block, so a match on these says nothing about redundancy.
IGNORED_METASLOTS = frozenset(
    {
        "name",
        "alias",
        "domain_of",
        "from_schema",
        "imported_from",
        "is_usage_slot",
        "owner",
        "usage_slot_name",
        "definition_uri",
        "slot_uri",
    }
)

# Boolean metaslots whose unset state means false, so `metaslot: false` in a
# `slot_usage` block restates what the class already inherits even though the
# baseline reads as None. `inlined` and `inlined_as_list` are deliberately absent:
# their effective value depends on whether the range class has an identifier
# (see `SchemaView.is_inlined`), so unset there does not simply mean false.
UNSET_MEANS_FALSE_METASLOTS = frozenset(
    {
        "abstract",
        "asymmetric",
        "children_are_mutually_disjoint",
        "designates_type",
        "id_prefixes_are_closed",
        "identifier",
        "inherited",
        "irreflexive",
        "is_class_field",
        "is_grouping_slot",
        "key",
        "list_elements_ordered",
        "list_elements_unique",
        "locally_reflexive",
        "mixin",
        "multivalued",
        "recommended",
        "reflexive",
        "required",
        "shared",
        "symmetric",
        "transitive",
    }
)


class Redundancy(NamedTuple):
    """One `slot_usage` metaslot assertion that matches the value it would inherit."""

    class_name: str
    slot_name: str
    metaslot: str
    value: Any
    baseline: str


def inherited_slot(
    schema_view: SchemaView, class_definition: Any, slot_name: str
) -> tuple[Optional[SlotDefinition], str]:
    """The slot as this class would see it without its own `slot_usage`.

    For a class with a parent, that is the parent's induced slot, which already
    folds in any refinement the parent made. Comparing against the global slot
    instead would wrongly flag a `slot_usage` that restores the global value
    after a parent narrowed it, which is one of the cases this report exists to
    tell apart.

    Returns the baseline definition and a label naming where it came from.
    """
    parent_name = class_definition.is_a
    if parent_name:
        try:
            return schema_view.induced_slot(
                slot_name, parent_name
            ), f"is_a {parent_name}"
        except (ValueError, KeyError):
            pass
    return schema_view.get_slot(slot_name), "global slot"


def is_empty(value: Any) -> bool:
    """True when a metaslot holds no authored value.

    LinkML populates unset metaslots with None or an empty collection, so those
    cannot be distinguished from "not written in the YAML" and are skipped.
    """
    return value is None or value == [] or value == {} or value == ()


def baseline_value_and_label(
    baseline_slot: SlotDefinition, baseline_label: str, metaslot: str
) -> tuple[Any, str]:
    """The inherited value to compare against, with unset booleans resolved.

    Most unset metaslots have to be skipped, because LinkML cannot tell "absent
    from the YAML" from "written as null". The boolean metaslots in
    `UNSET_MEANS_FALSE_METASLOTS` are the exception: unset means false there, so
    a class writing `required: false` over an unset baseline restates a value it
    already has. The label records that the baseline was unset rather than
    asserted, since the two read very differently to someone deciding what to cut.
    """
    value = getattr(baseline_slot, metaslot, None)
    if value is None and metaslot in UNSET_MEANS_FALSE_METASLOTS:
        return False, f"{baseline_label}, unset so false"
    return value, baseline_label


def find_redundancies(schema_view: SchemaView) -> List[Redundancy]:
    """Return every `slot_usage` assertion that restates an inherited value."""
    redundancies: List[Redundancy] = []
    metaslot_names = [f.name for f in fields(SlotDefinition)]

    for class_name, class_definition in schema_view.all_classes(
        ordered_by=OrderedBy.LEXICAL
    ).items():
        if not class_definition.slot_usage:
            continue

        for slot_name, usage in class_definition.slot_usage.items():
            baseline_slot, baseline_label = inherited_slot(
                schema_view, class_definition, slot_name
            )
            if baseline_slot is None:
                # An attribute rather than a schema-level slot; nothing is inherited,
                # so nothing can be redundant with it.
                continue

            for metaslot in metaslot_names:
                if metaslot in IGNORED_METASLOTS:
                    continue

                usage_value = getattr(usage, metaslot, None)
                if is_empty(usage_value):
                    continue

                baseline_value, label = baseline_value_and_label(
                    baseline_slot, baseline_label, metaslot
                )
                if is_empty(baseline_value):
                    continue

                if usage_value == baseline_value:
                    redundancies.append(
                        Redundancy(class_name, slot_name, metaslot, usage_value, label)
                    )

    return redundancies


def summarize_value(value: Any, max_length: int = 100) -> str:
    """Render a metaslot value on one line, short enough to scan.

    Values such as `examples` and `structured_pattern` repr across several lines,
    which would corrupt the TSV and swamp the text report.
    """
    text = " ".join(repr(value).split())
    if len(text) > max_length:
        text = text[: max_length - 3] + "..."
    return text


def format_text(redundancies: List[Redundancy]) -> str:
    """Render findings grouped by class, for a human reader."""
    if not redundancies:
        return "No redundant slot_usage assertions found.\n"

    lines: List[str] = [
        f"{len(redundancies)} redundant slot_usage assertion(s). Each restates a value "
        "the class already inherits, so removing it would not change the induced slot.\n"
    ]
    current_class = None
    for item in sorted(redundancies):
        if item.class_name != current_class:
            current_class = item.class_name
            lines.append(f"\n{current_class}:")
        lines.append(
            f"  {item.slot_name}.{item.metaslot} = {summarize_value(item.value)}"
            f"   [same as {item.baseline}]"
        )
    return "\n".join(lines) + "\n"


def format_tsv(redundancies: List[Redundancy]) -> str:
    """Render findings as TSV, for diffing between releases."""
    lines = ["class\tslot\tmetaslot\tvalue\tbaseline"]
    for item in sorted(redundancies):
        lines.append(
            f"{item.class_name}\t{item.slot_name}\t{item.metaslot}"
            f"\t{summarize_value(item.value)}\t{item.baseline}"
        )
    return "\n".join(lines) + "\n"


@click.command()
@click.option(
    "--schema-file",
    default="src/schema/nmdc.yaml",
    show_default=True,
    help="Path to the schema file.",
)
@click.option(
    "--output-format",
    type=click.Choice(["text", "tsv"]),
    default="text",
    show_default=True,
    help="Report format.",
)
def main(schema_file: str, output_format: str) -> None:
    """Report slot_usage assertions that restate a value the class already inherits.

    The baseline is the parent's induced slot when the class has a parent, and the
    global slot definition otherwise. Each finding names which one it matched.
    """
    schema_view = SchemaView(schema_file)
    redundancies = find_redundancies(schema_view)
    renderer = format_tsv if output_format == "tsv" else format_text
    click.echo(renderer(redundancies), nl=False)


if __name__ == "__main__":
    main()
