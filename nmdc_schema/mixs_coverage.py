import csv
import click
from typing import List, Dict


@click.command()
@click.option('--in_file', default='assets/sheets-for-nmdc-submission-schema_import_slots_regardless.tsv',
              help='Full path to sheets-for-nmdc-submission-schema_import_slots_regardless.tsv including filename',
              type=str, required=True)
@click.option('--out_file', required=True, help='Output file path', type=str)
def cli(in_file: str, out_file: str):
    with open(in_file, "r") as f:
        reader = csv.DictReader(f, delimiter="\t")
        min_list = [
            {"slot": row["slot"], "destination class": dc}
            for row in reader
            for dc in row["destination class"].split("|")
        ]

    with open(out_file, "w") as f:
        writer = csv.DictWriter(f, fieldnames=['slot', 'destination class'], delimiter="\t")
        writer.writeheader()
        writer.writerows(min_list)


if __name__ == '__main__':
    cli()
