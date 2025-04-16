from nmdc_schema.migrators.adapters.adapter_base import AdapterBase
from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.6.0.part_1"
    _to_version = "11.6.0.part_2"

    def __init__(self, adapter: AdapterBase=None, logger=None):
        super().__init__(adapter, logger)

        self.ids_of_metatranscriptome_data_generation_with_no_output = set()
        self.ids_of_data_objects_to_update = set()
        self.data_object_type_update_map = {
            "Metagenome Raw Reads": "Metatranscriptome Raw Reads",
            "Metagenome Raw Read 1": "Metatranscriptome Raw Read 1",
            "Metagenome Raw Read 2": "Metatranscriptome Raw Read 2",
        }

    def upgrade(self) -> None:
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""

        self.ids_of_metatranscriptome_data_generation_with_no_output = set()
        self.ids_of_data_objects_to_update = set()

        self.adapter.do_for_each_document("data_generation_set", self.scan_data_generation_set)
        self.adapter.do_for_each_document("workflow_execution_set", self.scan_workflow_execution_set)
        self.logger.info(f"Found {len(self.ids_of_data_objects_to_update)} data objects to update.")

        self.adapter.process_each_document("data_object_set",[self.update_data_object_type])

    def scan_data_generation_set(self, data_generation: dict) -> None:
        r"""
        If the incoming data_generation object has analyte_category set to "metatranscriptome", and
        has_output is not set, add the id of the data_generation object to the set of
        ids_of_metatranscriptome_data_generation_with_no_output. This set will be used when scanning
        the workflow_execution_set. If the incoming data_generation object has analyte_category set
        to "metatranscriptome", and has_output is set, add each data_generation id in the has_output
        list to the set of ids_of_data_objects_to_update.

        >>> m = Migrator()
        >>> m.scan_data_generation_set({'id': 'nmdc:dgns-11-12345678', 'analyte_category': 'metatranscriptome', 'has_output': ["nmdc:dobj-11-abcd1234"]})
        >>> m.ids_of_data_objects_to_update
        {'nmdc:dobj-11-abcd1234'}
        >>> m.ids_of_metatranscriptome_data_generation_with_no_output
        set()
        >>> m = Migrator()
        >>> m.scan_data_generation_set({'id': 'nmdc:dgns-11-12345678', 'analyte_category': 'metagenome', 'has_output': ["nmdc:dobj-11-abcd1234"]})
        >>> m.ids_of_data_objects_to_update
        set()
        >>> m.ids_of_metatranscriptome_data_generation_with_no_output
        set()
        >>> m = Migrator()
        >>> m.scan_data_generation_set({'id': 'nmdc:dgns-11-12345678', 'analyte_category': 'metatranscriptome'})
        >>> m.ids_of_data_objects_to_update
        set()
        >>> m.ids_of_metatranscriptome_data_generation_with_no_output
        {'nmdc:dgns-11-12345678'}
        """
        if data_generation.get("analyte_category") == "metatranscriptome":
            if "has_output" not in data_generation:
                self.ids_of_metatranscriptome_data_generation_with_no_output.add(data_generation["id"])
            else:
                for output in data_generation.get("has_output", []):
                    self.ids_of_data_objects_to_update.add(output)

    def scan_workflow_execution_set(self, workflow_execution: dict) -> None:
        r"""
        If the incoming workflow_execution object has was_informed_by relationship to a
        data_generation object that was flagged in the scan_data_generation_set step (i.e. it is
        in the ids_of_metatranscriptome_data_generation_with_no_output set), and the
        workflow_execution object has a has_output field, add each data_generation id in the
        has_output list to the set of ids_of_data_objects_to_update.

        >>> m = Migrator()
        >>> m.ids_of_metatranscriptome_data_generation_with_no_output = {'nmdc:dgns-11-12345678'}
        >>> m.scan_workflow_execution_set({'id': 'nmdc:wfmsa-11-12345678', 'type': 'nmdc:MetagenomeSequencing', 'was_informed_by': 'nmdc:dgns-11-12345678', 'has_output': ["nmdc:dobj-11-abcd1234"]})
        >>> m.ids_of_data_objects_to_update
        {'nmdc:dobj-11-abcd1234'}
        >>> m = Migrator()
        >>> m.ids_of_metatranscriptome_data_generation_with_no_output = {'nmdc:dgns-11-12345678'}
        >>> m.scan_workflow_execution_set({'id': 'nmdc:wfmsa-11-12345678', 'type': 'nmdc:MetagenomeSequencing', 'was_informed_by': 'nmdc:dgns-11-98765432', 'has_output': ["nmdc:dobj-11-abcd1234"]})
        >>> m.ids_of_data_objects_to_update
        set()
        """
        if workflow_execution.get("type") != "nmdc:MetagenomeSequencing":
            return

        if "was_informed_by" in workflow_execution:
            data_generation_id = workflow_execution["was_informed_by"]
            if data_generation_id in self.ids_of_metatranscriptome_data_generation_with_no_output:
                for output in workflow_execution.get("has_output", []):
                    self.ids_of_data_objects_to_update.add(output)

    def update_data_object_type(self, data_object: dict) -> dict:
        r"""
        Update the data_object_type of data_objects whose ids are in the
        ids_of_data_objects_to_update set. If the current data_object_type is "Metagenome Raw
        Reads", change it to "Metatranscriptome Raw Reads". If the data_object_type is "Metagenome
        Raw Read 1", change it to "Metatranscriptome Raw Read 1". If the data_object_type is
        "Metagenome Raw Read 2", change it to "Metatranscriptome Raw Read 2". Otherwise, do nothing.

        >>> m = Migrator()

        # In reality, this would be set by scan_data_generation_set and scan_workflow_execution_set
        >>> m.ids_of_data_objects_to_update = {"nmdc:dobj-11-abcd1234"}

        >>> m.update_data_object_type({'id': 'nmdc:dobj-11-abcd1234', 'data_object_type': 'Metagenome Raw Reads'})
        {'id': 'nmdc:dobj-11-abcd1234', 'data_object_type': 'Metatranscriptome Raw Reads'}
        >>> m.update_data_object_type({'id': 'nmdc:dobj-11-abcd1234', 'data_object_type': 'Metagenome Raw Read 1'})
        {'id': 'nmdc:dobj-11-abcd1234', 'data_object_type': 'Metatranscriptome Raw Read 1'}
        >>> m.update_data_object_type({'id': 'nmdc:dobj-11-abcd1234', 'data_object_type': 'Metagenome Raw Read 2'})
        {'id': 'nmdc:dobj-11-abcd1234', 'data_object_type': 'Metatranscriptome Raw Read 2'}

        # Don't update data_objects that have a data_object_type that we don't care about
        >>> m.update_data_object_type({'id': 'nmdc:dobj-11-abcd1234', 'data_object_type': 'Metagenome Bins Barplot'})
        {'id': 'nmdc:dobj-11-abcd1234', 'data_object_type': 'Metagenome Bins Barplot'}

        # Don't update data_objects that are not in the ids_of_data_objects_to_update set
        >>> m.update_data_object_type({'id': 'nmdc:dobj-11-wxyz9871', 'data_object_type': 'Metagenome Raw Reads'})
        {'id': 'nmdc:dobj-11-wxyz9871', 'data_object_type': 'Metagenome Raw Reads'}
        """
        data_object_id = data_object["id"]
        if data_object_id not in self.ids_of_data_objects_to_update:
            return data_object

        data_object_type = data_object["data_object_type"]
        if data_object_type not in self.data_object_type_update_map:
            return data_object

        data_object["data_object_type"] = self.data_object_type_update_map[data_object_type]
        return data_object
