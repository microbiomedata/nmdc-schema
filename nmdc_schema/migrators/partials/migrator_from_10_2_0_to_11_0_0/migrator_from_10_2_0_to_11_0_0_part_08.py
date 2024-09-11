import difflib
import uuid
from typing import List

from nmdc_schema.migrators.migrator_base import MigratorBase
from nmdc_schema.migrators.helpers import load_yaml_asset


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "X"
    _to_version = "PR19_and_PR70"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Read the instrument data into an instance variable up front, for future reference.
        self.instruments: List[dict] = load_yaml_asset("migrator_from_10_2_0_to_11_0_0_part_08/instrument_set.yaml")

    def upgrade(self):
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""

        self.adapter.create_collection(collection_name="instrument_set")
        self.fill_instrument_set()
      
        self.adapter.process_each_document(collection_name="omics_processing_set", pipeline=[self.transform_instrument_slot]) 

    def fill_instrument_set(self):
        r"""
        Fills the instrument_set collection from a YAML file of curated instrument instances
        
        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>>
        >>> database = {"instrument_set": []}  # seeds the database
        >>> adapter = DictionaryAdapter(database=database)
        >>> m = Migrator(adapter=adapter)
        >>> m.fill_instrument_set()
        >>> result = adapter.get_document_having_value_in_field('instrument_set', 'name', value='12T FT-ICR MS')
        >>> result['name']
        '12T FT-ICR MS'
        >>> result['vendor']
        'bruker'
        >>> result['model']
        'solarix_12T'
        >>> result['type']
        'nmdc:Instrument'
        """

        for instrument in self.instruments:
            self.adapter.insert_document("instrument_set", instrument)

    def transform_instrument_slot(self, omics_doc: dict):
        r"""
        Changes the `instrument_name` slot to be `instrument_used`, and replaces the name string value with an identifier for 
        the instrument

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>>
        >>> database = {
        ...     'instrument_set': [
        ...        {'id': 'nmdc:inst-456', 'name': '12T FT-ICR MS', 'model':'solarix_12T', 'vendor':'bruker', 'type':'nmdc:Instrument'},
        ...        {'id': 'nmdc:inst-101', 'name': 'Illumina NovaSeq 6000', 'model':'my model', 'vendor':'my vendor', 'type':'nmdc:Instrument'},
        ...     ]
        ... } 
        >>> adapter = DictionaryAdapter(database=database)
        >>> m = Migrator(adapter=adapter)
        >>> m.transform_instrument_slot({'id': 'nmdc:omcp-123', 'instrument_name': '12T_FTICR_B'})
        {'id': 'nmdc:omcp-123', 'instrument_used': ['nmdc:inst-456']}
        >>> m.transform_instrument_slot({'id': 'nmdc:omcp-001', 'instrument_name': 'NovaSeq X'})
        {'id': 'nmdc:omcp-001', 'instrument_used': ['nmdc:inst-101']}

        Sanity tests related to `difflib`:
        >>> difflib.get_close_matches("a", ["ab", "cd"], n=1, cutoff=0.25)  # returns list containing the closest match
        ['ab']
        >>> difflib.get_close_matches("x", ["ab", "cd"], n=1, cutoff=0.25)  # returns empty list when no close matches
        []
        """

        if "instrument_name" in omics_doc:
            original_instrument_name = omics_doc["instrument_name"]

            # SPECIAL CASE: If the instrument name contains–but does not end with—"NovaSeq" (e.g. "NovaSeq S4"
            #               or "NovaSeq SP"), map it to "Illumina NovaSeq 6000", specifically.
            if "NovaSeq" in omics_doc['instrument_name'] and not omics_doc['instrument_name'].endswith("NovaSeq"):
                instrument = self.adapter.get_document_having_value_in_field(
                    collection_name="instrument_set", field_name="name", value="Illumina NovaSeq 6000"
                )

                self.logger.info(f"'instrument_name' in '{omics_doc['id']}' is '{omics_doc['instrument_name']}' "
                                 f"and will be mapped to instrument named 'Illumina NovaSeq 6000'")
            else:
                # Get a list of the allowed instrument names.
                #
                # Note: Instead of consulting the database, we consult the YAML file that was used to seed the database.
                #
                instruments = load_yaml_asset("migrator_from_10_2_0_to_11_0_0_part_08/instrument_set.yaml")
                allowed_instrument_names = [instrument["name"] for instrument in instruments]

                # Determine which of the allowed instrument names most closely matches the original one.
                # Reference: https://docs.python.org/3/library/difflib.html#difflib.get_close_matches
                cutoff = 0.25
                matches = difflib.get_close_matches(original_instrument_name, allowed_instrument_names, n=1, cutoff=cutoff)
                if len(matches) > 0:
                    allowed_instrument_name = matches[0]  # this is the most closely-matching, allowed instrument name

                    # Use the allowed instrument whose name most closely matches the original instrument's name.
                    self.logger.info(f"'instrument_name' in '{omics_doc['id']}' is '{omics_doc['instrument_name']}' "
                                     f"and will be mapped to instrument named '{allowed_instrument_name}'")

                    instrument = self.adapter.get_document_having_value_in_field(
                        collection_name="instrument_set", field_name="name", value=allowed_instrument_name
                    )

                else:
                    raise ValueError(f"The 'instrument_name' value ({original_instrument_name}) "
                                     f"on the OmicsProcessing document ({omics_doc['id']}) "
                                     f"does not match any of the allowed instrument names "
                                     f"(with a similarity score of at least {cutoff}).")

            # Map the Omics document to the allowed instrument.
            instrument_id = instrument.get("id")
            omics_doc["instrument_used"] = [instrument_id]

            # Delete the obsolete field from the Omics document.
            del omics_doc["instrument_name"]

        return omics_doc


        