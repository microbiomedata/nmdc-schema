#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pkgutil, pkg_resources, io, click, yaml
from linkml.utils.rawloader import load_raw_schema


def get_nmdc_dict() -> dict:
    """
    Parses the nmdc.yaml file into a dict.

    Returns
    -------
    dict
        The dict of the keys and value in the nmdc.yaml file.
    """
    # get nmdc.yaml file from the package data
    nmdc_yaml = io.BytesIO(pkgutil.get_data("nmdc_schema", "nmdc.yaml"))

    # convert yaml to dict
    nmdc_dict = yaml.load(nmdc_yaml, Loader=yaml.CLoader)

    # return dict
    return nmdc_dict


def get_nmdc_schema_package_version() -> str:
    """
    Returns the version of the nmdc_schema package.

    Returns
    -------
    str
        The version of the nmdc_schema package.
    """
    return pkg_resources.get_distribution("nmdc_schema").version


def get_nmdc_schema_version() -> str:
    """
    Returns the version specified in the nmdc.yaml file.

    Returns
    -------
    str
        The version in the nmdc.yaml file.
    """
    nmdc_yaml = io.BytesIO(pkgutil.get_data("nmdc_schema", "nmdc.yaml"))
    nmdc_schema = load_raw_schema(nmdc_yaml)
    return nmdc_schema.version


def get_nmdc_schema_metamodel_version() -> str:
    """
    Returns the metamodel version specified in the nmdc.yaml file.

    Returns
    -------
    str
        The metamodel version in the nmdc.yaml file.
    """
    nmdc_yaml = io.BytesIO(pkgutil.get_data("nmdc_schema", "nmdc.yaml"))
    nmdc_schema = load_raw_schema(nmdc_yaml)
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