import os
import unittest

from linkml.validators.jsonschemavalidator import JsonSchemaDataValidator

from nmdc_schema.nmdc import PersonValue, CreditAssociation, Study

ROOT = os.path.join(os.path.dirname(__file__), '..')
SCHEMA_DIR = os.path.join(ROOT, "src", "schema")
SCHEMA_FILE = os.path.join(SCHEMA_DIR, 'nmdc.yaml')


class TestCA(unittest.TestCase):

    def test_sum(self):
        validator = JsonSchemaDataValidator(SCHEMA_FILE)

        pv1 = PersonValue(has_raw_value="GW Carver")
        pv2 = PersonValue(has_raw_value="L Pasteur")

        ca1 = CreditAssociation(applies_to_person=pv1, applied_roles=["Supervision", "Validation"])
        ca2 = CreditAssociation(applies_to_person=pv2, applied_roles=["Investigation"])

        s = Study(id="nmdc:sty-e3e05c16-8c9a-421e-ade5-cde4e5a435fa", study_category="research_study")

        # # why is schema loaded each time?
        validator.validate_object(ca1, target_class=CreditAssociation)
        validator.validate_object(ca2, target_class=CreditAssociation)

        s.has_credit_associations.append(ca1)
        s.has_credit_associations.append(ca2)
        validator.validate_object(s, target_class=Study)

        self.assertEqual(type(s), Study)


if __name__ == '__main__':
    unittest.main()
