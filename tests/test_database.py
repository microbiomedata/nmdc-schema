import unittest

from nmdc_schema.nmdc import Database


class TestDatabase(unittest.TestCase):
    def test_database(self):
        """Test that a nmdc:Database instance can be created."""
        database = Database()

        # Not much to assert here; this is mainly a smoke test
        assert database.biosample_set == []
