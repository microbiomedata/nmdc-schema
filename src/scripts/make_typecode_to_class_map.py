from typing import List, Tuple

import click
from linkml_runtime import SchemaView

from nmdc_schema.nmdc_data import get_nmdc_schema_definition
from nmdc_schema.id_helpers import get_class_name_to_typecode_map


DATABASE_CLASS_NAME = "Database"
_schema_view: SchemaView | None = None


def get_schema_view() -> SchemaView:
    r"""
    Returns a lazily-initialized `SchemaView` for the NMDC schema.

    Initializing at first use, rather than at import time, keeps importing this
    module cheap and side-effect-free (which helps testing) and defers loading
    the schema until it is actually needed.
    """
    global _schema_view
    if _schema_view is None:
        _schema_view = SchemaView(get_nmdc_schema_definition())
    return _schema_view


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
                     r"portion of its `id` values, and which collections can contain instances of that schema class.")
    md_footer: str = r""  # currently empty — it's here if we need it
    return "\n\n".join(part for part in [md_header, md_intro, md_table, md_footer] if part)


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
    first_typecode = typecodes[0] if typecodes else ""
    return first_typecode


def get_collection_names_for_class_name(class_name: str) -> List[str]:
    r"""
    Returns the names of the collection(s) the schema says can contain instances of the specified class.

    Note: In the schema, each `multivalued`, `inlined_as_list` slot of the `Database` class represents a collection.
          Each such slot has a range indicated by its `range` attribute. The _effective_ range of the slot consists of
          both (a) the class identified by its `range` attribute and (b) all descendant classes of that class.

    >>> get_collection_names_for_class_name("")  # empty string
    []
    >>> get_collection_names_for_class_name("NonExistentClass")  # non-existent class
    []
    >>> get_collection_names_for_class_name("Study")  # class having no descendants
    ['study_set']
    >>> get_collection_names_for_class_name("DataGeneration")  # class having some descendants
    ['data_generation_set']
    >>> get_collection_names_for_class_name("NucleotideSequencing")
    ['data_generation_set']
    >>> get_collection_names_for_class_name("MassSpectrometry")
    ['data_generation_set']
    """
    collection_names_for_class_name = []
    schema_view = get_schema_view()

    # Process each slot of the "Database" class.
    for slot_name in schema_view.class_slots(class_name=DATABASE_CLASS_NAME):
        slot_definition = schema_view.induced_slot(slot_name, class_name=DATABASE_CLASS_NAME)

        # If this slot represents a collection, check whether the specified class is within the slot's range.
        if slot_definition.multivalued and slot_definition.inlined_as_list:
            slot_range = slot_definition.range
            if not slot_range:
                continue
            class_names_in_slot_range = schema_view.class_descendants(class_name=slot_range)
            if class_name in class_names_in_slot_range:
                collection_names_for_class_name.append(slot_name)

    return collection_names_for_class_name


@click.command()
def main():
    r"""
    Generates a Markdown document containing a table that can be used to map typecodes to schema classes.
    """

    # Get a dictionary that maps the name of each class defined in the schema to a list of all of
    # the typecodes that are compatible with the `id` slot of the class.
    all_class_name_to_typecodes = get_class_name_to_typecode_map()

    # Filter out the names of classes that lack typecodes, given that the table we will be rendering
    # is designed to be a "typecode-to-(something)" map, not a "(something)-to-typecode" map.
    class_name_to_typecodes = {c: t for c, t in all_class_name_to_typecodes.items() if len(t) > 0}

    # Build the Markdown table.
    md_table_lines: List[str] = [r"| Typecode(s) | Schema class | Collection name(s) |",
                                 r"| ----------- | ------------ | ------------------ |"]
    for class_name, compatible_typecodes in sorted(class_name_to_typecodes.items(), key=extract_comparison_key):
        formatted_typecodes = [f"`{typecode}`" for typecode in compatible_typecodes]  # wraps each one in backticks
        typecode_cell = ", ".join(formatted_typecodes)  # if multiple exist, separates them with commas
        schema_class_documentation_url = make_schema_class_documentation_url(class_name)
        class_cell = (f'<a href="{schema_class_documentation_url}" '
                      f'target="_blank" '
                      f'title="View {class_name} documentation">'
                      f'{class_name}'
                      f'</a>')  # uses HTML instead of Markdown so we can specify the `target` attribute
        collection_names = get_collection_names_for_class_name(class_name)
        formatted_collection_names = [f"`{collection_name}`" for collection_name in collection_names]
        collection_cell = ", ".join(formatted_collection_names)  # if multiple exist, separates them with commas
        md_table_lines.append(f"| {typecode_cell} | {class_cell} | {collection_cell} |")

    # Build the entire Markdown document.
    md_document = make_document(md_table="\n".join(md_table_lines))
    print(md_document)


if __name__ == '__main__':
    main()
