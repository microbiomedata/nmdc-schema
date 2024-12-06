from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.1.0"
    _to_version = "11.2.0.part_1"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # This is a dictionary of key-value pairs, where each key is the `id` of a `workflow_execution_set` document
        # and the corresponding value is the value we will store in that document's `uses_calibration` field.
        self.calibration_mappings = {}

    def upgrade(self) -> None:
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> database = dict(
        ...   data_generation_set=[
        ...       {'id': 1, 'type': 'nmdc:MassSpectrometry'},
        ...       {'id': 2, 'type': 'nmdc:MassSpectrometry', 'has_calibration': 'nmdc:calib-99-abc123'},
        ...       {'id': 3, 'type': '__AnythingElse__', 'has_calibration': 'nmdc:calib-99-abc123'},
        ...   ],
        ... )
        >>> m = Migrator(adapter=DictionaryAdapter(database=database))
        >>> m.upgrade()
        >>> database['data_generation_set'][0]
        {'id': 1, 'type': 'nmdc:MassSpectrometry'}
        >>> database['data_generation_set'][1]
        {'id': 2, 'type': 'nmdc:MassSpectrometry', 'generates_calibration': 'nmdc:calib-99-abc123'}
        >>> database['data_generation_set'][2]
        {'id': 3, 'type': '__AnythingElse__', 'has_calibration': 'nmdc:calib-99-abc123'}

        TODO: Update doctests to account for the two added function calls.
        """

        self.adapter.process_each_document(
            "data_generation_set",
            [
                self.rename_has_calibration_field,
            ],
        )

        self.adapter.process_each_document(
            "data_generation_set",
            [
                self.determine_calibration_mapping,
            ],
        )

        self.adapter.process_each_document(
            "workflow_execution_set",
            [
                self.apply_calibration_mapping,
            ],
        )

    def rename_has_calibration_field(self, data_generation: dict) -> dict:
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
        ...                                 'type': '__AnythingElse__',
        ...                                 'has_calibration': 'nmdc:calib-99-abc123'})  # test: has different `type`
        {'id': 1, 'type': '__AnythingElse__', 'has_calibration': 'nmdc:calib-99-abc123'}
        """
        if data_generation.get("type") == "nmdc:MassSpectrometry":
            if "has_calibration" in data_generation:
                self.logger.info(
                    f"Renaming `has_calibration` field to `generates_calibration` "
                    f"on document having id: {data_generation['id']}"
                )
                data_generation["generates_calibration"] = (
                    data_generation.pop("has_calibration")
                )

        return data_generation

    def determine_calibration_mapping(self, data_generation: dict) -> dict:
        r"""
        If the specified `data_generation_set` document meets certain criteria, adds its `generates_calibration` or
        `has_calibration` value to the instance-level dictionary that will later be used to populate the
        `uses_calibration` fields of `workflow_execution_set` documents; and if the `analyte_category` value of the
        `data_generation_set` document is "nom" (and not "metabolome"), deletes the `generates_calibration` or
        `has_calibration` field from that `data_generation_set` document.

        TODO: Add doctests.
        """

        # Make handy aliases for some values.
        data_generation_id = data_generation["id"]
        data_generation_analyte_category = data_generation.get("analyte_category")

        # Implement the algorithm discussed with schema maintainers.
        if data_generation_analyte_category == "nom" or data_generation_analyte_category == "metabolome":

            # Determine which calibration-related field this document has, if any.
            calibration_field_name = None
            if "generates_calibration" in data_generation:
                calibration_field_name = "generates_calibration"
            elif "has_calibration" in data_generation:
                calibration_field_name = "has_calibration"
            else:
                self.logger.warning(f"'data_generation_set' document '{data_generation_id}' has neither field")

            if calibration_field_name is not None:

                # Find the `workflow_execution_set` document whose `was_informed_by` field contains this document's `id`
                workflow_execution = self.adapter.get_document_having_value_in_field(
                    collection_name="workflow_execution_set",
                    field_name="was_informed_by",  # confirmed: this is a single valued field, not a multivalued one
                    value=data_generation_id,
                )
                if workflow_execution is not None:

                    # Update the instance-level dictionary, which will be "consumed" by a different method.
                    self.calibration_mappings[workflow_execution["id"]] = data_generation.get(calibration_field_name)

                    # If this `data_generation_set` document's `analyte_category` value was "nom", specifically,
                    # delete the calibration-related field from the document.
                    if data_generation_analyte_category == "nom":
                        data_generation.pop(calibration_field_name)
                else:
                    self.logger.warning(f"No 'workflow_execution_set' document has a "
                                        f"'was_informed_by' value of '{data_generation_id}'")

        return data_generation

    def apply_calibration_mapping(self, workflow_execution: dict) -> dict:
        r"""
        Sets the `uses_calibration` field to the value defined in the instance-level dictionary.

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> m = Migrator(adapter=DictionaryAdapter(database={}))
        >>> m.calibration_mappings = {'nmdc:wfe-99-abc123': 'nmdc:calib-99-def456'}
        >>> m.apply_calibration_mapping({'id': 'nmdc:wfe-99-abc123', 'type': 'nmdc:MetagenomeAnnotation'})  # id in map
        {'id': 'nmdc:wfe-99-abc123', 'type': 'nmdc:MetagenomeAnnotation', 'uses_calibration': 'nmdc:calib-99-def456'}
        >>> m.apply_calibration_mapping({'id': 'nmdc:wfe-00-abc123', 'type': 'nmdc:MetagenomeAnnotation'})  # random id
        {'id': 'nmdc:wfe-00-abc123', 'type': 'nmdc:MetagenomeAnnotation'}
        """
        workflow_execution_id = workflow_execution["id"]

        # Check whether this `workflow_execution_set` document's `id` value is a key in our dictionary.
        if workflow_execution_id in self.calibration_mappings.keys():

            # Set this `workflow_execution_set` document's `uses_calibration` field to the value from our dictionary.
            workflow_execution["uses_calibration"] = self.calibration_mappings[workflow_execution_id]

        return workflow_execution
