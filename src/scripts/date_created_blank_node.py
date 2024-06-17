import click
from datetime import datetime


@click.command()
def print_timestamp():
    current_datetime = datetime.utcnow().replace(microsecond=0).isoformat()
    output = f"""

[ ] <https://schema.org/dateCreated> "{current_datetime}"^^<http://www.w3.org/2001/XMLSchema#dateTime> ;
    <http://www.w3.org/2000/01/rdf-schema#comment> "https://api.microbiomedata.org" . 
"""
    click.echo(output)


if __name__ == '__main__':
    print_timestamp()
