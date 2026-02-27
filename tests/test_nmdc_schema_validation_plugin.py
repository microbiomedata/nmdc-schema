import pytest
import yaml
from linkml.validator import Validator, JsonschemaValidationPlugin

from nmdc_schema_validation_plugin import NmdcSchemaValidationPlugin
from tests import SCHEMA_FILE, ROOT


@pytest.fixture
def minimal_biosample():
    return {
        "id": "nmdc:bsm-99-dtTMNb",
        "type": "nmdc:Biosample",
        "associated_studies": ["nmdc:sty-00-abc123"],
        "env_broad_scale": {
            "type": "nmdc:ControlledIdentifiedTermValue",
            "has_raw_value": "ENVO:00002030",
            "term": {
                "id": "ENVO:00002030",
                "type": "nmdc:OntologyClass",
            }
        },
        "env_local_scale": {
            "type": "nmdc:ControlledIdentifiedTermValue",
            "has_raw_value": "ENVO:00002169",
            "term": {
                "id": "ENVO:00002169",
                "type": "nmdc:OntologyClass",
            }
        },
        "env_medium": {
            "type": "nmdc:ControlledIdentifiedTermValue",
            "has_raw_value": "ENVO:00005792",
            "term": {
                "id": "ENVO:00005792",
                "type": "nmdc:OntologyClass",
            }
        }
    }


@pytest.fixture(scope="module")
def nmdc_schema_validator():
    return Validator(
        schema=SCHEMA_FILE,
        validation_plugins=[
            NmdcSchemaValidationPlugin(),
        ]
    )


def test_valid_instance(nmdc_schema_validator, minimal_biosample):
    """Test that a Biosample instance with a correct QuantityValue unit alignment passes validation."""
    biosample_instance = {
        **minimal_biosample,
        "samp_store_temp": {
            "type": "nmdc:QuantityValue",
            "has_value": -80,
            "has_unit": "Cel"
        }
    }
    report = nmdc_schema_validator.validate(biosample_instance, target_class="Biosample")
    assert not report.results


def test_invalid_instance(nmdc_schema_validator, minimal_biosample):
    """Test that a valid Biosample instance with an incorrect QuantityValue unit alignment fails
    validation."""
    biosample_instance = {
        **minimal_biosample,
        "samp_store_temp": {
            "type": "nmdc:QuantityValue",
            "has_value": -80,
            "has_unit": "INVALID_UNIT"
        }
    }
    report = nmdc_schema_validator.validate(biosample_instance, target_class="Biosample")
    assert len(report.results) == 1
    assert "/samp_store_temp" in report.results[0].message, "message should reference path to invalid QuantityValue"
    assert "INVALID_UNIT" in report.results[0].message, "message should include the invalid unit"
    assert "Cel" in report.results[0].message, "message should include the expected unit"


def test_all_valid_examples(nmdc_schema_validator):
    """Test that all example files in src/data/valid validate successfully.

    This would be better as part of the `linkml-run-examples` command, but that CLI doesn't allow
    specifying custom validation plugins at present.
    """

    examples_dir = ROOT / "src/data/valid"
    for example_file in examples_dir.glob("*.yaml"):
        with open(example_file) as f:
            instance = yaml.safe_load(f)
        if '-' in example_file.name:
            target_class = example_file.name.split('-')[0]
        else:
            target_class = example_file.stem
        report = nmdc_schema_validator.validate(instance, target_class=target_class)
        assert not report.results, f"Validation errors in {example_file}"
