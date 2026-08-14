import pytest
import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin

from nmdc_schema_validation_plugin import NmdcSchemaValidationPlugin
from tests import SCHEMA_FILE, ROOT


@pytest.fixture
def minimal_biosample():
    return {
        "id": "nmdc:bsm-99-dtTMNb",
        "type": "nmdc:Biosample",
        "name": "minimal biosample",
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
    """Validator that runs ONLY the NMDC plugin, for unit-testing the plugin itself.

    Passing ``validation_plugins`` replaces linkml's default ``JsonschemaValidationPlugin``
    rather than adding to it, so this validator does no structural validation at all. That is
    what the two tests below want: they assert on the plugin's own results in isolation. Any
    test that means "this instance is valid" needs ``fully_validating_validator`` instead.
    """
    return Validator(
        schema=SCHEMA_FILE,
        validation_plugins=[
            NmdcSchemaValidationPlugin(),
        ],
    )


@pytest.fixture(scope="module")
def fully_validating_validator():
    """Validator that runs structural validation AND the NMDC plugin.

    ``JsonschemaValidationPlugin`` is linkml's default and covers required slots, id patterns,
    enum membership, and (in closed mode) unexpected properties. ``NmdcSchemaValidationPlugin``
    adds the QuantityValue unit-alignment check that the schema alone cannot express. Neither
    subsumes the other, so example data needs both.
    """
    return Validator(
        schema=SCHEMA_FILE,
        validation_plugins=[
            JsonschemaValidationPlugin(closed=True),
            NmdcSchemaValidationPlugin(),
        ],
    )


def test_valid_instance(nmdc_schema_validator, minimal_biosample):
    """Test that a Biosample instance with a correct QuantityValue unit alignment passes validation."""
    biosample_instance = {
        **minimal_biosample,
        "samp_store_temp": {
            "type": "nmdc:QuantityValue",
            "has_numeric_value": -80,
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
            "has_numeric_value": -80,
            "has_unit": "INVALID_UNIT"
        }
    }
    report = nmdc_schema_validator.validate(biosample_instance, target_class="Biosample")
    assert len(report.results) == 1
    assert "/samp_store_temp" in report.results[0].message, "message should reference path to invalid QuantityValue"
    assert "INVALID_UNIT" in report.results[0].message, "message should include the invalid unit"
    assert "Cel" in report.results[0].message, "message should include the expected unit"


def test_structural_defects_need_the_jsonschema_plugin(
    nmdc_schema_validator, fully_validating_validator, minimal_biosample
):
    """Guard the plugin-replacement trap that let structural defects through.

    Passing ``validation_plugins`` to ``Validator`` REPLACES linkml's default
    ``JsonschemaValidationPlugin`` rather than adding to it. A validator built with the NMDC plugin
    alone therefore accepts an instance with a broken id, a missing required slot, or an invented
    property. This test pins both halves of that: the plugin-only validator stays silent, and the
    fully validating one does not. If someone later drops ``JsonschemaValidationPlugin`` from
    ``fully_validating_validator``, this fails instead of quietly widening what passes.
    """
    structurally_broken = {
        **minimal_biosample,
        "id": "NOT-AN-NMDC-ID",
        "invented_slot": "no such slot in the schema",
    }

    plugin_only_report = nmdc_schema_validator.validate(
        structurally_broken, target_class="Biosample"
    )
    assert not plugin_only_report.results, (
        "the NMDC plugin alone is not expected to catch structural defects; "
        "if it now does, this test's premise has changed"
    )

    full_report = fully_validating_validator.validate(
        structurally_broken, target_class="Biosample"
    )
    assert full_report.results, "structural defects must be caught when jsonschema runs"


def test_all_valid_examples(fully_validating_validator):
    """Test that all example files in src/data/valid validate successfully.

    This would be better as part of the `linkml-run-examples` command, but that CLI doesn't allow
    specifying custom validation plugins at present. That is why the unit-alignment check is
    repeated here rather than left to `make test`'s examples runner.

    Use `fully_validating_validator`, not `nmdc_schema_validator`. The latter runs the NMDC plugin
    alone, which checks unit alignment and nothing else, so a file with a bad id pattern, a missing
    required slot, or an unexpected property passes it. The examples runner in `make test` catches
    those, but only there, which makes a green `pytest tests/` mean less than it appears to.

    If any example file's target class is absent from the materialized-patterns artifact, the
    test is marked skipped at the end with a list of affected files. This happens during feature
    development when new classes have been added to source YAML but the artifact has not yet been
    regenerated (per project policy, artifacts are only regenerated immediately before
    merge/release).
    """
    from linkml_runtime import SchemaView

    examples_dir = ROOT / "src/data/valid"
    schema_view = SchemaView(str(SCHEMA_FILE))
    skipped = []

    for example_file in sorted(examples_dir.glob("*.yaml")):
        with example_file.open(encoding="utf-8") as f:
            instance = yaml.safe_load(f)
        if '-' in example_file.name:
            target_class = example_file.name.split('-', 1)[0]
        else:
            target_class = example_file.stem

        if schema_view.get_class(target_class) is None:
            skipped.append(f"{example_file.name} (class '{target_class}' not in artifact)")
            continue

        report = fully_validating_validator.validate(instance, target_class=target_class)
        assert not report.results, f"Validation errors in {example_file}"

    if skipped:
        pytest.skip(f"Skipped {len(skipped)} file(s) — artifact stale: {'; '.join(skipped)}")
