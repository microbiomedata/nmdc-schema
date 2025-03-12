#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Provides CLI to return versions of the NMDC Schema, meta model and pypi package."""

from importlib import metadata

import click
from .nmdc_data import get_nmdc_schema_definition


def get_nmdc_schema_package_version() -> str:
    """
    Returns the version of the nmdc_schema package.

    Returns
    -------
    str
        The version of the nmdc_schema package.
    """
    return metadata.version("nmdc_schema")


def get_nmdc_schema_version() -> str:
    """
    Returns the version specified in the nmdc.yaml file.

    Returns
    -------
    str
        The version in the nmdc.yaml file.
    """
    nmdc_schema = get_nmdc_schema_definition()
    return nmdc_schema.version


def get_nmdc_schema_metamodel_version() -> str:
    """
    Returns the metamodel version specified in the nmdc.yaml file.

    Returns
    -------
    str
        The metamodel version in the nmdc.yaml file.
    """
    nmdc_schema = get_nmdc_schema_definition()
    return nmdc_schema.metamodel_version


##### CLI interface #####
@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.option(
    "--schema/--no-schema",
    "-s/-ns",
    default=True,
    show_default=True,
    help="specifies if nmdc schema version is printed",
)
@click.option(
    "--meta/--no-meta",
    "-m/-nm",
    default=False,
    show_default=True,
    help="specifies if nmdc schema metamodel version is printed",
)
@click.option(
    "--package/--no-package",
    "-pk/-npk",
    default=False,
    show_default=True,
    help="specifies if nmdc_schema package version is printed",
)
@click.option(
    "--all/--no-all",
    "-a/-na",
    default=False,
    show_default=True,
    help="specifies if all version information is printed",
)
def cli(schema, meta, package, all):
    if all == True:
        click.echo(get_nmdc_schema_version())
        click.echo(get_nmdc_schema_metamodel_version())
        click.echo(get_nmdc_schema_package_version())
    else:
        if meta == True:
            click.echo(get_nmdc_schema_metamodel_version())
        elif package == True:
            click.echo(get_nmdc_schema_package_version())
        else:
            click.echo(get_nmdc_schema_version())


if __name__ == "__main__":
    cli()  # CLI interface
