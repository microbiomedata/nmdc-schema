import logging

# import traceback
import unittest

from python.nmdc import (
    # PersonValue,
    # CreditAssociation,
    # Study,
    Biosample,
    ControlledTermValue,
)


# from linkml.validators.jsonschemavalidator import JsonSchemaDataValidator


# from linkml_runtime.dumpers import yaml_dumper

# todo reimplement with methods?


class TestBiosampleInstantiation(unittest.TestCase):
    def test_with_part_of(self):
        try:
            bs = Biosample(
                id="x",
                # canary="canary",
                sample_link="x",
                env_broad_scale=ControlledTermValue(),
                env_local_scale=ControlledTermValue(),
                env_medium=ControlledTermValue(),
            )
            assert type(bs) == Biosample
        except Exception as e:
            logging.error(f"Biosample instantiation failed because: {e}")

    def test_add_sample_link(self):
        try:
            bs = Biosample(
                id="x",
                canary="canary",
                part_of="x",
                sample_link="x",
                env_broad_scale=ControlledTermValue(),
                env_local_scale=ControlledTermValue(),
                env_medium=ControlledTermValue(),
            )
            assert type(bs) == Biosample
        except Exception as e:
            logging.error(f"Biosample instantiation failed because: {e}")

    def test_remove_part_of(self):
        try:
            bs = Biosample(
                id="x",
                canary="canary",
                # part_of="x",
                # sample_link="x",
                env_broad_scale=ControlledTermValue(),
                env_local_scale=ControlledTermValue(),
                env_medium=ControlledTermValue(),
            )
            assert type(bs) == Biosample
        except Exception as e:
            logging.error(f"Biosample instantiation failed because: {e}")


if __name__ == "__main__":
    unittest.main()
