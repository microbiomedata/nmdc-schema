from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper

# Consider the id for the env_broad_scale belonging to the Biosample with id ‘gold:Gb0110680’:
#  env_broad_scale:
#     has_raw_value: grassland biome [ENVO:01000177]
#     term:
#       id: grassland biome [ENVO:01000177]

schema_file = 'nmdc_materialized_patterns.yaml'

sv = SchemaView(schema_file)

biosample_induced_ebs = sv.induced_slot('env_broad_scale', 'Biosample')
print(yaml_dumper.dumps(biosample_induced_ebs))

controlled_identified_term_value_induced_term = sv.induced_slot('term', 'ControlledIdentifiedTermValue')
print(yaml_dumper.dumps(controlled_identified_term_value_induced_term))

controlled_identified_term_value_induced_id = sv.induced_slot('id', 'OntologyClass')
print(yaml_dumper.dumps(controlled_identified_term_value_induced_id))

ontology_class = sv.induced_class('OntologyClass')
print(yaml_dumper.dumps(ontology_class))
