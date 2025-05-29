from nmdc_schema.migrators.migrator_base import MigratorBase

class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.8.0.part_3"
    _to_version = "11.8.0.part_4"

    def upgrade(self) -> None:
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""
        self.adapter.do_for_each_document("configuration_set", self.validate_mass_spec_config_slots)
        self.adapter.do_for_each_document("configuration_set", self.validate_chrom_config_slots)

    def validate_mass_spec_config_slots(self, configuration_record: dict) -> None:
        r"""
        If the configuration record is of type MassSpectrometryConfiguration, does not have mass_spectrometry_acquisition_strategy, resolution_categories, mass_analyzers, ionization_source, mass_spectrum_collection_modes, and polarity_mode OR any of those keys does not have a value, raise a ValueError.

        >>> m = Migrator()
        >>> m.validate_mass_spec_config_slots({"id": 123, "type": "nmdc:MassSpectrometryConfiguration", "mass_spectrometry_acquisition_strategy": "data_independent_acquisition", "resolution_categories": "high", "mass_analyzers": "ion_trap", "ionization_source": "electron_ionization", "mass_spectrum_collection_modes": "centroid", "polarity_mode": "positive"})
        >>> m.validate_mass_spec_config_slots({"id": 123, "type": "nmdc:MassSpectrometryConfiguration", "mass_spectrometry_acquisition_strategy": "data_independent_acquisition", "resolution_categories": "high", "mass_analyzers": "ion_trap", "ionization_source": "electron_ionization", "mass_spectrum_collection_modes": "centroid"})
        Traceback (most recent call last):
        ...
        ValueError: `polarity_mode` is required and is not present in the configuration record 123
        >>> m.validate_mass_spec_config_slots({"id": 123, "type": "nmdc:MassSpectrometryConfiguration", "mass_spectrometry_acquisition_strategy": "data_independent_acquisition", "resolution_categories": "high", "mass_analyzers": "ion_trap", "ionization_source": "electron_ionization", "polarity_mode": "positive"})
        Traceback (most recent call last):
        ... 
        ValueError: `mass_spectrum_collection_modes` is required and is not present in the configuration record 123
        >>> m.validate_mass_spec_config_slots({"id": 123, "type": "nmdc:MassSpectrometryConfiguration", "mass_spectrometry_acquisition_strategy": "data_independent_acquisition", "resolution_categories": "high", "mass_analyzers": "ion_trap", "mass_spectrum_collection_modes": "centroid", "polarity_mode": "positive"})
        Traceback (most recent call last):
        ...
        ValueError: `ionization_source` is required and is not present in the configuration record 123
        >>> m.validate_mass_spec_config_slots({"id": 123, "type": "nmdc:MassSpectrometryConfiguration", "mass_spectrometry_acquisition_strategy": "data_independent_acquisition", "resolution_categories": "high", "mass_spectrum_collection_modes": "centroid", "polarity_mode": "positive"})
        Traceback (most recent call last):
        ...
        ValueError: `mass_analyzers` is required and is not present in the configuration record 123
        >>> m.validate_mass_spec_config_slots({"id": 123, "type": "nmdc:MassSpectrometryConfiguration", "mass_spectrometry_acquisition_strategy": "data_independent_acquisition", "mass_analyzers": "ion_trap", "ionization_source": "electron_ionization", "mass_spectrum_collection_modes": "centroid", "polarity_mode": "positive"})
        Traceback (most recent call last):
        ...
        ValueError: `resolution_categories` is required and is not present in the configuration record 123
        >>> m.validate_mass_spec_config_slots({"id": 123, "type": "nmdc:MassSpectrometryConfiguration", "resolution_categories": "high", "mass_analyzers": "ion_trap", "ionization_source": "electron_ionization", "mass_spectrum_collection_modes": "centroid", "polarity_mode": "positive"})
        Traceback (most recent call last):
        ...
        ValueError: `mass_spectrometry_acquisition_strategy` is required and is not present in the configuration record 123
        """
        config_record_id = configuration_record.get("id")
        # get the slots that are required for mass spectrometry configuration
        if configuration_record.get("type") == "nmdc:MassSpectrometryConfiguration":
            mass_spectrometry_acquisition_strategy = configuration_record.get("mass_spectrometry_acquisition_strategy")
            if mass_spectrometry_acquisition_strategy is None:
                raise ValueError(f"`mass_spectrometry_acquisition_strategy` is required and is not present in the configuration record {config_record_id}")
            
            resolution_categories = configuration_record.get("resolution_categories")
            if resolution_categories is None:
                raise ValueError(f"`resolution_categories` is required and is not present in the configuration record {config_record_id}")
            
            mass_analyzers = configuration_record.get("mass_analyzers")
            if mass_analyzers is None:
                raise ValueError(f"`mass_analyzers` is required and is not present in the configuration record {config_record_id}")
            
            ionization_source = configuration_record.get("ionization_source")
            if ionization_source is None:
                raise ValueError(f"`ionization_source` is required and is not present in the configuration record {config_record_id}")
            
            mass_spectrum_collection_modes = configuration_record.get("mass_spectrum_collection_modes")
            if mass_spectrum_collection_modes is None:
                raise ValueError(f"`mass_spectrum_collection_modes` is required and is not present in the configuration record {config_record_id}")
            
            polarity_mode = configuration_record.get("polarity_mode")
            if polarity_mode is None:
                raise ValueError(f"`polarity_mode` is required and is not present in the configuration record {config_record_id}")
    
    def validate_chrom_config_slots(self, configuration_record:dict) -> None:
        r"""
        If the configuration record is of type `ChromatographyConfiguration` and either (a) its `chromatographic_category` field is missing or consists of `None`, or (b) its `stationary_phase` field is missing or consists of `None`, raise a `ValueError`.

        >>> m = Migrator()
        >>> m.validate_chrom_config_slots({"id": 123, "type": "nmdc:ChromatographyConfiguration", "chromatographic_category": "gas_chromatography", "stationary_phase": "C18"})
        >>> m.validate_chrom_config_slots({"id": 123, "type": "nmdc:ChromatographyConfiguration", "chromatographic_category": "gas_chromatography"})
        Traceback (most recent call last):
        ...
        ValueError: `stationary_phase` is required and is not present in the configuration record 123
        >>> m.validate_chrom_config_slots({"id": 123, "type": "nmdc:ChromatographyConfiguration", "stationary_phase": "C18"})
        Traceback (most recent call last):
        ...
        ValueError: `chromatographic_category` is required and is not present in the configuration record 123
        """
        config_record_id = configuration_record.get("id")
        if configuration_record.get("type") == "nmdc:ChromatographyConfiguration":
            chromatographic_category = configuration_record.get("chromatographic_category")
            if chromatographic_category is None:
                raise ValueError(f"`chromatographic_category` is required and is not present in the configuration record {config_record_id}")
            
            stationary_phase = configuration_record.get("stationary_phase")
            if stationary_phase is None:
                raise ValueError(f"`stationary_phase` is required and is not present in the configuration record {config_record_id}")
            
