import unittest

from nmdc_schema.nmdc import FieldResearchSite


class TestBiosampleInstantiation(unittest.TestCase):
    def test_with_part_of(self):
        frs = FieldResearchSite(id="frs:1", )
        self.assertIsNotNone(frs)


if __name__ == "__main__":
    unittest.main()
