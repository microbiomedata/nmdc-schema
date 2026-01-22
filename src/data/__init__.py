"""Sample data, and functions that facilitate accessing that sample data.

Note: This module was initialized as a copy/paste/adapt of the `src/sample_data/__init__.py` module in
      another repository containing a LinkML schema—i.e. the `bertron-schema` repository—linked here:
      https://github.com/ber-data/bertron-schema/blob/445b359ee6dcd7472dfe19e86db50f56536bf645/src/sample_data/__init__.py
"""

import json
from importlib import resources
from importlib.abc import Traversable
from pathlib import Path
from typing import Any

import yaml

# Define the path someone could use to `import` the Python package _containing_ the
# `invalid/` and `valid/` directories (e.g. `import {something}`); which, currently,
# happens to be the directory containing this `__init__.py` file.
PACKAGE_IMPORT_PATH = "data"

# Define a mapping from file extension to a function that can be used to parse the
# content of a file having that extension.
PARSERS_BY_FILE_EXTENSION = {
    "yaml": yaml.safe_load,
    "yml": yaml.safe_load,
    "json": json.loads,
}


def _get_traversable() -> Traversable:
    """Get a `Traversable` object for the `data/` package.

    The `Traversable` object can be used to access resources contained
    within the `data` package, whether this function is called
    from this package's source tree, or in an installed distribution.

    Returns:
        A `Traversable` object for the `data/` package.

    References:
    - https://docs.python.org/3/library/importlib.resources.html#importlib.resources.files
    - https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.Traversable

    """
    # Create a `Traversable` object that can be passed to the `resources.as_file()` function.
    return resources.files(PACKAGE_IMPORT_PATH)


def get_sample_data_file_paths() -> list[str]:
    """List the paths to all available sample data files.

    These are the paths that can be passed to the `get_sample_data` and
    `get_sample_data_text` functions.

    Returns:
        A list of file paths (relative to the `data/` directory) to all
        ".yaml", ".yml", and ".json" files residing within `data/`.

    """
    traversable = _get_traversable()
    file_extension_patterns = [f"**/*.{ext}" for ext in PARSERS_BY_FILE_EXTENSION]
    with resources.as_file(traversable) as path:
        paths = [
            str(p.relative_to(path))
            for pattern in file_extension_patterns
            for p in path.glob(pattern)
        ]
        return sorted(paths)


def get_sample_data_text(file_path: str, encoding: str = "utf-8") -> str:
    """Get the text content of a sample data file.

    Args:
        file_path: The path to the sample data file, relative to the `data/` directory.
        encoding: The text encoding to use when reading the file.

    Returns:
        The text content of the specified sample data file.

    References:
    - https://docs.python.org/3/library/importlib.resources.html#importlib.resources.as_file

    """
    traversable = _get_traversable().joinpath(file_path)
    with resources.as_file(traversable) as path:
        return path.read_text(encoding=encoding)


def get_sample_data(file_path: str, encoding: str = "utf-8") -> Any:  # noqa: ANN401
    """Get a Python value representing the content of a JSON/YAML-formatted sample data file.

    Args:
        file_path: The path to the sample data file, relative to the `data/` directory.
        encoding: The text encoding to use when reading the file.

    Returns:
        The content of the specified sample data file, parsed into a Python value
        (in practice this is typically a dictionary or list).

    """
    # Determine which parsing function we will use, based upon the file's extension.
    path = Path(file_path)
    file_extension = path.suffix.lstrip(".")  # ".yaml" -> "yaml"
    if file_extension in PARSERS_BY_FILE_EXTENSION:
        parse = PARSERS_BY_FILE_EXTENSION[file_extension]
    else:
        # Raise an error indicating that we don't support files having that extension.
        # Note: The `!r` after the in-string variable below calls `repr()` on the value.
        #       Since the value is a string, the string will appear wrapped in quotes.
        msg = f"Filename extension suggests an unsupported file type: {file_path!r}"
        raise ValueError(msg)

    text = get_sample_data_text(file_path, encoding=encoding)
    return parse(text)
