# Auto generated from sample_id.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-10-03T14:44:44
# Schema: sample_id
#
# id: https://microbiomedata/schema/sample_id
# description: This file defines terms that appear in the 'Sample ID' section of the NMDC sample metadata
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
class AnalysisTypeEnum(EnumDefinitionImpl):

    metabolomics = PermissibleValue(text="metabolomics")
    metagenomics = PermissibleValue(text="metagenomics")
    metaproteomics = PermissibleValue(text="metaproteomics")
    metatranscriptomics = PermissibleValue(text="metatranscriptomics")

    _defn = EnumDefinition(
        name="AnalysisTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "natural organic matter",
                PermissibleValue(text="natural organic matter") )

# Slots
class slots:
    pass

slots.analysis_type = Slot(uri=NMDC.analysis_type, name="analysis_type", curie=NMDC.curie('analysis_type'),
                   model_uri=NMDC.analysis_type, domain=None, range=Optional[Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]]])

slots.sample_link = Slot(uri=NMDC.sample_link, name="sample_link", curie=NMDC.curie('sample_link'),
                   model_uri=NMDC.sample_link, domain=None, range=Optional[Union[str, List[str]]])
