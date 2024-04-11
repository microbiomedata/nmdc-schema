from nmdc_schema.migrators.migrator_base import MigratorBase
import uuid

# TODO: Add JGI and Gold identifiers? Add name?
# TODO: remove import uuid and fix minter function to how we will actually mint ids.
# TODO: Figure out where migrator will go. Write now written before collection name change. Need to change collection names if going after that migration. 
# Needs to come after the analyte_category migration
# TODO: Do we need to include a "name" slot for these? If so, what should the names be?
# TODO: Add doc tests


class Migrator(MigratorBase):
    """
    Migrates data from X to PR9, namely creates the workflow_chain_set, moves was_informed_by onto the
    WorkflowChain instances, and changes the part_of slots on WorkflowExecution subclass instances to the id
    of the corresponding WorfklowChain.
    """

    _from_version = "X"
    _to_version = "PR9"


    def __init__(self, adapter=None, logger=None):
        r"""Initialize an empty dictionary that maps was_informed_by values (omics processing id) to their
        respective workflow chain ids
        """

        super().__init__()
        self.adapter = adapter
        self.logger = logger
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
            "metaproteomics_analysis_activity_set"
        ]

        # Map was_informed_by slot values to newly minted workflow chain ids and populate workflow execution records part_of
        # with newly minted workflow chain id.
        for workflow_execution in workflow_executions:
            self.adapter.process_each_document(collection_name=workflow_execution, 
                                               pipeline=[self.was_informed_by_chain_mapping,
                                                         self.update_part_of_slot])
        
        # Create dictionary that maps omics processing ids to their analyte categories
        self.adapter.process_each_document(collection_name="omics_processing_set",
                                           pipeline=[self.omics_id_analyte_category_mapping])
        
        # Create and populate workflow_chain_set
        self.adapter.create_collection("workflow_chain_set")
        self.populate_workflow_chain()

        # Remove the was_informed_by slot on the WorkflowExecution records if they match in their corresponding WorkflowChain records
        for workflow_execution in workflow_executions:
            self.adapter.process_each_document(collection_name=workflow_execution,
                                               pipeline=[self.remove_was_informed_by])

    def mint_ids(self):

        return str(uuid.uuid4())


    def was_informed_by_chain_mapping(self, workflow_doc: dict):
        r"""
        Get the was_informed_by value (an omics processing id) from the first WorkflowExecution steps document and create a dictionary of the
        omics processing id with its corresponding worfklow chain id
        """

        workflow_chain_id = self.mint_ids()

        # Get the omics_processing_id from the was_informed_by slot of the read_qc_doc
        omics_processing_id = workflow_doc["was_informed_by"]

        if omics_processing_id not in self.workflow_omics_dict:

            self.workflow_omics_dict[omics_processing_id] = workflow_chain_id

        return workflow_doc

    
    def update_part_of_slot(self, doc: dict):
        r"""
        Replace the value, if there is one, in the part_of slot with the corresponding workflow chain id."""

        informed_by_omics_id = doc["was_informed_by"]
        workflow_chain_id = self.workflow_omics_dict.get(informed_by_omics_id)
        
        doc["part_of"] = [workflow_chain_id]

        return doc
    
    def omics_id_analyte_category_mapping(self, omics_doc: dict):
        r"""
        Get the analyte_category slot value from the omics processing docs (value from WorfklowExecution was_informed_by
        slot) and create a dictionary that maps omics id to analyte_category value)
        """
    
        omics_doc_id = omics_doc["id"]
        analyte_category = omics_doc["analyte_category"]

        self.omics_analyte_category_dict[omics_doc_id] = analyte_category

        return omics_doc
    
    def populate_workflow_chain(self):

        for omics_id, workflow_chain_id in self.workflow_omics_dict.items():
            workflow_chain_doc = {}
            if omics_id in self.omics_analyte_category_dict:
                analyte_category = self.omics_analyte_category_dict.get(omics_id)

            workflow_chain_doc["id"] = workflow_chain_id
            workflow_chain_doc["was_informed_by"] = omics_id

            workflow_chain_doc["analyte_category"] = analyte_category

            workflow_chain_doc["type"] = "nmdc:WorkflowChain"

            self.adapter.insert_document("workflow_chain_set", workflow_chain_doc)

            
    def remove_was_informed_by(self, workflow_doc: dict):

        omics_id = workflow_doc["was_informed_by"]
        workflow_chain_id = workflow_doc["part_of"]

        workflow_chain_doc = self.adapter.get_document_having_value_in_field(collection_name="workflow_chain_set", field_name="id", value=workflow_chain_id)
        
        if workflow_chain_doc["was_informed_by"] == omics_id:
            del workflow_doc["was_informed_by"]
        else:
            self.logger.error(f"WorkflowExecution doc with {workflow_doc['id']} was_informed_by slot does not match its workflow chain doc with id: {workflow_chain_doc['id']} was_informed_by_slot")

        return workflow_doc

    