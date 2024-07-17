import re
from typing import Dict

from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""
    Migrates a database between two schemas.

    Note: In schema version 10.3.0, the `NomAnalysisActivity.id` slot had this `structured_pattern.syntax`:
          "{id_nmdc_prefix}:wfnom-{id_shoulder}-{id_blade}{id_version}{id_locus}"

          In schema version 10.4.0, it has _this_ `structured_pattern.syntax`:
          "{id_nmdc_prefix}:wfnom-{id_shoulder}-{id_blade}{id_version}"

          That specific change was made in commit `a1d5686`:
          https://github.com/microbiomedata/nmdc-schema/commit/a1d5686

          This migrator was designed to migrate `NomAnalysisActivity.id` values to conform to the latter pattern,
          and to update the `was_generated_by` fields of the associated `data_object_set` documents accordingly.
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

    # A mapping from `DataObject.id` value to `NomAnalysisActivity.id` value.
    data_object_id_to_nom_id_map: Dict[str, str] = dict()

    def upgrade(self) -> None:
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""

        self.adapter.process_each_document(
            "nom_analysis_activity_set",
            [
                self.populate_alternative_identifiers,
                self.update_nom_analysis_activity_id,
            ],
        )

        self.adapter.process_each_document(collection_name="data_object_set",
                                           pipeline=[self.update_was_generated_by_field])

    def update_was_generated_by_field(self, data_object: dict) -> dict:
        r"""
        Updates the `was_generated_by` field of the specified `data_object_set` document so that it contains
        the `id` of the `nom_analysis_activity_set` document that "generated" that `data_object_set` document.

        >>> m = Migrator()
        >>> m.data_object_id_to_nom_id_map = {'do1': 'nom1.1'}
        >>> m.update_was_generated_by_field({'id': 'do1', 'was_generated_by': 'nom1'})  # changes `was_generated_by`
        {'id': 'do1', 'was_generated_by': 'nom1.1'}
        >>> m.update_was_generated_by_field({'id': 'do2', 'was_generated_by': 'nom2'})  # no change (not in dictionary)
        {'id': 'do2', 'was_generated_by': 'nom2'}
        """

        data_object_id = data_object["id"]
        if data_object_id in self.data_object_id_to_nom_id_map.keys():
            data_object["was_generated_by"] = self.data_object_id_to_nom_id_map[data_object_id]

        return data_object

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
        If the specified `nom_analysis_activity` document has an invalid `id`,
        this function does two things:
        1. Make the `id` valid (by appending a version number to it); and
        2. If it has a `has_output` field (which is a list) consisting of a single item,
           add an entry to the `data_object_id_to_nom_id_map` dictionary, using
           the `has_output` value as the key and the newly-valid `id` as the value.
           Raise an exception if the `has_output` list contains more than 1 item.

        If the specified `nom_analysis_activity` document already has a valid `id`,
        this function does nothing.

        >>> m = Migrator()
        >>> # test: adds version number to id
        >>> m.update_nom_analysis_activity_id({'id': 'nmdc:wfnom-13-7yf9qj85'})
        {'id': 'nmdc:wfnom-13-7yf9qj85.1'}
        >>> # test: if version number is already there, no change
        >>> m.update_nom_analysis_activity_id({'id': 'nmdc:wfnom-13-7yf9qj85.1'})
        {'id': 'nmdc:wfnom-13-7yf9qj85.1'}

        Test the production of the ID map.

        >>> m.data_object_id_to_nom_id_map = {}
        >>> m.update_nom_analysis_activity_id({'id': 'nmdc:wfnom-13-7yf9qj85',
        ...                                    'has_output': ['do1']})  # creates dict entry
        {'id': 'nmdc:wfnom-13-7yf9qj85.1', 'has_output': ['do1']}
        >>> len(m.data_object_id_to_nom_id_map.keys())
        1
        >>> m.data_object_id_to_nom_id_map['do1']
        'nmdc:wfnom-13-7yf9qj85.1'
        >>> m.update_nom_analysis_activity_id({'id': 'nmdc:wfnom-13-7yf9qj86',
        ...                                    'has_output': ['do2']})  # creates other dict entry
        {'id': 'nmdc:wfnom-13-7yf9qj86.1', 'has_output': ['do2']}
        >>> len(m.data_object_id_to_nom_id_map.keys())
        2
        >>> m.data_object_id_to_nom_id_map['do1']
        'nmdc:wfnom-13-7yf9qj85.1'
        >>> m.data_object_id_to_nom_id_map['do2']
        'nmdc:wfnom-13-7yf9qj86.1'
        """
        nom_analysis_activity_id = nom_analysis_activity["id"]

        self.logger.info(
            f"Checking ID for NomAnalysisActivity: {nom_analysis_activity_id}"
        )

        # Get the `has_output` value, if any, of the `nom_analysis_activity` document;
        # treating `null` values as empty lists.
        nom_outputs = []
        if "has_output" in nom_analysis_activity.keys():
            if nom_analysis_activity["has_output"] is not None:
                nom_outputs = nom_analysis_activity["has_output"]

        # If the `id` is invalid, do two things:
        # 1. Append a version number to it; and
        # 2. Record the `id` of the `DataObject`, if any, that is the output of this `NomAnalysisActivity`.
        if not self.is_valid_id(nom_analysis_activity_id):
            nom_analysis_activity_id_new = f"{nom_analysis_activity_id}.1"
            nom_analysis_activity["id"] = nom_analysis_activity_id_new

            if len(nom_outputs) > 1:
                raise ValueError(f"NomAnalysisActivity ({nom_analysis_activity_id}) 'has_output' field "
                                 f"contains more than one item. Contains: {nom_outputs}")
            elif len(nom_outputs) == 1:
                data_object_id = nom_outputs[0]
                if data_object_id in self.data_object_id_to_nom_id_map.keys():
                    raise ValueError(f"Multiple NomAnalysisActivity instances have same DataObject ({data_object_id}) "
                                     f"instance as their output.")
                self.data_object_id_to_nom_id_map[data_object_id] = nom_analysis_activity_id_new
            else:  # This `NomAnalysisActivity` instance didn't have any output.
                pass

        return nom_analysis_activity
