from nmdc_schema.nmdc_pydantic import Database

def test_create_database_instance():
    """A smoke test to ensure that the nmdc_pydantic.py module can be imported and used to create
    an instance of the Database class."""

    db_instance = Database()
    assert isinstance(db_instance, Database)
