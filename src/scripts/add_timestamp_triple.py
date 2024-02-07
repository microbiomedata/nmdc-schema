import click
from rdflib import Graph, Namespace, BNode, Literal, XSD
from datetime import datetime

@click.command()
@click.option('--output', type=click.Path())
def add_triple(output):
    """Add a triple to an existing RDF TTL file with a blank node as the subject and schema:dateCreated as the predicate."""
    
    g = Graph()

    for ns_prefix, ns_uri in {
        'schema': 'http://schema.org/',
    }.items():
        g.bind(ns_prefix, ns_uri)  # not Namespace()

    subject_blank_node = BNode()

    predicate_uri = g.namespace_manager.expand_curie('schema:dateCreated')

    current_datetime = str(datetime.now().isoformat())

    object_literal = Literal(current_datetime, datatype=XSD.dateTime)

    g.add((subject_blank_node, predicate_uri, object_literal))

    serialized_graph = g.serialize(format='ttl')

    print(serialized_graph)

    g.serialize(destination=output, format='ttl')


if __name__ == '__main__':
    add_triple()
