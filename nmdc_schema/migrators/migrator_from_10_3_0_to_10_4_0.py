import re

from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""
    Migrates a database between two schemas.

    Note: In schema version 10.3.0, the `NomAnalysisActivity.id` slot had this `structured_pattern.syntax`:
          "{id_nmdc_prefix}:wfnom-{id_shoulder}-{id_blade}{id_version}{id_locus}"

          In schema version 10.4.0, it had _this_ `structured_pattern.syntax`:
          "{id_nmdc_prefix}:wfnom-{id_shoulder}-{id_blade}{id_version}"

          That specific change was made in commit `a1d5686`:
          https://github.com/microbiomedata/nmdc-schema/commit/a1d5686

          This migrator was designed to migrate `NomAnalysisActivity.id` values to conform to the latter pattern.
    """

    _from_version = "10.3.0"
    _to_version = "10.4.0"

    # Note: I think the author of the migrator got this regex pattern by running `$ make all`
    #       and getting this pattern from the file `project/nmdc_materialized_patterns.yaml`.
    #       Reference: https://github.com/microbiomedata/nmdc-schema/pull/2059#discussion_r1639005255
    #
    pattern = re.compile(
        r"(^(nmdc):wfnom-([0-9][a-z]{0,6}[0-9])-([A-Za-z0-9]{1,})(\.[0-9]{1,})$)"
    )

    def upgrade(self) -> None:
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""

        self.adapter.process_each_document(
            "nom_analysis_activity_set",
            [
                self.populate_alternative_identifiers,
                self.update_nom_analysis_activity_id,
            ],
        )

    def is_valid_id(self, s: str) -> bool:
        r"""
        Helper function that checks whether a string is a valid ID.
        Reference: https://docs.python.org/3/library/re.html#re.Pattern.search

        >>> m = Migrator()
        >>> m.is_valid_id("nmdc:wfnom-13-7yf9qj85")
        False
        >>> m.is_valid_id("nmdc:wfnom-13-7yf9qj85.1")
        True
        >>> m.is_valid_id("nmdc:wfnom-13-7yf9qj85.10")
        True
        """

        return self.pattern.search(s) is not None

    def populate_alternative_identifiers(self, nom_analysis_activity: dict) -> dict:
        r"""
        Checks to see if a nom_analysis_activity has any alternative_identifiers.
        If there are any, then the ID is added if it's invalid.
        If there are not any, then the alternative_identifiers slot is created
        if needed with the invalid id as a value.

        >>> m = Migrator()
        >>> # test: adds alternative identifiers
        >>> m.populate_alternative_identifiers({'id': 'nmdc:wfnom-13-7yf9qj85'})
        {'id': 'nmdc:wfnom-13-7yf9qj85', 'alternative_identifiers': ['nmdc:wfnom-13-7yf9qj85']}
        >>> # test: no change, alternative identifiers already present with valid id
        >>> m.populate_alternative_identifiers({'id': 'nmdc:wfnom-13-7yf9qj85.1',
        ...                                     'alternative_identifiers': ['alt 1']})
        {'id': 'nmdc:wfnom-13-7yf9qj85.1', 'alternative_identifiers': ['alt 1']}
        >>> # test: no change, alternative identifiers not present, but with valid id
        >>> m.populate_alternative_identifiers({'id': 'nmdc:wfnom-13-7yf9qj85.1'})
        {'id': 'nmdc:wfnom-13-7yf9qj85.1'}

        """
        self.logger.info(
            f"Checking alternative_identifiers for NomAnalysisActivity: {nom_analysis_activity['id']}"
        )

        nom_id = nom_analysis_activity["id"]
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
        >>> # test: adds version number to id
        >>> m.update_nom_analysis_activity_id({'id': 'nmdc:wfnom-13-7yf9qj85'})
        {'id': 'nmdc:wfnom-13-7yf9qj85.1'}
        >>> # test: if version number is already there, no change
        >>> m.update_nom_analysis_activity_id({'id': 'nmdc:wfnom-13-7yf9qj85.1'})
        {'id': 'nmdc:wfnom-13-7yf9qj85.1'}

        """
        self.logger.info(
            f"Checking ID for NomAnalysisActivity: {nom_analysis_activity['id']}"
        )

        # If there's no version number, add one
        if not self.is_valid_id(nom_analysis_activity["id"]):
            nom_analysis_activity["id"] = str(nom_analysis_activity["id"]) + ".1"

        return nom_analysis_activity
