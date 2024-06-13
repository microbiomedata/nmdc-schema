import click
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.utils.schemaview import OrderedBy


@click.command()
@click.option('--schema-file', default='src/schema/nmdc.yaml',
              help='Path to the schema file.')
def display_slot_usage(schema_file):
    """
    Display slot usage for each class in the specified LinkML schema ordered lexically.
    """
    schema_view = SchemaView(schema_file)

    # Iterate over classes ordered lexically
    for ck, cv in schema_view.all_classes(ordered_by=OrderedBy.LEXICAL).items():
        if cv.slot_usage:
            click.echo(f"{ck}:")
            click.echo(yaml_dumper.dumps(cv.slot_usage))
            click.echo()


if __name__ == '__main__':
    display_slot_usage()
