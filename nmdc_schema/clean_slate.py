import pkgutil

# root yaml file
schema_root_bytes = pkgutil.get_data("nmdc_schema", "../src/schema/nmdc.yaml")
schema_root_string = str(schema_root_bytes, "utf-8")
print(type(schema_root_string))

# jsonschema
schema_json_bytes = pkgutil.get_data("nmdc_schema", "../project/jsonschema/nmdc.schema.json")
schema_json_string = str(schema_json_bytes, "utf-8")
print(type(schema_json_string))

print(schema_json_string)
