from typing import Dict, List

from nmdc_schema.migrators.helpers import load_yaml_asset
from nmdc_schema.migrators.migrator_base import MigratorBase
from nmdc_schema.migrators.adapters.adapter_base import AdapterBase


class Migrator(MigratorBase):
    """
    Migrates data from X to PR9.

    Namely, creates the `workflow_chain_set` collection, moves `was_informed_by` onto the `WorkflowChain` instances,
    and changes the `part_of` slots on instances of subclasses of `WorkflowExecutionActivity` to the id of the
    corresponding `WorkflowChain`.
    """

    _from_version = "X"
    _to_version = "PR9"

    def __init__(self, adapter: AdapterBase = None, logger=None):
        r"""
        Initializes some empty dictionaries and loads minted `WorkflowChain` ids from a YAML file into a list.
        """

        # Invoke the `__init__` method of the "parent" class.
        #
        # Note: In Python, when a "child" (i.e. inheriting) class doesn't have its own `__init__` method,
        #       it inherits the "parent" class's `__init__` method. As a result, that inherited `__init__`
        #       method is the one that Python automatically invokes when the "child" class is instantiated.
        #
        #       In contrast, _this_ "child" class _does_ have its own `__init__` method (this comment is in it),
        #       effectively opting the "child" class out of the aforementioned inheritance and automatic invocation
        #       of the "parent" class's `__init__` method. So, here, we invoke that method "manually."
        #
        super().__init__(adapter=adapter, logger=logger)

        self.omics_proc_id_to_workflow_chain_id: Dict[str, str] = {}
        self.omics_proc_id_to_analyte_category: Dict[str, str] = {}
        self.workflow_chain_ids: List[str] = load_yaml_asset("migrator_from_X_to_PR9/workflow_chain_ids.yaml")

    def upgrade(self):
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.
        """

        workflow_execution_activity_collection_names = [
            "metagenome_sequencing_activity_set",
            "read_qc_analysis_activity_set",
            "metagenome_assembly_set",
            "read_based_taxonomy_analysis_activity_set",
            "metagenome_annotation_activity_set",
            "mags_activity_set",
            "metabolomics_analysis_activity_set",
            "nom_analysis_activity_set",
            "metatranscriptome_activity_set",
            "metaproteomics_analysis_activity_set",
        ]

        # Populate the dictionary that maps `OmicsProcessing` IDs to `WorkflowChain` IDs (using the `was_informed_by`
        # field of the `WorkflowExecutionActivity` document); then, store those `WorkflowChain` IDs in the `part_of`
        # field of `WorkflowExecutionActivity` documents.
        for collection_name in workflow_execution_activity_collection_names:
            self.adapter.process_each_document(
                collection_name=collection_name,
                pipeline=[self.generate_mapping_from_omics_proc_id_to_workflow_chain_id, self.update_part_of_field],
            )

        self.logger.info(f"{len(self.omics_proc_id_to_workflow_chain_id)=}")

        # Populate the dictionary that maps `OmicsProcessing` IDs to their analyte categories.
        self.adapter.process_each_document(
            collection_name="omics_processing_set",
            pipeline=[self.generate_mapping_from_omics_proc_id_to_analyte_category],
        )

        # Create and populate the `workflow_chain_set` collection.
        self.adapter.create_collection("workflow_chain_set")
        self.populate_workflow_chain()

        # Remove the `was_informed_by` field from the `WorkflowExecutionActivity` documents
        # if they match in their corresponding `WorkflowChain` records.
        for collection_name in workflow_execution_activity_collection_names:
            self.adapter.process_each_document(
                collection_name=collection_name,
                pipeline=[self.remove_was_informed_by_field],
            )

    def generate_mapping_from_omics_proc_id_to_workflow_chain_id(self, workflow_execution_activity: dict):
        r"""
        Gets the `OmicsProcessing` ID from the `was_informed_by` field of the `WorkflowExecutionActivity` document
        and — if not already done — adds it to the dictionary that maps `OmicsProcessing` IDs to `WorkflowChain` IDs.

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>>
        >>> m = Migrator(adapter=DictionaryAdapter(database={}))
        >>> m.generate_mapping_from_omics_proc_id_to_workflow_chain_id({'id': 123, 'was_informed_by': 'nmdc:omcp-123'})
        {'id': 123, 'was_informed_by': 'nmdc:omcp-123'}
        >>> 'nmdc:omcp-123' in m.omics_proc_id_to_workflow_chain_id
        True
        """

        omics_processing_id = workflow_execution_activity["was_informed_by"]
        if omics_processing_id not in self.omics_proc_id_to_workflow_chain_id.keys():

            # Claim a minted `WorkflowChain` ID — if we have any unclaimed ones — for this `OmicsProcessing` document.
            if len(self.workflow_chain_ids) > 0:
                workflow_chain_id = self.workflow_chain_ids.pop(0)  # removes and returns the first item in the list
                self.omics_proc_id_to_workflow_chain_id[omics_processing_id] = workflow_chain_id
            else:
                self.logger.error(f"No WorkflowChain ID available for OmicsProcessing: {omics_processing_id}")

        return workflow_execution_activity

    def update_part_of_field(self, workflow_execution_activity: dict):
        r"""
        Populates (replacing the existing value, if any) the `part_of` field of the `WorkflowExecutionActivity`
        document, with a list consisting of the `OmicsProcessing` ID from its own `was_informed_by` field.

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>>
        >>> m = Migrator(adapter=DictionaryAdapter(database={}))
        >>> m.omics_proc_id_to_workflow_chain_id = {'nmdc:omcp-123': 'nmdc:wfc-456'}
        >>> result1 = m.update_part_of_field({'id': 456, 'was_informed_by': 'nmdc:omcp-123'})
        >>> result1
        {'id': 456, 'was_informed_by': 'nmdc:omcp-123', 'part_of': ['nmdc:wfc-456']}
        >>> result2 = m.update_part_of_field({'id': 456, 'was_informed_by': 'nmdc:omcp-123', 'part_of': ['nmdc:789']})
        >>> result2
        {'id': 456, 'was_informed_by': 'nmdc:omcp-123', 'part_of': ['nmdc:wfc-456']}
        """

        omics_processing_id = workflow_execution_activity["was_informed_by"]
        workflow_chain_id = self.omics_proc_id_to_workflow_chain_id.get(omics_processing_id)
        workflow_execution_activity["part_of"] = [workflow_chain_id]

        return workflow_execution_activity

    def generate_mapping_from_omics_proc_id_to_analyte_category(self, omics_doc: dict):
        r"""
        Generates a mapping from `OmicsProcessing` IDs to analyte categories.

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>>
        >>> m = Migrator(adapter=DictionaryAdapter(database={}))
        >>> omics_doc = {'id': 'nmdc:omcp-123', 'analyte_category': 'metagenome'}
        >>> result = m.generate_mapping_from_omics_proc_id_to_analyte_category(omics_doc)
        >>> result
        {'id': 'nmdc:omcp-123', 'analyte_category': 'metagenome'}
        >>> m.omics_proc_id_to_analyte_category
        {'nmdc:omcp-123': 'metagenome'}
        """

        omics_doc_id = omics_doc["id"]
        analyte_category = omics_doc["analyte_category"]

        self.omics_proc_id_to_analyte_category[omics_doc_id] = analyte_category

        return omics_doc

    def populate_workflow_chain(self) -> None:
        r"""
        Populates the `workflow_chain_set` collection based upon the mappings defined in this class's initializer.

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>>
        >>> database = {"workflow_chain_set": []}  # seeds the database
        >>> adapter = DictionaryAdapter(database=database)
        >>> m = Migrator(adapter=adapter)
        >>> m.omics_proc_id_to_workflow_chain_id = {'nmdc:omcp-123': 'nmdc:wfc-456'}
        >>> m.omics_proc_id_to_analyte_category = {'nmdc:omcp-123': 'metagenome'}
        >>> m.populate_workflow_chain()
        >>> adapter.get_document_having_value_in_field('workflow_chain_set', 'id', value='nmdc:wfc-456')
        {'id': 'nmdc:wfc-456', 'was_informed_by': 'nmdc:omcp-123', 'analyte_category': 'metagenome', 'type': 'nmdc:WorkflowChain', 'name': 'Workflow Chain for metagenome analysis of nmdc:omcp-123'}
        """

        for omics_id, workflow_chain_id in self.omics_proc_id_to_workflow_chain_id.items():
            workflow_chain_doc = {}

            analyte_category = None
            if omics_id in self.omics_proc_id_to_analyte_category:
                analyte_category = self.omics_proc_id_to_analyte_category.get(omics_id)

            workflow_chain_doc["id"] = workflow_chain_id
            workflow_chain_doc["was_informed_by"] = omics_id
            workflow_chain_doc["analyte_category"] = analyte_category
            workflow_chain_doc["type"] = "nmdc:WorkflowChain"
            workflow_chain_doc["name"] = (
                f"Workflow Chain for {analyte_category} analysis of {omics_id}"
            )

            self.adapter.insert_document("workflow_chain_set", workflow_chain_doc)

    def remove_was_informed_by_field(self, workflow_doc: dict):
        r"""
        Removes the was_informed_by slot from the workflow sets if its value matches its corresponding 
        workflow_chain_set doc's was_informed_by value.

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>>
        >>> database = {'workflow_chain_set': [{'id': 'nmdc:wfc-456', 'was_informed_by': 'nmdc:omcp-123'}]}  # in this example, our data store is a Python dictionary
        >>> adapter = DictionaryAdapter(database=database)
        >>> m = Migrator(adapter=adapter)
        >>> m.remove_was_informed_by_field({'id': 'nmdc:metab-123', 'part_of': ['nmdc:wfc-456'], 'was_informed_by': 'nmdc:omcp-123'})
        {'id': 'nmdc:metab-123', 'part_of': ['nmdc:wfc-456']}
        """

        omics_id = workflow_doc["was_informed_by"]
        workflow_chain_ids = workflow_doc["part_of"]
        
        for wfc_id in workflow_chain_ids:

            workflow_chain_doc = self.adapter.get_document_having_value_in_field(
                collection_name="workflow_chain_set", field_name="id", value=wfc_id
            )
            self.logger.info(f"{workflow_chain_doc['id']=}")

            if workflow_chain_doc["was_informed_by"] == omics_id:
                del workflow_doc["was_informed_by"]
            else:
                raise ValueError(f"The 'was_informed_by' value ({omics_id}) "
                                 f"on the WorkflowExecutionActivity document ({workflow_doc['id']}) "
                                 f"doesn't match the 'was_informed_by' value ({workflow_chain_doc['was_informed_by']}) "
                                 f"on the corresponding WorkflowChain document ({workflow_chain_doc['id']}).")

        return workflow_doc
