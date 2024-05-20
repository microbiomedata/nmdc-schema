import pprint

from linkml_runtime import SchemaView
from typing import List

from linkml_runtime.dumpers import yaml_dumper

scrutinized_file = "../schema/basic_slots.yaml"
reference_file = "../schema/nmdc.yaml"

skip_classes = ['Database', 'OntologyClass']

scrutinized_view = SchemaView(scrutinized_file)
reference_view = SchemaView(reference_file)

structured_patterns = {}

reference_classes = reference_view.all_classes()
reference_class_names = sorted(reference_classes.keys())

reference_slots = reference_view.all_slots()

for reference_class_name in reference_class_names:
    if reference_class_name in skip_classes:
        continue
    induced_reference_class = reference_view.induced_class(reference_class_name)
    reference_slots = induced_reference_class.attributes
    reference_slot_names = sorted(reference_slots.keys())
    reference_slot_names.sort()
    for reference_slot_name in reference_slot_names:
        range_dict = {}
        range_types = []
        ranges = []
        print(f"{reference_class_name}.{reference_slot_name}")
        global_range = reference_view.get_slot(
            reference_slot_name).range or reference_view.schema.default_range  # todo why couldn't I get that from reference_slots?
        print(f"    {global_range = }")
        range_types.append(reference_view.get_element(global_range).class_class_curie)  # todo lowest priority
        ranges.append(global_range)
        range_dict["global_range"] = {
            "range": global_range,
            "range_types": reference_view.get_element(global_range).class_class_curie,
        }

        usage = reference_classes[reference_class_name].slot_usage.get(reference_slot_name)  # todo medium priority?
        if usage is not None:
            if usage.range is not None:
                if usage.range == global_range:
                    warning = "redundant "
                else:
                    warning = ""
                print(f"    {warning}{usage.range = }")
                range_types.append(reference_view.get_element(usage.range).class_class_curie)
                ranges.append(usage.range)
                range_dict["usage.range"] = {
                    "range": usage.range,
                    "range_types": reference_view.get_element(usage.range).class_class_curie,
                }

        any_ofs = reference_slots[reference_slot_name].any_of  # todo highest priority?
        if len(any_ofs) > 0:
            for any_of in any_ofs:
                if any_of.range is not None:
                    print(f"    {any_of.range = }")
                    if "any_of.range" not in range_dict:
                        range_dict["any_of.range"] = []
                    range_types.append(reference_view.get_element(any_of.range).class_class_curie)
                    ranges.append(any_of.range)
                    range_dict["any_of.range"].append({
                        "range": any_of.range,
                        "range_types": reference_view.get_element(any_of.range).class_class_curie,
                    })
        ranges_zip = dict(zip(ranges, range_types))
        # pprint.pprint(ranges_zip)
        range_types = set(range_types)
        if len(range_types) > 1:
            print(f"    {range_types = }")

        pprint.pprint(range_dict)

        if "any_of.range" in range_dict:
            prioritized_ranges = range_dict["any_of.range"]
        elif "usage.range" in range_dict:
            prioritized_ranges = [range_dict["usage.range"]]
        else:
            prioritized_ranges = [range_dict["global_range"]]

        for prioritized_range in prioritized_ranges:
            if prioritized_range["range_types"] == "linkml:ClassDefinition":
                identifying_slot = reference_view.get_identifier_slot(prioritized_range["range"])
                if identifying_slot is not None and prioritized_range['range'] not in skip_classes:
                    print(f"    {prioritized_range = }")

    #     if "linkml:ClassDefinition" in range_types:
    #         for rk, rt in ranges_zip.items():
    #             if rt == "linkml:ClassDefinition":
    #                 descendants = reference_view.class_descendants(rk)
    #                 descendants.sort()
    #                 for descendant in descendants:
    #                     identifying_slot = reference_view.get_identifier_slot(descendant)
    #                     if identifying_slot:
    #                         print(f"        identifiable {descendant = }")
    #                         # does the idenifying slot have a pattern or structured patten by any route?
    #                 # print(f"    will check {len(descendants)} {descendants} for identifier slot")
    # # todo what is in the range? asserted global (including default range if necessary?), slot_usage direct, and/or slot_usage any_of

    # # reference_class = reference_view.induced_class(reference_class_name) # todo ask for attributes. will get dict not list
    # reference_class = reference_classes[reference_class_name]
    # reference_slot_names = reference_class.slots
    # reference_slot_names.sort()
    # for reference_slot_name in reference_slot_names:
    #     reference_slot_obj = reference_view.induced_slot(reference_slot_name, reference_class_name)
    #     reference_slot_range = reference_slot_obj.range  # todo what about any of ranges?
    #     # if reference_slot_obj.any_of:
    #     #     # print(f"{reference_slot_obj.any_of}")
    #     #     print("    ANY OF!")
    #     if reference_slot_range in reference_class_names:
    #         identifying_slot = reference_view.get_identifier_slot(reference_slot_range)
    #         if identifying_slot:
    #
    #             if identifying_slot.name in reference_class.slot_usage:
    #                 range_class = reference_view.induced_class(reference_slot_range)
    #                 x = range_class.attributes[identifying_slot.name]
    #                 if x.structured_pattern is not None and x.structured_pattern.syntax is not None:
    #                     print(
    #                         f"{reference_class_name}.{reference_slot_name} has range {reference_slot_range} which is identified by slot {identifying_slot.name} and follows structured pattern {x.structured_pattern.syntax}")
