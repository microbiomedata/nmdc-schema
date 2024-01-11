import pandas as pd
import click

COLUMN_MAPPINGS = {
    "ECOSYSTEM CATEGORY": "EcosystemCategoryEnum",
    "ECOSYSTEM SUBTYPE": "EcosystemSubtypeEnum",
    "ECOSYSTEM TYPE": "EcosystemTypeEnum",
    "ECOSYSTEM": "EcosystemEnum",
    "SPECIFIC ECOSYSTEM": "SpecificEcosystemEnum",
}


def read_excel(input_file):
    return pd.read_excel(input_file, engine="openpyxl")


def generate_rows(df):
    rows = []
    columns = list(set(df.columns) - set(["ECOSYSTEM PATH ID"]))
    # columns = list(df.columns - {"ECOSYSTEM PATH ID"})

    for col in columns:
        destination = COLUMN_MAPPINGS[col]
        values = df[col].unique()

        for value in values:
            row = {
                "DH pulldown column": destination,
                "DH pulldown option": value
            }
            rows.append(row)

    return rows


@click.command()
@click.option('-i', '--input-file', type=click.Path(exists=True), required=True,
              default='../../assets/GOLDs5levelEcosystemClassificationPaths.xlsx')
@click.option('-o', '--output-file', type=click.Path(), required=True,
              default='../../assets/gold_ecosystem_path_enumerations.tsv')
def main(input_file, output_file):
    print(f'Reading input file {input_file}')
    df = read_excel(input_file)

    print('Generating output rows')
    rows = generate_rows(df)

    print(f'Writing output to {output_file}')
    pd.DataFrame(rows).to_csv(output_file, index=False, sep='\t')

    print('Done!')


if __name__ == "__main__":
    main()
