import logging
from typing import Any, Type, Optional, List
from importlib import resources
from pathlib import Path
from migrator_base import MigratorBase
import yaml
import pkgutil
import importlib

logger = logging.getLogger(__name__)

# TODO: Determine directory path and package path dynamically, instead of hard-coding them.
MIGRATOR_DIRECTORY = "nmdc_schema/migrators"
MIGRATOR_PACKAGE = "nmdc_schema.migrators"


def get_migrator_module_names() -> List[str]:
    """
    Returns a list of all migrator module names.
    """

    module_names = [name for _, name, _ in pkgutil.iter_modules([MIGRATOR_DIRECTORY])]
    migrator_module_names = [s for s in module_names if s.startswith("migrator_from_")]  # filters the list
    return migrator_module_names


def get_migrator_to(destination_version: str) -> Optional[Type[MigratorBase]]:
    """
    Returns a migrator class, if any, that migrates data to the specified schema version.
    """

    matching_migrator_class = None
    for module_name in get_migrator_module_names():
        try:
            # Import the module having that name.
            # Reference: https://docs.python.org/3/library/importlib.html#importlib.import_module
            migrator_module = importlib.import_module(f".{module_name}", package=MIGRATOR_PACKAGE)

            # Get the `Migrator` class defined in that module.
            # Reference: https://docs.python.org/3/library/inspect.html#inspect.isclass
            migrator_class = getattr(migrator_module, "Migrator")
            if not issubclass(migrator_class, MigratorBase):
                raise TypeError

            # If that migrator class migrates data to the specified version, return the class.
            if migrator_class.get_destination_version() == destination_version:
                matching_migrator_class = migrator_class
                break  # no need to check other classes

        except (KeyError, ImportError, AttributeError, TypeError) as exception:
            logger.exception(f"Failed to get migrator. {exception}.")

    logger.warning(f"No compatible migrator found.")
    return matching_migrator_class


def load_yaml_asset(path_to_asset_file: str) -> Any:
    """
    Safely loads the contents of a YAML file into a Python object. This function was designed specifically to
    work in both the `nmdc-schema` development environment and in environments that import the `nmdc-schema` package.

    Parameters:
        path_to_asset_file: Filesystem path to the YAML file, relative to the root of the `assets` directory.

    References:
    - https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.joinpath
    - https://docs.python.org/3/library/importlib.resources.html#importlib.resources.files
    - https://docs.python.org/3/library/importlib.resources.html#importlib.resources.as_file
    - https://realpython.com/python-yaml/#load-a-document-from-a-string-a-file-or-a-stream
    """
    # Define the Python path someone could use to `import` the package containing the `assets` directory.
    package_import_path = MIGRATOR_PACKAGE

    # Define the filesystem path to the `assets` directory (relative to that package).
    path_to_assets_directory = "assets"

    # Build a filesystem path to the specified asset file (also relative to that package).
    path_to_asset = Path(path_to_assets_directory).joinpath(path_to_asset_file)

    # Create a `Traversable` object that can be passed to the `resources.as_file()` function.
    traversable_resource_container = resources.files(package_import_path).joinpath(path_to_asset)

    # Use `resources.as_file()` to get an `open()`-able path to the asset file.
    with resources.as_file(traversable_resource_container) as file_path:
        # Finally, open the asset file and parse its contents as YAML.
        with open(file_path, "r") as f:
            obj = yaml.safe_load(f)  # the object type depends upon the YAML data

    return obj
