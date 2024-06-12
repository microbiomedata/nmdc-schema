import re

from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas.
    """

    _from_version = "10.3.0"
    _to_version = "10.4.0"

    pattern = re.compile(r"\.[0-9]+$")

    def upgrade(self) -> None:
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""

        self.adapter.process_each_document(
            "nom_analysis_activity_set", [self.populate_alternative_identifiers,self.update_nom_analysis_activity_id]
        )
    
    def is_valid_id(self, s: str) -> bool:
        r"""
        Helper function that checks whether a string is a valid ID (has a version number).
        Reference: https://docs.python.org/3/library/re.html#re.Pattern.search

        >>> m = Migrator()
        >>> m.is_valid_id("invalid_id")
        False
        >>> m.is_valid_id("valid.1")
        True
        >>> m.is_valid_id("valid.123")
        True
        """

        return self.pattern.search(s) is not None


    def populate_alternative_identifiers(self, nom_analysis_activity: dict) -> dict:
        r"""
        Checks to see if a nom_analysis_activity has any alternative_identifiers. If there are any, then the ID is added if it's invalid.
        If there are not then the alternative_identifiers slot is created if needed with the invalid id as a value.

        >>> m = Migrator()
        >>> m.populate_alternative_identifiers({'id': '1'}) # test: adds alternative identifiers
        {'id': '1', 'alternative_identifiers': ['1']}
        >>> m.populate_alternative_identifiers({'id': '1.1','alternative_identifiers': ['alt 1']}) # test no change, alternative identifiers already present with valid id
        {'id': '1.1', 'alternative_identifiers': ['alt 1']}
        >>> m.populate_alternative_identifiers({'id': '1.1'}) # test no change, alternative identifiers not present, but with valid id
        {'id': '1.1'}

        """
        self.logger.info(f"Checking alternative_identifiers for NomAnalysisActivity: {nom_analysis_activity['id']}")

        nom_id = nom_analysis_activity['id']
        if not self.is_valid_id(nom_id):
            if "alternative_identifiers" not in nom_analysis_activity.keys():
                nom_analysis_activity["alternative_identifiers"] = []
            nom_analysis_activity["alternative_identifiers"].append(nom_id)

        return nom_analysis_activity

    def update_nom_analysis_activity_id(self, nom_analysis_activity: dict) -> dict:
        r"""
        Updates a nom_analysis_activity's id to contain a version number (.1),
        if it has no version number.

        >>> m = Migrator()
        >>> m.update_nom_analysis_activity_id({'id': '1'}) # test: adds version number to id
        {'id': '1.1'}
        >>> m.update_nom_analysis_activity_id({'id': '1.1'}) # test if version number is already there, no change
        {'id': '1.1'}

        """
        self.logger.info(f"Checking ID for NomAnalysisActivity: {nom_analysis_activity['id']}")

        
        # If there's no version number, add one
        if not self.is_valid_id(nom_analysis_activity["id"]):
            nom_analysis_activity['id'] = str(nom_analysis_activity['id']) + ".1"

        return nom_analysis_activity