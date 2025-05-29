from nmdc_schema.migrators.migrator_base import MigratorBase
from nmdc_schema.migrators.helpers import load_yaml_asset

class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.8.0.part_2"
    _to_version = "11.8.0.part_3"

    def upgrade(self) -> None:
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""
        self.adapter.do_for_each_document("data_generation_set", self.validate_mass_spec_slots)

    def validate_mass_spec_slots(self, data_generation_record: dict) -> None:
        r"""
        If the data object is of type `nmdc:MassSpectrometry` and either (a) its `eluent_introduction_category` field is missing or consists of `None`, or (b) its `has_mass_spectrometry_configuration` field is missing or consists of `None`, raise a `ValueError`.

        >>> m = Migrator()
        >>> m.validate_mass_spec_slots({"id": 123, "type": "nmdc:MassSpectrometry", "eluent_introduction_category": "gas_chromatography", "has_mass_spectrometry_configuration": "nmdc:mscon-123"})
        >>> m.validate_mass_spec_slots({"id": 123, "type": "nmdc:MassSpectrometry", "eluent_introduction_category": "gas_chromatography"})
        Traceback (most recent call last):
        ...
        ValueError: `has_mass_spectrometry_configuration` is required and is not present in the data object 123
        >>> m.validate_mass_spec_slots({"id": 123, "type": "nmdc:MassSpectrometry", "has_mass_spectrometry_configuration": "nmdc:mscon-123"})
        Traceback (most recent call last):
        ... 
        ValueError: `eluent_introduction_category` is required and is not present in the data object 123
        """
        # get the eluent_introduction_category and has_mass_spectrometry_configuration fields
        if data_generation_record.get("type") == "nmdc:MassSpectrometry":
            eluent_introduction_category = data_generation_record.get("eluent_introduction_category")
            if eluent_introduction_category is None:
                raise ValueError(f"`eluent_introduction_category` is required and is not present in the data object {data_generation_record.get('id')}")
            
            has_mass_spec_config = data_generation_record.get("has_mass_spectrometry_configuration")
            if has_mass_spec_config is None:
                raise ValueError(f"`has_mass_spectrometry_configuration` is required and is not present in the data object {data_generation_record.get('id')}")
