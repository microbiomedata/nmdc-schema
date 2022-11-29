import pprint

from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.linkml_model import SubsetDefinition

root_schema_file = 'src/schema/nmdc.yaml'
mixs_schema_file = 'src/schema/mixs.yaml'
core_schema_file = 'src/schema/core.yaml'
types_schema_url = 'https://w3id.org/linkml/types'
# merged_schema_file = 'target/nmdc_merged.yaml'
depleted_mixs_yaml = 'src/schema/mixs_depleted.yaml'
depleted_nmdc_yaml = 'src/schema/nmdc_depleted.yaml'

mixs_view = SchemaView(mixs_schema_file)
# mixs_view.merge_imports()
core_view = SchemaView(core_schema_file)

types_view = SchemaView(types_schema_url)

nmdc_view = SchemaView(root_schema_file)
# nmdc_elements = nmdc_view.all_elements()
#
# initial_element_count = len(nmdc_elements)
# print(initial_element_count)

nmdc_view.merge_imports()
nmdc_elements = nmdc_view.all_elements()

# merged_element_count = len(nmdc_elements)
# print(merged_element_count)

# yaml_dumper.dump(nmdc_view.schema, merged_schema_file)

mixs_elements = mixs_view.all_elements()

# types_dict = {}
for ek, ev in mixs_elements.items():
    e_from_core = core_view.get_element(ek)
    if e_from_core:
        efc_type = type(e_from_core).class_name
    else:
        efc_type = None

    et = type(ev).class_name
    # if et not in types_dict:
    #     types_dict[et] = [ek]
    # else:
    #     types_dict[et].append(ek)
    print(f"{ek} has type {et} in MIXS and {efc_type} in core")

    if efc_type == 'slot_definition' and ek in mixs_view.schema.slots:
        # mixs_view.delete_slot(ek)
        del mixs_view.schema.slots[ek]

    if efc_type == 'class_definition' and ek in mixs_view.schema.classes:
        del mixs_view.schema.classes[ek]

    if efc_type == 'enum_definition' and ek in mixs_view.schema.enums:
        del mixs_view.schema.enums[ek]

    if efc_type == 'type_definition' and ek in mixs_view.schema.types:
        del mixs_view.schema.types[ek]

del mixs_view.schema['imports']

yaml_dumper.dump(mixs_view.schema, depleted_mixs_yaml)

for nk, nv in nmdc_elements.items():
    e_from_core = core_view.get_element(nk)
    e_from_mixs = mixs_view.get_element(nk)
    e_from_types = types_view.get_element(nk)

    if e_from_mixs:
        efm_type = type(e_from_mixs).class_name
    else:
        efm_type = None

    if e_from_types:
        eft_type = type(e_from_types).class_name
    else:
        eft_type = None

    if e_from_core:
        efc_type = type(e_from_core).class_name
    else:
        efc_type = None

    nt = type(nv).class_name

    print(f"{nk} has type {nt} in NMDC and {efm_type} in MIxS")

    if efm_type == 'slot_definition' and not efc_type and nk in nmdc_view.schema.slots:
        del nmdc_view.schema.slots[nk]

    if efm_type == 'class_definition' and not efc_type and nk in nmdc_view.schema.classes:
        del nmdc_view.schema.classes[nk]

    if efm_type == 'enum_definition' and not efc_type and nk in nmdc_view.schema.enums:
        del nmdc_view.schema.enums[nk]

    if eft_type == 'type_definition' and nk in nmdc_view.schema.types:
        del nmdc_view.schema.types[nk]

    # if efm_type == 'type_definition' and nk in nmdc_view.schema.types:
    #     del nmdc_view.schema.types[nk]

nmdc_view.schema.imports.append('mixs_depleted')
nmdc_view.schema.imports.append('linkml:types')

# are we getting the subsets? see https://github.com/linkml/linkml-runtime/pull/230
nmdc_view.schema.subsets['mixs extension'] = SubsetDefinition(name="mixs extension")
nmdc_view.schema.subsets['workflow subset'] = SubsetDefinition(name="workflow subset")

yaml_dumper.dump(nmdc_view.schema, depleted_nmdc_yaml)
