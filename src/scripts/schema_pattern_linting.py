import click
import pprint
import re

from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.utils.schemaview import OrderedBy
from linkml_runtime.linkml_model.meta import EnumDefinition

DEFAULT_MIXS_SOURCE_PATH = "https://raw.githubusercontent.com/microbiomedata/nmdc-schema/main/src/schema/mixs.yaml"


@click.command()
@click.option('--schema-file', default='src/schema/nmdc.yaml', help='Path to schema file.')
@click.option(
    '--mixs-source-path',
    default=DEFAULT_MIXS_SOURCE_PATH,
    help='MIxS schema identifier to treat as the source (compared to element.from_schema) when filtering reports.',
)
def main(schema_file, mixs_source_path):
    schema_view = SchemaView(schema_file)

    schema_slots = schema_view.all_slots(ordered_by=OrderedBy.LEXICAL)

    print("Report of slots that aren't associated with any classes:\n")
    for sk, sv in schema_slots.items():
        classes_for_slot = schema_view.get_classes_by_slot(sv)
        if len(classes_for_slot) == 0:
            slot_uri_suffix = f", {sv.slot_uri}" if sv.slot_uri else ""
            slot_children = schema_view.slot_children(sk)
            slot_children_prefix = "parent " if len(slot_children) > 0 else ""
            print(f"No classes for {slot_children_prefix}slot {sk}{slot_uri_suffix}")
    print("\n")

    print("Report of enums that aren't associated with any slots:\n")
    schema_enums = schema_view.all_enums()
    for ek, ev in schema_enums.items():
        slots_for_enum = schema_view.get_slots_by_enum(ek)
        if len(slots_for_enum) == 0:
            print(f"No slots for {ek}")
    print("\n")

    print("Report of all types. Manual review recommended:\n")
    schema_types = schema_view.all_types()
    pprint.pprint(list(schema_types.keys()))
    print("\n")

    schema_elements = schema_view.all_elements()

    whitespace_keys = [key for key in schema_elements.keys() if any(char.isspace() for char in key)]

    print("Report of all elements whose names contain whitespace:\n")
    for wsk in whitespace_keys:
        wse = schema_view.get_element(wsk)

        if isinstance(wse, EnumDefinition):
            wse.permissible_values = None

        if wse.from_schema != mixs_source_path:
            print(yaml_dumper.dumps(wse))
    print("\n")

    print("Report of subsets usage:\n")
    declared_subsets = []
    subsets = schema_view.all_subsets()
    for sbk, sbv in subsets.items():
        if sbv.from_schema != mixs_source_path:
            declared_subsets.append(sbk)

    subset_usage = {}
    for ds in declared_subsets:
        subset_usage[ds] = []

    for ek, ev in schema_elements.items():
        if ev.in_subset:
            for subset in ev.in_subset:
                if subset in declared_subsets:
                    subset_usage[subset].append(ev.name)

    pprint.pprint(subset_usage)
    print("\n")

    print("Report of patterns with candidate unescaped literal dots:\n")
    print(
        "(a bare '.' between word characters, outside character classes; usually a CURIE "
        "prefix such as 'insdc.sra:' that should be written '\\.' so it is not a wildcard)\n"
    )

    def has_unescaped_prefix_dot(pattern_string):
        # Drop character-class spans, where '.' is already a literal.
        # Handle empty classes explicitly, then non-empty classes.
        cleaned = re.sub(r'\[\]', '', pattern_string)
        cleaned = re.sub(r'\[[^\]]+\]', '', cleaned)
        # A dot flanked by word characters; an escaped dot ('\\.') has a backslash
        # immediately before it, so the preceding character is not a word character.
        return re.search(r'[A-Za-z0-9]\.[A-Za-z0-9]', cleaned) is not None

    def patterns_of(slot_definition):
        found = []
        if slot_definition.pattern:
            found.append(slot_definition.pattern)
        if slot_definition.structured_pattern and slot_definition.structured_pattern.syntax:
            found.append(slot_definition.structured_pattern.syntax)
        return found

    seen_patterns = set()
    class_names = list(schema_view.all_classes().keys())
    all_slot_names = set(schema_slots.keys())
    seen_slot_groups = set()
    dangling_slot_group_messages = []
    for class_name in class_names:
        induced_slots = schema_view.class_induced_slots(class_name)
        for slot in induced_slots:
            for pattern_string in patterns_of(slot):
                key = (slot.name, pattern_string)
                if key in seen_patterns:
                    continue
                if has_unescaped_prefix_dot(pattern_string):
                    seen_patterns.add(key)
                    print(f"slot {slot.name} (in class {class_name}): {pattern_string}")
        for slot in induced_slots:
            if slot.slot_group and slot.slot_group not in all_slot_names:
                key = (class_name, slot.name, slot.slot_group)
                if key in seen_slot_groups:
                    continue
                seen_slot_groups.add(key)
                dangling_slot_group_messages.append(
                    f"class {class_name}, slot {slot.name}: slot_group '{slot.slot_group}' is not a defined slot"
                )
    for sk, sv in schema_slots.items():
        for pattern_string in patterns_of(sv):
            key = (sk, pattern_string)
            if key in seen_patterns:
                continue
            if has_unescaped_prefix_dot(pattern_string):
                seen_patterns.add(key)
                print(f"slot {sk}: {pattern_string}")
    print("\n")

    print("Report of dangling slot_group references (slot_group value is not a defined slot):\n")
    for message in dangling_slot_group_messages:
        print(message)
    print("\n")


if __name__ == '__main__':
    main()
