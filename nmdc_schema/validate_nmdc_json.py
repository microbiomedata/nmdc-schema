#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Provides CLI to validate json files against the NMDC jsonschema.

This is now deprecated by either

- linkml-run-examples (which doesn't require it's input to be wrapped in a Database but doesn't exhaustively report errors.
- check-jsonschema (which does require it's input to be wrapped in a Database and does exhaustively report errors.)
"""

import json, jsonschema, click
from .nmdc_data import get_nmdc_jsonschema, get_nmdc_jsonschema_dict
from deprecated import deprecated


@deprecated(
    reason="functionality moved to nmdc_data.get_nmdc_jsonschema_dict()"
)
def get_nmdc_schema() -> dict:
    """
    Returns the nmdc.schema.json package data file as a dict.
    NOTE: This method is depricated. Should use nmdc_data.get_nmdc_jsonschema_dict()

    Returns
    -------
    dict
        Dict representation of the nmdc.schema.json package data file.
    """
    return get_nmdc_jsonschema_dict()


@deprecated(reason="functionality moved to nmdc_data.get_nmdc_jsonschema()")
def get_nmdc_schema_json() -> str:
    """
    Returns the nmdc.schema.json package data file json.
    NOTE: This method is depricated. Should use nmdc_data.get_nmdc_jsonschema()

    Returns
    -------
    str
        JSON string representation of the nmdc.schema.json package data file.
    """
    return get_nmdc_jsonschema()


def is_valid_json(json_file: str, database_set: str = "") -> bool:
    """
    Determines if the data in json_file conforms to the NMDC json schema.

    Parameters
    ----------
    json_file : str
        Path to the file containing json formatted data.
    database_set : str, default=""
        An optional top level database set (e.g, study_set, biosample_set) that contains the data.

    Returns
    -------
    bool
        True if data conforms to the NMDC json schema; False otherwise.
    """
    with open(json_file, "r") as fh:
        json_data = json.load(fh)

        database_set = database_set.strip()
        if len(database_set) > 0:
            if type(json_data) == type([]):
                json_data = {f"{database_set}": json_data}
            else:
                json_data = {f"{database_set}": [json_data]}
    try:
        jsonschema.validate(
            instance=json_data, schema=get_nmdc_jsonschema_dict()
        )
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
@click.option(
    "--database-set",
    "-set",
    default="",
    help="An optional top level database set (e.g, study_set, biosample_set) that contains the data.",
)
def cli(input: str, database_set: str):
    if is_valid_json(input, database_set):
        click.echo("%s: The JSON data is VALID for NMDC schema." % input)
    else:
        click.echo(
            "%s: The JSON data is ** NOT ** valid for NMDC schema." % input
        )


if __name__ == "__main__":
    cli()  # CLI interface
