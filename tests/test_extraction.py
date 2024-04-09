import os
import unittest

from linkml.validators.jsonschemavalidator import JsonSchemaDataValidator
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.loaders import yaml_loader

from nmdc_schema.nmdc import PortionOfSubstance, QuantityValue, Extraction, ChromatographicSeparationProcess, \
    MobilePhaseSegment

ROOT = os.path.join(os.path.dirname(__file__), '..')
SCHEMA_DIR = os.path.join(ROOT, "src", "schema")
SCHEMA_FILE = os.path.join(SCHEMA_DIR, 'nmdc.yaml')


class TestExtraction(unittest.TestCase):

    def test_extraction(self):
        validator = JsonSchemaDataValidator(SCHEMA_FILE)  # it takes a long time to construct this

        substance1 = PortionOfSubstance(
            known_as="nmdc:chem-99-000005",
            type="nmdc:PortionOfSubstance",
        )  # see src/data/valid/Database-chemical_entity_set-1.yaml

        validator.validate_object(substance1, target_class=PortionOfSubstance)

        final_concentration = QuantityValue(
            type="nmdc:QuantityValue",
            has_numeric_value=5,
            has_unit="%"
        )

        validator.validate_object(final_concentration, target_class=QuantityValue)

        substance2 = PortionOfSubstance(
            known_as="nmdc:chem-99-000003",
            final_concentration=final_concentration,
            type="nmdc:PortionOfSubstance",
        )

        validator.validate_object(substance2, target_class=PortionOfSubstance)

        ex1 = Extraction(
            substances_used=[substance1, substance2],
            has_input=["nmdc:NOT_CHECKED_IN_TEST"],
            has_output=["nmdc:NOT_CHECKED_IN_TEST"],
            id="nmdc:NOT_CHECKED_IN_TEST",
            type="nmdc:Extraction",
        )

        validator.validate_object(ex1, target_class=Extraction)

        # print("\n")
        # print(ex1)
        #
        # print(yaml_dumper.dumps(ex1))

        extr_yaml_string = """
id: nmdc:NOT_CHECKED_IN_TEST
type: nmdc:Extraction
has_input:
- nmdc:NOT_CHECKED_IN_TEST
has_output:
- nmdc:NOT_CHECKED_IN_TEST
substances_used:
- type: nmdc:PortionOfSubstance
  known_as: nmdc:chem-99-000005
- type: nmdc:PortionOfSubstance
  final_concentration:
    type: nmdc:QuantityValue
    has_numeric_value: 5.0
    has_unit: '%'
  known_as: nmdc:chem-99-000003
"""

        from_yaml_string = yaml_loader.load(source=extr_yaml_string, target_class=Extraction)

        assert ex1 == from_yaml_string


class TestChromatographySeparationProcess(unittest.TestCase):

    def test_phase_separation(self):
        pass

        validator = JsonSchemaDataValidator(SCHEMA_FILE)  # it takes a long time to construct this

        substance1 = PortionOfSubstance(
            known_as="nmdc:chem-99-000005",
            type="nmdc:PortionOfSubstance",
        )  # see src/data/valid/Database-chemical_entity_set-1.yaml

        validator.validate_object(substance1, target_class=PortionOfSubstance)

        final_concentration = QuantityValue(
            type="nmdc:QuantityValue",
            has_numeric_value=5,
            has_unit="%"
        )

        validator.validate_object(final_concentration, target_class=QuantityValue)

        substance2 = PortionOfSubstance(
            known_as="nmdc:chem-99-000003",
            final_concentration=final_concentration,
            type="nmdc:PortionOfSubstance",
        )

        validator.validate_object(substance2, target_class=PortionOfSubstance)

        #             ordered_mobile_phases=[substance1, substance2],
        #

        duration1 = QuantityValue(
            type="nmdc:QuantityValue",
            has_numeric_value=5,
            has_unit="minutes"
        )

        validator.validate_object(duration1, target_class=QuantityValue)

        mbp1 = MobilePhaseSegment(
            substances_used=[substance1],
            type="nmdc:MobilePhaseSegment",
            duration=duration1
        )

        validator.validate_object(mbp1, target_class=MobilePhaseSegment)

        mbp2 = MobilePhaseSegment(
            substances_used=[substance2],
            type="nmdc:MobilePhaseSegment",
            duration=duration1
        )

        validator.validate_object(mbp2, target_class=MobilePhaseSegment)

        csp = ChromatographicSeparationProcess(
            id="nmdc:NOT_CHECKED_IN_TEST",
            chromatographic_category="liquid_chromatography",
            stationary_phase="C8",
            type="nmdc:ChromatographicSeparationProcess",
            ordered_mobile_phases=[mbp1, mbp2],
        )

        validator.validate_object(csp, target_class=ChromatographicSeparationProcess)

        # print("\n")
        # print(csp)
        #
        # print(yaml_dumper.dumps(csp))

        extr_yaml_string = """
id: nmdc:NOT_CHECKED_IN_TEST
type: nmdc:ChromatographicSeparationProcess
chromatographic_category: liquid_chromatography
ordered_mobile_phases:
- type: nmdc:MobilePhaseSegment
  duration:
    type: nmdc:QuantityValue
    has_numeric_value: 5.0
    has_unit: minutes
  substances_used:
  - type: nmdc:PortionOfSubstance
    known_as: nmdc:chem-99-000005
- type: nmdc:MobilePhaseSegment
  duration:
    type: nmdc:QuantityValue
    has_numeric_value: 5.0
    has_unit: minutes
  substances_used:
  - type: nmdc:PortionOfSubstance
    final_concentration:
      type: nmdc:QuantityValue
      has_numeric_value: 5.0
      has_unit: '%'
    known_as: nmdc:chem-99-000003
stationary_phase: C8
        """

        from_yaml_string = yaml_loader.load(source=extr_yaml_string, target_class=ChromatographicSeparationProcess)

        assert csp == from_yaml_string


if __name__ == '__main__':
    unittest.main()
