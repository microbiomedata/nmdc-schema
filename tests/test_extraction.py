import os
import unittest

from linkml.validators.jsonschemavalidator import JsonSchemaDataValidator
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.loaders import yaml_loader

from nmdc_schema.nmdc import ConstituentOfFluid, QuantityValue, Fluid, Extraction, ChromatographicSeparationProcess

ROOT = os.path.join(os.path.dirname(__file__), '..')
SCHEMA_DIR = os.path.join(ROOT, "src", "schema")
SCHEMA_FILE = os.path.join(SCHEMA_DIR, 'nmdc.yaml')


class TestExtraction(unittest.TestCase):

    def test_extraction(self):
        # validator = JsonSchemaDataValidator(SCHEMA_FILE)  # it takes a long time to construct this

        component1 = ConstituentOfFluid(
            name="deionized water",
        )
        # validator.validate_object(component1, target_class=ConstituentOfFluid)

        qv2 = QuantityValue(has_numeric_value=10, has_unit="%")
        # validator.validate_object(qv2, target_class=QuantityValue)

        component2 = ConstituentOfFluid(
            name="methanol",
            concentration=qv2
        )
        # validator.validate_object(component2, target_class=ConstituentOfFluid)

        fluid_1 = Fluid(
            has_constituents=[component1, component2],
            volume=QuantityValue(
                has_numeric_value=100,
                has_unit="mL"
            )
        )
        # validator.validate_object(fluid_1, target_class=Fluid)

        ex1 = Extraction(
            id="nmdc:ILLEGAL_ID_VAL",
            has_input=["nmdc:ILLEGAL_ID_VAL"],
            has_output=["nmdc:ILLEGAL_ID_VAL"],
            extractant=fluid_1,
        )

        # validator.validate_object(fluid_1, target_class=Fluid)

        print("\n")
        print(ex1)

        print(yaml_dumper.dumps(ex1))

        extr_yaml_string = """
id: nmdc:ILLEGAL_ID_VAL
designated_class: nmdc:Extraction
has_input:
- nmdc:ILLEGAL_ID_VAL
has_output:
- nmdc:ILLEGAL_ID_VAL
extractant:
  has_constituents:
  - name: deionized water
  - name: methanol
    concentration:
      has_numeric_value: 10.0
      has_unit: '%'
  volume:
    has_numeric_value: 100.0
    has_unit: mL
"""

        from_yaml_string = yaml_loader.load(source=extr_yaml_string, target_class=Extraction)


class TestChromatographySeparationProcess(unittest.TestCase):

    def test_phase_separation(self):
        # validator = JsonSchemaDataValidator(SCHEMA_FILE)  # it takes a long time to construct this

        component1 = ConstituentOfFluid(
            name="deionized water",
        )
        # validator.validate_object(component1, target_class=ConstituentOfFluid)

        qv2 = QuantityValue(has_numeric_value=10, has_unit="%")
        # validator.validate_object(qv2, target_class=QuantityValue)

        component2 = ConstituentOfFluid(
            name="methanol",
            concentration=qv2
        )
        # validator.validate_object(component2, target_class=ConstituentOfFluid)

        fluid_1 = Fluid(
            has_constituents=[component1, component2],
            volume=QuantityValue(
                has_numeric_value=100,
                has_unit="mL"
            ),
        )

        ps1 = ChromatographicSeparationProcess(
            id="nmdc:ILLEGAL_ID_VAL",
            ordered_mobile_phases=fluid_1,
            stationary_phase="C8",
        )

        print("\n")
        print(yaml_dumper.dumps(ps1))


if __name__ == '__main__':
    unittest.main()
