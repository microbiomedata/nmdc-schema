# Auto generated from mixs_inspired.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-12-14T14:54:23
# Schema: mixs_inspired
#
# id: https://microbiomedata/schema/mixs_inspired
# description: This file defines terms that appear in the 'MIxS Inspired' section of the NMDC sample metadata
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


# Slots
class slots:
    pass

slots.collection_date_inc = Slot(uri=NMDC.collection_date_inc, name="collection_date_inc", curie=NMDC.curie('collection_date_inc'),
                   model_uri=NMDC.collection_date_inc, domain=None, range=Optional[str])

slots.collection_time = Slot(uri=NMDC.collection_time, name="collection_time", curie=NMDC.curie('collection_time'),
                   model_uri=NMDC.collection_time, domain=None, range=Optional[str])

slots.collection_time_inc = Slot(uri=NMDC.collection_time_inc, name="collection_time_inc", curie=NMDC.curie('collection_time_inc'),
                   model_uri=NMDC.collection_time_inc, domain=None, range=Optional[str])

slots.experimental_factor_other = Slot(uri=NMDC.experimental_factor_other, name="experimental_factor_other", curie=NMDC.curie('experimental_factor_other'),
                   model_uri=NMDC.experimental_factor_other, domain=None, range=Optional[str])

slots.filter_method = Slot(uri=NMDC.filter_method, name="filter_method", curie=NMDC.curie('filter_method'),
                   model_uri=NMDC.filter_method, domain=None, range=Optional[str])

slots.isotope_exposure = Slot(uri=NMDC.isotope_exposure, name="isotope_exposure", curie=NMDC.curie('isotope_exposure'),
                   model_uri=NMDC.isotope_exposure, domain=None, range=Optional[str])

slots.micro_biomass_c_meth = Slot(uri=NMDC.micro_biomass_c_meth, name="micro_biomass_c_meth", curie=NMDC.curie('micro_biomass_c_meth'),
                   model_uri=NMDC.micro_biomass_c_meth, domain=None, range=Optional[str])

slots.micro_biomass_n_meth = Slot(uri=NMDC.micro_biomass_n_meth, name="micro_biomass_n_meth", curie=NMDC.curie('micro_biomass_n_meth'),
                   model_uri=NMDC.micro_biomass_n_meth, domain=None, range=Optional[str])

slots.microbial_biomass_c = Slot(uri=NMDC.microbial_biomass_c, name="microbial_biomass_c", curie=NMDC.curie('microbial_biomass_c'),
                   model_uri=NMDC.microbial_biomass_c, domain=None, range=Optional[str])

slots.microbial_biomass_n = Slot(uri=NMDC.microbial_biomass_n, name="microbial_biomass_n", curie=NMDC.curie('microbial_biomass_n'),
                   model_uri=NMDC.microbial_biomass_n, domain=None, range=Optional[str])

slots.non_microb_biomass = Slot(uri=NMDC.non_microb_biomass, name="non_microb_biomass", curie=NMDC.curie('non_microb_biomass'),
                   model_uri=NMDC.non_microb_biomass, domain=None, range=Optional[str])

slots.non_microb_biomass_method = Slot(uri=NMDC.non_microb_biomass_method, name="non_microb_biomass_method", curie=NMDC.curie('non_microb_biomass_method'),
                   model_uri=NMDC.non_microb_biomass_method, domain=None, range=Optional[str])

slots.org_nitro_method = Slot(uri=NMDC.org_nitro_method, name="org_nitro_method", curie=NMDC.curie('org_nitro_method'),
                   model_uri=NMDC.org_nitro_method, domain=None, range=Optional[str])

slots.other_treatment = Slot(uri=NMDC.other_treatment, name="other_treatment", curie=NMDC.curie('other_treatment'),
                   model_uri=NMDC.other_treatment, domain=None, range=Optional[str])

slots.start_date_inc = Slot(uri=NMDC.start_date_inc, name="start_date_inc", curie=NMDC.curie('start_date_inc'),
                   model_uri=NMDC.start_date_inc, domain=None, range=Optional[str])

slots.start_time_inc = Slot(uri=NMDC.start_time_inc, name="start_time_inc", curie=NMDC.curie('start_time_inc'),
                   model_uri=NMDC.start_time_inc, domain=None, range=Optional[str])
