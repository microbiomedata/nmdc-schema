# Auto generated from jgi_metagenomics.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-10-31T15:51:04
# Schema: jgi_metagenomics
#
# id: https://microbiomedata/schema/jgi_metagenomics
# description: This file defines terms that appear in the 'JGI-Metagenomics' section of the NMDC sample metadata
#              submission portal, which is implemented with DataHarmonizer as of Spring 2022
# license: license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NMDC = CurieNamespace('nmdc', 'https://w3id.org/nmdc/')
DEFAULT_ = NMDC


# Types

# Class references




# Enumerations
class DnaContTypeEnum(EnumDefinitionImpl):

    plate = PermissibleValue(text="plate")
    tube = PermissibleValue(text="tube")

    _defn = EnumDefinition(
        name="DnaContTypeEnum",
    )

class DnaDnaseEnum(EnumDefinitionImpl):

    no = PermissibleValue(text="no")
    yes = PermissibleValue(text="yes")

    _defn = EnumDefinition(
        name="DnaDnaseEnum",
    )

class DnaSampleFormatEnum(EnumDefinitionImpl):

    DNAStable = PermissibleValue(text="DNAStable")
    Ethanol = PermissibleValue(text="Ethanol")
    PBS = PermissibleValue(text="PBS")
    Pellet = PermissibleValue(text="Pellet")
    RNAStable = PermissibleValue(text="RNAStable")
    TE = PermissibleValue(text="TE")
    Water = PermissibleValue(text="Water")

    _defn = EnumDefinition(
        name="DnaSampleFormatEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "10 mM Tris-HCl",
                PermissibleValue(text="10 mM Tris-HCl") )
        setattr(cls, "Low EDTA TE",
                PermissibleValue(text="Low EDTA TE") )
        setattr(cls, "MDA reaction buffer",
                PermissibleValue(text="MDA reaction buffer") )

# Slots
class slots:
    pass

slots.dna_absorb1 = Slot(uri=NMDC.dna_absorb1, name="dna_absorb1", curie=NMDC.curie('dna_absorb1'),
                   model_uri=NMDC.dna_absorb1, domain=None, range=Optional[str])

slots.dna_absorb2 = Slot(uri=NMDC.dna_absorb2, name="dna_absorb2", curie=NMDC.curie('dna_absorb2'),
                   model_uri=NMDC.dna_absorb2, domain=None, range=Optional[str])

slots.dna_collect_site = Slot(uri=NMDC.dna_collect_site, name="dna_collect_site", curie=NMDC.curie('dna_collect_site'),
                   model_uri=NMDC.dna_collect_site, domain=None, range=Optional[str])

slots.dna_concentration = Slot(uri=NMDC.dna_concentration, name="dna_concentration", curie=NMDC.curie('dna_concentration'),
                   model_uri=NMDC.dna_concentration, domain=None, range=Optional[str])

slots.dna_cont_type = Slot(uri=NMDC.dna_cont_type, name="dna_cont_type", curie=NMDC.curie('dna_cont_type'),
                   model_uri=NMDC.dna_cont_type, domain=None, range=Optional[Union[str, "DnaContTypeEnum"]])

slots.dna_cont_well = Slot(uri=NMDC.dna_cont_well, name="dna_cont_well", curie=NMDC.curie('dna_cont_well'),
                   model_uri=NMDC.dna_cont_well, domain=None, range=Optional[str])

slots.dna_container_id = Slot(uri=NMDC.dna_container_id, name="dna_container_id", curie=NMDC.curie('dna_container_id'),
                   model_uri=NMDC.dna_container_id, domain=None, range=Optional[str])

slots.dna_dnase = Slot(uri=NMDC.dna_dnase, name="dna_dnase", curie=NMDC.curie('dna_dnase'),
                   model_uri=NMDC.dna_dnase, domain=None, range=Optional[Union[str, "DnaDnaseEnum"]])

slots.dna_isolate_meth = Slot(uri=NMDC.dna_isolate_meth, name="dna_isolate_meth", curie=NMDC.curie('dna_isolate_meth'),
                   model_uri=NMDC.dna_isolate_meth, domain=None, range=Optional[str])

slots.dna_organisms = Slot(uri=NMDC.dna_organisms, name="dna_organisms", curie=NMDC.curie('dna_organisms'),
                   model_uri=NMDC.dna_organisms, domain=None, range=Optional[str])

slots.dna_project_contact = Slot(uri=NMDC.dna_project_contact, name="dna_project_contact", curie=NMDC.curie('dna_project_contact'),
                   model_uri=NMDC.dna_project_contact, domain=None, range=Optional[str])

slots.dna_samp_id = Slot(uri=NMDC.dna_samp_id, name="dna_samp_id", curie=NMDC.curie('dna_samp_id'),
                   model_uri=NMDC.dna_samp_id, domain=None, range=Optional[str])

slots.dna_sample_format = Slot(uri=NMDC.dna_sample_format, name="dna_sample_format", curie=NMDC.curie('dna_sample_format'),
                   model_uri=NMDC.dna_sample_format, domain=None, range=Optional[Union[str, "DnaSampleFormatEnum"]])

slots.dna_sample_name = Slot(uri=NMDC.dna_sample_name, name="dna_sample_name", curie=NMDC.curie('dna_sample_name'),
                   model_uri=NMDC.dna_sample_name, domain=None, range=Optional[str])

slots.dna_seq_project = Slot(uri=NMDC.dna_seq_project, name="dna_seq_project", curie=NMDC.curie('dna_seq_project'),
                   model_uri=NMDC.dna_seq_project, domain=None, range=Optional[str])

slots.dna_seq_project_pi = Slot(uri=NMDC.dna_seq_project_pi, name="dna_seq_project_pi", curie=NMDC.curie('dna_seq_project_pi'),
                   model_uri=NMDC.dna_seq_project_pi, domain=None, range=Optional[str])

slots.dna_seq_project_name = Slot(uri=NMDC.dna_seq_project_name, name="dna_seq_project_name", curie=NMDC.curie('dna_seq_project_name'),
                   model_uri=NMDC.dna_seq_project_name, domain=None, range=Optional[str])

slots.dna_volume = Slot(uri=NMDC.dna_volume, name="dna_volume", curie=NMDC.curie('dna_volume'),
                   model_uri=NMDC.dna_volume, domain=None, range=Optional[str])

slots.proposal_dna = Slot(uri=NMDC.proposal_dna, name="proposal_dna", curie=NMDC.curie('proposal_dna'),
                   model_uri=NMDC.proposal_dna, domain=None, range=Optional[str])
