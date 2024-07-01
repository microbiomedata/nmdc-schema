import json

import click
import curies
import rdflib
from rdflib import Graph, term, XSD, URIRef, Namespace


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
@click.option(
    "-p",
    "--emsl-uuid-replacement",
    required=True,
    help="A prefix, from one of the jsonld-context-jsons, that should replace the UUID prefix used in some emsl_biosample_identifiers values",
)
def expand_curies(input_ttl, output_ttl, jsonld_context_jsons, emsl_uuid_replacement):
    """Expand CURIE literals in an RDF graph to their full URI references."""

    graph = Graph()

    for_chaining = []
    for jsonld_context_file in jsonld_context_jsons:
        print(f"Loading prefixes from {jsonld_context_file}")
        with open(jsonld_context_file) as json_file:
            temp_dict = json.load(json_file)
        if '@context' in temp_dict and '@vocab' in temp_dict['@context']:  # todo make a list of excluded keys
            del temp_dict['@context']['@vocab']
        temp_context = curies.load_jsonld_context(temp_dict)
        for_chaining.append(temp_context)

    converter = curies.chain(for_chaining)

    for prefix, uri_prefix in converter.prefix_map.items():
        graph.bind(prefix, rdflib.Namespace(uri_prefix), override=False, replace=False)

    print(f"Loading {input_ttl}")
    graph.parse(input_ttl, format="ttl")
    print(f"Loaded {input_ttl}")

    print("Iterating over triples")
    for s, p, o in graph:
        if o.__class__ == term.Literal and o.datatype == XSD.anyURI:
            o_str = str(o)
            curie_parts = o_str.split(":")
            current_prefix = curie_parts[0]
            current_suffix = curie_parts[1]
            as_true_curie = None
            if current_prefix == "UUID" and current_suffix:
                if str(p) == "https://w3id.org/nmdc/emsl_biosample_identifiers":
                    as_true_curie = (
                        URIRef(graph.namespace_manager.expand_curie(
                            f"{emsl_uuid_replacement}:{current_suffix}")))
                    click.echo(f"Replaced UUID with {emsl_uuid_replacement} in {o_str}")
            else:
                try:
                    as_true_curie = URIRef(graph.namespace_manager.expand_curie(o_str))
                except Exception as e:
                    if current_prefix.isupper():
                        as_true_curie = URIRef(
                            graph.namespace_manager.expand_curie(f"{current_prefix.lower()}:{current_suffix}"))
                    elif current_prefix.islower():
                        as_true_curie = URIRef(
                            graph.namespace_manager.expand_curie(f"{current_prefix.upper()}:{current_suffix}"))
                    else:
                        print(e)
            graph.add((s, p, as_true_curie))
            graph.remove((s, p, o))

    print(f"Serializing to {output_ttl}")
    graph.serialize(
        destination=output_ttl
    )

    click.echo("Expanded CURIE literals in RDF graph.")


if __name__ == "__main__":
    expand_curies()
