import re
from nmdc_schema.migrators.migrator_base import MigratorBase


DOI_URL_PATTERN = r"^https?:\/\/[a-zA-Z\.]+\/10\."


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "7.7.2"
    _to_version = "7.8.0"

    def upgrade(self):
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""

        self.adapter.process_each_document("study_set", [self.replace_doi_field_with_award_dois_list_field])

    def replace_doi_field_with_award_dois_list_field(self, study: dict) -> dict:
        r"""
        Removes the `doi` field. If `doi.has_raw_value` contained a specific type of URL string, this function also adds
        an `award_dois` field whose value is a list containing a CURIE string derived from that URL string.

        >>> m = Migrator()
        >>> m.replace_doi_field_with_award_dois_list_field({'id': 123})  # no `doi` field
        {'id': 123}
        >>> m.replace_doi_field_with_award_dois_list_field({'id': 123, 'doi': {'has_raw_value': 'not-a-url'}})
        {'id': 123}
        >>> m.replace_doi_field_with_award_dois_list_field(
        ...     {'id': 123, 'doi': {'has_raw_value': 'https://example.com/10.other_stuff'}}
        ... )
        {'id': 123, 'award_dois': ['doi:10.other_stuff']}
        """

        self.logger.info(f"Starting migration of {study['id']}")
        if "doi" in study:
            match = re.search(DOI_URL_PATTERN, study["doi"]["has_raw_value"])
            if match:
                start_index = match.end()
                as_curie = f"doi:10.{study['doi']['has_raw_value'][start_index:]}"
                study["award_dois"] = [as_curie]
            del study["doi"]
        return study
