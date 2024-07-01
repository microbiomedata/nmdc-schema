from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    """
    Migrates data from X to PR129, namely changes the slot names has_metabolite_quantifications to has_metabolite_identifications
    and metabolite_quantified to metabolite_identified.
    """

    _from_version = "X"
    _to_version = "PR129"

    def upgrade(self):
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.
        """

        self.adapter.process_each_document(collection_name="metabolomics_analysis_activity_set", pipeline=[self.change_metab_slot_names])

    def change_metab_slot_names(self, metab_doc: dict) -> dict:
        r"""
        Changes the slot names has_metabolite_quantifications to has_metabolite_identifications
        and metabolite_quantified to metabolite_identified.

        >>> m = Migrator()  
        >>> m.change_metab_slot_names({'id': 123, 'has_metabolite_quantifications': [{'metabolite_quantified': 'chebi:16997'}]})  
        {'id': 123, 'has_metabolite_identifications': [{'metabolite_identified': 'chebi:16997'}]}
        """

        if "has_metabolite_quantifications" in metab_doc:
            metab_doc["has_metabolite_identifications"] = metab_doc.pop("has_metabolite_quantifications")
            for metabolite in metab_doc["has_metabolite_identifications"]:
                metabolite["metabolite_identified"] = metabolite.pop("metabolite_quantified")
           
        return metab_doc
