import re
from datetime import datetime

from nmdc_schema.migrators.migrator_base import MigratorBase


# GOLD-sourced timestamp pattern: DD-MON-YY HH.MM.SS.NNNNNNNNN AM/PM
# Example: "30-OCT-14 12.00.00.000000000 AM"
# These are legacy dates from GOLD that were passed through by the GOLD translator.
# Reference: https://github.com/microbiomedata/nmdc-runtime/blob/5b418100f24667616173285555b233b5dad9f43f/nmdc_runtime/site/translation/gold_translator.py
# Going forward, add_date/mod_date reflect when records were added/modified in NMDC.
_GOLD_DATE_FORMAT = "%d-%b-%y %I.%M.%S.%f000 %p"

_ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_ISO_DATETIME_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}")


def normalize_date_to_datetime(value: str) -> str:
    r"""
    Normalizes a date string to RFC 3339 datetime format (YYYY-MM-DDTHH:MM:SSZ),
    setting its time to midnight if it lacks time info, and setting—not
    converting—its time zone to UTC (i.e. "Z") if it lacks time zone info.

    All output values are UTC with a trailing Z designator, as required by
    JSON Schema's date-time format (RFC 3339).

    If the value is already an ISO datetime string (YYYY-MM-DDTHH:MM:SS), appends Z if missing.
    If the value is an ISO date (YYYY-MM-DD), appends T00:00:00Z.
    If the value is a GOLD-sourced timestamp, parses and converts to datetime.
    Raises ValueError for empty strings or unparseable values.

    >>> normalize_date_to_datetime('2024-11-07T15:02:18')
    '2024-11-07T15:02:18Z'
    >>> normalize_date_to_datetime('2024-11-07T15:02:18Z')
    '2024-11-07T15:02:18Z'
    >>> normalize_date_to_datetime('2021-03-31')
    '2021-03-31T00:00:00Z'
    >>> normalize_date_to_datetime('30-OCT-14 12.00.00.000000000 AM')
    '2014-10-30T00:00:00Z'
    >>> normalize_date_to_datetime('22-MAY-20 06.13.12.927000000 PM')
    '2020-05-22T18:13:12Z'
    >>> normalize_date_to_datetime('17-AUG-17 05.38.34.719000000 PM')
    '2017-08-17T17:38:34Z'
    >>> normalize_date_to_datetime('07-MAY-24 12.00.00.000000000 AM')
    '2024-05-07T00:00:00Z'
    >>> normalize_date_to_datetime('04-APR-20 08.26.35.067000000 AM')
    '2020-04-04T08:26:35Z'
    >>> normalize_date_to_datetime('')
    Traceback (most recent call last):
        ...
    ValueError: Cannot normalize empty date string
    >>> normalize_date_to_datetime('foo')
    Traceback (most recent call last):
        ...
    ValueError: Cannot normalize date string: 'foo'
    >>> normalize_date_to_datetime('fooo-ba-ar')
    Traceback (most recent call last):
        ...
    ValueError: Cannot normalize date string: 'fooo-ba-ar'

    Compact ISO 8601 (no separators) is not matched by the regex and raises ValueError:
    >>> normalize_date_to_datetime('20260310T042405')
    Traceback (most recent call last):
        ...
    ValueError: Cannot normalize date string: '20260310T042405'
    """
    if not value:
        raise ValueError("Cannot normalize empty date string")

    # Already ISO datetime (YYYY-MM-DDTHH:MM:SS...)
    if _ISO_DATETIME_RE.match(value):
        return value.rstrip("Z") + "Z"

    # ISO date (YYYY-MM-DD) — append conventional midnight time
    if _ISO_DATE_RE.match(value):
        return value + "T00:00:00Z"

    # GOLD-sourced format: DD-MON-YY HH.MM.SS.NNNNNNNNN AM/PM
    # The fractional seconds field is 9 digits; strptime %f handles 6 digits,
    # so we treat the last 3 as literal zeros in the format string.
    try:
        dt = datetime.strptime(value, _GOLD_DATE_FORMAT)
        return dt.strftime("%Y-%m-%dT%H:%M:%S") + "Z"
    except ValueError:
        raise ValueError(f"Cannot normalize date string: {value!r}")


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.16.1"
    _to_version = "11.17.0"

    def upgrade(self, commit_changes: bool = False) -> None:
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""

        self.adapter.process_each_document(
            "biosample_set", [self.move_dates_to_provenance_metadata]
        )
        self.adapter.process_each_document(
            "data_generation_set", [self.move_dates_to_provenance_metadata]
        )

    def move_dates_to_provenance_metadata(self, document: dict) -> dict:
        r"""
        Moves top-level `add_date` and `mod_date` fields from a document
        into its `provenance_metadata` sub-document, normalizing all date
        formats to RFC 3339 datetime strings (YYYY-MM-DDTHH:MM:SSZ).

        >>> m = Migrator()

        Document with both ISO dates — moved and promoted to datetime:
        >>> m.move_dates_to_provenance_metadata({'id': 'nmdc:bsm-99-abc', 'add_date': '2021-03-31', 'mod_date': '2023-01-25'})
        {'id': 'nmdc:bsm-99-abc', 'provenance_metadata': {'type': 'nmdc:ProvenanceMetadata', 'add_date': '2021-03-31T00:00:00Z', 'mod_date': '2023-01-25T00:00:00Z'}}

        Document with existing provenance_metadata — preserves other fields:
        >>> m.move_dates_to_provenance_metadata({'id': 'nmdc:bsm-99-def', 'add_date': '2021-03-31', 'mod_date': '2023-01-25', 'provenance_metadata': {'type': 'nmdc:ProvenanceMetadata', 'source_system_of_record': 'NMDC_Submission_Portal'}})
        {'id': 'nmdc:bsm-99-def', 'provenance_metadata': {'type': 'nmdc:ProvenanceMetadata', 'source_system_of_record': 'NMDC_Submission_Portal', 'add_date': '2021-03-31T00:00:00Z', 'mod_date': '2023-01-25T00:00:00Z'}}

        Document with neither date — no change:
        >>> m.move_dates_to_provenance_metadata({'id': 'nmdc:bsm-99-ghi'})
        {'id': 'nmdc:bsm-99-ghi'}

        Document with only add_date — moves just that one:
        >>> m.move_dates_to_provenance_metadata({'id': 'nmdc:bsm-99-jkl', 'add_date': '2021-03-31'})
        {'id': 'nmdc:bsm-99-jkl', 'provenance_metadata': {'type': 'nmdc:ProvenanceMetadata', 'add_date': '2021-03-31T00:00:00Z'}}

        Document with only mod_date — moves just that one:
        >>> m.move_dates_to_provenance_metadata({'id': 'nmdc:bsm-99-mno', 'mod_date': '2023-01-25'})
        {'id': 'nmdc:bsm-99-mno', 'provenance_metadata': {'type': 'nmdc:ProvenanceMetadata', 'mod_date': '2023-01-25T00:00:00Z'}}

        GOLD-sourced dates are normalized to RFC 3339 datetime:
        >>> m.move_dates_to_provenance_metadata({'id': 'nmdc:dgns-99-pqr', 'add_date': '30-OCT-14 12.00.00.000000000 AM', 'mod_date': '22-MAY-20 06.13.12.927000000 PM'})
        {'id': 'nmdc:dgns-99-pqr', 'provenance_metadata': {'type': 'nmdc:ProvenanceMetadata', 'add_date': '2014-10-30T00:00:00Z', 'mod_date': '2020-05-22T18:13:12Z'}}

        ISO datetime is preserved (Z appended if missing):
        >>> m.move_dates_to_provenance_metadata({'id': 'nmdc:dgns-99-stu', 'mod_date': '2024-11-07T15:02:18'})
        {'id': 'nmdc:dgns-99-stu', 'provenance_metadata': {'type': 'nmdc:ProvenanceMetadata', 'mod_date': '2024-11-07T15:02:18Z'}}
        """

        add_date = document.pop("add_date", None)
        mod_date = document.pop("mod_date", None)

        if add_date is not None or mod_date is not None:
            if "provenance_metadata" not in document:
                document["provenance_metadata"] = {
                    "type": "nmdc:ProvenanceMetadata"
                }

            if add_date is not None:
                document["provenance_metadata"]["add_date"] = normalize_date_to_datetime(add_date)
            if mod_date is not None:
                document["provenance_metadata"]["mod_date"] = normalize_date_to_datetime(mod_date)

        return document
