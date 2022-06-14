import unittest

from linkml_runtime.dumpers import yaml_dumper

from python.nmdc import FlatterStudy, PersonValue, CreditAssociation, Study

from linkml.validators.jsonschemavalidator import JsonSchemaDataValidator


class TestCA(unittest.TestCase):
    # nmdc_schema = "https://raw.githubusercontent.com/microbiomedata/nmdc-schema/main/src/schema/nmdc.yaml"
    nmdc_schema = "../src/schema/nmdc.yaml"

    validator = JsonSchemaDataValidator(nmdc_schema)

    pv1 = PersonValue(has_raw_value="GW Carver")
    pv2 = PersonValue(has_raw_value="L Pasteur")

    ca1 = CreditAssociation(applies_to_person=pv1, applied_roles=["Supervision", "Validation"])
    ca2 = CreditAssociation(applies_to_person=pv2, applied_roles=["Investigation"])

    fs = FlatterStudy()
    fs.flatter_has_credit_associations = ca1

    s = Study(id="abc")
    # s = Study(id="abc", has_credit_associations={"ca1": ca1, "ca2": ca2})

    # # why is schema loaded each time?
    validator.validate_object(ca1, target_class=CreditAssociation)
    validator.validate_object(ca2, target_class=CreditAssociation)
    validator.validate_object(fs, target_class=FlatterStudy)
    validator.validate_object(s, target_class=Study)


if __name__ == '__main__':
    unittest.main()
