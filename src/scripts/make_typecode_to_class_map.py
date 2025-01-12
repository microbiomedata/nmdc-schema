import re
from typing import Dict, List

import click
from linkml_runtime import SchemaView
from nmdc_schema.nmdc_data import get_nmdc_schema_definition

schema_view = SchemaView(get_nmdc_schema_definition())


def make_schema_class_documentation_url(class_name: str) -> str:
    r"""
    Returns the URL of the documentation for the schema class having the specified name.
    """

    base_url = "https://microbiomedata.github.io/nmdc-schema/"
    return f"{base_url}/{class_name}"


def make_document(md_table: str = "") -> str:
    r"""
    Returns a Markdown document (page) that includes the specified table.
    """

    md_header: str = r"# Typecode to class map"
    md_intro: str = (r"Schema class definitions include structured patterns that constrain the format of their `id` "
                     r"values. One element of the structured pattern is the _typecode_. The following table—which was "
                     r"derived from the schema—shows which schema class can have a given string in the _typecode_ "
                     r"portion of its `id` values.")
    md_footer: str = r""  # currently empty — it's here if we need it
    return "\n\n".join([md_header, md_intro, md_table, md_footer])


def get_typecodes_from_slot_pattern(slot_pattern: str) -> List[str]:
    r"""
    Extracts typecodes from a slot pattern; i.e., the value of the `pattern` property of a slot definition.

    >>> get_typecodes_from_slot_pattern("(nmdc):foo-...")
    []
    >>> get_typecodes_from_slot_pattern("^(nmdc):foo-...")
    ['foo']
    >>> get_typecodes_from_slot_pattern("^(nmdc):(foo|bar)-...")
    ['foo', 'bar']
    >>> get_typecodes_from_slot_pattern("^(nmdc):(foo|bar|baz)-...")
    ['foo', 'bar', 'baz']
    """
    typecodes: List[str] = []

    id_pattern = re.compile(r"^\^\(nmdc\):(.+?)-")  # the `+?` is a lazy matcher (opposite of greedy)
    match_obj = id_pattern.match(slot_pattern)
    if match_obj is not None:
        typecode_portion = match_obj.group(1)

        # Extract the typecode from a single-typecode pattern, or extract all typecodes from a multi-typecode pattern.
        if "(" not in typecode_portion:
            typecodes = [typecode_portion]
        else:
            typecodes = typecode_portion.lstrip("(").rstrip(")").split("|")

    return typecodes


@click.command()
def main():
    r"""
    Generates a Markdown document containing a table that can be used to map typecodes to schema classes.
    """

    # Initialize the data structure that will map each class name to
    # the typecode(s) that are compatible with its `id` slot.
    class_name_to_typecodes: Dict[str, List[str]] = {}

    # Iterate over all class definitions in the schema.
    all_class_defs_by_class_name = schema_view.all_classes()
    for class_name, class_def in all_class_defs_by_class_name.items():
        induced_slot_defs = schema_view.class_induced_slots(class_name)

        # Iterate over all slot definitions in this class definition.
        for slot_def in induced_slot_defs:
            slot_name = slot_def.name

            # If this slot's name is `id`, get all the typecodes — if any — from the slot definition's pattern.
            if slot_name == "id":
                typecodes = get_typecodes_from_slot_pattern(slot_def.pattern)
                if len(typecodes) > 0:
                    class_name_to_typecodes[class_name] = typecodes

    # Build the Markdown table.
    md_table_lines: List[str] = [r"| Typecode(s) | Schema class |",
                                 r"| ----------- | ------------ |"]
    for class_name, typecodes in class_name_to_typecodes.items():
        formatted_typecodes = [f"`{typecode}`" for typecode in typecodes]  # wraps each one in backticks
        typecode_cell = ", ".join(formatted_typecodes)  # if multiple exist, separates them with commas
        schema_class_documentation_url = make_schema_class_documentation_url(class_name)
        class_cell = (f'<a href="{schema_class_documentation_url}" '
                      f'target="_blank" '
                      f'title="View {class_name} documentation">'
                      f'{class_name}'
                      f'</a>')  # uses HTML instead of Markdown so we can specify the `target` attribute
        md_table_lines.append(f"| {typecode_cell} | {class_cell} |")

    # Build the entire Markdown document.
    md_document = make_document(md_table="\n".join(md_table_lines))
    print(md_document)


if __name__ == '__main__':
    main()
