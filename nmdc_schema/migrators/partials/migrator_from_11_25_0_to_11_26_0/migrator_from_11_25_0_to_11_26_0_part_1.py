"""Normalize malformed EFO CURIEs in Biosample ``term.id`` values.

https://github.com/microbiomedata/nmdc-schema/pull/3573 changes the ``EFO`` expansion to
``http://www.ebi.ac.uk/efo/EFO_``, so the local part of an ``EFO:`` CURIE must be the bare
number. Production biosamples also hold a lowercase ``efo:`` prefix, which the schema does not
declare. This partial rewrites both forms:

- ``EFO:EFO_0001779`` and ``efo:EFO_0001779`` become ``EFO:0001779``

Only ``term.id`` values are changed. ``has_raw_value`` is the submitter's text and is kept.
A scan of all 27,448 production biosamples on 2026-11-10 found 345 such ids in 345
biosamples: 205 ``EFO:EFO_0001779``, 105 ``efo:EFO_0001759`` and 35 ``efo:EFO_0004725``.
Other collections were not scanned.
"""

from __future__ import annotations

import re

from nmdc_schema.migrators.adapters.mongo_adapter import MongoAdapter
from nmdc_schema.migrators.migrator_base import MigratorBase

EFO_WITH_REPEATED_PREFIX = re.compile(r"^(?:EFO|efo):EFO_(\d+)$")


def normalize_term_id(term_id: str) -> str:
    r"""Return the normalized CURIE, or the input unchanged when no rule applies.

    >>> normalize_term_id("EFO:EFO_0001779")
    'EFO:0001779'
    >>> normalize_term_id("efo:EFO_0004725")
    'EFO:0004725'

    Values that are already well formed, or that match no rule, are returned unchanged:

    >>> normalize_term_id("EFO:0001779")
    'EFO:0001779'
    >>> normalize_term_id("ENVO:00002034")
    'ENVO:00002034'
    >>> normalize_term_id("NCBI:txid15368")
    'NCBI:txid15368'
    """
    efo_match = EFO_WITH_REPEATED_PREFIX.fullmatch(term_id)
    if efo_match:
        return f"EFO:{efo_match.group(1)}"
    return term_id


class Migrator(MigratorBase):
    r"""Rewrite malformed EFO CURIEs in ``term.id`` values on ``biosample_set``."""

    _from_version = "11.25.0"
    _to_version = "11.26.0.part_1"

    def upgrade(self, commit_changes: bool = False) -> None:
        r"""
        Normalize ``term.id`` in every ``biosample_set`` document.

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> db = {
        ...     "biosample_set": [
        ...         {
        ...             "id": "nmdc:bsm-1",
        ...             "type": "nmdc:Biosample",
        ...             "experimental_factor": {
        ...                 "type": "nmdc:ControlledTermValue",
        ...                 "has_raw_value": "metabolite measurement [efo:EFO_0004725]",
        ...                 "term": {"type": "nmdc:OntologyClass", "id": "efo:EFO_0004725"},
        ...             },
        ...         },
        ...         {
        ...             "id": "nmdc:bsm-2",
        ...             "type": "nmdc:Biosample",
        ...             "env_medium": {
        ...                 "type": "nmdc:ControlledIdentifiedTermValue",
        ...                 "term": {"type": "nmdc:OntologyClass", "id": "ENVO:00001998"},
        ...             },
        ...         },
        ...     ]
        ... }
        >>> Migrator(adapter=DictionaryAdapter(database=db)).upgrade()
        >>> db["biosample_set"][0]["experimental_factor"]["term"]["id"]
        'EFO:0004725'
        >>> db["biosample_set"][0]["experimental_factor"]["has_raw_value"]
        'metabolite measurement [efo:EFO_0004725]'
        >>> db["biosample_set"][1]["env_medium"]["term"]["id"]
        'ENVO:00001998'
        """
        self._warn_if_commit_ignored(commit_changes)

        if isinstance(self.adapter, MongoAdapter):
            try:
                self.adapter.process_collections_in_transaction(
                    collection_names=["biosample_set"],
                    document_processor=self.normalize_document_term_ids,
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
            self.adapter.process_each_document("biosample_set", [self.normalize_document_term_ids])
            if not commit_changes:
                self.logger.info(
                    "Note: Non-MongoDB adapter doesn't support rollback - changes are applied immediately"
                )

    def normalize_document_term_ids(self, document: dict) -> dict:
        r"""Normalize every ``term.id`` found anywhere in the document, including inside lists.

        >>> m = Migrator()
        >>> m.normalize_document_term_ids(
        ...     {"id": "nmdc:bsm-3",
        ...      "chem_administration": [{"term": {"id": "EFO:EFO_0000001"}}, {"term": {"id": "CHEBI:41981"}}],
        ...      "experimental_factor": {"term": {"id": "EFO:EFO_0001779"}, "has_raw_value": "EFO:EFO_0001779"}}
        ... )
        {'id': 'nmdc:bsm-3', 'chem_administration': [{'term': {'id': 'EFO:0000001'}}, {'term': {'id': 'CHEBI:41981'}}], 'experimental_factor': {'term': {'id': 'EFO:0001779'}, 'has_raw_value': 'EFO:EFO_0001779'}}
        >>> m.normalize_document_term_ids({"id": "nmdc:bsm-4"})
        {'id': 'nmdc:bsm-4'}
        """
        self._normalize_in_place(document)
        return document

    def _normalize_in_place(self, node: object) -> None:
        if isinstance(node, dict):
            term = node.get("term")
            if isinstance(term, dict) and isinstance(term.get("id"), str):
                normalized = normalize_term_id(term["id"])
                if normalized != term["id"]:
                    self.logger.info(f"Rewriting term id {term['id']} to {normalized}")
                    term["id"] = normalized
            for value in node.values():
                self._normalize_in_place(value)
        elif isinstance(node, list):
            for value in node:
                self._normalize_in_place(value)
