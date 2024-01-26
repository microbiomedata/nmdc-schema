import logging

import unittest

from nmdc_schema.nmdc import (
    Biosample,
    ControlledIdentifiedTermValue, OntologyClass, ControlledTermValue,
)


class TestBiosampleInstantiation(unittest.TestCase):
    def test_with_part_of(self):

        bs = Biosample(
            id="bs:1",
            associated_studies=[
                "study:1",
                "study:2",
            ],
            env_broad_scale=ControlledIdentifiedTermValue(
                term=OntologyClass(
                    id="ENVO:00000000",
                    type="nmdc:OntologyClass",
                ),
                type="nmdc:ControlledIdentifiedTermValue",
            ),
            env_local_scale=ControlledIdentifiedTermValue(
                term=OntologyClass(
                    id="ENVO:00000000",
                    type="nmdc:OntologyClass",
                ),
                type="nmdc:ControlledIdentifiedTermValue",
            ),
            env_medium=ControlledIdentifiedTermValue(
                term=OntologyClass(
                    id="ENVO:00000000",
                    type="nmdc:OntologyClass",
                ),
                type="nmdc:ControlledIdentifiedTermValue",
            ),
            type="nmdc:Biosample",
        )

    def test_invalid_biosample_empty_env_triad_terms(self):
        with self.assertRaises(Exception):
            bs = Biosample(
                env_broad_scale=ControlledTermValue(),
                env_local_scale=ControlledTermValue(),
                env_medium=ControlledTermValue(),
                id="x",
                associated_studies="x",
                type="nmdc:Biosample",
            )


if __name__ == "__main__":
    unittest.main()
