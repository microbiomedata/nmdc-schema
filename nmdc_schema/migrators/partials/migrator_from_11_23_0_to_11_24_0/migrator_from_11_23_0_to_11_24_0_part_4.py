"""Reshape credit-association agents for Person and applies_to_agent.

See https://github.com/microbiomedata/nmdc-schema/issues/3375
"""

from __future__ import annotations

from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Rename PersonValue to Person, drop has_raw_value, and rename applies_to_person.

    Walks ``has_credit_associations`` on ``study_set`` and ``data_generation_set``
    after part 3 has filled ``name``. Under 11.23, ``applies_to_person`` is required
    and ranged to ``PersonValue``, so ``type`` is ``nmdc:PersonValue``.
    """

    _from_version = "11.24.0.part_3"
    _to_version = "11.24.0.part_4"

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
        ...                                       "name": "A",
        ...                                       "has_raw_value": "A",
        ...                                       "orcid": "orcid:0000-0002-1195-1608"}},
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
        ...                                       "name": "C",
        ...                                       "has_raw_value": "C"}},
        ...             ],
        ...         },
        ...     ],
        ... }
        >>> Migrator(adapter=DictionaryAdapter(database=db)).upgrade()
        >>> db["study_set"][0]["has_credit_associations"][0]["applies_to_agent"]
        {'type': 'nmdc:Person', 'name': 'A', 'orcid': 'orcid:0000-0002-1195-1608'}
        >>> db["data_generation_set"][0]["has_credit_associations"][0]["applies_to_agent"]
        {'type': 'nmdc:Person', 'name': 'C'}
        """
        self._warn_if_commit_ignored(commit_changes)
        self.adapter.process_each_document(
            "study_set", [self.reshape_document_credit_agents]
        )
        self.adapter.process_each_document(
            "data_generation_set", [self.reshape_document_credit_agents]
        )

    def reshape_document_credit_agents(self, document: dict) -> dict:
        r"""Rename applies_to_person, set type to Person, and drop has_raw_value.

        >>> m = Migrator()
        >>> m.reshape_document_credit_agents(
        ...     {"id": "nmdc:sty-1",
        ...      "has_credit_associations": [
        ...          {"applies_to_person": {"type": "nmdc:PersonValue",
        ...                                "name": "Nancy Hess",
        ...                                "has_raw_value": "Nancy hess"}},
        ...          {"applies_to_person": {"type": "nmdc:PersonValue",
        ...                                "name": "James Stegen"}},
        ...      ]}
        ... )
        {'id': 'nmdc:sty-1', 'has_credit_associations': [{'applies_to_agent': {'type': 'nmdc:Person', 'name': 'Nancy Hess'}}, {'applies_to_agent': {'type': 'nmdc:Person', 'name': 'James Stegen'}}]}
        >>> m.reshape_document_credit_agents({"id": "nmdc:sty-2"})
        {'id': 'nmdc:sty-2'}
        """
        for association in document.get("has_credit_associations") or []:
            if not isinstance(association, dict):
                continue
            person = association.pop("applies_to_person", None)
            if not isinstance(person, dict):
                continue
            person["type"] = "nmdc:Person"
            person.pop("has_raw_value", None)
            association["applies_to_agent"] = person
        return document
