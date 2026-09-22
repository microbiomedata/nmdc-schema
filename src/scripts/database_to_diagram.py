"""Validate an NMDC Database example and generate a Mermaid instance diagram.

The source LinkML schema determines collections, reference ranges, and embedded
objects. Rendering uses the repository's shared Mermaid-to-SVG Make rule.
"""

import argparse
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml_runtime import SchemaView
from nmdc_schema_validation_plugin import NmdcSchemaValidationPlugin
from refscan.lib.helpers import (
    get_collection_name_to_class_names_map,
    get_names_of_classes_in_effective_range_of_slot,
    translate_class_uri_into_schema_class_name,
)

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SCHEMA = ROOT / "src/schema/nmdc.yaml"
COLORS = {
    "sample": "#e5f2ec",
    "process": "#e7effa",
    "data": "#fff0d9",
    "manifest": "#f1e8fa",
    "ontology": "#f3f4f6",
    "record": "#eef0f4",
    "external": "#ffffff",
}


@dataclass
class Node:
    """A collection record, an identified embedded object, or an external ID."""

    record: dict
    class_name: str
    kind: str


class DiagramSchema:
    """Share source-schema interpretation and validation across example files."""

    def __init__(self, path: Path = DEFAULT_SCHEMA) -> None:
        self.view = SchemaView(str(path), merge_imports=True)
        self.view.materialize_patterns()
        self.collections = get_collection_name_to_class_names_map(self.view)
        self.collection_classes = set().union(*map(set, self.collections.values()))
        self.validator = Validator(
            schema=self.view.schema,
            validation_plugins=[
                JsonschemaValidationPlugin(closed=True),
                NmdcSchemaValidationPlugin(),
            ],
        )

    def validate(self, database: dict) -> None:
        """Check structure, materialized ID patterns, and NMDC storage units."""
        if not isinstance(database, dict):
            raise ValueError("Expected a Database object")
        results = self.validator.validate(database, target_class="Database").results
        if results:
            raise ValueError(
                "Invalid Database:\n" + "\n".join(result.message for result in results)
            )

    def class_name(self, record: dict, fallback: str | None = None) -> str:
        """Resolve the actual class URI, including non-nmdc class URIs."""
        if "type" not in record and fallback:
            return fallback
        name = translate_class_uri_into_schema_class_name(self.view, record.get("type"))
        if name is None:
            raise ValueError(f"Unknown schema class URI: {record.get('type')!r}")
        return name

    def node(self, record: dict, fallback: str | None = None) -> Node:
        """Style by schema ancestry rather than by spelling of identifiers."""
        name = self.class_name(record, fallback)
        ancestors = self.view.class_ancestors(name)
        kind = "record"
        for parent, candidate in (
            ("Manifest", "manifest"),
            ("DataObject", "data"),
            ("PlannedProcess", "process"),
            ("MaterialEntity", "sample"),
            ("OntologyClass", "ontology"),
        ):
            if parent in ancestors:
                kind = candidate
                break
        return Node(record, name, kind)


@lru_cache(maxsize=1)
def default_schema() -> DiagramSchema:
    """Reuse the source schema for callers processing multiple examples."""
    return DiagramSchema()


def build_graph(
    database: dict, allow_external: bool = False, schema: DiagramSchema | None = None
) -> tuple[dict[str, Node], list[tuple[str, str, str]]]:
    """Validate and draw all collection records and schema-defined relationships.

    Identified inline objects get occurrence-specific nodes, so repeated ontology
    terms with different annotations are not silently combined. Anonymous wrappers
    are traversed using dotted/indexed edge paths. Scalar URI fields remain values;
    only slots with class ranges become references. Missing collection records are
    errors unless allow_external is enabled. Isolated records are retained.
    """
    schema = schema or default_schema()
    schema.validate(database)
    nodes: dict[str, Node] = {}
    locations = {}
    edges = set()
    pending = []

    for collection in sorted(schema.collections):
        for index, record in enumerate(database.get(collection, []) or []):
            name = schema.class_name(record)
            identifier_slot = schema.view.get_identifier_slot(name)
            location = f"/{collection}/{index}"
            identifier = (
                record[identifier_slot.name]
                if identifier_slot
                else "record:" + location
            )
            if identifier in nodes:
                raise ValueError(f"Duplicate record id: {identifier}")
            nodes[identifier] = schema.node(record)
            locations[identifier] = location

    def walk(
        record: dict, class_name: str, owner: str, location: str, prefix: str = ""
    ) -> None:
        for slot_name, value in sorted(record.items()):
            if value is None:
                continue
            slot = schema.view.induced_slot(slot_name, class_name)
            ranges = set(
                get_names_of_classes_in_effective_range_of_slot(schema.view, slot)
            )
            if not ranges:
                continue
            predicate = f"{prefix}.{slot_name}" if prefix else slot_name
            values = (
                list(enumerate(value)) if isinstance(value, list) else [(None, value)]
            )
            # LinkML can inline multivalued, identified objects as a keyed mapping.
            if (
                isinstance(value, dict)
                and slot.multivalued
                and not slot.inlined_as_list
            ):
                identifier_slot = schema.view.get_identifier_slot(slot.range)
                if identifier_slot and "type" not in value:
                    values = [
                        (key, {identifier_slot.name: key, **item})
                        for key, item in value.items()
                    ]
            for index, item in values:
                path = f"{predicate}[{index}]" if index is not None else predicate
                item_location = f"{location}/{slot_name}" + (
                    f"/{index}" if index is not None else ""
                )
                if isinstance(item, dict):
                    child_class = schema.class_name(item, slot.range)
                    identifier_slot = schema.view.get_identifier_slot(child_class)
                    if identifier_slot and identifier_slot.name in item:
                        child_key = "inline:" + item_location
                        nodes[child_key] = schema.node(item, child_class)
                        edges.add((owner, child_key, path))
                        walk(item, child_class, child_key, item_location)
                    else:
                        walk(item, child_class, owner, item_location, path)
                elif isinstance(item, str):
                    pending.append((owner, item, predicate, ranges))

    for identifier, location in list(locations.items()):
        node = nodes[identifier]
        walk(node.record, node.class_name, identifier, location)

    missing = set()
    for owner, reference, predicate, ranges in pending:
        if reference in locations:
            if nodes[reference].class_name not in ranges:
                raise ValueError(
                    f"{owner}.{predicate} references {reference}, whose class "
                    f"{nodes[reference].class_name} is outside the slot range"
                )
        else:
            if ranges & schema.collection_classes:
                missing.add(reference)
            nodes.setdefault(
                reference, Node({"id": reference}, "External reference", "external")
            )
        edges.add((owner, reference, predicate))
    if missing and not allow_external:
        raise ValueError(
            "References absent from Database: "
            + ", ".join(sorted(missing))
            + ". Use --allow-external for deliberately partial examples."
        )
    return dict(sorted(nodes.items())), sorted(edges)


def label_values(value: Any, parts: list[str], path: str = "") -> list[str]:
    """Format selected scalar/quantity metadata without losing list positions."""
    if isinstance(value, list):
        return [
            line
            for index, item in enumerate(value)
            for line in label_values(item, parts, f"{path}[{index}]")
        ]
    if parts:
        key, *rest = parts
        if isinstance(value, dict) and key in value:
            return label_values(value[key], rest, f"{path}.{key}" if path else key)
        return []
    if isinstance(value, dict):
        unit = value.get("has_unit", "")
        if "has_numeric_value" in value:
            value = f"{value['has_numeric_value']} {unit}".strip()
        elif (
            "has_minimum_numeric_value" in value or "has_maximum_numeric_value" in value
        ):
            value = f"{value.get('has_minimum_numeric_value', '?')}–{value.get('has_maximum_numeric_value', '?')} {unit}".strip()
        elif "has_raw_value" in value:
            value = value["has_raw_value"]
        else:
            return []
    return [f"{path}: {value}"]


def node_label(
    node: Node, label_slots: tuple[str, ...] = (), location: str = ""
) -> str:
    """Show identity and optional metadata selected by the caller."""
    lines = [node.class_name]
    for slot in ("name", "id"):
        if node.record.get(slot) and node.record[slot] not in lines:
            lines.append(str(node.record[slot]))
    if len(lines) == 1 and location:
        lines.append(location.removeprefix("record:"))
    for slot in label_slots:
        lines.extend(label_values(node.record, slot.split(".")))
    return "\n".join(lines)


def mermaid_text(value: str) -> str:
    """Encode data so it cannot introduce Mermaid or HTML syntax."""
    return "".join(
        "<br/>"
        if c == "\n"
        else c
        if c.isalnum() or c in " :.,_-/[]()"
        else f"#{ord(c)};"
        for c in value
    )


def render_graph(
    nodes: dict[str, Node],
    edges: list[tuple[str, str, str]],
    direction: str = "TB",
    view: str = "relationships",
    label_slots: tuple[str, ...] = (),
    source: str = "Database",
) -> str:
    """Serialize one Mermaid graph; SVG rendering is delegated to Mermaid CLI.

    Relationships preserves subject→object direction. Workflow reverses has_input
    and was_generated_by for forward material/data flow, labeling the inverses.
    """
    names = {identifier: f"n{index}" for index, identifier in enumerate(nodes)}
    lines = [
        "%% Generated by src/scripts/database_to_diagram.py; edit the Database and regenerate.",
        f"%% Source: {source.replace(chr(10), ' ').replace(chr(13), ' ')}",
        f"%% View: {view}",
        f"flowchart {direction}",
    ]
    for identifier, node in nodes.items():
        label = mermaid_text(node_label(node, label_slots, identifier))
        shape = f'(["{label}"])' if node.kind == "process" else f'["{label}"]'
        lines.append(f"  {names[identifier]}{shape}:::{node.kind}")
    displayed = {}
    for source_id, target, predicate in edges:
        label = predicate
        if view == "workflow" and predicate in ("has_input", "was_generated_by"):
            source_id, target = target, source_id
            label = {
                "has_input": "input to (inverse has_input)",
                "was_generated_by": "generates (inverse was_generated_by)",
            }[predicate]
        arrow = (
            "-->"
            if predicate in ("has_input", "has_output", "was_generated_by")
            else "-.->"
        )
        displayed.setdefault((source_id, target, arrow), set()).add(label)
    for (source_id, target, arrow), labels in sorted(displayed.items()):
        label = mermaid_text(" / ".join(sorted(labels)))
        lines.append(f'  {names[source_id]} {arrow}|"{label}"| {names[target]}')
    for kind, color in COLORS.items():
        extra = ",stroke-dasharray:5 5" if kind == "external" else ""
        lines.append(
            f"  classDef {kind} fill:{color},stroke:#526278,color:#182334{extra}"
        )
    return "\n".join(lines) + "\n"


def main() -> None:
    """Validate a YAML/JSON Database and write or check its Mermaid diagram."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("database", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--direction", choices=("TB", "LR"), default="TB")
    parser.add_argument(
        "--view", choices=("relationships", "workflow"), default="relationships"
    )
    parser.add_argument(
        "--label-slot",
        action="append",
        default=[],
        help="Add scalar/quantity metadata to labels; dotted paths traverse anonymous objects and lists.",
    )
    parser.add_argument(
        "--allow-external",
        action="store_true",
        help="Draw unresolved references explicitly, while still validating record structure and units.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail if the saved Mermaid source differs; do not write files.",
    )
    args = parser.parse_args()
    try:
        database = yaml.safe_load(args.database.read_text(encoding="utf-8"))
        nodes, edges = build_graph(
            database, args.allow_external, DiagramSchema(args.schema)
        )
        source = args.database.resolve()
        source = (
            str(source.relative_to(ROOT))
            if source.is_relative_to(ROOT)
            else args.database.name
        )
        diagram = render_graph(
            nodes, edges, args.direction, args.view, tuple(args.label_slot), source
        )
        if args.check:
            if (
                not args.output.exists()
                or args.output.read_text(encoding="utf-8") != diagram
            ):
                raise ValueError(f"Diagram is out of date: {args.output}")
        else:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            if (
                not args.output.exists()
                or args.output.read_text(encoding="utf-8") != diagram
            ):
                args.output.write_text(diagram, encoding="utf-8")
    except (ValueError, KeyError, TypeError, OSError, yaml.YAMLError) as error:
        parser.error(str(error))
    print(
        f"{'Checked' if args.check else 'Wrote'} {args.output}: {len(nodes)} nodes, {len(edges)} relationships"
    )


if __name__ == "__main__":
    main()
