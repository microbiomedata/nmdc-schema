import click
import glob
import os
import sys
import yaml
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Optional

from linkml_runtime import SchemaView
from linkml_runtime.loaders import yaml_loader
from nmdc_schema.nmdc import Database

DATABASE_CLASS_NAME = "Database"


@dataclass(frozen=True, order=True)
class Reference:
    """A schema-derived reference from a source field to a target collection."""

    source_collection_name: str = field()
    source_class_name: str = field()
    source_field_name: str = field()
    target_collection_name: str = field()
    target_class_name: str = field()


@dataclass
class Violation:
    """A referential integrity violation: a reference to a nonexistent target."""

    source_collection_name: str
    source_class_name: str
    source_id: str
    source_field_name: str
    target_id: str
    allowed_target_collections: list[str]


def get_collection_names_from_schema(schema_view: SchemaView) -> list[str]:
    """Returns names of Database slots that represent collections (multivalued + inlined_as_list)."""
    collection_names = []
    for slot_name in schema_view.class_slots(DATABASE_CLASS_NAME):
        slot_definition = schema_view.induced_slot(slot_name, DATABASE_CLASS_NAME)
        if slot_definition.multivalued and slot_definition.inlined_as_list:
            collection_names.append(slot_name)
    return sorted(set(collection_names))


def get_names_of_classes_in_effective_range_of_slot(
    schema_view: SchemaView, slot_definition
) -> list[str]:
    """
    Determine the slot's effective range, taking into account any_of constraints.

    Replicates refscan/lib/helpers.py logic for resolving effective range.
    """
    names = []
    if "any_of" in slot_definition and len(slot_definition.any_of) > 0:
        for slot_expression in slot_definition.any_of:
            if slot_expression.range in schema_view.all_classes():
                names.extend(schema_view.class_descendants(slot_expression.range))
    else:
        if slot_definition.range in schema_view.all_classes():
            names.extend(schema_view.class_descendants(slot_definition.range))
    return list(set(names))


def get_collection_name_to_class_names_map(
    schema_view: SchemaView,
) -> dict[str, list[str]]:
    """Map each collection name to the class names whose instances can be stored in it."""
    mapping = {}
    for collection_name in get_collection_names_from_schema(schema_view):
        slot_definition = schema_view.induced_slot(collection_name, DATABASE_CLASS_NAME)
        class_names = get_names_of_classes_in_effective_range_of_slot(
            schema_view, slot_definition
        )
        mapping[collection_name] = class_names
    return mapping


def identify_references(
    schema_view: SchemaView,
    collection_name_to_class_names: dict[str, list[str]],
) -> list[Reference]:
    """
    Identify all inter-document references allowed by the schema.

    Replicates refscan/lib/helpers.py identify_references() logic.
    """
    references = []
    for collection_name, class_names in sorted(collection_name_to_class_names.items()):
        for class_name in class_names:
            for slot_name in schema_view.class_slots(class_name):
                slot_definition = schema_view.induced_slot(
                    slot_name=slot_name, class_name=class_name
                )
                eligible_target_classes = (
                    get_names_of_classes_in_effective_range_of_slot(
                        schema_view, slot_definition
                    )
                )
                for target_class in eligible_target_classes:
                    for (
                        target_collection,
                        classes_in_collection,
                    ) in collection_name_to_class_names.items():
                        if target_class in classes_in_collection:
                            ref = Reference(
                                source_collection_name=collection_name,
                                source_class_name=class_name,
                                source_field_name=slot_name,
                                target_collection_name=target_collection,
                                target_class_name=target_class,
                            )
                            references.append(ref)
    return references


def translate_class_uri_into_schema_class_name(
    schema_view: SchemaView, class_uri: str
) -> Optional[str]:
    """Convert a class_uri (e.g., 'nmdc:Biosample') to a schema class name (e.g., 'Biosample')."""
    for class_name, class_definition in schema_view.all_classes().items():
        if class_definition.class_uri == class_uri:
            return class_definition.name
    return None


def build_reference_lookup(
    references: list[Reference],
) -> dict[tuple[str, str, str], set[str]]:
    """
    Build a lookup: (source_collection, source_class, source_field) -> {target_collection_names}
    """
    lookup = defaultdict(set)
    for ref in references:
        key = (ref.source_collection_name, ref.source_class_name, ref.source_field_name)
        lookup[key].add(ref.target_collection_name)
    return dict(lookup)


def get_reference_fields_for_item(
    refs_by_collection: dict[str, list[tuple[str, str, set[str]]]],
    collection_name: str,
    item_class_name: str,
    schema_view: SchemaView,
) -> dict[str, set[str]]:
    """
    For a given item in a collection, determine which fields are reference slots
    and what target collections are allowed for each.

    Returns: dict[field_name, set[target_collection_names]]
    """
    field_targets = defaultdict(set)
    for src_cls, src_fld, allowed_targets in refs_by_collection.get(collection_name, []):
        if src_cls == item_class_name or item_class_name in schema_view.class_descendants(
            src_cls
        ):
            field_targets[src_fld].update(allowed_targets)
    return dict(field_targets)


def load_database_files(
    directory_path: str, schema_view: SchemaView
) -> Database:
    """Load and merge all Database-*.yaml files from directory into a single Database object."""
    database_slots = schema_view.class_induced_slots(DATABASE_CLASS_NAME)
    database_slot_names = sorted(slot.name for slot in database_slots)

    file_paths = sorted(glob.glob(os.path.join(directory_path, "Database-*.yaml")))
    interleaved_path = os.path.abspath(
        os.path.join(directory_path, "Database-interleaved.yaml")
    )
    file_paths = [
        f for f in file_paths if os.path.abspath(f) != interleaved_path
    ]

    collector = Database()
    seen_ids = defaultdict(set)

    for file in file_paths:
        click.echo(f"Loading: {file}", err=True)
        with open(file, "r") as f:
            data = yaml.safe_load(f)
        database = yaml_loader.load(data, Database)
        for slot in database_slot_names:
            payload = getattr(database, slot)
            if payload:
                if slot not in collector.__dict__:
                    collector.__dict__[slot] = []
                for item in payload:
                    if hasattr(item, "id") and item.id:
                        if item.id in seen_ids[slot]:
                            continue
                        seen_ids[slot].add(item.id)
                    collector.__dict__[slot].append(item)

    return collector


def load_single_file(input_file: str, schema_view: SchemaView) -> Database:
    """Load a single Database YAML file."""
    database_slot_names = sorted(
        slot.name for slot in schema_view.class_induced_slots(DATABASE_CLASS_NAME)
    )

    click.echo(f"Loading: {input_file}", err=True)
    with open(input_file, "r") as f:
        data = yaml.safe_load(f)
    database = yaml_loader.load(data, Database)

    collector = Database()
    for slot in database_slot_names:
        payload = getattr(database, slot)
        if payload:
            collector.__dict__[slot] = payload
    return collector


@click.command()
@click.option(
    "--directory-path",
    default="src/data/valid",
    help="Path to directory containing Database-*.yaml files.",
)
@click.option(
    "--input-file",
    default=None,
    help="Path to a single interleaved Database YAML file (overrides --directory-path).",
)
@click.option(
    "--schema-file",
    default="src/schema/nmdc.yaml",
    help="Schema file path.",
)
@click.option("--tsv", is_flag=True, help="Output violations in TSV format.")
def check_references(directory_path, input_file, schema_file, tsv):
    """Check referential integrity of YAML example data files against the NMDC schema."""

    # Phase A: Load data
    schema_view = SchemaView(schema_file)

    if input_file:
        collector = load_single_file(input_file, schema_view)
    else:
        collector = load_database_files(directory_path, schema_view)

    # Phase B: Build schema references catalog
    click.echo("\nAnalyzing schema for reference relationships...", err=True)
    collection_name_to_class_names = get_collection_name_to_class_names_map(schema_view)
    collection_names = get_collection_names_from_schema(schema_view)
    references = identify_references(schema_view, collection_name_to_class_names)
    ref_lookup = build_reference_lookup(references)

    # Pre-group references by collection for efficient lookup
    refs_by_collection: dict[str, list[tuple[str, str, set[str]]]] = defaultdict(list)
    for (src_coll, src_cls, src_fld), allowed_targets in ref_lookup.items():
        refs_by_collection[src_coll].append((src_cls, src_fld, allowed_targets))

    click.echo(
        f"Found {len(collection_names)} collections and "
        f"{len(references)} reference relationships.",
        err=True,
    )

    # Phase C: Build ID index
    id_to_collections: dict[str, set[str]] = {}
    for collection_name in collection_names:
        items = getattr(collector, collection_name) or []
        for item in items:
            if hasattr(item, "id") and item.id:
                id_to_collections.setdefault(item.id, set()).add(collection_name)

    click.echo(
        f"Indexed {len(id_to_collections)} unique IDs across all collections.\n",
        err=True,
    )

    # Phase D: Scan for violations
    violations = []
    for collection_name in collection_names:
        items = getattr(collector, collection_name) or []
        for item in items:
            # Determine class name from the loaded Python object
            item_class_name = type(item).__name__

            # Also try via type field -> class_uri mapping
            if hasattr(item, "type") and isinstance(item.type, str):
                mapped = translate_class_uri_into_schema_class_name(
                    schema_view, item.type
                )
                if mapped:
                    item_class_name = mapped

            item_id = getattr(item, "id", None) or "<no-id>"

            # Get reference fields for this item's class
            field_targets = get_reference_fields_for_item(
                refs_by_collection, collection_name, item_class_name, schema_view
            )

            for field_name, allowed_targets in field_targets.items():
                value = getattr(item, field_name, None)
                if value is None:
                    continue

                # Handle both single and multivalued slots
                if isinstance(value, list):
                    target_ids = [v for v in value if isinstance(v, str)]
                elif isinstance(value, str):
                    target_ids = [value]
                else:
                    continue

                for target_id in target_ids:
                    # Check if target_id exists in any of the allowed target collections
                    if target_id in id_to_collections:
                        if id_to_collections[target_id] & allowed_targets:
                            continue
                    violations.append(
                        Violation(
                            source_collection_name=collection_name,
                            source_class_name=item_class_name,
                            source_id=item_id,
                            source_field_name=field_name,
                            target_id=target_id,
                            allowed_target_collections=sorted(allowed_targets),
                        )
                    )

    # Output
    if tsv:
        if violations:
            click.echo(
                "source_collection\tsource_class\tsource_id\t"
                "source_field\ttarget_id\tallowed_target_collections"
            )
            for v in violations:
                click.echo(
                    f"{v.source_collection_name}\t{v.source_class_name}\t"
                    f"{v.source_id}\t{v.source_field_name}\t{v.target_id}\t"
                    f"{','.join(v.allowed_target_collections)}"
                )
    else:
        if violations:
            click.echo(
                f"Found {len(violations)} referential integrity violation(s):\n",
                err=True,
            )
            for v in violations:
                click.echo(
                    f"VIOLATION: {v.source_collection_name}/{v.source_id}"
                    f".{v.source_field_name} -> {v.target_id} "
                    f"(not found in {{{', '.join(v.allowed_target_collections)}}})"
                )
        else:
            click.echo("No referential integrity violations found.", err=True)

    sys.exit(1 if violations else 0)


if __name__ == "__main__":
    check_references()
