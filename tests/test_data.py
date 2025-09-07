"""Tests targeting functions that expose sample data."""

import json
from collections.abc import Generator
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest
import yaml

# TODO: Consider reconfiguring the package so that people can import the sample data
#       getter functions from the familiar `nmdc_schema` package, rather than from `src`.
from src.data import get_sample_data, get_sample_data_file_paths, get_sample_data_text


@pytest.fixture
def sample_json_content() -> str:
    """Fixture that returns the text content of a sample JSON file."""
    return r"""
{
  "id": "001",
  "name": "foo bar",
  "primary email": "foo.bar@example.com",
  "age_in_years": 33
}
"""

@pytest.fixture
def sample_yaml_content() -> str:
    """Fixture that returns the text content of a sample YAML file."""
    return r"""
# Some YAML documents begin with "front matter".
---
id: "001"
name: foo bar
primary email: foo.bar@example.com
age_in_years: 33
"""

@pytest.fixture(autouse=True)
def mock__get_traversable(
    monkeypatch: Generator[pytest.MonkeyPatch, None, None],
    sample_yaml_content: str,
    sample_json_content: str,
) -> Generator[None, None, None]:
    """Fixture that mocks the `sample_data._get_traversable` helper function.

    This fixture (a) creates a temporary directory, (b) populates it with sample data files,
    and (c) patches the `_get_traversable` function so it returns a `Path` object pointing
    to that temporary directory. This decouples the tests from the contents of the real
    `data/` directory that the module-under-test accesses in production.

    Note: All `Path` objects are also `Traversable` object.
    """
    with TemporaryDirectory() as temp_dir:
        temp_dir_path = Path(temp_dir)
        (temp_dir_path / "data.json").write_text(sample_json_content)
        (temp_dir_path / "data.yaml").write_text(sample_yaml_content)
        (temp_dir_path / "data.yml").write_text(sample_yaml_content)
        (temp_dir_path / "data.txt").write_text("some text")  # unsupported file suffix
        monkeypatch.setattr("src.data._get_traversable", lambda: temp_dir_path)
        yield None


def test_get_sample_data_file_paths_returns_list_of_file_paths_supported() -> None:
    """Test that `get_sample_data_file_paths` returns a list of the file paths we support."""
    assert get_sample_data_file_paths() == ["data.json", "data.yaml", "data.yml"]


def test_get_sample_data_text_returns_expected_sample_data_as_string(
    sample_json_content: str,
    sample_yaml_content: str,
) -> None:
    """Test that `get_sample_data_text` returns the sample data we expect, as a string."""
    for path in get_sample_data_file_paths():
        if path == "data.json":
            assert sample_json_content == get_sample_data_text(path)
        if path in ("data.yaml", "data.yml"):
            assert sample_yaml_content == get_sample_data_text(path)


def test_get_sample_data_returns_sample_data_as_python_object(
    sample_json_content: str,
    sample_yaml_content: str,
) -> None:
    """Test that `get_sample_data` returns sample data as a Python object."""
    for path in get_sample_data_file_paths():
        if path == "data.json":
            assert json.loads(sample_json_content) == get_sample_data(path)
        if path in ("data.yaml", "data.yml"):
            assert yaml.safe_load(sample_yaml_content) == get_sample_data(path)


def test_get_sample_data_rejects_unsupported_filename_extensions() -> None:
    """Test that `get_sample_data` raises an exception for an unsupported filename extension."""
    with pytest.raises(ValueError, match=r"^Filename extension"):
        get_sample_data("my_file.txt")
