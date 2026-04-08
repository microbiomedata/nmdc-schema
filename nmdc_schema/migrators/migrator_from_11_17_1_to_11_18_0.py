from typing import Dict, List

from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.17.1"
    _to_version = "11.18.0"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Initialize a map from study ID to a list of names of that study's associated biosamples.
        self.map_from_study_id_to_biosample_names: Dict[str, List[str]] = {}

    def upgrade(self, commit_changes: bool = False) -> None:
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.

        This does three things:
        1. Validates that each biosample has a name that is a string.
        2. Builds a map from study ID to the list of names of that study's associated biosamples.
        3. Validates that no study has multiple associated biosamples having the same name.

        We could, technically, do all of this in a single pass through the collection. We opted to
        split it into multiple passes to facilitate testing.
        """

        self.adapter.do_for_each_document(
            collection_name="biosample_set",
            action=self.validate_biosample_name,
        )

        self.map_from_study_id_to_biosample_names = {}  # ensure it's initially empty

        self.adapter.do_for_each_document(
            collection_name="biosample_set",
            action=self.add_biosample_name_to_map_of_study_id_to_biosample_names,
        )

        self.fail_if_any_study_has_duplicate_biosample_names()

    def validate_biosample_name(self, biosample: dict) -> None:
        r"""
        Validates the name of the specified biosample.

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> database = {'biosample_set': [{'id': 'nmdc:bsm-00-1', 'name': 'sample1'}, {'id': 'nmdc:bsm-00-2', 'name': 123}, {'id': 'nmdc:bsm-00-3'}]}
        >>> m = Migrator(adapter=DictionaryAdapter(database=database))
        >>> m.validate_biosample_name(database['biosample_set'][0])  # valid
        >>> m.validate_biosample_name(database['biosample_set'][1])  # invalid: non-string
        Traceback (most recent call last):
        ...
        ValueError: Biosample nmdc:bsm-00-2 lacks a string name
        >>> m.validate_biosample_name(database['biosample_set'][2])  # invalid: missing
        Traceback (most recent call last):
        ...
        ValueError: Biosample nmdc:bsm-00-3 lacks a string name
        """
        if "name" not in biosample or not isinstance(biosample["name"], str):
            raise ValueError(f"Biosample {biosample['id']} lacks a string name")

    def add_biosample_name_to_map_of_study_id_to_biosample_names(self, biosample: dict) -> None:
        r"""
        Adds the name of the specified biosample to the map from study ID to biosample names.
        
        Note: Once this has been invoked for each biosample, the resulting map can be used to
              check for duplicate biosample names within each study.

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> database = {'biosample_set': [
        ...     {'id': 'nmdc:bsm-00-1', 'name': 'apple', 'associated_studies': ['nmdc:sty-00-1', 'nmdc:sty-00-2']},
        ...     {'id': 'nmdc:bsm-00-2', 'name': 'banana', 'associated_studies': ['nmdc:sty-00-1']},
        ...     {'id': 'nmdc:bsm-00-3', 'name': 'apple', 'associated_studies': ['nmdc:sty-00-2']}
        ... ]}
        >>> m = Migrator(adapter=DictionaryAdapter(database=database))
        >>> m.add_biosample_name_to_map_of_study_id_to_biosample_names(database['biosample_set'][0])
        >>> m.add_biosample_name_to_map_of_study_id_to_biosample_names(database['biosample_set'][1])
        >>> m.add_biosample_name_to_map_of_study_id_to_biosample_names(database['biosample_set'][2])
        >>> m.map_from_study_id_to_biosample_names
        {'nmdc:sty-00-1': ['apple', 'banana'], 'nmdc:sty-00-2': ['apple', 'apple']}
        """

        study_ids = biosample["associated_studies"]
        name = biosample["name"]
        for study_id in study_ids:

            # Initialize this study's list, if necessary.
            if study_id not in self.map_from_study_id_to_biosample_names:
                self.map_from_study_id_to_biosample_names[study_id] = []
            
            # Add this biosample's name to the list.
            self.map_from_study_id_to_biosample_names[study_id].append(name)

    def fail_if_any_study_has_duplicate_biosample_names(self) -> None:
        r"""
        Raises an exception if any study has multiple biosamples that have the same name,
        according to the map from study ID to biosample names.

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> m = Migrator(adapter=DictionaryAdapter(database={}))
        >>> m.map_from_study_id_to_biosample_names = {'nmdc:sty-00-1': ['apple', 'banana'], 'nmdc:sty-00-2': ['apple', 'apple']}
        >>> m.fail_if_any_study_has_duplicate_biosample_names()
        Traceback (most recent call last):
        ...
        ValueError: Study nmdc:sty-00-2 has duplicate biosample names: ['apple']
        """

        for study_id, biosample_names in self.map_from_study_id_to_biosample_names.items():
            duplicate_biosample_names = {s for s in biosample_names if biosample_names.count(s) > 1}
            if len(duplicate_biosample_names) > 0:
                sorted_names: list = sorted(duplicate_biosample_names)  # sorting helps with testing
                raise ValueError(f"Study {study_id} has duplicate biosample names: {sorted_names}")
