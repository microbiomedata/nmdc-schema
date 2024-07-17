import logging

import unittest

from nmdc_schema.nmdc import (
    Biosample,
    ControlledIdentifiedTermValue, OntologyClass, ControlledTermValue,
)


class TestBiosampleInstantiation(unittest.TestCase):
    # @unittest.skip(
    #     "why is abs_air_humidity required? moving away from unit tests an instantiation test in gneeral anyway")
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
            samp_name="xxx",
        )

    def test_invalid_biosample(self):
        with self.assertRaises(Exception):
            bs = Biosample(
                id="x",
                part_of="x",
                env_broad_scale=ControlledTermValue(),
                env_local_scale=ControlledTermValue(),
                env_medium=ControlledTermValue(),
                samp_name="xxx",
            )


if __name__ == "__main__":
    unittest.main()
