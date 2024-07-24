import logging

import unittest

from nmdc_schema.get_nmdc_view import ViewGetter


class Getters(unittest.TestCase):
    def test_view_getter(self):
        view_getter = ViewGetter()
        nmdc_view = view_getter.get_view()
        self.assertEqual(nmdc_view.schema.name, "NMDC")


if __name__ == "__main__":
    unittest.main()
