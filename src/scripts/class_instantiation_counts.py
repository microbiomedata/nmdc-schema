import csv
import click
import pprint


@click.command()
@click.option('--schemasheets-input', default='../../local/usage_template.tsv',
              help='Input path for the usage template TSV.')
@click.option('--counts-input', default='../../Database-interleaved-class-count.tsv',
              help='Input path for the class count TSV.')
@click.option('--output', default='../../class_instantiation_counts.tsv', help='Output path for the resulting TSV.')
def process_data(output, schemasheets_input, counts_input):
    classes = {}

    # Read the usage_template file
    with open(schemasheets_input, 'r') as file:
        reader = csv.DictReader(file, delimiter='\t')
        for row in reader:
            if row['slot'] == "" and row['class'] != "":
                new_row_dict = {
                    'class': row['class'],
                    'class_uri': row['class_uri'],
                    'abstract': row['abstract'],
                }
                classes[row['class_uri']] = new_row_dict

    # Read the Database-interleaved-class-count file
    with open(counts_input, 'r') as file:
        # read the TSV file with dictreader. there is no header in the file
        reader = csv.DictReader(file, delimiter='\t', fieldnames=['count', 'class'])
        for row in reader:
            if row['class'] in classes:
                classes[row['class']]['count'] = row['count']

    classes_list = [v for k, v in classes.items()]

    # Write classes_list to a TSV file
    with open(output, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=classes_list[0].keys(), delimiter='\t')
        writer.writeheader()
        writer.writerows(classes_list)


if __name__ == '__main__':
    process_data()
