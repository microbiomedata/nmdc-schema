from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.1.0"
    _to_version = "11.2.0"

    def upgrade(self) -> None:
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> database = dict(
        ...   data_generation_set=[
        ...       {'id': 1, 'type': 'nmdc:MassSpectrometry'},
        ...       {'id': 2, 'type': 'nmdc:MassSpectrometry', 'has_calibration': 'nmdc:calib-99-abc123'},
        ...       {'id': 3, 'type': 'nmdc:NucleotideSequencing', 'has_calibration': 'nmdc:calib-99-abc123'},
        ...   ],
        ... )
        >>> m = Migrator(adapter=DictionaryAdapter(database=database))
        >>> m.upgrade()
        >>> database['data_generation_set'][0]
        {'id': 1, 'type': 'nmdc:MassSpectrometry'}
        >>> database['data_generation_set'][1]
        {'id': 2, 'type': 'nmdc:MassSpectrometry', 'generates_calibration': 'nmdc:calib-99-abc123'}
        >>> database['data_generation_set'][2]
        {'id': 3, 'type': 'nmdc:NucleotideSequencing', 'has_calibration': 'nmdc:calib-99-abc123'}
        """

        self.adapter.process_each_document(
            "data_generation_set",
            [
                self.rename_has_calibration_field,
            ],
        )

    def rename_has_calibration_field(self, data_generation_document: dict) -> dict:
        r"""
        Renames the `has_calibration` field to `generates_calibration`, if the document represents
        an instance of the `MassSpectrometry` class.

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> m = Migrator(adapter=DictionaryAdapter(database={}))
        >>> m.rename_has_calibration_field({'id': 1,
        ...                                 'type': 'nmdc:MassSpectrometry'})  # test: lacks `has_calibration`
        {'id': 1, 'type': 'nmdc:MassSpectrometry'}
        >>> m.rename_has_calibration_field({'id': 1,
        ...                                 'type': 'nmdc:MassSpectrometry',
        ...                                 'has_calibration': 'nmdc:calib-99-abc123'})  # test: has `has_calibration`
        {'id': 1, 'type': 'nmdc:MassSpectrometry', 'generates_calibration': 'nmdc:calib-99-abc123'}
        >>> m.rename_has_calibration_field({'id': 1,
        ...                                 'type': 'nmdc:NucleotideSequencing',
        ...                                 'has_calibration': 'nmdc:calib-99-abc123'})  # test: has different `type`
        {'id': 1, 'type': 'nmdc:NucleotideSequencing', 'has_calibration': 'nmdc:calib-99-abc123'}
        """
        if (
            "type" in data_generation_document
            and data_generation_document["type"] == "nmdc:MassSpectrometry"
        ):
            if "has_calibration" in data_generation_document:
                self.logger.info(
                    f"Renaming `has_calibration` field to `generates_calibration` "
                    f"on document having id: {data_generation_document['id']}"
                )
                data_generation_document["generates_calibration"] = (
                    data_generation_document.pop("has_calibration")
                )

        return data_generation_document
