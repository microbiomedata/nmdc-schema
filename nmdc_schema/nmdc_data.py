#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contains methods for retrieving embedded data from the nmdc-schema library."""

import io
import json
import pkgutil
from os.path import getatime
from typing import Dict, List, Optional
from enum import Enum

import click
import yaml
from linkml.utils.rawloader import load_raw_schema
from linkml_runtime.linkml_model.meta import SchemaDefinition
from linkml_runtime.utils.schemaview import SchemaView


class SchemaVariantIdentifier(str, Enum):
    r"""
    Identifiers of schema variants.

    >>> type(SchemaVariantIdentifier.nmdc_materialized_patterns) is SchemaVariantIdentifier
    True
    >>> "nmdc_materialized_patterns" == SchemaVariantIdentifier.nmdc_materialized_patterns
    True
    >>> type(SchemaVariantIdentifier.nmdc_materialized_patterns.value) is str
    True
    >>> "nmdc_materialized_patterns" == SchemaVariantIdentifier.nmdc_materialized_patterns.value
    True
    """

    nmdc_materialized_patterns = "nmdc_materialized_patterns"


def get_nmdc_yaml_bytesIO() -> io.BytesIO:
    """Returns the nmdc.yaml file as bytes steam.
    This function is not intended to be used directly, but it used by other functions

    Returns
    -------
    BytesIO
        A bytes stream of nmdc.yaml file.
    """
    # get nmdc.yaml file from the package data
    return io.BytesIO(pkgutil.get_data(__name__, "nmdc_materialized_patterns.yaml"))


def get_nmdc_yaml_bytes() -> bytes:
    """Reruns the nmdc.yaml file as bytes.

    Returns
    -------
    bytes
        The bytes of the nmdc.yaml file.
    """
    nmdc_yaml = get_nmdc_yaml_bytesIO()
    return nmdc_yaml.getvalue()


def get_nmdc_yaml_string() -> str:
    """Reruns the nmdc.yaml file as a string.

    Returns
    -------
    str
        A string containing the contents of nmdc.yaml file.
    """
    nmdc_yaml = get_nmdc_yaml_bytes()
    return nmdc_yaml.decode("utf-8")


def get_materialized_nmdc_yaml_string():
    materialized_nmdc_bytes_io = io.BytesIO(pkgutil.get_data(__name__, "nmdc_materialized_patterns.yaml"))
    materialized_nmdc_yaml_bytes = materialized_nmdc_bytes_io.getvalue()
    materialized_nmdc_yaml_string = materialized_nmdc_yaml_bytes.decode("utf-8")
    return materialized_nmdc_yaml_string


def get_nmdc_jsonschema_bytesIO(variant: Optional[SchemaVariantIdentifier] = None) -> io.BytesIO:
    """Returns the nmdc.schema.json file as bytes steam.
    This function is not intended to be used directly, but it used by other functions

    Returns
    -------
    BytesIO
        A bytes stream of nmdc.schema.json file.

    >>> stream_a = get_nmdc_jsonschema_bytesIO()
    >>> type(stream_a) is io.BytesIO
    True
    >>> stream_b = get_nmdc_jsonschema_bytesIO(variant=SchemaVariantIdentifier.nmdc_materialized_patterns)
    >>> type(stream_b) is io.BytesIO
    True
    """

    # Determine which JSON Schema file we will use.
    file_name = "nmdc.schema.json"
    if variant == SchemaVariantIdentifier.nmdc_materialized_patterns:
        file_name = "nmdc_materialized_patterns.schema.json"

    return io.BytesIO(pkgutil.get_data(__name__, file_name))


def get_nmdc_jsonschema_bytes(variant: Optional[SchemaVariantIdentifier] = None) -> bytes:
    """Returns the nmdc.schema.json file as bytes.

    Returns
    -------
    bytes
        The bytes of the nmdc.schema.json file.

    >>> bytes_a = get_nmdc_jsonschema_bytes()
    >>> type(bytes_a) is bytes and b"version" in bytes_a
    True
    >>> bytes_b = get_nmdc_jsonschema_bytes(variant=SchemaVariantIdentifier.nmdc_materialized_patterns)
    >>> type(bytes_b) is bytes and b"version" in bytes_b
    True
    >>> len(bytes_b) > len(bytes_a)  # assumes that including structured patterns makes the file larger
    True
    """
    nmdc_json = get_nmdc_jsonschema_bytesIO(variant=variant)
    return nmdc_json.getvalue()


def get_nmdc_jsonschema_string(variant: Optional[SchemaVariantIdentifier] = None) -> str:
    """Reruns the nmdc.schema.json file as a string.

    Returns
    -------
    str
        A string containing the contents of nmdc.schema.json file.

    >>> str_a = get_nmdc_jsonschema_string()
    >>> type(str_a) is str and "version" in str_a
    True
    >>> str_b = get_nmdc_jsonschema_string(variant=SchemaVariantIdentifier.nmdc_materialized_patterns)
    >>> type(str_b) is str and "version" in str_b
    True
    >>> len(str_b) > len(str_a)  # assumes that including structured patterns makes the file larger
    True
    """
    nmdc_json = get_nmdc_jsonschema_bytes(variant=variant)
    return nmdc_json.decode("utf-8")


def get_nmdc_jsonschema_dict(variant: Optional[SchemaVariantIdentifier] = None) -> Dict:
    """Parses the nmdc.schema.json file into a dict.

    Returns
    -------
    dict
        The dict of the keys and value in the nmdc.schema.json file.

    >>> dict_a = get_nmdc_jsonschema_dict()
    >>> type(dict_a) is dict and "version" in dict_a.keys()
    True
    >>> dict_b = get_nmdc_jsonschema_dict(variant=SchemaVariantIdentifier.nmdc_materialized_patterns)
    >>> type(dict_b) is dict and "version" in dict_b.keys()
    True
    """
    nmdc_json = get_nmdc_jsonschema_bytes(variant=variant)
    return json.loads(nmdc_json)


def get_nmdc_jsonschema(variant: Optional[SchemaVariantIdentifier] = None) -> str:
    """
    Returns the NMDC jsonschema (nmdc.schema.json) as json.

    Returns
    -------
    str
        JSON string representation of the NMDC jsonschema (nmdc.schema.json).
    """
    nmdc_schema = get_nmdc_jsonschema_dict(variant=variant)
    return json.dumps(nmdc_schema, indent=2)


def get_nmdc_schema_definition() -> SchemaDefinition:
    """Returns a LinkML SchemaDefinition object created from the nmdc.yaml file.

    Returns
    -------
    SchemaDefinition
        A SchemaDefinition object created from nmdc.yaml file.
    """
    nmdc_yaml = get_nmdc_yaml_string()
    return load_raw_schema(nmdc_yaml)


def get_nmdc_file_type_enums() -> List[Dict[str, str]]:
    """Returns list of dicts with information about each NMDC file enums.
    Each dict in the list has the key/values:
    {
        name: the name of the enum
        description: the description of the enum
        file_name_pattern: the pattern for the file type or None if not present
    }

    Returns
    -------
    List[Dict[str, str]]
    List of dicts with information about each NMDC file enum.
    """
    schema = get_nmdc_schema_definition()
    file_enums = schema.enums["FileTypeEnum"].permissible_values  # returns a dict

    # todo: report error
    # view = SchemaView(schema)
    # file_enums = view.get_enum("file type enum").permissible_values  # returns a dict

    # create list of objects with info about each file type enum
    enum_objs = []
    for key, permissible_val in file_enums.items():
        obj = {"name": key}
        # obj = {"name": permissible_val.text}
        obj["description"] = permissible_val.description

        # not every file type enum will have a file name pattern
        file_name_pattern = permissible_val.annotations.get("file_name_pattern", None)
        if file_name_pattern:
            obj["file_name_pattern"] = file_name_pattern.value
        else:
            obj["file_name_pattern"] = None

        enum_objs.append(obj)

    return enum_objs


def get_nmdc_file_type_enums_json() -> str:
    """Returns information about the file type enums as json.
    Each object contains the following key/values:
    {
        name: the name of the enum
        description: the description of the enum
        file_name_pattern: the pattern for the file type or null if not present
    }
    Note: Calls get_nmdc_file_type_enums() to fetch information.

    Returns
    -------
    str
        JSON formatted string of file type enum information.getatime
    """
    file_enums = get_nmdc_file_type_enums()
    return json.dumps(file_enums, indent=2)


def get_gold_sssom() -> str:
    """Returns the gold-to-mixs.sssom.tsv file from package.

    Returns
    -------
    str
        the gold-to-mixs.sssom.tsv file
    """
    sssom = io.BytesIO(pkgutil.get_data(__name__, "gold-to-mixs.sssom.tsv"))
    return sssom.getvalue().decode("utf-8")


##### CLI interface #####
@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.option(
    "--fetch",
    "-f",
    default="",
    help="""\b
    Fetches the specified data file from the nmdc-schema library.
    Only one argument is permitted.
    \b
    fetch arguments:
    yaml            returns the merged nmdc.yaml file as a string
    jsonschema      returns the NMDC jsonschema as json
    dict            returns the NMDC jsonschema as a dict
    schemadef       returns the LinkML SchemaDefinition created from the merged nmdc.yaml file
    filetypeenums   returns information about the NMDC file type enums as json
    goldsssom       returns the gold-to-mixs.sssom.tsv file contents
    """,
)
@click.pass_context
# def cli(ctx, as_yaml, as_json, as_bytes):
def cli(ctx, fetch):
    if "yaml" == fetch:
        click.echo(get_nmdc_yaml_string())
    elif "bytes" == fetch:
        click.echo(get_nmdc_yaml_bytes())
    elif "jsonschema" == fetch:
        click.echo(get_nmdc_jsonschema())
    elif "dict" == fetch:
        click.echo(get_nmdc_jsonschema_dict())
    elif "schemadef" == fetch:
        click.echo(get_nmdc_schema_definition())
    elif "filetypeenums" == fetch:
        click.echo(get_nmdc_file_type_enums_json())
    elif "goldsssom" == fetch:
        click.echo(get_gold_sssom())
    else:
        click.echo(ctx.get_help())


if __name__ == "__main__":
    cli()  # CLI interface
