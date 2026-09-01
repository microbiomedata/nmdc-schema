"""Fill PersonValue.name from has_raw_value when name is missing.

See https://github.com/microbiomedata/nmdc-schema/issues/2458
"""

from nmdc_schema.migrators.adapters.mongo_adapter import MongoAdapter
from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Require PersonValue.name by copying has_raw_value onto missing names.

    Walks ``has_credit_associations[].applies_to_person`` on ``study_set`` and
    ``data_generation_set`` after part 1 has already moved DataGeneration
    principal investigators onto credit associations. Production snapshot
    2026-08-24 had 405 fillable DataGeneration PIs and 0 records missing both
    slots; unfillable values raise.
    """

    _from_version = "11.24.0.part_2"
    _to_version = "11.24.0.part_3"

    def upgrade(self, commit_changes: bool = False) -> None:
        r"""
        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> db = {
        ...     "study_set": [
        ...         {
        ...             "id": "nmdc:sty-1",
        ...             "type": "nmdc:Study",
        ...             "has_credit_associations": [
        ...                 {"type": "prov:Association",
        ...                  "applies_to_person": {"type": "nmdc:PersonValue",
        ...                                       "name": "A"}},
        ...                 {"type": "prov:Association",
        ...                  "applies_to_person": {"type": "nmdc:PersonValue",
        ...                                       "has_raw_value": "B"}},
        ...             ],
        ...         },
        ...     ],
        ...     "data_generation_set": [
        ...         {
        ...             "id": "nmdc:dgns-1",
        ...             "type": "nmdc:NucleotideSequencing",
        ...             "has_credit_associations": [
        ...                 {"type": "prov:Association",
        ...                  "applied_roles": ["Principal Investigator"],
        ...                  "applies_to_person": {"type": "nmdc:PersonValue",
        ...                                       "has_raw_value": "James Stegen"}},
        ...             ],
        ...         },
        ...     ],
        ... }
        >>> Migrator(adapter=DictionaryAdapter(database=db)).upgrade()
        >>> db["study_set"][0]["has_credit_associations"][0]["applies_to_person"]["name"]
        'A'
        >>> db["study_set"][0]["has_credit_associations"][1]["applies_to_person"]["name"]
        'B'
        >>> db["data_generation_set"][0]["has_credit_associations"][0]["applies_to_person"]["name"]
        'James Stegen'
        """
        self._warn_if_commit_ignored(commit_changes)

        if isinstance(self.adapter, MongoAdapter):
            try:
                self.adapter.process_collections_in_transaction(
                    collection_names=["study_set", "data_generation_set"],
                    document_processor=self.fill_document_personvalue_names,
                    commit_changes=commit_changes,
                )
                if commit_changes:
                    self.logger.info("Transaction committed (changes have been saved)")
                else:
                    self.logger.info("Transaction rolled back (no changes were committed)")
            except Exception as e:
                self.logger.error(f"Migration failed: {e}")
                raise
        else:
            self.adapter.process_each_document(
                "study_set", [self.fill_document_personvalue_names]
            )
            self.adapter.process_each_document(
                "data_generation_set", [self.fill_document_personvalue_names]
            )
            if not commit_changes:
                self.logger.info(
                    "Note: Non-MongoDB adapter doesn't support rollback - changes are applied immediately"
                )

    def fill_document_personvalue_names(self, document: dict) -> dict:
        r"""Copy has_raw_value onto missing name on each credit-association PersonValue.

        Existing non-whitespace ``name`` is left unchanged, including casing.
        Missing, empty, or whitespace ``name`` is filled from ``has_raw_value``.

        >>> m = Migrator()
        >>> m.fill_document_personvalue_names(
        ...     {"id": "nmdc:dgns-1",
        ...      "has_credit_associations": [
        ...          {"applies_to_person": {"type": "nmdc:PersonValue",
        ...                                "name": "Nancy Hess",
        ...                                "has_raw_value": "Nancy hess"}},
        ...          {"applies_to_person": {"type": "nmdc:PersonValue",
        ...                                "has_raw_value": "James Stegen"}},
        ...          {"applies_to_person": {"name": "", "has_raw_value": "Eoin Brodie"}},
        ...          {"applies_to_person": {"name": "   ", "has_raw_value": "  Jennifer Pett-Ridge  "}},
        ...      ]}
        ... )
        {'id': 'nmdc:dgns-1', 'has_credit_associations': [{'applies_to_person': {'type': 'nmdc:PersonValue', 'name': 'Nancy Hess', 'has_raw_value': 'Nancy hess'}}, {'applies_to_person': {'type': 'nmdc:PersonValue', 'has_raw_value': 'James Stegen', 'name': 'James Stegen'}}, {'applies_to_person': {'name': 'Eoin Brodie', 'has_raw_value': 'Eoin Brodie'}}, {'applies_to_person': {'name': 'Jennifer Pett-Ridge', 'has_raw_value': '  Jennifer Pett-Ridge  '}}]}
        >>> m.fill_document_personvalue_names({"id": "nmdc:sty-2"})
        {'id': 'nmdc:sty-2'}
        >>> m.fill_document_personvalue_names(
        ...     {"id": "nmdc:dgns-3",
        ...      "has_credit_associations": [{"applies_to_person": {"type": "nmdc:PersonValue"}}]}
        ... )
        Traceback (most recent call last):
            ...
        ValueError: In nmdc:dgns-3: PersonValue has no usable name or has_raw_value
        """
        document_id = document.get("id", "<unknown id>")
        try:
            for association in document.get("has_credit_associations") or []:
                if not isinstance(association, dict):
                    continue
                person = association.get("applies_to_person")
                if not isinstance(person, dict):
                    continue
                name = person.get("name")
                if isinstance(name, str) and name.strip():
                    continue
                raw = person.get("has_raw_value")
                if isinstance(raw, str) and raw.strip():
                    person["name"] = raw.strip()
                    continue
                raise ValueError("PersonValue has no usable name or has_raw_value")
        except ValueError as exc:
            raise ValueError(f"In {document_id}: {exc}") from None
        return document
