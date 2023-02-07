from typing import List

from nmdc_schema.get_mixs_slots import MIxSSlotsGetter
from nmdc_schema.get_slots_from_view import SchemaSlotsGetter

import click


class IntersectionMixsSlotsGetter:
    mixs_term_getter: MIxSSlotsGetter = MIxSSlotsGetter()
    mixs_slotnames: List[str] = mixs_term_getter.get_unique_slot_names()
    slot_list = []

    def get_intersection_mixs_slots(self, slot_list_file) -> List[str]:
        print(f"slot_list_file: {slot_list_file}")
        with open(slot_list_file, 'r') as file:
            self.slot_list = [line.strip().split('\t')[0] for line in file]

        used_mixs_slots = list(set(self.mixs_slotnames) & set(self.slot_list))
        used_mixs_slots.sort()
        return used_mixs_slots


@click.command()
@click.option('--slot_list_file',
              '-s',
              type=click.Path(exists=True),
              required=True,
              help='Provide a single-column TSV file listing desired slots.')
@click.option('--output_file',
              '-o',
              type=click.File('w'),
              required=True,
              help='Your output will be written as a single-column TSV file.')
def main(slot_list_file, output_file):
    print(f"slot_list_file: {slot_list_file}")
    print(f"output_file: {output_file}")

    intersection_mixs_slot_getter = IntersectionMixsSlotsGetter()
    intersection_mixs_slots = intersection_mixs_slot_getter.get_intersection_mixs_slots(slot_list_file)

    with output_file:
        for slot in intersection_mixs_slots:
            output_file.write(f"{slot}\n")

    click.echo(f"The result has been written to {output_file.name}")


if __name__ == '__main__':
    main()
