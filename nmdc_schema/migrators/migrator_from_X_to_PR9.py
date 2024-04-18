import uuid

from nmdc_schema.migrators.migrator_base import MigratorBase
from nmdc_schema.migrators.adapters.adapter_base import AdapterBase


# TODO: remove import uuid and fix minter function to how we will actually mint ids.
# TODO: Add doc tests


class Migrator(MigratorBase):
    """
    Migrates data from X to PR9, namely creates the workflow_chain_set, moves was_informed_by onto the
    WorkflowChain instances, and changes the part_of slots on WorkflowExecution subclass instances to the id
    of the corresponding WorfklowChain.
    """

    _from_version = "X"
    _to_version = "PR9"

    def __init__(self, adapter: AdapterBase = None, logger=None):
        r"""
        Initialize an empty dictionary that maps was_informed_by values (omics processing id) to their
        respective workflow chain ids
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

        self.workflow_omics_dict = {}
        self.omics_analyte_category_dict = {}

    def upgrade(self):
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.
        """

        workflow_executions = [
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

        # Map was_informed_by slot values to newly minted workflow chain ids and populate workflow execution records part_of
        # with newly minted workflow chain id.
        for workflow_execution in workflow_executions:
            self.adapter.process_each_document(
                collection_name=workflow_execution,
                pipeline=[self.was_informed_by_chain_mapping, self.update_part_of_slot],
            )

        # Creates two dictionaries that maps 1) omics processing ids to their analyte categories, and
        # 2) maps associated_studies to the omics processing ids.
        self.adapter.process_each_document(
            collection_name="omics_processing_set",
            pipeline=[self.omics_id_analyte_category_mapping],
        )

        # Create and populate workflow_chain_set
        self.adapter.create_collection("workflow_chain_set")
        self.populate_workflow_chain()

        # Remove the was_informed_by slot on the WorkflowExecution records if they match in their corresponding WorkflowChain records
        for workflow_execution in workflow_executions:
            self.adapter.process_each_document(
                collection_name=workflow_execution,
                pipeline=[self.remove_was_informed_by],
            )

    def mint_id(self):
        r"""
        TODO: Replace me with real minting.
        """

        return "potato:" + str(uuid.uuid4())

    def was_informed_by_chain_mapping(self, workflow_doc: dict):
        r"""
        Get the was_informed_by value (an omics processing id) from the WorkflowExecution documents and
        create a dictionary of the omics processing id with its corresponding worfklow chain id

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>>
        >>> m = Migrator(adapter=DictionaryAdapter(database={}))
        >>> m.was_informed_by_chain_mapping({'id': 123, 'was_informed_by': 'nmdc:omcp-123'})
        {'id': 123, 'was_informed_by': 'nmdc:omcp-123'}
        >>> 'nmdc:omcp-123' in m.workflow_omics_dict
        True
        """

        # TODO: Replace me with real minting
        workflow_chain_id = self.mint_id()

        # Get the omics_processing_id from the was_informed_by slot of the read_qc_doc
        omics_processing_id = workflow_doc["was_informed_by"]

        if omics_processing_id not in self.workflow_omics_dict:
            self.workflow_omics_dict[omics_processing_id] = workflow_chain_id

        return workflow_doc

    def update_part_of_slot(self, workflow_doc: dict):
        r"""
        Replaces the value, if there is one, in the part_of slot in the workflow doc
        with the corresponding workflow chain id.

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>>
        >>> m = Migrator(adapter=DictionaryAdapter(database={}))
        >>> m.workflow_omics_dict = {'nmdc:omcp-123': 'nmdc:wfc-456'}
        >>> result1 = m.update_part_of_slot({'id': 456, 'was_informed_by': 'nmdc:omcp-123'})
        >>> result1
        {'id': 456, 'was_informed_by': 'nmdc:omcp-123', 'part_of': ['nmdc:wfc-456']}
        >>> result2 = m.update_part_of_slot({'id': 456, 'was_informed_by': 'nmdc:omcp-123', 'part_of': ['nmdc:789']})
        >>> result2
        {'id': 456, 'was_informed_by': 'nmdc:omcp-123', 'part_of': ['nmdc:wfc-456']}
        """

        informed_by_omics_id = workflow_doc["was_informed_by"]
        workflow_chain_id = self.workflow_omics_dict.get(informed_by_omics_id)

        workflow_doc["part_of"] = [workflow_chain_id]

        return workflow_doc

    def omics_id_analyte_category_mapping(self, omics_doc: dict):
        r"""
        Get the analyte_category slot value from the omics processing doc and create a dictionary that
        maps omics id to analyte_category value

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>>
        >>> m = Migrator(adapter=DictionaryAdapter(database={}))
        >>> omics_doc = {'id': 'nmdc:omcp-123', 'analyte_category': 'metagenome'}
        >>> result = m.omics_id_analyte_category_mapping(omics_doc)
        >>> result
        {'id': 'nmdc:omcp-123', 'analyte_category': 'metagenome'}
        >>> m.omics_analyte_category_dict
        {'nmdc:omcp-123': 'metagenome'}
        """

        omics_doc_id = omics_doc["id"]
        analyte_category = omics_doc["analyte_category"]

        self.omics_analyte_category_dict[omics_doc_id] = analyte_category

        return omics_doc

    def populate_workflow_chain(self):
        r"""
        Create and populate the workflow_chain_set collection based on the data in the workflow_omics_dict and 
        omics_analyte_category_dict.

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>>
        >>> database = {}  # in this example, our data store is a Python dictionary
        >>> adapter = DictionaryAdapter(database=database)
        >>> m = Migrator(adapter=adapter)
        >>> m.workflow_omics_dict = {'nmdc:omcp-123': 'nmdc:wfc-456'}
        >>> m.omics_analyte_category_dict = {'nmdc:omcp-123': 'metagenome'}
        >>> adapter.create_collection("workflow_chain_set")
        >>> m.populate_workflow_chain()
        >>> adapter.get_document_having_value_in_field('workflow_chain_set', 'id', value='nmdc:wfc-456')
        {'id': 'nmdc:wfc-456', 'was_informed_by': 'nmdc:omcp-123', 'analyte_category': 'metagenome', 'type': 'nmdc:WorkflowChain', 'name': 'Workflow Chain for metagenome analysis of nmdc:omcp-123'}
        """

        for omics_id, workflow_chain_id in self.workflow_omics_dict.items():
            workflow_chain_doc = {}

            if omics_id in self.omics_analyte_category_dict:
                analyte_category = self.omics_analyte_category_dict.get(omics_id)

            workflow_chain_doc["id"] = workflow_chain_id
            workflow_chain_doc["was_informed_by"] = omics_id

            workflow_chain_doc["analyte_category"] = analyte_category

            workflow_chain_doc["type"] = "nmdc:WorkflowChain"

            workflow_chain_doc["name"] = (
                f"Workflow Chain for {analyte_category} analysis of {omics_id}"
            )

            self.adapter.insert_document("workflow_chain_set", workflow_chain_doc)

    def remove_was_informed_by(self, workflow_doc: dict):
        r"""
        Removes the was_informed_by slot from the workflow sets if its value matches its corresponding 
        workflow_chain_set doc's was_informed_by value.

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>>
        >>> database = {}  # in this example, our data store is a Python dictionary
        >>> adapter = DictionaryAdapter(database=database)
        >>> m = Migrator(adapter=adapter)
        >>> m.workflow_omics_dict = {'nmdc:omcp-123': 'nmdc:wfc-456'}
        >>> m.omics_analyte_category_dict = {'nmdc:omcp-123': 'metagenome'}
        >>> adapter.create_collection("workflow_chain_set")
        >>> m.populate_workflow_chain()
        >>> adapter.get_document_having_value_in_field('workflow_chain_set', 'id', value='nmdc:wfc-456')
        >>> m.remove_was_informed_by({'id': 'nmdc:metab-123', 'part_of': ['nmdc:wfc-456'], 'was_informed_by': 'nmdc:omcp-123'})
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
                self.logger.error(
                    f"WorkflowExecution doc with id {workflow_doc['id']} was_informed_by slot does not match"
                    f"its workflow chain doc with id: {workflow_chain_doc['id']} was_informed_by_slot"
                )

        return workflow_doc
