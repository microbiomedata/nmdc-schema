from nmdc_schema.migrators.migrator_base import MigratorBase
from nmdc_schema.migrators.adapters.adapter_base import AdapterBase
from difflib import SequenceMatcher

class Migrator(MigratorBase):
    r"""
    Migrates data from X to PR31, removes used slot from WorkflowExecution subclasses and checks that the 
    value in the used slot on the WorkflowExecution classes matches the value on the DataGeneration 
    instances in the instrument_name slot.
    """

    _from_version = "X"
    _to_version = "PR31"

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
    
    def preprocess_string(self, s):
        r"""
        Normalizes strings prior to using SequenceMatcher. Removes white spaces, hyphens, and 
        underscores from a string so difflib's SequenceMatcher can find the longest contiguous 
        matching subsequence between two sequences and these characters will not interfere.
        >>> m = Migrator()
        >>> m.preprocess_string('a  b_-_c -de:f g')
        'abcde:fg'
        """

        return s.replace(" ", "").replace("_","").replace("-","")

    def remove_used_slot(self, doc: dict) -> dict:
        r"""
        Removes the `used` slot from `WorkflowExecution` subclasses if the value matches the 
        instrument_name slot from the corresponding `OmicsProcessing` document by the longest
        common sequence.

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>>
        >>> database = {'omics_processing_set':[{'id':'nmdc:omcp-123', 'instrument_name':'nmdc:wfc-456'}]}  # in this example, our data store is a Python dictionary
        >>> adapter = DictionaryAdapter(database=database)
        >>> m = Migrator(adapter=adapter)
        >>> m.remove_used_slot({'id': 'nmdc:metab-123', 'used': 'nmdc:wfc-456', 'was_informed_by': 'nmdc:omcp-123'})
        {'id': 'nmdc:metab-123', 'was_informed_by': 'nmdc:omcp-123'}
        """
        
        if "used" in doc:
            omics_processing_doc = self.adapter.get_document_having_value_in_field(
                collection_name="omics_processing_set", field_name="id", value=doc["was_informed_by"]
            )
            
            # Preprocess instrument strings to ignore hyphens, underscores, and blank spaces
            processed_workflow_instrument_string = self.preprocess_string(doc["used"])
            processed_omics_doc_instrument_string = self.preprocess_string(omics_processing_doc["instrument_name"])
            
            similarity_ratio = SequenceMatcher(None, processed_workflow_instrument_string, processed_omics_doc_instrument_string).ratio()
            threshold = 0.8
            if similarity_ratio >= threshold:
                if similarity_ratio < 1.0:
                    self.logger.info(f"Workflow with id {doc['id']} has instrument: {doc['used']} matches OmicsProcessing doc instrument: {omics_processing_doc['instrument_name']} well enough")
                doc.pop("used")
            else:
                raise ValueError(f"The 'used' value ({doc['used']}) "
                                 f"on the WorkflowExecution document ({doc['id']}) "
                                 f"does not match the instrument name ({omics_processing_doc['instrument_name']}).")
        
        return doc

    
