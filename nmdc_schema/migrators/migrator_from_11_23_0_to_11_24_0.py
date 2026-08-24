from nmdc_schema.migrators.migrator_base import MigratorBase
from nmdc_schema.migrators.partials.migrator_from_11_23_0_to_11_24_0 import (
    get_migrator_classes,
)


class Migrator(MigratorBase):
    r"""
    Migrates a database between two schemas.

    Partial 1 removes ``principal_investigator`` from Study (delete) and
    DataGeneration (copy onto ``has_credit_associations`` with applied role
    Principal Investigator, then delete).

    Partial 2 standardizes remaining ``PersonValue.orcid`` values onto the
    Bioregistry ``orcid:`` CURIE (nmdc-schema#3327).
    """

    _from_version = "11.23.0"
    _to_version = "11.24.0"

    def upgrade(self, commit_changes: bool = False) -> None:
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.

        This migrator uses partial migrators. It runs them in the order in which they are returned by
        the `get_migrator_classes` function.

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> db = {
        ...     "study_set": [
        ...         {
        ...             "id": "nmdc:sty-1",
        ...             "type": "nmdc:Study",
        ...             "principal_investigator": {"type": "nmdc:PersonValue", "name": "A",
        ...                                       "orcid": "0000-0002-1195-1608"},
        ...             "has_credit_associations": [
        ...                 {"type": "prov:Association",
        ...                  "applies_to_person": {"type": "nmdc:PersonValue",
        ...                                       "name": "B",
        ...                                       "orcid": "0000-0003-2254-399x"}},
        ...             ],
        ...         },
        ...     ],
        ...     "data_generation_set": [
        ...         {
        ...             "id": "nmdc:dgns-1",
        ...             "type": "nmdc:NucleotideSequencing",
        ...             "principal_investigator": {"type": "nmdc:PersonValue", "name": "C",
        ...                                       "orcid": "0000-0002-9108-5083"},
        ...         },
        ...     ],
        ... }
        >>> Migrator(adapter=DictionaryAdapter(database=db)).upgrade()
        >>> "principal_investigator" in db["study_set"][0]
        False
        >>> db["study_set"][0]["has_credit_associations"][0]["applies_to_person"]["orcid"]
        'orcid:0000-0003-2254-399X'
        >>> "principal_investigator" in db["data_generation_set"][0]
        False
        >>> db["data_generation_set"][0]["has_credit_associations"][0]["applies_to_person"]["orcid"]
        'orcid:0000-0002-9108-5083'
        >>> db["data_generation_set"][0]["has_credit_associations"][0]["applied_roles"]
        ['Principal Investigator']

        Args:
            commit_changes: If True, commits the changes. If False (default), performs a dry run or rollback.
        """

        migrator_classes = get_migrator_classes()
        num_migrators = len(migrator_classes)
        for idx, migrator_class in enumerate(migrator_classes):
            self.logger.info(f"Running migrator {idx + 1} of {num_migrators}")
            self.logger.debug(
                f"Migrating from {migrator_class.get_origin_version()} "
                f"to {migrator_class.get_destination_version()}"
            )
            migrator = migrator_class(adapter=self.adapter, logger=self.logger)
            migrator.upgrade(commit_changes=commit_changes)
