# Auto generated from nmdc.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-04-08 16:56
# Schema: NMDC
#
# id: https://microbiomedata/schema
# description: Schema for National Microbiome Data Collaborative (NMDC). This schem is organized into 3 separate
#              modules: This schema is organized into distinct modules: * a set of core types for representing
#              data values * the mixs schema (auto-translated from mixs excel) * annotation schema * the NMDC
#              schema itself
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml.utils.slot import Slot
from linkml.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml.utils.formatutils import camelcase, underscore, sfx
from linkml.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml.utils.curienamespace import CurieNamespace
from . annotation import FunctionalAnnotation, GenomeFeature, ReactionId, ReactionParticipant
from . core import AttributeValue, Bytes, ChemicalEntityId, ControlledTermValue, GeneProductId, GeolocationValue, MetaboliteQuantification, NamedThing, NamedThingId, PeptideQuantification, PersonValue, QuantityValue, TextValue, TimestampValue
from . prov import ActivityId
from . workflow_execution_activity import MAGsAnalysisActivity, MAGsAnalysisActivityId, MetabolomicsAnalysisActivity, MetabolomicsAnalysisActivityId, MetagenomeAnnotationActivity, MetagenomeAnnotationActivityId, MetagenomeAssembly, MetagenomeAssemblyId, MetaproteomicsAnalysisActivity, MetaproteomicsAnalysisActivityId, NomAnalysisActivity, NomAnalysisActivityId, ReadBasedAnalysisActivity, ReadBasedAnalysisActivityId, ReadQCAnalysisActivity, ReadQCAnalysisActivityId, WorkflowExecutionActivity, WorkflowExecutionActivityId
from linkml.utils.metamodelcore import Bool
from linkml_model.types import Boolean, Float, Integer, String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
GOLD = CurieNamespace('GOLD', 'https://identifiers.org/gold/')
MS = CurieNamespace('MS', 'http://purl.obolibrary.org/obo/MS_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
IGSN = CurieNamespace('igsn', 'https://app.geosamples.org/sample/igsn/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MIXS = CurieNamespace('mixs', 'https://w3id.org/gensc/')
NMDC = CurieNamespace('nmdc', 'https://microbiomedata/meta/')
QUD = CurieNamespace('qud', 'http://qudt.org/1.1/schema/qudt#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://example.org/UNKNOWN/rdfs/')
SKOS = CurieNamespace('skos', 'http://example.org/UNKNOWN/skos/')
WGS = CurieNamespace('wgs', 'http://www.w3.org/2003/01/geo/wgs84_pos')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = NMDC


# Types

# Class references
class DataObjectId(NamedThingId):
    pass


class BiosampleId(NamedThingId):
    pass


class StudyId(NamedThingId):
    pass


class BiosampleProcessingId(NamedThingId):
    pass


class OmicsProcessingId(BiosampleProcessingId):
    pass


@dataclass
class Database(YAMLRoot):
    """
    An abstract holder for any set of metadata and data. It does not need to correspond to an actual managed databse
    top level holder class. When translated to JSON-Schema this is the 'root' object. It should contain pointers to
    other objects of interest
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.Database
    class_class_curie: ClassVar[str] = "nmdc:Database"
    class_name: ClassVar[str] = "database"
    class_model_uri: ClassVar[URIRef] = NMDC.Database

    biosample_set: Optional[Union[Dict[Union[str, BiosampleId], Union[dict, "Biosample"]], List[Union[dict, "Biosample"]]]] = empty_dict()
    study_set: Optional[Union[Dict[Union[str, StudyId], Union[dict, "Study"]], List[Union[dict, "Study"]]]] = empty_dict()
    data_object_set: Optional[Union[Dict[Union[str, DataObjectId], Union[dict, "DataObject"]], List[Union[dict, "DataObject"]]]] = empty_dict()
    activity_set: Optional[Union[Dict[Union[str, WorkflowExecutionActivityId], Union[dict, WorkflowExecutionActivity]], List[Union[dict, WorkflowExecutionActivity]]]] = empty_dict()
    mags_activity_set: Optional[Union[Dict[Union[str, MAGsAnalysisActivityId], Union[dict, MAGsAnalysisActivity]], List[Union[dict, MAGsAnalysisActivity]]]] = empty_dict()
    metabolomics_analysis_activity_set: Optional[Union[Dict[Union[str, MetabolomicsAnalysisActivityId], Union[dict, MetabolomicsAnalysisActivity]], List[Union[dict, MetabolomicsAnalysisActivity]]]] = empty_dict()
    metaproteomics_analysis_activity_set: Optional[Union[Dict[Union[str, MetaproteomicsAnalysisActivityId], Union[dict, MetaproteomicsAnalysisActivity]], List[Union[dict, MetaproteomicsAnalysisActivity]]]] = empty_dict()
    metagenome_annotation_activity_set: Optional[Union[Dict[Union[str, MetagenomeAnnotationActivityId], Union[dict, MetagenomeAnnotationActivity]], List[Union[dict, MetagenomeAnnotationActivity]]]] = empty_dict()
    metagenome_assembly_set: Optional[Union[Dict[Union[str, MetagenomeAssemblyId], Union[dict, MetagenomeAssembly]], List[Union[dict, MetagenomeAssembly]]]] = empty_dict()
    read_QC_analysis_activity_set: Optional[Union[Dict[Union[str, ReadQCAnalysisActivityId], Union[dict, ReadQCAnalysisActivity]], List[Union[dict, ReadQCAnalysisActivity]]]] = empty_dict()
    read_based_analysis_activity_set: Optional[Union[Dict[Union[str, ReadBasedAnalysisActivityId], Union[dict, ReadBasedAnalysisActivity]], List[Union[dict, ReadBasedAnalysisActivity]]]] = empty_dict()
    nom_analysis_activity_set: Optional[Union[Dict[Union[str, NomAnalysisActivityId], Union[dict, NomAnalysisActivity]], List[Union[dict, NomAnalysisActivity]]]] = empty_dict()
    omics_processing_set: Optional[Union[Dict[Union[str, OmicsProcessingId], Union[dict, "OmicsProcessing"]], List[Union[dict, "OmicsProcessing"]]]] = empty_dict()
    functional_annotation_set: Optional[Union[Union[dict, FunctionalAnnotation], List[Union[dict, FunctionalAnnotation]]]] = empty_list()
    genome_feature_set: Optional[Union[Union[dict, GenomeFeature], List[Union[dict, GenomeFeature]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.biosample_set is None:
            self.biosample_set = []
        if not isinstance(self.biosample_set, (list, dict)):
            self.biosample_set = [self.biosample_set]
        self._normalize_inlined_slot(slot_name="biosample_set", slot_type=Biosample, key_name="id", inlined_as_list=None, keyed=True)

        if self.study_set is None:
            self.study_set = []
        if not isinstance(self.study_set, (list, dict)):
            self.study_set = [self.study_set]
        self._normalize_inlined_slot(slot_name="study_set", slot_type=Study, key_name="id", inlined_as_list=None, keyed=True)

        if self.data_object_set is None:
            self.data_object_set = []
        if not isinstance(self.data_object_set, (list, dict)):
            self.data_object_set = [self.data_object_set]
        self._normalize_inlined_slot(slot_name="data_object_set", slot_type=DataObject, key_name="id", inlined_as_list=None, keyed=True)

        if self.activity_set is None:
            self.activity_set = []
        if not isinstance(self.activity_set, (list, dict)):
            self.activity_set = [self.activity_set]
        self._normalize_inlined_slot(slot_name="activity_set", slot_type=WorkflowExecutionActivity, key_name="id", inlined_as_list=None, keyed=True)

        if self.mags_activity_set is None:
            self.mags_activity_set = []
        if not isinstance(self.mags_activity_set, (list, dict)):
            self.mags_activity_set = [self.mags_activity_set]
        self._normalize_inlined_slot(slot_name="mags_activity_set", slot_type=MAGsAnalysisActivity, key_name="id", inlined_as_list=None, keyed=True)

        if self.metabolomics_analysis_activity_set is None:
            self.metabolomics_analysis_activity_set = []
        if not isinstance(self.metabolomics_analysis_activity_set, (list, dict)):
            self.metabolomics_analysis_activity_set = [self.metabolomics_analysis_activity_set]
        self._normalize_inlined_slot(slot_name="metabolomics_analysis_activity_set", slot_type=MetabolomicsAnalysisActivity, key_name="id", inlined_as_list=None, keyed=True)

        if self.metaproteomics_analysis_activity_set is None:
            self.metaproteomics_analysis_activity_set = []
        if not isinstance(self.metaproteomics_analysis_activity_set, (list, dict)):
            self.metaproteomics_analysis_activity_set = [self.metaproteomics_analysis_activity_set]
        self._normalize_inlined_slot(slot_name="metaproteomics_analysis_activity_set", slot_type=MetaproteomicsAnalysisActivity, key_name="id", inlined_as_list=None, keyed=True)

        if self.metagenome_annotation_activity_set is None:
            self.metagenome_annotation_activity_set = []
        if not isinstance(self.metagenome_annotation_activity_set, (list, dict)):
            self.metagenome_annotation_activity_set = [self.metagenome_annotation_activity_set]
        self._normalize_inlined_slot(slot_name="metagenome_annotation_activity_set", slot_type=MetagenomeAnnotationActivity, key_name="id", inlined_as_list=None, keyed=True)

        if self.metagenome_assembly_set is None:
            self.metagenome_assembly_set = []
        if not isinstance(self.metagenome_assembly_set, (list, dict)):
            self.metagenome_assembly_set = [self.metagenome_assembly_set]
        self._normalize_inlined_slot(slot_name="metagenome_assembly_set", slot_type=MetagenomeAssembly, key_name="id", inlined_as_list=None, keyed=True)

        if self.read_QC_analysis_activity_set is None:
            self.read_QC_analysis_activity_set = []
        if not isinstance(self.read_QC_analysis_activity_set, (list, dict)):
            self.read_QC_analysis_activity_set = [self.read_QC_analysis_activity_set]
        self._normalize_inlined_slot(slot_name="read_QC_analysis_activity_set", slot_type=ReadQCAnalysisActivity, key_name="id", inlined_as_list=None, keyed=True)

        if self.read_based_analysis_activity_set is None:
            self.read_based_analysis_activity_set = []
        if not isinstance(self.read_based_analysis_activity_set, (list, dict)):
            self.read_based_analysis_activity_set = [self.read_based_analysis_activity_set]
        self._normalize_inlined_slot(slot_name="read_based_analysis_activity_set", slot_type=ReadBasedAnalysisActivity, key_name="id", inlined_as_list=None, keyed=True)

        if self.nom_analysis_activity_set is None:
            self.nom_analysis_activity_set = []
        if not isinstance(self.nom_analysis_activity_set, (list, dict)):
            self.nom_analysis_activity_set = [self.nom_analysis_activity_set]
        self._normalize_inlined_slot(slot_name="nom_analysis_activity_set", slot_type=NomAnalysisActivity, key_name="id", inlined_as_list=None, keyed=True)

        if self.omics_processing_set is None:
            self.omics_processing_set = []
        if not isinstance(self.omics_processing_set, (list, dict)):
            self.omics_processing_set = [self.omics_processing_set]
        self._normalize_inlined_slot(slot_name="omics_processing_set", slot_type=OmicsProcessing, key_name="id", inlined_as_list=None, keyed=True)

        if self.functional_annotation_set is None:
            self.functional_annotation_set = []
        if not isinstance(self.functional_annotation_set, list):
            self.functional_annotation_set = [self.functional_annotation_set]
        self.functional_annotation_set = [v if isinstance(v, FunctionalAnnotation) else FunctionalAnnotation(**v) for v in self.functional_annotation_set]

        if self.genome_feature_set is None:
            self.genome_feature_set = []
        if not isinstance(self.genome_feature_set, list):
            self.genome_feature_set = [self.genome_feature_set]
        self._normalize_inlined_slot(slot_name="genome_feature_set", slot_type=GenomeFeature, key_name="seqid", inlined_as_list=True, keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class DataObject(NamedThing):
    """
    An object that primarily consists of symbols that represent information. Files, records, and omics data are
    examples of data objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.DataObject
    class_class_curie: ClassVar[str] = "nmdc:DataObject"
    class_name: ClassVar[str] = "data object"
    class_model_uri: ClassVar[URIRef] = NMDC.DataObject

    id: Union[str, DataObjectId] = None
    file_size_bytes: Optional[int] = None
    md5_checksum: Optional[str] = None
    data_object_type: Optional[Union[dict, ControlledTermValue]] = None
    compression_type: Optional[str] = None
    was_generated_by: Optional[Union[str, ActivityId]] = None
    url: Optional[str] = None
    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DataObjectId):
            self.id = DataObjectId(self.id)

        if self.file_size_bytes is not None and not isinstance(self.file_size_bytes, int):
            self.file_size_bytes = int(self.file_size_bytes)

        if self.md5_checksum is not None and not isinstance(self.md5_checksum, str):
            self.md5_checksum = str(self.md5_checksum)

        if self.data_object_type is not None and not isinstance(self.data_object_type, ControlledTermValue):
            self.data_object_type = ControlledTermValue(**self.data_object_type)

        if self.compression_type is not None and not isinstance(self.compression_type, str):
            self.compression_type = str(self.compression_type)

        if self.was_generated_by is not None and not isinstance(self.was_generated_by, ActivityId):
            self.was_generated_by = ActivityId(self.was_generated_by)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass
class Biosample(NamedThing):
    """
    A material sample. It may be environmental (encompassing many organisms) or isolate or tissue. An environmental
    sample containing genetic material from multiple individuals is commonly referred to as a biosample.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.Biosample
    class_class_curie: ClassVar[str] = "nmdc:Biosample"
    class_name: ClassVar[str] = "biosample"
    class_model_uri: ClassVar[URIRef] = NMDC.Biosample

    id: Union[str, BiosampleId] = None
    type: Optional[str] = None
    agrochem_addition: Optional[Union[dict, QuantityValue]] = None
    alkalinity: Optional[Union[dict, QuantityValue]] = None
    alkalinity_method: Optional[Union[dict, TextValue]] = None
    alkyl_diethers: Optional[Union[dict, QuantityValue]] = None
    alt: Optional[Union[dict, QuantityValue]] = None
    al_sat: Optional[Union[dict, QuantityValue]] = None
    al_sat_meth: Optional[Union[dict, TextValue]] = None
    aminopept_act: Optional[Union[dict, QuantityValue]] = None
    ammonium: Optional[Union[dict, QuantityValue]] = None
    annual_precpt: Optional[Union[dict, QuantityValue]] = None
    annual_temp: Optional[Union[dict, QuantityValue]] = None
    bacteria_carb_prod: Optional[Union[dict, QuantityValue]] = None
    bishomohopanol: Optional[Union[dict, QuantityValue]] = None
    bromide: Optional[Union[dict, QuantityValue]] = None
    calcium: Optional[Union[dict, QuantityValue]] = None
    carb_nitro_ratio: Optional[Union[dict, QuantityValue]] = None
    chem_administration: Optional[Union[dict, ControlledTermValue]] = None
    chloride: Optional[Union[dict, QuantityValue]] = None
    chlorophyll: Optional[Union[dict, QuantityValue]] = None
    collection_date: Optional[Union[dict, TimestampValue]] = None
    cur_land_use: Optional[Union[dict, TextValue]] = None
    cur_vegetation: Optional[Union[dict, TextValue]] = None
    cur_vegetation_meth: Optional[Union[dict, TextValue]] = None
    crop_rotation: Optional[Union[dict, TextValue]] = None
    density: Optional[Union[dict, QuantityValue]] = None
    depth: Optional[Union[dict, QuantityValue]] = None
    diss_carb_dioxide: Optional[Union[dict, QuantityValue]] = None
    diss_hydrogen: Optional[Union[dict, QuantityValue]] = None
    diss_inorg_carb: Optional[Union[dict, QuantityValue]] = None
    diss_inorg_phosp: Optional[Union[dict, QuantityValue]] = None
    diss_org_carb: Optional[Union[dict, QuantityValue]] = None
    diss_org_nitro: Optional[Union[dict, QuantityValue]] = None
    diss_oxygen: Optional[Union[dict, QuantityValue]] = None
    drainage_class: Optional[Union[dict, TextValue]] = None
    elev: Optional[Union[dict, QuantityValue]] = None
    env_package: Optional[Union[dict, TextValue]] = None
    env_broad_scale: Optional[Union[dict, ControlledTermValue]] = None
    env_local_scale: Optional[Union[dict, ControlledTermValue]] = None
    env_medium: Optional[Union[dict, ControlledTermValue]] = None
    extreme_event: Optional[Union[dict, TimestampValue]] = None
    fao_class: Optional[Union[dict, TextValue]] = None
    fire: Optional[Union[dict, TimestampValue]] = None
    flooding: Optional[Union[dict, TimestampValue]] = None
    geo_loc_name: Optional[Union[dict, TextValue]] = None
    glucosidase_act: Optional[Union[dict, QuantityValue]] = None
    heavy_metals: Optional[Union[dict, QuantityValue]] = None
    heavy_metals_meth: Optional[Union[dict, TextValue]] = None
    horizon: Optional[Union[dict, TextValue]] = None
    horizon_meth: Optional[Union[dict, TextValue]] = None
    lat_lon: Optional[Union[dict, GeolocationValue]] = None
    link_addit_analys: Optional[Union[dict, TextValue]] = None
    link_class_info: Optional[Union[dict, TextValue]] = None
    link_climate_info: Optional[Union[dict, TextValue]] = None
    local_class: Optional[Union[dict, TextValue]] = None
    local_class_meth: Optional[Union[dict, TextValue]] = None
    magnesium: Optional[Union[dict, QuantityValue]] = None
    mean_frict_vel: Optional[Union[dict, QuantityValue]] = None
    mean_peak_frict_vel: Optional[Union[dict, QuantityValue]] = None
    microbial_biomass: Optional[Union[dict, QuantityValue]] = None
    microbial_biomass_meth: Optional[Union[dict, TextValue]] = None
    misc_param: Optional[Union[dict, QuantityValue]] = None
    n_alkanes: Optional[Union[dict, QuantityValue]] = None
    nitrate: Optional[Union[dict, QuantityValue]] = None
    nitrite: Optional[Union[dict, QuantityValue]] = None
    org_matter: Optional[Union[dict, QuantityValue]] = None
    org_nitro: Optional[Union[dict, QuantityValue]] = None
    organism_count: Optional[Union[dict, QuantityValue]] = None
    oxy_stat_samp: Optional[Union[dict, TextValue]] = None
    part_org_carb: Optional[Union[dict, QuantityValue]] = None
    perturbation: Optional[Union[dict, TextValue]] = None
    petroleum_hydrocarb: Optional[Union[dict, QuantityValue]] = None
    ph: Optional[Union[dict, QuantityValue]] = None
    ph_meth: Optional[Union[dict, TextValue]] = None
    phaeopigments: Optional[Union[dict, QuantityValue]] = None
    phosplipid_fatt_acid: Optional[Union[dict, QuantityValue]] = None
    pool_dna_extracts: Optional[Union[dict, TextValue]] = None
    potassium: Optional[Union[dict, QuantityValue]] = None
    pressure: Optional[Union[dict, QuantityValue]] = None
    previous_land_use: Optional[Union[dict, TextValue]] = None
    previous_land_use_meth: Optional[Union[dict, TextValue]] = None
    profile_position: Optional[Union[dict, TextValue]] = None
    redox_potential: Optional[Union[dict, QuantityValue]] = None
    salinity: Optional[Union[dict, QuantityValue]] = None
    salinity_meth: Optional[Union[dict, TextValue]] = None
    samp_collect_device: Optional[Union[dict, TextValue]] = None
    samp_store_dur: Optional[Union[dict, TextValue]] = None
    samp_store_loc: Optional[Union[dict, TextValue]] = None
    samp_store_temp: Optional[Union[dict, QuantityValue]] = None
    samp_vol_we_dna_ext: Optional[Union[dict, QuantityValue]] = None
    season_temp: Optional[Union[dict, QuantityValue]] = None
    season_precpt: Optional[Union[dict, QuantityValue]] = None
    sieving: Optional[Union[dict, QuantityValue]] = None
    size_frac_low: Optional[Union[dict, QuantityValue]] = None
    size_frac_up: Optional[Union[dict, QuantityValue]] = None
    slope_gradient: Optional[Union[dict, QuantityValue]] = None
    slope_aspect: Optional[Union[dict, QuantityValue]] = None
    sodium: Optional[Union[dict, QuantityValue]] = None
    soil_type: Optional[Union[dict, TextValue]] = None
    soil_type_meth: Optional[Union[dict, TextValue]] = None
    store_cond: Optional[Union[dict, TextValue]] = None
    sulfate: Optional[Union[dict, QuantityValue]] = None
    sulfide: Optional[Union[dict, QuantityValue]] = None
    temp: Optional[Union[dict, QuantityValue]] = None
    texture: Optional[Union[dict, QuantityValue]] = None
    texture_meth: Optional[Union[dict, TextValue]] = None
    tillage: Optional[Union[dict, TextValue]] = None
    tidal_stage: Optional[Union[dict, TextValue]] = None
    tot_carb: Optional[Union[dict, QuantityValue]] = None
    tot_depth_water_col: Optional[Union[dict, QuantityValue]] = None
    tot_diss_nitro: Optional[Union[dict, QuantityValue]] = None
    tot_org_carb: Optional[Union[dict, QuantityValue]] = None
    tot_org_c_meth: Optional[Union[dict, TextValue]] = None
    tot_nitro_content: Optional[Union[dict, QuantityValue]] = None
    tot_nitro_content_meth: Optional[Union[dict, TextValue]] = None
    tot_phosp: Optional[Union[dict, QuantityValue]] = None
    water_content: Optional[Union[dict, QuantityValue]] = None
    water_content_soil_meth: Optional[Union[dict, TextValue]] = None
    ecosystem: Optional[str] = None
    ecosystem_category: Optional[str] = None
    ecosystem_type: Optional[str] = None
    ecosystem_subtype: Optional[str] = None
    specific_ecosystem: Optional[str] = None
    add_date: Optional[str] = None
    community: Optional[str] = None
    habitat: Optional[str] = None
    host_name: Optional[str] = None
    identifier: Optional[str] = None
    location: Optional[str] = None
    mod_date: Optional[str] = None
    ncbi_taxonomy_name: Optional[str] = None
    proport_woa_temperature: Optional[str] = None
    salinity_category: Optional[str] = None
    sample_collection_site: Optional[str] = None
    soluble_iron_micromol: Optional[str] = None
    subsurface_depth: Optional[Union[dict, QuantityValue]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BiosampleId):
            self.id = BiosampleId(self.id)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.agrochem_addition is not None and not isinstance(self.agrochem_addition, QuantityValue):
            self.agrochem_addition = QuantityValue(**self.agrochem_addition)

        if self.alkalinity is not None and not isinstance(self.alkalinity, QuantityValue):
            self.alkalinity = QuantityValue(**self.alkalinity)

        if self.alkalinity_method is not None and not isinstance(self.alkalinity_method, TextValue):
            self.alkalinity_method = TextValue(**self.alkalinity_method)

        if self.alkyl_diethers is not None and not isinstance(self.alkyl_diethers, QuantityValue):
            self.alkyl_diethers = QuantityValue(**self.alkyl_diethers)

        if self.alt is not None and not isinstance(self.alt, QuantityValue):
            self.alt = QuantityValue(**self.alt)

        if self.al_sat is not None and not isinstance(self.al_sat, QuantityValue):
            self.al_sat = QuantityValue(**self.al_sat)

        if self.al_sat_meth is not None and not isinstance(self.al_sat_meth, TextValue):
            self.al_sat_meth = TextValue(**self.al_sat_meth)

        if self.aminopept_act is not None and not isinstance(self.aminopept_act, QuantityValue):
            self.aminopept_act = QuantityValue(**self.aminopept_act)

        if self.ammonium is not None and not isinstance(self.ammonium, QuantityValue):
            self.ammonium = QuantityValue(**self.ammonium)

        if self.annual_precpt is not None and not isinstance(self.annual_precpt, QuantityValue):
            self.annual_precpt = QuantityValue(**self.annual_precpt)

        if self.annual_temp is not None and not isinstance(self.annual_temp, QuantityValue):
            self.annual_temp = QuantityValue(**self.annual_temp)

        if self.bacteria_carb_prod is not None and not isinstance(self.bacteria_carb_prod, QuantityValue):
            self.bacteria_carb_prod = QuantityValue(**self.bacteria_carb_prod)

        if self.bishomohopanol is not None and not isinstance(self.bishomohopanol, QuantityValue):
            self.bishomohopanol = QuantityValue(**self.bishomohopanol)

        if self.bromide is not None and not isinstance(self.bromide, QuantityValue):
            self.bromide = QuantityValue(**self.bromide)

        if self.calcium is not None and not isinstance(self.calcium, QuantityValue):
            self.calcium = QuantityValue(**self.calcium)

        if self.carb_nitro_ratio is not None and not isinstance(self.carb_nitro_ratio, QuantityValue):
            self.carb_nitro_ratio = QuantityValue(**self.carb_nitro_ratio)

        if self.chem_administration is not None and not isinstance(self.chem_administration, ControlledTermValue):
            self.chem_administration = ControlledTermValue(**self.chem_administration)

        if self.chloride is not None and not isinstance(self.chloride, QuantityValue):
            self.chloride = QuantityValue(**self.chloride)

        if self.chlorophyll is not None and not isinstance(self.chlorophyll, QuantityValue):
            self.chlorophyll = QuantityValue(**self.chlorophyll)

        if self.collection_date is not None and not isinstance(self.collection_date, TimestampValue):
            self.collection_date = TimestampValue(**self.collection_date)

        if self.cur_land_use is not None and not isinstance(self.cur_land_use, TextValue):
            self.cur_land_use = TextValue(**self.cur_land_use)

        if self.cur_vegetation is not None and not isinstance(self.cur_vegetation, TextValue):
            self.cur_vegetation = TextValue(**self.cur_vegetation)

        if self.cur_vegetation_meth is not None and not isinstance(self.cur_vegetation_meth, TextValue):
            self.cur_vegetation_meth = TextValue(**self.cur_vegetation_meth)

        if self.crop_rotation is not None and not isinstance(self.crop_rotation, TextValue):
            self.crop_rotation = TextValue(**self.crop_rotation)

        if self.density is not None and not isinstance(self.density, QuantityValue):
            self.density = QuantityValue(**self.density)

        if self.depth is not None and not isinstance(self.depth, QuantityValue):
            self.depth = QuantityValue(**self.depth)

        if self.diss_carb_dioxide is not None and not isinstance(self.diss_carb_dioxide, QuantityValue):
            self.diss_carb_dioxide = QuantityValue(**self.diss_carb_dioxide)

        if self.diss_hydrogen is not None and not isinstance(self.diss_hydrogen, QuantityValue):
            self.diss_hydrogen = QuantityValue(**self.diss_hydrogen)

        if self.diss_inorg_carb is not None and not isinstance(self.diss_inorg_carb, QuantityValue):
            self.diss_inorg_carb = QuantityValue(**self.diss_inorg_carb)

        if self.diss_inorg_phosp is not None and not isinstance(self.diss_inorg_phosp, QuantityValue):
            self.diss_inorg_phosp = QuantityValue(**self.diss_inorg_phosp)

        if self.diss_org_carb is not None and not isinstance(self.diss_org_carb, QuantityValue):
            self.diss_org_carb = QuantityValue(**self.diss_org_carb)

        if self.diss_org_nitro is not None and not isinstance(self.diss_org_nitro, QuantityValue):
            self.diss_org_nitro = QuantityValue(**self.diss_org_nitro)

        if self.diss_oxygen is not None and not isinstance(self.diss_oxygen, QuantityValue):
            self.diss_oxygen = QuantityValue(**self.diss_oxygen)

        if self.drainage_class is not None and not isinstance(self.drainage_class, TextValue):
            self.drainage_class = TextValue(**self.drainage_class)

        if self.elev is not None and not isinstance(self.elev, QuantityValue):
            self.elev = QuantityValue(**self.elev)

        if self.env_package is not None and not isinstance(self.env_package, TextValue):
            self.env_package = TextValue(**self.env_package)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, ControlledTermValue):
            self.env_broad_scale = ControlledTermValue(**self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, ControlledTermValue):
            self.env_local_scale = ControlledTermValue(**self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, ControlledTermValue):
            self.env_medium = ControlledTermValue(**self.env_medium)

        if self.extreme_event is not None and not isinstance(self.extreme_event, TimestampValue):
            self.extreme_event = TimestampValue(**self.extreme_event)

        if self.fao_class is not None and not isinstance(self.fao_class, TextValue):
            self.fao_class = TextValue(**self.fao_class)

        if self.fire is not None and not isinstance(self.fire, TimestampValue):
            self.fire = TimestampValue(**self.fire)

        if self.flooding is not None and not isinstance(self.flooding, TimestampValue):
            self.flooding = TimestampValue(**self.flooding)

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, TextValue):
            self.geo_loc_name = TextValue(**self.geo_loc_name)

        if self.glucosidase_act is not None and not isinstance(self.glucosidase_act, QuantityValue):
            self.glucosidase_act = QuantityValue(**self.glucosidase_act)

        if self.heavy_metals is not None and not isinstance(self.heavy_metals, QuantityValue):
            self.heavy_metals = QuantityValue(**self.heavy_metals)

        if self.heavy_metals_meth is not None and not isinstance(self.heavy_metals_meth, TextValue):
            self.heavy_metals_meth = TextValue(**self.heavy_metals_meth)

        if self.horizon is not None and not isinstance(self.horizon, TextValue):
            self.horizon = TextValue(**self.horizon)

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, TextValue):
            self.horizon_meth = TextValue(**self.horizon_meth)

        if self.lat_lon is not None and not isinstance(self.lat_lon, GeolocationValue):
            self.lat_lon = GeolocationValue(**self.lat_lon)

        if self.link_addit_analys is not None and not isinstance(self.link_addit_analys, TextValue):
            self.link_addit_analys = TextValue(**self.link_addit_analys)

        if self.link_class_info is not None and not isinstance(self.link_class_info, TextValue):
            self.link_class_info = TextValue(**self.link_class_info)

        if self.link_climate_info is not None and not isinstance(self.link_climate_info, TextValue):
            self.link_climate_info = TextValue(**self.link_climate_info)

        if self.local_class is not None and not isinstance(self.local_class, TextValue):
            self.local_class = TextValue(**self.local_class)

        if self.local_class_meth is not None and not isinstance(self.local_class_meth, TextValue):
            self.local_class_meth = TextValue(**self.local_class_meth)

        if self.magnesium is not None and not isinstance(self.magnesium, QuantityValue):
            self.magnesium = QuantityValue(**self.magnesium)

        if self.mean_frict_vel is not None and not isinstance(self.mean_frict_vel, QuantityValue):
            self.mean_frict_vel = QuantityValue(**self.mean_frict_vel)

        if self.mean_peak_frict_vel is not None and not isinstance(self.mean_peak_frict_vel, QuantityValue):
            self.mean_peak_frict_vel = QuantityValue(**self.mean_peak_frict_vel)

        if self.microbial_biomass is not None and not isinstance(self.microbial_biomass, QuantityValue):
            self.microbial_biomass = QuantityValue(**self.microbial_biomass)

        if self.microbial_biomass_meth is not None and not isinstance(self.microbial_biomass_meth, TextValue):
            self.microbial_biomass_meth = TextValue(**self.microbial_biomass_meth)

        if self.misc_param is not None and not isinstance(self.misc_param, QuantityValue):
            self.misc_param = QuantityValue(**self.misc_param)

        if self.n_alkanes is not None and not isinstance(self.n_alkanes, QuantityValue):
            self.n_alkanes = QuantityValue(**self.n_alkanes)

        if self.nitrate is not None and not isinstance(self.nitrate, QuantityValue):
            self.nitrate = QuantityValue(**self.nitrate)

        if self.nitrite is not None and not isinstance(self.nitrite, QuantityValue):
            self.nitrite = QuantityValue(**self.nitrite)

        if self.org_matter is not None and not isinstance(self.org_matter, QuantityValue):
            self.org_matter = QuantityValue(**self.org_matter)

        if self.org_nitro is not None and not isinstance(self.org_nitro, QuantityValue):
            self.org_nitro = QuantityValue(**self.org_nitro)

        if self.organism_count is not None and not isinstance(self.organism_count, QuantityValue):
            self.organism_count = QuantityValue(**self.organism_count)

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, TextValue):
            self.oxy_stat_samp = TextValue(**self.oxy_stat_samp)

        if self.part_org_carb is not None and not isinstance(self.part_org_carb, QuantityValue):
            self.part_org_carb = QuantityValue(**self.part_org_carb)

        if self.perturbation is not None and not isinstance(self.perturbation, TextValue):
            self.perturbation = TextValue(**self.perturbation)

        if self.petroleum_hydrocarb is not None and not isinstance(self.petroleum_hydrocarb, QuantityValue):
            self.petroleum_hydrocarb = QuantityValue(**self.petroleum_hydrocarb)

        if self.ph is not None and not isinstance(self.ph, QuantityValue):
            self.ph = QuantityValue(**self.ph)

        if self.ph_meth is not None and not isinstance(self.ph_meth, TextValue):
            self.ph_meth = TextValue(**self.ph_meth)

        if self.phaeopigments is not None and not isinstance(self.phaeopigments, QuantityValue):
            self.phaeopigments = QuantityValue(**self.phaeopigments)

        if self.phosplipid_fatt_acid is not None and not isinstance(self.phosplipid_fatt_acid, QuantityValue):
            self.phosplipid_fatt_acid = QuantityValue(**self.phosplipid_fatt_acid)

        if self.pool_dna_extracts is not None and not isinstance(self.pool_dna_extracts, TextValue):
            self.pool_dna_extracts = TextValue(**self.pool_dna_extracts)

        if self.potassium is not None and not isinstance(self.potassium, QuantityValue):
            self.potassium = QuantityValue(**self.potassium)

        if self.pressure is not None and not isinstance(self.pressure, QuantityValue):
            self.pressure = QuantityValue(**self.pressure)

        if self.previous_land_use is not None and not isinstance(self.previous_land_use, TextValue):
            self.previous_land_use = TextValue(**self.previous_land_use)

        if self.previous_land_use_meth is not None and not isinstance(self.previous_land_use_meth, TextValue):
            self.previous_land_use_meth = TextValue(**self.previous_land_use_meth)

        if self.profile_position is not None and not isinstance(self.profile_position, TextValue):
            self.profile_position = TextValue(**self.profile_position)

        if self.redox_potential is not None and not isinstance(self.redox_potential, QuantityValue):
            self.redox_potential = QuantityValue(**self.redox_potential)

        if self.salinity is not None and not isinstance(self.salinity, QuantityValue):
            self.salinity = QuantityValue(**self.salinity)

        if self.salinity_meth is not None and not isinstance(self.salinity_meth, TextValue):
            self.salinity_meth = TextValue(**self.salinity_meth)

        if self.samp_collect_device is not None and not isinstance(self.samp_collect_device, TextValue):
            self.samp_collect_device = TextValue(**self.samp_collect_device)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, TextValue):
            self.samp_store_dur = TextValue(**self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, TextValue):
            self.samp_store_loc = TextValue(**self.samp_store_loc)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, QuantityValue):
            self.samp_store_temp = QuantityValue(**self.samp_store_temp)

        if self.samp_vol_we_dna_ext is not None and not isinstance(self.samp_vol_we_dna_ext, QuantityValue):
            self.samp_vol_we_dna_ext = QuantityValue(**self.samp_vol_we_dna_ext)

        if self.season_temp is not None and not isinstance(self.season_temp, QuantityValue):
            self.season_temp = QuantityValue(**self.season_temp)

        if self.season_precpt is not None and not isinstance(self.season_precpt, QuantityValue):
            self.season_precpt = QuantityValue(**self.season_precpt)

        if self.sieving is not None and not isinstance(self.sieving, QuantityValue):
            self.sieving = QuantityValue(**self.sieving)

        if self.size_frac_low is not None and not isinstance(self.size_frac_low, QuantityValue):
            self.size_frac_low = QuantityValue(**self.size_frac_low)

        if self.size_frac_up is not None and not isinstance(self.size_frac_up, QuantityValue):
            self.size_frac_up = QuantityValue(**self.size_frac_up)

        if self.slope_gradient is not None and not isinstance(self.slope_gradient, QuantityValue):
            self.slope_gradient = QuantityValue(**self.slope_gradient)

        if self.slope_aspect is not None and not isinstance(self.slope_aspect, QuantityValue):
            self.slope_aspect = QuantityValue(**self.slope_aspect)

        if self.sodium is not None and not isinstance(self.sodium, QuantityValue):
            self.sodium = QuantityValue(**self.sodium)

        if self.soil_type is not None and not isinstance(self.soil_type, TextValue):
            self.soil_type = TextValue(**self.soil_type)

        if self.soil_type_meth is not None and not isinstance(self.soil_type_meth, TextValue):
            self.soil_type_meth = TextValue(**self.soil_type_meth)

        if self.store_cond is not None and not isinstance(self.store_cond, TextValue):
            self.store_cond = TextValue(**self.store_cond)

        if self.sulfate is not None and not isinstance(self.sulfate, QuantityValue):
            self.sulfate = QuantityValue(**self.sulfate)

        if self.sulfide is not None and not isinstance(self.sulfide, QuantityValue):
            self.sulfide = QuantityValue(**self.sulfide)

        if self.temp is not None and not isinstance(self.temp, QuantityValue):
            self.temp = QuantityValue(**self.temp)

        if self.texture is not None and not isinstance(self.texture, QuantityValue):
            self.texture = QuantityValue(**self.texture)

        if self.texture_meth is not None and not isinstance(self.texture_meth, TextValue):
            self.texture_meth = TextValue(**self.texture_meth)

        if self.tillage is not None and not isinstance(self.tillage, TextValue):
            self.tillage = TextValue(**self.tillage)

        if self.tidal_stage is not None and not isinstance(self.tidal_stage, TextValue):
            self.tidal_stage = TextValue(**self.tidal_stage)

        if self.tot_carb is not None and not isinstance(self.tot_carb, QuantityValue):
            self.tot_carb = QuantityValue(**self.tot_carb)

        if self.tot_depth_water_col is not None and not isinstance(self.tot_depth_water_col, QuantityValue):
            self.tot_depth_water_col = QuantityValue(**self.tot_depth_water_col)

        if self.tot_diss_nitro is not None and not isinstance(self.tot_diss_nitro, QuantityValue):
            self.tot_diss_nitro = QuantityValue(**self.tot_diss_nitro)

        if self.tot_org_carb is not None and not isinstance(self.tot_org_carb, QuantityValue):
            self.tot_org_carb = QuantityValue(**self.tot_org_carb)

        if self.tot_org_c_meth is not None and not isinstance(self.tot_org_c_meth, TextValue):
            self.tot_org_c_meth = TextValue(**self.tot_org_c_meth)

        if self.tot_nitro_content is not None and not isinstance(self.tot_nitro_content, QuantityValue):
            self.tot_nitro_content = QuantityValue(**self.tot_nitro_content)

        if self.tot_nitro_content_meth is not None and not isinstance(self.tot_nitro_content_meth, TextValue):
            self.tot_nitro_content_meth = TextValue(**self.tot_nitro_content_meth)

        if self.tot_phosp is not None and not isinstance(self.tot_phosp, QuantityValue):
            self.tot_phosp = QuantityValue(**self.tot_phosp)

        if self.water_content is not None and not isinstance(self.water_content, QuantityValue):
            self.water_content = QuantityValue(**self.water_content)

        if self.water_content_soil_meth is not None and not isinstance(self.water_content_soil_meth, TextValue):
            self.water_content_soil_meth = TextValue(**self.water_content_soil_meth)

        if self.ecosystem is not None and not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self.ecosystem_category is not None and not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self.ecosystem_type is not None and not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self.ecosystem_subtype is not None and not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self.specific_ecosystem is not None and not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self.add_date is not None and not isinstance(self.add_date, str):
            self.add_date = str(self.add_date)

        if self.community is not None and not isinstance(self.community, str):
            self.community = str(self.community)

        if self.habitat is not None and not isinstance(self.habitat, str):
            self.habitat = str(self.habitat)

        if self.host_name is not None and not isinstance(self.host_name, str):
            self.host_name = str(self.host_name)

        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if self.location is not None and not isinstance(self.location, str):
            self.location = str(self.location)

        if self.mod_date is not None and not isinstance(self.mod_date, str):
            self.mod_date = str(self.mod_date)

        if self.ncbi_taxonomy_name is not None and not isinstance(self.ncbi_taxonomy_name, str):
            self.ncbi_taxonomy_name = str(self.ncbi_taxonomy_name)

        if self.proport_woa_temperature is not None and not isinstance(self.proport_woa_temperature, str):
            self.proport_woa_temperature = str(self.proport_woa_temperature)

        if self.salinity_category is not None and not isinstance(self.salinity_category, str):
            self.salinity_category = str(self.salinity_category)

        if self.sample_collection_site is not None and not isinstance(self.sample_collection_site, str):
            self.sample_collection_site = str(self.sample_collection_site)

        if self.soluble_iron_micromol is not None and not isinstance(self.soluble_iron_micromol, str):
            self.soluble_iron_micromol = str(self.soluble_iron_micromol)

        if self.subsurface_depth is not None and not isinstance(self.subsurface_depth, QuantityValue):
            self.subsurface_depth = QuantityValue(**self.subsurface_depth)

        super().__post_init__(**kwargs)


@dataclass
class Study(NamedThing):
    """
    A study summarizes the overall goal of a research initiative and outlines the key objective of its underlying
    projects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.Study
    class_class_curie: ClassVar[str] = "nmdc:Study"
    class_name: ClassVar[str] = "study"
    class_model_uri: ClassVar[URIRef] = NMDC.Study

    id: Union[str, StudyId] = None
    ecosystem: Optional[str] = None
    ecosystem_category: Optional[str] = None
    ecosystem_type: Optional[str] = None
    ecosystem_subtype: Optional[str] = None
    specific_ecosystem: Optional[str] = None
    principal_investigator_name: Optional[Union[dict, PersonValue]] = None
    doi: Optional[Union[dict, AttributeValue]] = None
    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, StudyId):
            self.id = StudyId(self.id)

        if self.ecosystem is not None and not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self.ecosystem_category is not None and not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self.ecosystem_type is not None and not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self.ecosystem_subtype is not None and not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self.specific_ecosystem is not None and not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self.principal_investigator_name is not None and not isinstance(self.principal_investigator_name, PersonValue):
            self.principal_investigator_name = PersonValue(**self.principal_investigator_name)

        if self.doi is not None and not isinstance(self.doi, AttributeValue):
            self.doi = AttributeValue(**self.doi)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass
class BiosampleProcessing(NamedThing):
    """
    A process that takes one or more biosamples as inputs and generates one or as outputs. Examples of outputs include
    samples cultivated from another sample or data objects created by instruments runs.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.BiosampleProcessing
    class_class_curie: ClassVar[str] = "nmdc:BiosampleProcessing"
    class_name: ClassVar[str] = "biosample processing"
    class_model_uri: ClassVar[URIRef] = NMDC.BiosampleProcessing

    id: Union[str, BiosampleProcessingId] = None
    has_input: Optional[Union[Union[str, BiosampleId], List[Union[str, BiosampleId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BiosampleProcessingId):
            self.id = BiosampleProcessingId(self.id)

        if self.has_input is None:
            self.has_input = []
        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input]
        self.has_input = [v if isinstance(v, BiosampleId) else BiosampleId(v) for v in self.has_input]

        super().__post_init__(**kwargs)


@dataclass
class OmicsProcessing(BiosampleProcessing):
    """
    The methods and processes used to generate omics data from a biosample or organism.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.OmicsProcessing
    class_class_curie: ClassVar[str] = "nmdc:OmicsProcessing"
    class_name: ClassVar[str] = "omics processing"
    class_model_uri: ClassVar[URIRef] = NMDC.OmicsProcessing

    id: Union[str, OmicsProcessingId] = None
    add_date: Optional[str] = None
    mod_date: Optional[str] = None
    has_input: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()
    has_output: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()
    instrument_name: Optional[str] = None
    ncbi_project_name: Optional[str] = None
    omics_type: Optional[Union[dict, ControlledTermValue]] = None
    part_of: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()
    principal_investigator_name: Optional[Union[dict, PersonValue]] = None
    processing_institution: Optional[str] = None
    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, OmicsProcessingId):
            self.id = OmicsProcessingId(self.id)

        if self.add_date is not None and not isinstance(self.add_date, str):
            self.add_date = str(self.add_date)

        if self.mod_date is not None and not isinstance(self.mod_date, str):
            self.mod_date = str(self.mod_date)

        if self.has_input is None:
            self.has_input = []
        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input]
        self.has_input = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_input]

        if self.has_output is None:
            self.has_output = []
        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output]
        self.has_output = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_output]

        if self.instrument_name is not None and not isinstance(self.instrument_name, str):
            self.instrument_name = str(self.instrument_name)

        if self.ncbi_project_name is not None and not isinstance(self.ncbi_project_name, str):
            self.ncbi_project_name = str(self.ncbi_project_name)

        if self.omics_type is not None and not isinstance(self.omics_type, ControlledTermValue):
            self.omics_type = ControlledTermValue(**self.omics_type)

        if self.part_of is None:
            self.part_of = []
        if not isinstance(self.part_of, list):
            self.part_of = [self.part_of]
        self.part_of = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.part_of]

        if self.principal_investigator_name is not None and not isinstance(self.principal_investigator_name, PersonValue):
            self.principal_investigator_name = PersonValue(**self.principal_investigator_name)

        if self.processing_institution is not None and not isinstance(self.processing_institution, str):
            self.processing_institution = str(self.processing_institution)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.object_set = Slot(uri=NMDC.object_set, name="object set", curie=NMDC.curie('object_set'),
                   model_uri=NMDC.object_set, domain=Database, range=Optional[Union[str, List[str]]])

slots.biosample_set = Slot(uri=NMDC.biosample_set, name="biosample set", curie=NMDC.curie('biosample_set'),
                   model_uri=NMDC.biosample_set, domain=Database, range=Optional[Union[Dict[Union[str, BiosampleId], Union[dict, "Biosample"]], List[Union[dict, "Biosample"]]]])

slots.study_set = Slot(uri=NMDC.study_set, name="study set", curie=NMDC.curie('study_set'),
                   model_uri=NMDC.study_set, domain=Database, range=Optional[Union[Dict[Union[str, StudyId], Union[dict, "Study"]], List[Union[dict, "Study"]]]])

slots.data_object_set = Slot(uri=NMDC.data_object_set, name="data object set", curie=NMDC.curie('data_object_set'),
                   model_uri=NMDC.data_object_set, domain=Database, range=Optional[Union[Dict[Union[str, DataObjectId], Union[dict, "DataObject"]], List[Union[dict, "DataObject"]]]])

slots.genome_feature_set = Slot(uri=NMDC.genome_feature_set, name="genome feature set", curie=NMDC.curie('genome_feature_set'),
                   model_uri=NMDC.genome_feature_set, domain=Database, range=Optional[Union[Union[dict, GenomeFeature], List[Union[dict, GenomeFeature]]]])

slots.functional_annotation_set = Slot(uri=NMDC.functional_annotation_set, name="functional annotation set", curie=NMDC.curie('functional_annotation_set'),
                   model_uri=NMDC.functional_annotation_set, domain=Database, range=Optional[Union[Union[dict, FunctionalAnnotation], List[Union[dict, FunctionalAnnotation]]]])

slots.activity_set = Slot(uri=NMDC.activity_set, name="activity set", curie=NMDC.curie('activity_set'),
                   model_uri=NMDC.activity_set, domain=Database, range=Optional[Union[Dict[Union[str, WorkflowExecutionActivityId], Union[dict, WorkflowExecutionActivity]], List[Union[dict, WorkflowExecutionActivity]]]])

slots.mags_activity_set = Slot(uri=NMDC.mags_activity_set, name="mags activity set", curie=NMDC.curie('mags_activity_set'),
                   model_uri=NMDC.mags_activity_set, domain=Database, range=Optional[Union[Dict[Union[str, MAGsAnalysisActivityId], Union[dict, MAGsAnalysisActivity]], List[Union[dict, MAGsAnalysisActivity]]]])

slots.metabolomics_analysis_activity_set = Slot(uri=NMDC.metabolomics_analysis_activity_set, name="metabolomics analysis activity set", curie=NMDC.curie('metabolomics_analysis_activity_set'),
                   model_uri=NMDC.metabolomics_analysis_activity_set, domain=Database, range=Optional[Union[Dict[Union[str, MetabolomicsAnalysisActivityId], Union[dict, MetabolomicsAnalysisActivity]], List[Union[dict, MetabolomicsAnalysisActivity]]]])

slots.metaproteomics_analysis_activity_set = Slot(uri=NMDC.metaproteomics_analysis_activity_set, name="metaproteomics analysis activity set", curie=NMDC.curie('metaproteomics_analysis_activity_set'),
                   model_uri=NMDC.metaproteomics_analysis_activity_set, domain=Database, range=Optional[Union[Dict[Union[str, MetaproteomicsAnalysisActivityId], Union[dict, MetaproteomicsAnalysisActivity]], List[Union[dict, MetaproteomicsAnalysisActivity]]]])

slots.metagenome_annotation_activity_set = Slot(uri=NMDC.metagenome_annotation_activity_set, name="metagenome annotation activity set", curie=NMDC.curie('metagenome_annotation_activity_set'),
                   model_uri=NMDC.metagenome_annotation_activity_set, domain=Database, range=Optional[Union[Dict[Union[str, MetagenomeAnnotationActivityId], Union[dict, MetagenomeAnnotationActivity]], List[Union[dict, MetagenomeAnnotationActivity]]]])

slots.metagenome_assembly_set = Slot(uri=NMDC.metagenome_assembly_set, name="metagenome assembly set", curie=NMDC.curie('metagenome_assembly_set'),
                   model_uri=NMDC.metagenome_assembly_set, domain=Database, range=Optional[Union[Dict[Union[str, MetagenomeAssemblyId], Union[dict, MetagenomeAssembly]], List[Union[dict, MetagenomeAssembly]]]])

slots.read_QC_analysis_activity_set = Slot(uri=NMDC.read_QC_analysis_activity_set, name="read QC analysis activity set", curie=NMDC.curie('read_QC_analysis_activity_set'),
                   model_uri=NMDC.read_QC_analysis_activity_set, domain=Database, range=Optional[Union[Dict[Union[str, ReadQCAnalysisActivityId], Union[dict, ReadQCAnalysisActivity]], List[Union[dict, ReadQCAnalysisActivity]]]])

slots.read_based_analysis_activity_set = Slot(uri=NMDC.read_based_analysis_activity_set, name="read based analysis activity set", curie=NMDC.curie('read_based_analysis_activity_set'),
                   model_uri=NMDC.read_based_analysis_activity_set, domain=Database, range=Optional[Union[Dict[Union[str, ReadBasedAnalysisActivityId], Union[dict, ReadBasedAnalysisActivity]], List[Union[dict, ReadBasedAnalysisActivity]]]])

slots.nom_analysis_activity_set = Slot(uri=NMDC.nom_analysis_activity_set, name="nom analysis activity set", curie=NMDC.curie('nom_analysis_activity_set'),
                   model_uri=NMDC.nom_analysis_activity_set, domain=Database, range=Optional[Union[Dict[Union[str, NomAnalysisActivityId], Union[dict, NomAnalysisActivity]], List[Union[dict, NomAnalysisActivity]]]])

slots.omics_processing_set = Slot(uri=NMDC.omics_processing_set, name="omics processing set", curie=NMDC.curie('omics_processing_set'),
                   model_uri=NMDC.omics_processing_set, domain=Database, range=Optional[Union[Dict[Union[str, OmicsProcessingId], Union[dict, "OmicsProcessing"]], List[Union[dict, "OmicsProcessing"]]]])

slots.omics_type = Slot(uri=NMDC.omics_type, name="omics type", curie=NMDC.curie('omics_type'),
                   model_uri=NMDC.omics_type, domain=None, range=Optional[Union[dict, ControlledTermValue]])

slots.data_object_type = Slot(uri=NMDC.data_object_type, name="data object type", curie=NMDC.curie('data_object_type'),
                   model_uri=NMDC.data_object_type, domain=None, range=Optional[Union[dict, ControlledTermValue]])

slots.compression_type = Slot(uri=NMDC.compression_type, name="compression type", curie=NMDC.curie('compression_type'),
                   model_uri=NMDC.compression_type, domain=None, range=Optional[str])

slots.instrument_name = Slot(uri=NMDC.instrument_name, name="instrument_name", curie=NMDC.curie('instrument_name'),
                   model_uri=NMDC.instrument_name, domain=None, range=Optional[str])

slots.gold_path_field = Slot(uri=NMDC.gold_path_field, name="gold_path_field", curie=NMDC.curie('gold_path_field'),
                   model_uri=NMDC.gold_path_field, domain=None, range=Optional[str])

slots.ecosystem = Slot(uri=NMDC.ecosystem, name="ecosystem", curie=NMDC.curie('ecosystem'),
                   model_uri=NMDC.ecosystem, domain=None, range=Optional[str])

slots.ecosystem_category = Slot(uri=NMDC.ecosystem_category, name="ecosystem_category", curie=NMDC.curie('ecosystem_category'),
                   model_uri=NMDC.ecosystem_category, domain=None, range=Optional[str])

slots.ecosystem_type = Slot(uri=NMDC.ecosystem_type, name="ecosystem_type", curie=NMDC.curie('ecosystem_type'),
                   model_uri=NMDC.ecosystem_type, domain=None, range=Optional[str])

slots.ecosystem_subtype = Slot(uri=NMDC.ecosystem_subtype, name="ecosystem_subtype", curie=NMDC.curie('ecosystem_subtype'),
                   model_uri=NMDC.ecosystem_subtype, domain=None, range=Optional[str])

slots.specific_ecosystem = Slot(uri=NMDC.specific_ecosystem, name="specific_ecosystem", curie=NMDC.curie('specific_ecosystem'),
                   model_uri=NMDC.specific_ecosystem, domain=None, range=Optional[str])

slots.principal_investigator_name = Slot(uri=NMDC.principal_investigator_name, name="principal investigator name", curie=NMDC.curie('principal_investigator_name'),
                   model_uri=NMDC.principal_investigator_name, domain=None, range=Optional[Union[dict, PersonValue]])

slots.doi = Slot(uri=NMDC.doi, name="doi", curie=NMDC.curie('doi'),
                   model_uri=NMDC.doi, domain=None, range=Optional[Union[dict, AttributeValue]])

slots.add_date = Slot(uri=NMDC.add_date, name="add_date", curie=NMDC.curie('add_date'),
                   model_uri=NMDC.add_date, domain=None, range=Optional[str])

slots.mod_date = Slot(uri=NMDC.mod_date, name="mod_date", curie=NMDC.curie('mod_date'),
                   model_uri=NMDC.mod_date, domain=None, range=Optional[str])

slots.ecosystem_path_id = Slot(uri=NMDC.ecosystem_path_id, name="ecosystem_path_id", curie=NMDC.curie('ecosystem_path_id'),
                   model_uri=NMDC.ecosystem_path_id, domain=None, range=Optional[str])

slots.habitat = Slot(uri=NMDC.habitat, name="habitat", curie=NMDC.curie('habitat'),
                   model_uri=NMDC.habitat, domain=None, range=Optional[str])

slots.location = Slot(uri=NMDC.location, name="location", curie=NMDC.curie('location'),
                   model_uri=NMDC.location, domain=None, range=Optional[str])

slots.community = Slot(uri=NMDC.community, name="community", curie=NMDC.curie('community'),
                   model_uri=NMDC.community, domain=None, range=Optional[str])

slots.ncbi_taxonomy_name = Slot(uri=NMDC.ncbi_taxonomy_name, name="ncbi_taxonomy_name", curie=NMDC.curie('ncbi_taxonomy_name'),
                   model_uri=NMDC.ncbi_taxonomy_name, domain=None, range=Optional[str])

slots.ncbi_project_name = Slot(uri=NMDC.ncbi_project_name, name="ncbi_project_name", curie=NMDC.curie('ncbi_project_name'),
                   model_uri=NMDC.ncbi_project_name, domain=None, range=Optional[str])

slots.sample_collection_site = Slot(uri=NMDC.sample_collection_site, name="sample_collection_site", curie=NMDC.curie('sample_collection_site'),
                   model_uri=NMDC.sample_collection_site, domain=None, range=Optional[str])

slots.identifier = Slot(uri=NMDC.identifier, name="identifier", curie=NMDC.curie('identifier'),
                   model_uri=NMDC.identifier, domain=None, range=Optional[str])

slots.sample_collection_year = Slot(uri=NMDC.sample_collection_year, name="sample_collection_year", curie=NMDC.curie('sample_collection_year'),
                   model_uri=NMDC.sample_collection_year, domain=None, range=Optional[int])

slots.sample_collection_month = Slot(uri=NMDC.sample_collection_month, name="sample_collection_month", curie=NMDC.curie('sample_collection_month'),
                   model_uri=NMDC.sample_collection_month, domain=None, range=Optional[int])

slots.sample_collection_day = Slot(uri=NMDC.sample_collection_day, name="sample_collection_day", curie=NMDC.curie('sample_collection_day'),
                   model_uri=NMDC.sample_collection_day, domain=None, range=Optional[int])

slots.sample_collection_hour = Slot(uri=NMDC.sample_collection_hour, name="sample_collection_hour", curie=NMDC.curie('sample_collection_hour'),
                   model_uri=NMDC.sample_collection_hour, domain=None, range=Optional[int])

slots.sample_collection_minute = Slot(uri=NMDC.sample_collection_minute, name="sample_collection_minute", curie=NMDC.curie('sample_collection_minute'),
                   model_uri=NMDC.sample_collection_minute, domain=None, range=Optional[int])

slots.salinity_category = Slot(uri=NMDC.salinity_category, name="salinity_category", curie=NMDC.curie('salinity_category'),
                   model_uri=NMDC.salinity_category, domain=None, range=Optional[str])

slots.soluble_iron_micromol = Slot(uri=NMDC.soluble_iron_micromol, name="soluble_iron_micromol", curie=NMDC.curie('soluble_iron_micromol'),
                   model_uri=NMDC.soluble_iron_micromol, domain=None, range=Optional[str])

slots.host_name = Slot(uri=NMDC.host_name, name="host_name", curie=NMDC.curie('host_name'),
                   model_uri=NMDC.host_name, domain=None, range=Optional[str])

slots.subsurface_depth = Slot(uri=NMDC.subsurface_depth, name="subsurface_depth", curie=NMDC.curie('subsurface_depth'),
                   model_uri=NMDC.subsurface_depth, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.proport_woa_temperature = Slot(uri=NMDC.proport_woa_temperature, name="proport_woa_temperature", curie=NMDC.curie('proport_woa_temperature'),
                   model_uri=NMDC.proport_woa_temperature, domain=None, range=Optional[str])

slots.biogas_temperature = Slot(uri=NMDC.biogas_temperature, name="biogas_temperature", curie=NMDC.curie('biogas_temperature'),
                   model_uri=NMDC.biogas_temperature, domain=None, range=Optional[str])

slots.soil_annual_season_temp = Slot(uri=NMDC.soil_annual_season_temp, name="soil_annual_season_temp", curie=NMDC.curie('soil_annual_season_temp'),
                   model_uri=NMDC.soil_annual_season_temp, domain=None, range=Optional[str])

slots.biogas_retention_time = Slot(uri=NMDC.biogas_retention_time, name="biogas_retention_time", curie=NMDC.curie('biogas_retention_time'),
                   model_uri=NMDC.biogas_retention_time, domain=None, range=Optional[str])

slots.processing_institution = Slot(uri=NMDC.processing_institution, name="processing_institution", curie=NMDC.curie('processing_institution'),
                   model_uri=NMDC.processing_institution, domain=None, range=Optional[str])

slots.omics_type = Slot(uri=NMDC.omics_type, name="omics_type", curie=NMDC.curie('omics_type'),
                   model_uri=NMDC.omics_type, domain=None, range=Optional[str])

slots.completion_date = Slot(uri=NMDC.completion_date, name="completion_date", curie=NMDC.curie('completion_date'),
                   model_uri=NMDC.completion_date, domain=None, range=Optional[str])

slots.metabolite_quantified = Slot(uri=NMDC.metabolite_quantified, name="metabolite quantified", curie=NMDC.curie('metabolite_quantified'),
                   model_uri=NMDC.metabolite_quantified, domain=None, range=Optional[Union[str, ChemicalEntityId]])

slots.highest_similarity_score = Slot(uri=NMDC.highest_similarity_score, name="highest similarity score", curie=NMDC.curie('highest_similarity_score'),
                   model_uri=NMDC.highest_similarity_score, domain=None, range=Optional[float])

slots.alternate_identifiers = Slot(uri=NMDC.alternate_identifiers, name="alternate_identifiers", curie=NMDC.curie('alternate_identifiers'),
                   model_uri=NMDC.alternate_identifiers, domain=None, range=Optional[Union[str, List[str]]])

slots.peptide_sequence = Slot(uri=NMDC.peptide_sequence, name="peptide sequence", curie=NMDC.curie('peptide_sequence'),
                   model_uri=NMDC.peptide_sequence, domain=None, range=Optional[str])

slots.best_protein = Slot(uri=NMDC.best_protein, name="best protein", curie=NMDC.curie('best_protein'),
                   model_uri=NMDC.best_protein, domain=None, range=Optional[Union[str, GeneProductId]])

slots.all_proteins = Slot(uri=NMDC.all_proteins, name="all proteins", curie=NMDC.curie('all_proteins'),
                   model_uri=NMDC.all_proteins, domain=None, range=Optional[Union[Union[str, GeneProductId], List[Union[str, GeneProductId]]]])

slots.min_q_value = Slot(uri=NMDC.min_q_value, name="min_q_value", curie=NMDC.curie('min_q_value'),
                   model_uri=NMDC.min_q_value, domain=None, range=Optional[float])

slots.peptide_spectral_count = Slot(uri=NMDC.peptide_spectral_count, name="peptide_spectral_count", curie=NMDC.curie('peptide_spectral_count'),
                   model_uri=NMDC.peptide_spectral_count, domain=None, range=Optional[int])

slots.peptide_sum_masic_abundance = Slot(uri=NMDC.peptide_sum_masic_abundance, name="peptide_sum_masic_abundance", curie=NMDC.curie('peptide_sum_masic_abundance'),
                   model_uri=NMDC.peptide_sum_masic_abundance, domain=None, range=Optional[int])

slots.peptide_sequence_count = Slot(uri=NMDC.peptide_sequence_count, name="peptide_sequence_count", curie=NMDC.curie('peptide_sequence_count'),
                   model_uri=NMDC.peptide_sequence_count, domain=None, range=Optional[int])

slots.protein_spectral_count = Slot(uri=NMDC.protein_spectral_count, name="protein_spectral_count", curie=NMDC.curie('protein_spectral_count'),
                   model_uri=NMDC.protein_spectral_count, domain=None, range=Optional[int])

slots.protein_sum_masic_abundance = Slot(uri=NMDC.protein_sum_masic_abundance, name="protein_sum_masic_abundance", curie=NMDC.curie('protein_sum_masic_abundance'),
                   model_uri=NMDC.protein_sum_masic_abundance, domain=None, range=Optional[int])

slots.inchi = Slot(uri=NMDC.inchi, name="inchi", curie=NMDC.curie('inchi'),
                   model_uri=NMDC.inchi, domain=None, range=Optional[str])

slots.inchi_key = Slot(uri=NMDC.inchi_key, name="inchi key", curie=NMDC.curie('inchi_key'),
                   model_uri=NMDC.inchi_key, domain=None, range=Optional[str])

slots.smiles = Slot(uri=NMDC.smiles, name="smiles", curie=NMDC.curie('smiles'),
                   model_uri=NMDC.smiles, domain=None, range=Optional[Union[str, List[str]]])

slots.chemical_formula = Slot(uri=NMDC.chemical_formula, name="chemical formula", curie=NMDC.curie('chemical_formula'),
                   model_uri=NMDC.chemical_formula, domain=None, range=Optional[str])

slots.input_read_bases = Slot(uri=NMDC.input_read_bases, name="input_read_bases", curie=NMDC.curie('input_read_bases'),
                   model_uri=NMDC.input_read_bases, domain=None, range=Optional[float])

slots.output_read_bases = Slot(uri=NMDC.output_read_bases, name="output_read_bases", curie=NMDC.curie('output_read_bases'),
                   model_uri=NMDC.output_read_bases, domain=None, range=Optional[float])

slots.has_metabolite_quantifications = Slot(uri=NMDC.has_metabolite_quantifications, name="has metabolite quantifications", curie=NMDC.curie('has_metabolite_quantifications'),
                   model_uri=NMDC.has_metabolite_quantifications, domain=None, range=Optional[Union[Union[dict, MetaboliteQuantification], List[Union[dict, MetaboliteQuantification]]]])

slots.has_calibration = Slot(uri=NMDC.has_calibration, name="has calibration", curie=NMDC.curie('has_calibration'),
                   model_uri=NMDC.has_calibration, domain=None, range=Optional[str])

slots.has_peptide_quantifications = Slot(uri=NMDC.has_peptide_quantifications, name="has peptide quantifications", curie=NMDC.curie('has_peptide_quantifications'),
                   model_uri=NMDC.has_peptide_quantifications, domain=None, range=Optional[Union[Union[dict, PeptideQuantification], List[Union[dict, PeptideQuantification]]]])

slots.seqid = Slot(uri=NMDC.seqid, name="seqid", curie=NMDC.curie('seqid'),
                   model_uri=NMDC.seqid, domain=None, range=str)

slots.start = Slot(uri=NMDC.start, name="start", curie=NMDC.curie('start'),
                   model_uri=NMDC.start, domain=None, range=int)

slots.end = Slot(uri=NMDC.end, name="end", curie=NMDC.curie('end'),
                   model_uri=NMDC.end, domain=None, range=int)

slots.strand = Slot(uri=NMDC.strand, name="strand", curie=NMDC.curie('strand'),
                   model_uri=NMDC.strand, domain=None, range=Optional[str])

slots.phase = Slot(uri=NMDC.phase, name="phase", curie=NMDC.curie('phase'),
                   model_uri=NMDC.phase, domain=None, range=Optional[int])

slots.encodes = Slot(uri=NMDC.encodes, name="encodes", curie=NMDC.curie('encodes'),
                   model_uri=NMDC.encodes, domain=None, range=Optional[Union[str, GeneProductId]])

slots.feature_type = Slot(uri=NMDC.feature_type, name="feature type", curie=NMDC.curie('feature_type'),
                   model_uri=NMDC.feature_type, domain=None, range=Optional[str])

slots.has_part = Slot(uri=NMDC.has_part, name="has_part", curie=NMDC.curie('has_part'),
                   model_uri=NMDC.has_part, domain=None, range=Optional[Union[Union[str, ReactionId], List[Union[str, ReactionId]]]])

slots.left_participants = Slot(uri=NMDC.left_participants, name="left participants", curie=NMDC.curie('left_participants'),
                   model_uri=NMDC.left_participants, domain=None, range=Optional[Union[Union[dict, ReactionParticipant], List[Union[dict, ReactionParticipant]]]])

slots.right_participants = Slot(uri=NMDC.right_participants, name="right participants", curie=NMDC.curie('right_participants'),
                   model_uri=NMDC.right_participants, domain=None, range=Optional[Union[Union[dict, ReactionParticipant], List[Union[dict, ReactionParticipant]]]])

slots.direction = Slot(uri=NMDC.direction, name="direction", curie=NMDC.curie('direction'),
                   model_uri=NMDC.direction, domain=None, range=Optional[str])

slots.smarts_string = Slot(uri=NMDC.smarts_string, name="smarts string", curie=NMDC.curie('smarts_string'),
                   model_uri=NMDC.smarts_string, domain=None, range=Optional[str])

slots.is_diastereoselective = Slot(uri=NMDC.is_diastereoselective, name="is diastereoselective", curie=NMDC.curie('is_diastereoselective'),
                   model_uri=NMDC.is_diastereoselective, domain=None, range=Optional[Union[bool, Bool]])

slots.is_stereo = Slot(uri=NMDC.is_stereo, name="is stereo", curie=NMDC.curie('is_stereo'),
                   model_uri=NMDC.is_stereo, domain=None, range=Optional[Union[bool, Bool]])

slots.is_balanced = Slot(uri=NMDC.is_balanced, name="is balanced", curie=NMDC.curie('is_balanced'),
                   model_uri=NMDC.is_balanced, domain=None, range=Optional[Union[bool, Bool]])

slots.is_transport = Slot(uri=NMDC.is_transport, name="is transport", curie=NMDC.curie('is_transport'),
                   model_uri=NMDC.is_transport, domain=None, range=Optional[Union[bool, Bool]])

slots.is_fully_characterized = Slot(uri=NMDC.is_fully_characterized, name="is fully characterized", curie=NMDC.curie('is_fully_characterized'),
                   model_uri=NMDC.is_fully_characterized, domain=None, range=Optional[Union[bool, Bool]])

slots.chemical = Slot(uri=NMDC.chemical, name="chemical", curie=NMDC.curie('chemical'),
                   model_uri=NMDC.chemical, domain=None, range=Optional[Union[str, ChemicalEntityId]])

slots.stoichiometry = Slot(uri=NMDC.stoichiometry, name="stoichiometry", curie=NMDC.curie('stoichiometry'),
                   model_uri=NMDC.stoichiometry, domain=None, range=Optional[int])

slots.biosample_lat_lon = Slot(uri=NMDC.lat_lon, name="biosample_lat_lon", curie=NMDC.curie('lat_lon'),
                   model_uri=NMDC.biosample_lat_lon, domain=Biosample, range=Optional[Union[dict, GeolocationValue]],
                   pattern=re.compile(r'\d+[.\d+] \d+[.\d+]'))

slots.biosample_processing_has_input = Slot(uri=NMDC.has_input, name="biosample processing_has input", curie=NMDC.curie('has_input'),
                   model_uri=NMDC.biosample_processing_has_input, domain=BiosampleProcessing, range=Optional[Union[Union[str, BiosampleId], List[Union[str, BiosampleId]]]])
