#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pkgutil, json, jsonschema, io, click


def get_nmdc_schema() -> dict:
    """
    Returns the nmdc.schema.json package data file as a dict.

    Returns
    -------
    dict
        Dict representation of the nmdc.schema.json package data file.
    """
    nmdc_schema = io.BytesIO(pkgutil.get_data("nmdc_schema", "nmdc.schema.json"))
    return json.load(nmdc_schema)


def is_valid_json(json_file: str) -> bool:
    """
    Determines if the data in json_file conforms to the NMDC json schema.

    Parameters
    ----------
    json_file : str
        Path to the file containing json formatted data.

    Returns
    -------
    bool
        True if data conforms to the NMDC json schema; False otherwise.
    """
    with open(json_file, "r") as fh:
        json_data = json.load(fh)
    try:
        jsonschema.validate(instance=json_data, schema=get_nmdc_schema())
    except jsonschema.exceptions.ValidationError as err:
        print(err.message)
        return False

    return True


##### CLI interface #####
@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.option(
    "--input",
    "-i",
    help="the path the file containing json formatted data.",
)
def cli(input: str):
    if is_valid_json(input):
        click.echo("%s: The JSON data is VALID for NMDC schema." % input)
    else:
        click.echo("%s: The JSON data is ** NOT ** valid for NMDC schema." % input)


if __name__ == "__main__":
    cli()  # CLI interface
