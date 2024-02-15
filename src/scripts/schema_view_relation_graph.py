import pprint
from urllib.parse import quote

import click
from linkml_runtime import SchemaView
from rdflib import Graph, Namespace, RDF, RDFS, OWL

from linkml_runtime.utils.formatutils import camelcase, underscore

from linkml_runtime.dumpers import yaml_dumper

# todo contains a lot of hard-coding that could probably be replaced with some external source of prefix mappings

# todo do we want to materialize slot definitions?

# todo should properties be expressed as URIs (like numerical, for MIxS) or text labels?
#   actually it looks like just about everything should be expressed with a label-based URI
#     in order to integrate with the generated owl

# Create an RDF graph
g = Graph()

# Define custom namespaces
mat = Namespace("https://w3id.org/nmdc/materialized/")
mat_obj_prop = mat.ObjectProperty
mat_range = mat.range
mat_domain = mat.domain


def get_uri_for_element(element_name, schema_view, schema_default_prefix):
    element_obj = schema_view.get_element(element_name)
    element_type = type(element_obj).class_name
    if element_type == 'class_definition':
        return get_uri_for_class(element_name, schema_view, schema_default_prefix)
    elif element_type == 'enum_definition':
        return get_uri_for_enum(element_name, schema_view, schema_default_prefix)
    elif element_type == 'slot_definition':
        return get_uri_for_slot(element_name, schema_view, schema_default_prefix)
    elif element_type == 'type_definition':
        return get_uri_for_type(element_name, schema_view, schema_default_prefix)


def get_uri_for_class(element_name, schema_view, schema_default_prefix):
    element_obj = schema_view.get_element(element_name)
    return element_obj.class_uri or f"{schema_default_prefix}:{quote(camelcase(element_name))}"


def get_uri_for_enum(element_name, schema_view, schema_default_prefix):
    element_obj = schema_view.get_element(element_name)
    return element_obj.enum_uri or f"{schema_default_prefix}:{quote(camelcase(element_name))}"


def get_uri_for_slot(element_name, schema_view, schema_default_prefix):
    element_obj = schema_view.get_element(element_name)
    return element_obj.slot_uri or f"{schema_default_prefix}:{quote(underscore(element_name))}"


def get_uri_for_type(element_name, schema_view, schema_default_prefix):
    element_obj = schema_view.get_element(element_name)
    return element_obj.uri or f"{schema_default_prefix}:{quote(underscore(element_name))}"


@click.command()
@click.option('-s', '--schema', default='src/schema/nmdc.yaml', help='Path to schema file')
@click.option('-o', '--output', default='nmdc.materialized.ttl', help='Output TTL file path')
@click.option('-e', '--inc-enums', is_flag=True)
@click.option('-t', '--inc-types', is_flag=True)
@click.option('-a', '--inc-attr-vals', is_flag=True)
def cli(schema, output, inc_enums, inc_types, inc_attr_vals):
    schema_view = SchemaView(schema)

    schema_default_range_name = schema_view.schema.default_range
    schema_default_prefix = schema_view.schema.default_prefix

    all_classes = schema_view.all_classes()
    all_class_names = sorted(c.name for c in all_classes.values())

    for ns_prefix, ns_uri in {
        'MIXS': 'https://w3id.org/mixs/',
        'OBI': 'http://purl.obolibrary.org/obo/OBI_',
        'dcterms': 'http://purl.org/dc/terms/',
        'linkml': 'https://w3id.org/linkml/',
        'nmdc': 'https://w3id.org/nmdc/',
        'prov': 'http://www.w3.org/ns/prov#',
        'schema': 'http://schema.org/',
        'wgs84': 'http://www.w3.org/2003/01/geo/wgs84_pos#',
        'xsd': 'http://www.w3.org/2001/XMLSchema#',
    }.items():
        g.bind(ns_prefix, ns_uri)  # not Namespace()

    graph_as_curie_dict_list = []

    for current_class_name in all_class_names:
        current_class = schema_view.induced_class(current_class_name)
        current_class_class_uri = get_uri_for_element(current_class_name, schema_view, schema_default_prefix)
        class_slots = current_class.attributes
        class_slot_names = sorted(s.name for s in class_slots.values())

        for current_slot_name in class_slot_names:
            if current_slot_name == 'type':
                continue
            current_slot = schema_view.induced_slot(current_slot_name, current_class_name)
            current_slot_slot_uri = get_uri_for_element(current_slot_name, schema_view, schema_default_prefix)
            current_slot_range = current_slot.range or schema_default_range_name

            uri_for_range = get_uri_for_element(current_slot_range, schema_view, schema_default_prefix)

            print(
                f"{current_class_name} / {current_class_class_uri} {current_slot_name} / {current_slot_slot_uri} {current_slot_range} / {uri_for_range}")

            if uri_for_range:
                graph_as_curie_dict_list.append(
                    {'subject': current_class_class_uri, 'predicate': current_slot_slot_uri, 'object': uri_for_range}
                )

            if 'any_of' in current_slot and current_slot['any_of']:
                for any_of_object in current_slot['any_of']:
                    any_of_type = type(any_of_object).class_name
                    if any_of_type == "anonymous_slot_expression":
                        if 'range' in any_of_object and any_of_object['range']:
                            lazy_object = get_uri_for_element(any_of_object['range'], schema_view,
                                                              schema_default_prefix)
                            graph_as_curie_dict_list.append(
                                {'subject': current_class_class_uri, 'predicate': current_slot_slot_uri,
                                 'object': lazy_object}
                            )
                            print(
                                f"{current_class_name} / {current_class_class_uri} {current_slot_name} / {current_slot_slot_uri} {current_slot_range} / {lazy_object}")

    # Print triples with whitespace in any part
    for triple in graph_as_curie_dict_list:
        if any(' ' in part for part in triple.values()):
            pprint.pprint(triple)
            continue

        # Expand CURIEs and add triples to the RDF graph
        subject = g.namespace_manager.expand_curie(str(triple['subject']))
        predicate = g.namespace_manager.expand_curie(str(triple['predicate']))
        obj = g.namespace_manager.expand_curie(str(triple['object']))
        g.add((subject, predicate, obj))
        g.add((subject, RDF.type, OWL.Class))
        g.add((predicate, RDF.type, OWL.ObjectProperty))
        # g.add((predicate, RDF.type, g.namespace_manager.expand_curie("linkml:SlotDefinition")))
        g.add((predicate, RDFS.domain, subject))
        g.add((predicate, RDFS.range, obj))

        # why dies this type the subjects as xsd:AnyURI?

    # Serialize the RDF graph to a Turtle file
    g.serialize(destination=output, format='turtle')


if __name__ == '__main__':
    cli()

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
