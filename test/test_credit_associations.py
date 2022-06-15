import logging
import traceback
import unittest

from linkml.validators.jsonschemavalidator import JsonSchemaDataValidator

from python.nmdc import FlatterStudy, PersonValue, CreditAssociation, Study


# from linkml_runtime.dumpers import yaml_dumper


class TestCA(unittest.TestCase):
    # nmdc_schema = "https://raw.githubusercontent.com/microbiomedata/nmdc-schema/main/src/schema/nmdc.yaml"
    nmdc_schema = "../src/schema/nmdc.yaml"

    validator = JsonSchemaDataValidator(nmdc_schema)

    pv1 = PersonValue(has_raw_value="GW Carver")
    pv2 = PersonValue(has_raw_value="L Pasteur")

    ca1 = CreditAssociation(applies_to_person=pv1, applied_roles=["Supervision", "Validation"])
    ca2 = CreditAssociation(applies_to_person=pv2, applied_roles=["Investigation"])

    fs1 = FlatterStudy()
    fs1.flatter_has_credit_associations = ca1

    s1 = Study(id="abc")

    # # why is schema loaded each time?
    validator.validate_object(ca1, target_class=CreditAssociation)
    validator.validate_object(ca2, target_class=CreditAssociation)
    validator.validate_object(fs1, target_class=FlatterStudy)

    #   has credit associations:
    #     domain: study
    #     range: credit association
    #     multivalued: true
    #     inlined: true
    #     description: ...
    #     slot_uri: prov:qualifiedAssociation
    #     annotations:
    #       display_hint:
    #         tag: display_hint
    #         value: Other researchers associated with this study.

    #   inlined:
    #     domain: slot_definition
    #     range: boolean
    #     inherited: true
    #     description: >-
    #       True means that keyed or identified slot appears in an outer structure by value.  False means that only the key
    #       or identifier for the slot appears within the domain, referencing a structure that appears elsewhere.
    #     comments:
    #       - classes without keys or identifiers are necessarily inlined as lists
    #     in_subset:
    #       - basic
    #
    #   inlined_as_list:
    #     domain: slot_definition
    #     range: boolean
    #     inherited: true
    #     description: >-
    #       True means that an inlined slot is represented as a list of range instances.  False means that an inlined slot
    #       is represented as a dictionary, whose key is the slot key or identifier and whose value is the range instance.
    #     comments:
    #       - |-
    #         The default loader will accept either list or dictionary form as input.  This parameter controls internal
    #         representation and output.
    #       - |-
    #         A keyed or identified class with one additional slot can be input in a third form, a dictionary whose key
    #         is the key or identifier and whose value is the one additional element.  This form is still stored according
    #         to the inlined_as_list setting.
    #     in_subset:
    #       - basic

    try:
        s2 = Study(id="abc", has_credit_associations={"ca1": ca1, "ca2": ca2})
        # KeyError: 'applies to person'
    except Exception as e:
        logging.error(traceback.format_exc())

    try:
        s2 = Study(id="abc")
        s2.has_credit_associations.append(ca1)
        # AttributeError: 'dict' object has no attribute 'append'
    except Exception as e:
        logging.error(traceback.format_exc())

    try:
        validator.validate_object(s2, target_class=Study)
    except Exception as e:
        logging.error(traceback.format_exc())

    try:
        fs2 = FlatterStudy()
        fs2.flatter_credit_associations_ial.append(ca1)
        validator.validate_object(fs2, target_class=FlatterStudy)
    except Exception as e:
        logging.error(traceback.format_exc())


if __name__ == '__main__':
    unittest.main()
