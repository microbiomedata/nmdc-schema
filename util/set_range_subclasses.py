# import pprint
#
# from linkml_runtime import SchemaView
# from linkml_runtime.dumpers import yaml_dumper
#
# nmdc_schema_file = "../src/schema/nmdc.yaml"
#
# nmdc_view = SchemaView(nmdc_schema_file)
#
# # print(nmdc_view.schema.name)
#
# d = nmdc_view.induced_class('Database')
#
# print(type(d))
# # <class 'linkml_runtime.linkml_model.meta.ClassDefinition'>
#
# print(yaml_dumper.dumps(d))
#
# da = d.attributes()
#
# print(type(da))

raw = ['a', 'B', 'c']
print(raw)
lc = [x.lower() for x in raw]
print(lc)

raw_only = set(raw) - set(lc)
print(raw_only)
lc_only = set(lc) - set(raw)
print(lc_only)

strict_intersection = set(raw) & set(lc)
print(strict_intersection)
collection_centric = set(strict_intersection) | set(raw_only)
print(collection_centric)
