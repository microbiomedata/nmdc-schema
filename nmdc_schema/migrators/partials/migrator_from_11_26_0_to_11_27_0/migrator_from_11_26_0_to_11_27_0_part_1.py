"""Rewrite ``NCBI:txid`` taxon ids in Biosample ``term.id`` values to ``NCBITaxon:``.

The ``NCBI`` prefix expanded to the placeholder ``http://example.org/ncbitaxon/``
(https://github.com/microbiomedata/issues/issues/893), and 11.27.0 removes it. Its only
production use was ``host_taxid``, so this partial rewrites those ids:

- ``NCBI:txid15368`` becomes ``NCBITaxon:15368``

Only ``term.id`` values are changed. ``has_raw_value`` is the submitter's text and is kept.
A scan of all 27,448 production biosamples on 2026-11-10 found 105 such ids, all
``NCBI:txid15368`` in ``host_taxid``. The other collections, except functional_annotation_agg,
had no values starting with ``NCBI:``.
"""

from __future__ import annotations

import re

from nmdc_schema.migrators.adapters.mongo_adapter import MongoAdapter
from nmdc_schema.migrators.migrator_base import MigratorBase

NCBI_TXID = re.compile(r"^NCBI:txid(\d+)$")


def normalize_term_id(term_id: str) -> str:
    r"""Return the ``NCBITaxon:`` CURIE for an ``NCBI:txid`` id, or the input unchanged.

    >>> normalize_term_id("NCBI:txid15368")
    'NCBITaxon:15368'
    >>> normalize_term_id("NCBITaxon:15368")
    'NCBITaxon:15368'
    >>> normalize_term_id("NCBI:txidABC")
    'NCBI:txidABC'
    >>> normalize_term_id("EFO:0001779")
    'EFO:0001779'
    """
    ncbi_match = NCBI_TXID.fullmatch(term_id)
    if ncbi_match:
        return f"NCBITaxon:{ncbi_match.group(1)}"
    return term_id


class Migrator(MigratorBase):
    r"""Rewrite ``NCBI:txid`` term ids on ``biosample_set`` to ``NCBITaxon:``."""

    _from_version = "11.26.0"
    _to_version = "11.27.0.part_1"

    def upgrade(self, commit_changes: bool = False) -> None:
        r"""
        Normalize ``term.id`` in every ``biosample_set`` document.

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> db = {
        ...     "biosample_set": [
        ...         {
        ...             "id": "nmdc:bsm-1",
        ...             "type": "nmdc:Biosample",
        ...             "host_taxid": {
        ...                 "type": "nmdc:ControlledIdentifiedTermValue",
        ...                 "has_raw_value": "Brachypodium distachyon [NCBI:txid15368]",
        ...                 "term": {"type": "nmdc:OntologyClass", "id": "NCBI:txid15368"},
        ...             },
        ...         },
        ...         {
        ...             "id": "nmdc:bsm-2",
        ...             "type": "nmdc:Biosample",
        ...             "host_taxid": {
        ...                 "type": "nmdc:ControlledIdentifiedTermValue",
        ...                 "term": {"type": "nmdc:OntologyClass", "id": "NCBITaxon:3701"},
        ...             },
        ...         },
        ...     ]
        ... }
        >>> Migrator(adapter=DictionaryAdapter(database=db)).upgrade()
        >>> db["biosample_set"][0]["host_taxid"]["term"]["id"]
        'NCBITaxon:15368'
        >>> db["biosample_set"][0]["host_taxid"]["has_raw_value"]
        'Brachypodium distachyon [NCBI:txid15368]'
        >>> db["biosample_set"][1]["host_taxid"]["term"]["id"]
        'NCBITaxon:3701'
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
        ...     {"id": "nmdc:bsm-3", "host_taxid": {"term": {"id": "NCBI:txid9606"}, "has_raw_value": "NCBI:txid9606"}}
        ... )
        {'id': 'nmdc:bsm-3', 'host_taxid': {'term': {'id': 'NCBITaxon:9606'}, 'has_raw_value': 'NCBI:txid9606'}}
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
