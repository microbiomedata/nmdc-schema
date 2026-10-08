"""Tests for the --element option of src/scripts/ols4_embeddings_search.py.

The OLS4 API is not called: search_element is replaced with a recorder.
"""

from pathlib import Path

import pytest
from click.testing import CliRunner

from src.scripts import ols4_embeddings_search

SCHEMA = """\
id: https://example.org/test
name: test
prefixes:
  linkml: https://w3id.org/linkml/
imports:
  - linkml:types
default_range: string
classes:
  Sample:
    slots:
      - analysis_type
slots:
  analysis_type:
    range: AnalysisTypeEnum
enums:
  AnalysisTypeEnum:
    permissible_values:
      metagenomics: {}
      metabolomics: {}
  OtherEnum:
    permissible_values:
      other_value: {}
"""


@pytest.fixture
def run_search(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    schema_path = tmp_path / "schema.yaml"
    schema_path.write_text(SCHEMA)
    searched: list[tuple[str, str]] = []

    def record(subject_id, name, category, *args):
        searched.append((category, name))
        return []

    monkeypatch.setattr(ols4_embeddings_search, "search_element", record)

    def run(*options: str):
        result = CliRunner().invoke(
            ols4_embeddings_search.main,
            ["--schema", str(schema_path), "-o", str(tmp_path / "out.tsv"), *options],
        )
        return result, searched

    return run


def test_element_limits_search_to_one_enum_and_its_values(run_search):
    result, searched = run_search("--element", "AnalysisTypeEnum")
    assert result.exit_code == 0, result.output
    assert sorted(searched) == [
        ("enum", "AnalysisTypeEnum"),
        ("permissible_value", "metabolomics"),
        ("permissible_value", "metagenomics"),
    ]


def test_element_with_pvs_only_searches_just_the_values(run_search):
    result, searched = run_search(
        "--element", "AnalysisTypeEnum", "--element-types", "pvs"
    )
    assert result.exit_code == 0, result.output
    assert sorted(searched) == [
        ("permissible_value", "metabolomics"),
        ("permissible_value", "metagenomics"),
    ]


def test_element_is_repeatable_across_element_types(run_search):
    result, searched = run_search("--element", "Sample", "--element", "analysis_type")
    assert result.exit_code == 0, result.output
    assert sorted(searched) == [("class", "Sample"), ("slot", "analysis_type")]


def test_without_element_everything_is_searched(run_search):
    result, searched = run_search("--element-types", "enums")
    assert result.exit_code == 0, result.output
    assert sorted(searched) == [("enum", "AnalysisTypeEnum"), ("enum", "OtherEnum")]


def test_unknown_element_is_an_error_not_an_empty_run(run_search):
    result, searched = run_search(
        "--element", "AnalysisTypeEnum", "--element", "NoSuchEnum"
    )
    assert result.exit_code != 0
    assert "NoSuchEnum" in result.output
    assert searched == []


def test_element_outside_the_selected_types_is_an_error(run_search, tmp_path):
    result, searched = run_search("--element", "Sample", "--element-types", "pvs")
    assert result.exit_code != 0
    assert "Sample" in result.output
    assert searched == []
    assert not (tmp_path / "out.tsv").exists()


def test_one_unmatched_name_among_valid_ones_is_an_error(run_search, tmp_path):
    result, searched = run_search(
        "--element", "AnalysisTypeEnum", "--element", "Sample", "--element-types", "pvs"
    )
    assert result.exit_code != 0
    assert "Sample" in result.output
    assert "AnalysisTypeEnum" not in result.output.split("searches in")[-1]
    assert searched == []
    assert not (tmp_path / "out.tsv").exists()
