from nmdc_schema.migrators.migrator_base import MigratorBase
from nmdc_schema.migrators.helpers import load_yaml_asset
import difflib
import uuid


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "X"
    _to_version = "PR19_and_PR70"

    def upgrade(self):
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""

        self.adapter.create_collection(collection_name="instrument_set")
        self.fill_instrument_set()
        # change to datageneration set depending on when migrator will happen
        self.adapter.process_each_document(collection_name="omics_processing_set", pipeline=[self.transform_instrument_slot]) 

    def mint_ids(self):
        r"""
        TODO: Replace me with real minting
        """

        return "potato:" + str(uuid.uuid4())

    def fill_instrument_set(self):
        # r""""
        # Fills the instrument_set collection from a YAML file of curated instrument instances
        
        # >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        # >>>
        # >>> database = {"instrument_set": []}  # seeds the database
        # >>> adapter = DictionaryAdapter(database=database)
        # >>> m = Migrator(adapter=adapter)
        # >>> m.instruments = [{'name': 'hiseq', 'model': 'hiseq 2500', 'vendor': 'bruker', 'type': 'nmdc:Instrument'}]
        # >>> m.instrument_id = 'potato:123'
        # >>> m.fill_instrument_set()
        # >>> adapter.get_document_having_value_in_field('instrument_set', 'name', value='hiseq')
        # {'id': 'potato:123', 'name': 'hiseq', 'model': 'hiseq 2500', 'vendor': 'bruker', 'type': 'nmdc:Instrument'}

        # """

        instruments = load_yaml_asset("migrator_from_X_to_PR19_and_PR70/instrument_set.yaml")
        for instrument in instruments:
            
            # Mint instrument id and insert into dict
            instrument_id = self.mint_ids()
            instrument["id"] = instrument_id

            self.adapter.insert_document("instrument_set", instrument)

    def transform_instrument_slot(self, omics_doc: dict):
        r"""
        Changes the instrument_name slot to be instrument_used, and replaces the name string value with an identifier for 
        the instrument

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>>
        >>> database = {'instrument_set': [{'id': 'nmdc:inst-456', 'name': '12T FT-ICR MS', 'model':'solarix_12T', 'vendor':'bruker', 'type':'nmdc:Instrument'}]} 
        >>> adapter = DictionaryAdapter(database=database)
        >>> m = Migrator(adapter=adapter)
        >>> m.transform_instrument_slot({'id': 'nmdc:omcp-123', 'instrument_name': '12T_FTICR_B'})
        {'id': 'nmdc:omcp-123', 'instrument_used': 'nmdc:inst-456'}
        """

        if "instrument_name" in omics_doc:
            existing_instrument_name = omics_doc["instrument_name"]
            
            instruments = load_yaml_asset("migrator_from_X_to_PR19_and_PR70/instrument_set.yaml")
            allowed_instrument_names = [instrument["name"] for instrument in instruments]
            
            matches = difflib.get_close_matches(existing_instrument_name, allowed_instrument_names, n=1, cutoff=0.25)

            if matches:

                    # Match instrument_name with with instrument set and get corresponding instrument id
                    match = matches[0]
                    self.logger.info(f"instrument_name in {omics_doc['id']} is {omics_doc['instrument_name']} and will be matched to instrument with name {match}")
                    
                    instrument = self.adapter.get_document_having_value_in_field(
                        collection_name="instrument_set", field_name="name", value=match
                    )

                    instrument_id = instrument.get("id")
                    omics_doc["instrument_used"] = instrument_id
                    del omics_doc["instrument_name"]
        
            else:
                self.logger.error(f"The instrument_name {omics_doc['id']} has a value of {omics_doc['instrument_name']}, but did not have any matches with the cutoff set at 0.25")

        return omics_doc


        