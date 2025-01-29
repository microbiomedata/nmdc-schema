from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.3.0"
    _to_version = "11.4.0"

    def upgrade(self):
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""

        self.adapter.process_each_document("workflow_execution_set", [self.set_metab_analysis_category])

    def set_metab_analysis_category(self, workflow: dict) -> dict:
        r"""
        If the workflow execution record is of the type "nmdc:MetabolomicsAnalysis" and it has a `has_metabolite_identifications` field,
        add field `metabolomics_analysis_category` and assign it the value "gc_ms_metabolomics". If the record does not 
        have a `has_metabolite_identifications` field, it is assigned the value "lc_ms_lipidomics".

        >>> m = Migrator()
        >>> m.set_metab_analysis_category({'id': 123, 'type': 'nmdc:MetabolomicsAnalysis', 'has_metabolite_identifications': []})
        {'id': 123, 'type': 'nmdc:MetabolomicsAnalysis', 'has_metabolite_identifications': [], 'metabolomics_analysis_category': 'gc_ms_metabolomics'}
        >>> m.set_metab_analysis_category({'id': 123, 'type': 'nmdc:MetabolomicsAnalysis'})  # does not have has_metabolite_identifications field, therefore it's a lipid analysis
        {'id': 123, 'type': 'nmdc:MetabolomicsAnalysis', 'metabolomics_analysis_category': 'lc_ms_lipidomics'}
        >>> m.set_metab_analysis_category({'id': 123, 'type': 'nmdc:Metaproteomics'})  # not a metabolomics analysis
        {'id': 123, 'type': 'nmdc:Metaproteomics'}
        """

        if workflow["type"] == "nmdc:MetabolomicsAnalysis":
            if "has_metabolite_identifications" in workflow:
                workflow["metabolomics_analysis_category"] = "gc_ms_metabolomics"
            else:
                workflow["metabolomics_analysis_category"] = "lc_ms_lipidomics"
        return workflow