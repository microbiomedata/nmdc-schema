import pprint

from linkml_runtime.utils.schemaview import SchemaView

nmdc_mixs_file = "../src/schema/mixs.yaml"
mixs_6_file = "../mixs/model/schema/mixs.yaml"

nmdc_mixs_view = SchemaView(nmdc_mixs_file)
mixs_6_view = SchemaView(mixs_6_file)

mixs_6_slots = mixs_6_view.all_slots()
mixs_6_slot_names = [v.name for k, v in mixs_6_slots.items()]
mixs_6_slot_names.sort()
# print(mixs_6_slot_names)

nmdc_mixs_slots = nmdc_mixs_view.all_slots(imports=False)
nmdc_mixs_slot_names = [v.name for k, v in nmdc_mixs_slots.items()]
nmdc_mixs_slot_names.sort()
# print(nmdc_mixs_slot_names)

lost_slots = list(set(nmdc_mixs_slot_names) - set(mixs_6_slot_names))
lost_slots.sort()
pprint.pprint(lost_slots)

# nmdc_mixs_elements = nmdc_mixs_view.all_elements(imports=False)
#
# nmdc_mixs_element_names = [v.name for k, v in nmdc_mixs_elements.items()]
# nmdc_mixs_element_names.sort()
#
# type_dol = {}
# for i in nmdc_mixs_element_names:
#     i_type = type(i)
#     if i_type in type_dol:
#         type_dol[i_type].append(i)
#     else:
#         type_dol[i_type] = [i]
#
# print(list(type_dol.keys()))
