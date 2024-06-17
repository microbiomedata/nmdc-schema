import logging
from linkml_runtime import SchemaView
from typing import Dict, List, Union

import click

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

scrutinized_file = "../schema/basic_slots.yaml"
reference_file = "../schema/nmdc.yaml"

skip_classes = [
    'Database',
    'NamedThing',  # Fixed missing comma
    'OntologyClass',
]


def get_range_dict(reference_view: SchemaView, reference_slot_name: str, reference_class_name: str) -> Dict[
    str, Union[str, Dict[str, str]]]:
    """
    Get the range dictionary for a given slot name.

    :param reference_view: SchemaView of the reference schema
    :param reference_slot_name: Name of the slot being processed
    :param reference_class_name: Name of the class being processed
    :return: A tuple containing range dictionary, list of range types, and list of ranges
    """
    range_dict = {}
    range_types = []
    ranges = []

    global_range = reference_view.get_slot(reference_slot_name).range or reference_view.schema.default_range
    logger.info(f"    global_range = {global_range}")
    range_types.append(reference_view.get_element(global_range).class_class_curie)
    ranges.append(global_range)
    range_dict["global_range"] = {
        "range": global_range,
        "range_types": reference_view.get_element(global_range).class_class_curie,
    }

    return range_dict, range_types, ranges


def handle_usage(reference_view: SchemaView, usage, global_range: str, range_types: List[str], ranges: List[str],
                 range_dict: Dict[str, Union[str, Dict[str, str]]]) -> None:
    """
    Handle the slot usage ranges.

    :param reference_view: SchemaView of the reference schema
    :param usage: Slot usage information
    :param global_range: The global range of the slot
    :param range_types: List of range types
    :param ranges: List of ranges
    :param range_dict: Dictionary of ranges
    :return: None
    """
    if usage.range is not None:
        if usage.range != global_range:
            logger.info(f"    usage.range = {usage.range}")
        range_types.append(reference_view.get_element(usage.range).class_class_curie)
        ranges.append(usage.range)
        range_dict["usage.range"] = {
            "range": usage.range,
            "range_types": reference_view.get_element(usage.range).class_class_curie,
        }


def handle_any_of(reference_view: SchemaView, any_ofs: List, range_types: List[str], ranges: List[str],
                  range_dict: Dict[str, Union[str, Dict[str, str]]]) -> None:
    """
    Handle the any_of ranges for a slot.

    :param reference_view: SchemaView of the reference schema
    :param any_ofs: List of any_of ranges
    :param range_types: List of range types
    :param ranges: List of ranges
    :param range_dict: Dictionary of ranges
    :return: None
    """
    if any_ofs:
        for any_of in any_ofs:
            if any_of.range is not None:
                logger.info(f"    any_of.range = {any_of.range}")
                if "any_of.range" not in range_dict:
                    range_dict["any_of.range"] = []
                range_types.append(reference_view.get_element(any_of.range).class_class_curie)
                ranges.append(any_of.range)
                range_dict["any_of.range"].append({
                    "range": any_of.range,
                    "range_types": reference_view.get_element(any_of.range).class_class_curie,
                })


def get_prioritized_ranges(range_dict: Dict[str, Union[str, Dict[str, str]]]) -> List[Dict[str, str]]:
    """
    Get the prioritized ranges from the range dictionary.

    :param range_dict: Dictionary of ranges
    :return: List of prioritized ranges
    """
    if "any_of.range" in range_dict:
        return range_dict["any_of.range"]
    elif "usage.range" in range_dict:
        return [range_dict["usage.range"]]
    else:
        return [range_dict["global_range"]]


def process_prioritized_ranges(reference_view: SchemaView, prioritized_ranges: List[Dict[str, str]],
                               skip_classes: List[str], reference_class_name: str, reference_slot_name: str) -> None:
    """
    Process the prioritized ranges for a slot.

    :param reference_view: SchemaView of the reference schema
    :param prioritized_ranges: List of prioritized ranges
    :param skip_classes: List of classes to skip
    :param reference_class_name: Name of the class being processed
    :param reference_slot_name: Name of the slot being processed
    :return: None
    """
    for prioritized_range in prioritized_ranges:
        if prioritized_range["range_types"] == "linkml:ClassDefinition":
            process_class_definitions(reference_view, prioritized_range, skip_classes, reference_class_name,
                                      reference_slot_name)


def process_class_definitions(reference_view: SchemaView, prioritized_range: Dict[str, str], skip_classes: List[str],
                              reference_class_name: str, reference_slot_name: str) -> None:
    """
    Process the class definitions for a prioritized range.

    :param reference_view: SchemaView of the reference schema
    :param prioritized_range: Dictionary of prioritized range
    :param skip_classes: List of classes to skip
    :param reference_class_name: Name of the class being processed
    :param reference_slot_name: Name of the slot being processed
    :return: None
    """
    identifying_slot = reference_view.get_identifier_slot(prioritized_range["range"])
    if identifying_slot is not None and prioritized_range['range'] not in skip_classes:
        logger.info(f"    prioritized_range = {prioritized_range}")
        pr_descendants = sorted(reference_view.class_descendants(prioritized_range['range']))
        for pr_descendant in pr_descendants:
            process_descendants(reference_view, pr_descendant, reference_class_name, reference_slot_name)


def process_descendants(reference_view: SchemaView, pr_descendant: str, reference_class_name: str,
                        reference_slot_name: str) -> None:
    """
    Process the descendants of a class.

    :param reference_view: SchemaView of the reference schema
    :param pr_descendant: Name of the descendant class
    :param reference_class_name: Name of the class being processed
    :param reference_slot_name: Name of the slot being processed
    :return: None
    """
    pr_identifying_slot = reference_view.get_identifier_slot(pr_descendant)
    if pr_identifying_slot is not None:
        pr_is_object = reference_view.induced_slot(pr_identifying_slot.name, pr_descendant)
        if pr_is_object.structured_pattern is not None and pr_is_object.structured_pattern.syntax is not None:
            print(
                f"{reference_class_name}.{reference_slot_name} has range "
                f"{pr_descendant} with identifying slot {pr_identifying_slot.name} "
                f"with structured_pattern {pr_is_object.structured_pattern.syntax}")
        else:
            logger.info(
                f"{pr_descendant} has identifying slot {pr_identifying_slot.name} "
                f"but without a structured_pattern")
    else:
        logger.info(f"{pr_descendant} has no identifying slot")


@click.command()
@click.option('--schema-file', default="src/schema/nmdc.yaml", help="Path to the reference schema file.")
def main(schema_file):
    # Your existing script functions and logic here
    # Ensure your function calls and logic are indented to be included in the main function.

    """
    Main function to process the schema and extract structured patterns.

    :return: None
    """
    reference_view = SchemaView(schema_file)

    reference_classes = reference_view.all_classes()
    reference_class_names = sorted(reference_classes.keys())

    for reference_class_name in reference_class_names:
        if reference_class_name in skip_classes:
            continue
        induced_reference_class = reference_view.induced_class(reference_class_name)
        reference_slots = induced_reference_class.attributes
        reference_slot_names = sorted(reference_slots.keys())
        reference_slot_names.sort()

        for reference_slot_name in reference_slot_names:
            logger.info(f"{reference_class_name}.{reference_slot_name}")

            range_dict, range_types, ranges = get_range_dict(reference_view, reference_slot_name, reference_class_name)

            usage = reference_classes[reference_class_name].slot_usage.get(reference_slot_name)
            if usage is not None:
                handle_usage(reference_view, usage, range_dict["global_range"]["range"], range_types, ranges,
                             range_dict)

            any_ofs = reference_slots[reference_slot_name].any_of
            handle_any_of(reference_view, any_ofs, range_types, ranges, range_dict)

            range_types = set(range_types)
            if len(range_types) > 1:
                logger.info(f"    range_types = {range_types}")

            prioritized_ranges = get_prioritized_ranges(range_dict)
            process_prioritized_ranges(reference_view, prioritized_ranges, skip_classes, reference_class_name,
                                       reference_slot_name)


if __name__ == "__main__":
    main()
