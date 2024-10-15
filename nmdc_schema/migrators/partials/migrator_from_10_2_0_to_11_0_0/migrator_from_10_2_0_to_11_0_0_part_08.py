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
        >>> # Seed the database with instruments representative of those described in `instrument_set.yaml`.
        >>> #
        >>> # Note: These "input" names and the corresponding "output" names below were reviewed by a stakeholder at:
        >>> #       https://github.com/microbiomedata/berkeley-schema-fy24/pull/247#issuecomment-2342009832
        >>> #
        >>> database = dict(instrument_set=[])
        >>> for (id, name) in [
        ...     ('nmdc:inst-14-tjtq1d92', '12T FT-ICR MS'),
        ...     ('nmdc:inst-14-dzs60b60', '15T FT-ICR MS'),
        ...     ('nmdc:inst-14-nstrhv39', '21T FT-ICR MS'),
        ...     ('nmdc:inst-14-mwrrj632', '7T FT-ICR MS'),
        ...     ('nmdc:inst-14-fas8ny90', 'GC-MS'),
        ...     ('nmdc:inst-14-79zxap02', 'Illumina HiSeq'),
        ...     ('nmdc:inst-14-nn4b6k72', 'Illumina HiSeq 2500'),
        ...     ('nmdc:inst-14-xz5tb342', 'Illumina NextSeq 550'),
        ...     ('nmdc:inst-14-xx07be40', 'Illumina NovaSeq'),
        ...     ('nmdc:inst-14-mr4r2w09', 'Illumina NovaSeq 6000'),
        ...     ('nmdc:inst-14-kw06tx33', 'QExactHF03'),
        ...     ('nmdc:inst-14-e32bpm65', 'QExactP02'),
        ...     ('nmdc:inst-14-njkx0e66', 'VOrbiETD04'),
        ... ]:
        ...     instrument_doc = dict(id=id, name=name, model='', vendor='', type='nmdc:Instrument')
        ...     database['instrument_set'].append(instrument_doc)
        >>> adapter = DictionaryAdapter(database=database)
        >>> m = Migrator(adapter=adapter)
        >>> m.transform_instrument_slot({'id': 'nmdc:omcp-001', 'instrument_name': '12T_FTICR_B'})
        {'id': 'nmdc:omcp-001', 'instrument_used': ['nmdc:inst-14-tjtq1d92']}
        >>> m.transform_instrument_slot({'id': 'nmdc:omcp-001', 'instrument_name': '21T_Agilent'})
        {'id': 'nmdc:omcp-001', 'instrument_used': ['nmdc:inst-14-nstrhv39']}
        >>> m.transform_instrument_slot({'id': 'nmdc:omcp-001', 'instrument_name': '21T Agilent'})
        {'id': 'nmdc:omcp-001', 'instrument_used': ['nmdc:inst-14-nstrhv39']}
        >>> m.transform_instrument_slot({'id': 'nmdc:omcp-001', 'instrument_name': '7T_FT_ICR_MS'})
        {'id': 'nmdc:omcp-001', 'instrument_used': ['nmdc:inst-14-mwrrj632']}
        >>> m.transform_instrument_slot({'id': 'nmdc:omcp-001', 'instrument_name': 'Agilent_GC_MS_01'})
        {'id': 'nmdc:omcp-001', 'instrument_used': ['nmdc:inst-14-fas8ny90']}
        >>> m.transform_instrument_slot({'id': 'nmdc:omcp-001', 'instrument_name': 'Illumina HiSeq'})
        {'id': 'nmdc:omcp-001', 'instrument_used': ['nmdc:inst-14-79zxap02']}
        >>> m.transform_instrument_slot({'id': 'nmdc:omcp-001', 'instrument_name': 'Illumina HiSeq 2500-1TB'})
        {'id': 'nmdc:omcp-001', 'instrument_used': ['nmdc:inst-14-nn4b6k72']}
        >>> m.transform_instrument_slot({'id': 'nmdc:omcp-001', 'instrument_name': 'QExactP02'})
        {'id': 'nmdc:omcp-001', 'instrument_used': ['nmdc:inst-14-e32bpm65']}
        >>> m.transform_instrument_slot({'id': 'nmdc:omcp-001', 'instrument_name': 'QExactHF03'})
        {'id': 'nmdc:omcp-001', 'instrument_used': ['nmdc:inst-14-kw06tx33']}
        >>> m.transform_instrument_slot({'id': 'nmdc:omcp-001', 'instrument_name': 'Illumina NovaSeq S4'})
        {'id': 'nmdc:omcp-001', 'instrument_used': ['nmdc:inst-14-mr4r2w09']}
        >>> m.transform_instrument_slot({'id': 'nmdc:omcp-001', 'instrument_name': 'Illumina NovaSeq'})
        {'id': 'nmdc:omcp-001', 'instrument_used': ['nmdc:inst-14-xx07be40']}
        >>> m.transform_instrument_slot({'id': 'nmdc:omcp-001', 'instrument_name': 'Illumina NextSeq550'})
        {'id': 'nmdc:omcp-001', 'instrument_used': ['nmdc:inst-14-xz5tb342']}
        >>> m.transform_instrument_slot({'id': 'nmdc:omcp-001', 'instrument_name': 'NovaSeq SP'})
        {'id': 'nmdc:omcp-001', 'instrument_used': ['nmdc:inst-14-mr4r2w09']}
        >>> m.transform_instrument_slot({'id': 'nmdc:omcp-001', 'instrument_name': 'Illumina Illumina HiSeq'})
        {'id': 'nmdc:omcp-001', 'instrument_used': ['nmdc:inst-14-79zxap02']}

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


        