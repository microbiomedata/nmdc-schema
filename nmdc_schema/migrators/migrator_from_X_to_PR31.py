from nmdc_schema.migrators.migrator_base import MigratorBase
from nmdc_schema.migrators.adapters.adapter_base import AdapterBase

class Migrator(MigratorBase):
    r"""
    Migrates data from X to PR31, removes used slot from WorkflowExecution subclasses and checks that the 
    value in the used slot on the WorkflowExecution classes matches the value on the DataGeneration 
    instances in the instrument_name slot.
    """

    _from_version = "X"
    _to_version = "PR31"

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

        self.omics_processing_instrument_dict = {}


    def upgrade(self):
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""
        
        workflow_execution_collection_names = [
            "mags_activity_set",
            "metabolomics_analysis_activity_set",
            "metagenome_annotation_activity_set",
            "metagenome_assembly_set",
            "metagenome_sequencing_activity_set",
            "metatranscriptome_activity_set",
            "nom_analysis_activity_set",
            "omics_processing_set",
            "read_based_taxonomy_analysis_activity_set",
            "read_qc_analysis_activity_set"
            "metaproteomics_analysis_activity_set"   
        ]
        
        for collection_name in workflow_execution_collection_names:
            self.adapter.process_each_document(
                collection_name=collection_name,
                pipeline=[self.remove_used_slot],
            )

        self.adapter.process_each_document(collection_name="omics_processing_set", pipeline=[self.add_instrument_name])

        for collection_name in workflow_execution_collection_names:
            self.adapter.process_each_document(
                collection_name=collection_name,
                pipeline=[self.remove_used_slot],
            )
    
    def remove_used_slot(self, doc: dict) -> dict:
        r"""
        Removes the `used` slot from `WorkflowExecution` subclasses.

        If the value of the `used` slot does not match the value of the `instrument_name` slot of a related `OmicsProcessing`,
        log the error.

        Or if the `instrument_name` is missing in `OmicsProcessing` but `used` exists in `WorfklowExecution`, add `instrument_name` to `OmicsProcessing`.

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>>
        >>> database = {'omics_processing_set':[{'id':'nmdc:omcp-123', 'instrument_name':'nmdc:wfc-456'}]}  # in this example, our data store is a Python dictionary
        >>> adapter = DictionaryAdapter(database=database)
        >>> m = Migrator(adapter=adapter)
        >>> m.remove_used_slot({'id': 'nmdc:metab-123', 'used': 'nmdc:wfc-456', 'was_informed_by': 'nmdc:omcp-123'})
        {'id': 'nmdc:metab-123', 'was_informed_by': 'nmdc:omcp-123'}
        """
        if "used" in doc:
            try:
                omics_processing_doc = self.adapter.get_document_having_value_in_field(
                    collection_name="omics_processing_set", field_name="id", value=doc["was_informed_by"]
                    )

                if doc["used"] == omics_processing_doc["instrument_name"]:
                    doc.pop("used")
                elif 'instrument_name' not in omics_processing_doc:
                    # Get the omics_processing_id from the was_informed_by slot of the workflow execution doc
                    omics_processing_id = omics_processing_doc["id"]
                    
                    if omics_processing_id not in self.omics_processing_instrument_dict:
                        # add id to dictionary associated with the instrument_name
                        self.omics_processing_instrument_dict[omics_processing_id] = doc["used"]

            except:
                self.logger.error(f"WorkflowExecution {doc['id']} used: {doc['used']} does not match OmicsProcessing {omics_processing_doc['id']} instrument_name {omics_processing_doc['instrument_name']}.")
        
        return doc

    def add_instrument_name(self, doc: dict) -> dict:
        r"""
        Add `instrument_name` to `OmicsProcessing` set using the `omics_processing_instrument_dict` from the `init`.

        >>> m = Migrator()
        >>> m.omics_processing_instrument_dict['nmdc:omcp-123'] = 'nmdc:wfc-456'
        >>> m.add_instrument_name({'id': 'nmdc:omcp-123'})
        {'id': 'nmdc:omcp-123', 'instrument_name': 'nmdc:wfc-456'}
        """
        omics_processing_id = doc['id']
        doc["instrument_name"] = self.omics_processing_instrument_dict[omics_processing_id]

        return doc

    
