"""Standardize PersonValue.orcid onto the Bioregistry ``orcid:`` CURIE.

See https://github.com/microbiomedata/nmdc-schema/issues/3327
"""

from __future__ import annotations

import re
import unicodedata

from nmdc_schema.migrators.adapters.mongo_adapter import MongoAdapter
from nmdc_schema.migrators.migrator_base import MigratorBase

# Destination pattern from nmdc-schema#3327. Shape only; does not verify the
# ISO 7064 mod 11-2 check digit.
TARGET = re.compile(r"^orcid:\d{4}-\d{4}-\d{4}-\d{3}(\d|X)$")
URL_PREFIXES = ("https://orcid.org/", "http://orcid.org/")
# Confirmed one-off: Michael SanClements on nmdc:sty-11-8bjf2432 is missing a digit.
# Do not generalize this into a "pad a zero" rule.
KNOWN_BARE_FIXES = {
    "000-0002-1962-3561": "0000-0002-1962-3561",
}


def normalize_orcid(value: str | None) -> str | None:
    """Return an ``orcid:`` CURIE, or None to drop the key.

    Values that already match the destination pattern are returned unchanged.

    Already conforming:
    >>> normalize_orcid('orcid:0000-0002-4439-2398')
    'orcid:0000-0002-4439-2398'

    Adds the ``orcid:`` prefix:
    >>> normalize_orcid('0000-0002-1195-1608')
    'orcid:0000-0002-1195-1608'

    Uppercases a lowercase checksum:
    >>> normalize_orcid('0000-0003-2254-399x')
    'orcid:0000-0003-2254-399X'

    Strips whitespace and control characters:
    >>> normalize_orcid('\\t0000-0002-1057-7239')
    'orcid:0000-0002-1057-7239'
    >>> normalize_orcid('0000-0001-9557-3001\\u202c')
    'orcid:0000-0001-9557-3001'

    Extracts the identifier from an ORCID URL:
    >>> normalize_orcid(' https://orcid.org/0000-0002-9108-5083')
    'orcid:0000-0002-9108-5083'

    Drops empty strings and None:
    >>> normalize_orcid('') is None
    True
    >>> normalize_orcid(None) is None
    True

    Fixes the confirmed SanClements typo:
    >>> normalize_orcid('000-0002-1962-3561')
    'orcid:0000-0002-1962-3561'

    Raises on unrepairable values:
    >>> normalize_orcid('not-an-orcid')
    Traceback (most recent call last):
        ...
    ValueError: unrepairable orcid: 'not-an-orcid'
    >>> normalize_orcid(123)
    Traceback (most recent call last):
        ...
    ValueError: orcid is not a string: 123
    """
    if value is None:
        return None
    if not isinstance(value, str):
        raise ValueError(f"orcid is not a string: {value!r}")
    if TARGET.fullmatch(value):
        return value
    cleaned = "".join(ch for ch in value if unicodedata.category(ch) not in {"Cc", "Cf"})
    cleaned = cleaned.strip()
    if cleaned == "":
        return None
    lowered = cleaned.lower()
    for prefix in URL_PREFIXES:
        if lowered.startswith(prefix):
            cleaned = cleaned[len(prefix) :].strip().rstrip("/")
            break
    if cleaned.lower().startswith("orcid:"):
        cleaned = cleaned.split(":", 1)[1]
    if cleaned.endswith("x"):
        cleaned = cleaned[:-1] + "X"
    cleaned = KNOWN_BARE_FIXES.get(cleaned, cleaned)
    curie = f"orcid:{cleaned}"
    if TARGET.fullmatch(curie):
        return curie
    raise ValueError(f"unrepairable orcid: {value!r}")


class Migrator(MigratorBase):
    r"""Rewrite PersonValue.orcid onto the Bioregistry ``orcid:`` CURIE.

    Walks ``has_credit_associations[].applies_to_person`` on ``study_set`` and
    ``data_generation_set`` after part 1 has already removed
    ``principal_investigator``. Empty strings drop the key; unrepairable
    values raise so leftover strings cannot fail the new slot pattern silently.
    """

    _from_version = "11.24.0.part_1"
    _to_version = "11.24.0.part_2"

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
        ...                                       "orcid": "0000-0002-1195-1608"}},
        ...                 {"type": "prov:Association",
        ...                  "applies_to_person": {"type": "nmdc:PersonValue",
        ...                                       "name": "B",
        ...                                       "orcid": ""}},
        ...                 {"type": "prov:Association",
        ...                  "applies_to_person": {"type": "nmdc:PersonValue",
        ...                                       "name": "C"}},
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
        ...                                       "name": "D",
        ...                                       "orcid": "0000-0003-2254-399x"}},
        ...             ],
        ...         },
        ...     ],
        ... }
        >>> Migrator(adapter=DictionaryAdapter(database=db)).upgrade()
        >>> db["study_set"][0]["has_credit_associations"][0]["applies_to_person"]["orcid"]
        'orcid:0000-0002-1195-1608'
        >>> "orcid" in db["study_set"][0]["has_credit_associations"][1]["applies_to_person"]
        False
        >>> "orcid" in db["study_set"][0]["has_credit_associations"][2]["applies_to_person"]
        False
        >>> db["data_generation_set"][0]["has_credit_associations"][0]["applies_to_person"]["orcid"]
        'orcid:0000-0003-2254-399X'
        """
        self._warn_if_commit_ignored(commit_changes)

        if isinstance(self.adapter, MongoAdapter):
            try:
                self.adapter.process_collections_in_transaction(
                    collection_names=["study_set", "data_generation_set"],
                    document_processor=self.normalize_document_personvalue_orcids,
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
                "study_set", [self.normalize_document_personvalue_orcids]
            )
            self.adapter.process_each_document(
                "data_generation_set", [self.normalize_document_personvalue_orcids]
            )
            if not commit_changes:
                self.logger.info(
                    "Note: Non-MongoDB adapter doesn't support rollback - changes are applied immediately"
                )

    def normalize_document_personvalue_orcids(self, document: dict) -> dict:
        r"""Normalize or drop ``orcid`` on each credit-association PersonValue.

        >>> m = Migrator()
        >>> m.normalize_document_personvalue_orcids(
        ...     {"id": "nmdc:sty-1",
        ...      "has_credit_associations": [
        ...          {"applies_to_person": {"type": "nmdc:PersonValue",
        ...                                "orcid": "0000-0002-1195-1608"}},
        ...          {"applies_to_person": {"orcid": "000-0002-1962-3561"}},
        ...          {"applies_to_person": {"orcid": ""}},
        ...          {"applies_to_person": {"name": "C"}},
        ...      ]}
        ... )
        {'id': 'nmdc:sty-1', 'has_credit_associations': [{'applies_to_person': {'type': 'nmdc:PersonValue', 'orcid': 'orcid:0000-0002-1195-1608'}}, {'applies_to_person': {'orcid': 'orcid:0000-0002-1962-3561'}}, {'applies_to_person': {}}, {'applies_to_person': {'name': 'C'}}]}
        >>> m.normalize_document_personvalue_orcids({"id": "nmdc:sty-2"})
        {'id': 'nmdc:sty-2'}
        >>> m.normalize_document_personvalue_orcids(
        ...     {"id": "nmdc:sty-3",
        ...      "has_credit_associations": [{"applies_to_person": {"orcid": "not-an-orcid"}}]}
        ... )
        Traceback (most recent call last):
            ...
        ValueError: In nmdc:sty-3: unrepairable orcid: 'not-an-orcid'
        """
        document_id = document.get("id", "<unknown id>")
        try:
            for association in document.get("has_credit_associations") or []:
                if not isinstance(association, dict):
                    continue
                person = association.get("applies_to_person")
                if not isinstance(person, dict) or "orcid" not in person:
                    continue
                normalized = normalize_orcid(person["orcid"])
                if normalized is None:
                    person.pop("orcid", None)
                else:
                    person["orcid"] = normalized
        except ValueError as exc:
            raise ValueError(f"In {document_id}: {exc}") from None
        return document
