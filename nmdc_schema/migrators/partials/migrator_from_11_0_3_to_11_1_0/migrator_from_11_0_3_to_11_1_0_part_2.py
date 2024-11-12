from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    # Note: This migrator was introduced via PR 2203 (i.e. https://github.com/microbiomedata/nmdc-schema/pull/2203).
    _from_version = "11.1.0.part_1"
    _to_version = "11.1.0.part_2" 

    def upgrade(self):
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""

        self.adapter.process_each_document(
            "functional_annotation_agg", [self.move_metagenome_id_to_was_generated_by]
        )

    def move_metagenome_id_to_was_generated_by(self, fun_agg: dict) -> dict:
        r"""
        Updates the `FunctionalAnnotationAggMember` records so the value originally in its `metagenome_annotation_id` field 
        is stored in a new field named `was_generated_by`; and removes the `metagenome_annotation_id` field.

        `metagenome_annotation_id` is required on these records and has the same value as `was_generated_by` in the new schema,
        so no data is lost in this migration nor do we need to check for the existence of the field.

        >>> m = Migrator()
        >>> m.move_metagenome_id_to_was_generated_by({'metagenome_annotation_id': 'mgm123', 'count': 1})
        {'count': 1, 'was_generated_by': 'mgm123'}
        
        """
        fun_agg["was_generated_by"] = fun_agg.pop("metagenome_annotation_id")
        return fun_agg
