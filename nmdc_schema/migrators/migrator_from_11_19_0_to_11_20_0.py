import re

from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.19.0"
    _to_version = "11.20.0"

    def upgrade(self, commit_changes: bool = False) -> None:
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.
        """

        self.adapter.process_each_document(
            collection_name="study_set",
            pipeline=[self._enhance_study_name]
        )

    def _enhance_study_name(self, study: dict) -> dict:
        r"""
        Prefixes every occurrence of the prefix "micro" or "Micro" within the study's name,
        with a microscope emoji (🔬).

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> database = {
        ...   "study_set": [
        ...     {"name": "Microbial communities in microenvironments"},
        ...     {"name": "Foomicrobar"},
        ...   ]
        ... }
        >>> migrator = Migrator(adapter=DictionaryAdapter(database=database))
        >>> migrator._enhance_study_name(database["study_set"][0])
        {'name': '🔬 Microbial communities in 🔬 microenvironments'}
        >>> migrator._enhance_study_name(database["study_set"][1])
        {'name': 'Foomicrobar'}
        """

        # Short circuit if the study doesn't have a name.
        if "name" not in study:
            return study

        # Replace all occurrences of "micro" or "Micro" with "🔬 micro" or "🔬 Micro", respectively.
        study["name"] = re.sub(
            pattern=r"\b([Mm])icro",
            repl=r"🔬 \1icro",
            string=study["name"],
        )

        return study
