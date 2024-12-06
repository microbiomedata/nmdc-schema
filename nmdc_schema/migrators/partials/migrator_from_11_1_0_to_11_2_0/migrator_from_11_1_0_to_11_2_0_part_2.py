# Note: This migrator was originally introduced by @kheal in PR https://github.com/microbiomedata/nmdc-schema/pull/2276
#       It has since been renamed and relocated from its original name and location.

from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.2.0.part_1"
    _to_version = "11.2.0.part_2"

    def upgrade(self):
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""

        self.adapter.process_each_document("workflow_execution_set", [self.set_metap_analysis_category])

    def set_metap_analysis_category(self, workflow: dict) -> dict:
        r"""
        If the workflow execution records is of the type "nmdc:MetaproteomicsAnalysis",
        add field `metaproteomics_analysis_category` and assign it the value "matched_metagenome".

        >>> m = Migrator()
        >>> m.set_metap_analysis_category({'id': 123, 'type': 'nmdc:MetaproteomicsAnalysis'})  # field doesn't exist yet
        {'id': 123, 'type': 'nmdc:MetaproteomicsAnalysis', 'metaproteomics_analysis_category': 'matched_metagenome'}
        >>> m.set_metap_analysis_category({'id': 123, 'type': 'nmdc:MetabolomicsAnalysis'})  # not a metaproteomics analysis
        {'id': 123, 'type': 'nmdc:MetabolomicsAnalysis'}
        """

        if workflow["type"] == "nmdc:MetaproteomicsAnalysis":
            if "metaproteomics_analysis_category" not in workflow:
                workflow["metaproteomics_analysis_category"] = "matched_metagenome"
        return workflow
