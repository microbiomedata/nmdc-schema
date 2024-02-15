import re
from pathlib import Path
from functools import wraps

import click

# TODO: Determine directory path dynamically, instead of hard-coding it.
MIGRATOR_DIRECTORY = "nmdc_schema/migrators"


def click_option_validator(function_to_decorate):
    r"""
    This decorator wraps a function in another function, which strips away the
    first two arguments and then passes the third argument to the wrapped function.
    """

    # Note: The `@wraps(fn)` decorator makes the wrapper function "look like" the wrapped
    #       function; in that the wrapper will adopt the latter's name and docstring.
    #       Reference: https://docs.python.org/3/library/functools.html#functools.wraps
    @wraps(function_to_decorate)
    def wrapper(click_context, param, param_value):
        return function_to_decorate(param_value)

    return wrapper


@click_option_validator
def validate_version_identifier(version_identifier: str) -> str:
    r"""
    Validates a version identifier, raising an exception if it's invalid.

    Reference: https://click.palletsprojects.com/en/8.1.x/options/#callbacks-for-validation

    >>> validate_version_identifier(None, None, "1.2.3")
    '1.2.3'
    >>> validate_version_identifier(None, None, "1.2.")  # doesn't end with a number
    Traceback (most recent call last):
    ...
    click.exceptions.BadParameter: Invalid format.
    >>> validate_version_identifier(None, None, "1.2")
    '1.2'
    >>> validate_version_identifier(None, None, "123.456.789")
    '123.456.789'
    >>> validate_version_identifier(None, None, "123.456.789.1")  # 4 parts
    Traceback (most recent call last):
    ...
    click.exceptions.BadParameter: Invalid format.
    >>> validate_version_identifier(None, None, "123")
    '123'
    """
    if re.fullmatch(r"^(\d+)(\.\d+){0,2}$", version_identifier) is None:
        raise click.BadParameter("Invalid format.")

    return version_identifier


@click.command()
@click.option(
    "--from-version",
    "--from",
    type=str,
    required=True,
    help='Schema version from which the migrator will migrate data (e.g. "1.0").',
    prompt="From schema version",
    callback=validate_version_identifier,
)
@click.option(
    "--to-version",
    "--to",
    type=str,
    required=True,
    prompt="To schema version",
    help='Schema version to which the migrator will migrate data (e.g. "1.1").',
    callback=validate_version_identifier,
)
def create_migrator(from_version: str, to_version: str) -> None:
    """
    Create a migrator class based upon the specified version identifiers.
    """

    # Generate the migrator module name.
    from_version_snake = from_version.replace(".", "_")
    to_version_snake = to_version.replace(".", "_")
    file_name = f"migrator_from_{from_version_snake}_to_{to_version_snake}.py"

    # Generate the migrator file contents.
    # TODO: Move this to a dedicated template file to facilitate maintenance.
    file_contents = f'''
from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "{from_version}"
    _to_version = "{to_version}"    
    
    def upgrade(self) -> None:
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""
        pass

'''

    # Create and populate the file (unless it already exists).
    file_path = Path(MIGRATOR_DIRECTORY) / Path(file_name)

    try:
        # Note: The "x" stands for "exclusive creation" mode, a mode in
        #       which an exception is thrown if the file already exists.
        with file_path.open("x") as file:
            file.write(file_contents)
        click.echo(f"Created '{file_name}' successfully.")
    except FileExistsError:
        click.echo(f"Error: File '{file_name}' already exists: {file_path}", err=True)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)

    return None


if __name__ == "__main__":
    create_migrator()
