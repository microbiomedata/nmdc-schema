import pprint
from urllib.parse import quote

import click
from linkml_runtime import SchemaView
from rdflib import Graph, Namespace

from linkml_runtime.utils.formatutils import camelcase, underscore

# todo contains a lot of hard-coding that could probably be replaced with some external source of prefix mappings

# todo do we want to materialize slot definitions?

# todo should properties be expressed as URIs (like numerical, for MIxS) or text labels?
#   actually it looks like just about everything should be expressed with a label-based URI
#     in order to integrate with the generated owl

### materialization
# OBI:0000011 dcterms:description xsd:string
# nmdc:Database nmdc:planned_process_set OBI:0000011
# etc

### OWL
# nmdc:PlannedProcess a owl:Class,
#     skos:exactMatch OBI:0000011 ;

### materialization
# prov:Association nmdc:applied_roles nmdc:credit%20enum ;

### OWL
# nmdc:CreditEnum a owl:Class,

# nmdc:Biosample dcterms:description xsd:string ;
#     dcterms:isPartOf nmdc:NamedThing ;
#     MIXS:0000001 nmdc:QuantityValue ;

# nmdc:DataObject dcterms:description xsd:string ;
#     nmdc:alternative_identifiers xsd:anyURI ;
#     nmdc:compression_type xsd:string ;
#     nmdc:data_object_type nmdc:file%20type%20enum ;

# nmdc:OmicsProcessing dcterms:description xsd:string ;
#     dcterms:isPartOf nmdc:NamedThing ;
#     MIXS:0000037 nmdc:TextValue ;

# nmdc:FieldResearchSite dcterms:description xsd:string ;
#     dcterms:isPartOf nmdc:NamedThing ;
#     MIXS:0000009 nmdc:GeolocationValue ;

### OWL

# nmdc:SampleTypeEnum a owl:Class,
#         linkml:EnumDefinition ;
#     owl:unionOf ( <https://w3id.org/nmdc/SampleTypeEnum#soil> <https://w3id.org/nmdc/SampleTypeEnum#water_extract_soil> ) ;
#     linkml:permissible_values <https://w3id.org/nmdc/SampleTypeEnum#soil>,
#         <https://w3id.org/nmdc/SampleTypeEnum#water_extract_soil> .

# Create an RDF graph
g = Graph()


@click.command()
@click.option('-s', '--schema', default='src/schema/nmdc.yaml', help='Path to schema file')
@click.option('-o', '--output', default='output.ttl', help='Output TTL file path')
@click.option('-e', '--inc-enums', is_flag=True)
@click.option('-t', '--inc-types', is_flag=True)
def cli(schema, output, inc_enums, inc_types):
    schema_view = SchemaView(schema)

    schema_default_range_name = schema_view.schema.default_range
    schema_default_prefix = schema_view.schema.default_prefix

    all_classes = schema_view.all_classes()
    all_class_names = sorted(c.name for c in all_classes.values())

    for ns_prefix, ns_uri in {
        'ex': 'http://example.org/',
        'MIXS': 'https://w3id.org/mixs/',
        'dcterms': 'http://purl.org/dc/terms/',
        'nmdc': 'https://w3id.org/nmdc/',
        'prov': 'http://www.w3.org/ns/prov#',
        'schema': 'http://schema.org/',
        'wgs84': 'http://www.w3.org/2003/01/geo/wgs84_pos#',
        'xsd': 'http://www.w3.org/2001/XMLSchema#',
        'OBI': 'http://purl.obolibrary.org/obo/OBI_',
        'slot': 'http://example.com/slot/',
    }.items():
        g.bind(ns_prefix, ns_uri)  # not Namespace()

    graph_as_curie_dict = []

    for current_class_name in all_class_names:
        current_class = schema_view.induced_class(current_class_name)
        # current_class_class_uri = current_class.class_uri or f"{schema_default_prefix}:{current_class_name}"
        current_class_class_uri = f"{schema_default_prefix}:{camelcase(current_class_name)}"
        class_slots = current_class.attributes
        class_slot_names = sorted(s.name for s in class_slots.values())

        for current_slot_name in class_slot_names:
            current_slot = schema_view.get_slot(current_slot_name)
            # current_slot_slot_uri = current_slot.slot_uri or f"{schema_default_prefix}:{current_slot_name}"
            # current_slot_slot_uri = f"{schema_default_prefix}:{underscore(current_slot_name)}"
            current_slot_slot_uri = f"slot:{underscore(current_slot_name)}"
            current_slot_range = current_slot.range or schema_default_range_name
            current_slot_range_obj = schema_view.get_element(current_slot_range)
            current_slot_range_type = type(current_slot_range_obj).class_name

            uri_for_range = None
            if current_slot_range_type == 'class_definition':
                uri_for_range = (
                    # current_slot_range_obj.class_uri or
                    # f"{schema_default_prefix}:{quote(camelcase(current_slot_range))}"
                    f"{schema_default_prefix}:{quote(camelcase(current_slot_range))}"
                )
            elif current_slot_range_type == 'enum_definition' and inc_enums:
                uri_for_range = (
                        current_slot_range_obj.enum_uri or
                        f"{schema_default_prefix}:{quote(camelcase(current_slot_range))}"
                )
            elif current_slot_range_type == 'type_definition' and inc_types:
                uri_for_range = (
                        current_slot_range_obj.uri or
                        f"{schema_default_prefix}:{quote(current_slot_range)}"
                )

            if uri_for_range:
                graph_as_curie_dict.append(
                    {'subject': current_class_class_uri, 'predicate': current_slot_slot_uri, 'object': uri_for_range}
                )

    # Print triples with whitespace in any part
    for triple in graph_as_curie_dict:
        if any(' ' in part for part in triple.values()):
            pprint.pprint(triple)
            continue

        # Expand CURIEs and add triples to the RDF graph
        subject = g.namespace_manager.expand_curie(str(triple['subject']))
        predicate = g.namespace_manager.expand_curie(str(triple['predicate']))
        obj = g.namespace_manager.expand_curie(str(triple['object']))
        g.add((subject, predicate, obj))

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
