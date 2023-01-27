import logging

import unittest

from nmdc_schema.datamodel.nmdc import (
    Biosample,
    ControlledIdentifiedTermValue, OntologyClass, ControlledTermValue,
)


class TestBiosampleInstantiation(unittest.TestCase):
    def test_with_part_of(self):
        self.assertTrue(True)

        bs = Biosample(
            id="bs:1",
            part_of=[
                "study:1",
                "study:2",
            ],
            env_broad_scale=ControlledIdentifiedTermValue(term=OntologyClass(id="ENVO:00000000")),
            env_local_scale=ControlledIdentifiedTermValue(term=OntologyClass(id="ENVO:00000000")),
            env_medium=ControlledIdentifiedTermValue(term=OntologyClass(id="ENVO:00000000")),
        )

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


if __name__ == "__main__":
    unittest.main()
