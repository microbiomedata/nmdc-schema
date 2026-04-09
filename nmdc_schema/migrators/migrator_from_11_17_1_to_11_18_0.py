import re
from typing import Dict, List

from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.17.1"
    _to_version = "11.18.0"

    # This is the regex pattern defined in the schema we're migrating _to_.
    # Reference: The definition of the slot named `doi_value`.
    _target_doi_pattern = r"^doi:10\.\d{2,9}/.*$"

    # This is a variant of regex pattern defined in the schema we're migrating _to_.
    # This variant is "agnostic" to the first part of the `id` value, and is only
    # "picky" about the last part of the `id` value (i.e. the suffix).
    #
    # Reference: The definition of the `id_version` "settings" item, and the
    #            materialized pattern used for `MetagenomeAnnotation.id`.
    #
    _target_workflow_execution_id_pattern = r"^.+\.[1-9]{1}[0-9]{0,}$"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Initialize a map from study ID to a list of names of that study's associated biosamples.
        self.map_from_study_id_to_biosample_names: Dict[str, List[str]] = {}

    def upgrade(self, commit_changes: bool = False) -> None:
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.

        TODO: Consider reducing the number of passes we make through the `biosample_set` collection,
              as a performance improvement.
        """

        # Validate the format of DOIs in studies.
        self.adapter.do_for_each_document(
            collection_name="study_set",
            action=self.validate_study_fields_containing_dois,
        )

        # Validate the format of DOIs in biosamples.
        self.adapter.do_for_each_document(
            collection_name="biosample_set",
            action=self.validate_biosample_fields_containing_dois,
        )

        # Confirm each biosample has a name that is a string.
        self.adapter.do_for_each_document(
            collection_name="biosample_set",
            action=self.validate_biosample_name,
        )

        # Builds a map from study ID to the list of names of that study's associated biosamples.
        self.map_from_study_id_to_biosample_names = {}  # ensure it's initially empty
        self.adapter.do_for_each_document(
            collection_name="biosample_set",
            action=self.add_biosample_name_to_map_of_study_id_to_biosample_names,
        )

        # Confirm no study has multiple associated biosamples having the same name.
        self.fail_if_any_study_has_duplicate_biosample_names()

        # Confirm that the suffix of the `id` of each `WorkflowExecution` conforms to the new schema.
        self.adapter.do_for_each_document(
            collection_name="workflow_execution_set",
            action=self.validate_workflow_execution_id_suffix,
        )

    def validate_study_fields_containing_dois(self, study: dict) -> None:
        r"""
        Validates the format of the `doi_value` value of each `Doi` instance, if any, in
        the specified study's `associated_dois` field.

        Reference: https://microbiomedata.github.io/nmdc-schema/doi_value/

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> database = {'study_set': [
        ...     {'id': 'nmdc:sty-00-1', 'associated_dois': [{'doi_value': 'doi:10.1234/abc'}]},
        ...     {'id': 'nmdc:sty-00-2', 'associated_dois': [{'doi_value': 'doi:10_1234/abc'}]},
        ...     {'id': 'nmdc:sty-00-3'}
        ... ]}
        >>> m = Migrator(adapter=DictionaryAdapter(database=database))
        >>> m.validate_study_fields_containing_dois(database['study_set'][0])  # valid
        >>> m.validate_study_fields_containing_dois(database['study_set'][1])  # invalid: doi_value has invalid format
        Traceback (most recent call last):
        ...
        ValueError: Study nmdc:sty-00-2 has an associated DOI whose value has an invalid format: doi:10_1234/abc
        >>> m.validate_study_fields_containing_dois(database['study_set'][2])  # valid: no associated_dois field
        """

        if "associated_dois" in study:
            for doi_instance in study["associated_dois"]:
                doi = doi_instance["doi_value"]
                if not isinstance(doi, str) or not re.match(self._target_doi_pattern, doi):
                    raise ValueError(f"Study {study['id']} has an associated DOI whose value has an invalid format: {doi}")

    def validate_biosample_fields_containing_dois(self, biosample: dict) -> None:
        r"""
        Validates the format of each DOI in the specified biosample's fields that contain DOIs.
        Distinguishes a DOI from a PMID and a URL by its prefix (out of those three kinds of
        strings, only a DOI can begin with `doi:`—in fact, it _must_ begin with that prefix).

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> database = {'biosample_set': [
        ...     {'id': 'nmdc:bsm-00-1', 'salinity_meth': 'doi:10.1234/abc'},
        ...     {'id': 'nmdc:bsm-00-2', 'salinity_meth': 'doi:10_1234/abc'},
        ...     {'id': 'nmdc:bsm-00-3', 'salinity_meth': 'https://www.example.com'},
        ... ]}
        >>> m = Migrator(adapter=DictionaryAdapter(database=database))
        >>> m.validate_biosample_fields_containing_dois(database['biosample_set'][0])  # valid
        >>> m.validate_biosample_fields_containing_dois(database['biosample_set'][1])  # invalid: DOI has invalid format
        Traceback (most recent call last):
        ...
        ValueError: Biosample nmdc:bsm-00-2 has a salinity_meth DOI having an invalid format: doi:10_1234/abc
        >>> m.validate_biosample_fields_containing_dois(database['biosample_set'][2])  # ignored by this function
        """

        names_of_fields_that_can_contain_doi = [
            "salinity_meth",
            "micro_biomass_c_meth",
            "micro_biomass_n_meth",
            "non_microb_biomass_method",
            "org_nitro_method",
        ]

        for field_name in names_of_fields_that_can_contain_doi:
            if field_name in biosample:
                field_value = biosample[field_name]

                # Check whether this is a value this migrator is responsible for checking.
                if isinstance(field_value, str) and field_value.startswith("doi:"):
                    doi = biosample[field_name]  # concise alias
                    if not re.match(self._target_doi_pattern, doi):
                        raise ValueError(f"Biosample {biosample['id']} has a {field_name} DOI having an invalid format: {doi}")

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

    def validate_workflow_execution_id_suffix(self, workflow_execution: dict) -> None:
        r"""
        Validates that the suffix of the `id` of the specified `WorkflowExecution` conforms to the
        new schema, which says that the first digit of the suffix cannot be 0.

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> database = {'workflow_execution_set': [
        ...     {'id': 'nmdc:wfe-00-1'},
        ...     {'id': 'nmdc:wfe-00-1.1'},
        ...     {'id': 'nmdc:wfe-00-1.2'},
        ...     {'id': 'nmdc:wfe-00-1.0'},
        ...     {'id': 'nmdc:wfe-00-1.01'},
        ...     {'id': 'nmdc:wfe-00-1.10'},
        ... ]}
        >>> m = Migrator(adapter=DictionaryAdapter(database=database))
        >>> m.validate_workflow_execution_id_suffix(database['workflow_execution_set'][0])  # invalid: no suffix
        Traceback (most recent call last):
        ...
        ValueError: WorkflowExecution nmdc:wfe-00-1 has an invalid ID suffix
        >>> m.validate_workflow_execution_id_suffix(database['workflow_execution_set'][1])  # valid
        >>> m.validate_workflow_execution_id_suffix(database['workflow_execution_set'][2])  # valid
        >>> m.validate_workflow_execution_id_suffix(database['workflow_execution_set'][3])  # invalid: suffix has 0 as first digit
        Traceback (most recent call last):
        ...
        ValueError: WorkflowExecution nmdc:wfe-00-1.0 has an invalid ID suffix
        >>> m.validate_workflow_execution_id_suffix(database['workflow_execution_set'][4])  # invalid: suffix has 0 as first digit
        Traceback (most recent call last):
        ...
        ValueError: WorkflowExecution nmdc:wfe-00-1.01 has an invalid ID suffix
        >>> m.validate_workflow_execution_id_suffix(database['workflow_execution_set'][5])  # valid
        """
        if not re.match(self._target_workflow_execution_id_pattern, workflow_execution["id"]):
            raise ValueError(f"WorkflowExecution {workflow_execution['id']} has an invalid ID suffix")
