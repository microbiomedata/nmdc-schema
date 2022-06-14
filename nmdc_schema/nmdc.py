# Auto generated from nmdc.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-05-06T11:22:11
# Schema: NMDC
#
# id: https://microbiomedata/schema
# description: Schema for National Microbiome Data Collaborative (NMDC). This schema is organized into distinct
#              modules: * a set of core types for representing data values * the mixs schema (auto-translated from
#              mixs excel) * annotation schema * the NMDC schema itself
# license: https://creativecommons.org/publicdomain/zero/1.0/

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
from linkml_runtime.linkml_model.types import Boolean, Datetime, Double, Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDateTime

metamodel_version = "1.7.0"
version = "2.1.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
CAS = CurieNamespace('CAS', 'http://identifiers.org/cas/')
CATH = CurieNamespace('CATH', 'http://identifiers.org/cath/')
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
CHEMBL_COMPOUND = CurieNamespace('CHEMBL_COMPOUND', 'http://identifiers.org/chembl.compound/')
COG = CurieNamespace('COG', 'http://example.org/UNKNOWN/COG/')
DRUGBANK = CurieNamespace('DRUGBANK', 'http://identifiers.org/drugbank/')
EC = CurieNamespace('EC', 'http://example.org/UNKNOWN/EC/')
EGGNOG = CurieNamespace('EGGNOG', 'http://identifiers.org/eggnog/')
GO = CurieNamespace('GO', 'http://purl.obolibrary.org/obo/GO_')
GOLD = CurieNamespace('GOLD', 'https://identifiers.org/gold/')
HMDB = CurieNamespace('HMDB', 'http://identifiers.org/hmdb/')
ISA = CurieNamespace('ISA', 'http://example.org/UNKNOWN/ISA/')
KEGG_COMPOUND = CurieNamespace('KEGG_COMPOUND', 'http://identifiers.org/kegg.compound/')
KEGG_ORTHOLOGY = CurieNamespace('KEGG_ORTHOLOGY', 'http://identifiers.org/kegg.orthology/')
KEGG_PATHWAY = CurieNamespace('KEGG_PATHWAY', 'http://identifiers.org/kegg.pathway/')
KEGG_REACTION = CurieNamespace('KEGG_REACTION', 'http://identifiers.org/kegg.reaction/')
MESH = CurieNamespace('MESH', 'http://identifiers.org/mesh/')
MIXS = CurieNamespace('MIXS', 'https://w3id.org/gensc/')
MS = CurieNamespace('MS', 'http://purl.obolibrary.org/obo/MS_')
METACYC = CurieNamespace('MetaCyc', 'http://example.org/UNKNOWN/MetaCyc/')
METANETX = CurieNamespace('MetaNetX', 'http://example.org/UNKNOWN/MetaNetX/')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
PANTHER_FAMILY = CurieNamespace('PANTHER_FAMILY', 'http://identifiers.org/panther.family/')
PFAM = CurieNamespace('PFAM', 'http://identifiers.org/pfam/')
PR = CurieNamespace('PR', 'http://purl.obolibrary.org/obo/PR_')
PUBCHEM_COMPOUND = CurieNamespace('PUBCHEM_COMPOUND', 'http://identifiers.org/pubchem.compound/')
RHEA = CurieNamespace('RHEA', 'http://identifiers.org/rhea/')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
RETRORULES = CurieNamespace('RetroRules', 'http://example.org/UNKNOWN/RetroRules/')
SEED = CurieNamespace('SEED', 'http://identifiers.org/seed/')
SIO = CurieNamespace('SIO', 'http://semanticscience.org/resource/SIO_')
SUPFAM = CurieNamespace('SUPFAM', 'http://identifiers.org/supfam/')
TIGRFAM = CurieNamespace('TIGRFAM', 'http://identifiers.org/tigrfam/')
UNIPROTKB = CurieNamespace('UniProtKB', 'http://example.org/UNKNOWN/UniProtKB/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
GTPO = CurieNamespace('gtpo', 'http://example.org/UNKNOWN/gtpo/')
IGSN = CurieNamespace('igsn', 'https://app.geosamples.org/sample/igsn/')
IMG_TAXON = CurieNamespace('img_taxon', 'http://img.jgi.doe.gov/cgi-bin/w/main.cgi?section=TaxonDetail&taxon_oid=')
INSDC_SRS = CurieNamespace('insdc_srs', 'http://example.org/UNKNOWN/insdc.srs/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MGNIFY = CurieNamespace('mgnify', 'http://example.org/UNKNOWN/mgnify/')
MIXS = CurieNamespace('mixs', 'https://w3id.org/gensc/')
NMDC = CurieNamespace('nmdc', 'https://microbiomedata/meta/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
QUD = CurieNamespace('qud', 'http://qudt.org/1.1/schema/qudt#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://example.org/UNKNOWN/rdfs/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SIO = CurieNamespace('sio', 'http://semanticscience.org/resource/SIO_')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
WGS = CurieNamespace('wgs', 'http://www.w3.org/2003/01/geo/wgs84_pos')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = NMDC


# Types
class Bytes(int):
    """ An integer value that corresponds to a size in bytes """
    type_class_uri = XSD.int
    type_class_curie = "xsd:int"
    type_name = "bytes"
    type_model_uri = NMDC.Bytes


class DecimalDegree(float):
    """ A decimal degree expresses latitude or longitude as decimal fractions. """
    type_class_uri = XSD.decimal
    type_class_curie = "xsd:decimal"
    type_name = "decimal degree"
    type_model_uri = NMDC.DecimalDegree


class LanguageCode(str):
    """ A language code conforming to ISO_639-1 """
    type_class_uri = XSD.language
    type_class_curie = "xsd:language"
    type_name = "language code"
    type_model_uri = NMDC.LanguageCode


class Unit(str):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "unit"
    type_model_uri = NMDC.Unit


class ExternalIdentifier(Uriorcurie):
    """ A CURIE representing an external identifier """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "external identifier"
    type_model_uri = NMDC.ExternalIdentifier


# Class references
class NamedThingId(extended_str):
    pass


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


class OntologyClassId(NamedThingId):
    pass


class EnvironmentalMaterialTermId(OntologyClassId):
    pass


class PersonId(NamedThingId):
    pass


class InstrumentId(NamedThingId):
    pass


class ChemicalEntityId(OntologyClassId):
    pass


class GeneProductId(NamedThingId):
    pass


class ActivityId(extended_str):
    pass


class WorkflowExecutionActivityId(ActivityId):
    pass


class MetagenomeAssemblyId(WorkflowExecutionActivityId):
    pass


class MetatranscriptomeAssemblyId(WorkflowExecutionActivityId):
    pass


class MetagenomeAnnotationActivityId(WorkflowExecutionActivityId):
    pass


class MetatranscriptomeAnnotationActivityId(WorkflowExecutionActivityId):
    pass


class MetatranscriptomeActivityId(WorkflowExecutionActivityId):
    pass


class MAGsAnalysisActivityId(WorkflowExecutionActivityId):
    pass


class ReadQCAnalysisActivityId(WorkflowExecutionActivityId):
    pass


class ReadBasedAnalysisActivityId(WorkflowExecutionActivityId):
    pass


class MetabolomicsAnalysisActivityId(WorkflowExecutionActivityId):
    pass


class MetaproteomicsAnalysisActivityId(WorkflowExecutionActivityId):
    pass


class NomAnalysisActivityId(WorkflowExecutionActivityId):
    pass


class FunctionalAnnotationTermId(OntologyClassId):
    pass


class PathwayId(FunctionalAnnotationTermId):
    pass


class ReactionId(FunctionalAnnotationTermId):
    pass


class OrthologyGroupId(FunctionalAnnotationTermId):
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
    activity_set: Optional[Union[Dict[Union[str, WorkflowExecutionActivityId], Union[dict, "WorkflowExecutionActivity"]], List[Union[dict, "WorkflowExecutionActivity"]]]] = empty_dict()
    mags_activity_set: Optional[Union[Dict[Union[str, MAGsAnalysisActivityId], Union[dict, "MAGsAnalysisActivity"]], List[Union[dict, "MAGsAnalysisActivity"]]]] = empty_dict()
    metabolomics_analysis_activity_set: Optional[Union[Dict[Union[str, MetabolomicsAnalysisActivityId], Union[dict, "MetabolomicsAnalysisActivity"]], List[Union[dict, "MetabolomicsAnalysisActivity"]]]] = empty_dict()
    metaproteomics_analysis_activity_set: Optional[Union[Dict[Union[str, MetaproteomicsAnalysisActivityId], Union[dict, "MetaproteomicsAnalysisActivity"]], List[Union[dict, "MetaproteomicsAnalysisActivity"]]]] = empty_dict()
    metagenome_annotation_activity_set: Optional[Union[Dict[Union[str, MetagenomeAnnotationActivityId], Union[dict, "MetagenomeAnnotationActivity"]], List[Union[dict, "MetagenomeAnnotationActivity"]]]] = empty_dict()
    metagenome_assembly_set: Optional[Union[Dict[Union[str, MetagenomeAssemblyId], Union[dict, "MetagenomeAssembly"]], List[Union[dict, "MetagenomeAssembly"]]]] = empty_dict()
    metatranscriptome_activity_set: Optional[Union[Dict[Union[str, MetatranscriptomeActivityId], Union[dict, "MetatranscriptomeActivity"]], List[Union[dict, "MetatranscriptomeActivity"]]]] = empty_dict()
    read_QC_analysis_activity_set: Optional[Union[Dict[Union[str, ReadQCAnalysisActivityId], Union[dict, "ReadQCAnalysisActivity"]], List[Union[dict, "ReadQCAnalysisActivity"]]]] = empty_dict()
    read_based_analysis_activity_set: Optional[Union[Dict[Union[str, ReadBasedAnalysisActivityId], Union[dict, "ReadBasedAnalysisActivity"]], List[Union[dict, "ReadBasedAnalysisActivity"]]]] = empty_dict()
    nom_analysis_activity_set: Optional[Union[Dict[Union[str, NomAnalysisActivityId], Union[dict, "NomAnalysisActivity"]], List[Union[dict, "NomAnalysisActivity"]]]] = empty_dict()
    omics_processing_set: Optional[Union[Dict[Union[str, OmicsProcessingId], Union[dict, "OmicsProcessing"]], List[Union[dict, "OmicsProcessing"]]]] = empty_dict()
    functional_annotation_set: Optional[Union[Union[dict, "FunctionalAnnotation"], List[Union[dict, "FunctionalAnnotation"]]]] = empty_list()
    genome_feature_set: Optional[Union[Union[dict, "GenomeFeature"], List[Union[dict, "GenomeFeature"]]]] = empty_list()
    nmdc_schema_version: Optional[str] = None
    date_created: Optional[str] = None
    etl_software_version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="biosample_set", slot_type=Biosample, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="study_set", slot_type=Study, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="data_object_set", slot_type=DataObject, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="activity_set", slot_type=WorkflowExecutionActivity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="mags_activity_set", slot_type=MAGsAnalysisActivity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="metabolomics_analysis_activity_set", slot_type=MetabolomicsAnalysisActivity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="metaproteomics_analysis_activity_set", slot_type=MetaproteomicsAnalysisActivity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="metagenome_annotation_activity_set", slot_type=MetagenomeAnnotationActivity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="metagenome_assembly_set", slot_type=MetagenomeAssembly, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="metatranscriptome_activity_set", slot_type=MetatranscriptomeActivity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="read_QC_analysis_activity_set", slot_type=ReadQCAnalysisActivity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="read_based_analysis_activity_set", slot_type=ReadBasedAnalysisActivity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="nom_analysis_activity_set", slot_type=NomAnalysisActivity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="omics_processing_set", slot_type=OmicsProcessing, key_name="id", keyed=True)

        if not isinstance(self.functional_annotation_set, list):
            self.functional_annotation_set = [self.functional_annotation_set] if self.functional_annotation_set is not None else []
        self.functional_annotation_set = [v if isinstance(v, FunctionalAnnotation) else FunctionalAnnotation(**as_dict(v)) for v in self.functional_annotation_set]

        if not isinstance(self.genome_feature_set, list):
            self.genome_feature_set = [self.genome_feature_set] if self.genome_feature_set is not None else []
        self.genome_feature_set = [v if isinstance(v, GenomeFeature) else GenomeFeature(**as_dict(v)) for v in self.genome_feature_set]

        if self.nmdc_schema_version is not None and not isinstance(self.nmdc_schema_version, str):
            self.nmdc_schema_version = str(self.nmdc_schema_version)

        if self.date_created is not None and not isinstance(self.date_created, str):
            self.date_created = str(self.date_created)

        if self.etl_software_version is not None and not isinstance(self.etl_software_version, str):
            self.etl_software_version = str(self.etl_software_version)

        super().__post_init__(**kwargs)


@dataclass
class CreditAssociation(YAMLRoot):
    """
    This class supports binding associated researchers to studies. There will be at least a slot for a CRediT
    Contributor Role (https://casrai.org/credit/) and for a person value Specifically see the associated researchers
    tab on the NMDC_SampleMetadata-V4_CommentsForUpdates at
    https://docs.google.com/spreadsheets/d/1INlBo5eoqn2efn4H2P2i8rwRBtnbDVTqXrochJEAPko/edit#gid=0
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.Association
    class_class_curie: ClassVar[str] = "prov:Association"
    class_name: ClassVar[str] = "credit association"
    class_model_uri: ClassVar[URIRef] = NMDC.CreditAssociation

    applies_to_person: Union[dict, "PersonValue"] = None
    applied_roles: Union[Union[str, "CreditEnum"], List[Union[str, "CreditEnum"]]] = None
    applied_role: Optional[Union[str, "CreditEnum"]] = None
    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.applies_to_person):
            self.MissingRequiredField("applies_to_person")
        if not isinstance(self.applies_to_person, PersonValue):
            self.applies_to_person = PersonValue(**as_dict(self.applies_to_person))

        if self._is_empty(self.applied_roles):
            self.MissingRequiredField("applied_roles")
        if not isinstance(self.applied_roles, list):
            self.applied_roles = [self.applied_roles] if self.applied_roles is not None else []
        self.applied_roles = [v if isinstance(v, CreditEnum) else CreditEnum(v) for v in self.applied_roles]

        if self.applied_role is not None and not isinstance(self.applied_role, CreditEnum):
            self.applied_role = CreditEnum(self.applied_role)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass
class NamedThing(YAMLRoot):
    """
    a databased entity or concept/class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.NamedThing
    class_class_curie: ClassVar[str] = "nmdc:NamedThing"
    class_name: ClassVar[str] = "named thing"
    class_model_uri: ClassVar[URIRef] = NMDC.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    alternative_identifiers: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.alternative_identifiers, list):
            self.alternative_identifiers = [self.alternative_identifiers] if self.alternative_identifiers is not None else []
        self.alternative_identifiers = [v if isinstance(v, str) else str(v) for v in self.alternative_identifiers]

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
    name: str = None
    description: str = None
    file_size_bytes: Optional[int] = None
    md5_checksum: Optional[str] = None
    data_object_type: Optional[Union[str, "FileTypeEnum"]] = None
    compression_type: Optional[str] = None
    was_generated_by: Optional[Union[str, ActivityId]] = None
    url: Optional[str] = None
    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataObjectId):
            self.id = DataObjectId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.file_size_bytes is not None and not isinstance(self.file_size_bytes, int):
            self.file_size_bytes = int(self.file_size_bytes)

        if self.md5_checksum is not None and not isinstance(self.md5_checksum, str):
            self.md5_checksum = str(self.md5_checksum)

        if self.data_object_type is not None and not isinstance(self.data_object_type, FileTypeEnum):
            self.data_object_type = FileTypeEnum(self.data_object_type)

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
    part_of: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    env_broad_scale: Union[dict, "ControlledTermValue"] = None
    env_local_scale: Union[dict, "ControlledTermValue"] = None
    env_medium: Union[dict, "ControlledTermValue"] = None
    type: Optional[str] = None
    alternative_identifiers: Optional[Union[str, List[str]]] = empty_list()
    agrochem_addition: Optional[Union[dict, "QuantityValue"]] = None
    alkalinity: Optional[Union[dict, "QuantityValue"]] = None
    alkalinity_method: Optional[Union[dict, "TextValue"]] = None
    alkyl_diethers: Optional[Union[dict, "QuantityValue"]] = None
    alt: Optional[Union[dict, "QuantityValue"]] = None
    al_sat: Optional[Union[dict, "QuantityValue"]] = None
    al_sat_meth: Optional[Union[dict, "TextValue"]] = None
    aminopept_act: Optional[Union[dict, "QuantityValue"]] = None
    ammonium: Optional[Union[dict, "QuantityValue"]] = None
    annual_precpt: Optional[Union[dict, "QuantityValue"]] = None
    annual_temp: Optional[Union[dict, "QuantityValue"]] = None
    bacteria_carb_prod: Optional[Union[dict, "QuantityValue"]] = None
    bishomohopanol: Optional[Union[dict, "QuantityValue"]] = None
    bromide: Optional[Union[dict, "QuantityValue"]] = None
    calcium: Optional[Union[dict, "QuantityValue"]] = None
    carb_nitro_ratio: Optional[Union[dict, "QuantityValue"]] = None
    chem_administration: Optional[Union[dict, "ControlledTermValue"]] = None
    chloride: Optional[Union[dict, "QuantityValue"]] = None
    chlorophyll: Optional[Union[dict, "QuantityValue"]] = None
    collection_date: Optional[Union[dict, "TimestampValue"]] = None
    cur_land_use: Optional[Union[dict, "TextValue"]] = None
    cur_vegetation: Optional[Union[dict, "TextValue"]] = None
    cur_vegetation_meth: Optional[Union[dict, "TextValue"]] = None
    crop_rotation: Optional[Union[dict, "TextValue"]] = None
    density: Optional[Union[dict, "QuantityValue"]] = None
    depth: Optional[Union[dict, "QuantityValue"]] = None
    diss_carb_dioxide: Optional[Union[dict, "QuantityValue"]] = None
    diss_hydrogen: Optional[Union[dict, "QuantityValue"]] = None
    diss_inorg_carb: Optional[Union[dict, "QuantityValue"]] = None
    diss_inorg_phosp: Optional[Union[dict, "QuantityValue"]] = None
    diss_org_carb: Optional[Union[dict, "QuantityValue"]] = None
    diss_org_nitro: Optional[Union[dict, "QuantityValue"]] = None
    diss_oxygen: Optional[Union[dict, "QuantityValue"]] = None
    drainage_class: Optional[Union[dict, "TextValue"]] = None
    elev: Optional[Union[dict, "QuantityValue"]] = None
    env_package: Optional[Union[dict, "TextValue"]] = None
    extreme_event: Optional[Union[dict, "TimestampValue"]] = None
    fao_class: Optional[Union[dict, "TextValue"]] = None
    fire: Optional[Union[dict, "TimestampValue"]] = None
    flooding: Optional[Union[dict, "TimestampValue"]] = None
    geo_loc_name: Optional[Union[dict, "TextValue"]] = None
    glucosidase_act: Optional[Union[dict, "QuantityValue"]] = None
    heavy_metals: Optional[Union[dict, "QuantityValue"]] = None
    heavy_metals_meth: Optional[Union[dict, "TextValue"]] = None
    horizon: Optional[Union[dict, "TextValue"]] = None
    horizon_meth: Optional[Union[dict, "TextValue"]] = None
    lat_lon: Optional[Union[dict, "GeolocationValue"]] = None
    link_addit_analys: Optional[Union[dict, "TextValue"]] = None
    link_class_info: Optional[Union[dict, "TextValue"]] = None
    link_climate_info: Optional[Union[dict, "TextValue"]] = None
    local_class: Optional[Union[dict, "TextValue"]] = None
    local_class_meth: Optional[Union[dict, "TextValue"]] = None
    magnesium: Optional[Union[dict, "QuantityValue"]] = None
    mean_frict_vel: Optional[Union[dict, "QuantityValue"]] = None
    mean_peak_frict_vel: Optional[Union[dict, "QuantityValue"]] = None
    microbial_biomass: Optional[Union[dict, "QuantityValue"]] = None
    microbial_biomass_meth: Optional[Union[dict, "TextValue"]] = None
    misc_param: Optional[Union[dict, "QuantityValue"]] = None
    n_alkanes: Optional[Union[dict, "QuantityValue"]] = None
    nitrate: Optional[Union[dict, "QuantityValue"]] = None
    nitrite: Optional[Union[dict, "QuantityValue"]] = None
    org_matter: Optional[Union[dict, "QuantityValue"]] = None
    org_nitro: Optional[Union[dict, "QuantityValue"]] = None
    organism_count: Optional[Union[dict, "QuantityValue"]] = None
    oxy_stat_samp: Optional[Union[dict, "TextValue"]] = None
    part_org_carb: Optional[Union[dict, "QuantityValue"]] = None
    perturbation: Optional[Union[dict, "TextValue"]] = None
    petroleum_hydrocarb: Optional[Union[dict, "QuantityValue"]] = None
    ph: Optional[Union[dict, "QuantityValue"]] = None
    ph_meth: Optional[Union[dict, "TextValue"]] = None
    phaeopigments: Optional[Union[dict, "QuantityValue"]] = None
    phosplipid_fatt_acid: Optional[Union[dict, "QuantityValue"]] = None
    pool_dna_extracts: Optional[Union[dict, "TextValue"]] = None
    potassium: Optional[Union[dict, "QuantityValue"]] = None
    pressure: Optional[Union[dict, "QuantityValue"]] = None
    previous_land_use: Optional[Union[dict, "TextValue"]] = None
    previous_land_use_meth: Optional[Union[dict, "TextValue"]] = None
    profile_position: Optional[Union[dict, "TextValue"]] = None
    redox_potential: Optional[Union[dict, "QuantityValue"]] = None
    salinity: Optional[Union[dict, "QuantityValue"]] = None
    salinity_meth: Optional[Union[dict, "TextValue"]] = None
    samp_collect_device: Optional[Union[dict, "TextValue"]] = None
    samp_mat_process: Optional[Union[dict, "ControlledTermValue"]] = None
    samp_store_dur: Optional[Union[dict, "TextValue"]] = None
    samp_store_loc: Optional[Union[dict, "TextValue"]] = None
    samp_store_temp: Optional[Union[dict, "QuantityValue"]] = None
    samp_vol_we_dna_ext: Optional[Union[dict, "QuantityValue"]] = None
    season_temp: Optional[Union[dict, "QuantityValue"]] = None
    season_precpt: Optional[Union[dict, "QuantityValue"]] = None
    sieving: Optional[Union[dict, "QuantityValue"]] = None
    size_frac_low: Optional[Union[dict, "QuantityValue"]] = None
    size_frac_up: Optional[Union[dict, "QuantityValue"]] = None
    slope_gradient: Optional[Union[dict, "QuantityValue"]] = None
    slope_aspect: Optional[Union[dict, "QuantityValue"]] = None
    sodium: Optional[Union[dict, "QuantityValue"]] = None
    soil_type: Optional[Union[dict, "TextValue"]] = None
    soil_type_meth: Optional[Union[dict, "TextValue"]] = None
    store_cond: Optional[Union[dict, "TextValue"]] = None
    sulfate: Optional[Union[dict, "QuantityValue"]] = None
    sulfide: Optional[Union[dict, "QuantityValue"]] = None
    temp: Optional[Union[dict, "QuantityValue"]] = None
    texture: Optional[Union[dict, "QuantityValue"]] = None
    texture_meth: Optional[Union[dict, "TextValue"]] = None
    tillage: Optional[Union[dict, "TextValue"]] = None
    tidal_stage: Optional[Union[dict, "TextValue"]] = None
    tot_carb: Optional[Union[dict, "QuantityValue"]] = None
    tot_depth_water_col: Optional[Union[dict, "QuantityValue"]] = None
    tot_diss_nitro: Optional[Union[dict, "QuantityValue"]] = None
    tot_org_carb: Optional[Union[dict, "QuantityValue"]] = None
    tot_org_c_meth: Optional[Union[dict, "TextValue"]] = None
    tot_nitro_content: Optional[Union[dict, "QuantityValue"]] = None
    tot_phosp: Optional[Union[dict, "QuantityValue"]] = None
    water_content: Optional[Union[dict, "QuantityValue"]] = None
    ecosystem: Optional[str] = None
    ecosystem_category: Optional[str] = None
    ecosystem_type: Optional[str] = None
    ecosystem_subtype: Optional[str] = None
    specific_ecosystem: Optional[str] = None
    add_date: Optional[str] = None
    community: Optional[str] = None
    depth2: Optional[Union[dict, "QuantityValue"]] = None
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
    subsurface_depth: Optional[Union[dict, "QuantityValue"]] = None
    subsurface_depth2: Optional[Union[dict, "QuantityValue"]] = None
    GOLD_sample_identifiers: Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]] = empty_list()
    INSDC_biosample_identifiers: Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]] = empty_list()
    INSDC_secondary_sample_identifiers: Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]] = empty_list()
    tot_nitro_cont_meth: Optional[str] = None
    water_cont_soil_meth: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiosampleId):
            self.id = BiosampleId(self.id)

        if self._is_empty(self.part_of):
            self.MissingRequiredField("part_of")
        if not isinstance(self.part_of, list):
            self.part_of = [self.part_of] if self.part_of is not None else []
        self.part_of = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.part_of]

        if self._is_empty(self.env_broad_scale):
            self.MissingRequiredField("env_broad_scale")
        if not isinstance(self.env_broad_scale, ControlledTermValue):
            self.env_broad_scale = ControlledTermValue(**as_dict(self.env_broad_scale))

        if self._is_empty(self.env_local_scale):
            self.MissingRequiredField("env_local_scale")
        if not isinstance(self.env_local_scale, ControlledTermValue):
            self.env_local_scale = ControlledTermValue(**as_dict(self.env_local_scale))

        if self._is_empty(self.env_medium):
            self.MissingRequiredField("env_medium")
        if not isinstance(self.env_medium, ControlledTermValue):
            self.env_medium = ControlledTermValue(**as_dict(self.env_medium))

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.alternative_identifiers, list):
            self.alternative_identifiers = [self.alternative_identifiers] if self.alternative_identifiers is not None else []
        self.alternative_identifiers = [v if isinstance(v, str) else str(v) for v in self.alternative_identifiers]

        if self.agrochem_addition is not None and not isinstance(self.agrochem_addition, QuantityValue):
            self.agrochem_addition = QuantityValue(**as_dict(self.agrochem_addition))

        if self.alkalinity is not None and not isinstance(self.alkalinity, QuantityValue):
            self.alkalinity = QuantityValue(**as_dict(self.alkalinity))

        if self.alkalinity_method is not None and not isinstance(self.alkalinity_method, TextValue):
            self.alkalinity_method = TextValue(**as_dict(self.alkalinity_method))

        if self.alkyl_diethers is not None and not isinstance(self.alkyl_diethers, QuantityValue):
            self.alkyl_diethers = QuantityValue(**as_dict(self.alkyl_diethers))

        if self.alt is not None and not isinstance(self.alt, QuantityValue):
            self.alt = QuantityValue(**as_dict(self.alt))

        if self.al_sat is not None and not isinstance(self.al_sat, QuantityValue):
            self.al_sat = QuantityValue(**as_dict(self.al_sat))

        if self.al_sat_meth is not None and not isinstance(self.al_sat_meth, TextValue):
            self.al_sat_meth = TextValue(**as_dict(self.al_sat_meth))

        if self.aminopept_act is not None and not isinstance(self.aminopept_act, QuantityValue):
            self.aminopept_act = QuantityValue(**as_dict(self.aminopept_act))

        if self.ammonium is not None and not isinstance(self.ammonium, QuantityValue):
            self.ammonium = QuantityValue(**as_dict(self.ammonium))

        if self.annual_precpt is not None and not isinstance(self.annual_precpt, QuantityValue):
            self.annual_precpt = QuantityValue(**as_dict(self.annual_precpt))

        if self.annual_temp is not None and not isinstance(self.annual_temp, QuantityValue):
            self.annual_temp = QuantityValue(**as_dict(self.annual_temp))

        if self.bacteria_carb_prod is not None and not isinstance(self.bacteria_carb_prod, QuantityValue):
            self.bacteria_carb_prod = QuantityValue(**as_dict(self.bacteria_carb_prod))

        if self.bishomohopanol is not None and not isinstance(self.bishomohopanol, QuantityValue):
            self.bishomohopanol = QuantityValue(**as_dict(self.bishomohopanol))

        if self.bromide is not None and not isinstance(self.bromide, QuantityValue):
            self.bromide = QuantityValue(**as_dict(self.bromide))

        if self.calcium is not None and not isinstance(self.calcium, QuantityValue):
            self.calcium = QuantityValue(**as_dict(self.calcium))

        if self.carb_nitro_ratio is not None and not isinstance(self.carb_nitro_ratio, QuantityValue):
            self.carb_nitro_ratio = QuantityValue(**as_dict(self.carb_nitro_ratio))

        if self.chem_administration is not None and not isinstance(self.chem_administration, ControlledTermValue):
            self.chem_administration = ControlledTermValue(**as_dict(self.chem_administration))

        if self.chloride is not None and not isinstance(self.chloride, QuantityValue):
            self.chloride = QuantityValue(**as_dict(self.chloride))

        if self.chlorophyll is not None and not isinstance(self.chlorophyll, QuantityValue):
            self.chlorophyll = QuantityValue(**as_dict(self.chlorophyll))

        if self.collection_date is not None and not isinstance(self.collection_date, TimestampValue):
            self.collection_date = TimestampValue(**as_dict(self.collection_date))

        if self.cur_land_use is not None and not isinstance(self.cur_land_use, TextValue):
            self.cur_land_use = TextValue(**as_dict(self.cur_land_use))

        if self.cur_vegetation is not None and not isinstance(self.cur_vegetation, TextValue):
            self.cur_vegetation = TextValue(**as_dict(self.cur_vegetation))

        if self.cur_vegetation_meth is not None and not isinstance(self.cur_vegetation_meth, TextValue):
            self.cur_vegetation_meth = TextValue(**as_dict(self.cur_vegetation_meth))

        if self.crop_rotation is not None and not isinstance(self.crop_rotation, TextValue):
            self.crop_rotation = TextValue(**as_dict(self.crop_rotation))

        if self.density is not None and not isinstance(self.density, QuantityValue):
            self.density = QuantityValue(**as_dict(self.density))

        if self.depth is not None and not isinstance(self.depth, QuantityValue):
            self.depth = QuantityValue(**as_dict(self.depth))

        if self.diss_carb_dioxide is not None and not isinstance(self.diss_carb_dioxide, QuantityValue):
            self.diss_carb_dioxide = QuantityValue(**as_dict(self.diss_carb_dioxide))

        if self.diss_hydrogen is not None and not isinstance(self.diss_hydrogen, QuantityValue):
            self.diss_hydrogen = QuantityValue(**as_dict(self.diss_hydrogen))

        if self.diss_inorg_carb is not None and not isinstance(self.diss_inorg_carb, QuantityValue):
            self.diss_inorg_carb = QuantityValue(**as_dict(self.diss_inorg_carb))

        if self.diss_inorg_phosp is not None and not isinstance(self.diss_inorg_phosp, QuantityValue):
            self.diss_inorg_phosp = QuantityValue(**as_dict(self.diss_inorg_phosp))

        if self.diss_org_carb is not None and not isinstance(self.diss_org_carb, QuantityValue):
            self.diss_org_carb = QuantityValue(**as_dict(self.diss_org_carb))

        if self.diss_org_nitro is not None and not isinstance(self.diss_org_nitro, QuantityValue):
            self.diss_org_nitro = QuantityValue(**as_dict(self.diss_org_nitro))

        if self.diss_oxygen is not None and not isinstance(self.diss_oxygen, QuantityValue):
            self.diss_oxygen = QuantityValue(**as_dict(self.diss_oxygen))

        if self.drainage_class is not None and not isinstance(self.drainage_class, TextValue):
            self.drainage_class = TextValue(**as_dict(self.drainage_class))

        if self.elev is not None and not isinstance(self.elev, QuantityValue):
            self.elev = QuantityValue(**as_dict(self.elev))

        if self.env_package is not None and not isinstance(self.env_package, TextValue):
            self.env_package = TextValue(**as_dict(self.env_package))

        if self.extreme_event is not None and not isinstance(self.extreme_event, TimestampValue):
            self.extreme_event = TimestampValue(**as_dict(self.extreme_event))

        if self.fao_class is not None and not isinstance(self.fao_class, TextValue):
            self.fao_class = TextValue(**as_dict(self.fao_class))

        if self.fire is not None and not isinstance(self.fire, TimestampValue):
            self.fire = TimestampValue(**as_dict(self.fire))

        if self.flooding is not None and not isinstance(self.flooding, TimestampValue):
            self.flooding = TimestampValue(**as_dict(self.flooding))

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, TextValue):
            self.geo_loc_name = TextValue(**as_dict(self.geo_loc_name))

        if self.glucosidase_act is not None and not isinstance(self.glucosidase_act, QuantityValue):
            self.glucosidase_act = QuantityValue(**as_dict(self.glucosidase_act))

        if self.heavy_metals is not None and not isinstance(self.heavy_metals, QuantityValue):
            self.heavy_metals = QuantityValue(**as_dict(self.heavy_metals))

        if self.heavy_metals_meth is not None and not isinstance(self.heavy_metals_meth, TextValue):
            self.heavy_metals_meth = TextValue(**as_dict(self.heavy_metals_meth))

        if self.horizon is not None and not isinstance(self.horizon, TextValue):
            self.horizon = TextValue(**as_dict(self.horizon))

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, TextValue):
            self.horizon_meth = TextValue(**as_dict(self.horizon_meth))

        if self.lat_lon is not None and not isinstance(self.lat_lon, GeolocationValue):
            self.lat_lon = GeolocationValue(**as_dict(self.lat_lon))

        if self.link_addit_analys is not None and not isinstance(self.link_addit_analys, TextValue):
            self.link_addit_analys = TextValue(**as_dict(self.link_addit_analys))

        if self.link_class_info is not None and not isinstance(self.link_class_info, TextValue):
            self.link_class_info = TextValue(**as_dict(self.link_class_info))

        if self.link_climate_info is not None and not isinstance(self.link_climate_info, TextValue):
            self.link_climate_info = TextValue(**as_dict(self.link_climate_info))

        if self.local_class is not None and not isinstance(self.local_class, TextValue):
            self.local_class = TextValue(**as_dict(self.local_class))

        if self.local_class_meth is not None and not isinstance(self.local_class_meth, TextValue):
            self.local_class_meth = TextValue(**as_dict(self.local_class_meth))

        if self.magnesium is not None and not isinstance(self.magnesium, QuantityValue):
            self.magnesium = QuantityValue(**as_dict(self.magnesium))

        if self.mean_frict_vel is not None and not isinstance(self.mean_frict_vel, QuantityValue):
            self.mean_frict_vel = QuantityValue(**as_dict(self.mean_frict_vel))

        if self.mean_peak_frict_vel is not None and not isinstance(self.mean_peak_frict_vel, QuantityValue):
            self.mean_peak_frict_vel = QuantityValue(**as_dict(self.mean_peak_frict_vel))

        if self.microbial_biomass is not None and not isinstance(self.microbial_biomass, QuantityValue):
            self.microbial_biomass = QuantityValue(**as_dict(self.microbial_biomass))

        if self.microbial_biomass_meth is not None and not isinstance(self.microbial_biomass_meth, TextValue):
            self.microbial_biomass_meth = TextValue(**as_dict(self.microbial_biomass_meth))

        if self.misc_param is not None and not isinstance(self.misc_param, QuantityValue):
            self.misc_param = QuantityValue(**as_dict(self.misc_param))

        if self.n_alkanes is not None and not isinstance(self.n_alkanes, QuantityValue):
            self.n_alkanes = QuantityValue(**as_dict(self.n_alkanes))

        if self.nitrate is not None and not isinstance(self.nitrate, QuantityValue):
            self.nitrate = QuantityValue(**as_dict(self.nitrate))

        if self.nitrite is not None and not isinstance(self.nitrite, QuantityValue):
            self.nitrite = QuantityValue(**as_dict(self.nitrite))

        if self.org_matter is not None and not isinstance(self.org_matter, QuantityValue):
            self.org_matter = QuantityValue(**as_dict(self.org_matter))

        if self.org_nitro is not None and not isinstance(self.org_nitro, QuantityValue):
            self.org_nitro = QuantityValue(**as_dict(self.org_nitro))

        if self.organism_count is not None and not isinstance(self.organism_count, QuantityValue):
            self.organism_count = QuantityValue(**as_dict(self.organism_count))

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, TextValue):
            self.oxy_stat_samp = TextValue(**as_dict(self.oxy_stat_samp))

        if self.part_org_carb is not None and not isinstance(self.part_org_carb, QuantityValue):
            self.part_org_carb = QuantityValue(**as_dict(self.part_org_carb))

        if self.perturbation is not None and not isinstance(self.perturbation, TextValue):
            self.perturbation = TextValue(**as_dict(self.perturbation))

        if self.petroleum_hydrocarb is not None and not isinstance(self.petroleum_hydrocarb, QuantityValue):
            self.petroleum_hydrocarb = QuantityValue(**as_dict(self.petroleum_hydrocarb))

        if self.ph is not None and not isinstance(self.ph, QuantityValue):
            self.ph = QuantityValue(**as_dict(self.ph))

        if self.ph_meth is not None and not isinstance(self.ph_meth, TextValue):
            self.ph_meth = TextValue(**as_dict(self.ph_meth))

        if self.phaeopigments is not None and not isinstance(self.phaeopigments, QuantityValue):
            self.phaeopigments = QuantityValue(**as_dict(self.phaeopigments))

        if self.phosplipid_fatt_acid is not None and not isinstance(self.phosplipid_fatt_acid, QuantityValue):
            self.phosplipid_fatt_acid = QuantityValue(**as_dict(self.phosplipid_fatt_acid))

        if self.pool_dna_extracts is not None and not isinstance(self.pool_dna_extracts, TextValue):
            self.pool_dna_extracts = TextValue(**as_dict(self.pool_dna_extracts))

        if self.potassium is not None and not isinstance(self.potassium, QuantityValue):
            self.potassium = QuantityValue(**as_dict(self.potassium))

        if self.pressure is not None and not isinstance(self.pressure, QuantityValue):
            self.pressure = QuantityValue(**as_dict(self.pressure))

        if self.previous_land_use is not None and not isinstance(self.previous_land_use, TextValue):
            self.previous_land_use = TextValue(**as_dict(self.previous_land_use))

        if self.previous_land_use_meth is not None and not isinstance(self.previous_land_use_meth, TextValue):
            self.previous_land_use_meth = TextValue(**as_dict(self.previous_land_use_meth))

        if self.profile_position is not None and not isinstance(self.profile_position, TextValue):
            self.profile_position = TextValue(**as_dict(self.profile_position))

        if self.redox_potential is not None and not isinstance(self.redox_potential, QuantityValue):
            self.redox_potential = QuantityValue(**as_dict(self.redox_potential))

        if self.salinity is not None and not isinstance(self.salinity, QuantityValue):
            self.salinity = QuantityValue(**as_dict(self.salinity))

        if self.salinity_meth is not None and not isinstance(self.salinity_meth, TextValue):
            self.salinity_meth = TextValue(**as_dict(self.salinity_meth))

        if self.samp_collect_device is not None and not isinstance(self.samp_collect_device, TextValue):
            self.samp_collect_device = TextValue(**as_dict(self.samp_collect_device))

        if self.samp_mat_process is not None and not isinstance(self.samp_mat_process, ControlledTermValue):
            self.samp_mat_process = ControlledTermValue(**as_dict(self.samp_mat_process))

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, TextValue):
            self.samp_store_dur = TextValue(**as_dict(self.samp_store_dur))

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, TextValue):
            self.samp_store_loc = TextValue(**as_dict(self.samp_store_loc))

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, QuantityValue):
            self.samp_store_temp = QuantityValue(**as_dict(self.samp_store_temp))

        if self.samp_vol_we_dna_ext is not None and not isinstance(self.samp_vol_we_dna_ext, QuantityValue):
            self.samp_vol_we_dna_ext = QuantityValue(**as_dict(self.samp_vol_we_dna_ext))

        if self.season_temp is not None and not isinstance(self.season_temp, QuantityValue):
            self.season_temp = QuantityValue(**as_dict(self.season_temp))

        if self.season_precpt is not None and not isinstance(self.season_precpt, QuantityValue):
            self.season_precpt = QuantityValue(**as_dict(self.season_precpt))

        if self.sieving is not None and not isinstance(self.sieving, QuantityValue):
            self.sieving = QuantityValue(**as_dict(self.sieving))

        if self.size_frac_low is not None and not isinstance(self.size_frac_low, QuantityValue):
            self.size_frac_low = QuantityValue(**as_dict(self.size_frac_low))

        if self.size_frac_up is not None and not isinstance(self.size_frac_up, QuantityValue):
            self.size_frac_up = QuantityValue(**as_dict(self.size_frac_up))

        if self.slope_gradient is not None and not isinstance(self.slope_gradient, QuantityValue):
            self.slope_gradient = QuantityValue(**as_dict(self.slope_gradient))

        if self.slope_aspect is not None and not isinstance(self.slope_aspect, QuantityValue):
            self.slope_aspect = QuantityValue(**as_dict(self.slope_aspect))

        if self.sodium is not None and not isinstance(self.sodium, QuantityValue):
            self.sodium = QuantityValue(**as_dict(self.sodium))

        if self.soil_type is not None and not isinstance(self.soil_type, TextValue):
            self.soil_type = TextValue(**as_dict(self.soil_type))

        if self.soil_type_meth is not None and not isinstance(self.soil_type_meth, TextValue):
            self.soil_type_meth = TextValue(**as_dict(self.soil_type_meth))

        if self.store_cond is not None and not isinstance(self.store_cond, TextValue):
            self.store_cond = TextValue(**as_dict(self.store_cond))

        if self.sulfate is not None and not isinstance(self.sulfate, QuantityValue):
            self.sulfate = QuantityValue(**as_dict(self.sulfate))

        if self.sulfide is not None and not isinstance(self.sulfide, QuantityValue):
            self.sulfide = QuantityValue(**as_dict(self.sulfide))

        if self.temp is not None and not isinstance(self.temp, QuantityValue):
            self.temp = QuantityValue(**as_dict(self.temp))

        if self.texture is not None and not isinstance(self.texture, QuantityValue):
            self.texture = QuantityValue(**as_dict(self.texture))

        if self.texture_meth is not None and not isinstance(self.texture_meth, TextValue):
            self.texture_meth = TextValue(**as_dict(self.texture_meth))

        if self.tillage is not None and not isinstance(self.tillage, TextValue):
            self.tillage = TextValue(**as_dict(self.tillage))

        if self.tidal_stage is not None and not isinstance(self.tidal_stage, TextValue):
            self.tidal_stage = TextValue(**as_dict(self.tidal_stage))

        if self.tot_carb is not None and not isinstance(self.tot_carb, QuantityValue):
            self.tot_carb = QuantityValue(**as_dict(self.tot_carb))

        if self.tot_depth_water_col is not None and not isinstance(self.tot_depth_water_col, QuantityValue):
            self.tot_depth_water_col = QuantityValue(**as_dict(self.tot_depth_water_col))

        if self.tot_diss_nitro is not None and not isinstance(self.tot_diss_nitro, QuantityValue):
            self.tot_diss_nitro = QuantityValue(**as_dict(self.tot_diss_nitro))

        if self.tot_org_carb is not None and not isinstance(self.tot_org_carb, QuantityValue):
            self.tot_org_carb = QuantityValue(**as_dict(self.tot_org_carb))

        if self.tot_org_c_meth is not None and not isinstance(self.tot_org_c_meth, TextValue):
            self.tot_org_c_meth = TextValue(**as_dict(self.tot_org_c_meth))

        if self.tot_nitro_content is not None and not isinstance(self.tot_nitro_content, QuantityValue):
            self.tot_nitro_content = QuantityValue(**as_dict(self.tot_nitro_content))

        if self.tot_phosp is not None and not isinstance(self.tot_phosp, QuantityValue):
            self.tot_phosp = QuantityValue(**as_dict(self.tot_phosp))

        if self.water_content is not None and not isinstance(self.water_content, QuantityValue):
            self.water_content = QuantityValue(**as_dict(self.water_content))

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

        if self.depth2 is not None and not isinstance(self.depth2, QuantityValue):
            self.depth2 = QuantityValue(**as_dict(self.depth2))

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
            self.subsurface_depth = QuantityValue(**as_dict(self.subsurface_depth))

        if self.subsurface_depth2 is not None and not isinstance(self.subsurface_depth2, QuantityValue):
            self.subsurface_depth2 = QuantityValue(**as_dict(self.subsurface_depth2))

        if not isinstance(self.GOLD_sample_identifiers, list):
            self.GOLD_sample_identifiers = [self.GOLD_sample_identifiers] if self.GOLD_sample_identifiers is not None else []
        self.GOLD_sample_identifiers = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(v) for v in self.GOLD_sample_identifiers]

        if not isinstance(self.INSDC_biosample_identifiers, list):
            self.INSDC_biosample_identifiers = [self.INSDC_biosample_identifiers] if self.INSDC_biosample_identifiers is not None else []
        self.INSDC_biosample_identifiers = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(v) for v in self.INSDC_biosample_identifiers]

        if not isinstance(self.INSDC_secondary_sample_identifiers, list):
            self.INSDC_secondary_sample_identifiers = [self.INSDC_secondary_sample_identifiers] if self.INSDC_secondary_sample_identifiers is not None else []
        self.INSDC_secondary_sample_identifiers = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(v) for v in self.INSDC_secondary_sample_identifiers]

        if self.tot_nitro_cont_meth is not None and not isinstance(self.tot_nitro_cont_meth, str):
            self.tot_nitro_cont_meth = str(self.tot_nitro_cont_meth)

        if self.water_cont_soil_meth is not None and not isinstance(self.water_cont_soil_meth, str):
            self.water_cont_soil_meth = str(self.water_cont_soil_meth)

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
    principal_investigator: Optional[Union[dict, "PersonValue"]] = None
    doi: Optional[Union[dict, "AttributeValue"]] = None
    title: Optional[str] = None
    alternative_titles: Optional[Union[str, List[str]]] = empty_list()
    alternative_descriptions: Optional[Union[str, List[str]]] = empty_list()
    alternative_names: Optional[Union[str, List[str]]] = empty_list()
    abstract: Optional[str] = None
    objective: Optional[str] = None
    websites: Optional[Union[str, List[str]]] = empty_list()
    publications: Optional[Union[str, List[str]]] = empty_list()
    ess_dive_datasets: Optional[Union[str, List[str]]] = empty_list()
    type: Optional[str] = None
    relevant_protocols: Optional[Union[str, List[str]]] = empty_list()
    funding_sources: Optional[Union[str, List[str]]] = empty_list()
    INSDC_bioproject_identifiers: Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]] = empty_list()
    INSDC_SRA_ENA_study_identifiers: Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]] = empty_list()
    GOLD_study_identifiers: Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]] = empty_list()
    MGnify_project_identifiers: Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]] = empty_list()
    has_credit_associations: Optional[Union[Union[dict, "CreditAssociation"], List[Union[dict, "CreditAssociation"]]]] = empty_list()
    study_image: Optional[Union[Union[dict, "ImageValue"], List[Union[dict, "ImageValue"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
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

        if self.principal_investigator is not None and not isinstance(self.principal_investigator, PersonValue):
            self.principal_investigator = PersonValue(**as_dict(self.principal_investigator))

        if self.doi is not None and not isinstance(self.doi, AttributeValue):
            self.doi = AttributeValue(**as_dict(self.doi))

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.alternative_titles, list):
            self.alternative_titles = [self.alternative_titles] if self.alternative_titles is not None else []
        self.alternative_titles = [v if isinstance(v, str) else str(v) for v in self.alternative_titles]

        if not isinstance(self.alternative_descriptions, list):
            self.alternative_descriptions = [self.alternative_descriptions] if self.alternative_descriptions is not None else []
        self.alternative_descriptions = [v if isinstance(v, str) else str(v) for v in self.alternative_descriptions]

        if not isinstance(self.alternative_names, list):
            self.alternative_names = [self.alternative_names] if self.alternative_names is not None else []
        self.alternative_names = [v if isinstance(v, str) else str(v) for v in self.alternative_names]

        if self.abstract is not None and not isinstance(self.abstract, str):
            self.abstract = str(self.abstract)

        if self.objective is not None and not isinstance(self.objective, str):
            self.objective = str(self.objective)

        if not isinstance(self.websites, list):
            self.websites = [self.websites] if self.websites is not None else []
        self.websites = [v if isinstance(v, str) else str(v) for v in self.websites]

        if not isinstance(self.publications, list):
            self.publications = [self.publications] if self.publications is not None else []
        self.publications = [v if isinstance(v, str) else str(v) for v in self.publications]

        if not isinstance(self.ess_dive_datasets, list):
            self.ess_dive_datasets = [self.ess_dive_datasets] if self.ess_dive_datasets is not None else []
        self.ess_dive_datasets = [v if isinstance(v, str) else str(v) for v in self.ess_dive_datasets]

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.relevant_protocols, list):
            self.relevant_protocols = [self.relevant_protocols] if self.relevant_protocols is not None else []
        self.relevant_protocols = [v if isinstance(v, str) else str(v) for v in self.relevant_protocols]

        if not isinstance(self.funding_sources, list):
            self.funding_sources = [self.funding_sources] if self.funding_sources is not None else []
        self.funding_sources = [v if isinstance(v, str) else str(v) for v in self.funding_sources]

        if not isinstance(self.INSDC_bioproject_identifiers, list):
            self.INSDC_bioproject_identifiers = [self.INSDC_bioproject_identifiers] if self.INSDC_bioproject_identifiers is not None else []
        self.INSDC_bioproject_identifiers = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(v) for v in self.INSDC_bioproject_identifiers]

        if not isinstance(self.INSDC_SRA_ENA_study_identifiers, list):
            self.INSDC_SRA_ENA_study_identifiers = [self.INSDC_SRA_ENA_study_identifiers] if self.INSDC_SRA_ENA_study_identifiers is not None else []
        self.INSDC_SRA_ENA_study_identifiers = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(v) for v in self.INSDC_SRA_ENA_study_identifiers]

        if not isinstance(self.GOLD_study_identifiers, list):
            self.GOLD_study_identifiers = [self.GOLD_study_identifiers] if self.GOLD_study_identifiers is not None else []
        self.GOLD_study_identifiers = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(v) for v in self.GOLD_study_identifiers]

        if not isinstance(self.MGnify_project_identifiers, list):
            self.MGnify_project_identifiers = [self.MGnify_project_identifiers] if self.MGnify_project_identifiers is not None else []
        self.MGnify_project_identifiers = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(v) for v in self.MGnify_project_identifiers]

        self._normalize_inlined_as_dict(slot_name="has_credit_associations", slot_type=CreditAssociation, key_name="applies to person", keyed=False)

        if not isinstance(self.study_image, list):
            self.study_image = [self.study_image] if self.study_image is not None else []
        self.study_image = [v if isinstance(v, ImageValue) else ImageValue(**as_dict(v)) for v in self.study_image]

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
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiosampleProcessingId):
            self.id = BiosampleProcessingId(self.id)

        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
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
    omics_type: Optional[Union[dict, "ControlledTermValue"]] = None
    part_of: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()
    principal_investigator: Optional[Union[dict, "PersonValue"]] = None
    processing_institution: Optional[str] = None
    type: Optional[str] = None
    GOLD_sequencing_project_identifiers: Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]] = empty_list()
    INSDC_experiment_identifiers: Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]] = empty_list()
    samp_vol_we_dna_ext: Optional[Union[dict, "QuantityValue"]] = None
    nucl_acid_ext: Optional[Union[dict, "TextValue"]] = None
    nucl_acid_amp: Optional[Union[dict, "TextValue"]] = None
    target_gene: Optional[Union[dict, "TextValue"]] = None
    target_subfragment: Optional[Union[dict, "TextValue"]] = None
    pcr_primers: Optional[Union[dict, "TextValue"]] = None
    pcr_cond: Optional[Union[dict, "TextValue"]] = None
    seq_meth: Optional[Union[dict, "TextValue"]] = None
    seq_quality_check: Optional[Union[dict, "TextValue"]] = None
    chimera_check: Optional[Union[dict, "TextValue"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OmicsProcessingId):
            self.id = OmicsProcessingId(self.id)

        if self._is_empty(self.has_input):
            self.MissingRequiredField("has_input")
        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
        self.has_input = [v if isinstance(v, BiosampleId) else BiosampleId(v) for v in self.has_input]

        if self.add_date is not None and not isinstance(self.add_date, str):
            self.add_date = str(self.add_date)

        if self.mod_date is not None and not isinstance(self.mod_date, str):
            self.mod_date = str(self.mod_date)

        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
        self.has_input = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_input]

        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output] if self.has_output is not None else []
        self.has_output = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_output]

        if self.instrument_name is not None and not isinstance(self.instrument_name, str):
            self.instrument_name = str(self.instrument_name)

        if self.ncbi_project_name is not None and not isinstance(self.ncbi_project_name, str):
            self.ncbi_project_name = str(self.ncbi_project_name)

        if self.omics_type is not None and not isinstance(self.omics_type, ControlledTermValue):
            self.omics_type = ControlledTermValue(**as_dict(self.omics_type))

        if not isinstance(self.part_of, list):
            self.part_of = [self.part_of] if self.part_of is not None else []
        self.part_of = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.part_of]

        if self.principal_investigator is not None and not isinstance(self.principal_investigator, PersonValue):
            self.principal_investigator = PersonValue(**as_dict(self.principal_investigator))

        if self.processing_institution is not None and not isinstance(self.processing_institution, str):
            self.processing_institution = str(self.processing_institution)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.GOLD_sequencing_project_identifiers, list):
            self.GOLD_sequencing_project_identifiers = [self.GOLD_sequencing_project_identifiers] if self.GOLD_sequencing_project_identifiers is not None else []
        self.GOLD_sequencing_project_identifiers = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(v) for v in self.GOLD_sequencing_project_identifiers]

        if not isinstance(self.INSDC_experiment_identifiers, list):
            self.INSDC_experiment_identifiers = [self.INSDC_experiment_identifiers] if self.INSDC_experiment_identifiers is not None else []
        self.INSDC_experiment_identifiers = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(v) for v in self.INSDC_experiment_identifiers]

        if self.samp_vol_we_dna_ext is not None and not isinstance(self.samp_vol_we_dna_ext, QuantityValue):
            self.samp_vol_we_dna_ext = QuantityValue(**as_dict(self.samp_vol_we_dna_ext))

        if self.nucl_acid_ext is not None and not isinstance(self.nucl_acid_ext, TextValue):
            self.nucl_acid_ext = TextValue(**as_dict(self.nucl_acid_ext))

        if self.nucl_acid_amp is not None and not isinstance(self.nucl_acid_amp, TextValue):
            self.nucl_acid_amp = TextValue(**as_dict(self.nucl_acid_amp))

        if self.target_gene is not None and not isinstance(self.target_gene, TextValue):
            self.target_gene = TextValue(**as_dict(self.target_gene))

        if self.target_subfragment is not None and not isinstance(self.target_subfragment, TextValue):
            self.target_subfragment = TextValue(**as_dict(self.target_subfragment))

        if self.pcr_primers is not None and not isinstance(self.pcr_primers, TextValue):
            self.pcr_primers = TextValue(**as_dict(self.pcr_primers))

        if self.pcr_cond is not None and not isinstance(self.pcr_cond, TextValue):
            self.pcr_cond = TextValue(**as_dict(self.pcr_cond))

        if self.seq_meth is not None and not isinstance(self.seq_meth, TextValue):
            self.seq_meth = TextValue(**as_dict(self.seq_meth))

        if self.seq_quality_check is not None and not isinstance(self.seq_quality_check, TextValue):
            self.seq_quality_check = TextValue(**as_dict(self.seq_quality_check))

        if self.chimera_check is not None and not isinstance(self.chimera_check, TextValue):
            self.chimera_check = TextValue(**as_dict(self.chimera_check))

        super().__post_init__(**kwargs)


@dataclass
class OntologyClass(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.OntologyClass
    class_class_curie: ClassVar[str] = "nmdc:OntologyClass"
    class_name: ClassVar[str] = "ontology class"
    class_model_uri: ClassVar[URIRef] = NMDC.OntologyClass

    id: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EnvironmentalMaterialTerm(OntologyClass):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.EnvironmentalMaterialTerm
    class_class_curie: ClassVar[str] = "nmdc:EnvironmentalMaterialTerm"
    class_name: ClassVar[str] = "environmental material term"
    class_model_uri: ClassVar[URIRef] = NMDC.EnvironmentalMaterialTerm

    id: Union[str, EnvironmentalMaterialTermId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnvironmentalMaterialTermId):
            self.id = EnvironmentalMaterialTermId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class AttributeValue(YAMLRoot):
    """
    The value for any value of a attribute for a sample. This object can hold both the un-normalized atomic value and
    the structured value
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.AttributeValue
    class_class_curie: ClassVar[str] = "nmdc:AttributeValue"
    class_name: ClassVar[str] = "attribute value"
    class_model_uri: ClassVar[URIRef] = NMDC.AttributeValue

    has_raw_value: Optional[str] = None
    was_generated_by: Optional[Union[str, ActivityId]] = None
    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_raw_value is not None and not isinstance(self.has_raw_value, str):
            self.has_raw_value = str(self.has_raw_value)

        if self.was_generated_by is not None and not isinstance(self.was_generated_by, ActivityId):
            self.was_generated_by = ActivityId(self.was_generated_by)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass
class QuantityValue(AttributeValue):
    """
    A simple quantity, e.g. 2cm
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.QuantityValue
    class_class_curie: ClassVar[str] = "nmdc:QuantityValue"
    class_name: ClassVar[str] = "quantity value"
    class_model_uri: ClassVar[URIRef] = NMDC.QuantityValue

    has_unit: Optional[str] = None
    has_numeric_value: Optional[float] = None
    has_minimum_numeric_value: Optional[float] = None
    has_maximum_numeric_value: Optional[float] = None
    has_raw_value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_unit is not None and not isinstance(self.has_unit, str):
            self.has_unit = str(self.has_unit)

        if self.has_numeric_value is not None and not isinstance(self.has_numeric_value, float):
            self.has_numeric_value = float(self.has_numeric_value)

        if self.has_minimum_numeric_value is not None and not isinstance(self.has_minimum_numeric_value, float):
            self.has_minimum_numeric_value = float(self.has_minimum_numeric_value)

        if self.has_maximum_numeric_value is not None and not isinstance(self.has_maximum_numeric_value, float):
            self.has_maximum_numeric_value = float(self.has_maximum_numeric_value)

        if self.has_raw_value is not None and not isinstance(self.has_raw_value, str):
            self.has_raw_value = str(self.has_raw_value)

        super().__post_init__(**kwargs)


@dataclass
class ImageValue(AttributeValue):
    """
    An attribute value representing an image.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.ImageValue
    class_class_curie: ClassVar[str] = "nmdc:ImageValue"
    class_name: ClassVar[str] = "image value"
    class_model_uri: ClassVar[URIRef] = NMDC.ImageValue

    url: Optional[str] = None
    description: Optional[str] = None
    display_order: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.display_order is not None and not isinstance(self.display_order, str):
            self.display_order = str(self.display_order)

        super().__post_init__(**kwargs)


@dataclass
class PersonValue(AttributeValue):
    """
    An attribute value representing a person
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.PersonValue
    class_class_curie: ClassVar[str] = "nmdc:PersonValue"
    class_name: ClassVar[str] = "person value"
    class_model_uri: ClassVar[URIRef] = NMDC.PersonValue

    orcid: Optional[str] = None
    profile_image_url: Optional[str] = None
    email: Optional[str] = None
    name: Optional[str] = None
    websites: Optional[Union[str, List[str]]] = empty_list()
    has_raw_value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.orcid is not None and not isinstance(self.orcid, str):
            self.orcid = str(self.orcid)

        if self.profile_image_url is not None and not isinstance(self.profile_image_url, str):
            self.profile_image_url = str(self.profile_image_url)

        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.websites, list):
            self.websites = [self.websites] if self.websites is not None else []
        self.websites = [v if isinstance(v, str) else str(v) for v in self.websites]

        if self.has_raw_value is not None and not isinstance(self.has_raw_value, str):
            self.has_raw_value = str(self.has_raw_value)

        super().__post_init__(**kwargs)


@dataclass
class Person(NamedThing):
    """
    represents a person, such as a researcher
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.Person
    class_class_curie: ClassVar[str] = "nmdc:Person"
    class_name: ClassVar[str] = "person"
    class_model_uri: ClassVar[URIRef] = NMDC.Person

    id: Union[str, PersonId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MAGBin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.MAGBin
    class_class_curie: ClassVar[str] = "nmdc:MAGBin"
    class_name: ClassVar[str] = "MAG bin"
    class_model_uri: ClassVar[URIRef] = NMDC.MAGBin

    type: Optional[str] = None
    bin_name: Optional[str] = None
    number_of_contig: Optional[int] = None
    completeness: Optional[float] = None
    contamination: Optional[float] = None
    gene_count: Optional[int] = None
    bin_quality: Optional[str] = None
    num_16s: Optional[int] = None
    num_5s: Optional[int] = None
    num_23s: Optional[int] = None
    num_tRNA: Optional[int] = None
    gtdbtk_domain: Optional[str] = None
    gtdbtk_phylum: Optional[str] = None
    gtdbtk_class: Optional[str] = None
    gtdbtk_order: Optional[str] = None
    gtdbtk_family: Optional[str] = None
    gtdbtk_genus: Optional[str] = None
    gtdbtk_species: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.bin_name is not None and not isinstance(self.bin_name, str):
            self.bin_name = str(self.bin_name)

        if self.number_of_contig is not None and not isinstance(self.number_of_contig, int):
            self.number_of_contig = int(self.number_of_contig)

        if self.completeness is not None and not isinstance(self.completeness, float):
            self.completeness = float(self.completeness)

        if self.contamination is not None and not isinstance(self.contamination, float):
            self.contamination = float(self.contamination)

        if self.gene_count is not None and not isinstance(self.gene_count, int):
            self.gene_count = int(self.gene_count)

        if self.bin_quality is not None and not isinstance(self.bin_quality, str):
            self.bin_quality = str(self.bin_quality)

        if self.num_16s is not None and not isinstance(self.num_16s, int):
            self.num_16s = int(self.num_16s)

        if self.num_5s is not None and not isinstance(self.num_5s, int):
            self.num_5s = int(self.num_5s)

        if self.num_23s is not None and not isinstance(self.num_23s, int):
            self.num_23s = int(self.num_23s)

        if self.num_tRNA is not None and not isinstance(self.num_tRNA, int):
            self.num_tRNA = int(self.num_tRNA)

        if self.gtdbtk_domain is not None and not isinstance(self.gtdbtk_domain, str):
            self.gtdbtk_domain = str(self.gtdbtk_domain)

        if self.gtdbtk_phylum is not None and not isinstance(self.gtdbtk_phylum, str):
            self.gtdbtk_phylum = str(self.gtdbtk_phylum)

        if self.gtdbtk_class is not None and not isinstance(self.gtdbtk_class, str):
            self.gtdbtk_class = str(self.gtdbtk_class)

        if self.gtdbtk_order is not None and not isinstance(self.gtdbtk_order, str):
            self.gtdbtk_order = str(self.gtdbtk_order)

        if self.gtdbtk_family is not None and not isinstance(self.gtdbtk_family, str):
            self.gtdbtk_family = str(self.gtdbtk_family)

        if self.gtdbtk_genus is not None and not isinstance(self.gtdbtk_genus, str):
            self.gtdbtk_genus = str(self.gtdbtk_genus)

        if self.gtdbtk_species is not None and not isinstance(self.gtdbtk_species, str):
            self.gtdbtk_species = str(self.gtdbtk_species)

        super().__post_init__(**kwargs)


@dataclass
class Instrument(NamedThing):
    """
    A material entity that is designed to perform a function in a scientific investigation, but is not a reagent[OBI].
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.Instrument
    class_class_curie: ClassVar[str] = "nmdc:Instrument"
    class_name: ClassVar[str] = "instrument"
    class_model_uri: ClassVar[URIRef] = NMDC.Instrument

    id: Union[str, InstrumentId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InstrumentId):
            self.id = InstrumentId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MetaboliteQuantification(YAMLRoot):
    """
    This is used to link a metabolomics analysis workflow to a specific metabolite
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.MetaboliteQuantification
    class_class_curie: ClassVar[str] = "nmdc:MetaboliteQuantification"
    class_name: ClassVar[str] = "metabolite quantification"
    class_model_uri: ClassVar[URIRef] = NMDC.MetaboliteQuantification

    alternative_identifiers: Optional[Union[str, List[str]]] = empty_list()
    metabolite_quantified: Optional[Union[str, ChemicalEntityId]] = None
    highest_similarity_score: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.alternative_identifiers, list):
            self.alternative_identifiers = [self.alternative_identifiers] if self.alternative_identifiers is not None else []
        self.alternative_identifiers = [v if isinstance(v, str) else str(v) for v in self.alternative_identifiers]

        if self.metabolite_quantified is not None and not isinstance(self.metabolite_quantified, ChemicalEntityId):
            self.metabolite_quantified = ChemicalEntityId(self.metabolite_quantified)

        if self.highest_similarity_score is not None and not isinstance(self.highest_similarity_score, float):
            self.highest_similarity_score = float(self.highest_similarity_score)

        super().__post_init__(**kwargs)


@dataclass
class PeptideQuantification(YAMLRoot):
    """
    This is used to link a metaproteomics analysis workflow to a specific peptide sequence and related information
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.PeptideQuantification
    class_class_curie: ClassVar[str] = "nmdc:PeptideQuantification"
    class_name: ClassVar[str] = "peptide quantification"
    class_model_uri: ClassVar[URIRef] = NMDC.PeptideQuantification

    peptide_sequence: Optional[str] = None
    best_protein: Optional[Union[str, GeneProductId]] = None
    all_proteins: Optional[Union[Union[str, GeneProductId], List[Union[str, GeneProductId]]]] = empty_list()
    min_q_value: Optional[float] = None
    peptide_spectral_count: Optional[int] = None
    peptide_sum_masic_abundance: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.peptide_sequence is not None and not isinstance(self.peptide_sequence, str):
            self.peptide_sequence = str(self.peptide_sequence)

        if self.best_protein is not None and not isinstance(self.best_protein, GeneProductId):
            self.best_protein = GeneProductId(self.best_protein)

        if not isinstance(self.all_proteins, list):
            self.all_proteins = [self.all_proteins] if self.all_proteins is not None else []
        self.all_proteins = [v if isinstance(v, GeneProductId) else GeneProductId(v) for v in self.all_proteins]

        if self.min_q_value is not None and not isinstance(self.min_q_value, float):
            self.min_q_value = float(self.min_q_value)

        if self.peptide_spectral_count is not None and not isinstance(self.peptide_spectral_count, int):
            self.peptide_spectral_count = int(self.peptide_spectral_count)

        if self.peptide_sum_masic_abundance is not None and not isinstance(self.peptide_sum_masic_abundance, int):
            self.peptide_sum_masic_abundance = int(self.peptide_sum_masic_abundance)

        super().__post_init__(**kwargs)


@dataclass
class ProteinQuantification(YAMLRoot):
    """
    This is used to link a metaproteomics analysis workflow to a specific protein
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.ProteinQuantification
    class_class_curie: ClassVar[str] = "nmdc:ProteinQuantification"
    class_name: ClassVar[str] = "protein quantification"
    class_model_uri: ClassVar[URIRef] = NMDC.ProteinQuantification

    best_protein: Optional[Union[str, GeneProductId]] = None
    all_proteins: Optional[Union[Union[str, GeneProductId], List[Union[str, GeneProductId]]]] = empty_list()
    peptide_sequence_count: Optional[int] = None
    protein_spectral_count: Optional[int] = None
    protein_sum_masic_abundance: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.best_protein is not None and not isinstance(self.best_protein, GeneProductId):
            self.best_protein = GeneProductId(self.best_protein)

        if not isinstance(self.all_proteins, list):
            self.all_proteins = [self.all_proteins] if self.all_proteins is not None else []
        self.all_proteins = [v if isinstance(v, GeneProductId) else GeneProductId(v) for v in self.all_proteins]

        if self.peptide_sequence_count is not None and not isinstance(self.peptide_sequence_count, int):
            self.peptide_sequence_count = int(self.peptide_sequence_count)

        if self.protein_spectral_count is not None and not isinstance(self.protein_spectral_count, int):
            self.protein_spectral_count = int(self.protein_spectral_count)

        if self.protein_sum_masic_abundance is not None and not isinstance(self.protein_sum_masic_abundance, int):
            self.protein_sum_masic_abundance = int(self.protein_sum_masic_abundance)

        super().__post_init__(**kwargs)


@dataclass
class ChemicalEntity(OntologyClass):
    """
    An atom or molecule that can be represented with a chemical formula. Include lipids, glycans, natural products,
    drugs. There may be different terms for distinct acid-base forms, protonation states
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.ChemicalEntity
    class_class_curie: ClassVar[str] = "nmdc:ChemicalEntity"
    class_name: ClassVar[str] = "chemical entity"
    class_model_uri: ClassVar[URIRef] = NMDC.ChemicalEntity

    id: Union[str, ChemicalEntityId] = None
    inchi: Optional[str] = None
    inchi_key: Optional[str] = None
    smiles: Optional[Union[str, List[str]]] = empty_list()
    chemical_formula: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalEntityId):
            self.id = ChemicalEntityId(self.id)

        if self.inchi is not None and not isinstance(self.inchi, str):
            self.inchi = str(self.inchi)

        if self.inchi_key is not None and not isinstance(self.inchi_key, str):
            self.inchi_key = str(self.inchi_key)

        if not isinstance(self.smiles, list):
            self.smiles = [self.smiles] if self.smiles is not None else []
        self.smiles = [v if isinstance(v, str) else str(v) for v in self.smiles]

        if self.chemical_formula is not None and not isinstance(self.chemical_formula, str):
            self.chemical_formula = str(self.chemical_formula)

        super().__post_init__(**kwargs)


@dataclass
class GeneProduct(NamedThing):
    """
    A molecule encoded by a gene that has an evolved function
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.GeneProduct
    class_class_curie: ClassVar[str] = "nmdc:GeneProduct"
    class_name: ClassVar[str] = "gene product"
    class_model_uri: ClassVar[URIRef] = NMDC.GeneProduct

    id: Union[str, GeneProductId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneProductId):
            self.id = GeneProductId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class TextValue(AttributeValue):
    """
    A basic string value
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.TextValue
    class_class_curie: ClassVar[str] = "nmdc:TextValue"
    class_name: ClassVar[str] = "text value"
    class_model_uri: ClassVar[URIRef] = NMDC.TextValue

    language: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.language is not None and not isinstance(self.language, str):
            self.language = str(self.language)

        super().__post_init__(**kwargs)


class UrlValue(AttributeValue):
    """
    A value that is a string that conforms to URL syntax
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.UrlValue
    class_class_curie: ClassVar[str] = "nmdc:UrlValue"
    class_name: ClassVar[str] = "url value"
    class_model_uri: ClassVar[URIRef] = NMDC.UrlValue


class TimestampValue(AttributeValue):
    """
    A value that is a timestamp. The range should be ISO-8601
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.TimestampValue
    class_class_curie: ClassVar[str] = "nmdc:TimestampValue"
    class_name: ClassVar[str] = "timestamp value"
    class_model_uri: ClassVar[URIRef] = NMDC.TimestampValue


@dataclass
class IntegerValue(AttributeValue):
    """
    A value that is an integer
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.IntegerValue
    class_class_curie: ClassVar[str] = "nmdc:IntegerValue"
    class_name: ClassVar[str] = "integer value"
    class_model_uri: ClassVar[URIRef] = NMDC.IntegerValue

    has_numeric_value: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_numeric_value is not None and not isinstance(self.has_numeric_value, float):
            self.has_numeric_value = float(self.has_numeric_value)

        super().__post_init__(**kwargs)


@dataclass
class BooleanValue(AttributeValue):
    """
    A value that is a boolean
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.BooleanValue
    class_class_curie: ClassVar[str] = "nmdc:BooleanValue"
    class_name: ClassVar[str] = "boolean value"
    class_model_uri: ClassVar[URIRef] = NMDC.BooleanValue

    has_boolean_value: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_boolean_value is not None and not isinstance(self.has_boolean_value, Bool):
            self.has_boolean_value = Bool(self.has_boolean_value)

        super().__post_init__(**kwargs)


@dataclass
class ControlledTermValue(AttributeValue):
    """
    A controlled term or class from an ontology
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.ControlledTermValue
    class_class_curie: ClassVar[str] = "nmdc:ControlledTermValue"
    class_name: ClassVar[str] = "controlled term value"
    class_model_uri: ClassVar[URIRef] = NMDC.ControlledTermValue

    term: Optional[Union[dict, OntologyClass]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.term is not None and not isinstance(self.term, OntologyClass):
            self.term = OntologyClass(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass
class GeolocationValue(AttributeValue):
    """
    A normalized value for a location on the earth's surface
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.GeolocationValue
    class_class_curie: ClassVar[str] = "nmdc:GeolocationValue"
    class_name: ClassVar[str] = "geolocation value"
    class_model_uri: ClassVar[URIRef] = NMDC.GeolocationValue

    latitude: Optional[float] = None
    longitude: Optional[float] = None
    has_raw_value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.latitude is not None and not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        if self.has_raw_value is not None and not isinstance(self.has_raw_value, str):
            self.has_raw_value = str(self.has_raw_value)

        super().__post_init__(**kwargs)


@dataclass
class Activity(YAMLRoot):
    """
    a provence-generating activity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.Activity
    class_class_curie: ClassVar[str] = "nmdc:Activity"
    class_name: ClassVar[str] = "activity"
    class_model_uri: ClassVar[URIRef] = NMDC.Activity

    id: Union[str, ActivityId] = None
    name: Optional[str] = None
    started_at_time: Optional[Union[str, XSDDateTime]] = None
    ended_at_time: Optional[Union[str, XSDDateTime]] = None
    was_informed_by: Optional[Union[str, ActivityId]] = None
    was_associated_with: Optional[Union[dict, "Agent"]] = None
    used: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActivityId):
            self.id = ActivityId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.started_at_time is not None and not isinstance(self.started_at_time, XSDDateTime):
            self.started_at_time = XSDDateTime(self.started_at_time)

        if self.ended_at_time is not None and not isinstance(self.ended_at_time, XSDDateTime):
            self.ended_at_time = XSDDateTime(self.ended_at_time)

        if self.was_informed_by is not None and not isinstance(self.was_informed_by, ActivityId):
            self.was_informed_by = ActivityId(self.was_informed_by)

        if self.was_associated_with is not None and not isinstance(self.was_associated_with, Agent):
            self.was_associated_with = Agent(**as_dict(self.was_associated_with))

        if self.used is not None and not isinstance(self.used, str):
            self.used = str(self.used)

        super().__post_init__(**kwargs)


@dataclass
class Agent(YAMLRoot):
    """
    a provence-generating agent
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.Agent
    class_class_curie: ClassVar[str] = "nmdc:Agent"
    class_name: ClassVar[str] = "agent"
    class_model_uri: ClassVar[URIRef] = NMDC.Agent

    acted_on_behalf_of: Optional[Union[dict, "Agent"]] = None
    was_informed_by: Optional[Union[str, ActivityId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.acted_on_behalf_of is not None and not isinstance(self.acted_on_behalf_of, Agent):
            self.acted_on_behalf_of = Agent(**as_dict(self.acted_on_behalf_of))

        if self.was_informed_by is not None and not isinstance(self.was_informed_by, ActivityId):
            self.was_informed_by = ActivityId(self.was_informed_by)

        super().__post_init__(**kwargs)


@dataclass
class WorkflowExecutionActivity(Activity):
    """
    Represents an instance of an execution of a particular workflow
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/workflow_execution_activity/WorkflowExecutionActivity")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "workflow execution activity"
    class_model_uri: ClassVar[URIRef] = NMDC.WorkflowExecutionActivity

    id: Union[str, WorkflowExecutionActivityId] = None
    execution_resource: str = None
    git_url: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_output: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    type: str = None
    started_at_time: Union[str, XSDDateTime] = None
    ended_at_time: Union[str, XSDDateTime] = None
    was_informed_by: Union[str, ActivityId] = None
    part_of: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()
    was_associated_with: Optional[Union[str, WorkflowExecutionActivityId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WorkflowExecutionActivityId):
            self.id = WorkflowExecutionActivityId(self.id)

        if self._is_empty(self.execution_resource):
            self.MissingRequiredField("execution_resource")
        if not isinstance(self.execution_resource, str):
            self.execution_resource = str(self.execution_resource)

        if self._is_empty(self.git_url):
            self.MissingRequiredField("git_url")
        if not isinstance(self.git_url, str):
            self.git_url = str(self.git_url)

        if self._is_empty(self.has_input):
            self.MissingRequiredField("has_input")
        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
        self.has_input = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_input]

        if self._is_empty(self.has_output):
            self.MissingRequiredField("has_output")
        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output] if self.has_output is not None else []
        self.has_output = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_output]

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.started_at_time):
            self.MissingRequiredField("started_at_time")
        if not isinstance(self.started_at_time, XSDDateTime):
            self.started_at_time = XSDDateTime(self.started_at_time)

        if self._is_empty(self.ended_at_time):
            self.MissingRequiredField("ended_at_time")
        if not isinstance(self.ended_at_time, XSDDateTime):
            self.ended_at_time = XSDDateTime(self.ended_at_time)

        if self._is_empty(self.was_informed_by):
            self.MissingRequiredField("was_informed_by")
        if not isinstance(self.was_informed_by, ActivityId):
            self.was_informed_by = ActivityId(self.was_informed_by)

        if not isinstance(self.part_of, list):
            self.part_of = [self.part_of] if self.part_of is not None else []
        self.part_of = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.part_of]

        if self.was_associated_with is not None and not isinstance(self.was_associated_with, WorkflowExecutionActivityId):
            self.was_associated_with = WorkflowExecutionActivityId(self.was_associated_with)

        super().__post_init__(**kwargs)


@dataclass
class MetagenomeAssembly(WorkflowExecutionActivity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/workflow_execution_activity/MetagenomeAssembly")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "metagenome assembly"
    class_model_uri: ClassVar[URIRef] = NMDC.MetagenomeAssembly

    id: Union[str, MetagenomeAssemblyId] = None
    execution_resource: str = None
    git_url: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_output: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    type: str = None
    started_at_time: Union[str, XSDDateTime] = None
    ended_at_time: Union[str, XSDDateTime] = None
    was_informed_by: Union[str, ActivityId] = None
    asm_score: Optional[float] = None
    scaffolds: Optional[float] = None
    scaf_logsum: Optional[float] = None
    scaf_powsum: Optional[float] = None
    scaf_max: Optional[float] = None
    scaf_bp: Optional[float] = None
    scaf_N50: Optional[float] = None
    scaf_N90: Optional[float] = None
    scaf_L50: Optional[float] = None
    scaf_L90: Optional[float] = None
    scaf_n_gt50K: Optional[float] = None
    scaf_l_gt50K: Optional[float] = None
    scaf_pct_gt50K: Optional[float] = None
    contigs: Optional[float] = None
    contig_bp: Optional[float] = None
    ctg_N50: Optional[float] = None
    ctg_L50: Optional[float] = None
    ctg_N90: Optional[float] = None
    ctg_L90: Optional[float] = None
    ctg_logsum: Optional[float] = None
    ctg_powsum: Optional[float] = None
    ctg_max: Optional[float] = None
    gap_pct: Optional[float] = None
    gc_std: Optional[float] = None
    gc_avg: Optional[float] = None
    num_input_reads: Optional[float] = None
    num_aligned_reads: Optional[float] = None
    INSDC_assembly_identifiers: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MetagenomeAssemblyId):
            self.id = MetagenomeAssemblyId(self.id)

        if self.asm_score is not None and not isinstance(self.asm_score, float):
            self.asm_score = float(self.asm_score)

        if self.scaffolds is not None and not isinstance(self.scaffolds, float):
            self.scaffolds = float(self.scaffolds)

        if self.scaf_logsum is not None and not isinstance(self.scaf_logsum, float):
            self.scaf_logsum = float(self.scaf_logsum)

        if self.scaf_powsum is not None and not isinstance(self.scaf_powsum, float):
            self.scaf_powsum = float(self.scaf_powsum)

        if self.scaf_max is not None and not isinstance(self.scaf_max, float):
            self.scaf_max = float(self.scaf_max)

        if self.scaf_bp is not None and not isinstance(self.scaf_bp, float):
            self.scaf_bp = float(self.scaf_bp)

        if self.scaf_N50 is not None and not isinstance(self.scaf_N50, float):
            self.scaf_N50 = float(self.scaf_N50)

        if self.scaf_N90 is not None and not isinstance(self.scaf_N90, float):
            self.scaf_N90 = float(self.scaf_N90)

        if self.scaf_L50 is not None and not isinstance(self.scaf_L50, float):
            self.scaf_L50 = float(self.scaf_L50)

        if self.scaf_L90 is not None and not isinstance(self.scaf_L90, float):
            self.scaf_L90 = float(self.scaf_L90)

        if self.scaf_n_gt50K is not None and not isinstance(self.scaf_n_gt50K, float):
            self.scaf_n_gt50K = float(self.scaf_n_gt50K)

        if self.scaf_l_gt50K is not None and not isinstance(self.scaf_l_gt50K, float):
            self.scaf_l_gt50K = float(self.scaf_l_gt50K)

        if self.scaf_pct_gt50K is not None and not isinstance(self.scaf_pct_gt50K, float):
            self.scaf_pct_gt50K = float(self.scaf_pct_gt50K)

        if self.contigs is not None and not isinstance(self.contigs, float):
            self.contigs = float(self.contigs)

        if self.contig_bp is not None and not isinstance(self.contig_bp, float):
            self.contig_bp = float(self.contig_bp)

        if self.ctg_N50 is not None and not isinstance(self.ctg_N50, float):
            self.ctg_N50 = float(self.ctg_N50)

        if self.ctg_L50 is not None and not isinstance(self.ctg_L50, float):
            self.ctg_L50 = float(self.ctg_L50)

        if self.ctg_N90 is not None and not isinstance(self.ctg_N90, float):
            self.ctg_N90 = float(self.ctg_N90)

        if self.ctg_L90 is not None and not isinstance(self.ctg_L90, float):
            self.ctg_L90 = float(self.ctg_L90)

        if self.ctg_logsum is not None and not isinstance(self.ctg_logsum, float):
            self.ctg_logsum = float(self.ctg_logsum)

        if self.ctg_powsum is not None and not isinstance(self.ctg_powsum, float):
            self.ctg_powsum = float(self.ctg_powsum)

        if self.ctg_max is not None and not isinstance(self.ctg_max, float):
            self.ctg_max = float(self.ctg_max)

        if self.gap_pct is not None and not isinstance(self.gap_pct, float):
            self.gap_pct = float(self.gap_pct)

        if self.gc_std is not None and not isinstance(self.gc_std, float):
            self.gc_std = float(self.gc_std)

        if self.gc_avg is not None and not isinstance(self.gc_avg, float):
            self.gc_avg = float(self.gc_avg)

        if self.num_input_reads is not None and not isinstance(self.num_input_reads, float):
            self.num_input_reads = float(self.num_input_reads)

        if self.num_aligned_reads is not None and not isinstance(self.num_aligned_reads, float):
            self.num_aligned_reads = float(self.num_aligned_reads)

        if self.INSDC_assembly_identifiers is not None and not isinstance(self.INSDC_assembly_identifiers, str):
            self.INSDC_assembly_identifiers = str(self.INSDC_assembly_identifiers)

        super().__post_init__(**kwargs)


@dataclass
class MetatranscriptomeAssembly(WorkflowExecutionActivity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/workflow_execution_activity/MetatranscriptomeAssembly")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "metatranscriptome assembly"
    class_model_uri: ClassVar[URIRef] = NMDC.MetatranscriptomeAssembly

    id: Union[str, MetatranscriptomeAssemblyId] = None
    execution_resource: str = None
    git_url: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_output: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    type: str = None
    started_at_time: Union[str, XSDDateTime] = None
    ended_at_time: Union[str, XSDDateTime] = None
    was_informed_by: Union[str, ActivityId] = None
    asm_score: Optional[float] = None
    scaffolds: Optional[float] = None
    scaf_logsum: Optional[float] = None
    scaf_powsum: Optional[float] = None
    scaf_max: Optional[float] = None
    scaf_bp: Optional[float] = None
    scaf_N50: Optional[float] = None
    scaf_N90: Optional[float] = None
    scaf_L50: Optional[float] = None
    scaf_L90: Optional[float] = None
    scaf_n_gt50K: Optional[float] = None
    scaf_l_gt50K: Optional[float] = None
    scaf_pct_gt50K: Optional[float] = None
    contigs: Optional[float] = None
    contig_bp: Optional[float] = None
    ctg_N50: Optional[float] = None
    ctg_L50: Optional[float] = None
    ctg_N90: Optional[float] = None
    ctg_L90: Optional[float] = None
    ctg_logsum: Optional[float] = None
    ctg_powsum: Optional[float] = None
    ctg_max: Optional[float] = None
    gap_pct: Optional[float] = None
    gc_std: Optional[float] = None
    gc_avg: Optional[float] = None
    num_input_reads: Optional[float] = None
    num_aligned_reads: Optional[float] = None
    INSDC_assembly_identifiers: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MetatranscriptomeAssemblyId):
            self.id = MetatranscriptomeAssemblyId(self.id)

        if self.asm_score is not None and not isinstance(self.asm_score, float):
            self.asm_score = float(self.asm_score)

        if self.scaffolds is not None and not isinstance(self.scaffolds, float):
            self.scaffolds = float(self.scaffolds)

        if self.scaf_logsum is not None and not isinstance(self.scaf_logsum, float):
            self.scaf_logsum = float(self.scaf_logsum)

        if self.scaf_powsum is not None and not isinstance(self.scaf_powsum, float):
            self.scaf_powsum = float(self.scaf_powsum)

        if self.scaf_max is not None and not isinstance(self.scaf_max, float):
            self.scaf_max = float(self.scaf_max)

        if self.scaf_bp is not None and not isinstance(self.scaf_bp, float):
            self.scaf_bp = float(self.scaf_bp)

        if self.scaf_N50 is not None and not isinstance(self.scaf_N50, float):
            self.scaf_N50 = float(self.scaf_N50)

        if self.scaf_N90 is not None and not isinstance(self.scaf_N90, float):
            self.scaf_N90 = float(self.scaf_N90)

        if self.scaf_L50 is not None and not isinstance(self.scaf_L50, float):
            self.scaf_L50 = float(self.scaf_L50)

        if self.scaf_L90 is not None and not isinstance(self.scaf_L90, float):
            self.scaf_L90 = float(self.scaf_L90)

        if self.scaf_n_gt50K is not None and not isinstance(self.scaf_n_gt50K, float):
            self.scaf_n_gt50K = float(self.scaf_n_gt50K)

        if self.scaf_l_gt50K is not None and not isinstance(self.scaf_l_gt50K, float):
            self.scaf_l_gt50K = float(self.scaf_l_gt50K)

        if self.scaf_pct_gt50K is not None and not isinstance(self.scaf_pct_gt50K, float):
            self.scaf_pct_gt50K = float(self.scaf_pct_gt50K)

        if self.contigs is not None and not isinstance(self.contigs, float):
            self.contigs = float(self.contigs)

        if self.contig_bp is not None and not isinstance(self.contig_bp, float):
            self.contig_bp = float(self.contig_bp)

        if self.ctg_N50 is not None and not isinstance(self.ctg_N50, float):
            self.ctg_N50 = float(self.ctg_N50)

        if self.ctg_L50 is not None and not isinstance(self.ctg_L50, float):
            self.ctg_L50 = float(self.ctg_L50)

        if self.ctg_N90 is not None and not isinstance(self.ctg_N90, float):
            self.ctg_N90 = float(self.ctg_N90)

        if self.ctg_L90 is not None and not isinstance(self.ctg_L90, float):
            self.ctg_L90 = float(self.ctg_L90)

        if self.ctg_logsum is not None and not isinstance(self.ctg_logsum, float):
            self.ctg_logsum = float(self.ctg_logsum)

        if self.ctg_powsum is not None and not isinstance(self.ctg_powsum, float):
            self.ctg_powsum = float(self.ctg_powsum)

        if self.ctg_max is not None and not isinstance(self.ctg_max, float):
            self.ctg_max = float(self.ctg_max)

        if self.gap_pct is not None and not isinstance(self.gap_pct, float):
            self.gap_pct = float(self.gap_pct)

        if self.gc_std is not None and not isinstance(self.gc_std, float):
            self.gc_std = float(self.gc_std)

        if self.gc_avg is not None and not isinstance(self.gc_avg, float):
            self.gc_avg = float(self.gc_avg)

        if self.num_input_reads is not None and not isinstance(self.num_input_reads, float):
            self.num_input_reads = float(self.num_input_reads)

        if self.num_aligned_reads is not None and not isinstance(self.num_aligned_reads, float):
            self.num_aligned_reads = float(self.num_aligned_reads)

        if self.INSDC_assembly_identifiers is not None and not isinstance(self.INSDC_assembly_identifiers, str):
            self.INSDC_assembly_identifiers = str(self.INSDC_assembly_identifiers)

        super().__post_init__(**kwargs)


@dataclass
class MetagenomeAnnotationActivity(WorkflowExecutionActivity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/workflow_execution_activity/MetagenomeAnnotationActivity")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "metagenome annotation activity"
    class_model_uri: ClassVar[URIRef] = NMDC.MetagenomeAnnotationActivity

    id: Union[str, MetagenomeAnnotationActivityId] = None
    execution_resource: str = None
    git_url: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_output: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    type: str = None
    started_at_time: Union[str, XSDDateTime] = None
    ended_at_time: Union[str, XSDDateTime] = None
    was_informed_by: Union[str, ActivityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MetagenomeAnnotationActivityId):
            self.id = MetagenomeAnnotationActivityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MetatranscriptomeAnnotationActivity(WorkflowExecutionActivity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/workflow_execution_activity/MetatranscriptomeAnnotationActivity")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "metatranscriptome annotation activity"
    class_model_uri: ClassVar[URIRef] = NMDC.MetatranscriptomeAnnotationActivity

    id: Union[str, MetatranscriptomeAnnotationActivityId] = None
    execution_resource: str = None
    git_url: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_output: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    type: str = None
    started_at_time: Union[str, XSDDateTime] = None
    ended_at_time: Union[str, XSDDateTime] = None
    was_informed_by: Union[str, ActivityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MetatranscriptomeAnnotationActivityId):
            self.id = MetatranscriptomeAnnotationActivityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MetatranscriptomeActivity(WorkflowExecutionActivity):
    """
    A metatranscriptome activity that e.g. pools assembly and annotation activity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/workflow_execution_activity/MetatranscriptomeActivity")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "metatranscriptome activity"
    class_model_uri: ClassVar[URIRef] = NMDC.MetatranscriptomeActivity

    id: Union[str, MetatranscriptomeActivityId] = None
    execution_resource: str = None
    git_url: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_output: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    type: str = None
    started_at_time: Union[str, XSDDateTime] = None
    ended_at_time: Union[str, XSDDateTime] = None
    was_informed_by: Union[str, ActivityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MetatranscriptomeActivityId):
            self.id = MetatranscriptomeActivityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MAGsAnalysisActivity(WorkflowExecutionActivity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/workflow_execution_activity/MAGsAnalysisActivity")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "MAGs analysis activity"
    class_model_uri: ClassVar[URIRef] = NMDC.MAGsAnalysisActivity

    id: Union[str, MAGsAnalysisActivityId] = None
    execution_resource: str = None
    git_url: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_output: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    type: str = None
    started_at_time: Union[str, XSDDateTime] = None
    ended_at_time: Union[str, XSDDateTime] = None
    was_informed_by: Union[str, ActivityId] = None
    input_contig_num: Optional[int] = None
    binned_contig_num: Optional[int] = None
    too_short_contig_num: Optional[int] = None
    lowDepth_contig_num: Optional[int] = None
    unbinned_contig_num: Optional[int] = None
    mags_list: Optional[Union[Union[dict, MAGBin], List[Union[dict, MAGBin]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MAGsAnalysisActivityId):
            self.id = MAGsAnalysisActivityId(self.id)

        if self.input_contig_num is not None and not isinstance(self.input_contig_num, int):
            self.input_contig_num = int(self.input_contig_num)

        if self.binned_contig_num is not None and not isinstance(self.binned_contig_num, int):
            self.binned_contig_num = int(self.binned_contig_num)

        if self.too_short_contig_num is not None and not isinstance(self.too_short_contig_num, int):
            self.too_short_contig_num = int(self.too_short_contig_num)

        if self.lowDepth_contig_num is not None and not isinstance(self.lowDepth_contig_num, int):
            self.lowDepth_contig_num = int(self.lowDepth_contig_num)

        if self.unbinned_contig_num is not None and not isinstance(self.unbinned_contig_num, int):
            self.unbinned_contig_num = int(self.unbinned_contig_num)

        if not isinstance(self.mags_list, list):
            self.mags_list = [self.mags_list] if self.mags_list is not None else []
        self.mags_list = [v if isinstance(v, MAGBin) else MAGBin(**as_dict(v)) for v in self.mags_list]

        super().__post_init__(**kwargs)


@dataclass
class ReadQCAnalysisActivity(WorkflowExecutionActivity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/workflow_execution_activity/ReadQCAnalysisActivity")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "read QC analysis activity"
    class_model_uri: ClassVar[URIRef] = NMDC.ReadQCAnalysisActivity

    id: Union[str, ReadQCAnalysisActivityId] = None
    execution_resource: str = None
    git_url: str = None
    type: str = None
    started_at_time: Union[str, XSDDateTime] = None
    ended_at_time: Union[str, XSDDateTime] = None
    was_informed_by: Union[str, ActivityId] = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_output: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    input_read_count: Optional[float] = None
    input_base_count: Optional[float] = None
    output_read_count: Optional[float] = None
    output_base_count: Optional[float] = None
    input_read_bases: Optional[float] = None
    output_read_bases: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReadQCAnalysisActivityId):
            self.id = ReadQCAnalysisActivityId(self.id)

        if self._is_empty(self.has_input):
            self.MissingRequiredField("has_input")
        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
        self.has_input = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_input]

        if self._is_empty(self.has_output):
            self.MissingRequiredField("has_output")
        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output] if self.has_output is not None else []
        self.has_output = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_output]

        if self.input_read_count is not None and not isinstance(self.input_read_count, float):
            self.input_read_count = float(self.input_read_count)

        if self.input_base_count is not None and not isinstance(self.input_base_count, float):
            self.input_base_count = float(self.input_base_count)

        if self.output_read_count is not None and not isinstance(self.output_read_count, float):
            self.output_read_count = float(self.output_read_count)

        if self.output_base_count is not None and not isinstance(self.output_base_count, float):
            self.output_base_count = float(self.output_base_count)

        if self.input_read_bases is not None and not isinstance(self.input_read_bases, float):
            self.input_read_bases = float(self.input_read_bases)

        if self.output_read_bases is not None and not isinstance(self.output_read_bases, float):
            self.output_read_bases = float(self.output_read_bases)

        super().__post_init__(**kwargs)


@dataclass
class ReadBasedAnalysisActivity(WorkflowExecutionActivity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/workflow_execution_activity/ReadBasedAnalysisActivity")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "read based analysis activity"
    class_model_uri: ClassVar[URIRef] = NMDC.ReadBasedAnalysisActivity

    id: Union[str, ReadBasedAnalysisActivityId] = None
    execution_resource: str = None
    git_url: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_output: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    type: str = None
    started_at_time: Union[str, XSDDateTime] = None
    ended_at_time: Union[str, XSDDateTime] = None
    was_informed_by: Union[str, ActivityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReadBasedAnalysisActivityId):
            self.id = ReadBasedAnalysisActivityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MetabolomicsAnalysisActivity(WorkflowExecutionActivity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/workflow_execution_activity/MetabolomicsAnalysisActivity")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "metabolomics analysis activity"
    class_model_uri: ClassVar[URIRef] = NMDC.MetabolomicsAnalysisActivity

    id: Union[str, MetabolomicsAnalysisActivityId] = None
    execution_resource: str = None
    git_url: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_output: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    type: str = None
    started_at_time: Union[str, XSDDateTime] = None
    ended_at_time: Union[str, XSDDateTime] = None
    was_informed_by: Union[str, ActivityId] = None
    used: Optional[Union[str, InstrumentId]] = None
    has_metabolite_quantifications: Optional[Union[Union[dict, MetaboliteQuantification], List[Union[dict, MetaboliteQuantification]]]] = empty_list()
    has_calibration: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MetabolomicsAnalysisActivityId):
            self.id = MetabolomicsAnalysisActivityId(self.id)

        if self.used is not None and not isinstance(self.used, InstrumentId):
            self.used = InstrumentId(self.used)

        if not isinstance(self.has_metabolite_quantifications, list):
            self.has_metabolite_quantifications = [self.has_metabolite_quantifications] if self.has_metabolite_quantifications is not None else []
        self.has_metabolite_quantifications = [v if isinstance(v, MetaboliteQuantification) else MetaboliteQuantification(**as_dict(v)) for v in self.has_metabolite_quantifications]

        if self.has_calibration is not None and not isinstance(self.has_calibration, str):
            self.has_calibration = str(self.has_calibration)

        super().__post_init__(**kwargs)


@dataclass
class MetaproteomicsAnalysisActivity(WorkflowExecutionActivity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/workflow_execution_activity/MetaproteomicsAnalysisActivity")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "metaproteomics analysis activity"
    class_model_uri: ClassVar[URIRef] = NMDC.MetaproteomicsAnalysisActivity

    id: Union[str, MetaproteomicsAnalysisActivityId] = None
    execution_resource: str = None
    git_url: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_output: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    type: str = None
    started_at_time: Union[str, XSDDateTime] = None
    ended_at_time: Union[str, XSDDateTime] = None
    was_informed_by: Union[str, ActivityId] = None
    used: Optional[Union[str, InstrumentId]] = None
    has_peptide_quantifications: Optional[Union[Union[dict, PeptideQuantification], List[Union[dict, PeptideQuantification]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MetaproteomicsAnalysisActivityId):
            self.id = MetaproteomicsAnalysisActivityId(self.id)

        if self.used is not None and not isinstance(self.used, InstrumentId):
            self.used = InstrumentId(self.used)

        if not isinstance(self.has_peptide_quantifications, list):
            self.has_peptide_quantifications = [self.has_peptide_quantifications] if self.has_peptide_quantifications is not None else []
        self.has_peptide_quantifications = [v if isinstance(v, PeptideQuantification) else PeptideQuantification(**as_dict(v)) for v in self.has_peptide_quantifications]

        super().__post_init__(**kwargs)


@dataclass
class NomAnalysisActivity(WorkflowExecutionActivity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/workflow_execution_activity/NomAnalysisActivity")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "nom analysis activity"
    class_model_uri: ClassVar[URIRef] = NMDC.NomAnalysisActivity

    id: Union[str, NomAnalysisActivityId] = None
    execution_resource: str = None
    git_url: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_output: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    type: str = None
    started_at_time: Union[str, XSDDateTime] = None
    ended_at_time: Union[str, XSDDateTime] = None
    was_informed_by: Union[str, ActivityId] = None
    used: Optional[Union[str, InstrumentId]] = None
    has_calibration: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NomAnalysisActivityId):
            self.id = NomAnalysisActivityId(self.id)

        if self.used is not None and not isinstance(self.used, InstrumentId):
            self.used = InstrumentId(self.used)

        if self.has_calibration is not None and not isinstance(self.has_calibration, str):
            self.has_calibration = str(self.has_calibration)

        super().__post_init__(**kwargs)


@dataclass
class GenomeFeature(YAMLRoot):
    """
    A feature localized to an interval along a genome
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/GenomeFeature")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "genome feature"
    class_model_uri: ClassVar[URIRef] = NMDC.GenomeFeature

    seqid: str = None
    start: int = None
    end: int = None
    type: Optional[Union[str, OntologyClassId]] = None
    strand: Optional[str] = None
    phase: Optional[int] = None
    encodes: Optional[Union[str, GeneProductId]] = None
    feature_type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.seqid):
            self.MissingRequiredField("seqid")
        if not isinstance(self.seqid, str):
            self.seqid = str(self.seqid)

        if self._is_empty(self.start):
            self.MissingRequiredField("start")
        if not isinstance(self.start, int):
            self.start = int(self.start)

        if self._is_empty(self.end):
            self.MissingRequiredField("end")
        if not isinstance(self.end, int):
            self.end = int(self.end)

        if self.type is not None and not isinstance(self.type, OntologyClassId):
            self.type = OntologyClassId(self.type)

        if self.strand is not None and not isinstance(self.strand, str):
            self.strand = str(self.strand)

        if self.phase is not None and not isinstance(self.phase, int):
            self.phase = int(self.phase)

        if self.encodes is not None and not isinstance(self.encodes, GeneProductId):
            self.encodes = GeneProductId(self.encodes)

        if self.feature_type is not None and not isinstance(self.feature_type, str):
            self.feature_type = str(self.feature_type)

        super().__post_init__(**kwargs)


@dataclass
class FunctionalAnnotationTerm(OntologyClass):
    """
    Abstract grouping class for any term/descriptor that can be applied to a functional unit of a genome (protein,
    ncRNA, complex).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/FunctionalAnnotationTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "functional annotation term"
    class_model_uri: ClassVar[URIRef] = NMDC.FunctionalAnnotationTerm

    id: Union[str, FunctionalAnnotationTermId] = None

@dataclass
class Pathway(FunctionalAnnotationTerm):
    """
    A pathway is a sequence of steps/reactions carried out by an organism or community of organisms
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/Pathway")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "pathway"
    class_model_uri: ClassVar[URIRef] = NMDC.Pathway

    id: Union[str, PathwayId] = None
    has_part: Optional[Union[Union[str, ReactionId], List[Union[str, ReactionId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PathwayId):
            self.id = PathwayId(self.id)

        if not isinstance(self.has_part, list):
            self.has_part = [self.has_part] if self.has_part is not None else []
        self.has_part = [v if isinstance(v, ReactionId) else ReactionId(v) for v in self.has_part]

        super().__post_init__(**kwargs)


@dataclass
class Reaction(FunctionalAnnotationTerm):
    """
    An individual biochemical transformation carried out by a functional unit of an organism, in which a collection of
    substrates are transformed into a collection of products. Can also represent transporters
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/Reaction")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "reaction"
    class_model_uri: ClassVar[URIRef] = NMDC.Reaction

    id: Union[str, ReactionId] = None
    left_participants: Optional[Union[Union[dict, "ReactionParticipant"], List[Union[dict, "ReactionParticipant"]]]] = empty_list()
    right_participants: Optional[Union[Union[dict, "ReactionParticipant"], List[Union[dict, "ReactionParticipant"]]]] = empty_list()
    direction: Optional[str] = None
    smarts_string: Optional[str] = None
    is_diastereoselective: Optional[Union[bool, Bool]] = None
    is_stereo: Optional[Union[bool, Bool]] = None
    is_balanced: Optional[Union[bool, Bool]] = None
    is_transport: Optional[Union[bool, Bool]] = None
    is_fully_characterized: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReactionId):
            self.id = ReactionId(self.id)

        if not isinstance(self.left_participants, list):
            self.left_participants = [self.left_participants] if self.left_participants is not None else []
        self.left_participants = [v if isinstance(v, ReactionParticipant) else ReactionParticipant(**as_dict(v)) for v in self.left_participants]

        if not isinstance(self.right_participants, list):
            self.right_participants = [self.right_participants] if self.right_participants is not None else []
        self.right_participants = [v if isinstance(v, ReactionParticipant) else ReactionParticipant(**as_dict(v)) for v in self.right_participants]

        if self.direction is not None and not isinstance(self.direction, str):
            self.direction = str(self.direction)

        if self.smarts_string is not None and not isinstance(self.smarts_string, str):
            self.smarts_string = str(self.smarts_string)

        if self.is_diastereoselective is not None and not isinstance(self.is_diastereoselective, Bool):
            self.is_diastereoselective = Bool(self.is_diastereoselective)

        if self.is_stereo is not None and not isinstance(self.is_stereo, Bool):
            self.is_stereo = Bool(self.is_stereo)

        if self.is_balanced is not None and not isinstance(self.is_balanced, Bool):
            self.is_balanced = Bool(self.is_balanced)

        if self.is_transport is not None and not isinstance(self.is_transport, Bool):
            self.is_transport = Bool(self.is_transport)

        if self.is_fully_characterized is not None and not isinstance(self.is_fully_characterized, Bool):
            self.is_fully_characterized = Bool(self.is_fully_characterized)

        super().__post_init__(**kwargs)


@dataclass
class ReactionParticipant(YAMLRoot):
    """
    Instances of this link a reaction to a chemical entity participant
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/ReactionParticipant")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "reaction participant"
    class_model_uri: ClassVar[URIRef] = NMDC.ReactionParticipant

    chemical: Optional[Union[str, ChemicalEntityId]] = None
    stoichiometry: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.chemical is not None and not isinstance(self.chemical, ChemicalEntityId):
            self.chemical = ChemicalEntityId(self.chemical)

        if self.stoichiometry is not None and not isinstance(self.stoichiometry, int):
            self.stoichiometry = int(self.stoichiometry)

        super().__post_init__(**kwargs)


@dataclass
class OrthologyGroup(FunctionalAnnotationTerm):
    """
    A set of genes or gene products in which all members are orthologous
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/OrthologyGroup")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "orthology group"
    class_model_uri: ClassVar[URIRef] = NMDC.OrthologyGroup

    id: Union[str, OrthologyGroupId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrthologyGroupId):
            self.id = OrthologyGroupId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class FunctionalAnnotation(YAMLRoot):
    """
    An assignment of a function term (e.g. reaction or pathway) that is executed by a gene product, or which the gene
    product plays an active role in. Functional annotations can be assigned manually by curators, or automatically in
    workflows. In the context of NMDC, all function annotation is performed automatically, typically using HMM or
    Blast type methods
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/FunctionalAnnotation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "functional annotation"
    class_model_uri: ClassVar[URIRef] = NMDC.FunctionalAnnotation

    was_generated_by: Optional[Union[str, MetagenomeAnnotationActivityId]] = None
    subject: Optional[Union[str, GeneProductId]] = None
    has_function: Optional[str] = None
    type: Optional[Union[str, OntologyClassId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.was_generated_by is not None and not isinstance(self.was_generated_by, MetagenomeAnnotationActivityId):
            self.was_generated_by = MetagenomeAnnotationActivityId(self.was_generated_by)

        if self.subject is not None and not isinstance(self.subject, GeneProductId):
            self.subject = GeneProductId(self.subject)

        if self.has_function is not None and not isinstance(self.has_function, str):
            self.has_function = str(self.has_function)

        if self.type is not None and not isinstance(self.type, OntologyClassId):
            self.type = OntologyClassId(self.type)

        super().__post_init__(**kwargs)


# Enumerations
class FileTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="FileTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "FT ICR-MS Analysis Results",
                PermissibleValue(text="FT ICR-MS Analysis Results",
                                 description="FT ICR-MS-based molecular formula assignment results table") )
        setattr(cls, "GC-MS Metabolomics Results",
                PermissibleValue(text="GC-MS Metabolomics Results",
                                 description="GC-MS-based metabolite assignment results table") )
        setattr(cls, "Metaproteomics Workflow Statistics",
                PermissibleValue(text="Metaproteomics Workflow Statistics",
                                 description="Aggregate workflow statistics file") )
        setattr(cls, "Protein Report",
                PermissibleValue(text="Protein Report",
                                 description="Filtered protein report file") )
        setattr(cls, "Peptide Report",
                PermissibleValue(text="Peptide Report",
                                 description="Filtered peptide report file") )
        setattr(cls, "Unfiltered Metaproteomics Results",
                PermissibleValue(text="Unfiltered Metaproteomics Results",
                                 description="MSGFjobs and MASIC output file") )
        setattr(cls, "Read Count and RPKM",
                PermissibleValue(text="Read Count and RPKM",
                                 description="Annotation read count and RPKM per feature JSON") )
        setattr(cls, "QC non-rRNA R2",
                PermissibleValue(text="QC non-rRNA R2",
                                 description="QC removed rRNA reads (R2) fastq") )
        setattr(cls, "QC non-rRNA R1",
                PermissibleValue(text="QC non-rRNA R1",
                                 description="QC removed rRNA reads (R1) fastq") )
        setattr(cls, "Metagenome Bins",
                PermissibleValue(text="Metagenome Bins",
                                 description="Metagenome bin contigs fasta") )
        setattr(cls, "CheckM Statistics",
                PermissibleValue(text="CheckM Statistics",
                                 description="CheckM statistics report") )
        setattr(cls, "GOTTCHA2 Krona Plot",
                PermissibleValue(text="GOTTCHA2 Krona Plot",
                                 description="GOTTCHA2 krona plot HTML file") )
        setattr(cls, "Kraken2 Krona Plot",
                PermissibleValue(text="Kraken2 Krona Plot",
                                 description="Kraken2 krona plot HTML file") )
        setattr(cls, "Centrifuge Krona Plot",
                PermissibleValue(text="Centrifuge Krona Plot",
                                 description="Centrifug krona plot HTML file") )
        setattr(cls, "Kraken2 Classification Report",
                PermissibleValue(text="Kraken2 Classification Report",
                                 description="Kraken2 output report file") )
        setattr(cls, "Kraken2 Taxonomic Classification",
                PermissibleValue(text="Kraken2 Taxonomic Classification",
                                 description="Kraken2 output read classification file") )
        setattr(cls, "Centrifuge Classification Report",
                PermissibleValue(text="Centrifuge Classification Report",
                                 description="Centrifuge output report file") )
        setattr(cls, "Centrifuge Taxonomic Classification",
                PermissibleValue(text="Centrifuge Taxonomic Classification",
                                 description="Centrifuge output read classification file") )
        setattr(cls, "Structural Annotation GFF",
                PermissibleValue(text="Structural Annotation GFF",
                                 description="GFF3 format file with structural annotations") )
        setattr(cls, "Functional Annotation GFF",
                PermissibleValue(text="Functional Annotation GFF",
                                 description="GFF3 format file with functional annotations") )
        setattr(cls, "Annotation Amino Acid FASTA",
                PermissibleValue(text="Annotation Amino Acid FASTA",
                                 description="FASTA amino acid file for annotated proteins") )
        setattr(cls, "Annotation Enzyme Commission",
                PermissibleValue(text="Annotation Enzyme Commission",
                                 description="Tab delimited file for EC annotation") )
        setattr(cls, "Annotation KEGG Orthology",
                PermissibleValue(text="Annotation KEGG Orthology",
                                 description="Tab delimited file for KO annotation") )
        setattr(cls, "Assembly Coverage BAM",
                PermissibleValue(text="Assembly Coverage BAM",
                                 description="Sorted bam file of reads mapping back to the final assembly") )
        setattr(cls, "Assembly AGP",
                PermissibleValue(text="Assembly AGP",
                                 description="An AGP format file that describes the assembly") )
        setattr(cls, "Assembly Scaffolds",
                PermissibleValue(text="Assembly Scaffolds",
                                 description="Final assembly scaffolds fasta") )
        setattr(cls, "Assembly Contigs",
                PermissibleValue(text="Assembly Contigs",
                                 description="Final assembly contigs fasta") )
        setattr(cls, "Assembly Coverage Stats",
                PermissibleValue(text="Assembly Coverage Stats",
                                 description="Assembled contigs coverage information") )
        setattr(cls, "Filtered Sequencing Reads",
                PermissibleValue(text="Filtered Sequencing Reads",
                                 description="Reads QC result fastq (clean data)") )
        setattr(cls, "QC Statistics",
                PermissibleValue(text="QC Statistics",
                                 description="Reads QC summary statistics") )
        setattr(cls, "TIGRFam Annotation GFF",
                PermissibleValue(text="TIGRFam Annotation GFF",
                                 description="GFF3 format file with TIGRfam") )
        setattr(cls, "Clusters of Orthologous Groups (COG) Annotation GFF",
                PermissibleValue(text="Clusters of Orthologous Groups (COG) Annotation GFF",
                                 description="GFF3 format file with COGs") )
        setattr(cls, "CATH FunFams (Functional Families) Annotation GFF",
                PermissibleValue(text="CATH FunFams (Functional Families) Annotation GFF",
                                 description="GFF3 format file with CATH FunFams") )
        setattr(cls, "SUPERFam Annotation GFF",
                PermissibleValue(text="SUPERFam Annotation GFF",
                                 description="GFF3 format file with SUPERFam") )
        setattr(cls, "SMART Annotation GFF",
                PermissibleValue(text="SMART Annotation GFF",
                                 description="GFF3 format file with SMART") )
        setattr(cls, "Pfam Annotation GFF",
                PermissibleValue(text="Pfam Annotation GFF",
                                 description="GFF3 format file with Pfam") )
        setattr(cls, "Direct Infusion FT ICR-MS Raw Data",
                PermissibleValue(text="Direct Infusion FT ICR-MS Raw Data",
                                 description="Direct infusion 21 Tesla Fourier Transform ion cyclotron resonance mass spectrometry raw data acquired in broadband full scan mode") )

class CreditEnum(EnumDefinitionImpl):

    Conceptualization = PermissibleValue(text="Conceptualization",
                                                         description="Conceptualization")
    Investigation = PermissibleValue(text="Investigation",
                                                 description="Investigation")
    Methodology = PermissibleValue(text="Methodology",
                                             description="Methodology")
    Resources = PermissibleValue(text="Resources",
                                         description="Resources")
    Software = PermissibleValue(text="Software",
                                       description="Software")
    Supervision = PermissibleValue(text="Supervision",
                                             description="Supervision")
    Validation = PermissibleValue(text="Validation",
                                           description="Validation")
    Visualization = PermissibleValue(text="Visualization",
                                                 description="Visualization")

    _defn = EnumDefinition(
        name="CreditEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Data curation",
                PermissibleValue(text="Data curation",
                                 description="Data curation") )
        setattr(cls, "Formal Analysis",
                PermissibleValue(text="Formal Analysis",
                                 description="Formal Analysis") )
        setattr(cls, "Funding acquisition",
                PermissibleValue(text="Funding acquisition",
                                 description="Funding acquisition") )
        setattr(cls, "Project administration",
                PermissibleValue(text="Project administration",
                                 description="Project administration") )
        setattr(cls, "Writing original draft",
                PermissibleValue(text="Writing original draft",
                                 description="Writing – original draft") )
        setattr(cls, "Writing review and editing",
                PermissibleValue(text="Writing review and editing",
                                 description="Writing – review & editing") )
        setattr(cls, "Principal Investigator",
                PermissibleValue(text="Principal Investigator",
                                 description="principal investigator role",
                                 meaning=OBI["0000103"]) )

class ArchStrucEnum(EnumDefinitionImpl):

    building = PermissibleValue(text="building")
    shed = PermissibleValue(text="shed")
    home = PermissibleValue(text="home")

    _defn = EnumDefinition(
        name="ArchStrucEnum",
    )

class BiolStatEnum(EnumDefinitionImpl):

    wild = PermissibleValue(text="wild")
    natural = PermissibleValue(text="natural")
    hybrid = PermissibleValue(text="hybrid")
    mutant = PermissibleValue(text="mutant")

    _defn = EnumDefinition(
        name="BiolStatEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "semi-natural",
                PermissibleValue(text="semi-natural") )
        setattr(cls, "inbred line",
                PermissibleValue(text="inbred line") )
        setattr(cls, "breeder's line",
                PermissibleValue(text="breeder's line") )
        setattr(cls, "clonal selection",
                PermissibleValue(text="clonal selection") )

class BioticRelationshipEnum(EnumDefinitionImpl):

    parasite = PermissibleValue(text="parasite")
    commensal = PermissibleValue(text="commensal")
    symbiont = PermissibleValue(text="symbiont")

    _defn = EnumDefinition(
        name="BioticRelationshipEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "free living",
                PermissibleValue(text="free living") )

class BuildDocsEnum(EnumDefinitionImpl):

    schedule = PermissibleValue(text="schedule")
    sections = PermissibleValue(text="sections")
    submittals = PermissibleValue(text="submittals")
    windows = PermissibleValue(text="windows")

    _defn = EnumDefinition(
        name="BuildDocsEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "building information model",
                PermissibleValue(text="building information model") )
        setattr(cls, "commissioning report",
                PermissibleValue(text="commissioning report") )
        setattr(cls, "complaint logs",
                PermissibleValue(text="complaint logs") )
        setattr(cls, "contract administration",
                PermissibleValue(text="contract administration") )
        setattr(cls, "cost estimate",
                PermissibleValue(text="cost estimate") )
        setattr(cls, "janitorial schedules or logs",
                PermissibleValue(text="janitorial schedules or logs") )
        setattr(cls, "maintenance plans",
                PermissibleValue(text="maintenance plans") )
        setattr(cls, "shop drawings",
                PermissibleValue(text="shop drawings") )
        setattr(cls, "ventilation system",
                PermissibleValue(text="ventilation system") )

class BuildOccupTypeEnum(EnumDefinitionImpl):

    office = PermissibleValue(text="office")
    market = PermissibleValue(text="market")
    restaurant = PermissibleValue(text="restaurant")
    residence = PermissibleValue(text="residence")
    school = PermissibleValue(text="school")
    residential = PermissibleValue(text="residential")
    commercial = PermissibleValue(text="commercial")
    airport = PermissibleValue(text="airport")

    _defn = EnumDefinition(
        name="BuildOccupTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "low rise",
                PermissibleValue(text="low rise") )
        setattr(cls, "high rise",
                PermissibleValue(text="high rise") )
        setattr(cls, "wood framed",
                PermissibleValue(text="wood framed") )
        setattr(cls, "health care",
                PermissibleValue(text="health care") )
        setattr(cls, "sports complex",
                PermissibleValue(text="sports complex") )

class BuildingSettingEnum(EnumDefinitionImpl):

    urban = PermissibleValue(text="urban")
    suburban = PermissibleValue(text="suburban")
    exurban = PermissibleValue(text="exurban")
    rural = PermissibleValue(text="rural")

    _defn = EnumDefinition(
        name="BuildingSettingEnum",
    )

class CeilCondEnum(EnumDefinitionImpl):

    new = PermissibleValue(text="new")
    damaged = PermissibleValue(text="damaged")
    rupture = PermissibleValue(text="rupture")

    _defn = EnumDefinition(
        name="CeilCondEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "visible wear",
                PermissibleValue(text="visible wear") )
        setattr(cls, "needs repair",
                PermissibleValue(text="needs repair") )

class CeilFinishMatEnum(EnumDefinitionImpl):

    drywall = PermissibleValue(text="drywall")
    tiles = PermissibleValue(text="tiles")
    PVC = PermissibleValue(text="PVC")
    plasterboard = PermissibleValue(text="plasterboard")
    metal = PermissibleValue(text="metal")
    fiberglass = PermissibleValue(text="fiberglass")
    stucco = PermissibleValue(text="stucco")
    wood = PermissibleValue(text="wood")

    _defn = EnumDefinition(
        name="CeilFinishMatEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "mineral fibre",
                PermissibleValue(text="mineral fibre") )
        setattr(cls, "mineral wool/calcium silicate",
                PermissibleValue(text="mineral wool/calcium silicate") )

class CeilTextureEnum(EnumDefinitionImpl):

    knockdown = PermissibleValue(text="knockdown")
    popcorn = PermissibleValue(text="popcorn")
    smooth = PermissibleValue(text="smooth")
    swirl = PermissibleValue(text="swirl")

    _defn = EnumDefinition(
        name="CeilTextureEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "crows feet",
                PermissibleValue(text="crows feet") )
        setattr(cls, "crows-foot stomp",
                PermissibleValue(text="crows-foot stomp") )
        setattr(cls, "double skip",
                PermissibleValue(text="double skip") )
        setattr(cls, "hawk and trowel",
                PermissibleValue(text="hawk and trowel") )
        setattr(cls, "orange peel",
                PermissibleValue(text="orange peel") )
        setattr(cls, "rosebud stomp",
                PermissibleValue(text="rosebud stomp") )
        setattr(cls, "Santa-Fe texture",
                PermissibleValue(text="Santa-Fe texture") )
        setattr(cls, "skip trowel",
                PermissibleValue(text="skip trowel") )
        setattr(cls, "stomp knockdown",
                PermissibleValue(text="stomp knockdown") )

class CeilTypeEnum(EnumDefinitionImpl):

    cathedral = PermissibleValue(text="cathedral")
    dropped = PermissibleValue(text="dropped")
    concave = PermissibleValue(text="concave")
    coffered = PermissibleValue(text="coffered")
    cove = PermissibleValue(text="cove")
    stretched = PermissibleValue(text="stretched")

    _defn = EnumDefinition(
        name="CeilTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "barrel-shaped",
                PermissibleValue(text="barrel-shaped") )

class CurLandUseEnum(EnumDefinitionImpl):

    cities = PermissibleValue(text="cities")
    farmstead = PermissibleValue(text="farmstead")
    rock = PermissibleValue(text="rock")
    sand = PermissibleValue(text="sand")
    gravel = PermissibleValue(text="gravel")
    mudflats = PermissibleValue(text="mudflats")
    badlands = PermissibleValue(text="badlands")
    rangeland = PermissibleValue(text="rangeland")
    hayland = PermissibleValue(text="hayland")

    _defn = EnumDefinition(
        name="CurLandUseEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "industrial areas",
                PermissibleValue(text="industrial areas") )
        setattr(cls, "roads/railroads",
                PermissibleValue(text="roads/railroads") )
        setattr(cls, "salt flats",
                PermissibleValue(text="salt flats") )
        setattr(cls, "permanent snow or ice",
                PermissibleValue(text="permanent snow or ice") )
        setattr(cls, "saline seeps",
                PermissibleValue(text="saline seeps") )
        setattr(cls, "mines/quarries",
                PermissibleValue(text="mines/quarries") )
        setattr(cls, "oil waste areas",
                PermissibleValue(text="oil waste areas") )
        setattr(cls, "small grains",
                PermissibleValue(text="small grains") )
        setattr(cls, "row crops",
                PermissibleValue(text="row crops") )
        setattr(cls, "vegetable crops",
                PermissibleValue(text="vegetable crops") )
        setattr(cls, "horticultural plants (e.g. tulips)",
                PermissibleValue(text="horticultural plants (e.g. tulips)") )
        setattr(cls, "marshlands (grass,sedges,rushes)",
                PermissibleValue(text="marshlands (grass,sedges,rushes)") )
        setattr(cls, "tundra (mosses,lichens)",
                PermissibleValue(text="tundra (mosses,lichens)") )
        setattr(cls, "pastureland (grasslands used for livestock grazing)",
                PermissibleValue(text="pastureland (grasslands used for livestock grazing)") )
        setattr(cls, "meadows (grasses,alfalfa,fescue,bromegrass,timothy)",
                PermissibleValue(text="meadows (grasses,alfalfa,fescue,bromegrass,timothy)") )
        setattr(cls, "shrub land (e.g. mesquite,sage-brush,creosote bush,shrub oak,eucalyptus)",
                PermissibleValue(text="shrub land (e.g. mesquite,sage-brush,creosote bush,shrub oak,eucalyptus)") )
        setattr(cls, "successional shrub land (tree saplings,hazels,sumacs,chokecherry,shrub dogwoods,blackberries)",
                PermissibleValue(text="successional shrub land (tree saplings,hazels,sumacs,chokecherry,shrub dogwoods,blackberries)") )
        setattr(cls, "shrub crops (blueberries,nursery ornamentals,filberts)",
                PermissibleValue(text="shrub crops (blueberries,nursery ornamentals,filberts)") )
        setattr(cls, "vine crops (grapes)",
                PermissibleValue(text="vine crops (grapes)") )
        setattr(cls, "conifers (e.g. pine,spruce,fir,cypress)",
                PermissibleValue(text="conifers (e.g. pine,spruce,fir,cypress)") )
        setattr(cls, "hardwoods (e.g. oak,hickory,elm,aspen)",
                PermissibleValue(text="hardwoods (e.g. oak,hickory,elm,aspen)") )
        setattr(cls, "intermixed hardwood and conifers",
                PermissibleValue(text="intermixed hardwood and conifers") )
        setattr(cls, "tropical (e.g. mangrove,palms)",
                PermissibleValue(text="tropical (e.g. mangrove,palms)") )
        setattr(cls, "rainforest (evergreen forest receiving greater than 406 cm annual rainfall)",
                PermissibleValue(text="rainforest (evergreen forest receiving greater than 406 cm annual rainfall)") )
        setattr(cls, "swamp (permanent or semi-permanent water body dominated by woody plants)",
                PermissibleValue(text="swamp (permanent or semi-permanent water body dominated by woody plants)") )
        setattr(cls, "crop trees (nuts,fruit,christmas trees,nursery trees)",
                PermissibleValue(text="crop trees (nuts,fruit,christmas trees,nursery trees)") )

class DeposEnvEnum(EnumDefinitionImpl):

    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="DeposEnvEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Continental - Alluvial",
                PermissibleValue(text="Continental - Alluvial") )
        setattr(cls, "Continental - Aeolian",
                PermissibleValue(text="Continental - Aeolian") )
        setattr(cls, "Continental - Fluvial",
                PermissibleValue(text="Continental - Fluvial") )
        setattr(cls, "Continental - Lacustrine",
                PermissibleValue(text="Continental - Lacustrine") )
        setattr(cls, "Transitional - Deltaic",
                PermissibleValue(text="Transitional - Deltaic") )
        setattr(cls, "Transitional - Tidal",
                PermissibleValue(text="Transitional - Tidal") )
        setattr(cls, "Transitional - Lagoonal",
                PermissibleValue(text="Transitional - Lagoonal") )
        setattr(cls, "Transitional - Beach",
                PermissibleValue(text="Transitional - Beach") )
        setattr(cls, "Transitional - Lake",
                PermissibleValue(text="Transitional - Lake") )
        setattr(cls, "Marine - Shallow",
                PermissibleValue(text="Marine - Shallow") )
        setattr(cls, "Marine - Deep",
                PermissibleValue(text="Marine - Deep") )
        setattr(cls, "Marine - Reef",
                PermissibleValue(text="Marine - Reef") )
        setattr(cls, "Other - Evaporite",
                PermissibleValue(text="Other - Evaporite") )
        setattr(cls, "Other - Glacial",
                PermissibleValue(text="Other - Glacial") )
        setattr(cls, "Other - Volcanic",
                PermissibleValue(text="Other - Volcanic") )

class DoorCompTypeEnum(EnumDefinitionImpl):

    revolving = PermissibleValue(text="revolving")
    sliding = PermissibleValue(text="sliding")
    telescopic = PermissibleValue(text="telescopic")

    _defn = EnumDefinition(
        name="DoorCompTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "metal covered",
                PermissibleValue(text="metal covered") )

class DoorCondEnum(EnumDefinitionImpl):

    damaged = PermissibleValue(text="damaged")
    new = PermissibleValue(text="new")
    rupture = PermissibleValue(text="rupture")

    _defn = EnumDefinition(
        name="DoorCondEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "needs repair",
                PermissibleValue(text="needs repair") )
        setattr(cls, "visible wear",
                PermissibleValue(text="visible wear") )

class DoorDirectEnum(EnumDefinitionImpl):

    inward = PermissibleValue(text="inward")
    outward = PermissibleValue(text="outward")
    sideways = PermissibleValue(text="sideways")

    _defn = EnumDefinition(
        name="DoorDirectEnum",
    )

class DoorLocEnum(EnumDefinitionImpl):

    north = PermissibleValue(text="north")
    south = PermissibleValue(text="south")
    east = PermissibleValue(text="east")
    west = PermissibleValue(text="west")

    _defn = EnumDefinition(
        name="DoorLocEnum",
    )

class DoorMatEnum(EnumDefinitionImpl):

    aluminum = PermissibleValue(text="aluminum")
    fiberboard = PermissibleValue(text="fiberboard")
    fiberglass = PermissibleValue(text="fiberglass")
    metal = PermissibleValue(text="metal")
    vinyl = PermissibleValue(text="vinyl")
    wood = PermissibleValue(text="wood")

    _defn = EnumDefinition(
        name="DoorMatEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "cellular PVC",
                PermissibleValue(text="cellular PVC") )
        setattr(cls, "engineered plastic",
                PermissibleValue(text="engineered plastic") )
        setattr(cls, "thermoplastic alloy",
                PermissibleValue(text="thermoplastic alloy") )
        setattr(cls, "wood/plastic composite",
                PermissibleValue(text="wood/plastic composite") )

class DoorMoveEnum(EnumDefinitionImpl):

    collapsible = PermissibleValue(text="collapsible")
    folding = PermissibleValue(text="folding")
    revolving = PermissibleValue(text="revolving")
    sliding = PermissibleValue(text="sliding")
    swinging = PermissibleValue(text="swinging")

    _defn = EnumDefinition(
        name="DoorMoveEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "rolling shutter",
                PermissibleValue(text="rolling shutter") )

class DoorTypeEnum(EnumDefinitionImpl):

    composite = PermissibleValue(text="composite")
    metal = PermissibleValue(text="metal")
    wooden = PermissibleValue(text="wooden")

    _defn = EnumDefinition(
        name="DoorTypeEnum",
    )

class DoorTypeMetalEnum(EnumDefinitionImpl):

    collapsible = PermissibleValue(text="collapsible")
    hollow = PermissibleValue(text="hollow")

    _defn = EnumDefinition(
        name="DoorTypeMetalEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "corrugated steel",
                PermissibleValue(text="corrugated steel") )
        setattr(cls, "rolling shutters",
                PermissibleValue(text="rolling shutters") )
        setattr(cls, "steel plate",
                PermissibleValue(text="steel plate") )

class DoorTypeWoodEnum(EnumDefinitionImpl):

    battened = PermissibleValue(text="battened")
    flush = PermissibleValue(text="flush")
    louvered = PermissibleValue(text="louvered")

    _defn = EnumDefinition(
        name="DoorTypeWoodEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "bettened and ledged",
                PermissibleValue(text="bettened and ledged") )
        setattr(cls, "ledged and braced",
                PermissibleValue(text="ledged and braced") )
        setattr(cls, "ledged and framed",
                PermissibleValue(text="ledged and framed") )
        setattr(cls, "ledged, braced and frame",
                PermissibleValue(text="ledged, braced and frame") )
        setattr(cls, "framed and paneled",
                PermissibleValue(text="framed and paneled") )
        setattr(cls, "glashed or sash",
                PermissibleValue(text="glashed or sash") )
        setattr(cls, "wire gauged",
                PermissibleValue(text="wire gauged") )

class DrainageClassEnum(EnumDefinitionImpl):

    poorly = PermissibleValue(text="poorly")
    well = PermissibleValue(text="well")

    _defn = EnumDefinition(
        name="DrainageClassEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "very poorly",
                PermissibleValue(text="very poorly") )
        setattr(cls, "somewhat poorly",
                PermissibleValue(text="somewhat poorly") )
        setattr(cls, "moderately well",
                PermissibleValue(text="moderately well") )
        setattr(cls, "excessively drained",
                PermissibleValue(text="excessively drained") )

class DrawingsEnum(EnumDefinitionImpl):

    operation = PermissibleValue(text="operation")
    construction = PermissibleValue(text="construction")
    bid = PermissibleValue(text="bid")
    design = PermissibleValue(text="design")
    diagram = PermissibleValue(text="diagram")
    sketch = PermissibleValue(text="sketch")

    _defn = EnumDefinition(
        name="DrawingsEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "as built",
                PermissibleValue(text="as built") )
        setattr(cls, "building navigation map",
                PermissibleValue(text="building navigation map") )

class ExtWallOrientEnum(EnumDefinitionImpl):

    north = PermissibleValue(text="north")
    south = PermissibleValue(text="south")
    east = PermissibleValue(text="east")
    west = PermissibleValue(text="west")
    northeast = PermissibleValue(text="northeast")
    southeast = PermissibleValue(text="southeast")
    southwest = PermissibleValue(text="southwest")
    northwest = PermissibleValue(text="northwest")

    _defn = EnumDefinition(
        name="ExtWallOrientEnum",
    )

class ExtWindowOrientEnum(EnumDefinitionImpl):

    north = PermissibleValue(text="north")
    south = PermissibleValue(text="south")
    east = PermissibleValue(text="east")
    west = PermissibleValue(text="west")
    northeast = PermissibleValue(text="northeast")
    southeast = PermissibleValue(text="southeast")
    southwest = PermissibleValue(text="southwest")
    northwest = PermissibleValue(text="northwest")

    _defn = EnumDefinition(
        name="ExtWindowOrientEnum",
    )

class FaoClassEnum(EnumDefinitionImpl):

    Acrisols = PermissibleValue(text="Acrisols")
    Andosols = PermissibleValue(text="Andosols")
    Arenosols = PermissibleValue(text="Arenosols")
    Cambisols = PermissibleValue(text="Cambisols")
    Chernozems = PermissibleValue(text="Chernozems")
    Ferralsols = PermissibleValue(text="Ferralsols")
    Fluvisols = PermissibleValue(text="Fluvisols")
    Gleysols = PermissibleValue(text="Gleysols")
    Greyzems = PermissibleValue(text="Greyzems")
    Gypsisols = PermissibleValue(text="Gypsisols")
    Histosols = PermissibleValue(text="Histosols")
    Kastanozems = PermissibleValue(text="Kastanozems")
    Lithosols = PermissibleValue(text="Lithosols")
    Luvisols = PermissibleValue(text="Luvisols")
    Nitosols = PermissibleValue(text="Nitosols")
    Phaeozems = PermissibleValue(text="Phaeozems")
    Planosols = PermissibleValue(text="Planosols")
    Podzols = PermissibleValue(text="Podzols")
    Podzoluvisols = PermissibleValue(text="Podzoluvisols")
    Rankers = PermissibleValue(text="Rankers")
    Regosols = PermissibleValue(text="Regosols")
    Rendzinas = PermissibleValue(text="Rendzinas")
    Solonchaks = PermissibleValue(text="Solonchaks")
    Solonetz = PermissibleValue(text="Solonetz")
    Vertisols = PermissibleValue(text="Vertisols")
    Yermosols = PermissibleValue(text="Yermosols")

    _defn = EnumDefinition(
        name="FaoClassEnum",
    )

class FilterTypeEnum(EnumDefinitionImpl):

    HEPA = PermissibleValue(text="HEPA")
    electrostatic = PermissibleValue(text="electrostatic")

    _defn = EnumDefinition(
        name="FilterTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "particulate air filter",
                PermissibleValue(text="particulate air filter") )
        setattr(cls, "chemical air filter",
                PermissibleValue(text="chemical air filter") )
        setattr(cls, "low-MERV pleated media",
                PermissibleValue(text="low-MERV pleated media") )
        setattr(cls, "gas-phase or ultraviolet air treatments",
                PermissibleValue(text="gas-phase or ultraviolet air treatments") )

class FloorCondEnum(EnumDefinitionImpl):

    new = PermissibleValue(text="new")
    damaged = PermissibleValue(text="damaged")
    rupture = PermissibleValue(text="rupture")

    _defn = EnumDefinition(
        name="FloorCondEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "visible wear",
                PermissibleValue(text="visible wear") )
        setattr(cls, "needs repair",
                PermissibleValue(text="needs repair") )

class FloorFinishMatEnum(EnumDefinitionImpl):

    tile = PermissibleValue(text="tile")
    carpet = PermissibleValue(text="carpet")
    rug = PermissibleValue(text="rug")
    lineoleum = PermissibleValue(text="lineoleum")
    stone = PermissibleValue(text="stone")
    bamboo = PermissibleValue(text="bamboo")
    cork = PermissibleValue(text="cork")
    terrazo = PermissibleValue(text="terrazo")
    concrete = PermissibleValue(text="concrete")
    none = PermissibleValue(text="none")
    sealed = PermissibleValue(text="sealed")
    paint = PermissibleValue(text="paint")

    _defn = EnumDefinition(
        name="FloorFinishMatEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "wood strip or parquet",
                PermissibleValue(text="wood strip or parquet") )
        setattr(cls, "laminate wood",
                PermissibleValue(text="laminate wood") )
        setattr(cls, "vinyl composition tile",
                PermissibleValue(text="vinyl composition tile") )
        setattr(cls, "sheet vinyl",
                PermissibleValue(text="sheet vinyl") )
        setattr(cls, "clear finish",
                PermissibleValue(text="clear finish") )
        setattr(cls, "none or unfinished",
                PermissibleValue(text="none or unfinished") )

class FloorStrucEnum(EnumDefinitionImpl):

    balcony = PermissibleValue(text="balcony")
    concrete = PermissibleValue(text="concrete")

    _defn = EnumDefinition(
        name="FloorStrucEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "floating floor",
                PermissibleValue(text="floating floor") )
        setattr(cls, "glass floor",
                PermissibleValue(text="glass floor") )
        setattr(cls, "raised floor",
                PermissibleValue(text="raised floor") )
        setattr(cls, "sprung floor",
                PermissibleValue(text="sprung floor") )
        setattr(cls, "wood-framed",
                PermissibleValue(text="wood-framed") )

class FloorWaterMoldEnum(EnumDefinitionImpl):

    condensation = PermissibleValue(text="condensation")

    _defn = EnumDefinition(
        name="FloorWaterMoldEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "mold odor",
                PermissibleValue(text="mold odor") )
        setattr(cls, "wet floor",
                PermissibleValue(text="wet floor") )
        setattr(cls, "water stains",
                PermissibleValue(text="water stains") )
        setattr(cls, "wall discoloration",
                PermissibleValue(text="wall discoloration") )
        setattr(cls, "floor discoloration",
                PermissibleValue(text="floor discoloration") )
        setattr(cls, "ceiling discoloration",
                PermissibleValue(text="ceiling discoloration") )
        setattr(cls, "peeling paint or wallpaper",
                PermissibleValue(text="peeling paint or wallpaper") )
        setattr(cls, "bulging walls",
                PermissibleValue(text="bulging walls") )

class FreqCleanEnum(EnumDefinitionImpl):

    Daily = PermissibleValue(text="Daily")
    Weekly = PermissibleValue(text="Weekly")
    Monthly = PermissibleValue(text="Monthly")
    Quarterly = PermissibleValue(text="Quarterly")
    Annually = PermissibleValue(text="Annually")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="FreqCleanEnum",
    )

class FurnitureEnum(EnumDefinitionImpl):

    cabinet = PermissibleValue(text="cabinet")
    chair = PermissibleValue(text="chair")
    desks = PermissibleValue(text="desks")

    _defn = EnumDefinition(
        name="FurnitureEnum",
    )

class GenderRestroomEnum(EnumDefinitionImpl):

    female = PermissibleValue(text="female")
    male = PermissibleValue(text="male")
    unisex = PermissibleValue(text="unisex")

    _defn = EnumDefinition(
        name="GenderRestroomEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "all gender",
                PermissibleValue(text="all gender") )
        setattr(cls, "gender neurtral",
                PermissibleValue(text="gender neurtral") )
        setattr(cls, "male and female",
                PermissibleValue(text="male and female") )

class GrowthHabitEnum(EnumDefinitionImpl):

    erect = PermissibleValue(text="erect")
    spreading = PermissibleValue(text="spreading")
    prostrate = PermissibleValue(text="prostrate")

    _defn = EnumDefinition(
        name="GrowthHabitEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "semi-erect",
                PermissibleValue(text="semi-erect") )

class HandidnessEnum(EnumDefinitionImpl):

    ambidexterity = PermissibleValue(text="ambidexterity")

    _defn = EnumDefinition(
        name="HandidnessEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "left handedness",
                PermissibleValue(text="left handedness") )
        setattr(cls, "mixed-handedness",
                PermissibleValue(text="mixed-handedness") )
        setattr(cls, "right handedness",
                PermissibleValue(text="right handedness") )

class HcProducedEnum(EnumDefinitionImpl):

    Oil = PermissibleValue(text="Oil")
    Gas = PermissibleValue(text="Gas")
    Bitumen = PermissibleValue(text="Bitumen")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="HcProducedEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Gas-Condensate",
                PermissibleValue(text="Gas-Condensate") )
        setattr(cls, "Coalbed Methane",
                PermissibleValue(text="Coalbed Methane") )

class HcrEnum(EnumDefinitionImpl):

    Coalbed = PermissibleValue(text="Coalbed")
    Shale = PermissibleValue(text="Shale")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="HcrEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Oil Reservoir",
                PermissibleValue(text="Oil Reservoir") )
        setattr(cls, "Gas Reservoir",
                PermissibleValue(text="Gas Reservoir") )
        setattr(cls, "Oil Sand",
                PermissibleValue(text="Oil Sand") )
        setattr(cls, "Tight Oil Reservoir",
                PermissibleValue(text="Tight Oil Reservoir") )
        setattr(cls, "Tight Gas Reservoir",
                PermissibleValue(text="Tight Gas Reservoir") )

class HcrGeolAgeEnum(EnumDefinitionImpl):

    Archean = PermissibleValue(text="Archean")
    Cambrian = PermissibleValue(text="Cambrian")
    Carboniferous = PermissibleValue(text="Carboniferous")
    Cenozoic = PermissibleValue(text="Cenozoic")
    Cretaceous = PermissibleValue(text="Cretaceous")
    Devonian = PermissibleValue(text="Devonian")
    Jurassic = PermissibleValue(text="Jurassic")
    Mesozoic = PermissibleValue(text="Mesozoic")
    Neogene = PermissibleValue(text="Neogene")
    Ordovician = PermissibleValue(text="Ordovician")
    Paleogene = PermissibleValue(text="Paleogene")
    Paleozoic = PermissibleValue(text="Paleozoic")
    Permian = PermissibleValue(text="Permian")
    Precambrian = PermissibleValue(text="Precambrian")
    Proterozoic = PermissibleValue(text="Proterozoic")
    Silurian = PermissibleValue(text="Silurian")
    Triassic = PermissibleValue(text="Triassic")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="HcrGeolAgeEnum",
    )

class HeatCoolTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="HeatCoolTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "radiant system",
                PermissibleValue(text="radiant system") )
        setattr(cls, "heat pump",
                PermissibleValue(text="heat pump") )
        setattr(cls, "forced air system",
                PermissibleValue(text="forced air system") )
        setattr(cls, "steam forced heat",
                PermissibleValue(text="steam forced heat") )
        setattr(cls, "wood stove",
                PermissibleValue(text="wood stove") )

class HeatDelivLocEnum(EnumDefinitionImpl):

    north = PermissibleValue(text="north")
    south = PermissibleValue(text="south")
    east = PermissibleValue(text="east")
    west = PermissibleValue(text="west")

    _defn = EnumDefinition(
        name="HeatDelivLocEnum",
    )

class HorizonEnum(EnumDefinitionImpl):

    Permafrost = PermissibleValue(text="Permafrost")

    _defn = EnumDefinition(
        name="HorizonEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "O horizon",
                PermissibleValue(text="O horizon") )
        setattr(cls, "A horizon",
                PermissibleValue(text="A horizon") )
        setattr(cls, "E horizon",
                PermissibleValue(text="E horizon") )
        setattr(cls, "B horizon",
                PermissibleValue(text="B horizon") )
        setattr(cls, "C horizon",
                PermissibleValue(text="C horizon") )
        setattr(cls, "R layer",
                PermissibleValue(text="R layer") )

class HostSexEnum(EnumDefinitionImpl):

    female = PermissibleValue(text="female")
    hermaphrodite = PermissibleValue(text="hermaphrodite")
    male = PermissibleValue(text="male")
    neuter = PermissibleValue(text="neuter")

    _defn = EnumDefinition(
        name="HostSexEnum",
    )

class IndoorSpaceEnum(EnumDefinitionImpl):

    bedroom = PermissibleValue(text="bedroom")
    office = PermissibleValue(text="office")
    bathroom = PermissibleValue(text="bathroom")
    foyer = PermissibleValue(text="foyer")
    kitchen = PermissibleValue(text="kitchen")
    hallway = PermissibleValue(text="hallway")
    elevator = PermissibleValue(text="elevator")

    _defn = EnumDefinition(
        name="IndoorSpaceEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "locker room",
                PermissibleValue(text="locker room") )

class IndoorSurfEnum(EnumDefinitionImpl):

    cabinet = PermissibleValue(text="cabinet")
    ceiling = PermissibleValue(text="ceiling")
    door = PermissibleValue(text="door")
    shelving = PermissibleValue(text="shelving")
    window = PermissibleValue(text="window")
    wall = PermissibleValue(text="wall")

    _defn = EnumDefinition(
        name="IndoorSurfEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "counter top",
                PermissibleValue(text="counter top") )
        setattr(cls, "vent cover",
                PermissibleValue(text="vent cover") )

class IntWallCondEnum(EnumDefinitionImpl):

    new = PermissibleValue(text="new")
    damaged = PermissibleValue(text="damaged")
    rupture = PermissibleValue(text="rupture")

    _defn = EnumDefinition(
        name="IntWallCondEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "visible wear",
                PermissibleValue(text="visible wear") )
        setattr(cls, "needs repair",
                PermissibleValue(text="needs repair") )

class LightTypeEnum(EnumDefinitionImpl):

    none = PermissibleValue(text="none")

    _defn = EnumDefinition(
        name="LightTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "natural light",
                PermissibleValue(text="natural light") )
        setattr(cls, "electric light",
                PermissibleValue(text="electric light") )
        setattr(cls, "desk lamp",
                PermissibleValue(text="desk lamp") )
        setattr(cls, "flourescent lights",
                PermissibleValue(text="flourescent lights") )

class LithologyEnum(EnumDefinitionImpl):

    Basement = PermissibleValue(text="Basement")
    Chalk = PermissibleValue(text="Chalk")
    Chert = PermissibleValue(text="Chert")
    Coal = PermissibleValue(text="Coal")
    Conglomerate = PermissibleValue(text="Conglomerate")
    Diatomite = PermissibleValue(text="Diatomite")
    Dolomite = PermissibleValue(text="Dolomite")
    Limestone = PermissibleValue(text="Limestone")
    Sandstone = PermissibleValue(text="Sandstone")
    Shale = PermissibleValue(text="Shale")
    Siltstone = PermissibleValue(text="Siltstone")
    Volcanic = PermissibleValue(text="Volcanic")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="LithologyEnum",
    )

class MechStrucEnum(EnumDefinitionImpl):

    subway = PermissibleValue(text="subway")
    coach = PermissibleValue(text="coach")
    carriage = PermissibleValue(text="carriage")
    elevator = PermissibleValue(text="elevator")
    escalator = PermissibleValue(text="escalator")
    boat = PermissibleValue(text="boat")
    train = PermissibleValue(text="train")
    car = PermissibleValue(text="car")
    bus = PermissibleValue(text="bus")

    _defn = EnumDefinition(
        name="MechStrucEnum",
    )

class OccupDocumentEnum(EnumDefinitionImpl):

    estimate = PermissibleValue(text="estimate")
    videos = PermissibleValue(text="videos")

    _defn = EnumDefinition(
        name="OccupDocumentEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "automated count",
                PermissibleValue(text="automated count") )
        setattr(cls, "manual count",
                PermissibleValue(text="manual count") )

class OrganismCountEnum(EnumDefinitionImpl):

    ATP = PermissibleValue(text="ATP")
    MPN = PermissibleValue(text="MPN")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="OrganismCountEnum",
    )

class OxyStatSampEnum(EnumDefinitionImpl):

    aerobic = PermissibleValue(text="aerobic")
    anaerobic = PermissibleValue(text="anaerobic")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="OxyStatSampEnum",
    )

class PlantGrowthMedEnum(EnumDefinitionImpl):

    perlite = PermissibleValue(text="perlite")
    pumice = PermissibleValue(text="pumice")
    sand = PermissibleValue(text="sand")
    soil = PermissibleValue(text="soil")
    vermiculite = PermissibleValue(text="vermiculite")
    water = PermissibleValue(text="water")

    _defn = EnumDefinition(
        name="PlantGrowthMedEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "other artificial liquid medium",
                PermissibleValue(text="other artificial liquid medium") )
        setattr(cls, "other artificial solid medium",
                PermissibleValue(text="other artificial solid medium") )
        setattr(cls, "peat moss",
                PermissibleValue(text="peat moss") )

class PlantSexEnum(EnumDefinitionImpl):

    Androdioecious = PermissibleValue(text="Androdioecious")
    Androecious = PermissibleValue(text="Androecious")
    Androgynous = PermissibleValue(text="Androgynous")
    Androgynomonoecious = PermissibleValue(text="Androgynomonoecious")
    Andromonoecious = PermissibleValue(text="Andromonoecious")
    Bisexual = PermissibleValue(text="Bisexual")
    Dichogamous = PermissibleValue(text="Dichogamous")
    Diclinous = PermissibleValue(text="Diclinous")
    Dioecious = PermissibleValue(text="Dioecious")
    Gynodioecious = PermissibleValue(text="Gynodioecious")
    Gynoecious = PermissibleValue(text="Gynoecious")
    Gynomonoecious = PermissibleValue(text="Gynomonoecious")
    Hermaphroditic = PermissibleValue(text="Hermaphroditic")
    Imperfect = PermissibleValue(text="Imperfect")
    Monoclinous = PermissibleValue(text="Monoclinous")
    Monoecious = PermissibleValue(text="Monoecious")
    Perfect = PermissibleValue(text="Perfect")
    Polygamodioecious = PermissibleValue(text="Polygamodioecious")
    Polygamomonoecious = PermissibleValue(text="Polygamomonoecious")
    Polygamous = PermissibleValue(text="Polygamous")
    Protandrous = PermissibleValue(text="Protandrous")
    Protogynous = PermissibleValue(text="Protogynous")
    Subandroecious = PermissibleValue(text="Subandroecious")
    Subdioecious = PermissibleValue(text="Subdioecious")
    Subgynoecious = PermissibleValue(text="Subgynoecious")
    Synoecious = PermissibleValue(text="Synoecious")
    Trimonoecious = PermissibleValue(text="Trimonoecious")
    Trioecious = PermissibleValue(text="Trioecious")
    Unisexual = PermissibleValue(text="Unisexual")

    _defn = EnumDefinition(
        name="PlantSexEnum",
    )

class ProfilePositionEnum(EnumDefinitionImpl):

    summit = PermissibleValue(text="summit")
    shoulder = PermissibleValue(text="shoulder")
    backslope = PermissibleValue(text="backslope")
    footslope = PermissibleValue(text="footslope")
    toeslope = PermissibleValue(text="toeslope")

    _defn = EnumDefinition(
        name="ProfilePositionEnum",
    )

class QuadPosEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="QuadPosEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "North side",
                PermissibleValue(text="North side") )
        setattr(cls, "West side",
                PermissibleValue(text="West side") )
        setattr(cls, "South side",
                PermissibleValue(text="South side") )
        setattr(cls, "East side",
                PermissibleValue(text="East side") )

class RelSampLocEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="RelSampLocEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "edge of car",
                PermissibleValue(text="edge of car") )
        setattr(cls, "center of car",
                PermissibleValue(text="center of car") )
        setattr(cls, "under a seat",
                PermissibleValue(text="under a seat") )

class RelToOxygenEnum(EnumDefinitionImpl):

    aerobe = PermissibleValue(text="aerobe")
    anaerobe = PermissibleValue(text="anaerobe")
    facultative = PermissibleValue(text="facultative")
    microaerophilic = PermissibleValue(text="microaerophilic")
    microanaerobe = PermissibleValue(text="microanaerobe")

    _defn = EnumDefinition(
        name="RelToOxygenEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "obligate aerobe",
                PermissibleValue(text="obligate aerobe") )
        setattr(cls, "obligate anaerobe",
                PermissibleValue(text="obligate anaerobe") )

class RoomCondtEnum(EnumDefinitionImpl):

    new = PermissibleValue(text="new")
    damaged = PermissibleValue(text="damaged")
    rupture = PermissibleValue(text="rupture")

    _defn = EnumDefinition(
        name="RoomCondtEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "visible wear",
                PermissibleValue(text="visible wear") )
        setattr(cls, "needs repair",
                PermissibleValue(text="needs repair") )
        setattr(cls, "visible signs of mold/mildew",
                PermissibleValue(text="visible signs of mold/mildew") )

class RoomConnectedEnum(EnumDefinitionImpl):

    attic = PermissibleValue(text="attic")
    bathroom = PermissibleValue(text="bathroom")
    closet = PermissibleValue(text="closet")
    elevator = PermissibleValue(text="elevator")
    hallway = PermissibleValue(text="hallway")
    kitchen = PermissibleValue(text="kitchen")
    office = PermissibleValue(text="office")
    stairwell = PermissibleValue(text="stairwell")

    _defn = EnumDefinition(
        name="RoomConnectedEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "conference room",
                PermissibleValue(text="conference room") )
        setattr(cls, "examining room",
                PermissibleValue(text="examining room") )
        setattr(cls, "mail room",
                PermissibleValue(text="mail room") )

class RoomLocEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="RoomLocEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "corner room",
                PermissibleValue(text="corner room") )
        setattr(cls, "interior room",
                PermissibleValue(text="interior room") )
        setattr(cls, "exterior wall",
                PermissibleValue(text="exterior wall") )

class RoomSampPosEnum(EnumDefinitionImpl):

    center = PermissibleValue(text="center")

    _defn = EnumDefinition(
        name="RoomSampPosEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "north corner",
                PermissibleValue(text="north corner") )
        setattr(cls, "south corner",
                PermissibleValue(text="south corner") )
        setattr(cls, "west corner",
                PermissibleValue(text="west corner") )
        setattr(cls, "east corner",
                PermissibleValue(text="east corner") )
        setattr(cls, "northeast corner",
                PermissibleValue(text="northeast corner") )
        setattr(cls, "northwest corner",
                PermissibleValue(text="northwest corner") )
        setattr(cls, "southeast corner",
                PermissibleValue(text="southeast corner") )
        setattr(cls, "southwest corner",
                PermissibleValue(text="southwest corner") )

class RoomTypeEnum(EnumDefinitionImpl):

    attic = PermissibleValue(text="attic")
    bathroom = PermissibleValue(text="bathroom")
    closet = PermissibleValue(text="closet")
    elevator = PermissibleValue(text="elevator")
    hallway = PermissibleValue(text="hallway")
    kitchen = PermissibleValue(text="kitchen")
    stairwell = PermissibleValue(text="stairwell")
    lobby = PermissibleValue(text="lobby")
    vestibule = PermissibleValue(text="vestibule")
    laboratory_wet = PermissibleValue(text="laboratory_wet")
    laboratory_dry = PermissibleValue(text="laboratory_dry")
    gymnasium = PermissibleValue(text="gymnasium")
    natatorium = PermissibleValue(text="natatorium")
    auditorium = PermissibleValue(text="auditorium")
    lockers = PermissibleValue(text="lockers")
    cafe = PermissibleValue(text="cafe")
    warehouse = PermissibleValue(text="warehouse")

    _defn = EnumDefinition(
        name="RoomTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "conference room",
                PermissibleValue(text="conference room") )
        setattr(cls, "examining room",
                PermissibleValue(text="examining room") )
        setattr(cls, "mail room",
                PermissibleValue(text="mail room") )
        setattr(cls, "private office",
                PermissibleValue(text="private office") )
        setattr(cls, "open office",
                PermissibleValue(text="open office") )
        setattr(cls, ",restroom",
                PermissibleValue(text=",restroom") )
        setattr(cls, "mechanical or electrical room",
                PermissibleValue(text="mechanical or electrical room") )
        setattr(cls, "data center",
                PermissibleValue(text="data center") )

class SampCaptStatusEnum(EnumDefinitionImpl):

    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="SampCaptStatusEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "active surveillance in response to an outbreak",
                PermissibleValue(text="active surveillance in response to an outbreak") )
        setattr(cls, "active surveillance not initiated by an outbreak",
                PermissibleValue(text="active surveillance not initiated by an outbreak") )
        setattr(cls, "farm sample",
                PermissibleValue(text="farm sample") )
        setattr(cls, "market sample",
                PermissibleValue(text="market sample") )

class SampCollectPointEnum(EnumDefinitionImpl):

    well = PermissibleValue(text="well")
    wellhead = PermissibleValue(text="wellhead")
    separator = PermissibleValue(text="separator")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="SampCollectPointEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "test well",
                PermissibleValue(text="test well") )
        setattr(cls, "drilling rig",
                PermissibleValue(text="drilling rig") )
        setattr(cls, "storage tank",
                PermissibleValue(text="storage tank") )

class SampDisStageEnum(EnumDefinitionImpl):

    dissemination = PermissibleValue(text="dissemination")
    infection = PermissibleValue(text="infection")
    inoculation = PermissibleValue(text="inoculation")
    penetration = PermissibleValue(text="penetration")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="SampDisStageEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "growth and reproduction",
                PermissibleValue(text="growth and reproduction") )

class SampFloorEnum(EnumDefinitionImpl):

    basement = PermissibleValue(text="basement")
    lobby = PermissibleValue(text="lobby")

    _defn = EnumDefinition(
        name="SampFloorEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "1st floor",
                PermissibleValue(text="1st floor") )
        setattr(cls, "2nd floor",
                PermissibleValue(text="2nd floor") )

class SampMdEnum(EnumDefinitionImpl):

    DF = PermissibleValue(text="DF")
    RT = PermissibleValue(text="RT")
    KB = PermissibleValue(text="KB")
    MSL = PermissibleValue(text="MSL")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="SampMdEnum",
    )

class SampSubtypeEnum(EnumDefinitionImpl):

    biofilm = PermissibleValue(text="biofilm")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="SampSubtypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "oil phase",
                PermissibleValue(text="oil phase") )
        setattr(cls, "water phase",
                PermissibleValue(text="water phase") )
        setattr(cls, "not applicable",
                PermissibleValue(text="not applicable") )

class SampWeatherEnum(EnumDefinitionImpl):

    cloudy = PermissibleValue(text="cloudy")
    foggy = PermissibleValue(text="foggy")
    hail = PermissibleValue(text="hail")
    rain = PermissibleValue(text="rain")
    snow = PermissibleValue(text="snow")
    sleet = PermissibleValue(text="sleet")
    sunny = PermissibleValue(text="sunny")
    windy = PermissibleValue(text="windy")

    _defn = EnumDefinition(
        name="SampWeatherEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "clear sky",
                PermissibleValue(text="clear sky") )

class SeasonUseEnum(EnumDefinitionImpl):

    Spring = PermissibleValue(text="Spring")
    Summer = PermissibleValue(text="Summer")
    Fall = PermissibleValue(text="Fall")
    Winter = PermissibleValue(text="Winter")

    _defn = EnumDefinition(
        name="SeasonUseEnum",
    )

class SedimentTypeEnum(EnumDefinitionImpl):

    biogenous = PermissibleValue(text="biogenous")
    cosmogenous = PermissibleValue(text="cosmogenous")
    hydrogenous = PermissibleValue(text="hydrogenous")
    lithogenous = PermissibleValue(text="lithogenous")

    _defn = EnumDefinition(
        name="SedimentTypeEnum",
    )

class ShadingDeviceCondEnum(EnumDefinitionImpl):

    damaged = PermissibleValue(text="damaged")
    new = PermissibleValue(text="new")
    rupture = PermissibleValue(text="rupture")

    _defn = EnumDefinition(
        name="ShadingDeviceCondEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "needs repair",
                PermissibleValue(text="needs repair") )
        setattr(cls, "visible wear",
                PermissibleValue(text="visible wear") )

class ShadingDeviceTypeEnum(EnumDefinitionImpl):

    tree = PermissibleValue(text="tree")
    trellis = PermissibleValue(text="trellis")

    _defn = EnumDefinition(
        name="ShadingDeviceTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "bahama shutters",
                PermissibleValue(text="bahama shutters") )
        setattr(cls, "exterior roll blind",
                PermissibleValue(text="exterior roll blind") )
        setattr(cls, "gambrel awning",
                PermissibleValue(text="gambrel awning") )
        setattr(cls, "hood awning",
                PermissibleValue(text="hood awning") )
        setattr(cls, "porchroller awning",
                PermissibleValue(text="porchroller awning") )
        setattr(cls, "sarasota shutters",
                PermissibleValue(text="sarasota shutters") )
        setattr(cls, "slatted aluminum",
                PermissibleValue(text="slatted aluminum") )
        setattr(cls, "solid aluminum awning",
                PermissibleValue(text="solid aluminum awning") )
        setattr(cls, "sun screen",
                PermissibleValue(text="sun screen") )
        setattr(cls, "venetian awning",
                PermissibleValue(text="venetian awning") )

class SoilHorizonEnum(EnumDefinitionImpl):

    Permafrost = PermissibleValue(text="Permafrost")

    _defn = EnumDefinition(
        name="SoilHorizonEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "O horizon",
                PermissibleValue(text="O horizon") )
        setattr(cls, "A horizon",
                PermissibleValue(text="A horizon") )
        setattr(cls, "E horizon",
                PermissibleValue(text="E horizon") )
        setattr(cls, "B horizon",
                PermissibleValue(text="B horizon") )
        setattr(cls, "C horizon",
                PermissibleValue(text="C horizon") )
        setattr(cls, "R layer",
                PermissibleValue(text="R layer") )

class SpecificEnum(EnumDefinitionImpl):

    operation = PermissibleValue(text="operation")
    construction = PermissibleValue(text="construction")
    bid = PermissibleValue(text="bid")
    design = PermissibleValue(text="design")
    photos = PermissibleValue(text="photos")

    _defn = EnumDefinition(
        name="SpecificEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "as built",
                PermissibleValue(text="as built") )

class SrDepEnvEnum(EnumDefinitionImpl):

    Lacustine = PermissibleValue(text="Lacustine")
    Fluvioldeltaic = PermissibleValue(text="Fluvioldeltaic")
    Fluviomarine = PermissibleValue(text="Fluviomarine")
    Marine = PermissibleValue(text="Marine")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="SrDepEnvEnum",
    )

class SrGeolAgeEnum(EnumDefinitionImpl):

    Archean = PermissibleValue(text="Archean")
    Cambrian = PermissibleValue(text="Cambrian")
    Carboniferous = PermissibleValue(text="Carboniferous")
    Cenozoic = PermissibleValue(text="Cenozoic")
    Cretaceous = PermissibleValue(text="Cretaceous")
    Devonian = PermissibleValue(text="Devonian")
    Jurassic = PermissibleValue(text="Jurassic")
    Mesozoic = PermissibleValue(text="Mesozoic")
    Neogene = PermissibleValue(text="Neogene")
    Ordovician = PermissibleValue(text="Ordovician")
    Paleogene = PermissibleValue(text="Paleogene")
    Paleozoic = PermissibleValue(text="Paleozoic")
    Permian = PermissibleValue(text="Permian")
    Precambrian = PermissibleValue(text="Precambrian")
    Proterozoic = PermissibleValue(text="Proterozoic")
    Silurian = PermissibleValue(text="Silurian")
    Triassic = PermissibleValue(text="Triassic")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="SrGeolAgeEnum",
    )

class SrKerogTypeEnum(EnumDefinitionImpl):

    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="SrKerogTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Type I",
                PermissibleValue(text="Type I") )
        setattr(cls, "Type II",
                PermissibleValue(text="Type II") )
        setattr(cls, "Type III",
                PermissibleValue(text="Type III") )
        setattr(cls, "Type IV",
                PermissibleValue(text="Type IV") )

class SrLithologyEnum(EnumDefinitionImpl):

    Clastic = PermissibleValue(text="Clastic")
    Carbonate = PermissibleValue(text="Carbonate")
    Coal = PermissibleValue(text="Coal")
    Biosilicieous = PermissibleValue(text="Biosilicieous")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="SrLithologyEnum",
    )

class SubstructureTypeEnum(EnumDefinitionImpl):

    crawlspace = PermissibleValue(text="crawlspace")
    basement = PermissibleValue(text="basement")

    _defn = EnumDefinition(
        name="SubstructureTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "slab on grade",
                PermissibleValue(text="slab on grade") )

class SurfAirContEnum(EnumDefinitionImpl):

    dust = PermissibleValue(text="dust")
    radon = PermissibleValue(text="radon")
    nutrients = PermissibleValue(text="nutrients")
    biocides = PermissibleValue(text="biocides")

    _defn = EnumDefinition(
        name="SurfAirContEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "organic matter",
                PermissibleValue(text="organic matter") )
        setattr(cls, "particulate matter",
                PermissibleValue(text="particulate matter") )
        setattr(cls, "volatile organic compounds",
                PermissibleValue(text="volatile organic compounds") )
        setattr(cls, "biological contaminants",
                PermissibleValue(text="biological contaminants") )

class SurfMaterialEnum(EnumDefinitionImpl):

    adobe = PermissibleValue(text="adobe")
    carpet = PermissibleValue(text="carpet")
    concrete = PermissibleValue(text="concrete")
    glass = PermissibleValue(text="glass")
    metal = PermissibleValue(text="metal")
    paint = PermissibleValue(text="paint")
    plastic = PermissibleValue(text="plastic")
    stone = PermissibleValue(text="stone")
    stucco = PermissibleValue(text="stucco")
    tile = PermissibleValue(text="tile")
    vinyl = PermissibleValue(text="vinyl")
    wood = PermissibleValue(text="wood")

    _defn = EnumDefinition(
        name="SurfMaterialEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "cinder blocks",
                PermissibleValue(text="cinder blocks") )
        setattr(cls, "hay bales",
                PermissibleValue(text="hay bales") )
        setattr(cls, "stainless steel",
                PermissibleValue(text="stainless steel") )

class TidalStageEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="TidalStageEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "low tide",
                PermissibleValue(text="low tide") )
        setattr(cls, "ebb tide",
                PermissibleValue(text="ebb tide") )
        setattr(cls, "flood tide",
                PermissibleValue(text="flood tide") )
        setattr(cls, "high tide",
                PermissibleValue(text="high tide") )

class TillageEnum(EnumDefinitionImpl):

    drill = PermissibleValue(text="drill")
    chisel = PermissibleValue(text="chisel")
    tined = PermissibleValue(text="tined")
    mouldboard = PermissibleValue(text="mouldboard")

    _defn = EnumDefinition(
        name="TillageEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "cutting disc",
                PermissibleValue(text="cutting disc") )
        setattr(cls, "ridge till",
                PermissibleValue(text="ridge till") )
        setattr(cls, "strip tillage",
                PermissibleValue(text="strip tillage") )
        setattr(cls, "zonal tillage",
                PermissibleValue(text="zonal tillage") )
        setattr(cls, "disc plough",
                PermissibleValue(text="disc plough") )

class TrainLineEnum(EnumDefinitionImpl):

    red = PermissibleValue(text="red")
    green = PermissibleValue(text="green")
    orange = PermissibleValue(text="orange")

    _defn = EnumDefinition(
        name="TrainLineEnum",
    )

class TrainStatLocEnum(EnumDefinitionImpl):

    riverside = PermissibleValue(text="riverside")

    _defn = EnumDefinition(
        name="TrainStatLocEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "south station above ground",
                PermissibleValue(text="south station above ground") )
        setattr(cls, "south station underground",
                PermissibleValue(text="south station underground") )
        setattr(cls, "south station amtrak",
                PermissibleValue(text="south station amtrak") )
        setattr(cls, "forest hills",
                PermissibleValue(text="forest hills") )

class TrainStopLocEnum(EnumDefinitionImpl):

    end = PermissibleValue(text="end")
    mid = PermissibleValue(text="mid")
    downtown = PermissibleValue(text="downtown")

    _defn = EnumDefinition(
        name="TrainStopLocEnum",
    )

class VisMediaEnum(EnumDefinitionImpl):

    photos = PermissibleValue(text="photos")
    videos = PermissibleValue(text="videos")
    interiors = PermissibleValue(text="interiors")
    equipment = PermissibleValue(text="equipment")

    _defn = EnumDefinition(
        name="VisMediaEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "commonly of the building",
                PermissibleValue(text="commonly of the building") )
        setattr(cls, "site context (adjacent buildings, vegetation, terrain, streets)",
                PermissibleValue(text="site context (adjacent buildings, vegetation, terrain, streets)") )
        setattr(cls, "3D scans",
                PermissibleValue(text="3D scans") )

class WallConstTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="WallConstTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "frame construction",
                PermissibleValue(text="frame construction") )
        setattr(cls, "joisted masonry",
                PermissibleValue(text="joisted masonry") )
        setattr(cls, "light noncombustible",
                PermissibleValue(text="light noncombustible") )
        setattr(cls, "masonry noncombustible",
                PermissibleValue(text="masonry noncombustible") )
        setattr(cls, "modified fire resistive",
                PermissibleValue(text="modified fire resistive") )
        setattr(cls, "fire resistive",
                PermissibleValue(text="fire resistive") )

class WallFinishMatEnum(EnumDefinitionImpl):

    plaster = PermissibleValue(text="plaster")
    tile = PermissibleValue(text="tile")
    terrazzo = PermissibleValue(text="terrazzo")
    wood = PermissibleValue(text="wood")
    metal = PermissibleValue(text="metal")
    masonry = PermissibleValue(text="masonry")

    _defn = EnumDefinition(
        name="WallFinishMatEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "gypsum plaster",
                PermissibleValue(text="gypsum plaster") )
        setattr(cls, "veneer plaster",
                PermissibleValue(text="veneer plaster") )
        setattr(cls, "gypsum board",
                PermissibleValue(text="gypsum board") )
        setattr(cls, "stone facing",
                PermissibleValue(text="stone facing") )
        setattr(cls, "acoustical treatment",
                PermissibleValue(text="acoustical treatment") )

class WallLocEnum(EnumDefinitionImpl):

    north = PermissibleValue(text="north")
    south = PermissibleValue(text="south")
    east = PermissibleValue(text="east")
    west = PermissibleValue(text="west")

    _defn = EnumDefinition(
        name="WallLocEnum",
    )

class WallSurfTreatmentEnum(EnumDefinitionImpl):

    painted = PermissibleValue(text="painted")
    paneling = PermissibleValue(text="paneling")
    stucco = PermissibleValue(text="stucco")
    fabric = PermissibleValue(text="fabric")

    _defn = EnumDefinition(
        name="WallSurfTreatmentEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "wall paper",
                PermissibleValue(text="wall paper") )
        setattr(cls, "no treatment",
                PermissibleValue(text="no treatment") )

class WallTextureEnum(EnumDefinitionImpl):

    knockdown = PermissibleValue(text="knockdown")
    popcorn = PermissibleValue(text="popcorn")
    smooth = PermissibleValue(text="smooth")
    swirl = PermissibleValue(text="swirl")

    _defn = EnumDefinition(
        name="WallTextureEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "crows feet",
                PermissibleValue(text="crows feet") )
        setattr(cls, "crows-foot stomp",
                PermissibleValue(text="crows-foot stomp") )
        setattr(cls, "",
                PermissibleValue(text="") )
        setattr(cls, "double skip",
                PermissibleValue(text="double skip") )
        setattr(cls, "hawk and trowel",
                PermissibleValue(text="hawk and trowel") )
        setattr(cls, "orange peel",
                PermissibleValue(text="orange peel") )
        setattr(cls, "rosebud stomp",
                PermissibleValue(text="rosebud stomp") )
        setattr(cls, "Santa-Fe texture",
                PermissibleValue(text="Santa-Fe texture") )
        setattr(cls, "skip trowel",
                PermissibleValue(text="skip trowel") )
        setattr(cls, "stomp knockdown",
                PermissibleValue(text="stomp knockdown") )

class WaterFeatTypeEnum(EnumDefinitionImpl):

    fountain = PermissibleValue(text="fountain")
    pool = PermissibleValue(text="pool")
    stream = PermissibleValue(text="stream")
    waterfall = PermissibleValue(text="waterfall")

    _defn = EnumDefinition(
        name="WaterFeatTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "standing feature",
                PermissibleValue(text="standing feature") )

class WeekdayEnum(EnumDefinitionImpl):

    Monday = PermissibleValue(text="Monday")
    Tuesday = PermissibleValue(text="Tuesday")
    Wednesday = PermissibleValue(text="Wednesday")
    Thursday = PermissibleValue(text="Thursday")
    Friday = PermissibleValue(text="Friday")
    Saturday = PermissibleValue(text="Saturday")
    Sunday = PermissibleValue(text="Sunday")

    _defn = EnumDefinition(
        name="WeekdayEnum",
    )

class WindowCondEnum(EnumDefinitionImpl):

    damaged = PermissibleValue(text="damaged")
    new = PermissibleValue(text="new")
    rupture = PermissibleValue(text="rupture")

    _defn = EnumDefinition(
        name="WindowCondEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "needs repair",
                PermissibleValue(text="needs repair") )
        setattr(cls, "visible wear",
                PermissibleValue(text="visible wear") )

class WindowCoverEnum(EnumDefinitionImpl):

    blinds = PermissibleValue(text="blinds")
    curtains = PermissibleValue(text="curtains")
    none = PermissibleValue(text="none")

    _defn = EnumDefinition(
        name="WindowCoverEnum",
    )

class WindowHorizPosEnum(EnumDefinitionImpl):

    left = PermissibleValue(text="left")
    middle = PermissibleValue(text="middle")
    right = PermissibleValue(text="right")

    _defn = EnumDefinition(
        name="WindowHorizPosEnum",
    )

class WindowLocEnum(EnumDefinitionImpl):

    north = PermissibleValue(text="north")
    south = PermissibleValue(text="south")
    east = PermissibleValue(text="east")
    west = PermissibleValue(text="west")

    _defn = EnumDefinition(
        name="WindowLocEnum",
    )

class WindowMatEnum(EnumDefinitionImpl):

    clad = PermissibleValue(text="clad")
    fiberglass = PermissibleValue(text="fiberglass")
    metal = PermissibleValue(text="metal")
    vinyl = PermissibleValue(text="vinyl")
    wood = PermissibleValue(text="wood")

    _defn = EnumDefinition(
        name="WindowMatEnum",
    )

class WindowTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="WindowTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "single-hung sash window",
                PermissibleValue(text="single-hung sash window") )
        setattr(cls, "horizontal sash window",
                PermissibleValue(text="horizontal sash window") )
        setattr(cls, "fixed window",
                PermissibleValue(text="fixed window") )

class WindowVertPosEnum(EnumDefinitionImpl):

    bottom = PermissibleValue(text="bottom")
    middle = PermissibleValue(text="middle")
    top = PermissibleValue(text="top")
    low = PermissibleValue(text="low")
    high = PermissibleValue(text="high")

    _defn = EnumDefinition(
        name="WindowVertPosEnum",
    )

# Slots
class slots:
    pass

slots.ess_dive_datasets = Slot(uri=NMDC.ess_dive_datasets, name="ess dive datasets", curie=NMDC.curie('ess_dive_datasets'),
                   model_uri=NMDC.ess_dive_datasets, domain=None, range=Optional[Union[str, List[str]]])

slots.has_credit_associations = Slot(uri=PROV.qualifiedAssociation, name="has credit associations", curie=PROV.curie('qualifiedAssociation'),
                   model_uri=NMDC.has_credit_associations, domain=Study, range=Optional[Union[Union[dict, "CreditAssociation"], List[Union[dict, "CreditAssociation"]]]])

slots.study_image = Slot(uri=NMDC.study_image, name="study image", curie=NMDC.curie('study_image'),
                   model_uri=NMDC.study_image, domain=Study, range=Optional[Union[Union[dict, "ImageValue"], List[Union[dict, "ImageValue"]]]])

slots.relevant_protocols = Slot(uri=NMDC.relevant_protocols, name="relevant protocols", curie=NMDC.curie('relevant_protocols'),
                   model_uri=NMDC.relevant_protocols, domain=None, range=Optional[Union[str, List[str]]])

slots.funding_sources = Slot(uri=NMDC.funding_sources, name="funding sources", curie=NMDC.curie('funding_sources'),
                   model_uri=NMDC.funding_sources, domain=None, range=Optional[Union[str, List[str]]])

slots.applied_role = Slot(uri=PROV.hadRole, name="applied role", curie=PROV.curie('hadRole'),
                   model_uri=NMDC.applied_role, domain=CreditAssociation, range=Optional[Union[str, "CreditEnum"]])

slots.applied_roles = Slot(uri=NMDC.applied_roles, name="applied roles", curie=NMDC.curie('applied_roles'),
                   model_uri=NMDC.applied_roles, domain=CreditAssociation, range=Union[Union[str, "CreditEnum"], List[Union[str, "CreditEnum"]]])

slots.applies_to_person = Slot(uri=PROV.agent, name="applies to person", curie=PROV.curie('agent'),
                   model_uri=NMDC.applies_to_person, domain=CreditAssociation, range=Union[dict, "PersonValue"])

slots.object_set = Slot(uri=NMDC.object_set, name="object set", curie=NMDC.curie('object_set'),
                   model_uri=NMDC.object_set, domain=Database, range=Optional[Union[str, List[str]]])

slots.biosample_set = Slot(uri=NMDC.biosample_set, name="biosample set", curie=NMDC.curie('biosample_set'),
                   model_uri=NMDC.biosample_set, domain=Database, range=Optional[Union[Dict[Union[str, BiosampleId], Union[dict, "Biosample"]], List[Union[dict, "Biosample"]]]])

slots.study_set = Slot(uri=NMDC.study_set, name="study set", curie=NMDC.curie('study_set'),
                   model_uri=NMDC.study_set, domain=Database, range=Optional[Union[Dict[Union[str, StudyId], Union[dict, "Study"]], List[Union[dict, "Study"]]]])

slots.data_object_set = Slot(uri=NMDC.data_object_set, name="data object set", curie=NMDC.curie('data_object_set'),
                   model_uri=NMDC.data_object_set, domain=Database, range=Optional[Union[Dict[Union[str, DataObjectId], Union[dict, "DataObject"]], List[Union[dict, "DataObject"]]]])

slots.genome_feature_set = Slot(uri=NMDC.genome_feature_set, name="genome feature set", curie=NMDC.curie('genome_feature_set'),
                   model_uri=NMDC.genome_feature_set, domain=Database, range=Optional[Union[Union[dict, "GenomeFeature"], List[Union[dict, "GenomeFeature"]]]])

slots.functional_annotation_set = Slot(uri=NMDC.functional_annotation_set, name="functional annotation set", curie=NMDC.curie('functional_annotation_set'),
                   model_uri=NMDC.functional_annotation_set, domain=Database, range=Optional[Union[Union[dict, "FunctionalAnnotation"], List[Union[dict, "FunctionalAnnotation"]]]])

slots.activity_set = Slot(uri=NMDC.activity_set, name="activity set", curie=NMDC.curie('activity_set'),
                   model_uri=NMDC.activity_set, domain=Database, range=Optional[Union[Dict[Union[str, WorkflowExecutionActivityId], Union[dict, "WorkflowExecutionActivity"]], List[Union[dict, "WorkflowExecutionActivity"]]]])

slots.mags_activity_set = Slot(uri=NMDC.mags_activity_set, name="mags activity set", curie=NMDC.curie('mags_activity_set'),
                   model_uri=NMDC.mags_activity_set, domain=Database, range=Optional[Union[Dict[Union[str, MAGsAnalysisActivityId], Union[dict, "MAGsAnalysisActivity"]], List[Union[dict, "MAGsAnalysisActivity"]]]])

slots.metabolomics_analysis_activity_set = Slot(uri=NMDC.metabolomics_analysis_activity_set, name="metabolomics analysis activity set", curie=NMDC.curie('metabolomics_analysis_activity_set'),
                   model_uri=NMDC.metabolomics_analysis_activity_set, domain=Database, range=Optional[Union[Dict[Union[str, MetabolomicsAnalysisActivityId], Union[dict, "MetabolomicsAnalysisActivity"]], List[Union[dict, "MetabolomicsAnalysisActivity"]]]])

slots.metaproteomics_analysis_activity_set = Slot(uri=NMDC.metaproteomics_analysis_activity_set, name="metaproteomics analysis activity set", curie=NMDC.curie('metaproteomics_analysis_activity_set'),
                   model_uri=NMDC.metaproteomics_analysis_activity_set, domain=Database, range=Optional[Union[Dict[Union[str, MetaproteomicsAnalysisActivityId], Union[dict, "MetaproteomicsAnalysisActivity"]], List[Union[dict, "MetaproteomicsAnalysisActivity"]]]])

slots.metagenome_annotation_activity_set = Slot(uri=NMDC.metagenome_annotation_activity_set, name="metagenome annotation activity set", curie=NMDC.curie('metagenome_annotation_activity_set'),
                   model_uri=NMDC.metagenome_annotation_activity_set, domain=Database, range=Optional[Union[Dict[Union[str, MetagenomeAnnotationActivityId], Union[dict, "MetagenomeAnnotationActivity"]], List[Union[dict, "MetagenomeAnnotationActivity"]]]])

slots.metagenome_assembly_set = Slot(uri=NMDC.metagenome_assembly_set, name="metagenome assembly set", curie=NMDC.curie('metagenome_assembly_set'),
                   model_uri=NMDC.metagenome_assembly_set, domain=Database, range=Optional[Union[Dict[Union[str, MetagenomeAssemblyId], Union[dict, "MetagenomeAssembly"]], List[Union[dict, "MetagenomeAssembly"]]]])

slots.metatranscriptome_activity_set = Slot(uri=NMDC.metatranscriptome_activity_set, name="metatranscriptome activity set", curie=NMDC.curie('metatranscriptome_activity_set'),
                   model_uri=NMDC.metatranscriptome_activity_set, domain=Database, range=Optional[Union[Dict[Union[str, MetatranscriptomeActivityId], Union[dict, "MetatranscriptomeActivity"]], List[Union[dict, "MetatranscriptomeActivity"]]]])

slots.read_QC_analysis_activity_set = Slot(uri=NMDC.read_QC_analysis_activity_set, name="read QC analysis activity set", curie=NMDC.curie('read_QC_analysis_activity_set'),
                   model_uri=NMDC.read_QC_analysis_activity_set, domain=Database, range=Optional[Union[Dict[Union[str, ReadQCAnalysisActivityId], Union[dict, "ReadQCAnalysisActivity"]], List[Union[dict, "ReadQCAnalysisActivity"]]]])

slots.read_based_analysis_activity_set = Slot(uri=NMDC.read_based_analysis_activity_set, name="read based analysis activity set", curie=NMDC.curie('read_based_analysis_activity_set'),
                   model_uri=NMDC.read_based_analysis_activity_set, domain=Database, range=Optional[Union[Dict[Union[str, ReadBasedAnalysisActivityId], Union[dict, "ReadBasedAnalysisActivity"]], List[Union[dict, "ReadBasedAnalysisActivity"]]]])

slots.nom_analysis_activity_set = Slot(uri=NMDC.nom_analysis_activity_set, name="nom analysis activity set", curie=NMDC.curie('nom_analysis_activity_set'),
                   model_uri=NMDC.nom_analysis_activity_set, domain=Database, range=Optional[Union[Dict[Union[str, NomAnalysisActivityId], Union[dict, "NomAnalysisActivity"]], List[Union[dict, "NomAnalysisActivity"]]]])

slots.omics_processing_set = Slot(uri=NMDC.omics_processing_set, name="omics processing set", curie=NMDC.curie('omics_processing_set'),
                   model_uri=NMDC.omics_processing_set, domain=Database, range=Optional[Union[Dict[Union[str, OmicsProcessingId], Union[dict, "OmicsProcessing"]], List[Union[dict, "OmicsProcessing"]]]])

slots.omics_type = Slot(uri=NMDC.omics_type, name="omics type", curie=NMDC.curie('omics_type'),
                   model_uri=NMDC.omics_type, domain=None, range=Optional[Union[dict, ControlledTermValue]])

slots.data_object_type = Slot(uri=NMDC.data_object_type, name="data object type", curie=NMDC.curie('data_object_type'),
                   model_uri=NMDC.data_object_type, domain=None, range=Optional[Union[str, "FileTypeEnum"]])

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

slots.principal_investigator = Slot(uri=NMDC.principal_investigator, name="principal investigator", curie=NMDC.curie('principal_investigator'),
                   model_uri=NMDC.principal_investigator, domain=None, range=Optional[Union[dict, PersonValue]])

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

slots.depth2 = Slot(uri=NMDC.depth2, name="depth2", curie=NMDC.curie('depth2'),
                   model_uri=NMDC.depth2, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.subsurface_depth = Slot(uri=NMDC.subsurface_depth, name="subsurface_depth", curie=NMDC.curie('subsurface_depth'),
                   model_uri=NMDC.subsurface_depth, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.subsurface_depth2 = Slot(uri=NMDC.subsurface_depth2, name="subsurface_depth2", curie=NMDC.curie('subsurface_depth2'),
                   model_uri=NMDC.subsurface_depth2, domain=None, range=Optional[Union[dict, QuantityValue]])

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

slots.abs_air_humidity = Slot(uri=MIXS['0000122'], name="abs_air_humidity", curie=MIXS.curie('0000122'),
                   model_uri=NMDC.abs_air_humidity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.core_field = Slot(uri="str(uriorcurie)", name="core field", curie=None,
                   model_uri=NMDC.core_field, domain=None, range=Optional[str])

slots.add_recov_method = Slot(uri=MIXS['0001009'], name="add_recov_method", curie=MIXS.curie('0001009'),
                   model_uri=NMDC.add_recov_method, domain=None, range=Optional[Union[dict, TextValue]])

slots.additional_info = Slot(uri=MIXS['0000300'], name="additional_info", curie=MIXS.curie('0000300'),
                   model_uri=NMDC.additional_info, domain=None, range=Optional[Union[dict, TextValue]])

slots.address = Slot(uri=MIXS['0000218'], name="address", curie=MIXS.curie('0000218'),
                   model_uri=NMDC.address, domain=None, range=Optional[Union[dict, TextValue]])

slots.adj_room = Slot(uri=MIXS['0000219'], name="adj_room", curie=MIXS.curie('0000219'),
                   model_uri=NMDC.adj_room, domain=None, range=Optional[Union[dict, TextValue]])

slots.aero_struc = Slot(uri=MIXS['0000773'], name="aero_struc", curie=MIXS.curie('0000773'),
                   model_uri=NMDC.aero_struc, domain=None, range=Optional[Union[dict, TextValue]])

slots.agrochem_addition = Slot(uri=MIXS['0000639'], name="agrochem_addition", curie=MIXS.curie('0000639'),
                   model_uri=NMDC.agrochem_addition, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.air_temp = Slot(uri=MIXS['0000124'], name="air_temp", curie=MIXS.curie('0000124'),
                   model_uri=NMDC.air_temp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.air_temp_regm = Slot(uri=MIXS['0000551'], name="air_temp_regm", curie=MIXS.curie('0000551'),
                   model_uri=NMDC.air_temp_regm, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.al_sat = Slot(uri=MIXS['0000607'], name="al_sat", curie=MIXS.curie('0000607'),
                   model_uri=NMDC.al_sat, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.al_sat_meth = Slot(uri=MIXS['0000324'], name="al_sat_meth", curie=MIXS.curie('0000324'),
                   model_uri=NMDC.al_sat_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.alkalinity = Slot(uri=MIXS['0000421'], name="alkalinity", curie=MIXS.curie('0000421'),
                   model_uri=NMDC.alkalinity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.alkalinity_method = Slot(uri=MIXS['0000298'], name="alkalinity_method", curie=MIXS.curie('0000298'),
                   model_uri=NMDC.alkalinity_method, domain=None, range=Optional[Union[dict, TextValue]])

slots.alkyl_diethers = Slot(uri=MIXS['0000490'], name="alkyl_diethers", curie=MIXS.curie('0000490'),
                   model_uri=NMDC.alkyl_diethers, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.alt = Slot(uri=MIXS['0000094'], name="alt", curie=MIXS.curie('0000094'),
                   model_uri=NMDC.alt, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.environment_field = Slot(uri="str(uriorcurie)", name="environment field", curie=None,
                   model_uri=NMDC.environment_field, domain=None, range=Optional[str])

slots.aminopept_act = Slot(uri=MIXS['0000172'], name="aminopept_act", curie=MIXS.curie('0000172'),
                   model_uri=NMDC.aminopept_act, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.ammonium = Slot(uri=MIXS['0000427'], name="ammonium", curie=MIXS.curie('0000427'),
                   model_uri=NMDC.ammonium, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.amount_light = Slot(uri=MIXS['0000140'], name="amount_light", curie=MIXS.curie('0000140'),
                   model_uri=NMDC.amount_light, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.ances_data = Slot(uri=MIXS['0000247'], name="ances_data", curie=MIXS.curie('0000247'),
                   model_uri=NMDC.ances_data, domain=None, range=Optional[Union[dict, TextValue]])

slots.annual_precpt = Slot(uri=MIXS['0000644'], name="annual_precpt", curie=MIXS.curie('0000644'),
                   model_uri=NMDC.annual_precpt, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.annual_temp = Slot(uri=MIXS['0000642'], name="annual_temp", curie=MIXS.curie('0000642'),
                   model_uri=NMDC.annual_temp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.antibiotic_regm = Slot(uri=MIXS['0000553'], name="antibiotic_regm", curie=MIXS.curie('0000553'),
                   model_uri=NMDC.antibiotic_regm, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.api = Slot(uri=MIXS['0000157'], name="api", curie=MIXS.curie('0000157'),
                   model_uri=NMDC.api, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.arch_struc = Slot(uri=MIXS['0000774'], name="arch_struc", curie=MIXS.curie('0000774'),
                   model_uri=NMDC.arch_struc, domain=None, range=Optional[Union[dict, TextValue]])

slots.aromatics_pc = Slot(uri=MIXS['0000133'], name="aromatics_pc", curie=MIXS.curie('0000133'),
                   model_uri=NMDC.aromatics_pc, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.asphaltenes_pc = Slot(uri=MIXS['0000135'], name="asphaltenes_pc", curie=MIXS.curie('0000135'),
                   model_uri=NMDC.asphaltenes_pc, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.atmospheric_data = Slot(uri=MIXS['0001097'], name="atmospheric_data", curie=MIXS.curie('0001097'),
                   model_uri=NMDC.atmospheric_data, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.avg_dew_point = Slot(uri=MIXS['0000141'], name="avg_dew_point", curie=MIXS.curie('0000141'),
                   model_uri=NMDC.avg_dew_point, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.avg_occup = Slot(uri=MIXS['0000775'], name="avg_occup", curie=MIXS.curie('0000775'),
                   model_uri=NMDC.avg_occup, domain=None, range=Optional[Union[dict, TextValue]])

slots.avg_temp = Slot(uri=MIXS['0000142'], name="avg_temp", curie=MIXS.curie('0000142'),
                   model_uri=NMDC.avg_temp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.bac_prod = Slot(uri=MIXS['0000683'], name="bac_prod", curie=MIXS.curie('0000683'),
                   model_uri=NMDC.bac_prod, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.bac_resp = Slot(uri=MIXS['0000684'], name="bac_resp", curie=MIXS.curie('0000684'),
                   model_uri=NMDC.bac_resp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.bacteria_carb_prod = Slot(uri=MIXS['0000173'], name="bacteria_carb_prod", curie=MIXS.curie('0000173'),
                   model_uri=NMDC.bacteria_carb_prod, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.barometric_press = Slot(uri=MIXS['0000096'], name="barometric_press", curie=MIXS.curie('0000096'),
                   model_uri=NMDC.barometric_press, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.basin = Slot(uri=MIXS['0000290'], name="basin", curie=MIXS.curie('0000290'),
                   model_uri=NMDC.basin, domain=None, range=Optional[Union[dict, TextValue]])

slots.bathroom_count = Slot(uri=MIXS['0000776'], name="bathroom_count", curie=MIXS.curie('0000776'),
                   model_uri=NMDC.bathroom_count, domain=None, range=Optional[Union[dict, TextValue]])

slots.bedroom_count = Slot(uri=MIXS['0000777'], name="bedroom_count", curie=MIXS.curie('0000777'),
                   model_uri=NMDC.bedroom_count, domain=None, range=Optional[Union[dict, TextValue]])

slots.benzene = Slot(uri=MIXS['0000153'], name="benzene", curie=MIXS.curie('0000153'),
                   model_uri=NMDC.benzene, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.biochem_oxygen_dem = Slot(uri=MIXS['0000653'], name="biochem_oxygen_dem", curie=MIXS.curie('0000653'),
                   model_uri=NMDC.biochem_oxygen_dem, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.biocide = Slot(uri=MIXS['0001011'], name="biocide", curie=MIXS.curie('0001011'),
                   model_uri=NMDC.biocide, domain=None, range=Optional[Union[dict, TextValue]])

slots.biocide_admin_method = Slot(uri=MIXS['0000456'], name="biocide_admin_method", curie=MIXS.curie('0000456'),
                   model_uri=NMDC.biocide_admin_method, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.biol_stat = Slot(uri=MIXS['0000858'], name="biol_stat", curie=MIXS.curie('0000858'),
                   model_uri=NMDC.biol_stat, domain=None, range=Optional[Union[dict, TextValue]])

slots.biomass = Slot(uri=MIXS['0000174'], name="biomass", curie=MIXS.curie('0000174'),
                   model_uri=NMDC.biomass, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.biotic_regm = Slot(uri=MIXS['0001038'], name="biotic_regm", curie=MIXS.curie('0001038'),
                   model_uri=NMDC.biotic_regm, domain=None, range=Optional[Union[dict, TextValue]])

slots.biotic_relationship = Slot(uri=MIXS['0000028'], name="biotic_relationship", curie=MIXS.curie('0000028'),
                   model_uri=NMDC.biotic_relationship, domain=None, range=Optional[Union[dict, TextValue]])

slots.nucleic_acid_sequence_source_field = Slot(uri="str(uriorcurie)", name="nucleic acid sequence source field", curie=None,
                   model_uri=NMDC.nucleic_acid_sequence_source_field, domain=None, range=Optional[str])

slots.bishomohopanol = Slot(uri=MIXS['0000175'], name="bishomohopanol", curie=MIXS.curie('0000175'),
                   model_uri=NMDC.bishomohopanol, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.blood_press_diast = Slot(uri=MIXS['0000258'], name="blood_press_diast", curie=MIXS.curie('0000258'),
                   model_uri=NMDC.blood_press_diast, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.blood_press_syst = Slot(uri=MIXS['0000259'], name="blood_press_syst", curie=MIXS.curie('0000259'),
                   model_uri=NMDC.blood_press_syst, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.bromide = Slot(uri=MIXS['0000176'], name="bromide", curie=MIXS.curie('0000176'),
                   model_uri=NMDC.bromide, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.build_docs = Slot(uri=MIXS['0000787'], name="build_docs", curie=MIXS.curie('0000787'),
                   model_uri=NMDC.build_docs, domain=None, range=Optional[Union[dict, TextValue]])

slots.build_occup_type = Slot(uri=MIXS['0000761'], name="build_occup_type", curie=MIXS.curie('0000761'),
                   model_uri=NMDC.build_occup_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.building_setting = Slot(uri=MIXS['0000768'], name="building_setting", curie=MIXS.curie('0000768'),
                   model_uri=NMDC.building_setting, domain=None, range=Optional[Union[dict, TextValue]])

slots.built_struc_age = Slot(uri=MIXS['0000145'], name="built_struc_age", curie=MIXS.curie('0000145'),
                   model_uri=NMDC.built_struc_age, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.built_struc_set = Slot(uri=MIXS['0000778'], name="built_struc_set", curie=MIXS.curie('0000778'),
                   model_uri=NMDC.built_struc_set, domain=None, range=Optional[Union[dict, TextValue]])

slots.built_struc_type = Slot(uri=MIXS['0000721'], name="built_struc_type", curie=MIXS.curie('0000721'),
                   model_uri=NMDC.built_struc_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.calcium = Slot(uri=MIXS['0000432'], name="calcium", curie=MIXS.curie('0000432'),
                   model_uri=NMDC.calcium, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.carb_dioxide = Slot(uri=MIXS['0000097'], name="carb_dioxide", curie=MIXS.curie('0000097'),
                   model_uri=NMDC.carb_dioxide, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.carb_monoxide = Slot(uri=MIXS['0000098'], name="carb_monoxide", curie=MIXS.curie('0000098'),
                   model_uri=NMDC.carb_monoxide, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.carb_nitro_ratio = Slot(uri=MIXS['0000310'], name="carb_nitro_ratio", curie=MIXS.curie('0000310'),
                   model_uri=NMDC.carb_nitro_ratio, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.ceil_area = Slot(uri=MIXS['0000148'], name="ceil_area", curie=MIXS.curie('0000148'),
                   model_uri=NMDC.ceil_area, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.ceil_cond = Slot(uri=MIXS['0000779'], name="ceil_cond", curie=MIXS.curie('0000779'),
                   model_uri=NMDC.ceil_cond, domain=None, range=Optional[Union[dict, TextValue]])

slots.ceil_finish_mat = Slot(uri=MIXS['0000780'], name="ceil_finish_mat", curie=MIXS.curie('0000780'),
                   model_uri=NMDC.ceil_finish_mat, domain=None, range=Optional[Union[dict, TextValue]])

slots.ceil_struc = Slot(uri=MIXS['0000782'], name="ceil_struc", curie=MIXS.curie('0000782'),
                   model_uri=NMDC.ceil_struc, domain=None, range=Optional[Union[dict, TextValue]])

slots.ceil_texture = Slot(uri=MIXS['0000783'], name="ceil_texture", curie=MIXS.curie('0000783'),
                   model_uri=NMDC.ceil_texture, domain=None, range=Optional[Union[dict, TextValue]])

slots.ceil_thermal_mass = Slot(uri=MIXS['0000143'], name="ceil_thermal_mass", curie=MIXS.curie('0000143'),
                   model_uri=NMDC.ceil_thermal_mass, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.ceil_type = Slot(uri=MIXS['0000784'], name="ceil_type", curie=MIXS.curie('0000784'),
                   model_uri=NMDC.ceil_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.ceil_water_mold = Slot(uri=MIXS['0000781'], name="ceil_water_mold", curie=MIXS.curie('0000781'),
                   model_uri=NMDC.ceil_water_mold, domain=None, range=Optional[Union[dict, TextValue]])

slots.chem_administration = Slot(uri=MIXS['0000751'], name="chem_administration", curie=MIXS.curie('0000751'),
                   model_uri=NMDC.chem_administration, domain=None, range=Optional[Union[dict, ControlledTermValue]])

slots.chem_mutagen = Slot(uri=MIXS['0000555'], name="chem_mutagen", curie=MIXS.curie('0000555'),
                   model_uri=NMDC.chem_mutagen, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.chem_oxygen_dem = Slot(uri=MIXS['0000656'], name="chem_oxygen_dem", curie=MIXS.curie('0000656'),
                   model_uri=NMDC.chem_oxygen_dem, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.chem_treat_method = Slot(uri=MIXS['0000457'], name="chem_treat_method", curie=MIXS.curie('0000457'),
                   model_uri=NMDC.chem_treat_method, domain=None, range=Optional[str])

slots.chem_treatment = Slot(uri=MIXS['0001012'], name="chem_treatment", curie=MIXS.curie('0001012'),
                   model_uri=NMDC.chem_treatment, domain=None, range=Optional[Union[dict, TextValue]])

slots.chimera_check = Slot(uri=MIXS['0000052'], name="chimera_check", curie=MIXS.curie('0000052'),
                   model_uri=NMDC.chimera_check, domain=None, range=Optional[Union[dict, TextValue]])

slots.sequencing_field = Slot(uri="str(uriorcurie)", name="sequencing field", curie=None,
                   model_uri=NMDC.sequencing_field, domain=None, range=Optional[str])

slots.chloride = Slot(uri=MIXS['0000429'], name="chloride", curie=MIXS.curie('0000429'),
                   model_uri=NMDC.chloride, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.chlorophyll = Slot(uri=MIXS['0000177'], name="chlorophyll", curie=MIXS.curie('0000177'),
                   model_uri=NMDC.chlorophyll, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.climate_environment = Slot(uri=MIXS['0001040'], name="climate_environment", curie=MIXS.curie('0001040'),
                   model_uri=NMDC.climate_environment, domain=None, range=Optional[Union[dict, TextValue]])

slots.collection_date = Slot(uri=MIXS['0000011'], name="collection_date", curie=MIXS.curie('0000011'),
                   model_uri=NMDC.collection_date, domain=None, range=Optional[Union[dict, TimestampValue]])

slots.conduc = Slot(uri=MIXS['0000692'], name="conduc", curie=MIXS.curie('0000692'),
                   model_uri=NMDC.conduc, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cool_syst_id = Slot(uri=MIXS['0000785'], name="cool_syst_id", curie=MIXS.curie('0000785'),
                   model_uri=NMDC.cool_syst_id, domain=None, range=Optional[Union[dict, TextValue]])

slots.crop_rotation = Slot(uri=MIXS['0000318'], name="crop_rotation", curie=MIXS.curie('0000318'),
                   model_uri=NMDC.crop_rotation, domain=None, range=Optional[Union[dict, TextValue]])

slots.cult_root_med = Slot(uri=MIXS['0001041'], name="cult_root_med", curie=MIXS.curie('0001041'),
                   model_uri=NMDC.cult_root_med, domain=None, range=Optional[Union[dict, TextValue]])

slots.cur_land_use = Slot(uri=MIXS['0001080'], name="cur_land_use", curie=MIXS.curie('0001080'),
                   model_uri=NMDC.cur_land_use, domain=None, range=Optional[Union[dict, TextValue]])

slots.cur_vegetation = Slot(uri=MIXS['0000312'], name="cur_vegetation", curie=MIXS.curie('0000312'),
                   model_uri=NMDC.cur_vegetation, domain=None, range=Optional[Union[dict, TextValue]])

slots.cur_vegetation_meth = Slot(uri=MIXS['0000314'], name="cur_vegetation_meth", curie=MIXS.curie('0000314'),
                   model_uri=NMDC.cur_vegetation_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.date_last_rain = Slot(uri=MIXS['0000786'], name="date_last_rain", curie=MIXS.curie('0000786'),
                   model_uri=NMDC.date_last_rain, domain=None, range=Optional[Union[dict, TimestampValue]])

slots.density = Slot(uri=MIXS['0000435'], name="density", curie=MIXS.curie('0000435'),
                   model_uri=NMDC.density, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.depos_env = Slot(uri=MIXS['0000992'], name="depos_env", curie=MIXS.curie('0000992'),
                   model_uri=NMDC.depos_env, domain=None, range=Optional[Union[dict, TextValue]])

slots.depth = Slot(uri=MIXS['0000018'], name="depth", curie=MIXS.curie('0000018'),
                   model_uri=NMDC.depth, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.dew_point = Slot(uri=MIXS['0000129'], name="dew_point", curie=MIXS.curie('0000129'),
                   model_uri=NMDC.dew_point, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.diether_lipids = Slot(uri=MIXS['0000178'], name="diether_lipids", curie=MIXS.curie('0000178'),
                   model_uri=NMDC.diether_lipids, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.diss_carb_dioxide = Slot(uri=MIXS['0000436'], name="diss_carb_dioxide", curie=MIXS.curie('0000436'),
                   model_uri=NMDC.diss_carb_dioxide, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.diss_hydrogen = Slot(uri=MIXS['0000179'], name="diss_hydrogen", curie=MIXS.curie('0000179'),
                   model_uri=NMDC.diss_hydrogen, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.diss_inorg_carb = Slot(uri=MIXS['0000434'], name="diss_inorg_carb", curie=MIXS.curie('0000434'),
                   model_uri=NMDC.diss_inorg_carb, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.diss_inorg_nitro = Slot(uri=MIXS['0000698'], name="diss_inorg_nitro", curie=MIXS.curie('0000698'),
                   model_uri=NMDC.diss_inorg_nitro, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.diss_inorg_phosp = Slot(uri=MIXS['0000106'], name="diss_inorg_phosp", curie=MIXS.curie('0000106'),
                   model_uri=NMDC.diss_inorg_phosp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.diss_iron = Slot(uri=MIXS['0000139'], name="diss_iron", curie=MIXS.curie('0000139'),
                   model_uri=NMDC.diss_iron, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.diss_org_carb = Slot(uri=MIXS['0000433'], name="diss_org_carb", curie=MIXS.curie('0000433'),
                   model_uri=NMDC.diss_org_carb, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.diss_org_nitro = Slot(uri=MIXS['0000162'], name="diss_org_nitro", curie=MIXS.curie('0000162'),
                   model_uri=NMDC.diss_org_nitro, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.diss_oxygen = Slot(uri=MIXS['0000119'], name="diss_oxygen", curie=MIXS.curie('0000119'),
                   model_uri=NMDC.diss_oxygen, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.diss_oxygen_fluid = Slot(uri=MIXS['0000438'], name="diss_oxygen_fluid", curie=MIXS.curie('0000438'),
                   model_uri=NMDC.diss_oxygen_fluid, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.door_comp_type = Slot(uri=MIXS['0000795'], name="door_comp_type", curie=MIXS.curie('0000795'),
                   model_uri=NMDC.door_comp_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.door_cond = Slot(uri=MIXS['0000788'], name="door_cond", curie=MIXS.curie('0000788'),
                   model_uri=NMDC.door_cond, domain=None, range=Optional[Union[dict, TextValue]])

slots.door_direct = Slot(uri=MIXS['0000789'], name="door_direct", curie=MIXS.curie('0000789'),
                   model_uri=NMDC.door_direct, domain=None, range=Optional[Union[dict, TextValue]])

slots.door_loc = Slot(uri=MIXS['0000790'], name="door_loc", curie=MIXS.curie('0000790'),
                   model_uri=NMDC.door_loc, domain=None, range=Optional[Union[dict, TextValue]])

slots.door_mat = Slot(uri=MIXS['0000791'], name="door_mat", curie=MIXS.curie('0000791'),
                   model_uri=NMDC.door_mat, domain=None, range=Optional[Union[dict, TextValue]])

slots.door_move = Slot(uri=MIXS['0000792'], name="door_move", curie=MIXS.curie('0000792'),
                   model_uri=NMDC.door_move, domain=None, range=Optional[Union[dict, TextValue]])

slots.door_size = Slot(uri=MIXS['0000158'], name="door_size", curie=MIXS.curie('0000158'),
                   model_uri=NMDC.door_size, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.door_type = Slot(uri=MIXS['0000794'], name="door_type", curie=MIXS.curie('0000794'),
                   model_uri=NMDC.door_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.door_type_metal = Slot(uri=MIXS['0000796'], name="door_type_metal", curie=MIXS.curie('0000796'),
                   model_uri=NMDC.door_type_metal, domain=None, range=Optional[Union[dict, TextValue]])

slots.door_type_wood = Slot(uri=MIXS['0000797'], name="door_type_wood", curie=MIXS.curie('0000797'),
                   model_uri=NMDC.door_type_wood, domain=None, range=Optional[Union[dict, TextValue]])

slots.door_water_mold = Slot(uri=MIXS['0000793'], name="door_water_mold", curie=MIXS.curie('0000793'),
                   model_uri=NMDC.door_water_mold, domain=None, range=Optional[Union[dict, TextValue]])

slots.down_par = Slot(uri=MIXS['0000703'], name="down_par", curie=MIXS.curie('0000703'),
                   model_uri=NMDC.down_par, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.drainage_class = Slot(uri=MIXS['0001085'], name="drainage_class", curie=MIXS.curie('0001085'),
                   model_uri=NMDC.drainage_class, domain=None, range=Optional[Union[dict, TextValue]])

slots.drawings = Slot(uri=MIXS['0000798'], name="drawings", curie=MIXS.curie('0000798'),
                   model_uri=NMDC.drawings, domain=None, range=Optional[Union[dict, TextValue]])

slots.efficiency_percent = Slot(uri=MIXS['0000657'], name="efficiency_percent", curie=MIXS.curie('0000657'),
                   model_uri=NMDC.efficiency_percent, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.elev = Slot(uri=MIXS['0000093'], name="elev", curie=MIXS.curie('0000093'),
                   model_uri=NMDC.elev, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.elevator = Slot(uri=MIXS['0000799'], name="elevator", curie=MIXS.curie('0000799'),
                   model_uri=NMDC.elevator, domain=None, range=Optional[Union[dict, TextValue]])

slots.emulsions = Slot(uri=MIXS['0000660'], name="emulsions", curie=MIXS.curie('0000660'),
                   model_uri=NMDC.emulsions, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.env_broad_scale = Slot(uri=MIXS['0000012'], name="env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=NMDC.env_broad_scale, domain=None, range=Optional[Union[dict, ControlledTermValue]])

slots.env_local_scale = Slot(uri=MIXS['0000013'], name="env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=NMDC.env_local_scale, domain=None, range=Optional[Union[dict, ControlledTermValue]])

slots.env_medium = Slot(uri=MIXS['0000014'], name="env_medium", curie=MIXS.curie('0000014'),
                   model_uri=NMDC.env_medium, domain=None, range=Optional[Union[dict, ControlledTermValue]])

slots.escalator = Slot(uri=MIXS['0000800'], name="escalator", curie=MIXS.curie('0000800'),
                   model_uri=NMDC.escalator, domain=None, range=Optional[Union[dict, TextValue]])

slots.ethylbenzene = Slot(uri=MIXS['0000155'], name="ethylbenzene", curie=MIXS.curie('0000155'),
                   model_uri=NMDC.ethylbenzene, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.exp_duct = Slot(uri=MIXS['0000144'], name="exp_duct", curie=MIXS.curie('0000144'),
                   model_uri=NMDC.exp_duct, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.exp_pipe = Slot(uri=MIXS['0000220'], name="exp_pipe", curie=MIXS.curie('0000220'),
                   model_uri=NMDC.exp_pipe, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimental_factor = Slot(uri=MIXS['0000008'], name="experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=NMDC.experimental_factor, domain=None, range=Optional[Union[dict, ControlledTermValue]])

slots.investigation_field = Slot(uri="str(uriorcurie)", name="investigation field", curie=None,
                   model_uri=NMDC.investigation_field, domain=None, range=Optional[str])

slots.ext_door = Slot(uri=MIXS['0000170'], name="ext_door", curie=MIXS.curie('0000170'),
                   model_uri=NMDC.ext_door, domain=None, range=Optional[Union[dict, TextValue]])

slots.ext_wall_orient = Slot(uri=MIXS['0000817'], name="ext_wall_orient", curie=MIXS.curie('0000817'),
                   model_uri=NMDC.ext_wall_orient, domain=None, range=Optional[Union[dict, TextValue]])

slots.ext_window_orient = Slot(uri=MIXS['0000818'], name="ext_window_orient", curie=MIXS.curie('0000818'),
                   model_uri=NMDC.ext_window_orient, domain=None, range=Optional[Union[dict, TextValue]])

slots.extreme_event = Slot(uri=MIXS['0000320'], name="extreme_event", curie=MIXS.curie('0000320'),
                   model_uri=NMDC.extreme_event, domain=None, range=Optional[Union[dict, TimestampValue]])

slots.fao_class = Slot(uri=MIXS['0001083'], name="fao_class", curie=MIXS.curie('0001083'),
                   model_uri=NMDC.fao_class, domain=None, range=Optional[Union[dict, TextValue]])

slots.fertilizer_regm = Slot(uri=MIXS['0000556'], name="fertilizer_regm", curie=MIXS.curie('0000556'),
                   model_uri=NMDC.fertilizer_regm, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.field = Slot(uri=MIXS['0000291'], name="field", curie=MIXS.curie('0000291'),
                   model_uri=NMDC.field, domain=None, range=Optional[Union[dict, TextValue]])

slots.filter_type = Slot(uri=MIXS['0000765'], name="filter_type", curie=MIXS.curie('0000765'),
                   model_uri=NMDC.filter_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.fire = Slot(uri=MIXS['0001086'], name="fire", curie=MIXS.curie('0001086'),
                   model_uri=NMDC.fire, domain=None, range=Optional[Union[dict, TimestampValue]])

slots.fireplace_type = Slot(uri=MIXS['0000802'], name="fireplace_type", curie=MIXS.curie('0000802'),
                   model_uri=NMDC.fireplace_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.flooding = Slot(uri=MIXS['0000319'], name="flooding", curie=MIXS.curie('0000319'),
                   model_uri=NMDC.flooding, domain=None, range=Optional[Union[dict, TimestampValue]])

slots.floor_age = Slot(uri=MIXS['0000164'], name="floor_age", curie=MIXS.curie('0000164'),
                   model_uri=NMDC.floor_age, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.floor_area = Slot(uri=MIXS['0000165'], name="floor_area", curie=MIXS.curie('0000165'),
                   model_uri=NMDC.floor_area, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.floor_cond = Slot(uri=MIXS['0000803'], name="floor_cond", curie=MIXS.curie('0000803'),
                   model_uri=NMDC.floor_cond, domain=None, range=Optional[Union[dict, TextValue]])

slots.floor_count = Slot(uri=MIXS['0000225'], name="floor_count", curie=MIXS.curie('0000225'),
                   model_uri=NMDC.floor_count, domain=None, range=Optional[Union[dict, TextValue]])

slots.floor_finish_mat = Slot(uri=MIXS['0000804'], name="floor_finish_mat", curie=MIXS.curie('0000804'),
                   model_uri=NMDC.floor_finish_mat, domain=None, range=Optional[Union[dict, TextValue]])

slots.floor_struc = Slot(uri=MIXS['0000806'], name="floor_struc", curie=MIXS.curie('0000806'),
                   model_uri=NMDC.floor_struc, domain=None, range=Optional[Union[dict, TextValue]])

slots.floor_thermal_mass = Slot(uri=MIXS['0000166'], name="floor_thermal_mass", curie=MIXS.curie('0000166'),
                   model_uri=NMDC.floor_thermal_mass, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.floor_water_mold = Slot(uri=MIXS['0000805'], name="floor_water_mold", curie=MIXS.curie('0000805'),
                   model_uri=NMDC.floor_water_mold, domain=None, range=Optional[Union[dict, TextValue]])

slots.fluor = Slot(uri=MIXS['0000704'], name="fluor", curie=MIXS.curie('0000704'),
                   model_uri=NMDC.fluor, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.freq_clean = Slot(uri=MIXS['0000226'], name="freq_clean", curie=MIXS.curie('0000226'),
                   model_uri=NMDC.freq_clean, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.freq_cook = Slot(uri=MIXS['0000227'], name="freq_cook", curie=MIXS.curie('0000227'),
                   model_uri=NMDC.freq_cook, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.fungicide_regm = Slot(uri=MIXS['0000557'], name="fungicide_regm", curie=MIXS.curie('0000557'),
                   model_uri=NMDC.fungicide_regm, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.furniture = Slot(uri=MIXS['0000807'], name="furniture", curie=MIXS.curie('0000807'),
                   model_uri=NMDC.furniture, domain=None, range=Optional[Union[dict, TextValue]])

slots.gaseous_environment = Slot(uri=MIXS['0000558'], name="gaseous_environment", curie=MIXS.curie('0000558'),
                   model_uri=NMDC.gaseous_environment, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.gaseous_substances = Slot(uri=MIXS['0000661'], name="gaseous_substances", curie=MIXS.curie('0000661'),
                   model_uri=NMDC.gaseous_substances, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.gender_restroom = Slot(uri=MIXS['0000808'], name="gender_restroom", curie=MIXS.curie('0000808'),
                   model_uri=NMDC.gender_restroom, domain=None, range=Optional[Union[dict, TextValue]])

slots.genetic_mod = Slot(uri=MIXS['0000859'], name="genetic_mod", curie=MIXS.curie('0000859'),
                   model_uri=NMDC.genetic_mod, domain=None, range=Optional[Union[dict, TextValue]])

slots.geo_loc_name = Slot(uri=MIXS['0000010'], name="geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=NMDC.geo_loc_name, domain=None, range=Optional[Union[dict, TextValue]])

slots.glucosidase_act = Slot(uri=MIXS['0000137'], name="glucosidase_act", curie=MIXS.curie('0000137'),
                   model_uri=NMDC.glucosidase_act, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.gravidity = Slot(uri=MIXS['0000875'], name="gravidity", curie=MIXS.curie('0000875'),
                   model_uri=NMDC.gravidity, domain=None, range=Optional[Union[dict, TextValue]])

slots.gravity = Slot(uri=MIXS['0000559'], name="gravity", curie=MIXS.curie('0000559'),
                   model_uri=NMDC.gravity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.growth_facil = Slot(uri=MIXS['0001043'], name="growth_facil", curie=MIXS.curie('0001043'),
                   model_uri=NMDC.growth_facil, domain=None, range=Optional[Union[dict, ControlledTermValue]])

slots.growth_habit = Slot(uri=MIXS['0001044'], name="growth_habit", curie=MIXS.curie('0001044'),
                   model_uri=NMDC.growth_habit, domain=None, range=Optional[Union[dict, TextValue]])

slots.growth_hormone_regm = Slot(uri=MIXS['0000560'], name="growth_hormone_regm", curie=MIXS.curie('0000560'),
                   model_uri=NMDC.growth_hormone_regm, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.hall_count = Slot(uri=MIXS['0000228'], name="hall_count", curie=MIXS.curie('0000228'),
                   model_uri=NMDC.hall_count, domain=None, range=Optional[Union[dict, TextValue]])

slots.handidness = Slot(uri=MIXS['0000809'], name="handidness", curie=MIXS.curie('0000809'),
                   model_uri=NMDC.handidness, domain=None, range=Optional[Union[dict, TextValue]])

slots.hc_produced = Slot(uri=MIXS['0000989'], name="hc_produced", curie=MIXS.curie('0000989'),
                   model_uri=NMDC.hc_produced, domain=None, range=Optional[Union[dict, TextValue]])

slots.hcr = Slot(uri=MIXS['0000988'], name="hcr", curie=MIXS.curie('0000988'),
                   model_uri=NMDC.hcr, domain=None, range=Optional[Union[dict, TextValue]])

slots.hcr_fw_salinity = Slot(uri=MIXS['0000406'], name="hcr_fw_salinity", curie=MIXS.curie('0000406'),
                   model_uri=NMDC.hcr_fw_salinity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.hcr_geol_age = Slot(uri=MIXS['0000993'], name="hcr_geol_age", curie=MIXS.curie('0000993'),
                   model_uri=NMDC.hcr_geol_age, domain=None, range=Optional[Union[dict, TextValue]])

slots.hcr_pressure = Slot(uri=MIXS['0000395'], name="hcr_pressure", curie=MIXS.curie('0000395'),
                   model_uri=NMDC.hcr_pressure, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.hcr_temp = Slot(uri=MIXS['0000393'], name="hcr_temp", curie=MIXS.curie('0000393'),
                   model_uri=NMDC.hcr_temp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.heat_cool_type = Slot(uri=MIXS['0000766'], name="heat_cool_type", curie=MIXS.curie('0000766'),
                   model_uri=NMDC.heat_cool_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.heat_deliv_loc = Slot(uri=MIXS['0000810'], name="heat_deliv_loc", curie=MIXS.curie('0000810'),
                   model_uri=NMDC.heat_deliv_loc, domain=None, range=Optional[Union[dict, TextValue]])

slots.heat_sys_deliv_meth = Slot(uri=MIXS['0000812'], name="heat_sys_deliv_meth", curie=MIXS.curie('0000812'),
                   model_uri=NMDC.heat_sys_deliv_meth, domain=None, range=Optional[str])

slots.heat_system_id = Slot(uri=MIXS['0000833'], name="heat_system_id", curie=MIXS.curie('0000833'),
                   model_uri=NMDC.heat_system_id, domain=None, range=Optional[Union[dict, TextValue]])

slots.heavy_metals = Slot(uri=MIXS['0000652'], name="heavy_metals", curie=MIXS.curie('0000652'),
                   model_uri=NMDC.heavy_metals, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.heavy_metals_meth = Slot(uri=MIXS['0000343'], name="heavy_metals_meth", curie=MIXS.curie('0000343'),
                   model_uri=NMDC.heavy_metals_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.height_carper_fiber = Slot(uri=MIXS['0000167'], name="height_carper_fiber", curie=MIXS.curie('0000167'),
                   model_uri=NMDC.height_carper_fiber, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.herbicide_regm = Slot(uri=MIXS['0000561'], name="herbicide_regm", curie=MIXS.curie('0000561'),
                   model_uri=NMDC.herbicide_regm, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.horizon = Slot(uri=MIXS['0001082'], name="horizon", curie=MIXS.curie('0001082'),
                   model_uri=NMDC.horizon, domain=None, range=Optional[Union[dict, TextValue]])

slots.horizon_meth = Slot(uri=MIXS['0000321'], name="horizon_meth", curie=MIXS.curie('0000321'),
                   model_uri=NMDC.horizon_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.host_age = Slot(uri=MIXS['0000255'], name="host_age", curie=MIXS.curie('0000255'),
                   model_uri=NMDC.host_age, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.host_body_habitat = Slot(uri=MIXS['0000866'], name="host_body_habitat", curie=MIXS.curie('0000866'),
                   model_uri=NMDC.host_body_habitat, domain=None, range=Optional[Union[dict, TextValue]])

slots.host_body_product = Slot(uri=MIXS['0000888'], name="host_body_product", curie=MIXS.curie('0000888'),
                   model_uri=NMDC.host_body_product, domain=None, range=Optional[Union[dict, ControlledTermValue]])

slots.host_body_site = Slot(uri=MIXS['0000867'], name="host_body_site", curie=MIXS.curie('0000867'),
                   model_uri=NMDC.host_body_site, domain=None, range=Optional[Union[dict, ControlledTermValue]])

slots.host_body_temp = Slot(uri=MIXS['0000274'], name="host_body_temp", curie=MIXS.curie('0000274'),
                   model_uri=NMDC.host_body_temp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.host_color = Slot(uri=MIXS['0000260'], name="host_color", curie=MIXS.curie('0000260'),
                   model_uri=NMDC.host_color, domain=None, range=Optional[Union[dict, TextValue]])

slots.host_common_name = Slot(uri=MIXS['0000248'], name="host_common_name", curie=MIXS.curie('0000248'),
                   model_uri=NMDC.host_common_name, domain=None, range=Optional[Union[dict, TextValue]])

slots.host_diet = Slot(uri=MIXS['0000869'], name="host_diet", curie=MIXS.curie('0000869'),
                   model_uri=NMDC.host_diet, domain=None, range=Optional[Union[dict, TextValue]])

slots.host_dry_mass = Slot(uri=MIXS['0000257'], name="host_dry_mass", curie=MIXS.curie('0000257'),
                   model_uri=NMDC.host_dry_mass, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.host_family_relation = Slot(uri=MIXS['0000872'], name="host_family_relation", curie=MIXS.curie('0000872'),
                   model_uri=NMDC.host_family_relation, domain=None, range=Optional[Union[str, List[str]]])

slots.host_genotype = Slot(uri=MIXS['0000365'], name="host_genotype", curie=MIXS.curie('0000365'),
                   model_uri=NMDC.host_genotype, domain=None, range=Optional[Union[dict, TextValue]])

slots.host_growth_cond = Slot(uri=MIXS['0000871'], name="host_growth_cond", curie=MIXS.curie('0000871'),
                   model_uri=NMDC.host_growth_cond, domain=None, range=Optional[Union[dict, TextValue]])

slots.host_height = Slot(uri=MIXS['0000264'], name="host_height", curie=MIXS.curie('0000264'),
                   model_uri=NMDC.host_height, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.host_last_meal = Slot(uri=MIXS['0000870'], name="host_last_meal", curie=MIXS.curie('0000870'),
                   model_uri=NMDC.host_last_meal, domain=None, range=Optional[Union[dict, TextValue]])

slots.host_length = Slot(uri=MIXS['0000256'], name="host_length", curie=MIXS.curie('0000256'),
                   model_uri=NMDC.host_length, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.host_life_stage = Slot(uri=MIXS['0000251'], name="host_life_stage", curie=MIXS.curie('0000251'),
                   model_uri=NMDC.host_life_stage, domain=None, range=Optional[Union[dict, TextValue]])

slots.host_phenotype = Slot(uri=MIXS['0000874'], name="host_phenotype", curie=MIXS.curie('0000874'),
                   model_uri=NMDC.host_phenotype, domain=None, range=Optional[Union[dict, ControlledTermValue]])

slots.host_sex = Slot(uri=MIXS['0000811'], name="host_sex", curie=MIXS.curie('0000811'),
                   model_uri=NMDC.host_sex, domain=None, range=Optional[Union[dict, TextValue]])

slots.host_shape = Slot(uri=MIXS['0000261'], name="host_shape", curie=MIXS.curie('0000261'),
                   model_uri=NMDC.host_shape, domain=None, range=Optional[Union[dict, TextValue]])

slots.host_subject_id = Slot(uri=MIXS['0000861'], name="host_subject_id", curie=MIXS.curie('0000861'),
                   model_uri=NMDC.host_subject_id, domain=None, range=Optional[Union[dict, TextValue]])

slots.host_subspecf_genlin = Slot(uri=MIXS['0001318'], name="host_subspecf_genlin", curie=MIXS.curie('0001318'),
                   model_uri=NMDC.host_subspecf_genlin, domain=None, range=Optional[Union[str, List[str]]])

slots.host_substrate = Slot(uri=MIXS['0000252'], name="host_substrate", curie=MIXS.curie('0000252'),
                   model_uri=NMDC.host_substrate, domain=None, range=Optional[Union[dict, TextValue]])

slots.host_symbiont = Slot(uri=MIXS['0001298'], name="host_symbiont", curie=MIXS.curie('0001298'),
                   model_uri=NMDC.host_symbiont, domain=None, range=Optional[Union[str, List[str]]])

slots.host_taxid = Slot(uri=MIXS['0000250'], name="host_taxid", curie=MIXS.curie('0000250'),
                   model_uri=NMDC.host_taxid, domain=None, range=Optional[Union[dict, TextValue]])

slots.host_tot_mass = Slot(uri=MIXS['0000263'], name="host_tot_mass", curie=MIXS.curie('0000263'),
                   model_uri=NMDC.host_tot_mass, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.host_wet_mass = Slot(uri=MIXS['0000567'], name="host_wet_mass", curie=MIXS.curie('0000567'),
                   model_uri=NMDC.host_wet_mass, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.humidity = Slot(uri=MIXS['0000100'], name="humidity", curie=MIXS.curie('0000100'),
                   model_uri=NMDC.humidity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.humidity_regm = Slot(uri=MIXS['0000568'], name="humidity_regm", curie=MIXS.curie('0000568'),
                   model_uri=NMDC.humidity_regm, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.indoor_space = Slot(uri=MIXS['0000763'], name="indoor_space", curie=MIXS.curie('0000763'),
                   model_uri=NMDC.indoor_space, domain=None, range=Optional[Union[dict, TextValue]])

slots.indoor_surf = Slot(uri=MIXS['0000764'], name="indoor_surf", curie=MIXS.curie('0000764'),
                   model_uri=NMDC.indoor_surf, domain=None, range=Optional[Union[dict, TextValue]])

slots.indust_eff_percent = Slot(uri=MIXS['0000662'], name="indust_eff_percent", curie=MIXS.curie('0000662'),
                   model_uri=NMDC.indust_eff_percent, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.inorg_particles = Slot(uri=MIXS['0000664'], name="inorg_particles", curie=MIXS.curie('0000664'),
                   model_uri=NMDC.inorg_particles, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.inside_lux = Slot(uri=MIXS['0000168'], name="inside_lux", curie=MIXS.curie('0000168'),
                   model_uri=NMDC.inside_lux, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.int_wall_cond = Slot(uri=MIXS['0000813'], name="int_wall_cond", curie=MIXS.curie('0000813'),
                   model_uri=NMDC.int_wall_cond, domain=None, range=Optional[Union[dict, TextValue]])

slots.iw_bt_date_well = Slot(uri=MIXS['0001010'], name="iw_bt_date_well", curie=MIXS.curie('0001010'),
                   model_uri=NMDC.iw_bt_date_well, domain=None, range=Optional[Union[dict, TimestampValue]])

slots.iwf = Slot(uri=MIXS['0000455'], name="iwf", curie=MIXS.curie('0000455'),
                   model_uri=NMDC.iwf, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.last_clean = Slot(uri=MIXS['0000814'], name="last_clean", curie=MIXS.curie('0000814'),
                   model_uri=NMDC.last_clean, domain=None, range=Optional[Union[dict, TimestampValue]])

slots.lat_lon = Slot(uri=MIXS['0000009'], name="lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=NMDC.lat_lon, domain=None, range=Optional[Union[dict, GeolocationValue]])

slots.light_intensity = Slot(uri=MIXS['0000706'], name="light_intensity", curie=MIXS.curie('0000706'),
                   model_uri=NMDC.light_intensity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.light_regm = Slot(uri=MIXS['0000569'], name="light_regm", curie=MIXS.curie('0000569'),
                   model_uri=NMDC.light_regm, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.light_type = Slot(uri=MIXS['0000769'], name="light_type", curie=MIXS.curie('0000769'),
                   model_uri=NMDC.light_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.link_addit_analys = Slot(uri=MIXS['0000340'], name="link_addit_analys", curie=MIXS.curie('0000340'),
                   model_uri=NMDC.link_addit_analys, domain=None, range=Optional[Union[dict, TextValue]])

slots.link_class_info = Slot(uri=MIXS['0000329'], name="link_class_info", curie=MIXS.curie('0000329'),
                   model_uri=NMDC.link_class_info, domain=None, range=Optional[Union[dict, TextValue]])

slots.link_climate_info = Slot(uri=MIXS['0000328'], name="link_climate_info", curie=MIXS.curie('0000328'),
                   model_uri=NMDC.link_climate_info, domain=None, range=Optional[Union[dict, TextValue]])

slots.lithology = Slot(uri=MIXS['0000990'], name="lithology", curie=MIXS.curie('0000990'),
                   model_uri=NMDC.lithology, domain=None, range=Optional[Union[dict, TextValue]])

slots.local_class = Slot(uri=MIXS['0000330'], name="local_class", curie=MIXS.curie('0000330'),
                   model_uri=NMDC.local_class, domain=None, range=Optional[Union[dict, TextValue]])

slots.local_class_meth = Slot(uri=MIXS['0000331'], name="local_class_meth", curie=MIXS.curie('0000331'),
                   model_uri=NMDC.local_class_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.magnesium = Slot(uri=MIXS['0000431'], name="magnesium", curie=MIXS.curie('0000431'),
                   model_uri=NMDC.magnesium, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.max_occup = Slot(uri=MIXS['0000229'], name="max_occup", curie=MIXS.curie('0000229'),
                   model_uri=NMDC.max_occup, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.mean_frict_vel = Slot(uri=MIXS['0000498'], name="mean_frict_vel", curie=MIXS.curie('0000498'),
                   model_uri=NMDC.mean_frict_vel, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.mean_peak_frict_vel = Slot(uri=MIXS['0000502'], name="mean_peak_frict_vel", curie=MIXS.curie('0000502'),
                   model_uri=NMDC.mean_peak_frict_vel, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.mech_struc = Slot(uri=MIXS['0000815'], name="mech_struc", curie=MIXS.curie('0000815'),
                   model_uri=NMDC.mech_struc, domain=None, range=Optional[Union[dict, TextValue]])

slots.mechanical_damage = Slot(uri=MIXS['0001052'], name="mechanical_damage", curie=MIXS.curie('0001052'),
                   model_uri=NMDC.mechanical_damage, domain=None, range=Optional[Union[dict, TextValue]])

slots.methane = Slot(uri=MIXS['0000101'], name="methane", curie=MIXS.curie('0000101'),
                   model_uri=NMDC.methane, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.micro_biomass_meth = Slot(uri=MIXS['0000339'], name="micro_biomass_meth", curie=MIXS.curie('0000339'),
                   model_uri=NMDC.micro_biomass_meth, domain=None, range=Optional[str])

slots.microbial_biomass = Slot(uri=MIXS['0000650'], name="microbial_biomass", curie=MIXS.curie('0000650'),
                   model_uri=NMDC.microbial_biomass, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.microbial_biomass_meth = Slot(uri=MIXS['0000339'], name="microbial_biomass_meth", curie=MIXS.curie('0000339'),
                   model_uri=NMDC.microbial_biomass_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.mineral_nutr_regm = Slot(uri=MIXS['0000570'], name="mineral_nutr_regm", curie=MIXS.curie('0000570'),
                   model_uri=NMDC.mineral_nutr_regm, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.misc_param = Slot(uri=MIXS['0000752'], name="misc_param", curie=MIXS.curie('0000752'),
                   model_uri=NMDC.misc_param, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.n_alkanes = Slot(uri=MIXS['0000503'], name="n_alkanes", curie=MIXS.curie('0000503'),
                   model_uri=NMDC.n_alkanes, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.nitrate = Slot(uri=MIXS['0000425'], name="nitrate", curie=MIXS.curie('0000425'),
                   model_uri=NMDC.nitrate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.nitrite = Slot(uri=MIXS['0000426'], name="nitrite", curie=MIXS.curie('0000426'),
                   model_uri=NMDC.nitrite, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.nitro = Slot(uri=MIXS['0000504'], name="nitro", curie=MIXS.curie('0000504'),
                   model_uri=NMDC.nitro, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.non_min_nutr_regm = Slot(uri=MIXS['0000571'], name="non_min_nutr_regm", curie=MIXS.curie('0000571'),
                   model_uri=NMDC.non_min_nutr_regm, domain=None, range=Optional[Union[str, List[str]]])

slots.nucl_acid_amp = Slot(uri=MIXS['0000038'], name="nucl_acid_amp", curie=MIXS.curie('0000038'),
                   model_uri=NMDC.nucl_acid_amp, domain=None, range=Optional[Union[dict, TextValue]])

slots.nucl_acid_ext = Slot(uri=MIXS['0000037'], name="nucl_acid_ext", curie=MIXS.curie('0000037'),
                   model_uri=NMDC.nucl_acid_ext, domain=None, range=Optional[Union[dict, TextValue]])

slots.number_pets = Slot(uri=MIXS['0000231'], name="number_pets", curie=MIXS.curie('0000231'),
                   model_uri=NMDC.number_pets, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.number_plants = Slot(uri=MIXS['0000230'], name="number_plants", curie=MIXS.curie('0000230'),
                   model_uri=NMDC.number_plants, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.number_resident = Slot(uri=MIXS['0000232'], name="number_resident", curie=MIXS.curie('0000232'),
                   model_uri=NMDC.number_resident, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.occup_density_samp = Slot(uri=MIXS['0000217'], name="occup_density_samp", curie=MIXS.curie('0000217'),
                   model_uri=NMDC.occup_density_samp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.occup_document = Slot(uri=MIXS['0000816'], name="occup_document", curie=MIXS.curie('0000816'),
                   model_uri=NMDC.occup_document, domain=None, range=Optional[Union[dict, TextValue]])

slots.occup_samp = Slot(uri=MIXS['0000772'], name="occup_samp", curie=MIXS.curie('0000772'),
                   model_uri=NMDC.occup_samp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.org_carb = Slot(uri=MIXS['0000508'], name="org_carb", curie=MIXS.curie('0000508'),
                   model_uri=NMDC.org_carb, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.org_count_qpcr_info = Slot(uri=MIXS['0000099'], name="org_count_qpcr_info", curie=MIXS.curie('0000099'),
                   model_uri=NMDC.org_count_qpcr_info, domain=None, range=Optional[str])

slots.org_matter = Slot(uri=MIXS['0000204'], name="org_matter", curie=MIXS.curie('0000204'),
                   model_uri=NMDC.org_matter, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.org_nitro = Slot(uri=MIXS['0000205'], name="org_nitro", curie=MIXS.curie('0000205'),
                   model_uri=NMDC.org_nitro, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.org_particles = Slot(uri=MIXS['0000665'], name="org_particles", curie=MIXS.curie('0000665'),
                   model_uri=NMDC.org_particles, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.organism_count = Slot(uri=MIXS['0000103'], name="organism_count", curie=MIXS.curie('0000103'),
                   model_uri=NMDC.organism_count, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.owc_tvdss = Slot(uri=MIXS['0000405'], name="owc_tvdss", curie=MIXS.curie('0000405'),
                   model_uri=NMDC.owc_tvdss, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.oxy_stat_samp = Slot(uri=MIXS['0000753'], name="oxy_stat_samp", curie=MIXS.curie('0000753'),
                   model_uri=NMDC.oxy_stat_samp, domain=None, range=Optional[Union[dict, TextValue]])

slots.oxygen = Slot(uri=MIXS['0000104'], name="oxygen", curie=MIXS.curie('0000104'),
                   model_uri=NMDC.oxygen, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.part_org_carb = Slot(uri=MIXS['0000515'], name="part_org_carb", curie=MIXS.curie('0000515'),
                   model_uri=NMDC.part_org_carb, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.part_org_nitro = Slot(uri=MIXS['0000719'], name="part_org_nitro", curie=MIXS.curie('0000719'),
                   model_uri=NMDC.part_org_nitro, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.particle_class = Slot(uri=MIXS['0000206'], name="particle_class", curie=MIXS.curie('0000206'),
                   model_uri=NMDC.particle_class, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.pcr_cond = Slot(uri=MIXS['0000049'], name="pcr_cond", curie=MIXS.curie('0000049'),
                   model_uri=NMDC.pcr_cond, domain=None, range=Optional[Union[dict, TextValue]])

slots.pcr_primers = Slot(uri=MIXS['0000046'], name="pcr_primers", curie=MIXS.curie('0000046'),
                   model_uri=NMDC.pcr_primers, domain=None, range=Optional[Union[dict, TextValue]])

slots.permeability = Slot(uri=MIXS['0000404'], name="permeability", curie=MIXS.curie('0000404'),
                   model_uri=NMDC.permeability, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.perturbation = Slot(uri=MIXS['0000754'], name="perturbation", curie=MIXS.curie('0000754'),
                   model_uri=NMDC.perturbation, domain=None, range=Optional[Union[dict, TextValue]])

slots.pesticide_regm = Slot(uri=MIXS['0000573'], name="pesticide_regm", curie=MIXS.curie('0000573'),
                   model_uri=NMDC.pesticide_regm, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.petroleum_hydrocarb = Slot(uri=MIXS['0000516'], name="petroleum_hydrocarb", curie=MIXS.curie('0000516'),
                   model_uri=NMDC.petroleum_hydrocarb, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.ph = Slot(uri=MIXS['0001001'], name="ph", curie=MIXS.curie('0001001'),
                   model_uri=NMDC.ph, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.ph_meth = Slot(uri=MIXS['0001106'], name="ph_meth", curie=MIXS.curie('0001106'),
                   model_uri=NMDC.ph_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.ph_regm = Slot(uri=MIXS['0001056'], name="ph_regm", curie=MIXS.curie('0001056'),
                   model_uri=NMDC.ph_regm, domain=None, range=Optional[Union[dict, TextValue]])

slots.phaeopigments = Slot(uri=MIXS['0000180'], name="phaeopigments", curie=MIXS.curie('0000180'),
                   model_uri=NMDC.phaeopigments, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.phosphate = Slot(uri=MIXS['0000505'], name="phosphate", curie=MIXS.curie('0000505'),
                   model_uri=NMDC.phosphate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.phosplipid_fatt_acid = Slot(uri=MIXS['0000181'], name="phosplipid_fatt_acid", curie=MIXS.curie('0000181'),
                   model_uri=NMDC.phosplipid_fatt_acid, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.photon_flux = Slot(uri=MIXS['0000725'], name="photon_flux", curie=MIXS.curie('0000725'),
                   model_uri=NMDC.photon_flux, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.plant_growth_med = Slot(uri=MIXS['0001057'], name="plant_growth_med", curie=MIXS.curie('0001057'),
                   model_uri=NMDC.plant_growth_med, domain=None, range=Optional[Union[dict, ControlledTermValue]])

slots.plant_product = Slot(uri=MIXS['0001058'], name="plant_product", curie=MIXS.curie('0001058'),
                   model_uri=NMDC.plant_product, domain=None, range=Optional[Union[dict, TextValue]])

slots.plant_sex = Slot(uri=MIXS['0001059'], name="plant_sex", curie=MIXS.curie('0001059'),
                   model_uri=NMDC.plant_sex, domain=None, range=Optional[Union[dict, TextValue]])

slots.plant_struc = Slot(uri=MIXS['0001060'], name="plant_struc", curie=MIXS.curie('0001060'),
                   model_uri=NMDC.plant_struc, domain=None, range=Optional[Union[dict, ControlledTermValue]])

slots.pollutants = Slot(uri=MIXS['0000107'], name="pollutants", curie=MIXS.curie('0000107'),
                   model_uri=NMDC.pollutants, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.pool_dna_extracts = Slot(uri=MIXS['0000325'], name="pool_dna_extracts", curie=MIXS.curie('0000325'),
                   model_uri=NMDC.pool_dna_extracts, domain=None, range=Optional[Union[dict, TextValue]])

slots.porosity = Slot(uri=MIXS['0000211'], name="porosity", curie=MIXS.curie('0000211'),
                   model_uri=NMDC.porosity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.potassium = Slot(uri=MIXS['0000430'], name="potassium", curie=MIXS.curie('0000430'),
                   model_uri=NMDC.potassium, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.pour_point = Slot(uri=MIXS['0000127'], name="pour_point", curie=MIXS.curie('0000127'),
                   model_uri=NMDC.pour_point, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.pre_treatment = Slot(uri=MIXS['0000348'], name="pre_treatment", curie=MIXS.curie('0000348'),
                   model_uri=NMDC.pre_treatment, domain=None, range=Optional[Union[dict, TextValue]])

slots.pres_animal_insect = Slot(uri=MIXS['0000819'], name="pres_animal_insect", curie=MIXS.curie('0000819'),
                   model_uri=NMDC.pres_animal_insect, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(cat|dog|rodent|snake|other);\d+$'))

slots.pressure = Slot(uri=MIXS['0000412'], name="pressure", curie=MIXS.curie('0000412'),
                   model_uri=NMDC.pressure, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.prev_land_use_meth = Slot(uri=MIXS['0000316'], name="prev_land_use_meth", curie=MIXS.curie('0000316'),
                   model_uri=NMDC.prev_land_use_meth, domain=None, range=Optional[str])

slots.previous_land_use = Slot(uri=MIXS['0000315'], name="previous_land_use", curie=MIXS.curie('0000315'),
                   model_uri=NMDC.previous_land_use, domain=None, range=Optional[Union[dict, TextValue]])

slots.previous_land_use_meth = Slot(uri=MIXS['0000316'], name="previous_land_use_meth", curie=MIXS.curie('0000316'),
                   model_uri=NMDC.previous_land_use_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.primary_prod = Slot(uri=MIXS['0000728'], name="primary_prod", curie=MIXS.curie('0000728'),
                   model_uri=NMDC.primary_prod, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.primary_treatment = Slot(uri=MIXS['0000349'], name="primary_treatment", curie=MIXS.curie('0000349'),
                   model_uri=NMDC.primary_treatment, domain=None, range=Optional[Union[dict, TextValue]])

slots.prod_rate = Slot(uri=MIXS['0000452'], name="prod_rate", curie=MIXS.curie('0000452'),
                   model_uri=NMDC.prod_rate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.prod_start_date = Slot(uri=MIXS['0001008'], name="prod_start_date", curie=MIXS.curie('0001008'),
                   model_uri=NMDC.prod_start_date, domain=None, range=Optional[Union[dict, TimestampValue]])

slots.profile_position = Slot(uri=MIXS['0001084'], name="profile_position", curie=MIXS.curie('0001084'),
                   model_uri=NMDC.profile_position, domain=None, range=Optional[Union[dict, TextValue]])

slots.quad_pos = Slot(uri=MIXS['0000820'], name="quad_pos", curie=MIXS.curie('0000820'),
                   model_uri=NMDC.quad_pos, domain=None, range=Optional[Union[dict, TextValue]])

slots.radiation_regm = Slot(uri=MIXS['0000575'], name="radiation_regm", curie=MIXS.curie('0000575'),
                   model_uri=NMDC.radiation_regm, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.rainfall_regm = Slot(uri=MIXS['0000576'], name="rainfall_regm", curie=MIXS.curie('0000576'),
                   model_uri=NMDC.rainfall_regm, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.reactor_type = Slot(uri=MIXS['0000350'], name="reactor_type", curie=MIXS.curie('0000350'),
                   model_uri=NMDC.reactor_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.redox_potential = Slot(uri=MIXS['0000182'], name="redox_potential", curie=MIXS.curie('0000182'),
                   model_uri=NMDC.redox_potential, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.rel_air_humidity = Slot(uri=MIXS['0000121'], name="rel_air_humidity", curie=MIXS.curie('0000121'),
                   model_uri=NMDC.rel_air_humidity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.rel_humidity_out = Slot(uri=MIXS['0000188'], name="rel_humidity_out", curie=MIXS.curie('0000188'),
                   model_uri=NMDC.rel_humidity_out, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.rel_samp_loc = Slot(uri=MIXS['0000821'], name="rel_samp_loc", curie=MIXS.curie('0000821'),
                   model_uri=NMDC.rel_samp_loc, domain=None, range=Optional[Union[dict, TextValue]])

slots.rel_to_oxygen = Slot(uri=MIXS['0000015'], name="rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=NMDC.rel_to_oxygen, domain=None, range=Optional[Union[dict, TextValue]])

slots.reservoir = Slot(uri=MIXS['0000303'], name="reservoir", curie=MIXS.curie('0000303'),
                   model_uri=NMDC.reservoir, domain=None, range=Optional[Union[dict, TextValue]])

slots.resins_pc = Slot(uri=MIXS['0000134'], name="resins_pc", curie=MIXS.curie('0000134'),
                   model_uri=NMDC.resins_pc, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.room_air_exch_rate = Slot(uri=MIXS['0000169'], name="room_air_exch_rate", curie=MIXS.curie('0000169'),
                   model_uri=NMDC.room_air_exch_rate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.room_architec_elem = Slot(uri=MIXS['0000233'], name="room_architec_elem", curie=MIXS.curie('0000233'),
                   model_uri=NMDC.room_architec_elem, domain=None, range=Optional[str])

slots.room_condt = Slot(uri=MIXS['0000822'], name="room_condt", curie=MIXS.curie('0000822'),
                   model_uri=NMDC.room_condt, domain=None, range=Optional[Union[dict, TextValue]])

slots.room_connected = Slot(uri=MIXS['0000826'], name="room_connected", curie=MIXS.curie('0000826'),
                   model_uri=NMDC.room_connected, domain=None, range=Optional[Union[dict, TextValue]])

slots.room_count = Slot(uri=MIXS['0000234'], name="room_count", curie=MIXS.curie('0000234'),
                   model_uri=NMDC.room_count, domain=None, range=Optional[Union[dict, TextValue]])

slots.room_dim = Slot(uri=MIXS['0000192'], name="room_dim", curie=MIXS.curie('0000192'),
                   model_uri=NMDC.room_dim, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.room_door_dist = Slot(uri=MIXS['0000193'], name="room_door_dist", curie=MIXS.curie('0000193'),
                   model_uri=NMDC.room_door_dist, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.room_door_share = Slot(uri=MIXS['0000242'], name="room_door_share", curie=MIXS.curie('0000242'),
                   model_uri=NMDC.room_door_share, domain=None, range=Optional[Union[dict, TextValue]])

slots.room_hallway = Slot(uri=MIXS['0000238'], name="room_hallway", curie=MIXS.curie('0000238'),
                   model_uri=NMDC.room_hallway, domain=None, range=Optional[Union[dict, TextValue]])

slots.room_loc = Slot(uri=MIXS['0000823'], name="room_loc", curie=MIXS.curie('0000823'),
                   model_uri=NMDC.room_loc, domain=None, range=Optional[Union[dict, TextValue]])

slots.room_moist_dam_hist = Slot(uri=MIXS['0000235'], name="room_moist_dam_hist", curie=MIXS.curie('0000235'),
                   model_uri=NMDC.room_moist_dam_hist, domain=None, range=Optional[int])

slots.room_net_area = Slot(uri=MIXS['0000194'], name="room_net_area", curie=MIXS.curie('0000194'),
                   model_uri=NMDC.room_net_area, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.room_occup = Slot(uri=MIXS['0000236'], name="room_occup", curie=MIXS.curie('0000236'),
                   model_uri=NMDC.room_occup, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.room_samp_pos = Slot(uri=MIXS['0000824'], name="room_samp_pos", curie=MIXS.curie('0000824'),
                   model_uri=NMDC.room_samp_pos, domain=None, range=Optional[Union[dict, TextValue]])

slots.room_type = Slot(uri=MIXS['0000825'], name="room_type", curie=MIXS.curie('0000825'),
                   model_uri=NMDC.room_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.room_vol = Slot(uri=MIXS['0000195'], name="room_vol", curie=MIXS.curie('0000195'),
                   model_uri=NMDC.room_vol, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.room_wall_share = Slot(uri=MIXS['0000243'], name="room_wall_share", curie=MIXS.curie('0000243'),
                   model_uri=NMDC.room_wall_share, domain=None, range=Optional[Union[dict, TextValue]])

slots.room_window_count = Slot(uri=MIXS['0000237'], name="room_window_count", curie=MIXS.curie('0000237'),
                   model_uri=NMDC.room_window_count, domain=None, range=Optional[Union[dict, TextValue]])

slots.root_cond = Slot(uri=MIXS['0001061'], name="root_cond", curie=MIXS.curie('0001061'),
                   model_uri=NMDC.root_cond, domain=None, range=Optional[Union[dict, TextValue]])

slots.root_med_carbon = Slot(uri=MIXS['0000577'], name="root_med_carbon", curie=MIXS.curie('0000577'),
                   model_uri=NMDC.root_med_carbon, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.root_med_macronutr = Slot(uri=MIXS['0000578'], name="root_med_macronutr", curie=MIXS.curie('0000578'),
                   model_uri=NMDC.root_med_macronutr, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.root_med_micronutr = Slot(uri=MIXS['0000579'], name="root_med_micronutr", curie=MIXS.curie('0000579'),
                   model_uri=NMDC.root_med_micronutr, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.root_med_ph = Slot(uri=MIXS['0001062'], name="root_med_ph", curie=MIXS.curie('0001062'),
                   model_uri=NMDC.root_med_ph, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.root_med_regl = Slot(uri=MIXS['0000581'], name="root_med_regl", curie=MIXS.curie('0000581'),
                   model_uri=NMDC.root_med_regl, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.root_med_solid = Slot(uri=MIXS['0001063'], name="root_med_solid", curie=MIXS.curie('0001063'),
                   model_uri=NMDC.root_med_solid, domain=None, range=Optional[Union[dict, TextValue]])

slots.root_med_suppl = Slot(uri=MIXS['0000580'], name="root_med_suppl", curie=MIXS.curie('0000580'),
                   model_uri=NMDC.root_med_suppl, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.salinity = Slot(uri=MIXS['0000183'], name="salinity", curie=MIXS.curie('0000183'),
                   model_uri=NMDC.salinity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.salinity_meth = Slot(uri=MIXS['0000341'], name="salinity_meth", curie=MIXS.curie('0000341'),
                   model_uri=NMDC.salinity_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.salt_regm = Slot(uri=MIXS['0000582'], name="salt_regm", curie=MIXS.curie('0000582'),
                   model_uri=NMDC.salt_regm, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samp_capt_status = Slot(uri=MIXS['0000860'], name="samp_capt_status", curie=MIXS.curie('0000860'),
                   model_uri=NMDC.samp_capt_status, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_collec_device = Slot(uri=MIXS['0000002'], name="samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=NMDC.samp_collec_device, domain=None, range=Optional[str])

slots.samp_collec_method = Slot(uri=MIXS['0001225'], name="samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=NMDC.samp_collec_method, domain=None, range=Optional[str])

slots.samp_collect_device = Slot(uri=MIXS['0000002'], name="samp_collect_device", curie=MIXS.curie('0000002'),
                   model_uri=NMDC.samp_collect_device, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_collect_point = Slot(uri=MIXS['0001015'], name="samp_collect_point", curie=MIXS.curie('0001015'),
                   model_uri=NMDC.samp_collect_point, domain=None, range=Optional[Union[str, "SampCollectPointEnum"]])

slots.samp_dis_stage = Slot(uri=MIXS['0000249'], name="samp_dis_stage", curie=MIXS.curie('0000249'),
                   model_uri=NMDC.samp_dis_stage, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_floor = Slot(uri=MIXS['0000828'], name="samp_floor", curie=MIXS.curie('0000828'),
                   model_uri=NMDC.samp_floor, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_loc_corr_rate = Slot(uri=MIXS['0000136'], name="samp_loc_corr_rate", curie=MIXS.curie('0000136'),
                   model_uri=NMDC.samp_loc_corr_rate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samp_mat_process = Slot(uri=MIXS['0000016'], name="samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=NMDC.samp_mat_process, domain=None, range=Optional[Union[dict, ControlledTermValue]])

slots.samp_md = Slot(uri=MIXS['0000413'], name="samp_md", curie=MIXS.curie('0000413'),
                   model_uri=NMDC.samp_md, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samp_name = Slot(uri=MIXS['0001107'], name="samp_name", curie=MIXS.curie('0001107'),
                   model_uri=NMDC.samp_name, domain=None, range=Optional[str])

slots.samp_preserv = Slot(uri=MIXS['0000463'], name="samp_preserv", curie=MIXS.curie('0000463'),
                   model_uri=NMDC.samp_preserv, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samp_room_id = Slot(uri=MIXS['0000244'], name="samp_room_id", curie=MIXS.curie('0000244'),
                   model_uri=NMDC.samp_room_id, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_size = Slot(uri=MIXS['0000001'], name="samp_size", curie=MIXS.curie('0000001'),
                   model_uri=NMDC.samp_size, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samp_sort_meth = Slot(uri=MIXS['0000216'], name="samp_sort_meth", curie=MIXS.curie('0000216'),
                   model_uri=NMDC.samp_sort_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_store_dur = Slot(uri=MIXS['0000116'], name="samp_store_dur", curie=MIXS.curie('0000116'),
                   model_uri=NMDC.samp_store_dur, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_store_loc = Slot(uri=MIXS['0000755'], name="samp_store_loc", curie=MIXS.curie('0000755'),
                   model_uri=NMDC.samp_store_loc, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_store_temp = Slot(uri=MIXS['0000110'], name="samp_store_temp", curie=MIXS.curie('0000110'),
                   model_uri=NMDC.samp_store_temp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samp_subtype = Slot(uri=MIXS['0000999'], name="samp_subtype", curie=MIXS.curie('0000999'),
                   model_uri=NMDC.samp_subtype, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_time_out = Slot(uri=MIXS['0000196'], name="samp_time_out", curie=MIXS.curie('0000196'),
                   model_uri=NMDC.samp_time_out, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_transport_cond = Slot(uri=MIXS['0000410'], name="samp_transport_cond", curie=MIXS.curie('0000410'),
                   model_uri=NMDC.samp_transport_cond, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samp_tvdss = Slot(uri=MIXS['0000409'], name="samp_tvdss", curie=MIXS.curie('0000409'),
                   model_uri=NMDC.samp_tvdss, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samp_type = Slot(uri=MIXS['0000998'], name="samp_type", curie=MIXS.curie('0000998'),
                   model_uri=NMDC.samp_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_vol_we_dna_ext = Slot(uri=MIXS['0000111'], name="samp_vol_we_dna_ext", curie=MIXS.curie('0000111'),
                   model_uri=NMDC.samp_vol_we_dna_ext, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samp_weather = Slot(uri=MIXS['0000827'], name="samp_weather", curie=MIXS.curie('0000827'),
                   model_uri=NMDC.samp_weather, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_well_name = Slot(uri=MIXS['0000296'], name="samp_well_name", curie=MIXS.curie('0000296'),
                   model_uri=NMDC.samp_well_name, domain=None, range=Optional[Union[dict, TextValue]])

slots.saturates_pc = Slot(uri=MIXS['0000131'], name="saturates_pc", curie=MIXS.curie('0000131'),
                   model_uri=NMDC.saturates_pc, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.season = Slot(uri=MIXS['0000829'], name="season", curie=MIXS.curie('0000829'),
                   model_uri=NMDC.season, domain=None, range=Optional[Union[dict, TextValue]])

slots.season_environment = Slot(uri=MIXS['0001068'], name="season_environment", curie=MIXS.curie('0001068'),
                   model_uri=NMDC.season_environment, domain=None, range=Optional[Union[dict, TextValue]])

slots.season_precpt = Slot(uri=MIXS['0000645'], name="season_precpt", curie=MIXS.curie('0000645'),
                   model_uri=NMDC.season_precpt, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.season_temp = Slot(uri=MIXS['0000643'], name="season_temp", curie=MIXS.curie('0000643'),
                   model_uri=NMDC.season_temp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.season_use = Slot(uri=MIXS['0000830'], name="season_use", curie=MIXS.curie('0000830'),
                   model_uri=NMDC.season_use, domain=None, range=Optional[Union[dict, TextValue]])

slots.secondary_treatment = Slot(uri=MIXS['0000351'], name="secondary_treatment", curie=MIXS.curie('0000351'),
                   model_uri=NMDC.secondary_treatment, domain=None, range=Optional[Union[dict, TextValue]])

slots.sediment_type = Slot(uri=MIXS['0001078'], name="sediment_type", curie=MIXS.curie('0001078'),
                   model_uri=NMDC.sediment_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.seq_meth = Slot(uri=MIXS['0000050'], name="seq_meth", curie=MIXS.curie('0000050'),
                   model_uri=NMDC.seq_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.seq_quality_check = Slot(uri=MIXS['0000051'], name="seq_quality_check", curie=MIXS.curie('0000051'),
                   model_uri=NMDC.seq_quality_check, domain=None, range=Optional[Union[dict, TextValue]])

slots.sewage_type = Slot(uri=MIXS['0000215'], name="sewage_type", curie=MIXS.curie('0000215'),
                   model_uri=NMDC.sewage_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.shad_dev_water_mold = Slot(uri=MIXS['0000834'], name="shad_dev_water_mold", curie=MIXS.curie('0000834'),
                   model_uri=NMDC.shad_dev_water_mold, domain=None, range=Optional[str])

slots.shading_device_cond = Slot(uri=MIXS['0000831'], name="shading_device_cond", curie=MIXS.curie('0000831'),
                   model_uri=NMDC.shading_device_cond, domain=None, range=Optional[Union[dict, TextValue]])

slots.shading_device_loc = Slot(uri=MIXS['0000832'], name="shading_device_loc", curie=MIXS.curie('0000832'),
                   model_uri=NMDC.shading_device_loc, domain=None, range=Optional[Union[dict, TextValue]])

slots.shading_device_mat = Slot(uri=MIXS['0000245'], name="shading_device_mat", curie=MIXS.curie('0000245'),
                   model_uri=NMDC.shading_device_mat, domain=None, range=Optional[Union[dict, TextValue]])

slots.shading_device_type = Slot(uri=MIXS['0000835'], name="shading_device_type", curie=MIXS.curie('0000835'),
                   model_uri=NMDC.shading_device_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.sieving = Slot(uri=MIXS['0000322'], name="sieving", curie=MIXS.curie('0000322'),
                   model_uri=NMDC.sieving, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.silicate = Slot(uri=MIXS['0000184'], name="silicate", curie=MIXS.curie('0000184'),
                   model_uri=NMDC.silicate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.size_frac = Slot(uri=MIXS['0000017'], name="size_frac", curie=MIXS.curie('0000017'),
                   model_uri=NMDC.size_frac, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.size_frac_low = Slot(uri=MIXS['0000735'], name="size_frac_low", curie=MIXS.curie('0000735'),
                   model_uri=NMDC.size_frac_low, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.size_frac_up = Slot(uri=MIXS['0000736'], name="size_frac_up", curie=MIXS.curie('0000736'),
                   model_uri=NMDC.size_frac_up, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.slope_aspect = Slot(uri=MIXS['0000647'], name="slope_aspect", curie=MIXS.curie('0000647'),
                   model_uri=NMDC.slope_aspect, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.slope_gradient = Slot(uri=MIXS['0000646'], name="slope_gradient", curie=MIXS.curie('0000646'),
                   model_uri=NMDC.slope_gradient, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.sludge_retent_time = Slot(uri=MIXS['0000669'], name="sludge_retent_time", curie=MIXS.curie('0000669'),
                   model_uri=NMDC.sludge_retent_time, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.sodium = Slot(uri=MIXS['0000428'], name="sodium", curie=MIXS.curie('0000428'),
                   model_uri=NMDC.sodium, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.soil_horizon = Slot(uri=MIXS['0001082'], name="soil_horizon", curie=MIXS.curie('0001082'),
                   model_uri=NMDC.soil_horizon, domain=None, range=Optional[Union[str, "SoilHorizonEnum"]])

slots.soil_text_measure = Slot(uri=MIXS['0000335'], name="soil_text_measure", curie=MIXS.curie('0000335'),
                   model_uri=NMDC.soil_text_measure, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.soil_texture_meth = Slot(uri=MIXS['0000336'], name="soil_texture_meth", curie=MIXS.curie('0000336'),
                   model_uri=NMDC.soil_texture_meth, domain=None, range=Optional[str])

slots.soil_type = Slot(uri=MIXS['0000332'], name="soil_type", curie=MIXS.curie('0000332'),
                   model_uri=NMDC.soil_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.soil_type_meth = Slot(uri=MIXS['0000334'], name="soil_type_meth", curie=MIXS.curie('0000334'),
                   model_uri=NMDC.soil_type_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.solar_irradiance = Slot(uri=MIXS['0000112'], name="solar_irradiance", curie=MIXS.curie('0000112'),
                   model_uri=NMDC.solar_irradiance, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.soluble_inorg_mat = Slot(uri=MIXS['0000672'], name="soluble_inorg_mat", curie=MIXS.curie('0000672'),
                   model_uri=NMDC.soluble_inorg_mat, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.soluble_org_mat = Slot(uri=MIXS['0000673'], name="soluble_org_mat", curie=MIXS.curie('0000673'),
                   model_uri=NMDC.soluble_org_mat, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.soluble_react_phosp = Slot(uri=MIXS['0000738'], name="soluble_react_phosp", curie=MIXS.curie('0000738'),
                   model_uri=NMDC.soluble_react_phosp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.source_mat_id = Slot(uri=MIXS['0000026'], name="source_mat_id", curie=MIXS.curie('0000026'),
                   model_uri=NMDC.source_mat_id, domain=None, range=Optional[Union[dict, TextValue]])

slots.space_typ_state = Slot(uri=MIXS['0000770'], name="space_typ_state", curie=MIXS.curie('0000770'),
                   model_uri=NMDC.space_typ_state, domain=None, range=Optional[Union[dict, TextValue]])

slots.specific = Slot(uri=MIXS['0000836'], name="specific", curie=MIXS.curie('0000836'),
                   model_uri=NMDC.specific, domain=None, range=Optional[Union[dict, TextValue]])

slots.specific_humidity = Slot(uri=MIXS['0000214'], name="specific_humidity", curie=MIXS.curie('0000214'),
                   model_uri=NMDC.specific_humidity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.sr_dep_env = Slot(uri=MIXS['0000996'], name="sr_dep_env", curie=MIXS.curie('0000996'),
                   model_uri=NMDC.sr_dep_env, domain=None, range=Optional[Union[dict, TextValue]])

slots.sr_geol_age = Slot(uri=MIXS['0000997'], name="sr_geol_age", curie=MIXS.curie('0000997'),
                   model_uri=NMDC.sr_geol_age, domain=None, range=Optional[Union[dict, TextValue]])

slots.sr_kerog_type = Slot(uri=MIXS['0000994'], name="sr_kerog_type", curie=MIXS.curie('0000994'),
                   model_uri=NMDC.sr_kerog_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.sr_lithology = Slot(uri=MIXS['0000995'], name="sr_lithology", curie=MIXS.curie('0000995'),
                   model_uri=NMDC.sr_lithology, domain=None, range=Optional[Union[dict, TextValue]])

slots.standing_water_regm = Slot(uri=MIXS['0001069'], name="standing_water_regm", curie=MIXS.curie('0001069'),
                   model_uri=NMDC.standing_water_regm, domain=None, range=Optional[Union[dict, TextValue]])

slots.store_cond = Slot(uri=MIXS['0000327'], name="store_cond", curie=MIXS.curie('0000327'),
                   model_uri=NMDC.store_cond, domain=None, range=Optional[Union[dict, TextValue]])

slots.substructure_type = Slot(uri=MIXS['0000767'], name="substructure_type", curie=MIXS.curie('0000767'),
                   model_uri=NMDC.substructure_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.sulfate = Slot(uri=MIXS['0000423'], name="sulfate", curie=MIXS.curie('0000423'),
                   model_uri=NMDC.sulfate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.sulfate_fw = Slot(uri=MIXS['0000407'], name="sulfate_fw", curie=MIXS.curie('0000407'),
                   model_uri=NMDC.sulfate_fw, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.sulfide = Slot(uri=MIXS['0000424'], name="sulfide", curie=MIXS.curie('0000424'),
                   model_uri=NMDC.sulfide, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.surf_air_cont = Slot(uri=MIXS['0000759'], name="surf_air_cont", curie=MIXS.curie('0000759'),
                   model_uri=NMDC.surf_air_cont, domain=None, range=Optional[Union[dict, TextValue]])

slots.surf_humidity = Slot(uri=MIXS['0000123'], name="surf_humidity", curie=MIXS.curie('0000123'),
                   model_uri=NMDC.surf_humidity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.surf_material = Slot(uri=MIXS['0000758'], name="surf_material", curie=MIXS.curie('0000758'),
                   model_uri=NMDC.surf_material, domain=None, range=Optional[Union[dict, TextValue]])

slots.surf_moisture = Slot(uri=MIXS['0000128'], name="surf_moisture", curie=MIXS.curie('0000128'),
                   model_uri=NMDC.surf_moisture, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.surf_moisture_ph = Slot(uri=MIXS['0000760'], name="surf_moisture_ph", curie=MIXS.curie('0000760'),
                   model_uri=NMDC.surf_moisture_ph, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.surf_temp = Slot(uri=MIXS['0000125'], name="surf_temp", curie=MIXS.curie('0000125'),
                   model_uri=NMDC.surf_temp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.suspend_part_matter = Slot(uri=MIXS['0000741'], name="suspend_part_matter", curie=MIXS.curie('0000741'),
                   model_uri=NMDC.suspend_part_matter, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.suspend_solids = Slot(uri=MIXS['0000150'], name="suspend_solids", curie=MIXS.curie('0000150'),
                   model_uri=NMDC.suspend_solids, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tan = Slot(uri=MIXS['0000120'], name="tan", curie=MIXS.curie('0000120'),
                   model_uri=NMDC.tan, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.target_gene = Slot(uri=MIXS['0000044'], name="target_gene", curie=MIXS.curie('0000044'),
                   model_uri=NMDC.target_gene, domain=None, range=Optional[Union[dict, TextValue]])

slots.target_subfragment = Slot(uri=MIXS['0000045'], name="target_subfragment", curie=MIXS.curie('0000045'),
                   model_uri=NMDC.target_subfragment, domain=None, range=Optional[Union[dict, TextValue]])

slots.temp = Slot(uri=MIXS['0000113'], name="temp", curie=MIXS.curie('0000113'),
                   model_uri=NMDC.temp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.temp_out = Slot(uri=MIXS['0000197'], name="temp_out", curie=MIXS.curie('0000197'),
                   model_uri=NMDC.temp_out, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tertiary_treatment = Slot(uri=MIXS['0000352'], name="tertiary_treatment", curie=MIXS.curie('0000352'),
                   model_uri=NMDC.tertiary_treatment, domain=None, range=Optional[Union[dict, TextValue]])

slots.texture = Slot(uri=MIXS['0000335'], name="texture", curie=MIXS.curie('0000335'),
                   model_uri=NMDC.texture, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.texture_meth = Slot(uri=MIXS['0000336'], name="texture_meth", curie=MIXS.curie('0000336'),
                   model_uri=NMDC.texture_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.tidal_stage = Slot(uri=MIXS['0000750'], name="tidal_stage", curie=MIXS.curie('0000750'),
                   model_uri=NMDC.tidal_stage, domain=None, range=Optional[Union[dict, TextValue]])

slots.tillage = Slot(uri=MIXS['0001081'], name="tillage", curie=MIXS.curie('0001081'),
                   model_uri=NMDC.tillage, domain=None, range=Optional[Union[dict, TextValue]])

slots.tiss_cult_growth_med = Slot(uri=MIXS['0001070'], name="tiss_cult_growth_med", curie=MIXS.curie('0001070'),
                   model_uri=NMDC.tiss_cult_growth_med, domain=None, range=Optional[Union[dict, TextValue]])

slots.toluene = Slot(uri=MIXS['0000154'], name="toluene", curie=MIXS.curie('0000154'),
                   model_uri=NMDC.toluene, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tot_carb = Slot(uri=MIXS['0000525'], name="tot_carb", curie=MIXS.curie('0000525'),
                   model_uri=NMDC.tot_carb, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tot_depth_water_col = Slot(uri=MIXS['0000634'], name="tot_depth_water_col", curie=MIXS.curie('0000634'),
                   model_uri=NMDC.tot_depth_water_col, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tot_diss_nitro = Slot(uri=MIXS['0000744'], name="tot_diss_nitro", curie=MIXS.curie('0000744'),
                   model_uri=NMDC.tot_diss_nitro, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tot_inorg_nitro = Slot(uri=MIXS['0000745'], name="tot_inorg_nitro", curie=MIXS.curie('0000745'),
                   model_uri=NMDC.tot_inorg_nitro, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tot_iron = Slot(uri=MIXS['0000105'], name="tot_iron", curie=MIXS.curie('0000105'),
                   model_uri=NMDC.tot_iron, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tot_nitro = Slot(uri=MIXS['0000102'], name="tot_nitro", curie=MIXS.curie('0000102'),
                   model_uri=NMDC.tot_nitro, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tot_nitro_cont_meth = Slot(uri=MIXS['0000338'], name="tot_nitro_cont_meth", curie=MIXS.curie('0000338'),
                   model_uri=NMDC.tot_nitro_cont_meth, domain=None, range=Optional[str])

slots.tot_nitro_content = Slot(uri=MIXS['0000530'], name="tot_nitro_content", curie=MIXS.curie('0000530'),
                   model_uri=NMDC.tot_nitro_content, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tot_org_c_meth = Slot(uri=MIXS['0000337'], name="tot_org_c_meth", curie=MIXS.curie('0000337'),
                   model_uri=NMDC.tot_org_c_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.tot_org_carb = Slot(uri=MIXS['0000533'], name="tot_org_carb", curie=MIXS.curie('0000533'),
                   model_uri=NMDC.tot_org_carb, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tot_part_carb = Slot(uri=MIXS['0000747'], name="tot_part_carb", curie=MIXS.curie('0000747'),
                   model_uri=NMDC.tot_part_carb, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tot_phosp = Slot(uri=MIXS['0000117'], name="tot_phosp", curie=MIXS.curie('0000117'),
                   model_uri=NMDC.tot_phosp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tot_phosphate = Slot(uri=MIXS['0000689'], name="tot_phosphate", curie=MIXS.curie('0000689'),
                   model_uri=NMDC.tot_phosphate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tot_sulfur = Slot(uri=MIXS['0000419'], name="tot_sulfur", curie=MIXS.curie('0000419'),
                   model_uri=NMDC.tot_sulfur, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.train_line = Slot(uri=MIXS['0000837'], name="train_line", curie=MIXS.curie('0000837'),
                   model_uri=NMDC.train_line, domain=None, range=Optional[Union[dict, TextValue]])

slots.train_stat_loc = Slot(uri=MIXS['0000838'], name="train_stat_loc", curie=MIXS.curie('0000838'),
                   model_uri=NMDC.train_stat_loc, domain=None, range=Optional[Union[dict, TextValue]])

slots.train_stop_loc = Slot(uri=MIXS['0000839'], name="train_stop_loc", curie=MIXS.curie('0000839'),
                   model_uri=NMDC.train_stop_loc, domain=None, range=Optional[Union[dict, TextValue]])

slots.turbidity = Slot(uri=MIXS['0000191'], name="turbidity", curie=MIXS.curie('0000191'),
                   model_uri=NMDC.turbidity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tvdss_of_hcr_press = Slot(uri=MIXS['0000397'], name="tvdss_of_hcr_press", curie=MIXS.curie('0000397'),
                   model_uri=NMDC.tvdss_of_hcr_press, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tvdss_of_hcr_temp = Slot(uri=MIXS['0000394'], name="tvdss_of_hcr_temp", curie=MIXS.curie('0000394'),
                   model_uri=NMDC.tvdss_of_hcr_temp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.typ_occup_density = Slot(uri=MIXS['0000771'], name="typ_occup_density", curie=MIXS.curie('0000771'),
                   model_uri=NMDC.typ_occup_density, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.ventilation_rate = Slot(uri=MIXS['0000114'], name="ventilation_rate", curie=MIXS.curie('0000114'),
                   model_uri=NMDC.ventilation_rate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.ventilation_type = Slot(uri=MIXS['0000756'], name="ventilation_type", curie=MIXS.curie('0000756'),
                   model_uri=NMDC.ventilation_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.vfa = Slot(uri=MIXS['0000152'], name="vfa", curie=MIXS.curie('0000152'),
                   model_uri=NMDC.vfa, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.vfa_fw = Slot(uri=MIXS['0000408'], name="vfa_fw", curie=MIXS.curie('0000408'),
                   model_uri=NMDC.vfa_fw, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.vis_media = Slot(uri=MIXS['0000840'], name="vis_media", curie=MIXS.curie('0000840'),
                   model_uri=NMDC.vis_media, domain=None, range=Optional[Union[dict, TextValue]])

slots.viscosity = Slot(uri=MIXS['0000126'], name="viscosity", curie=MIXS.curie('0000126'),
                   model_uri=NMDC.viscosity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.volatile_org_comp = Slot(uri=MIXS['0000115'], name="volatile_org_comp", curie=MIXS.curie('0000115'),
                   model_uri=NMDC.volatile_org_comp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.wall_area = Slot(uri=MIXS['0000198'], name="wall_area", curie=MIXS.curie('0000198'),
                   model_uri=NMDC.wall_area, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.wall_const_type = Slot(uri=MIXS['0000841'], name="wall_const_type", curie=MIXS.curie('0000841'),
                   model_uri=NMDC.wall_const_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.wall_finish_mat = Slot(uri=MIXS['0000842'], name="wall_finish_mat", curie=MIXS.curie('0000842'),
                   model_uri=NMDC.wall_finish_mat, domain=None, range=Optional[Union[dict, TextValue]])

slots.wall_height = Slot(uri=MIXS['0000221'], name="wall_height", curie=MIXS.curie('0000221'),
                   model_uri=NMDC.wall_height, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.wall_loc = Slot(uri=MIXS['0000843'], name="wall_loc", curie=MIXS.curie('0000843'),
                   model_uri=NMDC.wall_loc, domain=None, range=Optional[Union[dict, TextValue]])

slots.wall_surf_treatment = Slot(uri=MIXS['0000845'], name="wall_surf_treatment", curie=MIXS.curie('0000845'),
                   model_uri=NMDC.wall_surf_treatment, domain=None, range=Optional[Union[dict, TextValue]])

slots.wall_texture = Slot(uri=MIXS['0000846'], name="wall_texture", curie=MIXS.curie('0000846'),
                   model_uri=NMDC.wall_texture, domain=None, range=Optional[Union[dict, TextValue]])

slots.wall_thermal_mass = Slot(uri=MIXS['0000222'], name="wall_thermal_mass", curie=MIXS.curie('0000222'),
                   model_uri=NMDC.wall_thermal_mass, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.wall_water_mold = Slot(uri=MIXS['0000844'], name="wall_water_mold", curie=MIXS.curie('0000844'),
                   model_uri=NMDC.wall_water_mold, domain=None, range=Optional[Union[dict, TextValue]])

slots.wastewater_type = Slot(uri=MIXS['0000353'], name="wastewater_type", curie=MIXS.curie('0000353'),
                   model_uri=NMDC.wastewater_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.water_cont_soil_meth = Slot(uri=MIXS['0000323'], name="water_cont_soil_meth", curie=MIXS.curie('0000323'),
                   model_uri=NMDC.water_cont_soil_meth, domain=None, range=Optional[str])

slots.water_content = Slot(uri=MIXS['0000185'], name="water_content", curie=MIXS.curie('0000185'),
                   model_uri=NMDC.water_content, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.water_current = Slot(uri=MIXS['0000203'], name="water_current", curie=MIXS.curie('0000203'),
                   model_uri=NMDC.water_current, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.water_cut = Slot(uri=MIXS['0000454'], name="water_cut", curie=MIXS.curie('0000454'),
                   model_uri=NMDC.water_cut, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.water_feat_size = Slot(uri=MIXS['0000223'], name="water_feat_size", curie=MIXS.curie('0000223'),
                   model_uri=NMDC.water_feat_size, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.water_feat_type = Slot(uri=MIXS['0000847'], name="water_feat_type", curie=MIXS.curie('0000847'),
                   model_uri=NMDC.water_feat_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.water_prod_rate = Slot(uri=MIXS['0000453'], name="water_prod_rate", curie=MIXS.curie('0000453'),
                   model_uri=NMDC.water_prod_rate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.water_temp_regm = Slot(uri=MIXS['0000590'], name="water_temp_regm", curie=MIXS.curie('0000590'),
                   model_uri=NMDC.water_temp_regm, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.watering_regm = Slot(uri=MIXS['0000591'], name="watering_regm", curie=MIXS.curie('0000591'),
                   model_uri=NMDC.watering_regm, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.weekday = Slot(uri=MIXS['0000848'], name="weekday", curie=MIXS.curie('0000848'),
                   model_uri=NMDC.weekday, domain=None, range=Optional[Union[dict, TextValue]])

slots.win = Slot(uri=MIXS['0000297'], name="win", curie=MIXS.curie('0000297'),
                   model_uri=NMDC.win, domain=None, range=Optional[Union[dict, TextValue]])

slots.wind_direction = Slot(uri=MIXS['0000757'], name="wind_direction", curie=MIXS.curie('0000757'),
                   model_uri=NMDC.wind_direction, domain=None, range=Optional[Union[dict, TextValue]])

slots.wind_speed = Slot(uri=MIXS['0000118'], name="wind_speed", curie=MIXS.curie('0000118'),
                   model_uri=NMDC.wind_speed, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.window_cond = Slot(uri=MIXS['0000849'], name="window_cond", curie=MIXS.curie('0000849'),
                   model_uri=NMDC.window_cond, domain=None, range=Optional[Union[dict, TextValue]])

slots.window_cover = Slot(uri=MIXS['0000850'], name="window_cover", curie=MIXS.curie('0000850'),
                   model_uri=NMDC.window_cover, domain=None, range=Optional[Union[dict, TextValue]])

slots.window_horiz_pos = Slot(uri=MIXS['0000851'], name="window_horiz_pos", curie=MIXS.curie('0000851'),
                   model_uri=NMDC.window_horiz_pos, domain=None, range=Optional[Union[dict, TextValue]])

slots.window_loc = Slot(uri=MIXS['0000852'], name="window_loc", curie=MIXS.curie('0000852'),
                   model_uri=NMDC.window_loc, domain=None, range=Optional[Union[dict, TextValue]])

slots.window_mat = Slot(uri=MIXS['0000853'], name="window_mat", curie=MIXS.curie('0000853'),
                   model_uri=NMDC.window_mat, domain=None, range=Optional[Union[dict, TextValue]])

slots.window_open_freq = Slot(uri=MIXS['0000246'], name="window_open_freq", curie=MIXS.curie('0000246'),
                   model_uri=NMDC.window_open_freq, domain=None, range=Optional[Union[dict, TextValue]])

slots.window_size = Slot(uri=MIXS['0000224'], name="window_size", curie=MIXS.curie('0000224'),
                   model_uri=NMDC.window_size, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.window_status = Slot(uri=MIXS['0000855'], name="window_status", curie=MIXS.curie('0000855'),
                   model_uri=NMDC.window_status, domain=None, range=Optional[Union[dict, TextValue]])

slots.window_type = Slot(uri=MIXS['0000856'], name="window_type", curie=MIXS.curie('0000856'),
                   model_uri=NMDC.window_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.window_vert_pos = Slot(uri=MIXS['0000857'], name="window_vert_pos", curie=MIXS.curie('0000857'),
                   model_uri=NMDC.window_vert_pos, domain=None, range=Optional[Union[dict, TextValue]])

slots.window_water_mold = Slot(uri=MIXS['0000854'], name="window_water_mold", curie=MIXS.curie('0000854'),
                   model_uri=NMDC.window_water_mold, domain=None, range=Optional[Union[dict, TextValue]])

slots.xylene = Slot(uri=MIXS['0000156'], name="xylene", curie=MIXS.curie('0000156'),
                   model_uri=NMDC.xylene, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.env_package = Slot(uri="str(uriorcurie)", name="env_package", curie=None,
                   model_uri=NMDC.env_package, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.env_package],
                   pattern=re.compile(r'[air|built environment|host\-associated|human\-associated|human\-skin|human\-oral|human\-gut|human\-vaginal|hydrocarbon resources\-cores|hydrocarbon resources\-fluids\/swabs|microbial mat\/biofilm|misc environment|plant\-associated|sediment|soil|wastewater\/sludge|water]'))

slots.language = Slot(uri=NMDC.language, name="language", curie=NMDC.curie('language'),
                   model_uri=NMDC.language, domain=None, range=Optional[str])

slots.attribute = Slot(uri=NMDC.attribute, name="attribute", curie=NMDC.curie('attribute'),
                   model_uri=NMDC.attribute, domain=None, range=Optional[str])

slots.has_raw_value = Slot(uri=NMDC.has_raw_value, name="has raw value", curie=NMDC.curie('has_raw_value'),
                   model_uri=NMDC.has_raw_value, domain=AttributeValue, range=Optional[str])

slots.has_unit = Slot(uri=NMDC.has_unit, name="has unit", curie=NMDC.curie('has_unit'),
                   model_uri=NMDC.has_unit, domain=None, range=Optional[str], mappings = [QUD.unit, SCHEMA.unitCode])

slots.has_numeric_value = Slot(uri=NMDC.has_numeric_value, name="has numeric value", curie=NMDC.curie('has_numeric_value'),
                   model_uri=NMDC.has_numeric_value, domain=None, range=Optional[float], mappings = [QUD.quantityValue, SCHEMA.value])

slots.has_minimum_numeric_value = Slot(uri=NMDC.has_minimum_numeric_value, name="has minimum numeric value", curie=NMDC.curie('has_minimum_numeric_value'),
                   model_uri=NMDC.has_minimum_numeric_value, domain=None, range=Optional[float])

slots.has_maximum_numeric_value = Slot(uri=NMDC.has_maximum_numeric_value, name="has maximum numeric value", curie=NMDC.curie('has_maximum_numeric_value'),
                   model_uri=NMDC.has_maximum_numeric_value, domain=None, range=Optional[float])

slots.has_boolean_value = Slot(uri=NMDC.has_boolean_value, name="has boolean value", curie=NMDC.curie('has_boolean_value'),
                   model_uri=NMDC.has_boolean_value, domain=None, range=Optional[Union[bool, Bool]])

slots.latitude = Slot(uri=WGS.lat, name="latitude", curie=WGS.curie('lat'),
                   model_uri=NMDC.latitude, domain=GeolocationValue, range=Optional[float], mappings = [SCHEMA.latitude])

slots.longitude = Slot(uri=WGS.long, name="longitude", curie=WGS.curie('long'),
                   model_uri=NMDC.longitude, domain=GeolocationValue, range=Optional[float], mappings = [SCHEMA.longitude])

slots.term = Slot(uri=RDF.type, name="term", curie=RDF.curie('type'),
                   model_uri=NMDC.term, domain=ControlledTermValue, range=Optional[Union[dict, OntologyClass]])

slots.orcid = Slot(uri=NMDC.orcid, name="orcid", curie=NMDC.curie('orcid'),
                   model_uri=NMDC.orcid, domain=PersonValue, range=Optional[str])

slots.email = Slot(uri=SCHEMA.email, name="email", curie=SCHEMA.curie('email'),
                   model_uri=NMDC.email, domain=None, range=Optional[str])

slots.alternate_emails = Slot(uri=NMDC.alternate_emails, name="alternate emails", curie=NMDC.curie('alternate_emails'),
                   model_uri=NMDC.alternate_emails, domain=None, range=Optional[str])

slots.profile_image_url = Slot(uri=NMDC.profile_image_url, name="profile image url", curie=NMDC.curie('profile_image_url'),
                   model_uri=NMDC.profile_image_url, domain=PersonValue, range=Optional[str])

slots.has_input = Slot(uri=NMDC.has_input, name="has input", curie=NMDC.curie('has_input'),
                   model_uri=NMDC.has_input, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_output = Slot(uri=NMDC.has_output, name="has output", curie=NMDC.curie('has_output'),
                   model_uri=NMDC.has_output, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.part_of = Slot(uri=DCTERMS.isPartOf, name="part of", curie=DCTERMS.curie('isPartOf'),
                   model_uri=NMDC.part_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.execution_resource = Slot(uri=NMDC.execution_resource, name="execution resource", curie=NMDC.curie('execution_resource'),
                   model_uri=NMDC.execution_resource, domain=None, range=Optional[str])

slots.url = Slot(uri=NMDC.url, name="url", curie=NMDC.curie('url'),
                   model_uri=NMDC.url, domain=None, range=Optional[str])

slots.display_order = Slot(uri=NMDC.display_order, name="display order", curie=NMDC.curie('display_order'),
                   model_uri=NMDC.display_order, domain=None, range=Optional[str])

slots.git_url = Slot(uri=NMDC.git_url, name="git url", curie=NMDC.curie('git_url'),
                   model_uri=NMDC.git_url, domain=None, range=Optional[str])

slots.file_size_bytes = Slot(uri=NMDC.file_size_bytes, name="file size bytes", curie=NMDC.curie('file_size_bytes'),
                   model_uri=NMDC.file_size_bytes, domain=None, range=Optional[int])

slots.md5_checksum = Slot(uri=NMDC.md5_checksum, name="md5 checksum", curie=NMDC.curie('md5_checksum'),
                   model_uri=NMDC.md5_checksum, domain=None, range=Optional[str])

slots.abstract = Slot(uri=NMDC.abstract, name="abstract", curie=NMDC.curie('abstract'),
                   model_uri=NMDC.abstract, domain=None, range=Optional[str])

slots.keywords = Slot(uri=NMDC.keywords, name="keywords", curie=NMDC.curie('keywords'),
                   model_uri=NMDC.keywords, domain=None, range=Optional[Union[str, List[str]]], mappings = [DCTERMS.subject])

slots.objective = Slot(uri=NMDC.objective, name="objective", curie=NMDC.curie('objective'),
                   model_uri=NMDC.objective, domain=None, range=Optional[str], mappings = [SIO["000337"]])

slots.websites = Slot(uri=NMDC.websites, name="websites", curie=NMDC.curie('websites'),
                   model_uri=NMDC.websites, domain=None, range=Optional[Union[str, List[str]]])

slots.publications = Slot(uri=NMDC.publications, name="publications", curie=NMDC.curie('publications'),
                   model_uri=NMDC.publications, domain=None, range=Optional[Union[str, List[str]]])

slots.started_at_time = Slot(uri=NMDC.started_at_time, name="started at time", curie=NMDC.curie('started_at_time'),
                   model_uri=NMDC.started_at_time, domain=None, range=Optional[Union[str, XSDDateTime]], mappings = [PROV.startedAtTime],
                   pattern=re.compile(r'^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$'))

slots.ended_at_time = Slot(uri=NMDC.ended_at_time, name="ended at time", curie=NMDC.curie('ended_at_time'),
                   model_uri=NMDC.ended_at_time, domain=None, range=Optional[Union[str, XSDDateTime]], mappings = [PROV.endedAtTime],
                   pattern=re.compile(r'^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$'))

slots.was_informed_by = Slot(uri=NMDC.was_informed_by, name="was informed by", curie=NMDC.curie('was_informed_by'),
                   model_uri=NMDC.was_informed_by, domain=None, range=Optional[Union[str, ActivityId]], mappings = [PROV.wasInformedBy])

slots.was_associated_with = Slot(uri=NMDC.was_associated_with, name="was associated with", curie=NMDC.curie('was_associated_with'),
                   model_uri=NMDC.was_associated_with, domain=None, range=Optional[Union[dict, Agent]], mappings = [PROV.wasAssociatedWith])

slots.acted_on_behalf_of = Slot(uri=NMDC.acted_on_behalf_of, name="acted on behalf of", curie=NMDC.curie('acted_on_behalf_of'),
                   model_uri=NMDC.acted_on_behalf_of, domain=None, range=Optional[Union[dict, Agent]], mappings = [PROV.actedOnBehalfOf])

slots.was_generated_by = Slot(uri=NMDC.was_generated_by, name="was generated by", curie=NMDC.curie('was_generated_by'),
                   model_uri=NMDC.was_generated_by, domain=None, range=Optional[Union[str, ActivityId]], mappings = [PROV.wasGeneratedBy])

slots.used = Slot(uri=NMDC.used, name="used", curie=NMDC.curie('used'),
                   model_uri=NMDC.used, domain=Activity, range=Optional[str], mappings = [PROV.used])

slots.metagenome_assembly_parameter = Slot(uri="str(uriorcurie)", name="metagenome assembly parameter", curie=None,
                   model_uri=NMDC.metagenome_assembly_parameter, domain=None, range=Optional[str])

slots.asm_score = Slot(uri="str(uriorcurie)", name="asm_score", curie=None,
                   model_uri=NMDC.asm_score, domain=None, range=Optional[float])

slots.scaffolds = Slot(uri="str(uriorcurie)", name="scaffolds", curie=None,
                   model_uri=NMDC.scaffolds, domain=None, range=Optional[float])

slots.scaf_logsum = Slot(uri="str(uriorcurie)", name="scaf_logsum", curie=None,
                   model_uri=NMDC.scaf_logsum, domain=None, range=Optional[float])

slots.scaf_powsum = Slot(uri="str(uriorcurie)", name="scaf_powsum", curie=None,
                   model_uri=NMDC.scaf_powsum, domain=None, range=Optional[float])

slots.scaf_max = Slot(uri="str(uriorcurie)", name="scaf_max", curie=None,
                   model_uri=NMDC.scaf_max, domain=None, range=Optional[float])

slots.scaf_bp = Slot(uri="str(uriorcurie)", name="scaf_bp", curie=None,
                   model_uri=NMDC.scaf_bp, domain=None, range=Optional[float])

slots.scaf_N50 = Slot(uri="str(uriorcurie)", name="scaf_N50", curie=None,
                   model_uri=NMDC.scaf_N50, domain=None, range=Optional[float])

slots.scaf_N90 = Slot(uri="str(uriorcurie)", name="scaf_N90", curie=None,
                   model_uri=NMDC.scaf_N90, domain=None, range=Optional[float])

slots.scaf_L50 = Slot(uri="str(uriorcurie)", name="scaf_L50", curie=None,
                   model_uri=NMDC.scaf_L50, domain=None, range=Optional[float])

slots.scaf_L90 = Slot(uri="str(uriorcurie)", name="scaf_L90", curie=None,
                   model_uri=NMDC.scaf_L90, domain=None, range=Optional[float])

slots.scaf_n_gt50K = Slot(uri="str(uriorcurie)", name="scaf_n_gt50K", curie=None,
                   model_uri=NMDC.scaf_n_gt50K, domain=None, range=Optional[float])

slots.scaf_l_gt50K = Slot(uri="str(uriorcurie)", name="scaf_l_gt50K", curie=None,
                   model_uri=NMDC.scaf_l_gt50K, domain=None, range=Optional[float])

slots.scaf_pct_gt50K = Slot(uri="str(uriorcurie)", name="scaf_pct_gt50K", curie=None,
                   model_uri=NMDC.scaf_pct_gt50K, domain=None, range=Optional[float])

slots.contigs = Slot(uri="str(uriorcurie)", name="contigs", curie=None,
                   model_uri=NMDC.contigs, domain=None, range=Optional[float])

slots.contig_bp = Slot(uri="str(uriorcurie)", name="contig_bp", curie=None,
                   model_uri=NMDC.contig_bp, domain=None, range=Optional[float])

slots.ctg_N50 = Slot(uri="str(uriorcurie)", name="ctg_N50", curie=None,
                   model_uri=NMDC.ctg_N50, domain=None, range=Optional[float])

slots.ctg_L50 = Slot(uri="str(uriorcurie)", name="ctg_L50", curie=None,
                   model_uri=NMDC.ctg_L50, domain=None, range=Optional[float])

slots.ctg_N90 = Slot(uri="str(uriorcurie)", name="ctg_N90", curie=None,
                   model_uri=NMDC.ctg_N90, domain=None, range=Optional[float])

slots.ctg_L90 = Slot(uri="str(uriorcurie)", name="ctg_L90", curie=None,
                   model_uri=NMDC.ctg_L90, domain=None, range=Optional[float])

slots.ctg_logsum = Slot(uri="str(uriorcurie)", name="ctg_logsum", curie=None,
                   model_uri=NMDC.ctg_logsum, domain=None, range=Optional[float])

slots.ctg_powsum = Slot(uri="str(uriorcurie)", name="ctg_powsum", curie=None,
                   model_uri=NMDC.ctg_powsum, domain=None, range=Optional[float])

slots.ctg_max = Slot(uri="str(uriorcurie)", name="ctg_max", curie=None,
                   model_uri=NMDC.ctg_max, domain=None, range=Optional[float])

slots.gap_pct = Slot(uri="str(uriorcurie)", name="gap_pct", curie=None,
                   model_uri=NMDC.gap_pct, domain=None, range=Optional[float])

slots.gc_std = Slot(uri="str(uriorcurie)", name="gc_std", curie=None,
                   model_uri=NMDC.gc_std, domain=None, range=Optional[float])

slots.gc_avg = Slot(uri="str(uriorcurie)", name="gc_avg", curie=None,
                   model_uri=NMDC.gc_avg, domain=None, range=Optional[float])

slots.num_input_reads = Slot(uri="str(uriorcurie)", name="num_input_reads", curie=None,
                   model_uri=NMDC.num_input_reads, domain=None, range=Optional[float])

slots.num_aligned_reads = Slot(uri="str(uriorcurie)", name="num_aligned_reads", curie=None,
                   model_uri=NMDC.num_aligned_reads, domain=None, range=Optional[float])

slots.read_QC_analysis_statistic = Slot(uri="str(uriorcurie)", name="read QC analysis statistic", curie=None,
                   model_uri=NMDC.read_QC_analysis_statistic, domain=None, range=Optional[str])

slots.mags_list = Slot(uri="str(uriorcurie)", name="mags list", curie=None,
                   model_uri=NMDC.mags_list, domain=None, range=Optional[Union[Union[dict, MAGBin], List[Union[dict, MAGBin]]]])

slots.too_short_contig_num = Slot(uri="str(uriorcurie)", name="too short contig num", curie=None,
                   model_uri=NMDC.too_short_contig_num, domain=None, range=Optional[int])

slots.binned_contig_num = Slot(uri="str(uriorcurie)", name="binned contig num", curie=None,
                   model_uri=NMDC.binned_contig_num, domain=None, range=Optional[int])

slots.input_contig_num = Slot(uri="str(uriorcurie)", name="input contig num", curie=None,
                   model_uri=NMDC.input_contig_num, domain=None, range=Optional[int])

slots.unbinned_contig_num = Slot(uri="str(uriorcurie)", name="unbinned contig num", curie=None,
                   model_uri=NMDC.unbinned_contig_num, domain=None, range=Optional[int])

slots.lowDepth_contig_num = Slot(uri="str(uriorcurie)", name="lowDepth contig num", curie=None,
                   model_uri=NMDC.lowDepth_contig_num, domain=None, range=Optional[int])

slots.input_read_count = Slot(uri="str(uriorcurie)", name="input read count", curie=None,
                   model_uri=NMDC.input_read_count, domain=None, range=Optional[float])

slots.input_base_count = Slot(uri="str(uriorcurie)", name="input base count", curie=None,
                   model_uri=NMDC.input_base_count, domain=None, range=Optional[float])

slots.output_read_count = Slot(uri="str(uriorcurie)", name="output read count", curie=None,
                   model_uri=NMDC.output_read_count, domain=None, range=Optional[float])

slots.output_base_count = Slot(uri="str(uriorcurie)", name="output base count", curie=None,
                   model_uri=NMDC.output_base_count, domain=None, range=Optional[float])

slots.subject = Slot(uri="str(uriorcurie)", name="subject", curie=None,
                   model_uri=NMDC.subject, domain=None, range=Optional[Union[str, GeneProductId]])

slots.has_function = Slot(uri="str(uriorcurie)", name="has function", curie=None,
                   model_uri=NMDC.has_function, domain=None, range=Optional[str])

slots.has_participants = Slot(uri="str(uriorcurie)", name="has participants", curie=None,
                   model_uri=NMDC.has_participants, domain=None, range=Optional[str])

slots.gff_coordinate = Slot(uri="str(uriorcurie)", name="gff coordinate", curie=None,
                   model_uri=NMDC.gff_coordinate, domain=None, range=Optional[int])

slots.external_database_identifiers = Slot(uri=NMDC.external_database_identifiers, name="external database identifiers", curie=NMDC.curie('external_database_identifiers'),
                   model_uri=NMDC.external_database_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]])

slots.GOLD_identifiers = Slot(uri=NMDC.GOLD_identifiers, name="GOLD identifiers", curie=NMDC.curie('GOLD_identifiers'),
                   model_uri=NMDC.GOLD_identifiers, domain=None, range=Optional[str])

slots.MGnify_identifiers = Slot(uri=NMDC.MGnify_identifiers, name="MGnify identifiers", curie=NMDC.curie('MGnify_identifiers'),
                   model_uri=NMDC.MGnify_identifiers, domain=None, range=Optional[str])

slots.INSDC_identifiers = Slot(uri=NMDC.INSDC_identifiers, name="INSDC identifiers", curie=NMDC.curie('INSDC_identifiers'),
                   model_uri=NMDC.INSDC_identifiers, domain=None, range=Optional[str])

slots.study_identifiers = Slot(uri=NMDC.study_identifiers, name="study identifiers", curie=NMDC.curie('study_identifiers'),
                   model_uri=NMDC.study_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]])

slots.INSDC_SRA_ENA_study_identifiers = Slot(uri=NMDC.INSDC_SRA_ENA_study_identifiers, name="INSDC SRA ENA study identifiers", curie=NMDC.curie('INSDC_SRA_ENA_study_identifiers'),
                   model_uri=NMDC.INSDC_SRA_ENA_study_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^insdc.sra:(E|D|S)RP[0-9]{6,}$'))

slots.INSDC_bioproject_identifiers = Slot(uri=NMDC.INSDC_bioproject_identifiers, name="INSDC bioproject identifiers", curie=NMDC.curie('INSDC_bioproject_identifiers'),
                   model_uri=NMDC.INSDC_bioproject_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^bioproject:PRJ[DEN][A-Z][0-9]+$'))

slots.GOLD_study_identifiers = Slot(uri=NMDC.GOLD_study_identifiers, name="GOLD study identifiers", curie=NMDC.curie('GOLD_study_identifiers'),
                   model_uri=NMDC.GOLD_study_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^GOLD:Gs[0-9]+$'))

slots.MGnify_project_identifiers = Slot(uri=NMDC.MGnify_project_identifiers, name="MGnify project identifiers", curie=NMDC.curie('MGnify_project_identifiers'),
                   model_uri=NMDC.MGnify_project_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^mgnify.proj:[A-Z]+[0-9]+$'))

slots.sample_identifiers = Slot(uri=NMDC.sample_identifiers, name="sample identifiers", curie=NMDC.curie('sample_identifiers'),
                   model_uri=NMDC.sample_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]])

slots.GOLD_sample_identifiers = Slot(uri=NMDC.GOLD_sample_identifiers, name="GOLD sample identifiers", curie=NMDC.curie('GOLD_sample_identifiers'),
                   model_uri=NMDC.GOLD_sample_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^GOLD:Gb[0-9]+$'))

slots.INSDC_biosample_identifiers = Slot(uri=NMDC.INSDC_biosample_identifiers, name="INSDC biosample identifiers", curie=NMDC.curie('INSDC_biosample_identifiers'),
                   model_uri=NMDC.INSDC_biosample_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^biosample:SAM[NED]([A-Z])?[0-9]+$'))

slots.INSDC_secondary_sample_identifiers = Slot(uri=NMDC.INSDC_secondary_sample_identifiers, name="INSDC secondary sample identifiers", curie=NMDC.curie('INSDC_secondary_sample_identifiers'),
                   model_uri=NMDC.INSDC_secondary_sample_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^biosample:(E|D|S)RS[0-9]{6,}$'))

slots.omics_processing_identifiers = Slot(uri=NMDC.omics_processing_identifiers, name="omics processing identifiers", curie=NMDC.curie('omics_processing_identifiers'),
                   model_uri=NMDC.omics_processing_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]])

slots.GOLD_sequencing_project_identifiers = Slot(uri=NMDC.GOLD_sequencing_project_identifiers, name="GOLD sequencing project identifiers", curie=NMDC.curie('GOLD_sequencing_project_identifiers'),
                   model_uri=NMDC.GOLD_sequencing_project_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^GOLD:Gp[0-9]+$'))

slots.INSDC_experiment_identifiers = Slot(uri=NMDC.INSDC_experiment_identifiers, name="INSDC experiment identifiers", curie=NMDC.curie('INSDC_experiment_identifiers'),
                   model_uri=NMDC.INSDC_experiment_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^insdc.sra:(E|D|S)RX[0-9]{6,}$'))

slots.analysis_identifiers = Slot(uri=NMDC.analysis_identifiers, name="analysis identifiers", curie=NMDC.curie('analysis_identifiers'),
                   model_uri=NMDC.analysis_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]])

slots.GOLD_analysis_project_identifiers = Slot(uri=NMDC.GOLD_analysis_project_identifiers, name="GOLD analysis project identifiers", curie=NMDC.curie('GOLD_analysis_project_identifiers'),
                   model_uri=NMDC.GOLD_analysis_project_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^GOLD:Ga[0-9]+$'))

slots.INSDC_analysis_identifiers = Slot(uri=NMDC.INSDC_analysis_identifiers, name="INSDC analysis identifiers", curie=NMDC.curie('INSDC_analysis_identifiers'),
                   model_uri=NMDC.INSDC_analysis_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^insdc.sra:(E|D|S)RR[0-9]{6,}$'))

slots.MGnify_analysis_identifiers = Slot(uri=NMDC.MGnify_analysis_identifiers, name="MGnify analysis identifiers", curie=NMDC.curie('MGnify_analysis_identifiers'),
                   model_uri=NMDC.MGnify_analysis_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]])

slots.assembly_identifiers = Slot(uri=NMDC.assembly_identifiers, name="assembly identifiers", curie=NMDC.curie('assembly_identifiers'),
                   model_uri=NMDC.assembly_identifiers, domain=None, range=Optional[str])

slots.INSDC_assembly_identifiers = Slot(uri=NMDC.INSDC_assembly_identifiers, name="INSDC assembly identifiers", curie=NMDC.curie('INSDC_assembly_identifiers'),
                   model_uri=NMDC.INSDC_assembly_identifiers, domain=None, range=Optional[str],
                   pattern=re.compile(r'^insdc.sra:[A-Z]+[0-9]+(\.[0-9]+)?$'))

slots.id = Slot(uri=NMDC.id, name="id", curie=NMDC.curie('id'),
                   model_uri=NMDC.id, domain=None, range=URIRef)

slots.name = Slot(uri=NMDC.name, name="name", curie=NMDC.curie('name'),
                   model_uri=NMDC.name, domain=None, range=Optional[str])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=NMDC.description, domain=None, range=Optional[str])

slots.type = Slot(uri=NMDC.type, name="type", curie=NMDC.curie('type'),
                   model_uri=NMDC.type, domain=None, range=Optional[str])

slots.title = Slot(uri=NMDC.title, name="title", curie=NMDC.curie('title'),
                   model_uri=NMDC.title, domain=None, range=Optional[str])

slots.alternative_titles = Slot(uri=NMDC.alternative_titles, name="alternative titles", curie=NMDC.curie('alternative_titles'),
                   model_uri=NMDC.alternative_titles, domain=None, range=Optional[Union[str, List[str]]])

slots.alternative_names = Slot(uri=NMDC.alternative_names, name="alternative names", curie=NMDC.curie('alternative_names'),
                   model_uri=NMDC.alternative_names, domain=None, range=Optional[Union[str, List[str]]])

slots.alternative_descriptions = Slot(uri=NMDC.alternative_descriptions, name="alternative descriptions", curie=NMDC.curie('alternative_descriptions'),
                   model_uri=NMDC.alternative_descriptions, domain=None, range=Optional[Union[str, List[str]]])

slots.alternative_identifiers = Slot(uri=NMDC.alternative_identifiers, name="alternative identifiers", curie=NMDC.curie('alternative_identifiers'),
                   model_uri=NMDC.alternative_identifiers, domain=None, range=Optional[Union[str, List[str]]])

slots.mAGBin__bin_name = Slot(uri=NMDC.bin_name, name="mAGBin__bin_name", curie=NMDC.curie('bin_name'),
                   model_uri=NMDC.mAGBin__bin_name, domain=None, range=Optional[str])

slots.mAGBin__number_of_contig = Slot(uri=NMDC.number_of_contig, name="mAGBin__number_of_contig", curie=NMDC.curie('number_of_contig'),
                   model_uri=NMDC.mAGBin__number_of_contig, domain=None, range=Optional[int])

slots.mAGBin__completeness = Slot(uri=NMDC.completeness, name="mAGBin__completeness", curie=NMDC.curie('completeness'),
                   model_uri=NMDC.mAGBin__completeness, domain=None, range=Optional[float])

slots.mAGBin__contamination = Slot(uri=NMDC.contamination, name="mAGBin__contamination", curie=NMDC.curie('contamination'),
                   model_uri=NMDC.mAGBin__contamination, domain=None, range=Optional[float])

slots.mAGBin__gene_count = Slot(uri=NMDC.gene_count, name="mAGBin__gene_count", curie=NMDC.curie('gene_count'),
                   model_uri=NMDC.mAGBin__gene_count, domain=None, range=Optional[int])

slots.mAGBin__bin_quality = Slot(uri=NMDC.bin_quality, name="mAGBin__bin_quality", curie=NMDC.curie('bin_quality'),
                   model_uri=NMDC.mAGBin__bin_quality, domain=None, range=Optional[str])

slots.mAGBin__num_16s = Slot(uri=NMDC.num_16s, name="mAGBin__num_16s", curie=NMDC.curie('num_16s'),
                   model_uri=NMDC.mAGBin__num_16s, domain=None, range=Optional[int])

slots.mAGBin__num_5s = Slot(uri=NMDC.num_5s, name="mAGBin__num_5s", curie=NMDC.curie('num_5s'),
                   model_uri=NMDC.mAGBin__num_5s, domain=None, range=Optional[int])

slots.mAGBin__num_23s = Slot(uri=NMDC.num_23s, name="mAGBin__num_23s", curie=NMDC.curie('num_23s'),
                   model_uri=NMDC.mAGBin__num_23s, domain=None, range=Optional[int])

slots.mAGBin__num_tRNA = Slot(uri=NMDC.num_tRNA, name="mAGBin__num_tRNA", curie=NMDC.curie('num_tRNA'),
                   model_uri=NMDC.mAGBin__num_tRNA, domain=None, range=Optional[int])

slots.mAGBin__gtdbtk_domain = Slot(uri=NMDC.gtdbtk_domain, name="mAGBin__gtdbtk_domain", curie=NMDC.curie('gtdbtk_domain'),
                   model_uri=NMDC.mAGBin__gtdbtk_domain, domain=None, range=Optional[str])

slots.mAGBin__gtdbtk_phylum = Slot(uri=NMDC.gtdbtk_phylum, name="mAGBin__gtdbtk_phylum", curie=NMDC.curie('gtdbtk_phylum'),
                   model_uri=NMDC.mAGBin__gtdbtk_phylum, domain=None, range=Optional[str])

slots.mAGBin__gtdbtk_class = Slot(uri=NMDC.gtdbtk_class, name="mAGBin__gtdbtk_class", curie=NMDC.curie('gtdbtk_class'),
                   model_uri=NMDC.mAGBin__gtdbtk_class, domain=None, range=Optional[str])

slots.mAGBin__gtdbtk_order = Slot(uri=NMDC.gtdbtk_order, name="mAGBin__gtdbtk_order", curie=NMDC.curie('gtdbtk_order'),
                   model_uri=NMDC.mAGBin__gtdbtk_order, domain=None, range=Optional[str])

slots.mAGBin__gtdbtk_family = Slot(uri=NMDC.gtdbtk_family, name="mAGBin__gtdbtk_family", curie=NMDC.curie('gtdbtk_family'),
                   model_uri=NMDC.mAGBin__gtdbtk_family, domain=None, range=Optional[str])

slots.mAGBin__gtdbtk_genus = Slot(uri=NMDC.gtdbtk_genus, name="mAGBin__gtdbtk_genus", curie=NMDC.curie('gtdbtk_genus'),
                   model_uri=NMDC.mAGBin__gtdbtk_genus, domain=None, range=Optional[str])

slots.mAGBin__gtdbtk_species = Slot(uri=NMDC.gtdbtk_species, name="mAGBin__gtdbtk_species", curie=NMDC.curie('gtdbtk_species'),
                   model_uri=NMDC.mAGBin__gtdbtk_species, domain=None, range=Optional[str])

slots.nmdc_schema_version = Slot(uri=NMDC.nmdc_schema_version, name="nmdc schema version", curie=NMDC.curie('nmdc_schema_version'),
                   model_uri=NMDC.nmdc_schema_version, domain=None, range=Optional[str])

slots.date_created = Slot(uri=NMDC.date_created, name="date created", curie=NMDC.curie('date_created'),
                   model_uri=NMDC.date_created, domain=None, range=Optional[str])

slots.etl_software_version = Slot(uri=NMDC.etl_software_version, name="etl software version", curie=NMDC.curie('etl_software_version'),
                   model_uri=NMDC.etl_software_version, domain=None, range=Optional[str])

slots.metabolite_quantified = Slot(uri=NMDC.metabolite_quantified, name="metabolite quantified", curie=NMDC.curie('metabolite_quantified'),
                   model_uri=NMDC.metabolite_quantified, domain=None, range=Optional[Union[str, ChemicalEntityId]])

slots.highest_similarity_score = Slot(uri=NMDC.highest_similarity_score, name="highest similarity score", curie=NMDC.curie('highest_similarity_score'),
                   model_uri=NMDC.highest_similarity_score, domain=None, range=Optional[float])

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

slots.database_nmdc_schema_version = Slot(uri=NMDC.nmdc_schema_version, name="database_nmdc schema version", curie=NMDC.curie('nmdc_schema_version'),
                   model_uri=NMDC.database_nmdc_schema_version, domain=Database, range=Optional[str])

slots.database_date_created = Slot(uri=NMDC.date_created, name="database_date created", curie=NMDC.curie('date_created'),
                   model_uri=NMDC.database_date_created, domain=Database, range=Optional[str])

slots.database_etl_software_version = Slot(uri=NMDC.etl_software_version, name="database_etl software version", curie=NMDC.curie('etl_software_version'),
                   model_uri=NMDC.database_etl_software_version, domain=Database, range=Optional[str])

slots.data_object_name = Slot(uri=NMDC.name, name="data object_name", curie=NMDC.curie('name'),
                   model_uri=NMDC.data_object_name, domain=DataObject, range=str)

slots.data_object_description = Slot(uri=DCTERMS.description, name="data object_description", curie=DCTERMS.curie('description'),
                   model_uri=NMDC.data_object_description, domain=DataObject, range=str)

slots.biosample_lat_lon = Slot(uri=MIXS['0000009'], name="biosample_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=NMDC.biosample_lat_lon, domain=Biosample, range=Optional[Union[dict, "GeolocationValue"]])

slots.biosample_env_broad_scale = Slot(uri=MIXS['0000012'], name="biosample_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=NMDC.biosample_env_broad_scale, domain=Biosample, range=Union[dict, "ControlledTermValue"])

slots.biosample_env_local_scale = Slot(uri=MIXS['0000013'], name="biosample_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=NMDC.biosample_env_local_scale, domain=Biosample, range=Union[dict, "ControlledTermValue"])

slots.biosample_env_medium = Slot(uri=MIXS['0000014'], name="biosample_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=NMDC.biosample_env_medium, domain=Biosample, range=Union[dict, "ControlledTermValue"])

slots.biosample_part_of = Slot(uri=DCTERMS.isPartOf, name="biosample_part of", curie=DCTERMS.curie('isPartOf'),
                   model_uri=NMDC.biosample_part_of, domain=Biosample, range=Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]])

slots.study_doi = Slot(uri=NMDC.doi, name="study_doi", curie=NMDC.curie('doi'),
                   model_uri=NMDC.study_doi, domain=Study, range=Optional[Union[dict, "AttributeValue"]])

slots.biosample_processing_has_input = Slot(uri=NMDC.has_input, name="biosample processing_has input", curie=NMDC.curie('has_input'),
                   model_uri=NMDC.biosample_processing_has_input, domain=BiosampleProcessing, range=Optional[Union[Union[str, BiosampleId], List[Union[str, BiosampleId]]]])

slots.omics_processing_has_input = Slot(uri=NMDC.has_input, name="omics processing_has input", curie=NMDC.curie('has_input'),
                   model_uri=NMDC.omics_processing_has_input, domain=OmicsProcessing, range=Union[Union[str, BiosampleId], List[Union[str, BiosampleId]]])

slots.attribute_value_type = Slot(uri=NMDC.type, name="attribute value_type", curie=NMDC.curie('type'),
                   model_uri=NMDC.attribute_value_type, domain=AttributeValue, range=Optional[str])

slots.quantity_value_has_raw_value = Slot(uri=NMDC.has_raw_value, name="quantity value_has raw value", curie=NMDC.curie('has_raw_value'),
                   model_uri=NMDC.quantity_value_has_raw_value, domain=QuantityValue, range=Optional[str])

slots.quantity_value_has_unit = Slot(uri=NMDC.has_unit, name="quantity value_has unit", curie=NMDC.curie('has_unit'),
                   model_uri=NMDC.quantity_value_has_unit, domain=QuantityValue, range=Optional[str], mappings = [QUD.unit, SCHEMA.unitCode])

slots.quantity_value_has_numeric_value = Slot(uri=NMDC.has_numeric_value, name="quantity value_has numeric value", curie=NMDC.curie('has_numeric_value'),
                   model_uri=NMDC.quantity_value_has_numeric_value, domain=QuantityValue, range=Optional[float], mappings = [QUD.quantityValue, SCHEMA.value])

slots.person_value_orcid = Slot(uri=NMDC.orcid, name="person value_orcid", curie=NMDC.curie('orcid'),
                   model_uri=NMDC.person_value_orcid, domain=PersonValue, range=Optional[str])

slots.person_value_email = Slot(uri=SCHEMA.email, name="person value_email", curie=SCHEMA.curie('email'),
                   model_uri=NMDC.person_value_email, domain=PersonValue, range=Optional[str])

slots.person_value_has_raw_value = Slot(uri=NMDC.has_raw_value, name="person value_has raw value", curie=NMDC.curie('has_raw_value'),
                   model_uri=NMDC.person_value_has_raw_value, domain=PersonValue, range=Optional[str])

slots.person_value_name = Slot(uri=NMDC.name, name="person value_name", curie=NMDC.curie('name'),
                   model_uri=NMDC.person_value_name, domain=PersonValue, range=Optional[str])

slots.person_id = Slot(uri=NMDC.id, name="person_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.person_id, domain=Person, range=Union[str, PersonId])

slots.metabolite_quantification_metabolite_quantified = Slot(uri=NMDC.metabolite_quantified, name="metabolite quantification_metabolite quantified", curie=NMDC.curie('metabolite_quantified'),
                   model_uri=NMDC.metabolite_quantification_metabolite_quantified, domain=MetaboliteQuantification, range=Optional[Union[str, ChemicalEntityId]])

slots.metabolite_quantification_highest_similarity_score = Slot(uri=NMDC.highest_similarity_score, name="metabolite quantification_highest similarity score", curie=NMDC.curie('highest_similarity_score'),
                   model_uri=NMDC.metabolite_quantification_highest_similarity_score, domain=MetaboliteQuantification, range=Optional[float])

slots.peptide_quantification_peptide_sequence = Slot(uri=NMDC.peptide_sequence, name="peptide quantification_peptide sequence", curie=NMDC.curie('peptide_sequence'),
                   model_uri=NMDC.peptide_quantification_peptide_sequence, domain=PeptideQuantification, range=Optional[str])

slots.peptide_quantification_best_protein = Slot(uri=NMDC.best_protein, name="peptide quantification_best protein", curie=NMDC.curie('best_protein'),
                   model_uri=NMDC.peptide_quantification_best_protein, domain=PeptideQuantification, range=Optional[Union[str, GeneProductId]])

slots.peptide_quantification_all_proteins = Slot(uri=NMDC.all_proteins, name="peptide quantification_all proteins", curie=NMDC.curie('all_proteins'),
                   model_uri=NMDC.peptide_quantification_all_proteins, domain=PeptideQuantification, range=Optional[Union[Union[str, GeneProductId], List[Union[str, GeneProductId]]]])

slots.peptide_quantification_min_q_value = Slot(uri=NMDC.min_q_value, name="peptide quantification_min_q_value", curie=NMDC.curie('min_q_value'),
                   model_uri=NMDC.peptide_quantification_min_q_value, domain=PeptideQuantification, range=Optional[float])

slots.peptide_quantification_peptide_spectral_count = Slot(uri=NMDC.peptide_spectral_count, name="peptide quantification_peptide_spectral_count", curie=NMDC.curie('peptide_spectral_count'),
                   model_uri=NMDC.peptide_quantification_peptide_spectral_count, domain=PeptideQuantification, range=Optional[int])

slots.peptide_quantification_peptide_sum_masic_abundance = Slot(uri=NMDC.peptide_sum_masic_abundance, name="peptide quantification_peptide_sum_masic_abundance", curie=NMDC.curie('peptide_sum_masic_abundance'),
                   model_uri=NMDC.peptide_quantification_peptide_sum_masic_abundance, domain=PeptideQuantification, range=Optional[int])

slots.protein_quantification_best_protein = Slot(uri=NMDC.best_protein, name="protein quantification_best protein", curie=NMDC.curie('best_protein'),
                   model_uri=NMDC.protein_quantification_best_protein, domain=ProteinQuantification, range=Optional[Union[str, GeneProductId]])

slots.protein_quantification_all_proteins = Slot(uri=NMDC.all_proteins, name="protein quantification_all proteins", curie=NMDC.curie('all_proteins'),
                   model_uri=NMDC.protein_quantification_all_proteins, domain=ProteinQuantification, range=Optional[Union[Union[str, GeneProductId], List[Union[str, GeneProductId]]]])

slots.protein_quantification_peptide_sequence_count = Slot(uri=NMDC.peptide_sequence_count, name="protein quantification_peptide_sequence_count", curie=NMDC.curie('peptide_sequence_count'),
                   model_uri=NMDC.protein_quantification_peptide_sequence_count, domain=ProteinQuantification, range=Optional[int])

slots.protein_quantification_protein_spectral_count = Slot(uri=NMDC.protein_spectral_count, name="protein quantification_protein_spectral_count", curie=NMDC.curie('protein_spectral_count'),
                   model_uri=NMDC.protein_quantification_protein_spectral_count, domain=ProteinQuantification, range=Optional[int])

slots.protein_quantification_protein_sum_masic_abundance = Slot(uri=NMDC.protein_sum_masic_abundance, name="protein quantification_protein_sum_masic_abundance", curie=NMDC.curie('protein_sum_masic_abundance'),
                   model_uri=NMDC.protein_quantification_protein_sum_masic_abundance, domain=ProteinQuantification, range=Optional[int])

slots.chemical_entity_inchi = Slot(uri=NMDC.inchi, name="chemical entity_inchi", curie=NMDC.curie('inchi'),
                   model_uri=NMDC.chemical_entity_inchi, domain=ChemicalEntity, range=Optional[str])

slots.chemical_entity_inchi_key = Slot(uri=NMDC.inchi_key, name="chemical entity_inchi key", curie=NMDC.curie('inchi_key'),
                   model_uri=NMDC.chemical_entity_inchi_key, domain=ChemicalEntity, range=Optional[str])

slots.chemical_entity_smiles = Slot(uri=NMDC.smiles, name="chemical entity_smiles", curie=NMDC.curie('smiles'),
                   model_uri=NMDC.chemical_entity_smiles, domain=ChemicalEntity, range=Optional[Union[str, List[str]]])

slots.chemical_entity_chemical_formula = Slot(uri=NMDC.chemical_formula, name="chemical entity_chemical formula", curie=NMDC.curie('chemical_formula'),
                   model_uri=NMDC.chemical_entity_chemical_formula, domain=ChemicalEntity, range=Optional[str])

slots.geolocation_value_has_raw_value = Slot(uri=NMDC.has_raw_value, name="geolocation value_has raw value", curie=NMDC.curie('has_raw_value'),
                   model_uri=NMDC.geolocation_value_has_raw_value, domain=GeolocationValue, range=Optional[str])

slots.workflow_execution_activity_was_associated_with = Slot(uri=NMDC.was_associated_with, name="workflow execution activity_was associated with", curie=NMDC.curie('was_associated_with'),
                   model_uri=NMDC.workflow_execution_activity_was_associated_with, domain=WorkflowExecutionActivity, range=Optional[Union[str, WorkflowExecutionActivityId]], mappings = [PROV.wasAssociatedWith])

slots.workflow_execution_activity_started_at_time = Slot(uri=NMDC.started_at_time, name="workflow execution activity_started at time", curie=NMDC.curie('started_at_time'),
                   model_uri=NMDC.workflow_execution_activity_started_at_time, domain=WorkflowExecutionActivity, range=Union[str, XSDDateTime], mappings = [PROV.startedAtTime],
                   pattern=re.compile(r'^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$'))

slots.workflow_execution_activity_ended_at_time = Slot(uri=NMDC.ended_at_time, name="workflow execution activity_ended at time", curie=NMDC.curie('ended_at_time'),
                   model_uri=NMDC.workflow_execution_activity_ended_at_time, domain=WorkflowExecutionActivity, range=Union[str, XSDDateTime], mappings = [PROV.endedAtTime],
                   pattern=re.compile(r'^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$'))

slots.workflow_execution_activity_git_url = Slot(uri=NMDC.git_url, name="workflow execution activity_git url", curie=NMDC.curie('git_url'),
                   model_uri=NMDC.workflow_execution_activity_git_url, domain=WorkflowExecutionActivity, range=str)

slots.workflow_execution_activity_has_input = Slot(uri=NMDC.has_input, name="workflow execution activity_has input", curie=NMDC.curie('has_input'),
                   model_uri=NMDC.workflow_execution_activity_has_input, domain=WorkflowExecutionActivity, range=Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]])

slots.workflow_execution_activity_has_output = Slot(uri=NMDC.has_output, name="workflow execution activity_has output", curie=NMDC.curie('has_output'),
                   model_uri=NMDC.workflow_execution_activity_has_output, domain=WorkflowExecutionActivity, range=Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]])

slots.workflow_execution_activity_was_informed_by = Slot(uri=NMDC.was_informed_by, name="workflow execution activity_was informed by", curie=NMDC.curie('was_informed_by'),
                   model_uri=NMDC.workflow_execution_activity_was_informed_by, domain=WorkflowExecutionActivity, range=Union[str, ActivityId], mappings = [PROV.wasInformedBy])

slots.workflow_execution_activity_execution_resource = Slot(uri=NMDC.execution_resource, name="workflow execution activity_execution resource", curie=NMDC.curie('execution_resource'),
                   model_uri=NMDC.workflow_execution_activity_execution_resource, domain=WorkflowExecutionActivity, range=str)

slots.workflow_execution_activity_type = Slot(uri=NMDC.type, name="workflow execution activity_type", curie=NMDC.curie('type'),
                   model_uri=NMDC.workflow_execution_activity_type, domain=WorkflowExecutionActivity, range=str)

slots.read_QC_analysis_activity_input_read_bases = Slot(uri=NMDC.input_read_bases, name="read QC analysis activity_input_read_bases", curie=NMDC.curie('input_read_bases'),
                   model_uri=NMDC.read_QC_analysis_activity_input_read_bases, domain=ReadQCAnalysisActivity, range=Optional[float])

slots.read_QC_analysis_activity_output_read_bases = Slot(uri=NMDC.output_read_bases, name="read QC analysis activity_output_read_bases", curie=NMDC.curie('output_read_bases'),
                   model_uri=NMDC.read_QC_analysis_activity_output_read_bases, domain=ReadQCAnalysisActivity, range=Optional[float])

slots.read_QC_analysis_activity_has_input = Slot(uri=NMDC.has_input, name="read QC analysis activity_has input", curie=NMDC.curie('has_input'),
                   model_uri=NMDC.read_QC_analysis_activity_has_input, domain=ReadQCAnalysisActivity, range=Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]])

slots.read_QC_analysis_activity_has_output = Slot(uri=NMDC.has_output, name="read QC analysis activity_has output", curie=NMDC.curie('has_output'),
                   model_uri=NMDC.read_QC_analysis_activity_has_output, domain=ReadQCAnalysisActivity, range=Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]])

slots.metabolomics_analysis_activity_used = Slot(uri=NMDC.used, name="metabolomics analysis activity_used", curie=NMDC.curie('used'),
                   model_uri=NMDC.metabolomics_analysis_activity_used, domain=MetabolomicsAnalysisActivity, range=Optional[Union[str, InstrumentId]], mappings = [PROV.used])

slots.metabolomics_analysis_activity_has_metabolite_quantifications = Slot(uri=NMDC.has_metabolite_quantifications, name="metabolomics analysis activity_has metabolite quantifications", curie=NMDC.curie('has_metabolite_quantifications'),
                   model_uri=NMDC.metabolomics_analysis_activity_has_metabolite_quantifications, domain=MetabolomicsAnalysisActivity, range=Optional[Union[Union[dict, MetaboliteQuantification], List[Union[dict, MetaboliteQuantification]]]])

slots.metabolomics_analysis_activity_has_calibration = Slot(uri=NMDC.has_calibration, name="metabolomics analysis activity_has calibration", curie=NMDC.curie('has_calibration'),
                   model_uri=NMDC.metabolomics_analysis_activity_has_calibration, domain=MetabolomicsAnalysisActivity, range=Optional[str])

slots.metaproteomics_analysis_activity_used = Slot(uri=NMDC.used, name="metaproteomics analysis activity_used", curie=NMDC.curie('used'),
                   model_uri=NMDC.metaproteomics_analysis_activity_used, domain=MetaproteomicsAnalysisActivity, range=Optional[Union[str, InstrumentId]], mappings = [PROV.used])

slots.metaproteomics_analysis_activity_has_peptide_quantifications = Slot(uri=NMDC.has_peptide_quantifications, name="metaproteomics analysis activity_has peptide quantifications", curie=NMDC.curie('has_peptide_quantifications'),
                   model_uri=NMDC.metaproteomics_analysis_activity_has_peptide_quantifications, domain=MetaproteomicsAnalysisActivity, range=Optional[Union[Union[dict, PeptideQuantification], List[Union[dict, PeptideQuantification]]]])

slots.nom_analysis_activity_used = Slot(uri=NMDC.used, name="nom analysis activity_used", curie=NMDC.curie('used'),
                   model_uri=NMDC.nom_analysis_activity_used, domain=NomAnalysisActivity, range=Optional[Union[str, InstrumentId]], mappings = [PROV.used])

slots.nom_analysis_activity_has_calibration = Slot(uri=NMDC.has_calibration, name="nom analysis activity_has calibration", curie=NMDC.curie('has_calibration'),
                   model_uri=NMDC.nom_analysis_activity_has_calibration, domain=NomAnalysisActivity, range=Optional[str])

slots.genome_feature_seqid = Slot(uri=NMDC.seqid, name="genome feature_seqid", curie=NMDC.curie('seqid'),
                   model_uri=NMDC.genome_feature_seqid, domain=GenomeFeature, range=str)

slots.genome_feature_type = Slot(uri=RDF.type, name="genome feature_type", curie=RDF.curie('type'),
                   model_uri=NMDC.genome_feature_type, domain=GenomeFeature, range=Optional[Union[str, OntologyClassId]])

slots.genome_feature_start = Slot(uri=NMDC.start, name="genome feature_start", curie=NMDC.curie('start'),
                   model_uri=NMDC.genome_feature_start, domain=GenomeFeature, range=int)

slots.genome_feature_end = Slot(uri=NMDC.end, name="genome feature_end", curie=NMDC.curie('end'),
                   model_uri=NMDC.genome_feature_end, domain=GenomeFeature, range=int)

slots.genome_feature_strand = Slot(uri=NMDC.strand, name="genome feature_strand", curie=NMDC.curie('strand'),
                   model_uri=NMDC.genome_feature_strand, domain=GenomeFeature, range=Optional[str])

slots.genome_feature_phase = Slot(uri=NMDC.phase, name="genome feature_phase", curie=NMDC.curie('phase'),
                   model_uri=NMDC.genome_feature_phase, domain=GenomeFeature, range=Optional[int])

slots.genome_feature_encodes = Slot(uri=NMDC.encodes, name="genome feature_encodes", curie=NMDC.curie('encodes'),
                   model_uri=NMDC.genome_feature_encodes, domain=GenomeFeature, range=Optional[Union[str, GeneProductId]])

slots.genome_feature_feature_type = Slot(uri=NMDC.feature_type, name="genome feature_feature type", curie=NMDC.curie('feature_type'),
                   model_uri=NMDC.genome_feature_feature_type, domain=GenomeFeature, range=Optional[str])

slots.pathway_has_part = Slot(uri=NMDC.has_part, name="pathway_has_part", curie=NMDC.curie('has_part'),
                   model_uri=NMDC.pathway_has_part, domain=Pathway, range=Optional[Union[Union[str, ReactionId], List[Union[str, ReactionId]]]])

slots.reaction_left_participants = Slot(uri=NMDC.left_participants, name="reaction_left participants", curie=NMDC.curie('left_participants'),
                   model_uri=NMDC.reaction_left_participants, domain=Reaction, range=Optional[Union[Union[dict, "ReactionParticipant"], List[Union[dict, "ReactionParticipant"]]]])

slots.reaction_right_participants = Slot(uri=NMDC.right_participants, name="reaction_right participants", curie=NMDC.curie('right_participants'),
                   model_uri=NMDC.reaction_right_participants, domain=Reaction, range=Optional[Union[Union[dict, "ReactionParticipant"], List[Union[dict, "ReactionParticipant"]]]])

slots.reaction_direction = Slot(uri=NMDC.direction, name="reaction_direction", curie=NMDC.curie('direction'),
                   model_uri=NMDC.reaction_direction, domain=Reaction, range=Optional[str])

slots.reaction_smarts_string = Slot(uri=NMDC.smarts_string, name="reaction_smarts string", curie=NMDC.curie('smarts_string'),
                   model_uri=NMDC.reaction_smarts_string, domain=Reaction, range=Optional[str])

slots.reaction_is_diastereoselective = Slot(uri=NMDC.is_diastereoselective, name="reaction_is diastereoselective", curie=NMDC.curie('is_diastereoselective'),
                   model_uri=NMDC.reaction_is_diastereoselective, domain=Reaction, range=Optional[Union[bool, Bool]])

slots.reaction_is_stereo = Slot(uri=NMDC.is_stereo, name="reaction_is stereo", curie=NMDC.curie('is_stereo'),
                   model_uri=NMDC.reaction_is_stereo, domain=Reaction, range=Optional[Union[bool, Bool]])

slots.reaction_is_balanced = Slot(uri=NMDC.is_balanced, name="reaction_is balanced", curie=NMDC.curie('is_balanced'),
                   model_uri=NMDC.reaction_is_balanced, domain=Reaction, range=Optional[Union[bool, Bool]])

slots.reaction_is_transport = Slot(uri=NMDC.is_transport, name="reaction_is transport", curie=NMDC.curie('is_transport'),
                   model_uri=NMDC.reaction_is_transport, domain=Reaction, range=Optional[Union[bool, Bool]])

slots.reaction_is_fully_characterized = Slot(uri=NMDC.is_fully_characterized, name="reaction_is fully characterized", curie=NMDC.curie('is_fully_characterized'),
                   model_uri=NMDC.reaction_is_fully_characterized, domain=Reaction, range=Optional[Union[bool, Bool]])

slots.reaction_participant_chemical = Slot(uri=NMDC.chemical, name="reaction participant_chemical", curie=NMDC.curie('chemical'),
                   model_uri=NMDC.reaction_participant_chemical, domain=ReactionParticipant, range=Optional[Union[str, ChemicalEntityId]])

slots.reaction_participant_stoichiometry = Slot(uri=NMDC.stoichiometry, name="reaction participant_stoichiometry", curie=NMDC.curie('stoichiometry'),
                   model_uri=NMDC.reaction_participant_stoichiometry, domain=ReactionParticipant, range=Optional[int])

slots.functional_annotation_has_function = Slot(uri="str(uriorcurie)", name="functional annotation_has function", curie=None,
                   model_uri=NMDC.functional_annotation_has_function, domain=FunctionalAnnotation, range=Optional[str],
                   pattern=re.compile(r'^(KEGG.PATHWAY:\w{2,4}\d{5}|KEGG.REACTION:R\d+|RHEA:\d{5}|MetaCyc:[A-Za-z0-9+_.%-:]+|EC:\d{1,2}(\.\d{0,3}){0,3}|GO:\d{7}|MetaNetX:(MNXR\d+|EMPTY)|SEED:\w+|KEGG\.ORTHOLOGY:K\d+|EGGNOG:\w+|PFAM:PF\d{5}|TIGRFAM:TIGR\d+|SUPFAM:\w+|CATH:[1-6]\.[0-9]+\.[0-9]+\.[0-9]+|PANTHER.FAMILY:PTHR\d{5}(\:SF\d{1,3})?)$'))

slots.functional_annotation_type = Slot(uri=NMDC.type, name="functional annotation_type", curie=NMDC.curie('type'),
                   model_uri=NMDC.functional_annotation_type, domain=FunctionalAnnotation, range=Optional[Union[str, OntologyClassId]])

slots.functional_annotation_was_generated_by = Slot(uri=NMDC.was_generated_by, name="functional annotation_was generated by", curie=NMDC.curie('was_generated_by'),
                   model_uri=NMDC.functional_annotation_was_generated_by, domain=FunctionalAnnotation, range=Optional[Union[str, MetagenomeAnnotationActivityId]], mappings = [PROV.wasGeneratedBy])
