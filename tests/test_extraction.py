import os
import unittest

from linkml.validators.jsonschemavalidator import JsonSchemaDataValidator
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.loaders import yaml_loader

from nmdc_schema.nmdc import SolutionComponent, QuantityValue, Solution, Extraction, ChromatographicSeparationProcess

ROOT = os.path.join(os.path.dirname(__file__), '..')
SCHEMA_DIR = os.path.join(ROOT, "src", "schema")
SCHEMA_FILE = os.path.join(SCHEMA_DIR, 'nmdc.yaml')


class TestExtraction(unittest.TestCase):

    def test_extraction(self):
        # validator = JsonSchemaDataValidator(SCHEMA_FILE)  # it takes a long time to construct this

        component1 = SolutionComponent(
            compound="deionized_water",
            type="nmdc:SolutionComponent",
        )
        # validator.validate_object(component1, target_class=SolutionComponent)

        qv2 = QuantityValue(
            has_numeric_value=10,
            has_unit="%",
            type="nmdc:QuantityValue",
        )
        # validator.validate_object(qv2, target_class=QuantityValue)

        component2 = SolutionComponent(
            compound="deionized_water",
            concentration=qv2,
            type="nmdc:SolutionComponent",
        )
        # validator.validate_object(component2, target_class=SolutionComponent)

        sol1 = Solution(
            has_solution_components=[component1, component2],
            volume=QuantityValue(
                has_numeric_value=100,
                has_unit="mL",
                type="nmdc:QuantityValue",
            ),
            type="nmdc:Solution",
        )
        # validator.validate_object(sol1, target_class=Solution)

        ex1 = Extraction(
            extractant=sol1,
            has_input=["nmdc:ILLEGAL_ID_VAL"],
            has_output=["nmdc:ILLEGAL_ID_VAL"],
            id="nmdc:ILLEGAL_ID_VAL",
            type="nmdc:Extraction",
        )

        # validator.validate_object(sol1, target_class=Solution)

        print("\n")
        print(ex1)

        print(yaml_dumper.dumps(ex1))

        # type: Extraction

        extr_yaml_string = """
id: nmdc:ILLEGAL_ID_VAL
type: nmdc:Extraction
has_input:
- nmdc:ILLEGAL_ID_VAL
has_output:
- nmdc:ILLEGAL_ID_VAL
extractant:
  has_solution_components:
  - compound: deionized_water
    type: nmdc:SolutionComponent
  - compound: deionized_water
    type: nmdc:SolutionComponent
    concentration:
      type: nmdc:QuantityValue
      has_numeric_value: 10.0
      has_unit: '%'
  type: nmdc:Solution
  volume:
    type: nmdc:QuantityValue
    has_numeric_value: 100.0
    has_unit: mL
"""

        from_yaml_string = yaml_loader.load(source=extr_yaml_string, target_class=Extraction)


class TestChromatographySeparationProcess(unittest.TestCase):

    def test_phase_separation(self):
        # validator = JsonSchemaDataValidator(SCHEMA_FILE)  # it takes a long time to construct this

        component1 = SolutionComponent(
            compound="deionized_water",
            type="nmdc:SolutionComponent",
        )
        # validator.validate_object(component1, target_class=SolutionComponent)

        qv2 = QuantityValue(
            has_numeric_value=10,
            has_unit="%",
            type="nmdc:QuantityValue",
        )
        # validator.validate_object(qv2, target_class=QuantityValue)

        component2 = SolutionComponent(
            compound="methanol",
            concentration=qv2,
            type="nmdc:SolutionComponent",
        )
        # validator.validate_object(component2, target_class=SolutionComponent)

        sol1 = Solution(
            has_solution_components=[component1, component2],
            volume=QuantityValue(
                has_numeric_value=100,
                has_unit="mL",
                type="nmdc:QuantityValue",
            ),
            type="nmdc:Solution",
        )

        ps1 = ChromatographicSeparationProcess(
            id="nmdc:ILLEGAL_ID_VAL",
            ordered_mobile_phases=sol1,
            stationary_phase="C8",
            type="nmdc:ChromatographicSeparationProcess",
        )

        print("\n")
        print(yaml_dumper.dumps(ps1))


if __name__ == '__main__':
    unittest.main()
