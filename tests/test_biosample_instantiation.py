import logging

import unittest

from nmdc_schema.nmdc import (
    Biosample,
    ControlledIdentifiedTermValue, OntologyClass, ControlledTermValue, TimestampValue, QuantityValue,
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
            ecosystem="xyz",
            ecosystem_category="xyz",
            ecosystem_subtype="xyz",
            ecosystem_type="xyz",
            elev=123,
            growth_facil="xyz",
            source_mat_id="xyz",
            specific_ecosystem="xyz",
            store_cond="xyz",
            collection_date=TimestampValue(has_raw_value="xyz"),
            depth=QuantityValue(has_raw_value="xyz"),
            samp_store_temp=QuantityValue(has_raw_value="xyz"),
        )

    def test_invalid_biosample(self):
        with self.assertRaises(Exception):
            bs = Biosample(
                id="x",
                part_of="x",
                env_broad_scale=ControlledIdentifiedTermValue(),
                env_local_scale=ControlledIdentifiedTermValue(),
                env_medium=ControlledIdentifiedTermValue(),
                ecosystem="xyz",
                ecosystem_category="xyz",
                ecosystem_subtype="xyz",
                ecosystem_type="xyz",
                elev=123,
                growth_facil="xyz",
                source_mat_id="xyz",
                specific_ecosystem="xyz",
                store_cond="xyz",
                collection_date=TimestampValue(has_raw_value="xyz"),
                depth=QuantityValue(has_raw_value="xyz"),
                samp_store_temp=QuantityValue(has_raw_value="xyz"),
            )


if __name__ == "__main__":
    unittest.main()
