from linkml_runtime.dumpers import yaml_dumper

from nmdc_schema.nmdc_schema_accepting_legacy_ids import Biosample, ControlledIdentifiedTermValue, OntologyClass


def do_test():
    bs = Biosample(id='xxx',
                   part_of='gold:Gs0114663',
                   env_medium=ControlledIdentifiedTermValue(
                       term=OntologyClass(id='ENVO:00010483', name='freshwater environment')),
                   env_broad_scale=ControlledIdentifiedTermValue(
                       term=OntologyClass(id='ENVO:00010483', name='freshwater environment')),
                   env_local_scale=ControlledIdentifiedTermValue(
                       term=OntologyClass(id='ENVO:00010483', name='freshwater environment')),
                   )

    print(yaml_dumper.dumps(bs))
