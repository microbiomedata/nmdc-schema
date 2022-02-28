# Auto generated from nmdc.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-02-28T12:58:16
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
    tot_nitro_content_meth: Optional[Union[dict, "TextValue"]] = None
    tot_phosp: Optional[Union[dict, "QuantityValue"]] = None
    water_content: Optional[Union[dict, "QuantityValue"]] = None
    water_content_soil_meth: Optional[Union[dict, "TextValue"]] = None
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

        if self.tot_nitro_content_meth is not None and not isinstance(self.tot_nitro_content_meth, TextValue):
            self.tot_nitro_content_meth = TextValue(**as_dict(self.tot_nitro_content_meth))

        if self.tot_phosp is not None and not isinstance(self.tot_phosp, QuantityValue):
            self.tot_phosp = QuantityValue(**as_dict(self.tot_phosp))

        if self.water_content is not None and not isinstance(self.water_content, QuantityValue):
            self.water_content = QuantityValue(**as_dict(self.water_content))

        if self.water_content_soil_meth is not None and not isinstance(self.water_content_soil_meth, TextValue):
            self.water_content_soil_meth = TextValue(**as_dict(self.water_content_soil_meth))

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

slots.submitted_to_insdc = Slot(uri="str(uriorcurie)", name="submitted_to_insdc", curie=None,
                   model_uri=NMDC.submitted_to_insdc, domain=None, range=Optional[Union[dict, BooleanValue]], mappings = [MIXS.submitted_to_insdc],
                   pattern=re.compile(r'[true|false]'))

slots.investigation_type = Slot(uri="str(uriorcurie)", name="investigation_type", curie=None,
                   model_uri=NMDC.investigation_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.investigation_type],
                   pattern=re.compile(r'[eukaryote|bacteria_archaea|plasmid|virus|organelle|metagenome|metatranscriptome|mimarks\-survey|mimarks\-specimen|misag|mimag|miuvig]'))

slots.project_name = Slot(uri="str(uriorcurie)", name="project_name", curie=None,
                   model_uri=NMDC.project_name, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.project_name])

slots.experimental_factor = Slot(uri="str(uriorcurie)", name="experimental_factor", curie=None,
                   model_uri=NMDC.experimental_factor, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.experimental_factor])

slots.lat_lon = Slot(uri="str(uriorcurie)", name="lat_lon", curie=None,
                   model_uri=NMDC.lat_lon, domain=None, range=Optional[Union[dict, GeolocationValue]], mappings = [MIXS.lat_lon],
                   pattern=re.compile(r'\d+[.\d+] \d+[.\d+]'))

slots.depth = Slot(uri="str(uriorcurie)", name="depth", curie=None,
                   model_uri=NMDC.depth, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.depth])

slots.alt = Slot(uri="str(uriorcurie)", name="alt", curie=None,
                   model_uri=NMDC.alt, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.alt],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.elev = Slot(uri="str(uriorcurie)", name="elev", curie=None,
                   model_uri=NMDC.elev, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.elev],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.geo_loc_name = Slot(uri="str(uriorcurie)", name="geo_loc_name", curie=None,
                   model_uri=NMDC.geo_loc_name, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.geo_loc_name])

slots.collection_date = Slot(uri="str(uriorcurie)", name="collection_date", curie=None,
                   model_uri=NMDC.collection_date, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.collection_date])

slots.env_broad_scale = Slot(uri="str(uriorcurie)", name="env_broad_scale", curie=None,
                   model_uri=NMDC.env_broad_scale, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.env_broad_scale],
                   pattern=re.compile(r'.* \S+:\S+'))

slots.env_local_scale = Slot(uri="str(uriorcurie)", name="env_local_scale", curie=None,
                   model_uri=NMDC.env_local_scale, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.env_local_scale],
                   pattern=re.compile(r'.* \S+:\S+'))

slots.env_medium = Slot(uri="str(uriorcurie)", name="env_medium", curie=None,
                   model_uri=NMDC.env_medium, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.env_medium],
                   pattern=re.compile(r'.* \S+:\S+'))

slots.env_package = Slot(uri="str(uriorcurie)", name="env_package", curie=None,
                   model_uri=NMDC.env_package, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.env_package],
                   pattern=re.compile(r'[air|built environment|host\-associated|human\-associated|human\-skin|human\-oral|human\-gut|human\-vaginal|hydrocarbon resources\-cores|hydrocarbon resources\-fluids\/swabs|microbial mat\/biofilm|misc environment|plant\-associated|sediment|soil|wastewater\/sludge|water]'))

slots.subspecf_gen_lin = Slot(uri="str(uriorcurie)", name="subspecf_gen_lin", curie=None,
                   model_uri=NMDC.subspecf_gen_lin, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.subspecf_gen_lin])

slots.ploidy = Slot(uri="str(uriorcurie)", name="ploidy", curie=None,
                   model_uri=NMDC.ploidy, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.ploidy],
                   pattern=re.compile(r'.* \S+:\S+'))

slots.num_replicons = Slot(uri="str(uriorcurie)", name="num_replicons", curie=None,
                   model_uri=NMDC.num_replicons, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.num_replicons])

slots.extrachrom_elements = Slot(uri="str(uriorcurie)", name="extrachrom_elements", curie=None,
                   model_uri=NMDC.extrachrom_elements, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.extrachrom_elements])

slots.estimated_size = Slot(uri="str(uriorcurie)", name="estimated_size", curie=None,
                   model_uri=NMDC.estimated_size, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.estimated_size])

slots.ref_biomaterial = Slot(uri="str(uriorcurie)", name="ref_biomaterial", curie=None,
                   model_uri=NMDC.ref_biomaterial, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ref_biomaterial])

slots.source_mat_id = Slot(uri="str(uriorcurie)", name="source_mat_id", curie=None,
                   model_uri=NMDC.source_mat_id, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.source_mat_id])

slots.pathogenicity = Slot(uri="str(uriorcurie)", name="pathogenicity", curie=None,
                   model_uri=NMDC.pathogenicity, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.pathogenicity])

slots.biotic_relationship = Slot(uri="str(uriorcurie)", name="biotic_relationship", curie=None,
                   model_uri=NMDC.biotic_relationship, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.biotic_relationship],
                   pattern=re.compile(r'[free living|parasitism|commensalism|symbiotic|mutualism]'))

slots.specific_host = Slot(uri="str(uriorcurie)", name="specific_host", curie=None,
                   model_uri=NMDC.specific_host, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.specific_host])

slots.host_spec_range = Slot(uri="str(uriorcurie)", name="host_spec_range", curie=None,
                   model_uri=NMDC.host_spec_range, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_spec_range])

slots.health_disease_stat = Slot(uri="str(uriorcurie)", name="health_disease_stat", curie=None,
                   model_uri=NMDC.health_disease_stat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.health_disease_stat],
                   pattern=re.compile(r'[healthy|diseased|dead|disease\-free|undetermined|recovering|resolving|pre\-existing condition|pathological|life threatening|congenital]'))

slots.trophic_level = Slot(uri="str(uriorcurie)", name="trophic_level", curie=None,
                   model_uri=NMDC.trophic_level, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.trophic_level],
                   pattern=re.compile(r'[autotroph|carboxydotroph|chemoautotroph|chemoheterotroph|chemolithoautotroph|chemolithotroph|chemoorganoheterotroph|chemoorganotroph|chemosynthetic|chemotroph|copiotroph|diazotroph|facultative|autotroph|heterotroph|lithoautotroph|lithoheterotroph|lithotroph|methanotroph|methylotroph|mixotroph|obligate|chemoautolithotroph|oligotroph|organoheterotroph|organotroph|photoautotroph|photoheterotroph|photolithoautotroph|photolithotroph|photosynthetic|phototroph]'))

slots.propagation = Slot(uri="str(uriorcurie)", name="propagation", curie=None,
                   model_uri=NMDC.propagation, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.propagation])

slots.encoded_traits = Slot(uri="str(uriorcurie)", name="encoded_traits", curie=None,
                   model_uri=NMDC.encoded_traits, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.encoded_traits])

slots.rel_to_oxygen = Slot(uri="str(uriorcurie)", name="rel_to_oxygen", curie=None,
                   model_uri=NMDC.rel_to_oxygen, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.rel_to_oxygen],
                   pattern=re.compile(r'[aerobe|anaerobe|facultative|microaerophilic|microanaerobe|obligate aerobe|obligate anaerobe]'))

slots.isol_growth_condt = Slot(uri="str(uriorcurie)", name="isol_growth_condt", curie=None,
                   model_uri=NMDC.isol_growth_condt, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.isol_growth_condt])

slots.samp_collect_device = Slot(uri="str(uriorcurie)", name="samp_collect_device", curie=None,
                   model_uri=NMDC.samp_collect_device, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_collect_device])

slots.samp_mat_process = Slot(uri="str(uriorcurie)", name="samp_mat_process", curie=None,
                   model_uri=NMDC.samp_mat_process, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.samp_mat_process])

slots.size_frac = Slot(uri="str(uriorcurie)", name="size_frac", curie=None,
                   model_uri=NMDC.size_frac, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.size_frac],
                   pattern=re.compile(r'\d+[.\d+]\-\d+[.\d+] \S+'))

slots.samp_size = Slot(uri="str(uriorcurie)", name="samp_size", curie=None,
                   model_uri=NMDC.samp_size, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.samp_size],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.source_uvig = Slot(uri="str(uriorcurie)", name="source_uvig", curie=None,
                   model_uri=NMDC.source_uvig, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.source_uvig],
                   pattern=re.compile(r'[metagenome (not viral targeted)|viral fraction metagenome (virome)|sequence\-targeted metagenome|metatranscriptome (not viral targeted)|viral fraction RNA metagenome (RNA virome)|sequence\-targeted RNA metagenome|microbial single amplified genome (SAG)|viral single amplified genome (vSAG)|isolate microbial genome|other]'))

slots.virus_enrich_appr = Slot(uri="str(uriorcurie)", name="virus_enrich_appr", curie=None,
                   model_uri=NMDC.virus_enrich_appr, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.virus_enrich_appr],
                   pattern=re.compile(r'[filtration|ultrafiltration|centrifugation|ultracentrifugation|PEG Precipitation|FeCl Precipitation|CsCl density gradient|DNAse|RNAse|targeted sequence capture|other|none]'))

slots.nucl_acid_ext = Slot(uri="str(uriorcurie)", name="nucl_acid_ext", curie=None,
                   model_uri=NMDC.nucl_acid_ext, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.nucl_acid_ext])

slots.nucl_acid_amp = Slot(uri="str(uriorcurie)", name="nucl_acid_amp", curie=None,
                   model_uri=NMDC.nucl_acid_amp, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.nucl_acid_amp])

slots.lib_size = Slot(uri="str(uriorcurie)", name="lib_size", curie=None,
                   model_uri=NMDC.lib_size, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.lib_size])

slots.lib_reads_seqd = Slot(uri="str(uriorcurie)", name="lib_reads_seqd", curie=None,
                   model_uri=NMDC.lib_reads_seqd, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.lib_reads_seqd])

slots.lib_layout = Slot(uri="str(uriorcurie)", name="lib_layout", curie=None,
                   model_uri=NMDC.lib_layout, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.lib_layout],
                   pattern=re.compile(r'[paired|single|vector|other]'))

slots.lib_vector = Slot(uri="str(uriorcurie)", name="lib_vector", curie=None,
                   model_uri=NMDC.lib_vector, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.lib_vector])

slots.lib_screen = Slot(uri="str(uriorcurie)", name="lib_screen", curie=None,
                   model_uri=NMDC.lib_screen, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.lib_screen])

slots.target_gene = Slot(uri="str(uriorcurie)", name="target_gene", curie=None,
                   model_uri=NMDC.target_gene, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.target_gene])

slots.target_subfragment = Slot(uri="str(uriorcurie)", name="target_subfragment", curie=None,
                   model_uri=NMDC.target_subfragment, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.target_subfragment])

slots.pcr_primers = Slot(uri="str(uriorcurie)", name="pcr_primers", curie=None,
                   model_uri=NMDC.pcr_primers, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.pcr_primers])

slots.mid = Slot(uri="str(uriorcurie)", name="mid", curie=None,
                   model_uri=NMDC.mid, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.mid])

slots.adapters = Slot(uri="str(uriorcurie)", name="adapters", curie=None,
                   model_uri=NMDC.adapters, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.adapters])

slots.pcr_cond = Slot(uri="str(uriorcurie)", name="pcr_cond", curie=None,
                   model_uri=NMDC.pcr_cond, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.pcr_cond],
                   pattern=re.compile(r'initial denaturation:degrees_minutes;annealing:degrees_minutes;elongation:degrees_minutes;final elongation:degrees_minutes;total cycles'))

slots.seq_meth = Slot(uri="str(uriorcurie)", name="seq_meth", curie=None,
                   model_uri=NMDC.seq_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.seq_meth],
                   pattern=re.compile(r'[MinION|GridION|PromethION|454 GS|454 GS 20|454 GS FLX|454 GS FLX+|454 GS FLX Titanium|454 GS Junior|Illumina Genome Analyzer|Illumina Genome Analyzer II|Illumina Genome Analyzer IIx|Illumina HiSeq 4000|Illumina HiSeq 3000|Illumina HiSeq 2500|Illumina HiSeq 2000|Illumina HiSeq 1500|Illumina HiSeq 1000|Illumina HiScanSQ|Illumina MiSeq|Illumina HiSeq X Five|Illumina HiSeq X Ten|Illumina NextSeq 500|Illumina NextSeq 550|AB SOLiD System|AB SOLiD System 2.0|AB SOLiD System 3.0|AB SOLiD 3 Plus System|AB SOLiD 4 System|AB SOLiD 4hq System|AB SOLiD PI System|AB 5500 Genetic Analyzer|AB 5500xl Genetic Analyzer|AB 5500xl\-W Genetic Analysis System|Ion Torrent PGM|Ion Torrent Proton|Ion Torrent S5|Ion Torrent S5 XL|PacBio RS|PacBio RS II|Sequel|AB 3730xL Genetic Analyzer|AB 3730 Genetic Analyzer|AB 3500xL Genetic Analyzer|AB 3500 Genetic Analyzer|AB 3130xL Genetic Analyzer|AB 3130 Genetic Analyzer|AB 310 Genetic Analyzer|BGISEQ\-500]'))

slots.seq_quality_check = Slot(uri="str(uriorcurie)", name="seq_quality_check", curie=None,
                   model_uri=NMDC.seq_quality_check, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.seq_quality_check],
                   pattern=re.compile(r'[none|manually edited]'))

slots.chimera_check = Slot(uri="str(uriorcurie)", name="chimera_check", curie=None,
                   model_uri=NMDC.chimera_check, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.chimera_check])

slots.tax_ident = Slot(uri="str(uriorcurie)", name="tax_ident", curie=None,
                   model_uri=NMDC.tax_ident, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.tax_ident],
                   pattern=re.compile(r'[16S rRNA gene|multi\-marker approach|other]'))

slots.assembly_qual = Slot(uri="str(uriorcurie)", name="assembly_qual", curie=None,
                   model_uri=NMDC.assembly_qual, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.assembly_qual],
                   pattern=re.compile(r'[Finished genome|High\-quality draft genome|Medium\-quality draft genome|Low\-quality draft genome|Genome fragment(s)]'))

slots.assembly_name = Slot(uri="str(uriorcurie)", name="assembly_name", curie=None,
                   model_uri=NMDC.assembly_name, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.assembly_name])

slots.assembly_software = Slot(uri="str(uriorcurie)", name="assembly_software", curie=None,
                   model_uri=NMDC.assembly_software, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.assembly_software])

slots.annot = Slot(uri="str(uriorcurie)", name="annot", curie=None,
                   model_uri=NMDC.annot, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.annot])

slots.number_contig = Slot(uri="str(uriorcurie)", name="number_contig", curie=None,
                   model_uri=NMDC.number_contig, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.number_contig])

slots.feat_pred = Slot(uri="str(uriorcurie)", name="feat_pred", curie=None,
                   model_uri=NMDC.feat_pred, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.feat_pred])

slots.ref_db = Slot(uri="str(uriorcurie)", name="ref_db", curie=None,
                   model_uri=NMDC.ref_db, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ref_db])

slots.sim_search_meth = Slot(uri="str(uriorcurie)", name="sim_search_meth", curie=None,
                   model_uri=NMDC.sim_search_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.sim_search_meth])

slots.tax_class = Slot(uri="str(uriorcurie)", name="tax_class", curie=None,
                   model_uri=NMDC.tax_class, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.tax_class])

slots._16s_recover = Slot(uri="str(uriorcurie)", name="_16s_recover", curie=None,
                   model_uri=NMDC._16s_recover, domain=None, range=Optional[Union[dict, BooleanValue]], mappings = [MIXS._16s_recover],
                   pattern=re.compile(r'[true|false]'))

slots._16s_recover_software = Slot(uri="str(uriorcurie)", name="_16s_recover_software", curie=None,
                   model_uri=NMDC._16s_recover_software, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS._16s_recover_software])

slots.trnas = Slot(uri="str(uriorcurie)", name="trnas", curie=None,
                   model_uri=NMDC.trnas, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.trnas])

slots.trna_ext_software = Slot(uri="str(uriorcurie)", name="trna_ext_software", curie=None,
                   model_uri=NMDC.trna_ext_software, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.trna_ext_software])

slots.compl_score = Slot(uri="str(uriorcurie)", name="compl_score", curie=None,
                   model_uri=NMDC.compl_score, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.compl_score])

slots.compl_software = Slot(uri="str(uriorcurie)", name="compl_software", curie=None,
                   model_uri=NMDC.compl_software, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.compl_software])

slots.compl_appr = Slot(uri="str(uriorcurie)", name="compl_appr", curie=None,
                   model_uri=NMDC.compl_appr, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.compl_appr],
                   pattern=re.compile(r'[marker gene|reference based|other]'))

slots.contam_score = Slot(uri="str(uriorcurie)", name="contam_score", curie=None,
                   model_uri=NMDC.contam_score, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.contam_score],
                   pattern=re.compile(r'\d+[.\d+] percentage'))

slots.contam_screen_input = Slot(uri="str(uriorcurie)", name="contam_screen_input", curie=None,
                   model_uri=NMDC.contam_screen_input, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.contam_screen_input],
                   pattern=re.compile(r'[reads| contigs]'))

slots.contam_screen_param = Slot(uri="str(uriorcurie)", name="contam_screen_param", curie=None,
                   model_uri=NMDC.contam_screen_param, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.contam_screen_param])

slots.decontam_software = Slot(uri="str(uriorcurie)", name="decontam_software", curie=None,
                   model_uri=NMDC.decontam_software, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.decontam_software],
                   pattern=re.compile(r'[checkm\/refinem|anvi\'o|prodege|bbtools:decontaminate.sh|acdc|combination]'))

slots.sort_tech = Slot(uri="str(uriorcurie)", name="sort_tech", curie=None,
                   model_uri=NMDC.sort_tech, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.sort_tech],
                   pattern=re.compile(r'[flow cytometric cell sorting|microfluidics|lazer\-tweezing|optical manipulation|micromanipulation|other]'))

slots.single_cell_lysis_appr = Slot(uri="str(uriorcurie)", name="single_cell_lysis_appr", curie=None,
                   model_uri=NMDC.single_cell_lysis_appr, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.single_cell_lysis_appr],
                   pattern=re.compile(r'[chemical|enzymatic|physical|combination]'))

slots.single_cell_lysis_prot = Slot(uri="str(uriorcurie)", name="single_cell_lysis_prot", curie=None,
                   model_uri=NMDC.single_cell_lysis_prot, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.single_cell_lysis_prot])

slots.wga_amp_appr = Slot(uri="str(uriorcurie)", name="wga_amp_appr", curie=None,
                   model_uri=NMDC.wga_amp_appr, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.wga_amp_appr],
                   pattern=re.compile(r'[pcr based|mda based]'))

slots.wga_amp_kit = Slot(uri="str(uriorcurie)", name="wga_amp_kit", curie=None,
                   model_uri=NMDC.wga_amp_kit, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.wga_amp_kit])

slots.bin_param = Slot(uri="str(uriorcurie)", name="bin_param", curie=None,
                   model_uri=NMDC.bin_param, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.bin_param],
                   pattern=re.compile(r'[homology search|kmer|coverage|codon usage|combination]'))

slots.bin_software = Slot(uri="str(uriorcurie)", name="bin_software", curie=None,
                   model_uri=NMDC.bin_software, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.bin_software],
                   pattern=re.compile(r'[metabat|maxbin|concoct|groupm|esom|metawatt|combination|other]'))

slots.reassembly_bin = Slot(uri="str(uriorcurie)", name="reassembly_bin", curie=None,
                   model_uri=NMDC.reassembly_bin, domain=None, range=Optional[Union[dict, BooleanValue]], mappings = [MIXS.reassembly_bin],
                   pattern=re.compile(r'[true|false]'))

slots.mag_cov_software = Slot(uri="str(uriorcurie)", name="mag_cov_software", curie=None,
                   model_uri=NMDC.mag_cov_software, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.mag_cov_software],
                   pattern=re.compile(r'[bwa|bbmap|bowtie|other]'))

slots.vir_ident_software = Slot(uri="str(uriorcurie)", name="vir_ident_software", curie=None,
                   model_uri=NMDC.vir_ident_software, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.vir_ident_software])

slots.pred_genome_type = Slot(uri="str(uriorcurie)", name="pred_genome_type", curie=None,
                   model_uri=NMDC.pred_genome_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.pred_genome_type],
                   pattern=re.compile(r'[DNA|dsDNA|ssDNA|RNA|dsRNA|ssRNA|ssRNA (+)|ssRNA (\-)|mixed|uncharacterized]'))

slots.pred_genome_struc = Slot(uri="str(uriorcurie)", name="pred_genome_struc", curie=None,
                   model_uri=NMDC.pred_genome_struc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.pred_genome_struc],
                   pattern=re.compile(r'[segmented|non\-segmented|undetermined]'))

slots.detec_type = Slot(uri="str(uriorcurie)", name="detec_type", curie=None,
                   model_uri=NMDC.detec_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.detec_type],
                   pattern=re.compile(r'[independent sequence (UViG)|provirus (UpViG)]'))

slots.votu_class_appr = Slot(uri="str(uriorcurie)", name="votu_class_appr", curie=None,
                   model_uri=NMDC.votu_class_appr, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.votu_class_appr])

slots.votu_seq_comp_appr = Slot(uri="str(uriorcurie)", name="votu_seq_comp_appr", curie=None,
                   model_uri=NMDC.votu_seq_comp_appr, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.votu_seq_comp_appr])

slots.votu_db = Slot(uri="str(uriorcurie)", name="votu_db", curie=None,
                   model_uri=NMDC.votu_db, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.votu_db])

slots.host_pred_appr = Slot(uri="str(uriorcurie)", name="host_pred_appr", curie=None,
                   model_uri=NMDC.host_pred_appr, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_pred_appr],
                   pattern=re.compile(r'[provirus|host sequence similarity|CRISPR spacer match|kmer similarity|co\-occurrence|combination|other]'))

slots.host_pred_est_acc = Slot(uri="str(uriorcurie)", name="host_pred_est_acc", curie=None,
                   model_uri=NMDC.host_pred_est_acc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_pred_est_acc])

slots.mixs_url = Slot(uri="str(uriorcurie)", name="mixs_url", curie=None,
                   model_uri=NMDC.mixs_url, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.mixs_url])

slots.sop = Slot(uri="str(uriorcurie)", name="sop", curie=None,
                   model_uri=NMDC.sop, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.sop])

slots.barometric_press = Slot(uri="str(uriorcurie)", name="barometric_press", curie=None,
                   model_uri=NMDC.barometric_press, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.barometric_press],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.carb_dioxide = Slot(uri="str(uriorcurie)", name="carb_dioxide", curie=None,
                   model_uri=NMDC.carb_dioxide, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.carb_dioxide],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.carb_monoxide = Slot(uri="str(uriorcurie)", name="carb_monoxide", curie=None,
                   model_uri=NMDC.carb_monoxide, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.carb_monoxide],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.chem_administration = Slot(uri="str(uriorcurie)", name="chem_administration", curie=None,
                   model_uri=NMDC.chem_administration, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.chem_administration])

slots.humidity = Slot(uri="str(uriorcurie)", name="humidity", curie=None,
                   model_uri=NMDC.humidity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.humidity],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.methane = Slot(uri="str(uriorcurie)", name="methane", curie=None,
                   model_uri=NMDC.methane, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.methane],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.misc_param = Slot(uri="str(uriorcurie)", name="misc_param", curie=None,
                   model_uri=NMDC.misc_param, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.misc_param])

slots.organism_count = Slot(uri="str(uriorcurie)", name="organism_count", curie=None,
                   model_uri=NMDC.organism_count, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.organism_count])

slots.oxygen = Slot(uri="str(uriorcurie)", name="oxygen", curie=None,
                   model_uri=NMDC.oxygen, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.oxygen],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.oxy_stat_samp = Slot(uri="str(uriorcurie)", name="oxy_stat_samp", curie=None,
                   model_uri=NMDC.oxy_stat_samp, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.oxy_stat_samp],
                   pattern=re.compile(r'[aerobic|anaerobic|other]'))

slots.perturbation = Slot(uri="str(uriorcurie)", name="perturbation", curie=None,
                   model_uri=NMDC.perturbation, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.perturbation])

slots.pollutants = Slot(uri="str(uriorcurie)", name="pollutants", curie=None,
                   model_uri=NMDC.pollutants, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.pollutants])

slots.resp_part_matter = Slot(uri="str(uriorcurie)", name="resp_part_matter", curie=None,
                   model_uri=NMDC.resp_part_matter, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.resp_part_matter])

slots.samp_salinity = Slot(uri="str(uriorcurie)", name="samp_salinity", curie=None,
                   model_uri=NMDC.samp_salinity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.samp_salinity],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.samp_store_dur = Slot(uri="str(uriorcurie)", name="samp_store_dur", curie=None,
                   model_uri=NMDC.samp_store_dur, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_store_dur])

slots.samp_store_loc = Slot(uri="str(uriorcurie)", name="samp_store_loc", curie=None,
                   model_uri=NMDC.samp_store_loc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_store_loc])

slots.samp_store_temp = Slot(uri="str(uriorcurie)", name="samp_store_temp", curie=None,
                   model_uri=NMDC.samp_store_temp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.samp_store_temp],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.samp_vol_we_dna_ext = Slot(uri="str(uriorcurie)", name="samp_vol_we_dna_ext", curie=None,
                   model_uri=NMDC.samp_vol_we_dna_ext, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.samp_vol_we_dna_ext],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.solar_irradiance = Slot(uri="str(uriorcurie)", name="solar_irradiance", curie=None,
                   model_uri=NMDC.solar_irradiance, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.solar_irradiance],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.temp = Slot(uri="str(uriorcurie)", name="temp", curie=None,
                   model_uri=NMDC.temp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.temp],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.ventilation_rate = Slot(uri="str(uriorcurie)", name="ventilation_rate", curie=None,
                   model_uri=NMDC.ventilation_rate, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.ventilation_rate],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.ventilation_type = Slot(uri="str(uriorcurie)", name="ventilation_type", curie=None,
                   model_uri=NMDC.ventilation_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ventilation_type])

slots.volatile_org_comp = Slot(uri="str(uriorcurie)", name="volatile_org_comp", curie=None,
                   model_uri=NMDC.volatile_org_comp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.volatile_org_comp])

slots.wind_direction = Slot(uri="str(uriorcurie)", name="wind_direction", curie=None,
                   model_uri=NMDC.wind_direction, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.wind_direction])

slots.wind_speed = Slot(uri="str(uriorcurie)", name="wind_speed", curie=None,
                   model_uri=NMDC.wind_speed, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.wind_speed],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.surf_material = Slot(uri="str(uriorcurie)", name="surf_material", curie=None,
                   model_uri=NMDC.surf_material, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.surf_material],
                   pattern=re.compile(r'[concrete|wood|stone|tile|plastic|glass|vinyl|metal|carpet|stainless steel|paint|cinder blocks|hay bales|stucco|adobe]'))

slots.surf_air_cont = Slot(uri="str(uriorcurie)", name="surf_air_cont", curie=None,
                   model_uri=NMDC.surf_air_cont, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.surf_air_cont],
                   pattern=re.compile(r'[dust|organic matter|particulate matter|volatile organic compounds|biological contaminants|radon|nutrients|biocides]'))

slots.rel_air_humidity = Slot(uri="str(uriorcurie)", name="rel_air_humidity", curie=None,
                   model_uri=NMDC.rel_air_humidity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.rel_air_humidity],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.abs_air_humidity = Slot(uri="str(uriorcurie)", name="abs_air_humidity", curie=None,
                   model_uri=NMDC.abs_air_humidity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.abs_air_humidity],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.surf_humidity = Slot(uri="str(uriorcurie)", name="surf_humidity", curie=None,
                   model_uri=NMDC.surf_humidity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.surf_humidity],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.air_temp = Slot(uri="str(uriorcurie)", name="air_temp", curie=None,
                   model_uri=NMDC.air_temp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.air_temp],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.surf_temp = Slot(uri="str(uriorcurie)", name="surf_temp", curie=None,
                   model_uri=NMDC.surf_temp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.surf_temp],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.surf_moisture_ph = Slot(uri="str(uriorcurie)", name="surf_moisture_ph", curie=None,
                   model_uri=NMDC.surf_moisture_ph, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.surf_moisture_ph],
                   pattern=re.compile(r'\d+[.\d+]'))

slots.build_occup_type = Slot(uri="str(uriorcurie)", name="build_occup_type", curie=None,
                   model_uri=NMDC.build_occup_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.build_occup_type],
                   pattern=re.compile(r'[office|market|restaurant|residence|school|residential|commercial|low rise|high rise|wood framed|office|health care|school|airport|sports complex]'))

slots.surf_moisture = Slot(uri="str(uriorcurie)", name="surf_moisture", curie=None,
                   model_uri=NMDC.surf_moisture, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.surf_moisture],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.dew_point = Slot(uri="str(uriorcurie)", name="dew_point", curie=None,
                   model_uri=NMDC.dew_point, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.dew_point],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.indoor_space = Slot(uri="str(uriorcurie)", name="indoor_space", curie=None,
                   model_uri=NMDC.indoor_space, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.indoor_space],
                   pattern=re.compile(r'[bedroom|office|bathroom|foyer|kitchen|locker room|hallway|elevator]'))

slots.indoor_surf = Slot(uri="str(uriorcurie)", name="indoor_surf", curie=None,
                   model_uri=NMDC.indoor_surf, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.indoor_surf],
                   pattern=re.compile(r'[counter top|window|wall|cabinet|ceiling|door|shelving|vent cover]'))

slots.filter_type = Slot(uri="str(uriorcurie)", name="filter_type", curie=None,
                   model_uri=NMDC.filter_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.filter_type],
                   pattern=re.compile(r'[particulate air filter|chemical air filter|low\-MERV pleated media|HEPA|electrostatic|gas\-phase or ultraviolet air treatments]'))

slots.heat_cool_type = Slot(uri="str(uriorcurie)", name="heat_cool_type", curie=None,
                   model_uri=NMDC.heat_cool_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.heat_cool_type],
                   pattern=re.compile(r'[radiant system|heat pump|forced air system|steam forced heat|wood stove]'))

slots.substructure_type = Slot(uri="str(uriorcurie)", name="substructure_type", curie=None,
                   model_uri=NMDC.substructure_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.substructure_type],
                   pattern=re.compile(r'[crawlspace|slab on grade|basement]'))

slots.building_setting = Slot(uri="str(uriorcurie)", name="building_setting", curie=None,
                   model_uri=NMDC.building_setting, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.building_setting],
                   pattern=re.compile(r'[urban|suburban|exurban|rural]'))

slots.light_type = Slot(uri="str(uriorcurie)", name="light_type", curie=None,
                   model_uri=NMDC.light_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.light_type],
                   pattern=re.compile(r'[natural light|electric light|desk lamp|flourescent lights|natural light|none]'))

slots.samp_sort_meth = Slot(uri="str(uriorcurie)", name="samp_sort_meth", curie=None,
                   model_uri=NMDC.samp_sort_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_sort_meth])

slots.space_typ_state = Slot(uri="str(uriorcurie)", name="space_typ_state", curie=None,
                   model_uri=NMDC.space_typ_state, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.space_typ_state],
                   pattern=re.compile(r'[typically occupied|typically unoccupied]'))

slots.typ_occup_density = Slot(uri="str(uriorcurie)", name="typ_occup_density", curie=None,
                   model_uri=NMDC.typ_occup_density, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.typ_occup_density],
                   pattern=re.compile(r'\d+[.\d+]'))

slots.occup_samp = Slot(uri="str(uriorcurie)", name="occup_samp", curie=None,
                   model_uri=NMDC.occup_samp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.occup_samp])

slots.occup_density_samp = Slot(uri="str(uriorcurie)", name="occup_density_samp", curie=None,
                   model_uri=NMDC.occup_density_samp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.occup_density_samp],
                   pattern=re.compile(r'\d+[.\d+]'))

slots.address = Slot(uri="str(uriorcurie)", name="address", curie=None,
                   model_uri=NMDC.address, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.address])

slots.adj_room = Slot(uri="str(uriorcurie)", name="adj_room", curie=None,
                   model_uri=NMDC.adj_room, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.adj_room])

slots.aero_struc = Slot(uri="str(uriorcurie)", name="aero_struc", curie=None,
                   model_uri=NMDC.aero_struc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.aero_struc],
                   pattern=re.compile(r'[plane|glider]'))

slots.amount_light = Slot(uri="str(uriorcurie)", name="amount_light", curie=None,
                   model_uri=NMDC.amount_light, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.amount_light],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.arch_struc = Slot(uri="str(uriorcurie)", name="arch_struc", curie=None,
                   model_uri=NMDC.arch_struc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.arch_struc],
                   pattern=re.compile(r'[building|shed|home]'))

slots.avg_occup = Slot(uri="str(uriorcurie)", name="avg_occup", curie=None,
                   model_uri=NMDC.avg_occup, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.avg_occup],
                   pattern=re.compile(r'\d+[.\d+]'))

slots.avg_dew_point = Slot(uri="str(uriorcurie)", name="avg_dew_point", curie=None,
                   model_uri=NMDC.avg_dew_point, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.avg_dew_point],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.avg_temp = Slot(uri="str(uriorcurie)", name="avg_temp", curie=None,
                   model_uri=NMDC.avg_temp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.avg_temp],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.bathroom_count = Slot(uri="str(uriorcurie)", name="bathroom_count", curie=None,
                   model_uri=NMDC.bathroom_count, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.bathroom_count])

slots.bedroom_count = Slot(uri="str(uriorcurie)", name="bedroom_count", curie=None,
                   model_uri=NMDC.bedroom_count, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.bedroom_count])

slots.built_struc_age = Slot(uri="str(uriorcurie)", name="built_struc_age", curie=None,
                   model_uri=NMDC.built_struc_age, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.built_struc_age],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.built_struc_set = Slot(uri="str(uriorcurie)", name="built_struc_set", curie=None,
                   model_uri=NMDC.built_struc_set, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.built_struc_set],
                   pattern=re.compile(r'[urban|rural]'))

slots.built_struc_type = Slot(uri="str(uriorcurie)", name="built_struc_type", curie=None,
                   model_uri=NMDC.built_struc_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.built_struc_type])

slots.ceil_area = Slot(uri="str(uriorcurie)", name="ceil_area", curie=None,
                   model_uri=NMDC.ceil_area, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.ceil_area],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.ceil_cond = Slot(uri="str(uriorcurie)", name="ceil_cond", curie=None,
                   model_uri=NMDC.ceil_cond, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ceil_cond],
                   pattern=re.compile(r'[new|visible wear|needs repair|damaged|rupture]'))

slots.ceil_finish_mat = Slot(uri="str(uriorcurie)", name="ceil_finish_mat", curie=None,
                   model_uri=NMDC.ceil_finish_mat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ceil_finish_mat],
                   pattern=re.compile(r'[drywall|mineral fibre|tiles|PVC|plasterboard|metal|fiberglass|stucco|mineral wool\/calcium silicate|wood]'))

slots.ceil_water_mold = Slot(uri="str(uriorcurie)", name="ceil_water_mold", curie=None,
                   model_uri=NMDC.ceil_water_mold, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ceil_water_mold],
                   pattern=re.compile(r'[presence of mold visible|no presence of mold visible]'))

slots.ceil_struc = Slot(uri="str(uriorcurie)", name="ceil_struc", curie=None,
                   model_uri=NMDC.ceil_struc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ceil_struc],
                   pattern=re.compile(r'[wood frame|concrete]'))

slots.ceil_texture = Slot(uri="str(uriorcurie)", name="ceil_texture", curie=None,
                   model_uri=NMDC.ceil_texture, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ceil_texture],
                   pattern=re.compile(r'[crows feet|crows\-foot stomp|double skip|hawk and trowel|knockdown|popcorn|orange peel|rosebud stomp|Santa\-Fe texture|skip trowel|smooth|stomp knockdown|swirl]'))

slots.ceil_thermal_mass = Slot(uri="str(uriorcurie)", name="ceil_thermal_mass", curie=None,
                   model_uri=NMDC.ceil_thermal_mass, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.ceil_thermal_mass],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.ceil_type = Slot(uri="str(uriorcurie)", name="ceil_type", curie=None,
                   model_uri=NMDC.ceil_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ceil_type],
                   pattern=re.compile(r'[cathedral|dropped|concave|barrel\-shaped|coffered|cove|stretched]'))

slots.cool_syst_id = Slot(uri="str(uriorcurie)", name="cool_syst_id", curie=None,
                   model_uri=NMDC.cool_syst_id, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.cool_syst_id])

slots.date_last_rain = Slot(uri="str(uriorcurie)", name="date_last_rain", curie=None,
                   model_uri=NMDC.date_last_rain, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.date_last_rain])

slots.build_docs = Slot(uri="str(uriorcurie)", name="build_docs", curie=None,
                   model_uri=NMDC.build_docs, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.build_docs],
                   pattern=re.compile(r'[building information model|commissioning report|complaint logs|contract administration|cost estimate|janitorial schedules or logs|maintenance plans|schedule|sections|shop drawings|submittals|ventilation system|windows] '))

slots.door_size = Slot(uri="str(uriorcurie)", name="door_size", curie=None,
                   model_uri=NMDC.door_size, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.door_size],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.door_cond = Slot(uri="str(uriorcurie)", name="door_cond", curie=None,
                   model_uri=NMDC.door_cond, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.door_cond],
                   pattern=re.compile(r'[damaged|needs repair|new|rupture|visible wear]'))

slots.door_direct = Slot(uri="str(uriorcurie)", name="door_direct", curie=None,
                   model_uri=NMDC.door_direct, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.door_direct],
                   pattern=re.compile(r'[inward|outward|sideways]'))

slots.door_loc = Slot(uri="str(uriorcurie)", name="door_loc", curie=None,
                   model_uri=NMDC.door_loc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.door_loc],
                   pattern=re.compile(r'[north|south|east|west]'))

slots.door_mat = Slot(uri="str(uriorcurie)", name="door_mat", curie=None,
                   model_uri=NMDC.door_mat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.door_mat],
                   pattern=re.compile(r'[aluminum|cellular PVC|engineered plastic|fiberboard|fiberglass|metal|thermoplastic alloy|vinyl|wood|wood\/plastic composite]'))

slots.door_move = Slot(uri="str(uriorcurie)", name="door_move", curie=None,
                   model_uri=NMDC.door_move, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.door_move],
                   pattern=re.compile(r'[collapsible|folding|revolving|rolling shutter|sliding|swinging] '))

slots.door_water_mold = Slot(uri="str(uriorcurie)", name="door_water_mold", curie=None,
                   model_uri=NMDC.door_water_mold, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.door_water_mold],
                   pattern=re.compile(r'[presence of mold visible|no presence of mold visible]'))

slots.door_type = Slot(uri="str(uriorcurie)", name="door_type", curie=None,
                   model_uri=NMDC.door_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.door_type],
                   pattern=re.compile(r'[composite|metal|wooden]'))

slots.door_comp_type = Slot(uri="str(uriorcurie)", name="door_comp_type", curie=None,
                   model_uri=NMDC.door_comp_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.door_comp_type],
                   pattern=re.compile(r'[metal covered|revolving|sliding|telescopic]'))

slots.door_type_metal = Slot(uri="str(uriorcurie)", name="door_type_metal", curie=None,
                   model_uri=NMDC.door_type_metal, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.door_type_metal],
                   pattern=re.compile(r'[collapsible|corrugated steel|hollow|rolling shutters|steel plate]'))

slots.door_type_wood = Slot(uri="str(uriorcurie)", name="door_type_wood", curie=None,
                   model_uri=NMDC.door_type_wood, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.door_type_wood],
                   pattern=re.compile(r'[bettened and ledged|battened|ledged and braced|battened|ledged and framed|battened|ledged, braced and frame|framed and paneled|glashed or sash|flush|louvered|wire gauged]'))

slots.drawings = Slot(uri="str(uriorcurie)", name="drawings", curie=None,
                   model_uri=NMDC.drawings, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.drawings],
                   pattern=re.compile(r'[operation|as built|construction|bid|design|building navigation map|diagram|sketch]'))

slots.elevator = Slot(uri="str(uriorcurie)", name="elevator", curie=None,
                   model_uri=NMDC.elevator, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.elevator])

slots.escalator = Slot(uri="str(uriorcurie)", name="escalator", curie=None,
                   model_uri=NMDC.escalator, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.escalator])

slots.exp_duct = Slot(uri="str(uriorcurie)", name="exp_duct", curie=None,
                   model_uri=NMDC.exp_duct, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.exp_duct],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.exp_pipe = Slot(uri="str(uriorcurie)", name="exp_pipe", curie=None,
                   model_uri=NMDC.exp_pipe, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.exp_pipe])

slots.ext_door = Slot(uri="str(uriorcurie)", name="ext_door", curie=None,
                   model_uri=NMDC.ext_door, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ext_door])

slots.fireplace_type = Slot(uri="str(uriorcurie)", name="fireplace_type", curie=None,
                   model_uri=NMDC.fireplace_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.fireplace_type],
                   pattern=re.compile(r'[gas burning|wood burning]'))

slots.floor_age = Slot(uri="str(uriorcurie)", name="floor_age", curie=None,
                   model_uri=NMDC.floor_age, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.floor_age],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.floor_area = Slot(uri="str(uriorcurie)", name="floor_area", curie=None,
                   model_uri=NMDC.floor_area, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.floor_area],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.floor_cond = Slot(uri="str(uriorcurie)", name="floor_cond", curie=None,
                   model_uri=NMDC.floor_cond, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.floor_cond],
                   pattern=re.compile(r'[new|visible wear|needs repair|damaged|rupture]'))

slots.floor_count = Slot(uri="str(uriorcurie)", name="floor_count", curie=None,
                   model_uri=NMDC.floor_count, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.floor_count])

slots.floor_finish_mat = Slot(uri="str(uriorcurie)", name="floor_finish_mat", curie=None,
                   model_uri=NMDC.floor_finish_mat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.floor_finish_mat],
                   pattern=re.compile(r'[tile|wood strip or parquet|carpet|rug|laminate wood|lineoleum|vinyl composition tile|sheet vinyl|stone|bamboo|cork|terrazo|concrete|none;specify unfinished|sealed|clear finish|paint]'))

slots.floor_water_mold = Slot(uri="str(uriorcurie)", name="floor_water_mold", curie=None,
                   model_uri=NMDC.floor_water_mold, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.floor_water_mold],
                   pattern=re.compile(r'[mold odor|wet floor|water stains|wall discoloration|floor discoloration|ceiling discoloration|peeling paint or wallpaper|bulging walls|condensation]'))

slots.floor_struc = Slot(uri="str(uriorcurie)", name="floor_struc", curie=None,
                   model_uri=NMDC.floor_struc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.floor_struc],
                   pattern=re.compile(r'[balcony|floating floor|glass floor|raised floor|sprung floor|wood\-framed|concrete]'))

slots.floor_thermal_mass = Slot(uri="str(uriorcurie)", name="floor_thermal_mass", curie=None,
                   model_uri=NMDC.floor_thermal_mass, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.floor_thermal_mass],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.freq_clean = Slot(uri="str(uriorcurie)", name="freq_clean", curie=None,
                   model_uri=NMDC.freq_clean, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.freq_clean])

slots.freq_cook = Slot(uri="str(uriorcurie)", name="freq_cook", curie=None,
                   model_uri=NMDC.freq_cook, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.freq_cook])

slots.furniture = Slot(uri="str(uriorcurie)", name="furniture", curie=None,
                   model_uri=NMDC.furniture, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.furniture],
                   pattern=re.compile(r'[cabinet|chair|desks]'))

slots.gender_restroom = Slot(uri="str(uriorcurie)", name="gender_restroom", curie=None,
                   model_uri=NMDC.gender_restroom, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.gender_restroom],
                   pattern=re.compile(r'[male|female]'))

slots.hall_count = Slot(uri="str(uriorcurie)", name="hall_count", curie=None,
                   model_uri=NMDC.hall_count, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.hall_count])

slots.handidness = Slot(uri="str(uriorcurie)", name="handidness", curie=None,
                   model_uri=NMDC.handidness, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.handidness],
                   pattern=re.compile(r'[ambidexterity|left handedness|mixed\-handedness|right handedness]'))

slots.heat_deliv_loc = Slot(uri="str(uriorcurie)", name="heat_deliv_loc", curie=None,
                   model_uri=NMDC.heat_deliv_loc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.heat_deliv_loc],
                   pattern=re.compile(r'[north|south|east|west]'))

slots.heat_system_deliv_meth = Slot(uri="str(uriorcurie)", name="heat_system_deliv_meth", curie=None,
                   model_uri=NMDC.heat_system_deliv_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.heat_system_deliv_meth],
                   pattern=re.compile(r'[conductive|radiant]'))

slots.heat_system_id = Slot(uri="str(uriorcurie)", name="heat_system_id", curie=None,
                   model_uri=NMDC.heat_system_id, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.heat_system_id])

slots.height_carper_fiber = Slot(uri="str(uriorcurie)", name="height_carper_fiber", curie=None,
                   model_uri=NMDC.height_carper_fiber, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.height_carper_fiber],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.inside_lux = Slot(uri="str(uriorcurie)", name="inside_lux", curie=None,
                   model_uri=NMDC.inside_lux, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.inside_lux],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.int_wall_cond = Slot(uri="str(uriorcurie)", name="int_wall_cond", curie=None,
                   model_uri=NMDC.int_wall_cond, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.int_wall_cond],
                   pattern=re.compile(r'[new|visible wear|needs repair|damaged|rupture]'))

slots.last_clean = Slot(uri="str(uriorcurie)", name="last_clean", curie=None,
                   model_uri=NMDC.last_clean, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.last_clean])

slots.max_occup = Slot(uri="str(uriorcurie)", name="max_occup", curie=None,
                   model_uri=NMDC.max_occup, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.max_occup])

slots.mech_struc = Slot(uri="str(uriorcurie)", name="mech_struc", curie=None,
                   model_uri=NMDC.mech_struc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.mech_struc],
                   pattern=re.compile(r'[subway|coach|carriage|elevator|escalator|boat|train|car|bus]'))

slots.number_plants = Slot(uri="str(uriorcurie)", name="number_plants", curie=None,
                   model_uri=NMDC.number_plants, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.number_plants])

slots.number_pets = Slot(uri="str(uriorcurie)", name="number_pets", curie=None,
                   model_uri=NMDC.number_pets, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.number_pets])

slots.number_resident = Slot(uri="str(uriorcurie)", name="number_resident", curie=None,
                   model_uri=NMDC.number_resident, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.number_resident])

slots.occup_document = Slot(uri="str(uriorcurie)", name="occup_document", curie=None,
                   model_uri=NMDC.occup_document, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.occup_document],
                   pattern=re.compile(r'[automated count|estimate|manual count|videos]'))

slots.ext_wall_orient = Slot(uri="str(uriorcurie)", name="ext_wall_orient", curie=None,
                   model_uri=NMDC.ext_wall_orient, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ext_wall_orient],
                   pattern=re.compile(r'[north|south|east|west|northeast|southeast|southwest|northwest]'))

slots.ext_window_orient = Slot(uri="str(uriorcurie)", name="ext_window_orient", curie=None,
                   model_uri=NMDC.ext_window_orient, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ext_window_orient],
                   pattern=re.compile(r'[north|south|east|west|northeast|southeast|southwest|northwest]'))

slots.rel_humidity_out = Slot(uri="str(uriorcurie)", name="rel_humidity_out", curie=None,
                   model_uri=NMDC.rel_humidity_out, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.rel_humidity_out],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.pres_animal = Slot(uri="str(uriorcurie)", name="pres_animal", curie=None,
                   model_uri=NMDC.pres_animal, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.pres_animal])

slots.quad_pos = Slot(uri="str(uriorcurie)", name="quad_pos", curie=None,
                   model_uri=NMDC.quad_pos, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.quad_pos],
                   pattern=re.compile(r'[North side|West side|South side|East side]'))

slots.rel_samp_loc = Slot(uri="str(uriorcurie)", name="rel_samp_loc", curie=None,
                   model_uri=NMDC.rel_samp_loc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.rel_samp_loc],
                   pattern=re.compile(r'[edge of car|center of car|under a seat]'))

slots.room_air_exch_rate = Slot(uri="str(uriorcurie)", name="room_air_exch_rate", curie=None,
                   model_uri=NMDC.room_air_exch_rate, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.room_air_exch_rate],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.room_architec_element = Slot(uri="str(uriorcurie)", name="room_architec_element", curie=None,
                   model_uri=NMDC.room_architec_element, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_architec_element])

slots.room_condt = Slot(uri="str(uriorcurie)", name="room_condt", curie=None,
                   model_uri=NMDC.room_condt, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_condt],
                   pattern=re.compile(r'[new|visible wear|needs repair|damaged|rupture|visible signs of mold\/mildew]'))

slots.room_count = Slot(uri="str(uriorcurie)", name="room_count", curie=None,
                   model_uri=NMDC.room_count, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_count])

slots.room_dim = Slot(uri="str(uriorcurie)", name="room_dim", curie=None,
                   model_uri=NMDC.room_dim, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.room_dim])

slots.room_door_dist = Slot(uri="str(uriorcurie)", name="room_door_dist", curie=None,
                   model_uri=NMDC.room_door_dist, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.room_door_dist])

slots.room_loc = Slot(uri="str(uriorcurie)", name="room_loc", curie=None,
                   model_uri=NMDC.room_loc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_loc],
                   pattern=re.compile(r'[corner room|interior room|exterior wall]'))

slots.room_moist_damage_hist = Slot(uri="str(uriorcurie)", name="room_moist_damage_hist", curie=None,
                   model_uri=NMDC.room_moist_damage_hist, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_moist_damage_hist])

slots.room_net_area = Slot(uri="str(uriorcurie)", name="room_net_area", curie=None,
                   model_uri=NMDC.room_net_area, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.room_net_area])

slots.room_occup = Slot(uri="str(uriorcurie)", name="room_occup", curie=None,
                   model_uri=NMDC.room_occup, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.room_occup])

slots.room_samp_pos = Slot(uri="str(uriorcurie)", name="room_samp_pos", curie=None,
                   model_uri=NMDC.room_samp_pos, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_samp_pos],
                   pattern=re.compile(r'[north corner|south corner|west corner|east corner|northeast corner|northwest corner|southeast corner|southwest corner|center]'))

slots.room_type = Slot(uri="str(uriorcurie)", name="room_type", curie=None,
                   model_uri=NMDC.room_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_type],
                   pattern=re.compile(r'[attic|bathroom|closet|conference room|elevator|examining room|hallway|kitchen|mail room|private office|open office|stairwell|,restroom|lobby|vestibule|mechanical or electrical room|data center|laboratory_wet|laboratory_dry|gymnasium|natatorium|auditorium|lockers|cafe|warehouse]'))

slots.room_vol = Slot(uri="str(uriorcurie)", name="room_vol", curie=None,
                   model_uri=NMDC.room_vol, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.room_vol])

slots.room_window_count = Slot(uri="str(uriorcurie)", name="room_window_count", curie=None,
                   model_uri=NMDC.room_window_count, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_window_count])

slots.room_connected = Slot(uri="str(uriorcurie)", name="room_connected", curie=None,
                   model_uri=NMDC.room_connected, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_connected],
                   pattern=re.compile(r'[attic|bathroom|closet|conference room|elevator|examining room|hallway|kitchen|mail room|office|stairwell]'))

slots.room_hallway = Slot(uri="str(uriorcurie)", name="room_hallway", curie=None,
                   model_uri=NMDC.room_hallway, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_hallway])

slots.room_door_share = Slot(uri="str(uriorcurie)", name="room_door_share", curie=None,
                   model_uri=NMDC.room_door_share, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_door_share])

slots.room_wall_share = Slot(uri="str(uriorcurie)", name="room_wall_share", curie=None,
                   model_uri=NMDC.room_wall_share, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_wall_share])

slots.samp_weather = Slot(uri="str(uriorcurie)", name="samp_weather", curie=None,
                   model_uri=NMDC.samp_weather, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_weather],
                   pattern=re.compile(r'[clear sky|cloudy|foggy|hail|rain|snow|sleet|sunny|windy]'))

slots.samp_floor = Slot(uri="str(uriorcurie)", name="samp_floor", curie=None,
                   model_uri=NMDC.samp_floor, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_floor])

slots.samp_room_id = Slot(uri="str(uriorcurie)", name="samp_room_id", curie=None,
                   model_uri=NMDC.samp_room_id, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_room_id])

slots.samp_time_out = Slot(uri="str(uriorcurie)", name="samp_time_out", curie=None,
                   model_uri=NMDC.samp_time_out, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_time_out],
                   pattern=re.compile(r'\d+[.\d+]'))

slots.season = Slot(uri="str(uriorcurie)", name="season", curie=None,
                   model_uri=NMDC.season, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.season],
                   pattern=re.compile(r'[Spring|Summer|Fall|Winter]'))

slots.season_use = Slot(uri="str(uriorcurie)", name="season_use", curie=None,
                   model_uri=NMDC.season_use, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.season_use],
                   pattern=re.compile(r'[Spring|Summer|Fall|Winter]'))

slots.shading_device_cond = Slot(uri="str(uriorcurie)", name="shading_device_cond", curie=None,
                   model_uri=NMDC.shading_device_cond, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.shading_device_cond],
                   pattern=re.compile(r'[damaged|needs repair|new|rupture|visible wear]'))

slots.shading_device_loc = Slot(uri="str(uriorcurie)", name="shading_device_loc", curie=None,
                   model_uri=NMDC.shading_device_loc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.shading_device_loc],
                   pattern=re.compile(r'[exterior|interior]'))

slots.shading_device_mat = Slot(uri="str(uriorcurie)", name="shading_device_mat", curie=None,
                   model_uri=NMDC.shading_device_mat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.shading_device_mat])

slots.shading_device_water_mold = Slot(uri="str(uriorcurie)", name="shading_device_water_mold", curie=None,
                   model_uri=NMDC.shading_device_water_mold, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.shading_device_water_mold],
                   pattern=re.compile(r'[presence of mold visible|no presence of mold visible]'))

slots.shading_device_type = Slot(uri="str(uriorcurie)", name="shading_device_type", curie=None,
                   model_uri=NMDC.shading_device_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.shading_device_type],
                   pattern=re.compile(r'[bahama shutters|exterior roll blind|gambrel awning|hood awning|porchroller awning|sarasota shutters|slatted aluminum|solid aluminum awning|sun screen|tree|trellis|venetian awning]'))

slots.specific_humidity = Slot(uri="str(uriorcurie)", name="specific_humidity", curie=None,
                   model_uri=NMDC.specific_humidity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.specific_humidity],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.specific = Slot(uri="str(uriorcurie)", name="specific", curie=None,
                   model_uri=NMDC.specific, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.specific],
                   pattern=re.compile(r'[operation|as built|construction|bid|design|photos]'))

slots.temp_out = Slot(uri="str(uriorcurie)", name="temp_out", curie=None,
                   model_uri=NMDC.temp_out, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.temp_out],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.train_line = Slot(uri="str(uriorcurie)", name="train_line", curie=None,
                   model_uri=NMDC.train_line, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.train_line],
                   pattern=re.compile(r'[red|green|orange]'))

slots.train_stat_loc = Slot(uri="str(uriorcurie)", name="train_stat_loc", curie=None,
                   model_uri=NMDC.train_stat_loc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.train_stat_loc],
                   pattern=re.compile(r'[south station above ground|south station underground|south station amtrak|forest hills|riverside]'))

slots.train_stop_loc = Slot(uri="str(uriorcurie)", name="train_stop_loc", curie=None,
                   model_uri=NMDC.train_stop_loc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.train_stop_loc],
                   pattern=re.compile(r'[end|mid|downtown]'))

slots.vis_media = Slot(uri="str(uriorcurie)", name="vis_media", curie=None,
                   model_uri=NMDC.vis_media, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.vis_media],
                   pattern=re.compile(r'[photos|videos|commonly of the building|site context (adjacent buildings, vegetation, terrain, streets)|interiors|equipment|3D scans]'))

slots.wall_area = Slot(uri="str(uriorcurie)", name="wall_area", curie=None,
                   model_uri=NMDC.wall_area, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.wall_area],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.wall_const_type = Slot(uri="str(uriorcurie)", name="wall_const_type", curie=None,
                   model_uri=NMDC.wall_const_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.wall_const_type],
                   pattern=re.compile(r'[frame construction|joisted masonry|light noncombustible|masonry noncombustible|modified fire resistive|fire resistive]'))

slots.wall_finish_mat = Slot(uri="str(uriorcurie)", name="wall_finish_mat", curie=None,
                   model_uri=NMDC.wall_finish_mat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.wall_finish_mat],
                   pattern=re.compile(r'[plaster|gypsum plaster|veneer plaster|gypsum board|tile|terrazzo|stone facing|acoustical treatment|wood|metal|masonry]'))

slots.wall_height = Slot(uri="str(uriorcurie)", name="wall_height", curie=None,
                   model_uri=NMDC.wall_height, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.wall_height],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.wall_loc = Slot(uri="str(uriorcurie)", name="wall_loc", curie=None,
                   model_uri=NMDC.wall_loc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.wall_loc],
                   pattern=re.compile(r'[north|south|east|west]'))

slots.wall_water_mold = Slot(uri="str(uriorcurie)", name="wall_water_mold", curie=None,
                   model_uri=NMDC.wall_water_mold, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.wall_water_mold],
                   pattern=re.compile(r'[presence of mold visible|no presence of mold visible]'))

slots.wall_surf_treatment = Slot(uri="str(uriorcurie)", name="wall_surf_treatment", curie=None,
                   model_uri=NMDC.wall_surf_treatment, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.wall_surf_treatment],
                   pattern=re.compile(r'[painted|wall paper|no treatment|paneling|stucco|fabric]'))

slots.wall_texture = Slot(uri="str(uriorcurie)", name="wall_texture", curie=None,
                   model_uri=NMDC.wall_texture, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.wall_texture],
                   pattern=re.compile(r'[crows feet|crows\-foot stomp|double skip|hawk and trowel|knockdown|popcorn|orange peel|rosebud stomp|Santa\-Fe texture|skip trowel|smooth|stomp knockdown|swirl]'))

slots.wall_thermal_mass = Slot(uri="str(uriorcurie)", name="wall_thermal_mass", curie=None,
                   model_uri=NMDC.wall_thermal_mass, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.wall_thermal_mass],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.water_feat_size = Slot(uri="str(uriorcurie)", name="water_feat_size", curie=None,
                   model_uri=NMDC.water_feat_size, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.water_feat_size],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.water_feat_type = Slot(uri="str(uriorcurie)", name="water_feat_type", curie=None,
                   model_uri=NMDC.water_feat_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.water_feat_type],
                   pattern=re.compile(r'[fountain|pool|standing feature|stream|waterfall]'))

slots.weekday = Slot(uri="str(uriorcurie)", name="weekday", curie=None,
                   model_uri=NMDC.weekday, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.weekday],
                   pattern=re.compile(r'[Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday]'))

slots.window_size = Slot(uri="str(uriorcurie)", name="window_size", curie=None,
                   model_uri=NMDC.window_size, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.window_size],
                   pattern=re.compile(r'\d+[.\d+] \S+ x \d+[.\d+] \S+'))

slots.window_cond = Slot(uri="str(uriorcurie)", name="window_cond", curie=None,
                   model_uri=NMDC.window_cond, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.window_cond],
                   pattern=re.compile(r'[damaged|needs repair|new|rupture|visible wear]'))

slots.window_cover = Slot(uri="str(uriorcurie)", name="window_cover", curie=None,
                   model_uri=NMDC.window_cover, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.window_cover],
                   pattern=re.compile(r'[blinds|curtains|none]'))

slots.window_horiz_pos = Slot(uri="str(uriorcurie)", name="window_horiz_pos", curie=None,
                   model_uri=NMDC.window_horiz_pos, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.window_horiz_pos],
                   pattern=re.compile(r'[left|middle|right]'))

slots.window_loc = Slot(uri="str(uriorcurie)", name="window_loc", curie=None,
                   model_uri=NMDC.window_loc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.window_loc],
                   pattern=re.compile(r'[north|south|east|west]'))

slots.window_mat = Slot(uri="str(uriorcurie)", name="window_mat", curie=None,
                   model_uri=NMDC.window_mat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.window_mat],
                   pattern=re.compile(r'[clad|fiberglass|metal|vinyl|wood]'))

slots.window_open_freq = Slot(uri="str(uriorcurie)", name="window_open_freq", curie=None,
                   model_uri=NMDC.window_open_freq, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.window_open_freq])

slots.window_water_mold = Slot(uri="str(uriorcurie)", name="window_water_mold", curie=None,
                   model_uri=NMDC.window_water_mold, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.window_water_mold],
                   pattern=re.compile(r'[presence of mold visible|no presence of mold visible]'))

slots.window_status = Slot(uri="str(uriorcurie)", name="window_status", curie=None,
                   model_uri=NMDC.window_status, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.window_status],
                   pattern=re.compile(r'[closed|open]'))

slots.window_type = Slot(uri="str(uriorcurie)", name="window_type", curie=None,
                   model_uri=NMDC.window_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.window_type],
                   pattern=re.compile(r'[single\-hung sash window|horizontal sash window|fixed window] '))

slots.window_vert_pos = Slot(uri="str(uriorcurie)", name="window_vert_pos", curie=None,
                   model_uri=NMDC.window_vert_pos, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.window_vert_pos],
                   pattern=re.compile(r'[bottom|middle|top|low|middle|high]'))

slots.ances_data = Slot(uri="str(uriorcurie)", name="ances_data", curie=None,
                   model_uri=NMDC.ances_data, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ances_data])

slots.biol_stat = Slot(uri="str(uriorcurie)", name="biol_stat", curie=None,
                   model_uri=NMDC.biol_stat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.biol_stat],
                   pattern=re.compile(r'[wild|natural|semi\-natural|inbred line|breeder\'s line|hybrid|clonal selection|mutant]'))

slots.genetic_mod = Slot(uri="str(uriorcurie)", name="genetic_mod", curie=None,
                   model_uri=NMDC.genetic_mod, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.genetic_mod])

slots.host_common_name = Slot(uri="str(uriorcurie)", name="host_common_name", curie=None,
                   model_uri=NMDC.host_common_name, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_common_name])

slots.samp_capt_status = Slot(uri="str(uriorcurie)", name="samp_capt_status", curie=None,
                   model_uri=NMDC.samp_capt_status, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_capt_status],
                   pattern=re.compile(r'[active surveillance in response to an outbreak|active surveillance not initiated by an outbreak|farm sample|market sample|other]'))

slots.samp_dis_stage = Slot(uri="str(uriorcurie)", name="samp_dis_stage", curie=None,
                   model_uri=NMDC.samp_dis_stage, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_dis_stage])

slots.host_taxid = Slot(uri="str(uriorcurie)", name="host_taxid", curie=None,
                   model_uri=NMDC.host_taxid, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_taxid])

slots.host_subject_id = Slot(uri="str(uriorcurie)", name="host_subject_id", curie=None,
                   model_uri=NMDC.host_subject_id, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_subject_id])

slots.host_age = Slot(uri="str(uriorcurie)", name="host_age", curie=None,
                   model_uri=NMDC.host_age, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_age],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.host_life_stage = Slot(uri="str(uriorcurie)", name="host_life_stage", curie=None,
                   model_uri=NMDC.host_life_stage, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_life_stage])

slots.host_sex = Slot(uri="str(uriorcurie)", name="host_sex", curie=None,
                   model_uri=NMDC.host_sex, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_sex],
                   pattern=re.compile(r'[male|female|neuter|hermaphrodite|not determined]'))

slots.host_disease_stat = Slot(uri="str(uriorcurie)", name="host_disease_stat", curie=None,
                   model_uri=NMDC.host_disease_stat, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.host_disease_stat])

slots.host_body_habitat = Slot(uri="str(uriorcurie)", name="host_body_habitat", curie=None,
                   model_uri=NMDC.host_body_habitat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_body_habitat])

slots.host_body_site = Slot(uri="str(uriorcurie)", name="host_body_site", curie=None,
                   model_uri=NMDC.host_body_site, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.host_body_site],
                   pattern=re.compile(r'.* \S+:\S+'))

slots.host_body_product = Slot(uri="str(uriorcurie)", name="host_body_product", curie=None,
                   model_uri=NMDC.host_body_product, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.host_body_product],
                   pattern=re.compile(r'.* \S+:\S+'))

slots.host_tot_mass = Slot(uri="str(uriorcurie)", name="host_tot_mass", curie=None,
                   model_uri=NMDC.host_tot_mass, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_tot_mass],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.host_height = Slot(uri="str(uriorcurie)", name="host_height", curie=None,
                   model_uri=NMDC.host_height, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_height],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.host_length = Slot(uri="str(uriorcurie)", name="host_length", curie=None,
                   model_uri=NMDC.host_length, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_length],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.host_diet = Slot(uri="str(uriorcurie)", name="host_diet", curie=None,
                   model_uri=NMDC.host_diet, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_diet])

slots.host_last_meal = Slot(uri="str(uriorcurie)", name="host_last_meal", curie=None,
                   model_uri=NMDC.host_last_meal, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_last_meal])

slots.host_growth_cond = Slot(uri="str(uriorcurie)", name="host_growth_cond", curie=None,
                   model_uri=NMDC.host_growth_cond, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_growth_cond])

slots.host_substrate = Slot(uri="str(uriorcurie)", name="host_substrate", curie=None,
                   model_uri=NMDC.host_substrate, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_substrate])

slots.host_family_relationship = Slot(uri="str(uriorcurie)", name="host_family_relationship", curie=None,
                   model_uri=NMDC.host_family_relationship, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_family_relationship])

slots.host_infra_specific_name = Slot(uri="str(uriorcurie)", name="host_infra_specific_name", curie=None,
                   model_uri=NMDC.host_infra_specific_name, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_infra_specific_name])

slots.host_infra_specific_rank = Slot(uri="str(uriorcurie)", name="host_infra_specific_rank", curie=None,
                   model_uri=NMDC.host_infra_specific_rank, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_infra_specific_rank])

slots.host_genotype = Slot(uri="str(uriorcurie)", name="host_genotype", curie=None,
                   model_uri=NMDC.host_genotype, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_genotype])

slots.host_phenotype = Slot(uri="str(uriorcurie)", name="host_phenotype", curie=None,
                   model_uri=NMDC.host_phenotype, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.host_phenotype],
                   pattern=re.compile(r'.* \S+:\S+'))

slots.host_body_temp = Slot(uri="str(uriorcurie)", name="host_body_temp", curie=None,
                   model_uri=NMDC.host_body_temp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_body_temp],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.host_dry_mass = Slot(uri="str(uriorcurie)", name="host_dry_mass", curie=None,
                   model_uri=NMDC.host_dry_mass, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_dry_mass],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.host_blood_press_diast = Slot(uri="str(uriorcurie)", name="host_blood_press_diast", curie=None,
                   model_uri=NMDC.host_blood_press_diast, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_blood_press_diast],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.host_blood_press_syst = Slot(uri="str(uriorcurie)", name="host_blood_press_syst", curie=None,
                   model_uri=NMDC.host_blood_press_syst, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_blood_press_syst],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.host_color = Slot(uri="str(uriorcurie)", name="host_color", curie=None,
                   model_uri=NMDC.host_color, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_color])

slots.host_shape = Slot(uri="str(uriorcurie)", name="host_shape", curie=None,
                   model_uri=NMDC.host_shape, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_shape])

slots.gravidity = Slot(uri="str(uriorcurie)", name="gravidity", curie=None,
                   model_uri=NMDC.gravidity, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.gravidity])

slots.ihmc_medication_code = Slot(uri="str(uriorcurie)", name="ihmc_medication_code", curie=None,
                   model_uri=NMDC.ihmc_medication_code, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ihmc_medication_code])

slots.smoker = Slot(uri="str(uriorcurie)", name="smoker", curie=None,
                   model_uri=NMDC.smoker, domain=None, range=Optional[Union[dict, BooleanValue]], mappings = [MIXS.smoker],
                   pattern=re.compile(r'[true|false]'))

slots.host_hiv_stat = Slot(uri="str(uriorcurie)", name="host_hiv_stat", curie=None,
                   model_uri=NMDC.host_hiv_stat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_hiv_stat],
                   pattern=re.compile(r'[true|false];[true|false]'))

slots.drug_usage = Slot(uri="str(uriorcurie)", name="drug_usage", curie=None,
                   model_uri=NMDC.drug_usage, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.drug_usage])

slots.host_body_mass_index = Slot(uri="str(uriorcurie)", name="host_body_mass_index", curie=None,
                   model_uri=NMDC.host_body_mass_index, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_body_mass_index],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.diet_last_six_month = Slot(uri="str(uriorcurie)", name="diet_last_six_month", curie=None,
                   model_uri=NMDC.diet_last_six_month, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.diet_last_six_month])

slots.weight_loss_3_month = Slot(uri="str(uriorcurie)", name="weight_loss_3_month", curie=None,
                   model_uri=NMDC.weight_loss_3_month, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.weight_loss_3_month],
                   pattern=re.compile(r'[true|false];\d+[.\d+] \S+'))

slots.ihmc_ethnicity = Slot(uri="str(uriorcurie)", name="ihmc_ethnicity", curie=None,
                   model_uri=NMDC.ihmc_ethnicity, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ihmc_ethnicity])

slots.host_occupation = Slot(uri="str(uriorcurie)", name="host_occupation", curie=None,
                   model_uri=NMDC.host_occupation, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_occupation])

slots.pet_farm_animal = Slot(uri="str(uriorcurie)", name="pet_farm_animal", curie=None,
                   model_uri=NMDC.pet_farm_animal, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.pet_farm_animal])

slots.travel_out_six_month = Slot(uri="str(uriorcurie)", name="travel_out_six_month", curie=None,
                   model_uri=NMDC.travel_out_six_month, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.travel_out_six_month])

slots.twin_sibling = Slot(uri="str(uriorcurie)", name="twin_sibling", curie=None,
                   model_uri=NMDC.twin_sibling, domain=None, range=Optional[Union[dict, BooleanValue]], mappings = [MIXS.twin_sibling],
                   pattern=re.compile(r'[true|false]'))

slots.medic_hist_perform = Slot(uri="str(uriorcurie)", name="medic_hist_perform", curie=None,
                   model_uri=NMDC.medic_hist_perform, domain=None, range=Optional[Union[dict, BooleanValue]], mappings = [MIXS.medic_hist_perform],
                   pattern=re.compile(r'[true|false]'))

slots.study_complt_stat = Slot(uri="str(uriorcurie)", name="study_complt_stat", curie=None,
                   model_uri=NMDC.study_complt_stat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.study_complt_stat],
                   pattern=re.compile(r'[true|false];[adverse event|non\-compliance|lost to follow up|other\-specify]'))

slots.pulmonary_disord = Slot(uri="str(uriorcurie)", name="pulmonary_disord", curie=None,
                   model_uri=NMDC.pulmonary_disord, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.pulmonary_disord])

slots.nose_throat_disord = Slot(uri="str(uriorcurie)", name="nose_throat_disord", curie=None,
                   model_uri=NMDC.nose_throat_disord, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.nose_throat_disord])

slots.blood_blood_disord = Slot(uri="str(uriorcurie)", name="blood_blood_disord", curie=None,
                   model_uri=NMDC.blood_blood_disord, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.blood_blood_disord])

slots.host_pulse = Slot(uri="str(uriorcurie)", name="host_pulse", curie=None,
                   model_uri=NMDC.host_pulse, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_pulse],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.gestation_state = Slot(uri="str(uriorcurie)", name="gestation_state", curie=None,
                   model_uri=NMDC.gestation_state, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.gestation_state])

slots.maternal_health_stat = Slot(uri="str(uriorcurie)", name="maternal_health_stat", curie=None,
                   model_uri=NMDC.maternal_health_stat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.maternal_health_stat])

slots.foetal_health_stat = Slot(uri="str(uriorcurie)", name="foetal_health_stat", curie=None,
                   model_uri=NMDC.foetal_health_stat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.foetal_health_stat])

slots.amniotic_fluid_color = Slot(uri="str(uriorcurie)", name="amniotic_fluid_color", curie=None,
                   model_uri=NMDC.amniotic_fluid_color, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.amniotic_fluid_color])

slots.kidney_disord = Slot(uri="str(uriorcurie)", name="kidney_disord", curie=None,
                   model_uri=NMDC.kidney_disord, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.kidney_disord])

slots.urogenit_tract_disor = Slot(uri="str(uriorcurie)", name="urogenit_tract_disor", curie=None,
                   model_uri=NMDC.urogenit_tract_disor, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.urogenit_tract_disor])

slots.urine_collect_meth = Slot(uri="str(uriorcurie)", name="urine_collect_meth", curie=None,
                   model_uri=NMDC.urine_collect_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.urine_collect_meth],
                   pattern=re.compile(r'[clean catch|catheter]'))

slots.gastrointest_disord = Slot(uri="str(uriorcurie)", name="gastrointest_disord", curie=None,
                   model_uri=NMDC.gastrointest_disord, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.gastrointest_disord])

slots.liver_disord = Slot(uri="str(uriorcurie)", name="liver_disord", curie=None,
                   model_uri=NMDC.liver_disord, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.liver_disord])

slots.special_diet = Slot(uri="str(uriorcurie)", name="special_diet", curie=None,
                   model_uri=NMDC.special_diet, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.special_diet],
                   pattern=re.compile(r'[low carb|reduced calorie|vegetarian|other(to be specified)]'))

slots.nose_mouth_teeth_throat_disord = Slot(uri="str(uriorcurie)", name="nose_mouth_teeth_throat_disord", curie=None,
                   model_uri=NMDC.nose_mouth_teeth_throat_disord, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.nose_mouth_teeth_throat_disord])

slots.time_last_toothbrush = Slot(uri="str(uriorcurie)", name="time_last_toothbrush", curie=None,
                   model_uri=NMDC.time_last_toothbrush, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.time_last_toothbrush])

slots.dermatology_disord = Slot(uri="str(uriorcurie)", name="dermatology_disord", curie=None,
                   model_uri=NMDC.dermatology_disord, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.dermatology_disord])

slots.time_since_last_wash = Slot(uri="str(uriorcurie)", name="time_since_last_wash", curie=None,
                   model_uri=NMDC.time_since_last_wash, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.time_since_last_wash])

slots.dominant_hand = Slot(uri="str(uriorcurie)", name="dominant_hand", curie=None,
                   model_uri=NMDC.dominant_hand, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.dominant_hand],
                   pattern=re.compile(r'[left|right|ambidextrous]'))

slots.menarche = Slot(uri="str(uriorcurie)", name="menarche", curie=None,
                   model_uri=NMDC.menarche, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.menarche])

slots.sexual_act = Slot(uri="str(uriorcurie)", name="sexual_act", curie=None,
                   model_uri=NMDC.sexual_act, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.sexual_act])

slots.pregnancy = Slot(uri="str(uriorcurie)", name="pregnancy", curie=None,
                   model_uri=NMDC.pregnancy, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.pregnancy])

slots.douche = Slot(uri="str(uriorcurie)", name="douche", curie=None,
                   model_uri=NMDC.douche, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.douche])

slots.birth_control = Slot(uri="str(uriorcurie)", name="birth_control", curie=None,
                   model_uri=NMDC.birth_control, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.birth_control])

slots.menopause = Slot(uri="str(uriorcurie)", name="menopause", curie=None,
                   model_uri=NMDC.menopause, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.menopause])

slots.hrt = Slot(uri="str(uriorcurie)", name="hrt", curie=None,
                   model_uri=NMDC.hrt, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.hrt])

slots.hysterectomy = Slot(uri="str(uriorcurie)", name="hysterectomy", curie=None,
                   model_uri=NMDC.hysterectomy, domain=None, range=Optional[Union[dict, BooleanValue]], mappings = [MIXS.hysterectomy],
                   pattern=re.compile(r'[true|false]'))

slots.gynecologic_disord = Slot(uri="str(uriorcurie)", name="gynecologic_disord", curie=None,
                   model_uri=NMDC.gynecologic_disord, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.gynecologic_disord])

slots.urogenit_disord = Slot(uri="str(uriorcurie)", name="urogenit_disord", curie=None,
                   model_uri=NMDC.urogenit_disord, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.urogenit_disord])

slots.hcr = Slot(uri="str(uriorcurie)", name="hcr", curie=None,
                   model_uri=NMDC.hcr, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.hcr],
                   pattern=re.compile(r'[Oil Reservoir|Gas Reservoir|Oil Sand|Coalbed|Shale|Tight Oil Reservoir|Tight Gas Reservoir|other]'))

slots.hc_produced = Slot(uri="str(uriorcurie)", name="hc_produced", curie=None,
                   model_uri=NMDC.hc_produced, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.hc_produced],
                   pattern=re.compile(r'[Oil|Gas\-Condensate|Gas|Bitumen|Coalbed Methane|other]'))

slots.basin = Slot(uri="str(uriorcurie)", name="basin", curie=None,
                   model_uri=NMDC.basin, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.basin])

slots.field = Slot(uri="str(uriorcurie)", name="field", curie=None,
                   model_uri=NMDC.field, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.field])

slots.reservoir = Slot(uri="str(uriorcurie)", name="reservoir", curie=None,
                   model_uri=NMDC.reservoir, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.reservoir])

slots.hcr_temp = Slot(uri="str(uriorcurie)", name="hcr_temp", curie=None,
                   model_uri=NMDC.hcr_temp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.hcr_temp],
                   pattern=re.compile(r'\d+[.\d+] \- \d+[.\d+] \S+'))

slots.tvdss_of_hcr_temp = Slot(uri="str(uriorcurie)", name="tvdss_of_hcr_temp", curie=None,
                   model_uri=NMDC.tvdss_of_hcr_temp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tvdss_of_hcr_temp],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.hcr_pressure = Slot(uri="str(uriorcurie)", name="hcr_pressure", curie=None,
                   model_uri=NMDC.hcr_pressure, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.hcr_pressure],
                   pattern=re.compile(r'\d+[.\d+] \- \d+[.\d+] \S+'))

slots.tvdss_of_hcr_pressure = Slot(uri="str(uriorcurie)", name="tvdss_of_hcr_pressure", curie=None,
                   model_uri=NMDC.tvdss_of_hcr_pressure, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tvdss_of_hcr_pressure],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.permeability = Slot(uri="str(uriorcurie)", name="permeability", curie=None,
                   model_uri=NMDC.permeability, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.permeability])

slots.porosity = Slot(uri="str(uriorcurie)", name="porosity", curie=None,
                   model_uri=NMDC.porosity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.porosity],
                   pattern=re.compile(r'\d+[.\d+] \- \d+[.\d+] \S+'))

slots.lithology = Slot(uri="str(uriorcurie)", name="lithology", curie=None,
                   model_uri=NMDC.lithology, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.lithology],
                   pattern=re.compile(r'[Basement|Chalk|Chert|Coal|Conglomerate|Diatomite|Dolomite|Limestone|Sandstone|Shale|Siltstone|Volcanic|other]'))

slots.depos_env = Slot(uri="str(uriorcurie)", name="depos_env", curie=None,
                   model_uri=NMDC.depos_env, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.depos_env],
                   pattern=re.compile(r'[Continental \- Alluvial|Continental \- Aeolian|Continental \- Fluvial|Continental \- Lacustrine|Transitional \- Deltaic|Transitional \- Tidal|Transitional \- Lagoonal|Transitional \- Beach|Transitional \- Lake|Marine \- Shallow|Marine \- Deep|Marine \- Reef|Other \- Evaporite|Other \- Glacial|Other \- Volcanic|other]'))

slots.hcr_geol_age = Slot(uri="str(uriorcurie)", name="hcr_geol_age", curie=None,
                   model_uri=NMDC.hcr_geol_age, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.hcr_geol_age],
                   pattern=re.compile(r'[Archean|Cambrian|Carboniferous|Cenozoic|Cretaceous|Devonian|Jurassic|Mesozoic|Neogene|Ordovician|Paleogene|Paleozoic|Permian|Precambrian|Proterozoic|Silurian|Triassic|other]'))

slots.owc_tvdss = Slot(uri="str(uriorcurie)", name="owc_tvdss", curie=None,
                   model_uri=NMDC.owc_tvdss, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.owc_tvdss],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.hcr_fw_salinity = Slot(uri="str(uriorcurie)", name="hcr_fw_salinity", curie=None,
                   model_uri=NMDC.hcr_fw_salinity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.hcr_fw_salinity],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.sulfate_fw = Slot(uri="str(uriorcurie)", name="sulfate_fw", curie=None,
                   model_uri=NMDC.sulfate_fw, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.sulfate_fw],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.vfa_fw = Slot(uri="str(uriorcurie)", name="vfa_fw", curie=None,
                   model_uri=NMDC.vfa_fw, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.vfa_fw],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.sr_kerog_type = Slot(uri="str(uriorcurie)", name="sr_kerog_type", curie=None,
                   model_uri=NMDC.sr_kerog_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.sr_kerog_type],
                   pattern=re.compile(r'[Type I|Type II|Type III|Type IV|other]'))

slots.sr_lithology = Slot(uri="str(uriorcurie)", name="sr_lithology", curie=None,
                   model_uri=NMDC.sr_lithology, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.sr_lithology],
                   pattern=re.compile(r'[Clastic|Carbonate|Coal|Biosilicieous|other]'))

slots.sr_dep_env = Slot(uri="str(uriorcurie)", name="sr_dep_env", curie=None,
                   model_uri=NMDC.sr_dep_env, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.sr_dep_env],
                   pattern=re.compile(r'[Lacustine|Fluvioldeltaic|Fluviomarine|Marine|other]'))

slots.sr_geol_age = Slot(uri="str(uriorcurie)", name="sr_geol_age", curie=None,
                   model_uri=NMDC.sr_geol_age, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.sr_geol_age],
                   pattern=re.compile(r'[Archean|Cambrian|Carboniferous|Cenozoic|Cretaceous|Devonian|Jurassic|Mesozoic|Neogene|Ordovician|Paleogene|Paleozoic|Permian|Precambrian|Proterozoic|Silurian|Triassic|other]'))

slots.samp_well_name = Slot(uri="str(uriorcurie)", name="samp_well_name", curie=None,
                   model_uri=NMDC.samp_well_name, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_well_name])

slots.win = Slot(uri="str(uriorcurie)", name="win", curie=None,
                   model_uri=NMDC.win, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.win])

slots.samp_type = Slot(uri="str(uriorcurie)", name="samp_type", curie=None,
                   model_uri=NMDC.samp_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_type],
                   pattern=re.compile(r'[core|rock trimmings|drill cuttings|piping section|coupon|pigging debris|solid deposit|produced fluid|produced water|injected water|water from treatment plant|fresh water|sea water|drilling fluid|procedural blank|positive control|negative control|other]'))

slots.samp_subtype = Slot(uri="str(uriorcurie)", name="samp_subtype", curie=None,
                   model_uri=NMDC.samp_subtype, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_subtype],
                   pattern=re.compile(r'[oil phase|water phase|biofilm|not applicable|other]'))

slots.pressure = Slot(uri="str(uriorcurie)", name="pressure", curie=None,
                   model_uri=NMDC.pressure, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.pressure],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.samp_tvdss = Slot(uri="str(uriorcurie)", name="samp_tvdss", curie=None,
                   model_uri=NMDC.samp_tvdss, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.samp_tvdss],
                   pattern=re.compile(r'\d+[.\d+]\-\d+[.\d+] \S+'))

slots.samp_md = Slot(uri="str(uriorcurie)", name="samp_md", curie=None,
                   model_uri=NMDC.samp_md, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.samp_md],
                   pattern=re.compile(r'\d+[.\d+] \S+;[GL|DF|RT|KB|MSL|other]'))

slots.samp_transport_cond = Slot(uri="str(uriorcurie)", name="samp_transport_cond", curie=None,
                   model_uri=NMDC.samp_transport_cond, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.samp_transport_cond],
                   pattern=re.compile(r'\d+[.\d+] \S+;\d+[.\d+] \S+'))

slots.organism_count_qpcr_info = Slot(uri="str(uriorcurie)", name="organism_count_qpcr_info", curie=None,
                   model_uri=NMDC.organism_count_qpcr_info, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.organism_count_qpcr_info])

slots.ph = Slot(uri="str(uriorcurie)", name="ph", curie=None,
                   model_uri=NMDC.ph, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.ph],
                   pattern=re.compile(r'\d+[.\d+]'))

slots.alkalinity = Slot(uri="str(uriorcurie)", name="alkalinity", curie=None,
                   model_uri=NMDC.alkalinity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.alkalinity],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.alkalinity_method = Slot(uri="str(uriorcurie)", name="alkalinity_method", curie=None,
                   model_uri=NMDC.alkalinity_method, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.alkalinity_method])

slots.sulfate = Slot(uri="str(uriorcurie)", name="sulfate", curie=None,
                   model_uri=NMDC.sulfate, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.sulfate],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.sulfide = Slot(uri="str(uriorcurie)", name="sulfide", curie=None,
                   model_uri=NMDC.sulfide, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.sulfide],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.tot_sulfur = Slot(uri="str(uriorcurie)", name="tot_sulfur", curie=None,
                   model_uri=NMDC.tot_sulfur, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_sulfur],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.nitrate = Slot(uri="str(uriorcurie)", name="nitrate", curie=None,
                   model_uri=NMDC.nitrate, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.nitrate],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.nitrite = Slot(uri="str(uriorcurie)", name="nitrite", curie=None,
                   model_uri=NMDC.nitrite, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.nitrite],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.ammonium = Slot(uri="str(uriorcurie)", name="ammonium", curie=None,
                   model_uri=NMDC.ammonium, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.ammonium],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.tot_nitro = Slot(uri="str(uriorcurie)", name="tot_nitro", curie=None,
                   model_uri=NMDC.tot_nitro, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_nitro],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.diss_iron = Slot(uri="str(uriorcurie)", name="diss_iron", curie=None,
                   model_uri=NMDC.diss_iron, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diss_iron],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.sodium = Slot(uri="str(uriorcurie)", name="sodium", curie=None,
                   model_uri=NMDC.sodium, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.sodium],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.chloride = Slot(uri="str(uriorcurie)", name="chloride", curie=None,
                   model_uri=NMDC.chloride, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.chloride],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.potassium = Slot(uri="str(uriorcurie)", name="potassium", curie=None,
                   model_uri=NMDC.potassium, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.potassium],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.magnesium = Slot(uri="str(uriorcurie)", name="magnesium", curie=None,
                   model_uri=NMDC.magnesium, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.magnesium],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.calcium = Slot(uri="str(uriorcurie)", name="calcium", curie=None,
                   model_uri=NMDC.calcium, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.calcium],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.tot_iron = Slot(uri="str(uriorcurie)", name="tot_iron", curie=None,
                   model_uri=NMDC.tot_iron, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_iron],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.diss_org_carb = Slot(uri="str(uriorcurie)", name="diss_org_carb", curie=None,
                   model_uri=NMDC.diss_org_carb, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diss_org_carb],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.diss_inorg_carb = Slot(uri="str(uriorcurie)", name="diss_inorg_carb", curie=None,
                   model_uri=NMDC.diss_inorg_carb, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diss_inorg_carb],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.diss_inorg_phosp = Slot(uri="str(uriorcurie)", name="diss_inorg_phosp", curie=None,
                   model_uri=NMDC.diss_inorg_phosp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diss_inorg_phosp],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.tot_phosp = Slot(uri="str(uriorcurie)", name="tot_phosp", curie=None,
                   model_uri=NMDC.tot_phosp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_phosp],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.suspend_solids = Slot(uri="str(uriorcurie)", name="suspend_solids", curie=None,
                   model_uri=NMDC.suspend_solids, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.suspend_solids])

slots.density = Slot(uri="str(uriorcurie)", name="density", curie=None,
                   model_uri=NMDC.density, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.density],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.diss_carb_dioxide = Slot(uri="str(uriorcurie)", name="diss_carb_dioxide", curie=None,
                   model_uri=NMDC.diss_carb_dioxide, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diss_carb_dioxide],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.diss_oxygen_fluid = Slot(uri="str(uriorcurie)", name="diss_oxygen_fluid", curie=None,
                   model_uri=NMDC.diss_oxygen_fluid, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diss_oxygen_fluid],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.vfa = Slot(uri="str(uriorcurie)", name="vfa", curie=None,
                   model_uri=NMDC.vfa, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.vfa],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.benzene = Slot(uri="str(uriorcurie)", name="benzene", curie=None,
                   model_uri=NMDC.benzene, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.benzene],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.toluene = Slot(uri="str(uriorcurie)", name="toluene", curie=None,
                   model_uri=NMDC.toluene, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.toluene],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.ethylbenzene = Slot(uri="str(uriorcurie)", name="ethylbenzene", curie=None,
                   model_uri=NMDC.ethylbenzene, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.ethylbenzene],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.xylene = Slot(uri="str(uriorcurie)", name="xylene", curie=None,
                   model_uri=NMDC.xylene, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.xylene],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.api = Slot(uri="str(uriorcurie)", name="api", curie=None,
                   model_uri=NMDC.api, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.api],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.tan = Slot(uri="str(uriorcurie)", name="tan", curie=None,
                   model_uri=NMDC.tan, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tan],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.viscosity = Slot(uri="str(uriorcurie)", name="viscosity", curie=None,
                   model_uri=NMDC.viscosity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.viscosity],
                   pattern=re.compile(r'\d+[.\d+] \S+;\d+[.\d+] \S+'))

slots.pour_point = Slot(uri="str(uriorcurie)", name="pour_point", curie=None,
                   model_uri=NMDC.pour_point, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.pour_point],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.saturates_pc = Slot(uri="str(uriorcurie)", name="saturates_pc", curie=None,
                   model_uri=NMDC.saturates_pc, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.saturates_pc])

slots.aromatics_pc = Slot(uri="str(uriorcurie)", name="aromatics_pc", curie=None,
                   model_uri=NMDC.aromatics_pc, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.aromatics_pc])

slots.resins_pc = Slot(uri="str(uriorcurie)", name="resins_pc", curie=None,
                   model_uri=NMDC.resins_pc, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.resins_pc])

slots.asphaltenes_pc = Slot(uri="str(uriorcurie)", name="asphaltenes_pc", curie=None,
                   model_uri=NMDC.asphaltenes_pc, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.asphaltenes_pc])

slots.additional_info = Slot(uri="str(uriorcurie)", name="additional_info", curie=None,
                   model_uri=NMDC.additional_info, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.additional_info])

slots.prod_start_date = Slot(uri="str(uriorcurie)", name="prod_start_date", curie=None,
                   model_uri=NMDC.prod_start_date, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.prod_start_date])

slots.prod_rate = Slot(uri="str(uriorcurie)", name="prod_rate", curie=None,
                   model_uri=NMDC.prod_rate, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.prod_rate],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.water_production_rate = Slot(uri="str(uriorcurie)", name="water_production_rate", curie=None,
                   model_uri=NMDC.water_production_rate, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.water_production_rate],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.water_cut = Slot(uri="str(uriorcurie)", name="water_cut", curie=None,
                   model_uri=NMDC.water_cut, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.water_cut],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.iwf = Slot(uri="str(uriorcurie)", name="iwf", curie=None,
                   model_uri=NMDC.iwf, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.iwf],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.add_recov_method = Slot(uri="str(uriorcurie)", name="add_recov_method", curie=None,
                   model_uri=NMDC.add_recov_method, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.add_recov_method])

slots.iw_bt_date_well = Slot(uri="str(uriorcurie)", name="iw_bt_date_well", curie=None,
                   model_uri=NMDC.iw_bt_date_well, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.iw_bt_date_well])

slots.biocide = Slot(uri="str(uriorcurie)", name="biocide", curie=None,
                   model_uri=NMDC.biocide, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.biocide])

slots.biocide_admin_method = Slot(uri="str(uriorcurie)", name="biocide_admin_method", curie=None,
                   model_uri=NMDC.biocide_admin_method, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.biocide_admin_method])

slots.chem_treatment = Slot(uri="str(uriorcurie)", name="chem_treatment", curie=None,
                   model_uri=NMDC.chem_treatment, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.chem_treatment])

slots.chem_treatment_method = Slot(uri="str(uriorcurie)", name="chem_treatment_method", curie=None,
                   model_uri=NMDC.chem_treatment_method, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.chem_treatment_method])

slots.samp_loc_corr_rate = Slot(uri="str(uriorcurie)", name="samp_loc_corr_rate", curie=None,
                   model_uri=NMDC.samp_loc_corr_rate, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.samp_loc_corr_rate],
                   pattern=re.compile(r'\d+[.\d+] \- \d+[.\d+] \S+'))

slots.samp_collection_point = Slot(uri="str(uriorcurie)", name="samp_collection_point", curie=None,
                   model_uri=NMDC.samp_collection_point, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_collection_point],
                   pattern=re.compile(r'[well|test well|drilling rig|wellhead|separator|storage tank|other]'))

slots.samp_preserv = Slot(uri="str(uriorcurie)", name="samp_preserv", curie=None,
                   model_uri=NMDC.samp_preserv, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.samp_preserv])

slots.alkyl_diethers = Slot(uri="str(uriorcurie)", name="alkyl_diethers", curie=None,
                   model_uri=NMDC.alkyl_diethers, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.alkyl_diethers],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.aminopept_act = Slot(uri="str(uriorcurie)", name="aminopept_act", curie=None,
                   model_uri=NMDC.aminopept_act, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.aminopept_act],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.bacteria_carb_prod = Slot(uri="str(uriorcurie)", name="bacteria_carb_prod", curie=None,
                   model_uri=NMDC.bacteria_carb_prod, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.bacteria_carb_prod],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.biomass = Slot(uri="str(uriorcurie)", name="biomass", curie=None,
                   model_uri=NMDC.biomass, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.biomass])

slots.bishomohopanol = Slot(uri="str(uriorcurie)", name="bishomohopanol", curie=None,
                   model_uri=NMDC.bishomohopanol, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.bishomohopanol],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.bromide = Slot(uri="str(uriorcurie)", name="bromide", curie=None,
                   model_uri=NMDC.bromide, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.bromide],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.carb_nitro_ratio = Slot(uri="str(uriorcurie)", name="carb_nitro_ratio", curie=None,
                   model_uri=NMDC.carb_nitro_ratio, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.carb_nitro_ratio],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.chlorophyll = Slot(uri="str(uriorcurie)", name="chlorophyll", curie=None,
                   model_uri=NMDC.chlorophyll, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.chlorophyll],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.diether_lipids = Slot(uri="str(uriorcurie)", name="diether_lipids", curie=None,
                   model_uri=NMDC.diether_lipids, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diether_lipids])

slots.diss_hydrogen = Slot(uri="str(uriorcurie)", name="diss_hydrogen", curie=None,
                   model_uri=NMDC.diss_hydrogen, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diss_hydrogen],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.diss_org_nitro = Slot(uri="str(uriorcurie)", name="diss_org_nitro", curie=None,
                   model_uri=NMDC.diss_org_nitro, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diss_org_nitro],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.diss_oxygen = Slot(uri="str(uriorcurie)", name="diss_oxygen", curie=None,
                   model_uri=NMDC.diss_oxygen, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diss_oxygen],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.glucosidase_act = Slot(uri="str(uriorcurie)", name="glucosidase_act", curie=None,
                   model_uri=NMDC.glucosidase_act, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.glucosidase_act],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.mean_frict_vel = Slot(uri="str(uriorcurie)", name="mean_frict_vel", curie=None,
                   model_uri=NMDC.mean_frict_vel, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.mean_frict_vel],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.mean_peak_frict_vel = Slot(uri="str(uriorcurie)", name="mean_peak_frict_vel", curie=None,
                   model_uri=NMDC.mean_peak_frict_vel, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.mean_peak_frict_vel],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.n_alkanes = Slot(uri="str(uriorcurie)", name="n_alkanes", curie=None,
                   model_uri=NMDC.n_alkanes, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.n_alkanes])

slots.nitro = Slot(uri="str(uriorcurie)", name="nitro", curie=None,
                   model_uri=NMDC.nitro, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.nitro],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.org_carb = Slot(uri="str(uriorcurie)", name="org_carb", curie=None,
                   model_uri=NMDC.org_carb, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.org_carb],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.org_matter = Slot(uri="str(uriorcurie)", name="org_matter", curie=None,
                   model_uri=NMDC.org_matter, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.org_matter],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.org_nitro = Slot(uri="str(uriorcurie)", name="org_nitro", curie=None,
                   model_uri=NMDC.org_nitro, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.org_nitro],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.part_org_carb = Slot(uri="str(uriorcurie)", name="part_org_carb", curie=None,
                   model_uri=NMDC.part_org_carb, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.part_org_carb],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.petroleum_hydrocarb = Slot(uri="str(uriorcurie)", name="petroleum_hydrocarb", curie=None,
                   model_uri=NMDC.petroleum_hydrocarb, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.petroleum_hydrocarb],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.phaeopigments = Slot(uri="str(uriorcurie)", name="phaeopigments", curie=None,
                   model_uri=NMDC.phaeopigments, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.phaeopigments])

slots.phosphate = Slot(uri="str(uriorcurie)", name="phosphate", curie=None,
                   model_uri=NMDC.phosphate, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.phosphate],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.phosplipid_fatt_acid = Slot(uri="str(uriorcurie)", name="phosplipid_fatt_acid", curie=None,
                   model_uri=NMDC.phosplipid_fatt_acid, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.phosplipid_fatt_acid])

slots.redox_potential = Slot(uri="str(uriorcurie)", name="redox_potential", curie=None,
                   model_uri=NMDC.redox_potential, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.redox_potential],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.salinity = Slot(uri="str(uriorcurie)", name="salinity", curie=None,
                   model_uri=NMDC.salinity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.salinity],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.silicate = Slot(uri="str(uriorcurie)", name="silicate", curie=None,
                   model_uri=NMDC.silicate, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.silicate],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.tot_carb = Slot(uri="str(uriorcurie)", name="tot_carb", curie=None,
                   model_uri=NMDC.tot_carb, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_carb],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.tot_nitro_content = Slot(uri="str(uriorcurie)", name="tot_nitro_content", curie=None,
                   model_uri=NMDC.tot_nitro_content, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_nitro_content],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.tot_org_carb = Slot(uri="str(uriorcurie)", name="tot_org_carb", curie=None,
                   model_uri=NMDC.tot_org_carb, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_org_carb],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.turbidity = Slot(uri="str(uriorcurie)", name="turbidity", curie=None,
                   model_uri=NMDC.turbidity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.turbidity],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.water_content = Slot(uri="str(uriorcurie)", name="water_content", curie=None,
                   model_uri=NMDC.water_content, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.water_content],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.water_current = Slot(uri="str(uriorcurie)", name="water_current", curie=None,
                   model_uri=NMDC.water_current, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.water_current],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.air_temp_regm = Slot(uri="str(uriorcurie)", name="air_temp_regm", curie=None,
                   model_uri=NMDC.air_temp_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.air_temp_regm])

slots.antibiotic_regm = Slot(uri="str(uriorcurie)", name="antibiotic_regm", curie=None,
                   model_uri=NMDC.antibiotic_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.antibiotic_regm])

slots.biotic_regm = Slot(uri="str(uriorcurie)", name="biotic_regm", curie=None,
                   model_uri=NMDC.biotic_regm, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.biotic_regm])

slots.chem_mutagen = Slot(uri="str(uriorcurie)", name="chem_mutagen", curie=None,
                   model_uri=NMDC.chem_mutagen, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.chem_mutagen])

slots.climate_environment = Slot(uri="str(uriorcurie)", name="climate_environment", curie=None,
                   model_uri=NMDC.climate_environment, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.climate_environment])

slots.cult_root_med = Slot(uri="str(uriorcurie)", name="cult_root_med", curie=None,
                   model_uri=NMDC.cult_root_med, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.cult_root_med])

slots.fertilizer_regm = Slot(uri="str(uriorcurie)", name="fertilizer_regm", curie=None,
                   model_uri=NMDC.fertilizer_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.fertilizer_regm])

slots.fungicide_regm = Slot(uri="str(uriorcurie)", name="fungicide_regm", curie=None,
                   model_uri=NMDC.fungicide_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.fungicide_regm])

slots.gaseous_environment = Slot(uri="str(uriorcurie)", name="gaseous_environment", curie=None,
                   model_uri=NMDC.gaseous_environment, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.gaseous_environment])

slots.gravity = Slot(uri="str(uriorcurie)", name="gravity", curie=None,
                   model_uri=NMDC.gravity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.gravity])

slots.growth_facil = Slot(uri="str(uriorcurie)", name="growth_facil", curie=None,
                   model_uri=NMDC.growth_facil, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.growth_facil])

slots.growth_habit = Slot(uri="str(uriorcurie)", name="growth_habit", curie=None,
                   model_uri=NMDC.growth_habit, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.growth_habit],
                   pattern=re.compile(r'[erect|semi\-erect|spreading|prostrate] '))

slots.growth_hormone_regm = Slot(uri="str(uriorcurie)", name="growth_hormone_regm", curie=None,
                   model_uri=NMDC.growth_hormone_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.growth_hormone_regm])

slots.herbicide_regm = Slot(uri="str(uriorcurie)", name="herbicide_regm", curie=None,
                   model_uri=NMDC.herbicide_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.herbicide_regm])

slots.host_wet_mass = Slot(uri="str(uriorcurie)", name="host_wet_mass", curie=None,
                   model_uri=NMDC.host_wet_mass, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_wet_mass],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.humidity_regm = Slot(uri="str(uriorcurie)", name="humidity_regm", curie=None,
                   model_uri=NMDC.humidity_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.humidity_regm])

slots.light_regm = Slot(uri="str(uriorcurie)", name="light_regm", curie=None,
                   model_uri=NMDC.light_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.light_regm])

slots.mechanical_damage = Slot(uri="str(uriorcurie)", name="mechanical_damage", curie=None,
                   model_uri=NMDC.mechanical_damage, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.mechanical_damage])

slots.mineral_nutr_regm = Slot(uri="str(uriorcurie)", name="mineral_nutr_regm", curie=None,
                   model_uri=NMDC.mineral_nutr_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.mineral_nutr_regm])

slots.non_mineral_nutr_regm = Slot(uri="str(uriorcurie)", name="non_mineral_nutr_regm", curie=None,
                   model_uri=NMDC.non_mineral_nutr_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.non_mineral_nutr_regm])

slots.ph_regm = Slot(uri="str(uriorcurie)", name="ph_regm", curie=None,
                   model_uri=NMDC.ph_regm, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ph_regm])

slots.pesticide_regm = Slot(uri="str(uriorcurie)", name="pesticide_regm", curie=None,
                   model_uri=NMDC.pesticide_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.pesticide_regm])

slots.plant_growth_med = Slot(uri="str(uriorcurie)", name="plant_growth_med", curie=None,
                   model_uri=NMDC.plant_growth_med, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.plant_growth_med],
                   pattern=re.compile(r'.* \S+:\S+'))

slots.plant_product = Slot(uri="str(uriorcurie)", name="plant_product", curie=None,
                   model_uri=NMDC.plant_product, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.plant_product])

slots.plant_sex = Slot(uri="str(uriorcurie)", name="plant_sex", curie=None,
                   model_uri=NMDC.plant_sex, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.plant_sex],
                   pattern=re.compile(r'[Androdioecious|Androecious|Androgynous|Androgynomonoecious|Andromonoecious|Bisexual|Dichogamous|Diclinous|Dioecious|Gynodioecious|Gynoecious|Gynomonoecious|Hermaphroditic|Imperfect|Monoclinous|Monoecious|Perfect|Polygamodioecious|Polygamomonoecious|Polygamous|Protandrous|Protogynous|Subandroecious|Subdioecious|Subgynoecious|Synoecious|Trimonoecious|Trioecious|Unisexual]'))

slots.plant_struc = Slot(uri="str(uriorcurie)", name="plant_struc", curie=None,
                   model_uri=NMDC.plant_struc, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.plant_struc],
                   pattern=re.compile(r'.* \S+:\S+'))

slots.radiation_regm = Slot(uri="str(uriorcurie)", name="radiation_regm", curie=None,
                   model_uri=NMDC.radiation_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.radiation_regm])

slots.rainfall_regm = Slot(uri="str(uriorcurie)", name="rainfall_regm", curie=None,
                   model_uri=NMDC.rainfall_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.rainfall_regm])

slots.root_cond = Slot(uri="str(uriorcurie)", name="root_cond", curie=None,
                   model_uri=NMDC.root_cond, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.root_cond])

slots.root_med_carbon = Slot(uri="str(uriorcurie)", name="root_med_carbon", curie=None,
                   model_uri=NMDC.root_med_carbon, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.root_med_carbon])

slots.root_med_macronutr = Slot(uri="str(uriorcurie)", name="root_med_macronutr", curie=None,
                   model_uri=NMDC.root_med_macronutr, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.root_med_macronutr])

slots.root_med_micronutr = Slot(uri="str(uriorcurie)", name="root_med_micronutr", curie=None,
                   model_uri=NMDC.root_med_micronutr, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.root_med_micronutr])

slots.root_med_suppl = Slot(uri="str(uriorcurie)", name="root_med_suppl", curie=None,
                   model_uri=NMDC.root_med_suppl, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.root_med_suppl])

slots.root_med_ph = Slot(uri="str(uriorcurie)", name="root_med_ph", curie=None,
                   model_uri=NMDC.root_med_ph, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.root_med_ph],
                   pattern=re.compile(r'\d+[.\d+]'))

slots.root_med_regl = Slot(uri="str(uriorcurie)", name="root_med_regl", curie=None,
                   model_uri=NMDC.root_med_regl, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.root_med_regl])

slots.root_med_solid = Slot(uri="str(uriorcurie)", name="root_med_solid", curie=None,
                   model_uri=NMDC.root_med_solid, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.root_med_solid])

slots.salt_regm = Slot(uri="str(uriorcurie)", name="salt_regm", curie=None,
                   model_uri=NMDC.salt_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.salt_regm])

slots.season_environment = Slot(uri="str(uriorcurie)", name="season_environment", curie=None,
                   model_uri=NMDC.season_environment, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.season_environment])

slots.standing_water_regm = Slot(uri="str(uriorcurie)", name="standing_water_regm", curie=None,
                   model_uri=NMDC.standing_water_regm, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.standing_water_regm])

slots.tiss_cult_growth_med = Slot(uri="str(uriorcurie)", name="tiss_cult_growth_med", curie=None,
                   model_uri=NMDC.tiss_cult_growth_med, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.tiss_cult_growth_med])

slots.water_temp_regm = Slot(uri="str(uriorcurie)", name="water_temp_regm", curie=None,
                   model_uri=NMDC.water_temp_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.water_temp_regm])

slots.watering_regm = Slot(uri="str(uriorcurie)", name="watering_regm", curie=None,
                   model_uri=NMDC.watering_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.watering_regm])

slots.particle_class = Slot(uri="str(uriorcurie)", name="particle_class", curie=None,
                   model_uri=NMDC.particle_class, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.particle_class])

slots.sediment_type = Slot(uri="str(uriorcurie)", name="sediment_type", curie=None,
                   model_uri=NMDC.sediment_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.sediment_type],
                   pattern=re.compile(r'[biogenous|cosmogenous|hydrogenous|lithogenous]'))

slots.tidal_stage = Slot(uri="str(uriorcurie)", name="tidal_stage", curie=None,
                   model_uri=NMDC.tidal_stage, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.tidal_stage],
                   pattern=re.compile(r'[low tide|ebb tide|flood tide|high tide]'))

slots.tot_depth_water_col = Slot(uri="str(uriorcurie)", name="tot_depth_water_col", curie=None,
                   model_uri=NMDC.tot_depth_water_col, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_depth_water_col],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.cur_land_use = Slot(uri="str(uriorcurie)", name="cur_land_use", curie=None,
                   model_uri=NMDC.cur_land_use, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.cur_land_use],
                   pattern=re.compile(r'[cities|farmstead|industrial areas|roads\/railroads|rock|sand|gravel|mudflats|salt flats|badlands|permanent snow or ice|saline seeps|mines\/quarries|oil waste areas|small grains|row crops|vegetable crops|horticultural plants (e.g. tulips)|marshlands (grass,sedges,rushes)|tundra (mosses,lichens)|rangeland|pastureland (grasslands used for livestock grazing)|hayland|meadows (grasses,alfalfa,fescue,bromegrass,timothy)|shrub land (e.g. mesquite,sage\-brush,creosote bush,shrub oak,eucalyptus)|successional shrub land (tree saplings,hazels,sumacs,chokecherry,shrub dogwoods,blackberries)|shrub crops (blueberries,nursery ornamentals,filberts)|vine crops (grapes)|conifers (e.g. pine,spruce,fir,cypress)|hardwoods (e.g. oak,hickory,elm,aspen)|intermixed hardwood and conifers|tropical (e.g. mangrove,palms)|rainforest (evergreen forest receiving >406 cm annual rainfall)|swamp (permanent or semi\-permanent water body dominated by woody plants)|crop trees (nuts,fruit,christmas trees,nursery trees)]'))

slots.cur_vegetation = Slot(uri="str(uriorcurie)", name="cur_vegetation", curie=None,
                   model_uri=NMDC.cur_vegetation, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.cur_vegetation])

slots.cur_vegetation_meth = Slot(uri="str(uriorcurie)", name="cur_vegetation_meth", curie=None,
                   model_uri=NMDC.cur_vegetation_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.cur_vegetation_meth])

slots.previous_land_use = Slot(uri="str(uriorcurie)", name="previous_land_use", curie=None,
                   model_uri=NMDC.previous_land_use, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.previous_land_use])

slots.previous_land_use_meth = Slot(uri="str(uriorcurie)", name="previous_land_use_meth", curie=None,
                   model_uri=NMDC.previous_land_use_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.previous_land_use_meth])

slots.crop_rotation = Slot(uri="str(uriorcurie)", name="crop_rotation", curie=None,
                   model_uri=NMDC.crop_rotation, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.crop_rotation])

slots.agrochem_addition = Slot(uri="str(uriorcurie)", name="agrochem_addition", curie=None,
                   model_uri=NMDC.agrochem_addition, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.agrochem_addition])

slots.tillage = Slot(uri="str(uriorcurie)", name="tillage", curie=None,
                   model_uri=NMDC.tillage, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.tillage],
                   pattern=re.compile(r'[drill|cutting disc|ridge till|strip tillage|zonal tillage|chisel|tined|mouldboard|disc plough]'))

slots.fire = Slot(uri="str(uriorcurie)", name="fire", curie=None,
                   model_uri=NMDC.fire, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.fire])

slots.flooding = Slot(uri="str(uriorcurie)", name="flooding", curie=None,
                   model_uri=NMDC.flooding, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.flooding])

slots.extreme_event = Slot(uri="str(uriorcurie)", name="extreme_event", curie=None,
                   model_uri=NMDC.extreme_event, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.extreme_event])

slots.horizon = Slot(uri="str(uriorcurie)", name="horizon", curie=None,
                   model_uri=NMDC.horizon, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.horizon],
                   pattern=re.compile(r'[O horizon|A horizon|E horizon|B horizon|C horizon|R layer|Permafrost]'))

slots.horizon_meth = Slot(uri="str(uriorcurie)", name="horizon_meth", curie=None,
                   model_uri=NMDC.horizon_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.horizon_meth])

slots.sieving = Slot(uri="str(uriorcurie)", name="sieving", curie=None,
                   model_uri=NMDC.sieving, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.sieving])

slots.water_content_soil_meth = Slot(uri="str(uriorcurie)", name="water_content_soil_meth", curie=None,
                   model_uri=NMDC.water_content_soil_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.water_content_soil_meth])

slots.pool_dna_extracts = Slot(uri="str(uriorcurie)", name="pool_dna_extracts", curie=None,
                   model_uri=NMDC.pool_dna_extracts, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.pool_dna_extracts])

slots.store_cond = Slot(uri="str(uriorcurie)", name="store_cond", curie=None,
                   model_uri=NMDC.store_cond, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.store_cond])

slots.link_climate_info = Slot(uri="str(uriorcurie)", name="link_climate_info", curie=None,
                   model_uri=NMDC.link_climate_info, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.link_climate_info])

slots.annual_temp = Slot(uri="str(uriorcurie)", name="annual_temp", curie=None,
                   model_uri=NMDC.annual_temp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.annual_temp],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.season_temp = Slot(uri="str(uriorcurie)", name="season_temp", curie=None,
                   model_uri=NMDC.season_temp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.season_temp],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.annual_precpt = Slot(uri="str(uriorcurie)", name="annual_precpt", curie=None,
                   model_uri=NMDC.annual_precpt, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.annual_precpt],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.season_precpt = Slot(uri="str(uriorcurie)", name="season_precpt", curie=None,
                   model_uri=NMDC.season_precpt, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.season_precpt],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.link_class_info = Slot(uri="str(uriorcurie)", name="link_class_info", curie=None,
                   model_uri=NMDC.link_class_info, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.link_class_info])

slots.fao_class = Slot(uri="str(uriorcurie)", name="fao_class", curie=None,
                   model_uri=NMDC.fao_class, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.fao_class],
                   pattern=re.compile(r'[Acrisols|Andosols|Arenosols|Cambisols|Chernozems|Ferralsols|Fluvisols|Gleysols|Greyzems|Gypsisols|Histosols|Kastanozems|Lithosols|Luvisols|Nitosols|Phaeozems|Planosols|Podzols|Podzoluvisols|Rankers|Regosols|Rendzinas|Solonchaks|Solonetz|Vertisols|Yermosols]'))

slots.local_class = Slot(uri="str(uriorcurie)", name="local_class", curie=None,
                   model_uri=NMDC.local_class, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.local_class])

slots.local_class_meth = Slot(uri="str(uriorcurie)", name="local_class_meth", curie=None,
                   model_uri=NMDC.local_class_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.local_class_meth])

slots.soil_type = Slot(uri="str(uriorcurie)", name="soil_type", curie=None,
                   model_uri=NMDC.soil_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.soil_type])

slots.soil_type_meth = Slot(uri="str(uriorcurie)", name="soil_type_meth", curie=None,
                   model_uri=NMDC.soil_type_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.soil_type_meth])

slots.slope_gradient = Slot(uri="str(uriorcurie)", name="slope_gradient", curie=None,
                   model_uri=NMDC.slope_gradient, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.slope_gradient],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.slope_aspect = Slot(uri="str(uriorcurie)", name="slope_aspect", curie=None,
                   model_uri=NMDC.slope_aspect, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.slope_aspect],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.profile_position = Slot(uri="str(uriorcurie)", name="profile_position", curie=None,
                   model_uri=NMDC.profile_position, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.profile_position],
                   pattern=re.compile(r'[summit|shoulder|backslope|footslope|toeslope]'))

slots.drainage_class = Slot(uri="str(uriorcurie)", name="drainage_class", curie=None,
                   model_uri=NMDC.drainage_class, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.drainage_class],
                   pattern=re.compile(r'[very poorly|poorly|somewhat poorly|moderately well|well|excessively drained]'))

slots.texture = Slot(uri="str(uriorcurie)", name="texture", curie=None,
                   model_uri=NMDC.texture, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.texture],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.texture_meth = Slot(uri="str(uriorcurie)", name="texture_meth", curie=None,
                   model_uri=NMDC.texture_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.texture_meth])

slots.ph_meth = Slot(uri="str(uriorcurie)", name="ph_meth", curie=None,
                   model_uri=NMDC.ph_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ph_meth])

slots.tot_org_c_meth = Slot(uri="str(uriorcurie)", name="tot_org_c_meth", curie=None,
                   model_uri=NMDC.tot_org_c_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.tot_org_c_meth])

slots.tot_nitro_content_meth = Slot(uri="str(uriorcurie)", name="tot_nitro_content_meth", curie=None,
                   model_uri=NMDC.tot_nitro_content_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.tot_nitro_content_meth])

slots.microbial_biomass = Slot(uri="str(uriorcurie)", name="microbial_biomass", curie=None,
                   model_uri=NMDC.microbial_biomass, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.microbial_biomass],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.microbial_biomass_meth = Slot(uri="str(uriorcurie)", name="microbial_biomass_meth", curie=None,
                   model_uri=NMDC.microbial_biomass_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.microbial_biomass_meth])

slots.link_addit_analys = Slot(uri="str(uriorcurie)", name="link_addit_analys", curie=None,
                   model_uri=NMDC.link_addit_analys, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.link_addit_analys])

slots.extreme_salinity = Slot(uri="str(uriorcurie)", name="extreme_salinity", curie=None,
                   model_uri=NMDC.extreme_salinity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.extreme_salinity],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.salinity_meth = Slot(uri="str(uriorcurie)", name="salinity_meth", curie=None,
                   model_uri=NMDC.salinity_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.salinity_meth])

slots.heavy_metals = Slot(uri="str(uriorcurie)", name="heavy_metals", curie=None,
                   model_uri=NMDC.heavy_metals, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.heavy_metals])

slots.heavy_metals_meth = Slot(uri="str(uriorcurie)", name="heavy_metals_meth", curie=None,
                   model_uri=NMDC.heavy_metals_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.heavy_metals_meth])

slots.al_sat = Slot(uri="str(uriorcurie)", name="al_sat", curie=None,
                   model_uri=NMDC.al_sat, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.al_sat],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.al_sat_meth = Slot(uri="str(uriorcurie)", name="al_sat_meth", curie=None,
                   model_uri=NMDC.al_sat_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.al_sat_meth])

slots.biochem_oxygen_dem = Slot(uri="str(uriorcurie)", name="biochem_oxygen_dem", curie=None,
                   model_uri=NMDC.biochem_oxygen_dem, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.biochem_oxygen_dem],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.chem_oxygen_dem = Slot(uri="str(uriorcurie)", name="chem_oxygen_dem", curie=None,
                   model_uri=NMDC.chem_oxygen_dem, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.chem_oxygen_dem],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.efficiency_percent = Slot(uri="str(uriorcurie)", name="efficiency_percent", curie=None,
                   model_uri=NMDC.efficiency_percent, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.efficiency_percent],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.emulsions = Slot(uri="str(uriorcurie)", name="emulsions", curie=None,
                   model_uri=NMDC.emulsions, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.emulsions])

slots.gaseous_substances = Slot(uri="str(uriorcurie)", name="gaseous_substances", curie=None,
                   model_uri=NMDC.gaseous_substances, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.gaseous_substances])

slots.indust_eff_percent = Slot(uri="str(uriorcurie)", name="indust_eff_percent", curie=None,
                   model_uri=NMDC.indust_eff_percent, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.indust_eff_percent],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.inorg_particles = Slot(uri="str(uriorcurie)", name="inorg_particles", curie=None,
                   model_uri=NMDC.inorg_particles, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.inorg_particles])

slots.org_particles = Slot(uri="str(uriorcurie)", name="org_particles", curie=None,
                   model_uri=NMDC.org_particles, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.org_particles])

slots.pre_treatment = Slot(uri="str(uriorcurie)", name="pre_treatment", curie=None,
                   model_uri=NMDC.pre_treatment, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.pre_treatment])

slots.primary_treatment = Slot(uri="str(uriorcurie)", name="primary_treatment", curie=None,
                   model_uri=NMDC.primary_treatment, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.primary_treatment])

slots.reactor_type = Slot(uri="str(uriorcurie)", name="reactor_type", curie=None,
                   model_uri=NMDC.reactor_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.reactor_type])

slots.secondary_treatment = Slot(uri="str(uriorcurie)", name="secondary_treatment", curie=None,
                   model_uri=NMDC.secondary_treatment, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.secondary_treatment])

slots.sewage_type = Slot(uri="str(uriorcurie)", name="sewage_type", curie=None,
                   model_uri=NMDC.sewage_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.sewage_type])

slots.sludge_retent_time = Slot(uri="str(uriorcurie)", name="sludge_retent_time", curie=None,
                   model_uri=NMDC.sludge_retent_time, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.sludge_retent_time],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.soluble_inorg_mat = Slot(uri="str(uriorcurie)", name="soluble_inorg_mat", curie=None,
                   model_uri=NMDC.soluble_inorg_mat, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.soluble_inorg_mat])

slots.soluble_org_mat = Slot(uri="str(uriorcurie)", name="soluble_org_mat", curie=None,
                   model_uri=NMDC.soluble_org_mat, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.soluble_org_mat])

slots.tertiary_treatment = Slot(uri="str(uriorcurie)", name="tertiary_treatment", curie=None,
                   model_uri=NMDC.tertiary_treatment, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.tertiary_treatment])

slots.tot_phosphate = Slot(uri="str(uriorcurie)", name="tot_phosphate", curie=None,
                   model_uri=NMDC.tot_phosphate, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_phosphate],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.wastewater_type = Slot(uri="str(uriorcurie)", name="wastewater_type", curie=None,
                   model_uri=NMDC.wastewater_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.wastewater_type])

slots.atmospheric_data = Slot(uri="str(uriorcurie)", name="atmospheric_data", curie=None,
                   model_uri=NMDC.atmospheric_data, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.atmospheric_data])

slots.bac_prod = Slot(uri="str(uriorcurie)", name="bac_prod", curie=None,
                   model_uri=NMDC.bac_prod, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.bac_prod],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.bac_resp = Slot(uri="str(uriorcurie)", name="bac_resp", curie=None,
                   model_uri=NMDC.bac_resp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.bac_resp],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.conduc = Slot(uri="str(uriorcurie)", name="conduc", curie=None,
                   model_uri=NMDC.conduc, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.conduc],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.diss_inorg_nitro = Slot(uri="str(uriorcurie)", name="diss_inorg_nitro", curie=None,
                   model_uri=NMDC.diss_inorg_nitro, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diss_inorg_nitro],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.down_par = Slot(uri="str(uriorcurie)", name="down_par", curie=None,
                   model_uri=NMDC.down_par, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.down_par],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.fluor = Slot(uri="str(uriorcurie)", name="fluor", curie=None,
                   model_uri=NMDC.fluor, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.fluor],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.light_intensity = Slot(uri="str(uriorcurie)", name="light_intensity", curie=None,
                   model_uri=NMDC.light_intensity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.light_intensity],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.part_org_nitro = Slot(uri="str(uriorcurie)", name="part_org_nitro", curie=None,
                   model_uri=NMDC.part_org_nitro, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.part_org_nitro],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.photon_flux = Slot(uri="str(uriorcurie)", name="photon_flux", curie=None,
                   model_uri=NMDC.photon_flux, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.photon_flux],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.primary_prod = Slot(uri="str(uriorcurie)", name="primary_prod", curie=None,
                   model_uri=NMDC.primary_prod, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.primary_prod],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.size_frac_low = Slot(uri="str(uriorcurie)", name="size_frac_low", curie=None,
                   model_uri=NMDC.size_frac_low, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.size_frac_low],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.size_frac_up = Slot(uri="str(uriorcurie)", name="size_frac_up", curie=None,
                   model_uri=NMDC.size_frac_up, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.size_frac_up],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.soluble_react_phosp = Slot(uri="str(uriorcurie)", name="soluble_react_phosp", curie=None,
                   model_uri=NMDC.soluble_react_phosp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.soluble_react_phosp],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.suspend_part_matter = Slot(uri="str(uriorcurie)", name="suspend_part_matter", curie=None,
                   model_uri=NMDC.suspend_part_matter, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.suspend_part_matter],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.tot_diss_nitro = Slot(uri="str(uriorcurie)", name="tot_diss_nitro", curie=None,
                   model_uri=NMDC.tot_diss_nitro, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_diss_nitro],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.tot_inorg_nitro = Slot(uri="str(uriorcurie)", name="tot_inorg_nitro", curie=None,
                   model_uri=NMDC.tot_inorg_nitro, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_inorg_nitro],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.tot_part_carb = Slot(uri="str(uriorcurie)", name="tot_part_carb", curie=None,
                   model_uri=NMDC.tot_part_carb, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_part_carb],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

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

slots.biosample_lat_lon = Slot(uri="str(uriorcurie)", name="biosample_lat_lon", curie=None,
                   model_uri=NMDC.biosample_lat_lon, domain=Biosample, range=Optional[Union[dict, "GeolocationValue"]], mappings = [MIXS.lat_lon],
                   pattern=re.compile(r'\d+[.\d+] \d+[.\d+]'))

slots.biosample_env_broad_scale = Slot(uri="str(uriorcurie)", name="biosample_env_broad_scale", curie=None,
                   model_uri=NMDC.biosample_env_broad_scale, domain=Biosample, range=Union[dict, "ControlledTermValue"], mappings = [MIXS.env_broad_scale],
                   pattern=re.compile(r'.* \S+:\S+'))

slots.biosample_env_local_scale = Slot(uri="str(uriorcurie)", name="biosample_env_local_scale", curie=None,
                   model_uri=NMDC.biosample_env_local_scale, domain=Biosample, range=Union[dict, "ControlledTermValue"], mappings = [MIXS.env_local_scale],
                   pattern=re.compile(r'.* \S+:\S+'))

slots.biosample_env_medium = Slot(uri="str(uriorcurie)", name="biosample_env_medium", curie=None,
                   model_uri=NMDC.biosample_env_medium, domain=Biosample, range=Union[dict, "ControlledTermValue"], mappings = [MIXS.env_medium],
                   pattern=re.compile(r'.* \S+:\S+'))

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
