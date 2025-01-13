from typing import Dict, List, Tuple

import click
from linkml_runtime import SchemaView
from nmdc_schema.nmdc_data import get_nmdc_schema_definition
from nmdc_schema.id_helpers import get_typecodes_compatible_with_existing_ids

schema_view = SchemaView(get_nmdc_schema_definition())


def make_schema_class_documentation_url(class_name: str) -> str:
    r"""
    Returns the URL of the documentation for the schema class having the specified name.

    >>> make_schema_class_documentation_url("Foo")
    'https://microbiomedata.github.io/nmdc-schema/Foo'
    """

    base_url = "https://microbiomedata.github.io/nmdc-schema"  # lacks trailing slash
    return f"{base_url}/{class_name}"


def make_document(md_table: str = "") -> str:
    r"""
    Returns a Markdown document (page) that includes the specified table.

    >>> isinstance(make_document(), str)
    True
    """

    md_header: str = r"# Typecode to class map"
    md_intro: str = (r"Schema class definitions include structured patterns that constrain the format of their `id` "
                     r"values. One element of the structured pattern is the _typecode_. The following table—which was "
                     r"derived from the schema—shows which schema class can have a given string in the _typecode_ "
                     r"portion of its `id` values.")
    md_footer: str = r""  # currently empty — it's here if we need it
    return "\n\n".join([md_header, md_intro, md_table, md_footer])


def extract_comparison_key(class_name_and_typecodes: Tuple[str, List[str]]) -> str:
    r"""
    Helper function used to extract a comparison key from a tuple, for use with `sorted(key=...)`.

    >>> extract_comparison_key(("MyClass", []))
    ''
    >>> extract_comparison_key(("MyClass", ['foo']))
    'foo'
    >>> extract_comparison_key(("MyClass", ['bar', 'foo']))
    'bar'
    """
    class_name, typecodes = class_name_and_typecodes
    first_typecode = typecodes[0] if len(typecodes) > 0 else ""
    return first_typecode


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
                typecodes = get_typecodes_compatible_with_existing_ids(slot_def.pattern)
                if len(typecodes) > 0:
                    sorted_typecodes = sorted(typecodes)
                    class_name_to_typecodes[class_name] = sorted_typecodes

    # Build the Markdown table.
    md_table_lines: List[str] = [r"| Typecode(s) | Schema class |",
                                 r"| ----------- | ------------ |"]
    for class_name, typecodes in sorted(class_name_to_typecodes.items(), key=extract_comparison_key):
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
