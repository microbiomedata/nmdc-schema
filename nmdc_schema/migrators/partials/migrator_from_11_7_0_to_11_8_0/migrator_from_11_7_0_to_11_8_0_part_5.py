from nmdc_schema.migrators.migrator_base import MigratorBase

class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.8.0.part_4"
    _to_version = "11.8.0.part_5"

    def upgrade(self) -> None:
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""
        self.adapter.do_for_each_document("material_processing_set", self.validate_sub_sampling_process_slot)

    def validate_sub_sampling_process_slot(self, material_processing_record: dict) -> None:
        r"""
        If the material processing record is of type SubSamplingProcess it should not have a `non_polar_layer` slot.
        If it does, raise a ValueError.
        
        >>> m = Migrator()
        >>> m.validate_sub_sampling_process_slot({"id": 123, "type": "nmdc:SubSamplingProcess"})
        >>> m.validate_sub_sampling_process_slot({"id": 123, "type": "nmdc:SubSamplingProcess", "non_polar_layer": "some_value"})
        Traceback (most recent call last):
        ...
        ValueError: `non_polar_layer` is not an allowed slot for SubSamplingProcess and is present in the material processing record 123
        """
        
        mp_record_id = material_processing_record.get("id")
        # Check if the material processing record is of type SubSamplingProcess
        if material_processing_record.get("type") == "nmdc:SubSamplingProcess":
            # Check if the non_polar_layer slot is present
            if "non_polar_layer" in material_processing_record:
                raise ValueError(f"`non_polar_layer` is not an allowed slot for SubSamplingProcess and is present in the material processing record {mp_record_id}")