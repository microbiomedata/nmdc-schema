import csv
import click


class ImportSlotsRegardless:

    def __init__(self, mixs_schema_url, slots_tsv):
        self.static_value_dict = {
            "source class": "soil MIMS",
            "source file or URL": mixs_schema_url,
            "slot": "",
            "section": "",
            "column order": "",
            "destination class": "placeholder_class"
        }

        self.mixs_slots_used_in_schema_tsv = slots_tsv
        self.mixs_slots_used_in_schema = list()

    def populate_mixs_slots_used_in_schema(self, input_file):
        with open(input_file, 'r') as file:
            self.mixs_slots_used_in_schema = [line.strip().split('\t')[0] for line in file]

    def make_import_slots_regardless_rows(self, input_file):
        self.populate_mixs_slots_used_in_schema(input_file)
        import_slots_regardless_rows = list()

        for slot in self.mixs_slots_used_in_schema:
            final_dict = self.static_value_dict.copy()
            final_dict["slot"] = slot
            import_slots_regardless_rows.append(final_dict)

        return import_slots_regardless_rows

    def write_import_slots_regardless_rows(self, output_file, input_file):
        fieldnames = list(self.static_value_dict.keys())
        slots_regardless_rows = self.make_import_slots_regardless_rows(input_file)
        with open(output_file, 'w', newline='') as output_file:
            writer = csv.DictWriter(output_file, fieldnames=fieldnames, delimiter='\t')
            writer.writeheader()
            for row in slots_regardless_rows:
                writer.writerow(row)


@click.command()
@click.option("--input_file", required=True, help="input file path from get-mixs-slots-used-in-schema")
@click.option("--output_file", required=True, help="output file path for sheets_and_friends")
@click.option("--slots-tsv", default="assets/mixs_slots_used_in_schema.tsv")
@click.option("--mixs-schema-url",
              default="https://raw.githubusercontent.com/microbiomedata/mixs/1da849346a80b717810a02d7c8ed74a22bcd84de/model/schema/mixs.yaml")
def main(output_file, input_file, slots_tsv, mixs_schema_url):
    import_slots = ImportSlotsRegardless(mixs_schema_url=mixs_schema_url, slots_tsv=slots_tsv)
    import_slots.write_import_slots_regardless_rows(output_file, input_file)
    click.echo("Import slots regardless file generated successfully.")


if __name__ == '__main__':
    main()
