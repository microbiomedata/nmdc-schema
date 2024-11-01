from nmdc_schema.migrators.migrator_base import MigratorBase
import re


class Migrator(MigratorBase):
    r"""
    Migrates a database between two schemas.

    This migrator removes the `has_calibration` field from all documents that represent an instance of
    the `NomAnalysis` and 'MetabolomicsAnalysis' class, and moves the information to its corresponding
    'MassSpectrometry` `has_calibration` slot.

    The creation of this migrator was in response to this issue:
    https://github.com/microbiomedata/nmdc-schema/issues/2139

    """

    _from_version = "11.0.3"
    _to_version = "11.1.0.part_1"

    def upgrade(self) -> None:
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> db = {
        ...   'workflow_execution_set': [
        ...     {'id': 'nmdc:wfx1', 'has_calibration': 'nmdc:dobj-13-abc123', 'was_informed_by': 'nmdc:dgen1', 'type': 'nmdc:MetabolomicsAnalysis'},
        ...     {'id': 'nmdc:wfx2', 'has_calibration': 'false', 'was_informed_by': 'nmdc:dgen2', 'type': 'nmdc:NomAnalysis'},
        ...     {'id': 'nmdc:wfx3', 'was_informed_by': 'nmdc:dgen3', 'type': 'nmdc:MetabolomicsAnalysis'}
        ...   ],
        ...   'data_generation_set': [
        ...     {'id': 'nmdc:dgen1'},
        ...     {'id': 'nmdc:dgen2'},
        ...     {'id': 'nmdc:dgen3'}
        ...   ],
        ...   'data_object_set': [
        ...     {'id': 'nmdc:dobj-13-abc123'}
        ...   ],
        ...   'calibration_set': [
        ...     {'id': 'nmdc:calib1', 'calibration_object': 'nmdc:dobj-13-abc123'}
        ...   ]
        ... }
        >>> a = DictionaryAdapter(database=db)
        >>> m = Migrator(adapter=a)
        >>> m.upgrade()
        >>> any('has_calibration' in doc for doc in db['workflow_execution_set'])  # Calibrations removed from workflow
        False
        >>> db['data_generation_set'][0]  # Calibration moved to data generation
        {'id': 'nmdc:dgen1', 'has_calibration': 'nmdc:calib1'}
        >>> db['data_generation_set'][1]  # No calibration added when value was 'false'
        {'id': 'nmdc:dgen2'}
        """
       

        self.adapter.process_each_document(collection_name="workflow_execution_set", pipeline=[self.store_and_remove_calibrations])
        self.adapter.process_each_document(collection_name="data_generation_set", pipeline=[self.update_data_gen_calibration])

    def check_has_calibration(self, has_calibration_value) -> bool:
        r"""
        Checks for a valid data object id format (starts with 'nmdc:dobj')

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> db = {}
        >>> a = DictionaryAdapter(database=db)
        >>> m = Migrator(adapter=a)
        >>> m.check_has_calibration('nmdc:dobj-13-abc123')  # Valid format
        True
        >>> m.check_has_calibration('false')  # Invalid format
        False
        >>> m.check_has_calibration('nmdc:something-else')  # Invalid format
        False
        """

        pattern = r'^nmdc:dobj'

        return bool(re.match(pattern, has_calibration_value))
    
    def check_for_valid_data_object(self, data_obj_id) -> bool:
        r"""
        Checks database for valid data object. Returns False if not valid

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> db = {
        ...   'data_object_set': [
        ...     {'id': 'nmdc:dobj-13-abc123'},
        ...     {'id': 'nmdc:dobj-13-def456'}
        ...   ]
        ... }
        >>> a = DictionaryAdapter(database=db)
        >>> m = Migrator(adapter=a)
        >>> m.check_for_valid_data_object('nmdc:dobj-13-abc123')  # Exists in database
        True
        >>> m.check_for_valid_data_object('nmdc:dobj-13-nonexistent')  # Doesn't exist
        False
        """

        data_obj_doc = self.adapter.get_document_having_value_in_field(
                    collection_name="data_object_set", field_name="id", value=data_obj_id
                    )
        
        return data_obj_doc is not None

    def store_and_remove_calibrations(self, workflow_execution_doc) -> dict:
        r"""
        Moves the `has_calibration` field from the `WorkflowExecution` document to
        the corresponding `DataGeneration` document.

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> db = {
        ...   'workflow_execution_set': [
        ...     {'id': 'nmdc:wfx1', 'has_calibration': 'nmdc:dobj-13-abc123', 'was_informed_by': 'nmdc:dgen1'},
        ...     {'id': 'nmdc:wfx2', 'has_calibration': 'false', 'was_informed_by': 'nmdc:dgen2'}
        ...   ],
        ...   'data_generation_set': [
        ...     {'id': 'nmdc:dgen1'},
        ...     {'id': 'nmdc:dgen2'}
        ...   ],
        ...   'data_object_set': [
        ...     {'id': 'nmdc:dobj-13-abc123'}
        ...   ],
        ...   'calibration_set': [
        ...     {'id': 'nmdc:calib1', 'calibration_object': 'nmdc:dobj-13-abc123'}
        ...   ]
        ... }
        >>> a = DictionaryAdapter(database=db)
        >>> m = Migrator(adapter=a)
        >>> workflow_execution_doc = {'id': 'nmdc:wfx1', 'has_calibration': 'nmdc:dobj-13-abc123', 'was_informed_by': 'nmdc:dgen1'}
        >>> m.store_and_remove_calibrations(workflow_execution_doc)
        {'id': 'nmdc:wfx1', 'was_informed_by': 'nmdc:dgen1'}
        >>> workflow_execution_doc = {'id': 'nmdc:wfx2', 'has_calibration': 'false', 'was_informed_by': 'nmdc:dgen2'}
        >>> m.store_and_remove_calibrations(workflow_execution_doc)
        {'id': 'nmdc:wfx2', 'was_informed_by': 'nmdc:dgen2'}
        >>> workflow_execution_doc = {'id': 'nmdc:wfx3', 'has_calibration': 'invalid', 'was_informed_by': 'nmdc:dgen3'}
        >>> m.store_and_remove_calibrations(workflow_execution_doc)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ValueError: The 'has_calibration' value (invalid) in document (nmdc:wfx3) is not recognized
        """

        calibration_mapping = {} #create dictionary to store mappings

        if "has_calibration" in workflow_execution_doc:
            has_calibration_data_obj_id = workflow_execution_doc.get("has_calibration")

            # If has_calibration has a string value of false, remove the slot altogether from the document
            if has_calibration_data_obj_id.lower() == 'false':
                workflow_execution_doc.pop("has_calibration")
            
            # If the has_calibration value is not a data object id or does not have a value of "false"
            # raise an error.
            elif not self.check_has_calibration(has_calibration_data_obj_id):
                raise ValueError(f"The 'has_calibration' value ({has_calibration_data_obj_id}) in document "
                             f"({workflow_execution_doc['id']}) is not recognized")
            
            # If has_calibration is a nmdc data object identifier:
            elif self.check_has_calibration(has_calibration_data_obj_id):
    
                if not self.check_for_valid_data_object(has_calibration_data_obj_id):
                    raise ValueError(f"The 'has_calibration' value ({has_calibration_data_obj_id}) in document "
                             f"({workflow_execution_doc['id']}) is not a valid data object. The data object does not exist")
                else:
                    data_gen_doc = self.adapter.get_document_having_value_in_field(
                        collection_name="data_generation_set", field_name="id", value=workflow_execution_doc["was_informed_by"])
                    
                    calibration_doc = self.adapter.get_document_having_value_in_field(
                        collection_name="calibration_set", field_name="calibration_object", value=has_calibration_data_obj_id)
                   
                   # Store has_calibrations in calibration_mapping dictionary
                    calibration_mapping[data_gen_doc["id"]] = calibration_doc["id"]

                    if not hasattr(self, "calibration_mappings"):
                        self.calibration_mappings = {}
                    self.calibration_mappings.update(calibration_mapping)

                    # Remove calibration slot after storing mappings
                    workflow_execution_doc.pop("has_calibration")

        return workflow_execution_doc
    
    def update_data_gen_calibration(self, data_gen_doc) -> dict:
        r"""
        Updates data generation documents with calibration information

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> db = {
        ...   'workflow_execution_set': [
        ...     {'id': 'nmdc:wfx1', 'has_calibration': 'nmdc:dobj-13-abc123', 'was_informed_by': 'nmdc:dgen1', 'type': 'nmdc:MetabolomicsAnalysis'}
        ...   ],
        ...   'data_generation_set': [
        ...     {'id': 'nmdc:dgen1'},
        ...     {'id': 'nmdc:dgen2'}  # doc without corresponding calibration
        ...   ],
        ...   'data_object_set': [
        ...     {'id': 'nmdc:dobj-13-abc123'}
        ...   ],
        ...   'calibration_set': [
        ...     {'id': 'nmdc:calib1', 'calibration_object': 'nmdc:dobj-13-abc123'}
        ...   ]
        ... }
        >>> a = DictionaryAdapter(database=db)
        >>> m = Migrator(adapter=a)
        >>> # First store calibrations
        >>> workflow_execution_doc = {'id': 'nmdc:wfx1', 'has_calibration': 'nmdc:dobj-13-abc123', 'was_informed_by': 'nmdc:dgen1', 'type': 'nmdc:MetabolomicsAnalysis'}
        >>> _ = m.store_and_remove_calibrations(workflow_execution_doc)  # Store the calibrations first
        >>> # Then test update_data_gen_calibration
        >>> m.update_data_gen_calibration({'id': 'nmdc:dgen1'})  # doc with corresponding calibration
        {'id': 'nmdc:dgen1', 'has_calibration': 'nmdc:calib1'}
        >>> # Test document without calibration
        >>> m.update_data_gen_calibration({'id': 'nmdc:dgen2'})  # doc without corresponding calibration
        {'id': 'nmdc:dgen2'}
        """

        if data_gen_doc["id"] in self.calibration_mappings:
            data_gen_doc["has_calibration"] = self.calibration_mappings[data_gen_doc["id"]]
        return data_gen_doc
