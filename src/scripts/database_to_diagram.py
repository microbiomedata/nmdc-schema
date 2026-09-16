"""Draw material/data flow from an NMDC Database YAML or JSON instance.

Edges come from has_input, has_output and DataObject.in_manifest. This is an
instance diagram, not a diagram of the schema's possible class relationships.
"""

import argparse
import json
from pathlib import Path

import yaml


REFERENCE_SLOTS = (
    "has_input",
    "has_output",
    "in_manifest",
    "associated_studies",
    "was_generated_by",
)
COLORS = {
    "sample": "#e5f2ec",
    "process": "#e7effa",
    "data": "#fff0d9",
    "manifest": "#f1e8fa",
    "external": "#ffffff",
}


def build_graph(database: dict, allow_external: bool = False) -> tuple[dict, list]:
    """Index records, check references, and return nodes and directed flow edges.

    A strict read requires closure for REFERENCE_SLOTS, including study and
    producer references that are checked but not drawn. Ontology terms and
    protocol URLs are not Database records. This is not schema validation.
    """
    if not isinstance(database, dict):
        raise ValueError("Expected a Database object with list-valued collections")
    records = {}
    for collection, members in database.items():
        if not collection.endswith("_set") or not isinstance(members, list):
            continue
        for record in members:
            identifier = record["id"]
            if identifier in records:
                raise ValueError(f"Duplicate record id: {identifier}")
            records[identifier] = record

    missing = set()
    edges = []
    for identifier, record in records.items():
        for slot in REFERENCE_SLOTS:
            values = record.get(slot, [])
            if isinstance(values, str):
                values = [values]
            for reference in values:
                if reference not in records:
                    missing.add(reference)
                if slot == "has_input":
                    edges.append((reference, identifier, slot))
                elif slot in ("has_output", "in_manifest"):
                    edges.append((identifier, reference, slot))
    if missing and not allow_external:
        raise ValueError(
            "References absent from Database: " + ", ".join(sorted(missing))
        )
    connected = {
        identifier for source, target, _ in edges for identifier in (source, target)
    }
    nodes = {
        identifier: records.get(identifier, {}) for identifier in sorted(connected)
    }
    return nodes, sorted(set(edges))


def node_kind(record: dict) -> str:
    """Choose a visual style without interpreting sample names or identifiers."""
    if not record:
        return "external"
    class_name = record["type"].split(":")[-1]
    if class_name == "Manifest":
        return "manifest"
    if class_name == "DataObject":
        return "data"
    if "has_input" in record or "has_output" in record:
        return "process"
    return "sample"


def node_label(identifier: str, record: dict) -> str:
    """Include instance identity and SIP measurements recorded in the source."""
    if not record:
        return f"External reference (not defined)\n{identifier}"
    lines = [record["type"].split(":")[-1], record.get("name", identifier)]
    if lines[-1] != identifier:
        lines.append(identifier)
    for slot in (
        "gradient_position",
        "gradient_pos_density",
        "gradient_pos_rel_am",
        "manifest_category",
    ):
        if slot in record:
            value = record[slot]
            if isinstance(value, dict):
                value = f"{value.get('has_numeric_value', value.get('has_raw_value', ''))} {value.get('has_unit', '')}".strip()
            lines.append(f"{slot}: {value}")
    for addition in record.get("isotopolog_additions", []):
        compound = addition.get("isotopolog", {})
        substance = addition.get("hetero_isotopolog") or compound.get(
            "has_raw_value", ""
        )
        lines.append(
            f"{addition['isotope']}; {addition['isotopolog_label']}; {substance}"
        )
    return "\n".join(lines)


def mermaid_text(value: str) -> str:
    """Encode label text so YAML content cannot introduce Mermaid syntax."""
    return "".join(
        "<br/>"
        if character == "\n"
        else character
        if character.isalnum() or character in " :.,_-/"
        else f"#{ord(character)};"
        for character in value
    )


def render_graph(
    nodes: dict, edges: list, output_format: str, direction: str = "TB"
) -> str:
    """Serialize the same instance graph as Mermaid or Graphviz DOT."""
    names = {identifier: f"n{index}" for index, identifier in enumerate(nodes)}
    if output_format == "mermaid":
        lines = [
            "%% Generated from Database data; edit the YAML, then regenerate.",
            f"flowchart {direction}",
        ]
        for identifier, record in nodes.items():
            label = mermaid_text(node_label(identifier, record))
            lines.append(f'  {names[identifier]}["{label}"]:::{node_kind(record)}')
        for source, target, relation in edges:
            arrow = "-.->" if relation == "in_manifest" else "-->"
            lines.append(f"  {names[source]} {arrow}|{relation}| {names[target]}")
        for kind, color in COLORS.items():
            lines.append(f"  classDef {kind} fill:{color},stroke:#526278,color:#182334")
    else:
        lines = [
            "// Generated from Database data; edit the YAML, then regenerate.",
            "digraph database {",
            f"  rankdir={direction};",
            '  graph [bgcolor="white", nodesep=0.3, ranksep=0.55];',
            '  node [fontname="Helvetica", fontsize=10, style="rounded,filled", color="#526278", margin="0.15,0.1"];',
            '  edge [fontname="Helvetica", fontsize=8, color="#526278"];',
        ]
        for identifier, record in nodes.items():
            kind = node_kind(record)
            shape = "ellipse" if kind == "process" else "box"
            label = json.dumps(node_label(identifier, record), ensure_ascii=False)
            lines.append(
                f'  {names[identifier]} [label={label}, shape={shape}, fillcolor="{COLORS[kind]}"];'
            )
        for source, target, relation in edges:
            style = "dashed" if relation == "in_manifest" else "solid"
            lines.append(
                f'  {names[source]} -> {names[target]} [label="{relation}", style={style}];'
            )
        lines.append("}")
    return "\n".join(lines) + "\n"


def main() -> None:
    """Generate a diagram source from a Database file."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("database", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--format", choices=("mermaid", "dot"), default="mermaid")
    parser.add_argument("--direction", choices=("TB", "LR"), default="TB")
    parser.add_argument(
        "--allow-external",
        action="store_true",
        help="Draw undefined flow references explicitly; otherwise reject missing references.",
    )
    args = parser.parse_args()
    try:
        database = yaml.safe_load(args.database.read_text(encoding="utf-8"))
        nodes, edges = build_graph(database, args.allow_external)
    except (ValueError, KeyError, TypeError) as error:
        parser.error(str(error))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        render_graph(nodes, edges, args.format, args.direction), encoding="utf-8"
    )
    print(f"Wrote {args.output}: {len(nodes)} nodes, {len(edges)} edges")


if __name__ == "__main__":
    main()
