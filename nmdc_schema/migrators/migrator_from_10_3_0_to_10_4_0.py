from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "10.3.0"
    _to_version = "10.4.0"

    def upgrade(self) -> None:
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""

        self.adapter.process_each_document(
            "nom_analysis_activity_set", [self.update_nom_analysis_activity_id]
        )

    def update_nom_analysis_activity_id(self, nom_analysis_activity: dict) -> dict:
        r"""
        Updates a nom_analysis_activity's id to contain a version number (.1),
        if it has no version number.

        >>> m = Migrator()
        >>> m.update_nom_analysis_activity_id({'id': '1'}) # test: adds version number to id
        {'id': '1.1'}
        """
        self.logger.info(f"Processing NomAnalysisActivity: {nom_analysis_activity['id']}")

        
        # If this data object's `data_object_type` consists of the invalid value, replace it with the valid value.
        if "." not in nom_analysis_activity['id']:
            nom_analysis_activity['id'] = str(nom_analysis_activity['id']) + ".1"

        return nom_analysis_activity