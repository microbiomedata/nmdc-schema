import pprint
from typing import List

import click

from nmdc_schema.get_nmdc_view import ViewGetter


class ClassSlotsGetter:
    @staticmethod
    def get_class_slots(class_name) -> List[str]:
        # assumes user wants slots from induced class
        # if the user adds a MIxS slot to class Biosample, will the view be created?
        # might need a pure YAML solution
        # or user could just add slot name to ???
        # most importantly, this get the view from nmdc_schema,nmdc_schema_merged.yaml
        # which won't include the user's changes!!!
        view_getter = ViewGetter()
        nmdc_view = view_getter.get_view()
        nmdc_class = nmdc_view.induced_class(class_name)
        class_slots = nmdc_class.attributes

        class_slot_names = [v.name for k, v in class_slots.items()]
        class_slot_names.sort()
        return class_slot_names


@click.command()
@click.option('--output_file',
              '-o',
              type=click.File('w'),
              required=True,
              help='Your output will be written as a single-column TSV file.')
@click.option('--class_name',
              '-c',
              required=True,
              help='For what class do you want to retrieve slots?.')
def main(output_file, class_name):
    class_slot_getter = ClassSlotsGetter()
    class_used_slots = class_slot_getter.get_class_slots(class_name)

    with output_file:
        for slot in class_used_slots:
            output_file.write(f"{slot}\n")

    click.echo(f"The result has been written to {output_file}")


if __name__ == '__main__':
    main()
