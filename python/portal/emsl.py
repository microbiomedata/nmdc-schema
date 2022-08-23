# Auto generated from emsl.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-08-23T09:40:40
# Schema: emsl
#
# id: https://microbiomedata/schema/emsl
# description: This file defines terms that appear in the 'EMSL' section of the NMDC sample metadata submission
#              portal, which is implemented with DataHarmonizer as of Spring 2022
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
NMDC = CurieNamespace('nmdc', 'https://microbiomedata/meta/')
DEFAULT_ = NMDC


# Types

# Class references




# Enumerations
class SampleTypeEnum(EnumDefinitionImpl):

    soil = PermissibleValue(text="soil")
    water_extract_soil = PermissibleValue(text="water_extract_soil")

    _defn = EnumDefinition(
        name="SampleTypeEnum",
    )

# Slots
class slots:
    pass

slots.EMSL_store_temp = Slot(uri=NMDC.EMSL_store_temp, name="EMSL_store_temp", curie=NMDC.curie('EMSL_store_temp'),
                   model_uri=NMDC.EMSL_store_temp, domain=None, range=Optional[str])

slots.project_ID = Slot(uri=NMDC.project_ID, name="project_ID", curie=NMDC.curie('project_ID'),
                   model_uri=NMDC.project_ID, domain=None, range=Optional[str])

slots.replicate_number = Slot(uri=NMDC.replicate_number, name="replicate_number", curie=NMDC.curie('replicate_number'),
                   model_uri=NMDC.replicate_number, domain=None, range=Optional[str])

slots.sample_shipped = Slot(uri=NMDC.sample_shipped, name="sample_shipped", curie=NMDC.curie('sample_shipped'),
                   model_uri=NMDC.sample_shipped, domain=None, range=Optional[str])

slots.sample_type = Slot(uri=NMDC.sample_type, name="sample_type", curie=NMDC.curie('sample_type'),
                   model_uri=NMDC.sample_type, domain=None, range=Optional[Union[str, "SampleTypeEnum"]])

slots.technical_reps = Slot(uri=NMDC.technical_reps, name="technical_reps", curie=NMDC.curie('technical_reps'),
                   model_uri=NMDC.technical_reps, domain=None, range=Optional[str])
