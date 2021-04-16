#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pkgutil, pkg_resources, io, click, yaml


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
    nmdc_dict = get_nmdc_dict()
    return nmdc_dict["version"]


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
    "--package/--no-package",
    "-pk/-npk",
    default=False,
    show_default=True,
    help="specifies if nmdc_schema package version is printed; default false",
)
def cli(schema, package):
    if schema == True:
        click.echo(get_nmdc_schema_version())
    if package == True:
        click.echo(get_nmdc_schema_package_version())


if __name__ == "__main__":
    cli()  # CLI interface