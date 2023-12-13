import logging
from typing import Any
from importlib import resources
from pathlib import Path
import yaml

logger = logging.getLogger(__name__)

# TODO: Determine directory path and package path dynamically, instead of hard-coding them.
MIGRATOR_DIRECTORY = "nmdc_schema/migrators"
MIGRATOR_PACKAGE = "nmdc_schema.migrators"


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
