from typing import List

from nmdc_schema.get_mixs_slots import MIxSSlotsGetter
from nmdc_schema.get_slots_from_view import SchemaSlotsGetter

import click


class UsedMixsSlotsGetter:
    mixs_term_getter: MIxSSlotsGetter = MIxSSlotsGetter()
    mixs_slotnames: List[str] = mixs_term_getter.get_unique_slot_names()

    schema_slots_getter: SchemaSlotsGetter = SchemaSlotsGetter()
    schema_slots: List[str] = schema_slots_getter.get_schema_slots()

    def get_used_mixs_slots(self) -> List[str]:
        used_mixs_slots = list(set(self.mixs_slotnames) & set(self.schema_slots))
        used_mixs_slots.sort()
        return used_mixs_slots


@click.command()
@click.option('--output_file',
              '-o',
              type=click.File('w'),
              required=True,
              help='Your output will be written as a single-column TSV file.')
def main(output_file):
    used_mixs_slot_getter = UsedMixsSlotsGetter()
    used_mixs_slots = used_mixs_slot_getter.get_used_mixs_slots()

    with output_file:
        for slot in used_mixs_slots:
            output_file.write(f"{slot}\n")

    click.echo(f"The result has been written to {output_file.name}")


if __name__ == '__main__':
    main()
