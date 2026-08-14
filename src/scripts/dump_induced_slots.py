"""Dump every induced slot value in the schema, for diffing across a refactor.

A change that claims not to alter the schema's meaning can be checked by running
this before and after and diffing. An empty diff proves no induced slot moved,
for every class and every slot at once.

This is not the same check as diffing `nmdc_schema/nmdc_materialized_patterns.yaml`.
That artifact is built with `--no-materialize-attributes`, so it does not expand
per-class induced slots, and a change to an inherited `required` or `range` does not
show up in it. This does expand them, which is why it was the gate used when removing
redundant `slot_usage` assertions (see `report_redundant_slot_usage.py`).

Usage:

    poetry run python src/scripts/dump_induced_slots.py > before.tsv
    # make the change
    poetry run python src/scripts/dump_induced_slots.py > after.tsv
    diff before.tsv after.tsv

Output is one row per class, slot, and populated metaslot, sorted so the diff is
stable. Roughly 18k rows for the current schema; it runs in about a second.
"""

from dataclasses import fields

import click
from linkml_runtime import SchemaView
from linkml_runtime.linkml_model.meta import SlotDefinition

# Recorded by the loader from where an element was read, so they say nothing about
# meaning and would add noise to a diff of the same schema at two commits.
PROVENANCE_METASLOTS = frozenset(
    {"from_schema", "imported_from", "source_file", "owner"}
)


def dump(schema_view: SchemaView) -> list[str]:
    """Every populated metaslot of every induced slot, as sorted TSV rows."""
    metaslots = sorted(
        f.name for f in fields(SlotDefinition) if f.name not in PROVENANCE_METASLOTS
    )
    rows: list[str] = []
    for class_name in sorted(schema_view.all_classes()):
        for slot_name in sorted(schema_view.class_slots(class_name)):
            try:
                induced = schema_view.induced_slot(slot_name, class_name)
            except (ValueError, KeyError) as error:
                rows.append(
                    f"{class_name}\t{slot_name}\t<ERROR>\t{type(error).__name__}"
                )
                continue
            for metaslot in metaslots:
                value = getattr(induced, metaslot, None)
                if value is None or value == [] or value == {} or value == ():
                    continue
                # Collapse multi-line reprs so one value stays one row.
                rows.append(
                    f"{class_name}\t{slot_name}\t{metaslot}\t{' '.join(repr(value).split())}"
                )
    return rows


@click.command()
@click.option(
    "--schema-file",
    default="src/schema/nmdc.yaml",
    show_default=True,
    help="Path to the schema file.",
)
def main(schema_file: str) -> None:
    """Dump every induced slot value, for diffing a refactor against its baseline."""
    click.echo("\n".join(dump(SchemaView(schema_file))))


if __name__ == "__main__":
    main()
