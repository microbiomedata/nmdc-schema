import logging
import traceback
import unittest

from linkml.validators.jsonschemavalidator import JsonSchemaDataValidator

from python.nmdc import PersonValue, CreditAssociation, Study


# from linkml_runtime.dumpers import yaml_dumper

# todo reimplement with methods?


class TestCA(unittest.TestCase):

    def test_sum(self):
        # nmdc_schema = "https://raw.githubusercontent.com/microbiomedata/nmdc-schema/main/src/schema/nmdc.yaml"
        nmdc_schema = "src/schema/nmdc.yaml"

        validator = JsonSchemaDataValidator(nmdc_schema)

        pv1 = PersonValue(has_raw_value="GW Carver")
        pv2 = PersonValue(has_raw_value="L Pasteur")

        ca1 = CreditAssociation(applies_to_person=pv1, applied_roles=["Supervision", "Validation"])
        ca2 = CreditAssociation(applies_to_person=pv2, applied_roles=["Investigation"])

        s = Study(id="abc")

        # # why is schema loaded each time?
        validator.validate_object(ca1, target_class=CreditAssociation)
        validator.validate_object(ca2, target_class=CreditAssociation)

        # try:
        #     s.has_credit_associations.append(ca1)
        #     s.has_credit_associations.append(ca2)
        #     validator.validate_object(s, target_class=Study)
        # except Exception as e:
        #     logging.error(traceback.format_exc())

        s.has_credit_associations.append(ca1)
        s.has_credit_associations.append(ca2)
        validator.validate_object(s, target_class=Study)

        print(s)

        self.assertEqual(type(s), Study)


if __name__ == '__main__':
    unittest.main()
