from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.linkml_model import SchemaDefinition

pmvfs = SchemaDefinition(name="prep_merge_vs_from_schema", id="http://example.com/prep_merge_vs_from_schema")
pmvfs.imports.append("src/schema/mixs_6_for_nmdc.yaml")
dumped = yaml_dumper.dumps(pmvfs)

print(dumped)
