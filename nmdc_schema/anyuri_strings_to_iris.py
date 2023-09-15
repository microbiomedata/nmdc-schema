import json
import pprint

import click
from rdflib import Graph, term, XSD, URIRef, Namespace


def read_json_file(file_path):
    with open(file_path, "r") as f:
        json_data = json.load(f)
    return json_data


def context_json_to_rdflib_namespaces(context_dict, graph):
    # pprint.pprint(context_dict)
    context = context_dict["@context"]
    for k, v in context.items():

        if k == "id":
            continue

        if isinstance(v, dict):
            if '@prefix' in v and "@id" in v and v['@prefix'] and v['@id']:
                graph.namespace_manager.bind(k, Namespace(v['@id']), override=False)
            else:
                pass
                # if '@id' in v:
                #     print(f"not asserting a prefix expansion for {k}, which has the element id {v['@id']}")
                # else:
                #     print(f"not asserting a prefix expansion for {k}, which is an element name and an element id")
        elif isinstance(v, str):
            graph.namespace_manager.bind(k, Namespace(v), override=False)


@click.command()
@click.option(
    "-i",
    "--input-ttl",
    required=True,
    type=click.Path(exists=True, dir_okay=False),
)
@click.option(
    "-o",
    "--output-ttl",
    required=True,
    type=click.Path(dir_okay=False),
)
@click.option(
    "-p",
    "--jsonld-context-jsons",
    multiple=True,
    required=True,
    type=click.Path(dir_okay=False),
)
def expand_curies(input_ttl, output_ttl, jsonld_context_jsons):
    """Expand CURIE literals in an RDF graph to their full URI references."""

    graph = Graph()

    for jsonld_context_file in jsonld_context_jsons:
        print(jsonld_context_file)
        context_dict = read_json_file(jsonld_context_file)
        context_json_to_rdflib_namespaces(context_dict, graph)

    for i in graph.namespace_manager.namespaces():
        print(i)

    print(f"Loading {input_ttl}")
    graph.parse(input_ttl, format="ttl")
    print(f"Loaded {input_ttl}")

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
