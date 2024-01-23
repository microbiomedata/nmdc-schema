import pprint
from urllib.parse import quote

import click
from linkml_runtime import SchemaView
from rdflib import Graph, Namespace


@click.command()
@click.option('-s', '--schema', default='src/schema/nmdc.yaml', help='Path to schema file')
@click.option('-o', '--output', default='slot-range-type-report.tsv', help='Output TSV file path')
def cli(schema, output):
    schema_view = SchemaView(schema)

    schema_default_range_name = schema_view.schema.default_range
    schema_default_prefix = schema_view.schema.default_prefix

    all_classes = schema_view.all_classes()
    all_class_names = [c.name for c in all_classes.values()]
    all_class_names.sort()

    # metatype_usage = []

    graph_as_curie_dict = []

    # Create an RDF graph
    g = Graph()

    # Define your custom namespace
    ex = Namespace("http://example.org/")

    MIXS = Namespace("https://w3id.org/mixs/")
    dcterms = Namespace("http://purl.org/dc/terms/")
    nmdc = Namespace("https://w3id.org/nmdc/")
    prov = Namespace("http://www.w3.org/ns/prov#")
    schema = Namespace("http://schema.org/")
    wgs84 = Namespace("http://www.w3.org/2003/01/geo/wgs84_pos#")
    xsd = Namespace("http://www.w3.org/2001/XMLSchema#")

    # Define your custom namespaces
    g.bind('nmdc', 'https://w3id.org/nmdc/')
    g.bind('MIXS', 'https://w3id.org/mixs/')
    g.bind('dcterms', 'http://purl.org/dc/terms/')
    g.bind('prov', 'http://www.w3.org/ns/prov#')
    g.bind('schema', 'http://schema.org/')
    g.bind('wgs84', 'http://www.w3.org/2003/01/geo/wgs84_pos#')
    g.bind('xsd', 'http://www.w3.org/2001/XMLSchema#')
    g.bind('OBI', 'http://purl.obolibrary.org/obo/OBI_')

    # as opposed to: @prefix MIXS: <https://w3id.org/mixs/> .

    for current_class_name in all_class_names:
        current_class = schema_view.induced_class(current_class_name)
        current_class_class_uri = None
        if current_class.class_uri:
            current_class_class_uri = current_class.class_uri
        else:
            current_class_class_uri = f"{schema_default_prefix}:{current_class_name}"
        class_slots = current_class.attributes  # dict
        class_slot_names = [s.name for s in class_slots.values()]
        for current_slot_name in class_slot_names:
            current_slot = schema_view.get_slot(current_slot_name)
            current_slot_slot_uri = None
            if current_slot.slot_uri:
                current_slot_slot_uri = current_slot.slot_uri
            else:
                current_slot_slot_uri = f"{schema_default_prefix}:{current_slot_name}"
            current_slot_range = None
            if current_slot.range:
                current_slot_range = current_slot.range
            else:
                current_slot_range = schema_default_range_name
            current_slot_range_obj = schema_view.get_element(current_slot_range)
            current_slot_range_type = type(current_slot_range_obj).class_name
            # metatype_usage.append(current_slot_range_type)
            uri_for_range = None
            if current_slot_range_type == 'class_definition':
                if current_slot_range_obj.class_uri:
                    uri_for_range = current_slot_range_obj.class_uri
                else:
                    uri_for_range = f"{schema_default_prefix}:{quote(current_slot_range)}"
            elif current_slot_range_type == 'enum_definition':
                if current_slot_range_obj.enum_uri:
                    uri_for_range = current_slot_range_obj.enum_uri
                else:
                    uri_for_range = f"{schema_default_prefix}:{quote(current_slot_range)}"
            elif current_slot_range_type == 'type_definition':
                if current_slot_range_obj.uri:
                    uri_for_range = current_slot_range_obj.uri
                else:
                    uri_for_range = f"{schema_default_prefix}:{quote(current_slot_range)}"
            graph_as_curie_dict.append(
                {'subject': current_class_class_uri, 'predicate': current_slot_slot_uri, 'object': uri_for_range})

    # WARNING:rdflib.term:nmdc:core field does not look like a valid URI, trying to serialize this will break.
    # etc

    # {'object': 'xsd:string',
    #  'predicate': 'nmdc:core field',
    #  'subject': 'nmdc:Biosample'}
    # {'object': 'xsd:string',
    #  'predicate': 'nmdc:environment field',
    #  'subject': 'nmdc:Biosample'}
    # {'object': 'xsd:double',
    #  'predicate': 'nmdc:has numeric value',
    #  'subject': 'nmdc:Biosample'}
    # {'object': 'xsd:string',
    #  'predicate': 'nmdc:has raw value',
    #  'subject': 'nmdc:Biosample'}
    # {'object': 'xsd:string',
    #  'predicate': 'nmdc:has unit',
    #  'subject': 'nmdc:Biosample'}
    # {'object': 'xsd:string',
    #  'predicate': 'nmdc:investigation field',
    #  'subject': 'nmdc:Biosample'}
    # {'object': 'xsd:string',
    #  'predicate': 'nmdc:nucleic acid sequence source field',
    #  'subject': 'nmdc:Biosample'}
    # {'object': 'xsd:string',
    #  'predicate': 'nmdc:sequencing field',
    #  'subject': 'nmdc:Biosample'}

    for triple in graph_as_curie_dict:
        if any(' ' in part for part in triple.values()):
            # Skip this triple if any part has whitespace
            pprint.pprint(triple)
            continue

        subject = g.namespace_manager.expand_curie(str(triple['subject']))
        predicate = g.namespace_manager.expand_curie(str(triple['predicate']))
        obj = g.namespace_manager.expand_curie(str(triple['object']))

        g.add((subject, predicate, obj))

    # Serialize the RDF graph to a Turtle file
    g.serialize(destination='output.ttl', format='turtle')


if __name__ == '__main__':
    cli()
