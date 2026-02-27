from datetime import datetime

from nmdc_schema.migrators.migrator_base import MigratorBase


# GOLD-format timestamp pattern: DD-MON-YY HH.MM.SS.NNNNNNNNN AM/PM
# Example: "30-OCT-14 12.00.00.000000000 AM"
_GOLD_DATE_FORMAT = "%d-%b-%y %I.%M.%S.%f000 %p"


def normalize_gold_date(value: str) -> str:
    r"""
    Normalizes a date string to ISO 8601 date format (YYYY-MM-DD).

    If the value is already in ISO date format, returns it unchanged.
    If the value is an ISO datetime string, extracts just the date portion.
    If the value is a GOLD-format timestamp, parses and converts to ISO date.

    >>> normalize_gold_date('2021-03-31')
    '2021-03-31'
    >>> normalize_gold_date('2024-11-07T15:02:18')
    '2024-11-07'
    >>> normalize_gold_date('30-OCT-14 12.00.00.000000000 AM')
    '2014-10-30'
    >>> normalize_gold_date('22-MAY-20 06.13.12.927000000 PM')
    '2020-05-22'
    >>> normalize_gold_date('17-AUG-17 05.38.34.719000000 PM')
    '2017-08-17'
    >>> normalize_gold_date('07-MAY-24 12.00.00.000000000 AM')
    '2024-05-07'
    >>> normalize_gold_date('04-APR-20 08.26.35.067000000 AM')
    '2020-04-04'
    """
    if not value or not isinstance(value, str):
        return value

    # Already ISO date (YYYY-MM-DD)
    if len(value) == 10 and value[4] == "-" and value[7] == "-":
        return value

    # ISO datetime (YYYY-MM-DDTHH:MM:SS...) — extract date portion
    if len(value) > 10 and value[4] == "-" and value[7] == "-" and value[10] == "T":
        return value[:10]

    # GOLD-format: DD-MON-YY HH.MM.SS.NNNNNNNNN AM/PM
    # The fractional seconds field is 9 digits; strptime %f handles 6 digits,
    # so we treat the last 3 as literal zeros in the format string.
    try:
        dt = datetime.strptime(value, _GOLD_DATE_FORMAT)
        return dt.strftime("%Y-%m-%d")
    except ValueError:
        # Return as-is if we can't parse — the validator will catch it
        return value


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
        into its `provenance_metadata` sub-document, normalizing GOLD-format
        timestamps to ISO date strings (YYYY-MM-DD).

        >>> m = Migrator()

        Document with both ISO dates — moved into provenance_metadata:
        >>> m.move_dates_to_provenance_metadata({'id': 'nmdc:bsm-99-abc', 'add_date': '2021-03-31', 'mod_date': '2023-01-25'})
        {'id': 'nmdc:bsm-99-abc', 'provenance_metadata': {'type': 'nmdc:ProvenanceMetadata', 'add_date': '2021-03-31', 'mod_date': '2023-01-25'}}

        Document with existing provenance_metadata — preserves other fields:
        >>> m.move_dates_to_provenance_metadata({'id': 'nmdc:bsm-99-def', 'add_date': '2021-03-31', 'mod_date': '2023-01-25', 'provenance_metadata': {'type': 'nmdc:ProvenanceMetadata', 'source_system_of_record': 'NMDC_Submission_Portal'}})
        {'id': 'nmdc:bsm-99-def', 'provenance_metadata': {'type': 'nmdc:ProvenanceMetadata', 'source_system_of_record': 'NMDC_Submission_Portal', 'add_date': '2021-03-31', 'mod_date': '2023-01-25'}}

        Document with neither date — no change:
        >>> m.move_dates_to_provenance_metadata({'id': 'nmdc:bsm-99-ghi'})
        {'id': 'nmdc:bsm-99-ghi'}

        Document with only add_date — moves just that one:
        >>> m.move_dates_to_provenance_metadata({'id': 'nmdc:bsm-99-jkl', 'add_date': '2021-03-31'})
        {'id': 'nmdc:bsm-99-jkl', 'provenance_metadata': {'type': 'nmdc:ProvenanceMetadata', 'add_date': '2021-03-31'}}

        Document with only mod_date — moves just that one:
        >>> m.move_dates_to_provenance_metadata({'id': 'nmdc:bsm-99-mno', 'mod_date': '2023-01-25'})
        {'id': 'nmdc:bsm-99-mno', 'provenance_metadata': {'type': 'nmdc:ProvenanceMetadata', 'mod_date': '2023-01-25'}}

        GOLD-format dates are normalized to ISO date:
        >>> m.move_dates_to_provenance_metadata({'id': 'nmdc:dgns-99-pqr', 'add_date': '30-OCT-14 12.00.00.000000000 AM', 'mod_date': '22-MAY-20 06.13.12.927000000 PM'})
        {'id': 'nmdc:dgns-99-pqr', 'provenance_metadata': {'type': 'nmdc:ProvenanceMetadata', 'add_date': '2014-10-30', 'mod_date': '2020-05-22'}}

        ISO datetime is normalized to date only:
        >>> m.move_dates_to_provenance_metadata({'id': 'nmdc:dgns-99-stu', 'mod_date': '2024-11-07T15:02:18'})
        {'id': 'nmdc:dgns-99-stu', 'provenance_metadata': {'type': 'nmdc:ProvenanceMetadata', 'mod_date': '2024-11-07'}}
        """

        add_date = document.pop("add_date", None)
        mod_date = document.pop("mod_date", None)

        if add_date is not None or mod_date is not None:
            if "provenance_metadata" not in document:
                document["provenance_metadata"] = {
                    "type": "nmdc:ProvenanceMetadata"
                }

            if add_date is not None:
                document["provenance_metadata"]["add_date"] = normalize_gold_date(add_date)
            if mod_date is not None:
                document["provenance_metadata"]["mod_date"] = normalize_gold_date(mod_date)

        return document
