import click
import yaml
from rdflib import Graph, term, XSD, URIRef, Namespace


def read_yaml_file(file_path):
    with open(file_path, "r") as f:
        yaml_data = yaml.safe_load(f)
    return yaml_data


@click.command()
@click.option(
    "-i",
    "--input-ttl",
    type=click.Path(exists=True, dir_okay=False),
    required=True
)
@click.option(
    "-o",
    "--output-ttl",
    type=click.Path(dir_okay=False),
    required=True
)
@click.option(
    "-p",
    "--prefixes-yaml",
    type=click.Path(dir_okay=False),
    required=True
)
def expand_curies(input_ttl, output_ttl, prefixes_yaml):
    """Expand CURIE literals in an RDF graph to their full URI references."""
    graph = Graph()
    print(f"Loading {input_ttl}")
    graph.parse(input_ttl, format="ttl")
    print(f"Loaded {input_ttl}")

    prefix_expansions = read_yaml_file(prefixes_yaml)

    for k, v in prefix_expansions.items():
        print(f"Binding '{k}' to <{v}>")
        graph.namespace_manager.bind(k, Namespace(v), override=False)

    print("Iterating over triples")
    for s, p, o in graph:
        if o.__class__ == term.Literal and o.datatype == XSD.anyURI:
            obj_curie_string_parts = o.value.split(":")
            if obj_curie_string_parts[0] == "UUID" and obj_curie_string_parts[1]:
                bare_uuid = URIRef(f"urn:uuid:{obj_curie_string_parts[1]}")
                graph.add((s, p, bare_uuid))
                graph.remove((s, p, o))
            else:
                as_true_curie = URIRef(graph.namespace_manager.expand_curie(o.value))
                graph.add((s, p, as_true_curie))
                graph.remove((s, p, o))

    print(f"Serializing to {output_ttl}")
    graph.serialize(
        destination=output_ttl
    )

    click.echo("Expanded CURIE literals in RDF graph.")


if __name__ == "__main__":
    expand_curies()
