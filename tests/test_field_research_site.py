import unittest

from nmdc_schema.nmdc import FieldResearchSite, TextValue, GeolocationValue


class TestBiosampleInstantiation(unittest.TestCase):
    def test_with_part_of(self):
        frs = FieldResearchSite(
            id="frs:1",
            geo_loc_name=TextValue(has_raw_value="USA, California, Stockton"),
            lat_lon=GeolocationValue(
                latitude=37.9577,
                longitude=-121.2908)
        )
        self.assertIsNotNone(frs)


if __name__ == "__main__":
    unittest.main()
