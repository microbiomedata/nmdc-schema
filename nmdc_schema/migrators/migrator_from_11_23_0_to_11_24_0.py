from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Remove principal_investigator from Study and DataGeneration records.

    Study: delete the slot. PI information is expected to already live on
    has_credit_associations (issues#1837).

    DataGeneration: that class did not previously allow has_credit_associations,
    so copy principal_investigator into a new Principal Investigator credit
    association and delete the old slot.
    """

    _from_version = "11.23.0"
    _to_version = "11.24.0"

    def upgrade(self, commit_changes: bool = False) -> None:
        r"""
        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> db = {
        ...     "study_set": [
        ...         {"id": "nmdc:sty-1", "type": "nmdc:Study",
        ...          "principal_investigator": {"type": "nmdc:PersonValue", "name": "A"}},
        ...         {"id": "nmdc:sty-2", "type": "nmdc:Study"},
        ...     ],
        ...     "data_generation_set": [
        ...         {"id": "nmdc:dgns-1", "type": "nmdc:NucleotideSequencing",
        ...          "principal_investigator": {"type": "nmdc:PersonValue", "name": "B", "email": "b@x.org"}},
        ...         {"id": "nmdc:dgns-2", "type": "nmdc:NucleotideSequencing"},
        ...     ],
        ... }
        >>> Migrator(adapter=DictionaryAdapter(database=db)).upgrade()
        >>> "principal_investigator" in db["study_set"][0]
        False
        >>> "principal_investigator" in db["study_set"][1]
        False
        >>> db["data_generation_set"][0]["has_credit_associations"]
        [{'type': 'prov:Association', 'applies_to_person': {'type': 'nmdc:PersonValue', 'name': 'B', 'email': 'b@x.org'}, 'applied_roles': ['Principal Investigator']}]
        >>> "principal_investigator" in db["data_generation_set"][0]
        False
        >>> "has_credit_associations" in db["data_generation_set"][1]
        False
        """
        self._warn_if_commit_ignored(commit_changes)
        self.adapter.process_each_document("study_set", [self.drop_study_principal_investigator])
        self.adapter.process_each_document(
            "data_generation_set", [self.move_data_generation_principal_investigator]
        )

    def drop_study_principal_investigator(self, study: dict) -> dict:
        r"""Delete principal_investigator from a Study document. Do not copy it.

        >>> m = Migrator()
        >>> m.drop_study_principal_investigator(
        ...     {"id": "nmdc:sty-1", "principal_investigator": {"name": "A"}}
        ... )
        {'id': 'nmdc:sty-1'}
        >>> m.drop_study_principal_investigator({"id": "nmdc:sty-2"})
        {'id': 'nmdc:sty-2'}
        """
        if "principal_investigator" in study:
            study.pop("principal_investigator")
        return study

    def move_data_generation_principal_investigator(self, record: dict) -> dict:
        r"""Move principal_investigator onto a new has_credit_associations list.

        >>> m = Migrator()
        >>> m.move_data_generation_principal_investigator(
        ...     {"id": "nmdc:dgns-1",
        ...      "principal_investigator": {"type": "nmdc:PersonValue", "name": "B", "email": "b@x.org"}}
        ... )
        {'id': 'nmdc:dgns-1', 'has_credit_associations': [{'type': 'prov:Association', 'applies_to_person': {'type': 'nmdc:PersonValue', 'name': 'B', 'email': 'b@x.org'}, 'applied_roles': ['Principal Investigator']}]}
        >>> m.move_data_generation_principal_investigator({"id": "nmdc:dgns-2"})
        {'id': 'nmdc:dgns-2'}
        """
        pi = record.pop("principal_investigator", None)
        if not isinstance(pi, dict):
            return record

        record["has_credit_associations"] = [
            {
                "type": "prov:Association",
                "applies_to_person": pi,
                "applied_roles": ["Principal Investigator"],
            }
        ]
        return record
