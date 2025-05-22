from nmdc_schema.migrators.migrator_base import MigratorBase
from nmdc_schema.migrators.helpers import load_yaml_asset

class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.8.0.part_2"
    _to_version = "11.8.0.part_3"

    def upgrade(self) -> None:
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""
        self.adapter.process_each_document("data_generation_set", [self.validate_mass_spec_slots])

    def validate_mass_spec_slots(self, data_object: dict) -> dict:
        r"""
        If the data object does not have eluent_introduction_category or has_mass_spectrometry_configuration, raise a ValueError.
        If the data object's eluent_introduction_category is liquid_chromatography, then ensure has_chromatography_configuration slot is present.

        >>> m = Migrator()
        >>> m.validate_mass_spec_slots({"id": 123, "type": "nmdc:MassSpectrometry", "eluent_introduction_category": "liquid_chromatography", "has_mass_spectrometry_configuration": "nmdc:mscon-123"})
        {'id': 123, 'type': 'nmdc:MassSpectrometry', 'eluent_introduction_category': 'liquid_chromatography', 'has_mass_spectrometry_configuration': 'nmdc:mscon-123'}
        """
        pass