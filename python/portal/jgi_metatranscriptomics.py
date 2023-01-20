# Auto generated from jgi_metatranscriptomics.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-01-20T15:23:28
# Schema: jgi_metatranscriptomics
#
# id: https://microbiomedata/schema/jgi_metatranscriptomics
# description: This file defines terms that appear in the 'JGI-Metatranscriptomics' section of the NMDC sample
#              metadata submission portal, which is implemented with DataHarmonizer as of Spring 2022
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
class DnaseRnaEnum(EnumDefinitionImpl):

    no = PermissibleValue(text="no")
    yes = PermissibleValue(text="yes")

    _defn = EnumDefinition(
        name="DnaseRnaEnum",
    )

class RnaContTypeEnum(EnumDefinitionImpl):

    plate = PermissibleValue(text="plate")
    tube = PermissibleValue(text="tube")

    _defn = EnumDefinition(
        name="RnaContTypeEnum",
    )

class RnaSampleFormatEnum(EnumDefinitionImpl):

    DNAStable = PermissibleValue(text="DNAStable")
    Ethanol = PermissibleValue(text="Ethanol")
    PBS = PermissibleValue(text="PBS")
    Pellet = PermissibleValue(text="Pellet")
    RNAStable = PermissibleValue(text="RNAStable")
    TE = PermissibleValue(text="TE")
    Water = PermissibleValue(text="Water")

    _defn = EnumDefinition(
        name="RnaSampleFormatEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "10 mM Tris-HCl",
                PermissibleValue(text="10 mM Tris-HCl") )
        setattr(cls, "Low EDTA TE",
                PermissibleValue(text="Low EDTA TE") )
        setattr(cls, "MDA reaction buffer",
                PermissibleValue(text="MDA reaction buffer") )
        setattr(cls, "Gentegra-DNA",
                PermissibleValue(text="Gentegra-DNA") )
        setattr(cls, "Gentegra-RNA",
                PermissibleValue(text="Gentegra-RNA") )

# Slots
class slots:
    pass

slots.dnase_rna = Slot(uri=NMDC.dnase_rna, name="dnase_rna", curie=NMDC.curie('dnase_rna'),
                   model_uri=NMDC.dnase_rna, domain=None, range=Optional[Union[str, "DnaseRnaEnum"]])

slots.proposal_rna = Slot(uri=NMDC.proposal_rna, name="proposal_rna", curie=NMDC.curie('proposal_rna'),
                   model_uri=NMDC.proposal_rna, domain=None, range=Optional[str])

slots.rna_absorb1 = Slot(uri=NMDC.rna_absorb1, name="rna_absorb1", curie=NMDC.curie('rna_absorb1'),
                   model_uri=NMDC.rna_absorb1, domain=None, range=Optional[str])

slots.rna_absorb2 = Slot(uri=NMDC.rna_absorb2, name="rna_absorb2", curie=NMDC.curie('rna_absorb2'),
                   model_uri=NMDC.rna_absorb2, domain=None, range=Optional[str])

slots.rna_collect_site = Slot(uri=NMDC.rna_collect_site, name="rna_collect_site", curie=NMDC.curie('rna_collect_site'),
                   model_uri=NMDC.rna_collect_site, domain=None, range=Optional[str])

slots.rna_concentration = Slot(uri=NMDC.rna_concentration, name="rna_concentration", curie=NMDC.curie('rna_concentration'),
                   model_uri=NMDC.rna_concentration, domain=None, range=Optional[str])

slots.rna_cont_type = Slot(uri=NMDC.rna_cont_type, name="rna_cont_type", curie=NMDC.curie('rna_cont_type'),
                   model_uri=NMDC.rna_cont_type, domain=None, range=Optional[Union[str, "RnaContTypeEnum"]])

slots.rna_cont_well = Slot(uri=NMDC.rna_cont_well, name="rna_cont_well", curie=NMDC.curie('rna_cont_well'),
                   model_uri=NMDC.rna_cont_well, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?!A1|A12|H1|H12)(([A-H][1-9])|([A-H]1[0-2]))$'))

slots.rna_container_id = Slot(uri=NMDC.rna_container_id, name="rna_container_id", curie=NMDC.curie('rna_container_id'),
                   model_uri=NMDC.rna_container_id, domain=None, range=Optional[str])

slots.rna_isolate_meth = Slot(uri=NMDC.rna_isolate_meth, name="rna_isolate_meth", curie=NMDC.curie('rna_isolate_meth'),
                   model_uri=NMDC.rna_isolate_meth, domain=None, range=Optional[str])

slots.rna_organisms = Slot(uri=NMDC.rna_organisms, name="rna_organisms", curie=NMDC.curie('rna_organisms'),
                   model_uri=NMDC.rna_organisms, domain=None, range=Optional[str])

slots.rna_project_contact = Slot(uri=NMDC.rna_project_contact, name="rna_project_contact", curie=NMDC.curie('rna_project_contact'),
                   model_uri=NMDC.rna_project_contact, domain=None, range=Optional[str])

slots.rna_samp_id = Slot(uri=NMDC.rna_samp_id, name="rna_samp_id", curie=NMDC.curie('rna_samp_id'),
                   model_uri=NMDC.rna_samp_id, domain=None, range=Optional[str])

slots.rna_sample_format = Slot(uri=NMDC.rna_sample_format, name="rna_sample_format", curie=NMDC.curie('rna_sample_format'),
                   model_uri=NMDC.rna_sample_format, domain=None, range=Optional[Union[str, "RnaSampleFormatEnum"]])

slots.rna_sample_name = Slot(uri=NMDC.rna_sample_name, name="rna_sample_name", curie=NMDC.curie('rna_sample_name'),
                   model_uri=NMDC.rna_sample_name, domain=None, range=Optional[str])

slots.rna_seq_project = Slot(uri=NMDC.rna_seq_project, name="rna_seq_project", curie=NMDC.curie('rna_seq_project'),
                   model_uri=NMDC.rna_seq_project, domain=None, range=Optional[str])

slots.rna_seq_project_pi = Slot(uri=NMDC.rna_seq_project_pi, name="rna_seq_project_pi", curie=NMDC.curie('rna_seq_project_pi'),
                   model_uri=NMDC.rna_seq_project_pi, domain=None, range=Optional[str])

slots.rna_seq_project_name = Slot(uri=NMDC.rna_seq_project_name, name="rna_seq_project_name", curie=NMDC.curie('rna_seq_project_name'),
                   model_uri=NMDC.rna_seq_project_name, domain=None, range=Optional[str])

slots.rna_volume = Slot(uri=NMDC.rna_volume, name="rna_volume", curie=NMDC.curie('rna_volume'),
                   model_uri=NMDC.rna_volume, domain=None, range=Optional[str])
