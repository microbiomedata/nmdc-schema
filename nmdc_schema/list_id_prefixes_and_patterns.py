import pprint

from linkml_runtime import SchemaView

schema_file = '../nmdc_schema/nmdc_schema_merged.yaml'

schema_view = SchemaView(schema_file)

schema_elements = schema_view.all_elements()

constraints_dict = {}
for ek, ev in schema_elements.items():
    et = type(ev).__name__
    current_key = f"{et} {ek}"
    if '_at_time' in ek:
        continue
    if 'id_prefixes' in ev and ev['id_prefixes']:
        current_id_prefixes = ev['id_prefixes']
        current_id_prefixes.sort()
        if current_key in constraints_dict:
            constraints_dict[current_key]['id_prefixes'] = current_id_prefixes
        else:
            constraints_dict[current_key] = {'id_prefixes': current_id_prefixes}
    if 'pattern' in ev and ev['pattern']:
        if current_key in constraints_dict:
            constraints_dict[current_key]['pattern'] = ev['pattern']
        else:
            constraints_dict[current_key] = {'pattern': ev['pattern']}
    if 'slot_usage' in ev and ev['slot_usage']:
        for uk, uv in ev['slot_usage'].items():
            current_key = f"{uk} used in {ek}"
            if 'id_prefixes' in uv and uv['id_prefixes']:
                current_id_prefixes = uv['id_prefixes']
                current_id_prefixes.sort()
                if current_key in constraints_dict:
                    constraints_dict[current_key]['id_prefixes'] = current_id_prefixes
                else:
                    constraints_dict[current_key] = {'id_prefixes': current_id_prefixes}
            if 'pattern' in uv and uv['pattern']:
                if current_key in constraints_dict:
                    constraints_dict[current_key]['pattern'] = uv['pattern']
                else:
                    constraints_dict[current_key] = {'pattern': uv['pattern']}

pprint.pprint(constraints_dict)
