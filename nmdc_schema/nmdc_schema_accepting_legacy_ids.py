# Auto generated from nmdc_schema_accepting_legacy_ids.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-06-17T20:17:08
# Schema: NMDC
#
# id: https://w3id.org/nmdc/nmdc
# description: Schema for National Microbiome Data Collaborative (NMDC).
#   This schema is organized into multiple modules, such as:
#
#    * a set of core types for representing data values
#    * a subset of the mixs schema
#    * an annotation schema
#    * the NMDC schema itself, into which the other modules are imported
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.metamodelcore import Bool, Curie, Decimal, ElementIdentifier, NCName, NodeIdentifier, URI, URIorCURIE, XSDDate, XSDDateTime, XSDTime

metamodel_version = "1.7.0"
version = "0.0.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
CATH = CurieNamespace('CATH', 'https://bioregistry.io/cath:')
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
CHEMBL_COMPOUND = CurieNamespace('CHEMBL_COMPOUND', 'https://bioregistry.io/chembl.compound:')
CHMO = CurieNamespace('CHMO', 'http://purl.obolibrary.org/obo/CHMO_')
COG = CurieNamespace('COG', 'https://bioregistry.io/cog:')
CONTAMINANT = CurieNamespace('Contaminant', 'http://example.org/contaminant/')
DRUGBANK = CurieNamespace('DRUGBANK', 'https://bioregistry.io/drugbank:')
EC = CurieNamespace('EC', 'https://bioregistry.io/eccode:')
EFO = CurieNamespace('EFO', 'http://www.ebi.ac.uk/efo/')
EGGNOG = CurieNamespace('EGGNOG', 'https://bioregistry.io/eggnog:')
ENVO = CurieNamespace('ENVO', 'http://purl.obolibrary.org/obo/ENVO_')
FBCV = CurieNamespace('FBcv', 'http://purl.obolibrary.org/obo/FBcv_')
FMA = CurieNamespace('FMA', 'http://purl.obolibrary.org/obo/FMA_')
GO = CurieNamespace('GO', 'http://purl.obolibrary.org/obo/GO_')
HMDB = CurieNamespace('HMDB', 'https://bioregistry.io/hmdb:')
ISA = CurieNamespace('ISA', 'http://example.org/isa/')
KEGG_COMPOUND = CurieNamespace('KEGG_COMPOUND', 'https://bioregistry.io/kegg.compound:')
KEGG_ORTHOLOGY = CurieNamespace('KEGG_ORTHOLOGY', 'https://bioregistry.io/kegg.orthology:')
KEGG_REACTION = CurieNamespace('KEGG_REACTION', 'https://bioregistry.io/kegg.reaction:')
KEGG_PATHWAY = CurieNamespace('KEGG_PATHWAY', 'https://bioregistry.io/kegg.pathway:')
MASSIVE = CurieNamespace('MASSIVE', 'https://bioregistry.io/reference/massive:')
MESH = CurieNamespace('MESH', 'https://bioregistry.io/mesh:')
MISO = CurieNamespace('MISO', 'http://purl.obolibrary.org/obo/MISO_')
MIXS = CurieNamespace('MIXS', 'https://w3id.org/mixs/')
MIXS_YAML = CurieNamespace('MIXS_yaml', 'https://raw.githubusercontent.com/microbiomedata/mixs/main/model/schema/')
MS = CurieNamespace('MS', 'http://purl.obolibrary.org/obo/MS_')
METACYC = CurieNamespace('MetaCyc', 'https://bioregistry.io/metacyc.compound:')
METANETX = CurieNamespace('MetaNetX', 'http://example.org/metanetx/')
NCBITAXON = CurieNamespace('NCBITaxon', 'http://purl.obolibrary.org/obo/NCBITaxon_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
ORCID = CurieNamespace('ORCID', 'https://orcid.org/')
PANTHER_FAMILY = CurieNamespace('PANTHER_FAMILY', 'https://bioregistry.io/panther.family:')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
PFAM = CurieNamespace('PFAM', 'https://bioregistry.io/pfam:')
PO = CurieNamespace('PO', 'http://purl.obolibrary.org/obo/PO_')
PR = CurieNamespace('PR', 'http://purl.obolibrary.org/obo/PR_')
PUBCHEM_COMPOUND = CurieNamespace('PUBCHEM_COMPOUND', 'https://bioregistry.io/pubchem.compound:')
RHEA = CurieNamespace('RHEA', 'https://bioregistry.io/rhea:')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
RETRORULES = CurieNamespace('RetroRules', 'http://example.org/retrorules/')
SEED = CurieNamespace('SEED', 'https://bioregistry.io/seed:')
SIO = CurieNamespace('SIO', 'http://semanticscience.org/resource/SIO_')
SO = CurieNamespace('SO', 'http://purl.obolibrary.org/obo/SO_')
SUPFAM = CurieNamespace('SUPFAM', 'https://bioregistry.io/supfam:')
TIGRFAM = CurieNamespace('TIGRFAM', 'https://bioregistry.io/tigrfam:')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
UO = CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_')
UNIPROTKB = CurieNamespace('UniProtKB', 'https://bioregistry.io/uniprot:')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
BIOPROJECT = CurieNamespace('bioproject', 'https://identifiers.org/bioproject:')
BIOSAMPLE = CurieNamespace('biosample', 'https://bioregistry.io/biosample:')
CAS = CurieNamespace('cas', 'https://bioregistry.io/cas:')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
DOI = CurieNamespace('doi', 'https://bioregistry.io/doi:')
EDAM_DATA = CurieNamespace('edam_data', 'http://edamontology.org/data_')
EMSL = CurieNamespace('emsl', 'http://example.org/emsl_in_mongodb/')
EMSL_PROJECT = CurieNamespace('emsl_project', 'https://bioregistry.io/emsl.project:')
EMSL_UUID_LIKE = CurieNamespace('emsl_uuid_like', 'http://example.org/emsl_uuid_like/')
GENERIC = CurieNamespace('generic', 'https://example.org/generic/')
GNPS_TASK = CurieNamespace('gnps_task', 'https://bioregistry.io/gnps.task:')
GOLD = CurieNamespace('gold', 'https://bioregistry.io/gold:')
GTPO = CurieNamespace('gtpo', 'http://example.org/gtpo/')
IGSN = CurieNamespace('igsn', 'https://app.geosamples.org/sample/igsn/')
IMG_TAXON = CurieNamespace('img_taxon', 'https://bioregistry.io/img.taxon:')
JGI = CurieNamespace('jgi', 'http://example.org/jgi/')
JGI_ANALYSIS = CurieNamespace('jgi_analysis', 'https://data.jgi.doe.gov/search?q=')
JGI_PROPOSAL = CurieNamespace('jgi_proposal', 'https://bioregistry.io/jgi.proposal:')
KEGG = CurieNamespace('kegg', 'https://bioregistry.io/kegg:')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MGNIFY_PROJ = CurieNamespace('mgnify_proj', 'https://bioregistry.io/mgnify.proj:')
MY_EMSL = CurieNamespace('my_emsl', 'https://release.my.emsl.pnnl.gov/released_data/')
NEON_IDENTIFIER = CurieNamespace('neon_identifier', 'http://example.org/neon/identifier/')
NEON_SCHEMA = CurieNamespace('neon_schema', 'http://example.org/neon/schema/')
NMDC = CurieNamespace('nmdc', 'https://w3id.org/nmdc/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
QUD = CurieNamespace('qud', 'http://qudt.org/1.1/schema/qudt#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SHEX = CurieNamespace('shex', 'http://www.w3.org/ns/shex#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
WGS84 = CurieNamespace('wgs84', 'http://www.w3.org/2003/01/geo/wgs84_pos#')
WIKIDATA = CurieNamespace('wikidata', 'http://www.wikidata.org/entity/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = NMDC


# Types
class String(str):
    """ A character string """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "string"
    type_model_uri = NMDC.String


class Integer(int):
    """ An integer """
    type_class_uri = XSD["integer"]
    type_class_curie = "xsd:integer"
    type_name = "integer"
    type_model_uri = NMDC.Integer


class Boolean(Bool):
    """ A binary (true or false) value """
    type_class_uri = XSD["boolean"]
    type_class_curie = "xsd:boolean"
    type_name = "boolean"
    type_model_uri = NMDC.Boolean


class Float(float):
    """ A real number that conforms to the xsd:float specification """
    type_class_uri = XSD["float"]
    type_class_curie = "xsd:float"
    type_name = "float"
    type_model_uri = NMDC.Float


class Double(float):
    """ A real number that conforms to the xsd:double specification """
    type_class_uri = XSD["double"]
    type_class_curie = "xsd:double"
    type_name = "double"
    type_model_uri = NMDC.Double


class Decimal(Decimal):
    """ A real number with arbitrary precision that conforms to the xsd:decimal specification """
    type_class_uri = XSD["decimal"]
    type_class_curie = "xsd:decimal"
    type_name = "decimal"
    type_model_uri = NMDC.Decimal


class Time(XSDTime):
    """ A time object represents a (local) time of day, independent of any particular day """
    type_class_uri = XSD["time"]
    type_class_curie = "xsd:time"
    type_name = "time"
    type_model_uri = NMDC.Time


class Date(XSDDate):
    """ a date (year, month and day) in an idealized calendar """
    type_class_uri = XSD["date"]
    type_class_curie = "xsd:date"
    type_name = "date"
    type_model_uri = NMDC.Date


class Datetime(XSDDateTime):
    """ The combination of a date and time """
    type_class_uri = XSD["dateTime"]
    type_class_curie = "xsd:dateTime"
    type_name = "datetime"
    type_model_uri = NMDC.Datetime


class DateOrDatetime(str):
    """ Either a date or a datetime """
    type_class_uri = LINKML["DateOrDatetime"]
    type_class_curie = "linkml:DateOrDatetime"
    type_name = "date_or_datetime"
    type_model_uri = NMDC.DateOrDatetime


class Uriorcurie(URIorCURIE):
    """ a URI or a CURIE """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "uriorcurie"
    type_model_uri = NMDC.Uriorcurie


class Curie(Curie):
    """ a compact URI """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "curie"
    type_model_uri = NMDC.Curie


class Uri(URI):
    """ a complete URI """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "uri"
    type_model_uri = NMDC.Uri


class Ncname(NCName):
    """ Prefix part of CURIE """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "ncname"
    type_model_uri = NMDC.Ncname


class Objectidentifier(ElementIdentifier):
    """ A URI or CURIE that represents an object in the model. """
    type_class_uri = SHEX["iri"]
    type_class_curie = "shex:iri"
    type_name = "objectidentifier"
    type_model_uri = NMDC.Objectidentifier


class Nodeidentifier(NodeIdentifier):
    """ A URI, CURIE or BNODE that represents a node in a model. """
    type_class_uri = SHEX["nonLiteral"]
    type_class_curie = "shex:nonLiteral"
    type_name = "nodeidentifier"
    type_model_uri = NMDC.Nodeidentifier


class Jsonpointer(str):
    """ A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "jsonpointer"
    type_model_uri = NMDC.Jsonpointer


class Jsonpath(str):
    """ A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "jsonpath"
    type_model_uri = NMDC.Jsonpath


class Sparqlpath(str):
    """ A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "sparqlpath"
    type_model_uri = NMDC.Sparqlpath


class Bytes(int):
    """ An integer value that corresponds to a size in bytes """
    type_class_uri = XSD["long"]
    type_class_curie = "xsd:long"
    type_name = "bytes"
    type_model_uri = NMDC.Bytes


class DecimalDegree(float):
    """ A decimal degree expresses latitude or longitude as decimal fractions. """
    type_class_uri = XSD["decimal"]
    type_class_curie = "xsd:decimal"
    type_name = "decimal degree"
    type_model_uri = NMDC.DecimalDegree


class LanguageCode(str):
    """ A language code conforming to ISO_639-1 """
    type_class_uri = XSD["language"]
    type_class_curie = "xsd:language"
    type_name = "language code"
    type_model_uri = NMDC.LanguageCode


class Unit(str):
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "unit"
    type_model_uri = NMDC.Unit


class ExternalIdentifier(Uriorcurie):
    """ A CURIE representing an external identifier """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "external_identifier"
    type_model_uri = NMDC.ExternalIdentifier


# Class references
class NamedThingId(URIorCURIE):
    pass


class GeneProductId(NamedThingId):
    pass


class OntologyClassId(NamedThingId):
    pass


class EnvironmentalMaterialTermId(OntologyClassId):
    pass


class ChemicalEntityId(OntologyClassId):
    pass


class FunctionalAnnotationTermId(OntologyClassId):
    pass


class PathwayId(FunctionalAnnotationTermId):
    pass


class OrthologyGroupId(FunctionalAnnotationTermId):
    pass


class MaterialEntityId(NamedThingId):
    pass


class BiosampleId(MaterialEntityId):
    pass


class ProcessedSampleId(MaterialEntityId):
    pass


class SiteId(MaterialEntityId):
    pass


class FieldResearchSiteId(SiteId):
    pass


class InstrumentId(MaterialEntityId):
    pass


class PlannedProcessId(NamedThingId):
    pass


class CollectingBiosamplesFromSiteId(PlannedProcessId):
    pass


class ProtocolExecutionId(PlannedProcessId):
    pass


class StorageProcessId(PlannedProcessId):
    pass


class MaterialProcessingId(PlannedProcessId):
    pass


class PoolingId(MaterialProcessingId):
    pass


class ExtractionId(MaterialProcessingId):
    pass


class LibraryPreparationId(MaterialProcessingId):
    pass


class SubSamplingProcessId(MaterialProcessingId):
    pass


class MixingProcessId(MaterialProcessingId):
    pass


class FiltrationProcessId(MaterialProcessingId):
    pass


class ChromatographicSeparationProcessId(MaterialProcessingId):
    pass


class DissolvingProcessId(MaterialProcessingId):
    pass


class ChemicalConversionProcessId(MaterialProcessingId):
    pass


class StudyId(NamedThingId):
    pass


class InformationObjectId(NamedThingId):
    pass


class ConfigurationId(InformationObjectId):
    pass


class MassSpectrometryConfigurationId(ConfigurationId):
    pass


class ChromatographyConfigurationId(ConfigurationId):
    pass


class DataObjectId(InformationObjectId):
    pass


class DataGenerationId(PlannedProcessId):
    pass


class NucleotideSequencingId(DataGenerationId):
    pass


class MassSpectrometryId(DataGenerationId):
    pass


class WorkflowExecutionId(PlannedProcessId):
    pass


class MetagenomeAnnotationId(WorkflowExecutionId):
    pass


class MetagenomeAssemblyId(WorkflowExecutionId):
    pass


class MetatranscriptomeAssemblyId(WorkflowExecutionId):
    pass


class MetatranscriptomeAnnotationId(WorkflowExecutionId):
    pass


class MetatranscriptomeAnalysisId(WorkflowExecutionId):
    pass


class MagsAnalysisId(WorkflowExecutionId):
    pass


class MetagenomeSequencingId(WorkflowExecutionId):
    pass


class ReadQcAnalysisId(WorkflowExecutionId):
    pass


class ReadBasedTaxonomyAnalysisId(WorkflowExecutionId):
    pass


class MetabolomicsAnalysisId(WorkflowExecutionId):
    pass


class MetaproteomicsAnalysisId(WorkflowExecutionId):
    pass


class NomAnalysisId(WorkflowExecutionId):
    pass


class CalibrationInformationId(InformationObjectId):
    pass


@dataclass
class FunctionalAnnotationAggMember(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["FunctionalAnnotationAggMember"]
    class_class_curie: ClassVar[str] = "nmdc:FunctionalAnnotationAggMember"
    class_name: ClassVar[str] = "FunctionalAnnotationAggMember"
    class_model_uri: ClassVar[URIRef] = NMDC.FunctionalAnnotationAggMember

    metagenome_annotation_id: Union[str, WorkflowExecutionId] = None
    gene_function_id: Union[str, URIorCURIE] = None
    count: int = None
    type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.metagenome_annotation_id):
            self.MissingRequiredField("metagenome_annotation_id")
        if not isinstance(self.metagenome_annotation_id, WorkflowExecutionId):
            self.metagenome_annotation_id = WorkflowExecutionId(self.metagenome_annotation_id)

        if self._is_empty(self.gene_function_id):
            self.MissingRequiredField("gene_function_id")
        if not isinstance(self.gene_function_id, URIorCURIE):
            self.gene_function_id = URIorCURIE(self.gene_function_id)

        if self._is_empty(self.count):
            self.MissingRequiredField("count")
        if not isinstance(self.count, int):
            self.count = int(self.count)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)

        super().__post_init__(**kwargs)


@dataclass
class Database(YAMLRoot):
    """
    An abstract holder for any set of metadata and data. It does not need to correspond to an actual managed database
    top level holder class. When translated to JSON-Schema this is the 'root' object. It should contain pointers to
    other objects of interest. For MongoDB, the lists of objects that Database slots point to correspond to
    **collections**.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["Database"]
    class_class_curie: ClassVar[str] = "nmdc:Database"
    class_name: ClassVar[str] = "Database"
    class_model_uri: ClassVar[URIRef] = NMDC.Database

    biosample_set: Optional[Union[Dict[Union[str, BiosampleId], Union[dict, "Biosample"]], List[Union[dict, "Biosample"]]]] = empty_dict()
    calibration_set: Optional[Union[Dict[Union[str, CalibrationInformationId], Union[dict, "CalibrationInformation"]], List[Union[dict, "CalibrationInformation"]]]] = empty_dict()
    chemical_entity_set: Optional[Union[Dict[Union[str, ChemicalEntityId], Union[dict, "ChemicalEntity"]], List[Union[dict, "ChemicalEntity"]]]] = empty_dict()
    collecting_biosamples_from_site_set: Optional[Union[Dict[Union[str, CollectingBiosamplesFromSiteId], Union[dict, "CollectingBiosamplesFromSite"]], List[Union[dict, "CollectingBiosamplesFromSite"]]]] = empty_dict()
    configuration_set: Optional[Union[Dict[Union[str, ConfigurationId], Union[dict, "Configuration"]], List[Union[dict, "Configuration"]]]] = empty_dict()
    data_generation_set: Optional[Union[Dict[Union[str, DataGenerationId], Union[dict, "DataGeneration"]], List[Union[dict, "DataGeneration"]]]] = empty_dict()
    data_object_set: Optional[Union[Dict[Union[str, DataObjectId], Union[dict, "DataObject"]], List[Union[dict, "DataObject"]]]] = empty_dict()
    field_research_site_set: Optional[Union[Dict[Union[str, FieldResearchSiteId], Union[dict, "FieldResearchSite"]], List[Union[dict, "FieldResearchSite"]]]] = empty_dict()
    functional_annotation_agg: Optional[Union[Union[dict, FunctionalAnnotationAggMember], List[Union[dict, FunctionalAnnotationAggMember]]]] = empty_list()
    functional_annotation_set: Optional[Union[Union[dict, "FunctionalAnnotation"], List[Union[dict, "FunctionalAnnotation"]]]] = empty_list()
    genome_feature_set: Optional[Union[Union[dict, "GenomeFeature"], List[Union[dict, "GenomeFeature"]]]] = empty_list()
    instrument_set: Optional[Union[Dict[Union[str, InstrumentId], Union[dict, "Instrument"]], List[Union[dict, "Instrument"]]]] = empty_dict()
    material_processing_set: Optional[Union[Dict[Union[str, MaterialProcessingId], Union[dict, "MaterialProcessing"]], List[Union[dict, "MaterialProcessing"]]]] = empty_dict()
    processed_sample_set: Optional[Union[Dict[Union[str, ProcessedSampleId], Union[dict, "ProcessedSample"]], List[Union[dict, "ProcessedSample"]]]] = empty_dict()
    protocol_execution_set: Optional[Union[Dict[Union[str, ProtocolExecutionId], Union[dict, "ProtocolExecution"]], List[Union[dict, "ProtocolExecution"]]]] = empty_dict()
    storage_process_set: Optional[Union[Dict[Union[str, StorageProcessId], Union[dict, "StorageProcess"]], List[Union[dict, "StorageProcess"]]]] = empty_dict()
    study_set: Optional[Union[Dict[Union[str, StudyId], Union[dict, "Study"]], List[Union[dict, "Study"]]]] = empty_dict()
    workflow_execution_set: Optional[Union[Dict[Union[str, WorkflowExecutionId], Union[dict, "WorkflowExecution"]], List[Union[dict, "WorkflowExecution"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="biosample_set", slot_type=Biosample, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="calibration_set", slot_type=CalibrationInformation, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="chemical_entity_set", slot_type=ChemicalEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="collecting_biosamples_from_site_set", slot_type=CollectingBiosamplesFromSite, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="configuration_set", slot_type=Configuration, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="data_generation_set", slot_type=DataGeneration, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="data_object_set", slot_type=DataObject, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="field_research_site_set", slot_type=FieldResearchSite, key_name="id", keyed=True)

        if not isinstance(self.functional_annotation_agg, list):
            self.functional_annotation_agg = [self.functional_annotation_agg] if self.functional_annotation_agg is not None else []
        self.functional_annotation_agg = [v if isinstance(v, FunctionalAnnotationAggMember) else FunctionalAnnotationAggMember(**as_dict(v)) for v in self.functional_annotation_agg]

        if not isinstance(self.functional_annotation_set, list):
            self.functional_annotation_set = [self.functional_annotation_set] if self.functional_annotation_set is not None else []
        self.functional_annotation_set = [v if isinstance(v, FunctionalAnnotation) else FunctionalAnnotation(**as_dict(v)) for v in self.functional_annotation_set]

        if not isinstance(self.genome_feature_set, list):
            self.genome_feature_set = [self.genome_feature_set] if self.genome_feature_set is not None else []
        self.genome_feature_set = [v if isinstance(v, GenomeFeature) else GenomeFeature(**as_dict(v)) for v in self.genome_feature_set]

        self._normalize_inlined_as_list(slot_name="instrument_set", slot_type=Instrument, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="material_processing_set", slot_type=MaterialProcessing, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="processed_sample_set", slot_type=ProcessedSample, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="protocol_execution_set", slot_type=ProtocolExecution, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="storage_process_set", slot_type=StorageProcess, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="study_set", slot_type=Study, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="workflow_execution_set", slot_type=WorkflowExecution, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class MobilePhaseSegment(YAMLRoot):
    """
    A fluid mixture of substances that flow though a chromatographic stationary phase.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["MobilePhaseSegment"]
    class_class_curie: ClassVar[str] = "nmdc:MobilePhaseSegment"
    class_name: ClassVar[str] = "MobilePhaseSegment"
    class_model_uri: ClassVar[URIRef] = NMDC.MobilePhaseSegment

    type: Union[str, URIorCURIE] = None
    duration: Optional[Union[dict, "QuantityValue"]] = None
    substances_used: Optional[Union[Union[dict, "PortionOfSubstance"], List[Union[dict, "PortionOfSubstance"]]]] = empty_list()
    volume: Optional[Union[dict, "QuantityValue"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)

        if self.duration is not None and not isinstance(self.duration, QuantityValue):
            self.duration = QuantityValue(**as_dict(self.duration))

        if not isinstance(self.substances_used, list):
            self.substances_used = [self.substances_used] if self.substances_used is not None else []
        self.substances_used = [v if isinstance(v, PortionOfSubstance) else PortionOfSubstance(**as_dict(v)) for v in self.substances_used]

        if self.volume is not None and not isinstance(self.volume, QuantityValue):
            self.volume = QuantityValue(**as_dict(self.volume))

        super().__post_init__(**kwargs)


@dataclass
class PortionOfSubstance(YAMLRoot):
    """
    A portion of any matter of defined composition that has discrete existence, whose origin may be biological,
    mineral or chemical.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["PortionOfSubstance"]
    class_class_curie: ClassVar[str] = "nmdc:PortionOfSubstance"
    class_name: ClassVar[str] = "PortionOfSubstance"
    class_model_uri: ClassVar[URIRef] = NMDC.PortionOfSubstance

    type: Union[str, URIorCURIE] = None
    final_concentration: Optional[Union[dict, "QuantityValue"]] = None
    known_as: Optional[Union[str, ChemicalEntityId]] = None
    mass: Optional[Union[dict, "QuantityValue"]] = None
    sample_state_information: Optional[Union[str, "SampleStateEnum"]] = None
    source_concentration: Optional[Union[dict, "QuantityValue"]] = None
    substance_role: Optional[Union[str, "SubstanceRoleEnum"]] = None
    volume: Optional[Union[dict, "QuantityValue"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)

        if self.final_concentration is not None and not isinstance(self.final_concentration, QuantityValue):
            self.final_concentration = QuantityValue(**as_dict(self.final_concentration))

        if self.known_as is not None and not isinstance(self.known_as, ChemicalEntityId):
            self.known_as = ChemicalEntityId(self.known_as)

        if self.mass is not None and not isinstance(self.mass, QuantityValue):
            self.mass = QuantityValue(**as_dict(self.mass))

        if self.sample_state_information is not None and not isinstance(self.sample_state_information, SampleStateEnum):
            self.sample_state_information = SampleStateEnum(self.sample_state_information)

        if self.source_concentration is not None and not isinstance(self.source_concentration, QuantityValue):
            self.source_concentration = QuantityValue(**as_dict(self.source_concentration))

        if self.substance_role is not None and not isinstance(self.substance_role, SubstanceRoleEnum):
            self.substance_role = SubstanceRoleEnum(self.substance_role)

        if self.volume is not None and not isinstance(self.volume, QuantityValue):
            self.volume = QuantityValue(**as_dict(self.volume))

        super().__post_init__(**kwargs)


@dataclass
class MagBin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["MagBin"]
    class_class_curie: ClassVar[str] = "nmdc:MagBin"
    class_name: ClassVar[str] = "MagBin"
    class_model_uri: ClassVar[URIRef] = NMDC.MagBin

    type: Union[str, URIorCURIE] = None
    bin_name: Optional[str] = None
    bin_quality: Optional[str] = None
    completeness: Optional[float] = None
    contamination: Optional[float] = None
    gene_count: Optional[int] = None
    gtdbtk_class: Optional[str] = None
    gtdbtk_domain: Optional[str] = None
    gtdbtk_family: Optional[str] = None
    gtdbtk_genus: Optional[str] = None
    gtdbtk_order: Optional[str] = None
    gtdbtk_phylum: Optional[str] = None
    gtdbtk_species: Optional[str] = None
    members_id: Optional[str] = None
    num_16s: Optional[int] = None
    num_23s: Optional[int] = None
    num_5s: Optional[int] = None
    num_t_rna: Optional[int] = None
    number_of_contig: Optional[int] = None
    total_bases: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)

        if self.bin_name is not None and not isinstance(self.bin_name, str):
            self.bin_name = str(self.bin_name)

        if self.bin_quality is not None and not isinstance(self.bin_quality, str):
            self.bin_quality = str(self.bin_quality)

        if self.completeness is not None and not isinstance(self.completeness, float):
            self.completeness = float(self.completeness)

        if self.contamination is not None and not isinstance(self.contamination, float):
            self.contamination = float(self.contamination)

        if self.gene_count is not None and not isinstance(self.gene_count, int):
            self.gene_count = int(self.gene_count)

        if self.gtdbtk_class is not None and not isinstance(self.gtdbtk_class, str):
            self.gtdbtk_class = str(self.gtdbtk_class)

        if self.gtdbtk_domain is not None and not isinstance(self.gtdbtk_domain, str):
            self.gtdbtk_domain = str(self.gtdbtk_domain)

        if self.gtdbtk_family is not None and not isinstance(self.gtdbtk_family, str):
            self.gtdbtk_family = str(self.gtdbtk_family)

        if self.gtdbtk_genus is not None and not isinstance(self.gtdbtk_genus, str):
            self.gtdbtk_genus = str(self.gtdbtk_genus)

        if self.gtdbtk_order is not None and not isinstance(self.gtdbtk_order, str):
            self.gtdbtk_order = str(self.gtdbtk_order)

        if self.gtdbtk_phylum is not None and not isinstance(self.gtdbtk_phylum, str):
            self.gtdbtk_phylum = str(self.gtdbtk_phylum)

        if self.gtdbtk_species is not None and not isinstance(self.gtdbtk_species, str):
            self.gtdbtk_species = str(self.gtdbtk_species)

        if self.members_id is not None and not isinstance(self.members_id, str):
            self.members_id = str(self.members_id)

        if self.num_16s is not None and not isinstance(self.num_16s, int):
            self.num_16s = int(self.num_16s)

        if self.num_23s is not None and not isinstance(self.num_23s, int):
            self.num_23s = int(self.num_23s)

        if self.num_5s is not None and not isinstance(self.num_5s, int):
            self.num_5s = int(self.num_5s)

        if self.num_t_rna is not None and not isinstance(self.num_t_rna, int):
            self.num_t_rna = int(self.num_t_rna)

        if self.number_of_contig is not None and not isinstance(self.number_of_contig, int):
            self.number_of_contig = int(self.number_of_contig)

        if self.total_bases is not None and not isinstance(self.total_bases, int):
            self.total_bases = int(self.total_bases)

        super().__post_init__(**kwargs)


@dataclass
class MetaboliteIdentification(YAMLRoot):
    """
    This is used to link a metabolomics analysis workflow to a specific metabolite
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["MetaboliteIdentification"]
    class_class_curie: ClassVar[str] = "nmdc:MetaboliteIdentification"
    class_name: ClassVar[str] = "MetaboliteIdentification"
    class_model_uri: ClassVar[URIRef] = NMDC.MetaboliteIdentification

    type: Union[str, URIorCURIE] = None
    alternative_identifiers: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    highest_similarity_score: Optional[float] = None
    metabolite_identified: Optional[Union[str, ChemicalEntityId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)

        if not isinstance(self.alternative_identifiers, list):
            self.alternative_identifiers = [self.alternative_identifiers] if self.alternative_identifiers is not None else []
        self.alternative_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.alternative_identifiers]

        if self.highest_similarity_score is not None and not isinstance(self.highest_similarity_score, float):
            self.highest_similarity_score = float(self.highest_similarity_score)

        if self.metabolite_identified is not None and not isinstance(self.metabolite_identified, ChemicalEntityId):
            self.metabolite_identified = ChemicalEntityId(self.metabolite_identified)

        super().__post_init__(**kwargs)


@dataclass
class PeptideQuantification(YAMLRoot):
    """
    This is used to link a metaproteomics analysis workflow to a specific peptide sequence and related information
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["PeptideQuantification"]
    class_class_curie: ClassVar[str] = "nmdc:PeptideQuantification"
    class_name: ClassVar[str] = "PeptideQuantification"
    class_model_uri: ClassVar[URIRef] = NMDC.PeptideQuantification

    type: Union[str, URIorCURIE] = None
    all_proteins: Optional[Union[Union[str, GeneProductId], List[Union[str, GeneProductId]]]] = empty_list()
    best_protein: Optional[Union[str, GeneProductId]] = None
    min_q_value: Optional[float] = None
    peptide_sequence: Optional[str] = None
    peptide_spectral_count: Optional[int] = None
    peptide_sum_masic_abundance: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)

        if not isinstance(self.all_proteins, list):
            self.all_proteins = [self.all_proteins] if self.all_proteins is not None else []
        self.all_proteins = [v if isinstance(v, GeneProductId) else GeneProductId(v) for v in self.all_proteins]

        if self.best_protein is not None and not isinstance(self.best_protein, GeneProductId):
            self.best_protein = GeneProductId(self.best_protein)

        if self.min_q_value is not None and not isinstance(self.min_q_value, float):
            self.min_q_value = float(self.min_q_value)

        if self.peptide_sequence is not None and not isinstance(self.peptide_sequence, str):
            self.peptide_sequence = str(self.peptide_sequence)

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

    class_class_uri: ClassVar[URIRef] = NMDC["ProteinQuantification"]
    class_class_curie: ClassVar[str] = "nmdc:ProteinQuantification"
    class_name: ClassVar[str] = "ProteinQuantification"
    class_model_uri: ClassVar[URIRef] = NMDC.ProteinQuantification

    type: Union[str, URIorCURIE] = None
    all_proteins: Optional[Union[Union[str, GeneProductId], List[Union[str, GeneProductId]]]] = empty_list()
    best_protein: Optional[Union[str, GeneProductId]] = None
    peptide_sequence_count: Optional[int] = None
    protein_spectral_count: Optional[int] = None
    protein_sum_masic_abundance: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)

        if not isinstance(self.all_proteins, list):
            self.all_proteins = [self.all_proteins] if self.all_proteins is not None else []
        self.all_proteins = [v if isinstance(v, GeneProductId) else GeneProductId(v) for v in self.all_proteins]

        if self.best_protein is not None and not isinstance(self.best_protein, GeneProductId):
            self.best_protein = GeneProductId(self.best_protein)

        if self.peptide_sequence_count is not None and not isinstance(self.peptide_sequence_count, int):
            self.peptide_sequence_count = int(self.peptide_sequence_count)

        if self.protein_spectral_count is not None and not isinstance(self.protein_spectral_count, int):
            self.protein_spectral_count = int(self.protein_spectral_count)

        if self.protein_sum_masic_abundance is not None and not isinstance(self.protein_sum_masic_abundance, int):
            self.protein_sum_masic_abundance = int(self.protein_sum_masic_abundance)

        super().__post_init__(**kwargs)


@dataclass
class GenomeFeature(YAMLRoot):
    """
    A feature localized to an interval along a genome
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["GenomeFeature"]
    class_class_curie: ClassVar[str] = "nmdc:GenomeFeature"
    class_name: ClassVar[str] = "GenomeFeature"
    class_model_uri: ClassVar[URIRef] = NMDC.GenomeFeature

    end: int = None
    seqid: str = None
    start: int = None
    type: Union[str, URIorCURIE] = None
    encodes: Optional[Union[str, GeneProductId]] = None
    feature_type: Optional[str] = None
    phase: Optional[int] = None
    strand: Optional[str] = None
    feature_category: Optional[Union[dict, "ControlledIdentifiedTermValue"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.end):
            self.MissingRequiredField("end")
        if not isinstance(self.end, int):
            self.end = int(self.end)

        if self._is_empty(self.seqid):
            self.MissingRequiredField("seqid")
        if not isinstance(self.seqid, str):
            self.seqid = str(self.seqid)

        if self._is_empty(self.start):
            self.MissingRequiredField("start")
        if not isinstance(self.start, int):
            self.start = int(self.start)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)

        if self.encodes is not None and not isinstance(self.encodes, GeneProductId):
            self.encodes = GeneProductId(self.encodes)

        if self.feature_type is not None and not isinstance(self.feature_type, str):
            self.feature_type = str(self.feature_type)

        if self.phase is not None and not isinstance(self.phase, int):
            self.phase = int(self.phase)

        if self.strand is not None and not isinstance(self.strand, str):
            self.strand = str(self.strand)

        if self.feature_category is not None and not isinstance(self.feature_category, ControlledIdentifiedTermValue):
            self.feature_category = ControlledIdentifiedTermValue(**as_dict(self.feature_category))

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

    class_class_uri: ClassVar[URIRef] = NMDC["FunctionalAnnotation"]
    class_class_curie: ClassVar[str] = "nmdc:FunctionalAnnotation"
    class_name: ClassVar[str] = "FunctionalAnnotation"
    class_model_uri: ClassVar[URIRef] = NMDC.FunctionalAnnotation

    type: Union[str, URIorCURIE] = None
    has_function: Optional[str] = None
    subject: Optional[Union[str, GeneProductId]] = None
    was_generated_by: Optional[Union[str, MetagenomeAnnotationId]] = None
    feature_category: Optional[Union[dict, "ControlledIdentifiedTermValue"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)

        if self.has_function is not None and not isinstance(self.has_function, str):
            self.has_function = str(self.has_function)

        if self.subject is not None and not isinstance(self.subject, GeneProductId):
            self.subject = GeneProductId(self.subject)

        if self.was_generated_by is not None and not isinstance(self.was_generated_by, MetagenomeAnnotationId):
            self.was_generated_by = MetagenomeAnnotationId(self.was_generated_by)

        if self.feature_category is not None and not isinstance(self.feature_category, ControlledIdentifiedTermValue):
            self.feature_category = ControlledIdentifiedTermValue(**as_dict(self.feature_category))

        super().__post_init__(**kwargs)


@dataclass
class AttributeValue(YAMLRoot):
    """
    The value for any value of a attribute for a sample. This object can hold both the un-normalized atomic value and
    the structured value
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["AttributeValue"]
    class_class_curie: ClassVar[str] = "nmdc:AttributeValue"
    class_name: ClassVar[str] = "AttributeValue"
    class_model_uri: ClassVar[URIRef] = NMDC.AttributeValue

    type: Union[str, URIorCURIE] = None
    has_raw_value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)

        if self.has_raw_value is not None and not isinstance(self.has_raw_value, str):
            self.has_raw_value = str(self.has_raw_value)

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_class_curie", type_designator_value)


            if target_cls is None:
                target_cls = cls._class_for("class_class_uri", type_designator_value)


            if target_cls is None:
                target_cls = cls._class_for("class_model_uri", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_class_curie', 'class_class_uri', 'class_model_uri']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass
class QuantityValue(AttributeValue):
    """
    A simple quantity, e.g. 2cm
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["QuantityValue"]
    class_class_curie: ClassVar[str] = "nmdc:QuantityValue"
    class_name: ClassVar[str] = "QuantityValue"
    class_model_uri: ClassVar[URIRef] = NMDC.QuantityValue

    type: Union[str, URIorCURIE] = None
    has_maximum_numeric_value: Optional[Decimal] = None
    has_minimum_numeric_value: Optional[Decimal] = None
    has_numeric_value: Optional[Decimal] = None
    has_unit: Optional[str] = None
    has_raw_value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_maximum_numeric_value is not None and not isinstance(self.has_maximum_numeric_value, Decimal):
            self.has_maximum_numeric_value = Decimal(self.has_maximum_numeric_value)

        if self.has_minimum_numeric_value is not None and not isinstance(self.has_minimum_numeric_value, Decimal):
            self.has_minimum_numeric_value = Decimal(self.has_minimum_numeric_value)

        if self.has_numeric_value is not None and not isinstance(self.has_numeric_value, Decimal):
            self.has_numeric_value = Decimal(self.has_numeric_value)

        if self.has_unit is not None and not isinstance(self.has_unit, str):
            self.has_unit = str(self.has_unit)

        if self.has_raw_value is not None and not isinstance(self.has_raw_value, str):
            self.has_raw_value = str(self.has_raw_value)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class ImageValue(AttributeValue):
    """
    An attribute value representing an image.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["ImageValue"]
    class_class_curie: ClassVar[str] = "nmdc:ImageValue"
    class_name: ClassVar[str] = "ImageValue"
    class_model_uri: ClassVar[URIRef] = NMDC.ImageValue

    type: Union[str, URIorCURIE] = None
    url: Optional[str] = None
    description: Optional[str] = None
    display_order: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.display_order is not None and not isinstance(self.display_order, int):
            self.display_order = int(self.display_order)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class PersonValue(AttributeValue):
    """
    An attribute value representing a person
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["PersonValue"]
    class_class_curie: ClassVar[str] = "nmdc:PersonValue"
    class_name: ClassVar[str] = "PersonValue"
    class_model_uri: ClassVar[URIRef] = NMDC.PersonValue

    type: Union[str, URIorCURIE] = None
    email: Optional[str] = None
    name: Optional[str] = None
    orcid: Optional[str] = None
    profile_image_url: Optional[str] = None
    websites: Optional[Union[str, List[str]]] = empty_list()
    has_raw_value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.orcid is not None and not isinstance(self.orcid, str):
            self.orcid = str(self.orcid)

        if self.profile_image_url is not None and not isinstance(self.profile_image_url, str):
            self.profile_image_url = str(self.profile_image_url)

        if not isinstance(self.websites, list):
            self.websites = [self.websites] if self.websites is not None else []
        self.websites = [v if isinstance(v, str) else str(v) for v in self.websites]

        if self.has_raw_value is not None and not isinstance(self.has_raw_value, str):
            self.has_raw_value = str(self.has_raw_value)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class TextValue(AttributeValue):
    """
    A basic string value
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["TextValue"]
    class_class_curie: ClassVar[str] = "nmdc:TextValue"
    class_name: ClassVar[str] = "TextValue"
    class_model_uri: ClassVar[URIRef] = NMDC.TextValue

    type: Union[str, URIorCURIE] = None
    language: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.language is not None and not isinstance(self.language, str):
            self.language = str(self.language)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class TimestampValue(AttributeValue):
    """
    A value that is a timestamp. The range should be ISO-8601
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["TimestampValue"]
    class_class_curie: ClassVar[str] = "nmdc:TimestampValue"
    class_name: ClassVar[str] = "TimestampValue"
    class_model_uri: ClassVar[URIRef] = NMDC.TimestampValue

    type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class ControlledTermValue(AttributeValue):
    """
    A controlled term or class from an ontology
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["ControlledTermValue"]
    class_class_curie: ClassVar[str] = "nmdc:ControlledTermValue"
    class_name: ClassVar[str] = "ControlledTermValue"
    class_model_uri: ClassVar[URIRef] = NMDC.ControlledTermValue

    type: Union[str, URIorCURIE] = None
    term: Optional[Union[dict, "OntologyClass"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.term is not None and not isinstance(self.term, OntologyClass):
            self.term = OntologyClass(**as_dict(self.term))

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class ControlledIdentifiedTermValue(ControlledTermValue):
    """
    A controlled term or class from an ontology, requiring the presence of term with an id
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["ControlledIdentifiedTermValue"]
    class_class_curie: ClassVar[str] = "nmdc:ControlledIdentifiedTermValue"
    class_name: ClassVar[str] = "ControlledIdentifiedTermValue"
    class_model_uri: ClassVar[URIRef] = NMDC.ControlledIdentifiedTermValue

    type: Union[str, URIorCURIE] = None
    term: Union[dict, "OntologyClass"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.term):
            self.MissingRequiredField("term")
        if not isinstance(self.term, OntologyClass):
            self.term = OntologyClass(**as_dict(self.term))

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class GeolocationValue(AttributeValue):
    """
    A normalized value for a location on the earth's surface
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["GeolocationValue"]
    class_class_curie: ClassVar[str] = "nmdc:GeolocationValue"
    class_name: ClassVar[str] = "GeolocationValue"
    class_model_uri: ClassVar[URIRef] = NMDC.GeolocationValue

    type: Union[str, URIorCURIE] = None
    latitude: float = None
    longitude: float = None
    has_raw_value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.latitude):
            self.MissingRequiredField("latitude")
        if not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self._is_empty(self.longitude):
            self.MissingRequiredField("longitude")
        if not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        if self.has_raw_value is not None and not isinstance(self.has_raw_value, str):
            self.has_raw_value = str(self.has_raw_value)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class NamedThing(YAMLRoot):
    """
    a databased entity or concept/class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["NamedThing"]
    class_class_curie: ClassVar[str] = "nmdc:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = NMDC.NamedThing

    id: Union[str, NamedThingId] = None
    type: Union[str, URIorCURIE] = None
    name: Optional[str] = None
    description: Optional[str] = None
    alternative_identifiers: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.alternative_identifiers, list):
            self.alternative_identifiers = [self.alternative_identifiers] if self.alternative_identifiers is not None else []
        self.alternative_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.alternative_identifiers]

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_class_curie", type_designator_value)


            if target_cls is None:
                target_cls = cls._class_for("class_class_uri", type_designator_value)


            if target_cls is None:
                target_cls = cls._class_for("class_model_uri", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_class_curie', 'class_class_uri', 'class_model_uri']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass
class GeneProduct(NamedThing):
    """
    A molecule encoded by a gene that has an evolved function
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["GeneProduct"]
    class_class_curie: ClassVar[str] = "nmdc:GeneProduct"
    class_name: ClassVar[str] = "GeneProduct"
    class_model_uri: ClassVar[URIRef] = NMDC.GeneProduct

    id: Union[str, GeneProductId] = None
    type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneProductId):
            self.id = GeneProductId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class OntologyClass(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["OntologyClass"]
    class_class_curie: ClassVar[str] = "nmdc:OntologyClass"
    class_name: ClassVar[str] = "OntologyClass"
    class_model_uri: ClassVar[URIRef] = NMDC.OntologyClass

    id: Union[str, OntologyClassId] = None
    type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class EnvironmentalMaterialTerm(OntologyClass):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["EnvironmentalMaterialTerm"]
    class_class_curie: ClassVar[str] = "nmdc:EnvironmentalMaterialTerm"
    class_name: ClassVar[str] = "EnvironmentalMaterialTerm"
    class_model_uri: ClassVar[URIRef] = NMDC.EnvironmentalMaterialTerm

    id: Union[str, EnvironmentalMaterialTermId] = None
    type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnvironmentalMaterialTermId):
            self.id = EnvironmentalMaterialTermId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class ChemicalEntity(OntologyClass):
    """
    An atom or molecule that can be represented with a chemical formula. Include lipids, glycans, natural products,
    drugs. There may be different terms for distinct acid-base forms, protonation states
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["ChemicalEntity"]
    class_class_curie: ClassVar[str] = "nmdc:ChemicalEntity"
    class_name: ClassVar[str] = "ChemicalEntity"
    class_model_uri: ClassVar[URIRef] = NMDC.ChemicalEntity

    id: Union[str, ChemicalEntityId] = None
    type: Union[str, URIorCURIE] = None
    alternative_names: Optional[Union[str, List[str]]] = empty_list()
    chemical_formula: Optional[str] = None
    inchi: Optional[str] = None
    inchi_key: Optional[str] = None
    smiles: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalEntityId):
            self.id = ChemicalEntityId(self.id)

        if not isinstance(self.alternative_names, list):
            self.alternative_names = [self.alternative_names] if self.alternative_names is not None else []
        self.alternative_names = [v if isinstance(v, str) else str(v) for v in self.alternative_names]

        if self.chemical_formula is not None and not isinstance(self.chemical_formula, str):
            self.chemical_formula = str(self.chemical_formula)

        if self.inchi is not None and not isinstance(self.inchi, str):
            self.inchi = str(self.inchi)

        if self.inchi_key is not None and not isinstance(self.inchi_key, str):
            self.inchi_key = str(self.inchi_key)

        if not isinstance(self.smiles, list):
            self.smiles = [self.smiles] if self.smiles is not None else []
        self.smiles = [v if isinstance(v, str) else str(v) for v in self.smiles]

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class FunctionalAnnotationTerm(OntologyClass):
    """
    Abstract grouping class for any term/descriptor that can be applied to a functional unit of a genome (protein,
    ncRNA, complex).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["FunctionalAnnotationTerm"]
    class_class_curie: ClassVar[str] = "nmdc:FunctionalAnnotationTerm"
    class_name: ClassVar[str] = "FunctionalAnnotationTerm"
    class_model_uri: ClassVar[URIRef] = NMDC.FunctionalAnnotationTerm

    id: Union[str, FunctionalAnnotationTermId] = None
    type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class Pathway(FunctionalAnnotationTerm):
    """
    A pathway is a sequence of steps/reactions carried out by an organism or community of organisms
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["Pathway"]
    class_class_curie: ClassVar[str] = "nmdc:Pathway"
    class_name: ClassVar[str] = "Pathway"
    class_model_uri: ClassVar[URIRef] = NMDC.Pathway

    id: Union[str, PathwayId] = None
    type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PathwayId):
            self.id = PathwayId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class OrthologyGroup(FunctionalAnnotationTerm):
    """
    A set of genes or gene products in which all members are orthologous
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["OrthologyGroup"]
    class_class_curie: ClassVar[str] = "nmdc:OrthologyGroup"
    class_name: ClassVar[str] = "OrthologyGroup"
    class_model_uri: ClassVar[URIRef] = NMDC.OrthologyGroup

    id: Union[str, OrthologyGroupId] = None
    type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrthologyGroupId):
            self.id = OrthologyGroupId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class FailureCategorization(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["FailureCategorization"]
    class_class_curie: ClassVar[str] = "nmdc:FailureCategorization"
    class_name: ClassVar[str] = "FailureCategorization"
    class_model_uri: ClassVar[URIRef] = NMDC.FailureCategorization

    type: Union[str, URIorCURIE] = None
    qc_failure_what: Optional[Union[str, "FailureWhatEnum"]] = None
    qc_failure_where: Optional[Union[str, "FailureWhereEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)

        if self.qc_failure_what is not None and not isinstance(self.qc_failure_what, FailureWhatEnum):
            self.qc_failure_what = FailureWhatEnum(self.qc_failure_what)

        if self.qc_failure_where is not None and not isinstance(self.qc_failure_where, FailureWhereEnum):
            self.qc_failure_where = FailureWhereEnum(self.qc_failure_where)

        super().__post_init__(**kwargs)


@dataclass
class MaterialEntity(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["MaterialEntity"]
    class_class_curie: ClassVar[str] = "nmdc:MaterialEntity"
    class_name: ClassVar[str] = "MaterialEntity"
    class_model_uri: ClassVar[URIRef] = NMDC.MaterialEntity

    id: Union[str, MaterialEntityId] = None
    type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class Biosample(MaterialEntity):
    """
    Biological source material which can be characterized by an experiment.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["Biosample"]
    class_class_curie: ClassVar[str] = "nmdc:Biosample"
    class_name: ClassVar[str] = "Biosample"
    class_model_uri: ClassVar[URIRef] = NMDC.Biosample

    id: Union[str, BiosampleId] = None
    type: Union[str, URIorCURIE] = None
    associated_studies: Union[Union[str, StudyId], List[Union[str, StudyId]]] = None
    env_broad_scale: Union[dict, ControlledIdentifiedTermValue] = None
    env_local_scale: Union[dict, ControlledIdentifiedTermValue] = None
    env_medium: Union[dict, ControlledIdentifiedTermValue] = None
    biosample_categories: Optional[Union[Union[str, "BiosampleCategoryEnum"], List[Union[str, "BiosampleCategoryEnum"]]]] = empty_list()
    collected_from: Optional[Union[str, FieldResearchSiteId]] = None
    embargoed: Optional[Union[bool, Bool]] = None
    host_disease_stat: Optional[Union[dict, TextValue]] = None
    host_taxid: Optional[Union[dict, ControlledIdentifiedTermValue]] = None
    img_identifiers: Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]] = empty_list()
    neon_biosample_identifiers: Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]] = empty_list()
    samp_name: Optional[str] = None
    gold_biosample_identifiers: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    insdc_biosample_identifiers: Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]] = empty_list()
    emsl_biosample_identifiers: Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]] = empty_list()
    igsn_biosample_identifiers: Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]] = empty_list()
    abs_air_humidity: Optional[Union[dict, QuantityValue]] = None
    add_recov_method: Optional[Union[dict, TextValue]] = None
    additional_info: Optional[Union[dict, TextValue]] = None
    address: Optional[Union[dict, TextValue]] = None
    adj_room: Optional[Union[dict, TextValue]] = None
    aero_struc: Optional[Union[dict, TextValue]] = None
    agrochem_addition: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    air_PM_concen: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    air_temp: Optional[Union[dict, QuantityValue]] = None
    air_temp_regm: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    al_sat: Optional[Union[dict, QuantityValue]] = None
    al_sat_meth: Optional[Union[dict, TextValue]] = None
    alkalinity: Optional[Union[dict, QuantityValue]] = None
    alkalinity_method: Optional[Union[dict, TextValue]] = None
    alkyl_diethers: Optional[Union[dict, QuantityValue]] = None
    alt: Optional[Union[dict, QuantityValue]] = None
    aminopept_act: Optional[Union[dict, QuantityValue]] = None
    ammonium: Optional[Union[dict, QuantityValue]] = None
    ammonium_nitrogen: Optional[Union[dict, QuantityValue]] = None
    amount_light: Optional[Union[dict, QuantityValue]] = None
    ances_data: Optional[Union[dict, TextValue]] = None
    annual_precpt: Optional[Union[dict, QuantityValue]] = None
    annual_temp: Optional[Union[dict, QuantityValue]] = None
    antibiotic_regm: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    api: Optional[Union[dict, QuantityValue]] = None
    arch_struc: Optional[Union[str, "ArchStrucEnum"]] = None
    aromatics_pc: Optional[Union[dict, TextValue]] = None
    asphaltenes_pc: Optional[Union[dict, TextValue]] = None
    atmospheric_data: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    avg_dew_point: Optional[Union[dict, QuantityValue]] = None
    avg_occup: Optional[Union[dict, TextValue]] = None
    avg_temp: Optional[Union[dict, QuantityValue]] = None
    bac_prod: Optional[Union[dict, QuantityValue]] = None
    bac_resp: Optional[Union[dict, QuantityValue]] = None
    bacteria_carb_prod: Optional[Union[dict, QuantityValue]] = None
    barometric_press: Optional[Union[dict, QuantityValue]] = None
    basin: Optional[Union[dict, TextValue]] = None
    bathroom_count: Optional[Union[dict, TextValue]] = None
    bedroom_count: Optional[Union[dict, TextValue]] = None
    benzene: Optional[Union[dict, QuantityValue]] = None
    biochem_oxygen_dem: Optional[Union[dict, QuantityValue]] = None
    biocide: Optional[Union[dict, TextValue]] = None
    biocide_admin_method: Optional[Union[dict, TextValue]] = None
    biol_stat: Optional[Union[str, "BiolStatEnum"]] = None
    biomass: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    biotic_regm: Optional[Union[dict, TextValue]] = None
    biotic_relationship: Optional[Union[str, "BioticRelationshipEnum"]] = None
    bishomohopanol: Optional[Union[dict, QuantityValue]] = None
    blood_press_diast: Optional[Union[dict, QuantityValue]] = None
    blood_press_syst: Optional[Union[dict, QuantityValue]] = None
    bromide: Optional[Union[dict, QuantityValue]] = None
    build_docs: Optional[Union[str, "BuildDocsEnum"]] = None
    build_occup_type: Optional[Union[Union[str, "BuildOccupTypeEnum"], List[Union[str, "BuildOccupTypeEnum"]]]] = empty_list()
    building_setting: Optional[Union[str, "BuildingSettingEnum"]] = None
    built_struc_age: Optional[Union[dict, QuantityValue]] = None
    built_struc_set: Optional[Union[dict, TextValue]] = None
    built_struc_type: Optional[Union[dict, TextValue]] = None
    calcium: Optional[Union[dict, QuantityValue]] = None
    carb_dioxide: Optional[Union[dict, QuantityValue]] = None
    carb_monoxide: Optional[Union[dict, QuantityValue]] = None
    carb_nitro_ratio: Optional[Union[dict, QuantityValue]] = None
    ceil_area: Optional[Union[dict, QuantityValue]] = None
    ceil_cond: Optional[Union[str, "CeilCondEnum"]] = None
    ceil_finish_mat: Optional[Union[str, "CeilFinishMatEnum"]] = None
    ceil_struc: Optional[Union[dict, TextValue]] = None
    ceil_texture: Optional[Union[str, "CeilTextureEnum"]] = None
    ceil_thermal_mass: Optional[Union[dict, QuantityValue]] = None
    ceil_type: Optional[Union[str, "CeilTypeEnum"]] = None
    ceil_water_mold: Optional[Union[dict, TextValue]] = None
    chem_administration: Optional[Union[Union[dict, ControlledTermValue], List[Union[dict, ControlledTermValue]]]] = empty_list()
    chem_mutagen: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    chem_oxygen_dem: Optional[Union[dict, QuantityValue]] = None
    chem_treat_method: Optional[str] = None
    chem_treatment: Optional[Union[dict, TextValue]] = None
    chloride: Optional[Union[dict, QuantityValue]] = None
    chlorophyll: Optional[Union[dict, QuantityValue]] = None
    climate_environment: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    collection_date: Optional[Union[dict, TimestampValue]] = None
    conduc: Optional[Union[dict, QuantityValue]] = None
    cool_syst_id: Optional[Union[dict, TextValue]] = None
    core_field: Optional[str] = None
    crop_rotation: Optional[Union[dict, TextValue]] = None
    cult_root_med: Optional[Union[dict, TextValue]] = None
    cur_land_use: Optional[Union[str, "CurLandUseEnum"]] = None
    cur_vegetation: Optional[Union[dict, TextValue]] = None
    cur_vegetation_meth: Optional[Union[dict, TextValue]] = None
    date_last_rain: Optional[Union[dict, TimestampValue]] = None
    density: Optional[Union[dict, QuantityValue]] = None
    depos_env: Optional[Union[str, "DeposEnvEnum"]] = None
    depth: Optional[Union[dict, QuantityValue]] = None
    dew_point: Optional[Union[dict, QuantityValue]] = None
    diether_lipids: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    diss_carb_dioxide: Optional[Union[dict, QuantityValue]] = None
    diss_hydrogen: Optional[Union[dict, QuantityValue]] = None
    diss_inorg_carb: Optional[Union[dict, QuantityValue]] = None
    diss_inorg_nitro: Optional[Union[dict, QuantityValue]] = None
    diss_inorg_phosp: Optional[Union[dict, QuantityValue]] = None
    diss_iron: Optional[Union[dict, QuantityValue]] = None
    diss_org_carb: Optional[Union[dict, QuantityValue]] = None
    diss_org_nitro: Optional[Union[dict, QuantityValue]] = None
    diss_oxygen: Optional[Union[dict, QuantityValue]] = None
    diss_oxygen_fluid: Optional[Union[dict, QuantityValue]] = None
    dna_cont_well: Optional[str] = None
    door_comp_type: Optional[Union[str, "DoorCompTypeEnum"]] = None
    door_cond: Optional[Union[str, "DoorCondEnum"]] = None
    door_direct: Optional[Union[str, "DoorDirectEnum"]] = None
    door_loc: Optional[Union[str, "DoorLocEnum"]] = None
    door_mat: Optional[Union[str, "DoorMatEnum"]] = None
    door_move: Optional[Union[str, "DoorMoveEnum"]] = None
    door_size: Optional[Union[dict, QuantityValue]] = None
    door_type: Optional[Union[str, "DoorTypeEnum"]] = None
    door_type_metal: Optional[Union[str, "DoorTypeMetalEnum"]] = None
    door_type_wood: Optional[Union[str, "DoorTypeWoodEnum"]] = None
    door_water_mold: Optional[Union[dict, TextValue]] = None
    down_par: Optional[Union[dict, QuantityValue]] = None
    drainage_class: Optional[Union[str, "DrainageClassEnum"]] = None
    drawings: Optional[Union[str, "DrawingsEnum"]] = None
    ecosystem: Optional[str] = None
    ecosystem_category: Optional[str] = None
    ecosystem_subtype: Optional[str] = None
    ecosystem_type: Optional[str] = None
    efficiency_percent: Optional[Union[dict, QuantityValue]] = None
    elev: Optional[float] = None
    elevator: Optional[Union[dict, TextValue]] = None
    emulsions: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    env_package: Optional[Union[dict, TextValue]] = None
    environment_field: Optional[str] = None
    escalator: Optional[Union[dict, TextValue]] = None
    ethylbenzene: Optional[Union[dict, QuantityValue]] = None
    exp_duct: Optional[Union[dict, QuantityValue]] = None
    exp_pipe: Optional[Union[dict, QuantityValue]] = None
    experimental_factor: Optional[Union[dict, ControlledTermValue]] = None
    ext_door: Optional[Union[dict, TextValue]] = None
    ext_wall_orient: Optional[Union[str, "ExtWallOrientEnum"]] = None
    ext_window_orient: Optional[Union[str, "ExtWindowOrientEnum"]] = None
    extreme_event: Optional[str] = None
    fao_class: Optional[Union[str, "FaoClassEnum"]] = None
    fertilizer_regm: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    field: Optional[Union[dict, TextValue]] = None
    filter_type: Optional[Union[Union[str, "FilterTypeEnum"], List[Union[str, "FilterTypeEnum"]]]] = empty_list()
    fire: Optional[str] = None
    fireplace_type: Optional[Union[dict, TextValue]] = None
    flooding: Optional[str] = None
    floor_age: Optional[Union[dict, QuantityValue]] = None
    floor_area: Optional[Union[dict, QuantityValue]] = None
    floor_cond: Optional[Union[str, "FloorCondEnum"]] = None
    floor_count: Optional[Union[dict, TextValue]] = None
    floor_finish_mat: Optional[Union[str, "FloorFinishMatEnum"]] = None
    floor_struc: Optional[Union[str, "FloorStrucEnum"]] = None
    floor_thermal_mass: Optional[Union[dict, QuantityValue]] = None
    floor_water_mold: Optional[Union[str, "FloorWaterMoldEnum"]] = None
    fluor: Optional[Union[dict, QuantityValue]] = None
    freq_clean: Optional[Union[dict, QuantityValue]] = None
    freq_cook: Optional[Union[dict, QuantityValue]] = None
    fungicide_regm: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    furniture: Optional[Union[str, "FurnitureEnum"]] = None
    gaseous_environment: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    gaseous_substances: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    gender_restroom: Optional[Union[str, "GenderRestroomEnum"]] = None
    genetic_mod: Optional[Union[dict, TextValue]] = None
    geo_loc_name: Optional[Union[dict, TextValue]] = None
    glucosidase_act: Optional[Union[dict, QuantityValue]] = None
    gravidity: Optional[Union[dict, TextValue]] = None
    gravity: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    growth_facil: Optional[Union[dict, ControlledTermValue]] = None
    growth_habit: Optional[Union[str, "GrowthHabitEnum"]] = None
    growth_hormone_regm: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    hall_count: Optional[Union[dict, TextValue]] = None
    handidness: Optional[Union[str, "HandidnessEnum"]] = None
    hc_produced: Optional[Union[str, "HcProducedEnum"]] = None
    hcr: Optional[Union[str, "HcrEnum"]] = None
    hcr_fw_salinity: Optional[Union[dict, QuantityValue]] = None
    hcr_geol_age: Optional[Union[str, "HcrGeolAgeEnum"]] = None
    hcr_pressure: Optional[Union[dict, TextValue]] = None
    hcr_temp: Optional[Union[dict, TextValue]] = None
    heat_cool_type: Optional[Union[Union[str, "HeatCoolTypeEnum"], List[Union[str, "HeatCoolTypeEnum"]]]] = empty_list()
    heat_deliv_loc: Optional[Union[str, "HeatDelivLocEnum"]] = None
    heat_sys_deliv_meth: Optional[str] = None
    heat_system_id: Optional[Union[dict, TextValue]] = None
    heavy_metals: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    heavy_metals_meth: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    height_carper_fiber: Optional[Union[dict, QuantityValue]] = None
    herbicide_regm: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    horizon_meth: Optional[Union[dict, TextValue]] = None
    host_age: Optional[Union[dict, QuantityValue]] = None
    host_body_habitat: Optional[Union[dict, TextValue]] = None
    host_body_product: Optional[Union[dict, ControlledTermValue]] = None
    host_body_site: Optional[Union[dict, ControlledTermValue]] = None
    host_body_temp: Optional[Union[dict, QuantityValue]] = None
    host_color: Optional[Union[dict, TextValue]] = None
    host_common_name: Optional[Union[dict, TextValue]] = None
    host_diet: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    host_dry_mass: Optional[Union[dict, QuantityValue]] = None
    host_family_relation: Optional[Union[str, List[str]]] = empty_list()
    host_genotype: Optional[Union[dict, TextValue]] = None
    host_growth_cond: Optional[Union[dict, TextValue]] = None
    host_height: Optional[Union[dict, QuantityValue]] = None
    host_last_meal: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    host_length: Optional[Union[dict, QuantityValue]] = None
    host_life_stage: Optional[Union[dict, TextValue]] = None
    host_phenotype: Optional[Union[dict, ControlledTermValue]] = None
    host_sex: Optional[Union[str, "HostSexEnum"]] = None
    host_shape: Optional[Union[dict, TextValue]] = None
    host_subject_id: Optional[Union[dict, TextValue]] = None
    host_subspecf_genlin: Optional[Union[str, List[str]]] = empty_list()
    host_substrate: Optional[Union[dict, TextValue]] = None
    host_symbiont: Optional[Union[str, List[str]]] = empty_list()
    host_tot_mass: Optional[Union[dict, QuantityValue]] = None
    host_wet_mass: Optional[Union[dict, QuantityValue]] = None
    humidity: Optional[Union[dict, QuantityValue]] = None
    humidity_regm: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    indoor_space: Optional[Union[str, "IndoorSpaceEnum"]] = None
    indoor_surf: Optional[Union[str, "IndoorSurfEnum"]] = None
    indust_eff_percent: Optional[Union[dict, QuantityValue]] = None
    inorg_particles: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    inside_lux: Optional[Union[dict, QuantityValue]] = None
    int_wall_cond: Optional[Union[str, "IntWallCondEnum"]] = None
    investigation_field: Optional[str] = None
    iw_bt_date_well: Optional[Union[dict, TimestampValue]] = None
    iwf: Optional[Union[dict, QuantityValue]] = None
    last_clean: Optional[Union[dict, TimestampValue]] = None
    lat_lon: Optional[Union[dict, GeolocationValue]] = None
    lbc_thirty: Optional[Union[dict, QuantityValue]] = None
    lbceq: Optional[Union[dict, QuantityValue]] = None
    light_intensity: Optional[Union[dict, QuantityValue]] = None
    light_regm: Optional[Union[dict, TextValue]] = None
    light_type: Optional[Union[Union[str, "LightTypeEnum"], List[Union[str, "LightTypeEnum"]]]] = empty_list()
    link_addit_analys: Optional[Union[dict, TextValue]] = None
    link_class_info: Optional[Union[dict, TextValue]] = None
    link_climate_info: Optional[Union[dict, TextValue]] = None
    lithology: Optional[Union[str, "LithologyEnum"]] = None
    local_class: Optional[Union[dict, TextValue]] = None
    local_class_meth: Optional[Union[dict, TextValue]] = None
    magnesium: Optional[Union[dict, QuantityValue]] = None
    manganese: Optional[Union[dict, QuantityValue]] = None
    max_occup: Optional[Union[dict, QuantityValue]] = None
    mean_frict_vel: Optional[Union[dict, QuantityValue]] = None
    mean_peak_frict_vel: Optional[Union[dict, QuantityValue]] = None
    mech_struc: Optional[Union[str, "MechStrucEnum"]] = None
    mechanical_damage: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    methane: Optional[Union[dict, QuantityValue]] = None
    micro_biomass_meth: Optional[str] = None
    microbial_biomass: Optional[Union[dict, QuantityValue]] = None
    mineral_nutr_regm: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    misc_param: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    n_alkanes: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    nitrate: Optional[Union[dict, QuantityValue]] = None
    nitrate_nitrogen: Optional[Union[dict, QuantityValue]] = None
    nitrite: Optional[Union[dict, QuantityValue]] = None
    nitrite_nitrogen: Optional[Union[dict, QuantityValue]] = None
    nitro: Optional[Union[dict, QuantityValue]] = None
    non_min_nutr_regm: Optional[Union[str, List[str]]] = empty_list()
    nucleic_acid_sequence_source_field: Optional[str] = None
    number_pets: Optional[Union[dict, QuantityValue]] = None
    number_plants: Optional[Union[dict, QuantityValue]] = None
    number_resident: Optional[Union[dict, QuantityValue]] = None
    occup_density_samp: Optional[Union[dict, QuantityValue]] = None
    occup_document: Optional[Union[str, "OccupDocumentEnum"]] = None
    occup_samp: Optional[Union[dict, QuantityValue]] = None
    org_carb: Optional[Union[dict, QuantityValue]] = None
    org_count_qpcr_info: Optional[str] = None
    org_matter: Optional[Union[dict, QuantityValue]] = None
    org_nitro: Optional[Union[dict, QuantityValue]] = None
    org_particles: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    organism_count: Optional[Union[Union[dict, QuantityValue], List[Union[dict, QuantityValue]]]] = empty_list()
    owc_tvdss: Optional[Union[dict, QuantityValue]] = None
    oxy_stat_samp: Optional[Union[str, "OxyStatSampEnum"]] = None
    oxygen: Optional[Union[dict, QuantityValue]] = None
    part_org_carb: Optional[Union[dict, QuantityValue]] = None
    part_org_nitro: Optional[Union[dict, QuantityValue]] = None
    particle_class: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    permeability: Optional[Union[dict, TextValue]] = None
    perturbation: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    pesticide_regm: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    petroleum_hydrocarb: Optional[Union[dict, QuantityValue]] = None
    ph: Optional[float] = None
    ph_meth: Optional[Union[dict, TextValue]] = None
    ph_regm: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    phaeopigments: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    phosphate: Optional[Union[dict, QuantityValue]] = None
    phosplipid_fatt_acid: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    photon_flux: Optional[Union[dict, QuantityValue]] = None
    plant_growth_med: Optional[Union[dict, ControlledTermValue]] = None
    plant_product: Optional[Union[dict, TextValue]] = None
    plant_sex: Optional[Union[str, "PlantSexEnum"]] = None
    plant_struc: Optional[Union[dict, ControlledTermValue]] = None
    pollutants: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    porosity: Optional[Union[dict, TextValue]] = None
    potassium: Optional[Union[dict, QuantityValue]] = None
    pour_point: Optional[Union[dict, QuantityValue]] = None
    pre_treatment: Optional[Union[dict, TextValue]] = None
    pres_animal_insect: Optional[str] = None
    pressure: Optional[Union[dict, QuantityValue]] = None
    prev_land_use_meth: Optional[str] = None
    previous_land_use: Optional[Union[dict, TextValue]] = None
    primary_prod: Optional[Union[dict, QuantityValue]] = None
    primary_treatment: Optional[Union[dict, TextValue]] = None
    prod_rate: Optional[Union[dict, QuantityValue]] = None
    prod_start_date: Optional[Union[dict, TimestampValue]] = None
    profile_position: Optional[Union[str, "ProfilePositionEnum"]] = None
    quad_pos: Optional[Union[str, "QuadPosEnum"]] = None
    radiation_regm: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    rainfall_regm: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    reactor_type: Optional[Union[dict, TextValue]] = None
    redox_potential: Optional[Union[dict, QuantityValue]] = None
    rel_air_humidity: Optional[Union[dict, QuantityValue]] = None
    rel_humidity_out: Optional[Union[dict, QuantityValue]] = None
    rel_samp_loc: Optional[Union[str, "RelSampLocEnum"]] = None
    reservoir: Optional[Union[dict, TextValue]] = None
    resins_pc: Optional[Union[dict, TextValue]] = None
    room_air_exch_rate: Optional[Union[dict, QuantityValue]] = None
    room_architec_elem: Optional[str] = None
    room_condt: Optional[Union[str, "RoomCondtEnum"]] = None
    room_connected: Optional[Union[str, "RoomConnectedEnum"]] = None
    room_count: Optional[Union[dict, TextValue]] = None
    room_dim: Optional[Union[dict, TextValue]] = None
    room_door_dist: Optional[Union[dict, TextValue]] = None
    room_door_share: Optional[Union[dict, TextValue]] = None
    room_hallway: Optional[Union[dict, TextValue]] = None
    room_loc: Optional[Union[str, "RoomLocEnum"]] = None
    room_moist_dam_hist: Optional[int] = None
    room_net_area: Optional[Union[dict, TextValue]] = None
    room_occup: Optional[Union[dict, QuantityValue]] = None
    room_samp_pos: Optional[Union[str, "RoomSampPosEnum"]] = None
    room_type: Optional[Union[str, "RoomTypeEnum"]] = None
    room_vol: Optional[Union[dict, TextValue]] = None
    room_wall_share: Optional[Union[dict, TextValue]] = None
    room_window_count: Optional[int] = None
    root_cond: Optional[Union[dict, TextValue]] = None
    root_med_carbon: Optional[Union[dict, TextValue]] = None
    root_med_macronutr: Optional[Union[dict, TextValue]] = None
    root_med_micronutr: Optional[Union[dict, TextValue]] = None
    root_med_ph: Optional[Union[dict, QuantityValue]] = None
    root_med_regl: Optional[Union[dict, TextValue]] = None
    root_med_solid: Optional[Union[dict, TextValue]] = None
    root_med_suppl: Optional[Union[dict, TextValue]] = None
    salinity: Optional[Union[dict, QuantityValue]] = None
    salinity_meth: Optional[Union[dict, TextValue]] = None
    salt_regm: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    samp_capt_status: Optional[Union[str, "SampCaptStatusEnum"]] = None
    samp_collec_device: Optional[str] = None
    samp_collec_method: Optional[str] = None
    samp_collect_point: Optional[Union[str, "SampCollectPointEnum"]] = None
    samp_dis_stage: Optional[Union[str, "SampDisStageEnum"]] = None
    samp_floor: Optional[Union[str, "SampFloorEnum"]] = None
    samp_loc_corr_rate: Optional[Union[dict, TextValue]] = None
    samp_mat_process: Optional[Union[dict, ControlledTermValue]] = None
    samp_md: Optional[Union[dict, QuantityValue]] = None
    samp_preserv: Optional[Union[dict, TextValue]] = None
    samp_room_id: Optional[Union[dict, TextValue]] = None
    samp_size: Optional[Union[dict, QuantityValue]] = None
    samp_sort_meth: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    samp_store_dur: Optional[Union[dict, TextValue]] = None
    samp_store_loc: Optional[Union[dict, TextValue]] = None
    samp_store_temp: Optional[Union[dict, QuantityValue]] = None
    samp_subtype: Optional[Union[str, "SampSubtypeEnum"]] = None
    samp_taxon_id: Optional[Union[dict, ControlledIdentifiedTermValue]] = None
    samp_time_out: Optional[Union[dict, TextValue]] = None
    samp_transport_cond: Optional[Union[dict, TextValue]] = None
    samp_tvdss: Optional[Union[dict, TextValue]] = None
    samp_type: Optional[Union[dict, TextValue]] = None
    samp_weather: Optional[Union[str, "SampWeatherEnum"]] = None
    samp_well_name: Optional[Union[dict, TextValue]] = None
    saturates_pc: Optional[Union[dict, TextValue]] = None
    season: Optional[Union[dict, TextValue]] = None
    season_environment: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    season_precpt: Optional[Union[dict, QuantityValue]] = None
    season_temp: Optional[Union[dict, QuantityValue]] = None
    season_use: Optional[Union[str, "SeasonUseEnum"]] = None
    secondary_treatment: Optional[Union[dict, TextValue]] = None
    sediment_type: Optional[Union[str, "SedimentTypeEnum"]] = None
    sequencing_field: Optional[str] = None
    sewage_type: Optional[Union[dict, TextValue]] = None
    shad_dev_water_mold: Optional[str] = None
    shading_device_cond: Optional[Union[str, "ShadingDeviceCondEnum"]] = None
    shading_device_loc: Optional[Union[dict, TextValue]] = None
    shading_device_mat: Optional[Union[dict, TextValue]] = None
    shading_device_type: Optional[Union[str, "ShadingDeviceTypeEnum"]] = None
    sieving: Optional[Union[dict, TextValue]] = None
    silicate: Optional[Union[dict, QuantityValue]] = None
    size_frac: Optional[Union[dict, TextValue]] = None
    size_frac_low: Optional[Union[dict, QuantityValue]] = None
    size_frac_up: Optional[Union[dict, QuantityValue]] = None
    slope_aspect: Optional[Union[dict, QuantityValue]] = None
    slope_gradient: Optional[Union[dict, QuantityValue]] = None
    sludge_retent_time: Optional[Union[dict, QuantityValue]] = None
    sodium: Optional[Union[dict, QuantityValue]] = None
    soil_horizon: Optional[Union[str, "SoilHorizonEnum"]] = None
    soil_text_measure: Optional[Union[dict, QuantityValue]] = None
    soil_texture_meth: Optional[str] = None
    soil_type: Optional[Union[dict, TextValue]] = None
    soil_type_meth: Optional[Union[dict, TextValue]] = None
    solar_irradiance: Optional[Union[dict, QuantityValue]] = None
    soluble_inorg_mat: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    soluble_org_mat: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    soluble_react_phosp: Optional[Union[dict, QuantityValue]] = None
    source_mat_id: Optional[Union[dict, TextValue]] = None
    space_typ_state: Optional[Union[dict, TextValue]] = None
    specific: Optional[Union[str, "SpecificEnum"]] = None
    specific_ecosystem: Optional[str] = None
    specific_humidity: Optional[Union[dict, QuantityValue]] = None
    sr_dep_env: Optional[Union[str, "SrDepEnvEnum"]] = None
    sr_geol_age: Optional[Union[str, "SrGeolAgeEnum"]] = None
    sr_kerog_type: Optional[Union[str, "SrKerogTypeEnum"]] = None
    sr_lithology: Optional[Union[str, "SrLithologyEnum"]] = None
    standing_water_regm: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    store_cond: Optional[Union[dict, TextValue]] = None
    substructure_type: Optional[Union[Union[str, "SubstructureTypeEnum"], List[Union[str, "SubstructureTypeEnum"]]]] = empty_list()
    sulfate: Optional[Union[dict, QuantityValue]] = None
    sulfate_fw: Optional[Union[dict, QuantityValue]] = None
    sulfide: Optional[Union[dict, QuantityValue]] = None
    surf_air_cont: Optional[Union[Union[str, "SurfAirContEnum"], List[Union[str, "SurfAirContEnum"]]]] = empty_list()
    surf_humidity: Optional[Union[dict, QuantityValue]] = None
    surf_material: Optional[Union[str, "SurfMaterialEnum"]] = None
    surf_moisture: Optional[Union[dict, QuantityValue]] = None
    surf_moisture_ph: Optional[float] = None
    surf_temp: Optional[Union[dict, QuantityValue]] = None
    suspend_part_matter: Optional[Union[dict, QuantityValue]] = None
    suspend_solids: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    tan: Optional[Union[dict, QuantityValue]] = None
    temp: Optional[Union[dict, QuantityValue]] = None
    temp_out: Optional[Union[dict, QuantityValue]] = None
    tertiary_treatment: Optional[Union[dict, TextValue]] = None
    tidal_stage: Optional[Union[str, "TidalStageEnum"]] = None
    tillage: Optional[Union[Union[str, "TillageEnum"], List[Union[str, "TillageEnum"]]]] = empty_list()
    tiss_cult_growth_med: Optional[Union[dict, TextValue]] = None
    toluene: Optional[Union[dict, QuantityValue]] = None
    tot_carb: Optional[Union[dict, QuantityValue]] = None
    tot_depth_water_col: Optional[Union[dict, QuantityValue]] = None
    tot_diss_nitro: Optional[Union[dict, QuantityValue]] = None
    tot_inorg_nitro: Optional[Union[dict, QuantityValue]] = None
    tot_iron: Optional[Union[dict, QuantityValue]] = None
    tot_nitro: Optional[Union[dict, QuantityValue]] = None
    tot_nitro_cont_meth: Optional[str] = None
    tot_nitro_content: Optional[Union[dict, QuantityValue]] = None
    tot_org_c_meth: Optional[Union[dict, TextValue]] = None
    tot_org_carb: Optional[Union[dict, QuantityValue]] = None
    tot_part_carb: Optional[Union[dict, QuantityValue]] = None
    tot_phosp: Optional[Union[dict, QuantityValue]] = None
    tot_phosphate: Optional[Union[dict, QuantityValue]] = None
    tot_sulfur: Optional[Union[dict, QuantityValue]] = None
    train_line: Optional[Union[str, "TrainLineEnum"]] = None
    train_stat_loc: Optional[Union[str, "TrainStatLocEnum"]] = None
    train_stop_loc: Optional[Union[str, "TrainStopLocEnum"]] = None
    turbidity: Optional[Union[dict, QuantityValue]] = None
    tvdss_of_hcr_press: Optional[Union[dict, QuantityValue]] = None
    tvdss_of_hcr_temp: Optional[Union[dict, QuantityValue]] = None
    typ_occup_density: Optional[float] = None
    ventilation_rate: Optional[Union[dict, QuantityValue]] = None
    ventilation_type: Optional[Union[dict, TextValue]] = None
    vfa: Optional[Union[dict, QuantityValue]] = None
    vfa_fw: Optional[Union[dict, QuantityValue]] = None
    vis_media: Optional[Union[str, "VisMediaEnum"]] = None
    viscosity: Optional[Union[dict, TextValue]] = None
    volatile_org_comp: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    wall_area: Optional[Union[dict, QuantityValue]] = None
    wall_const_type: Optional[Union[str, "WallConstTypeEnum"]] = None
    wall_finish_mat: Optional[Union[str, "WallFinishMatEnum"]] = None
    wall_height: Optional[Union[dict, QuantityValue]] = None
    wall_loc: Optional[Union[str, "WallLocEnum"]] = None
    wall_surf_treatment: Optional[Union[str, "WallSurfTreatmentEnum"]] = None
    wall_texture: Optional[Union[str, "WallTextureEnum"]] = None
    wall_thermal_mass: Optional[Union[dict, QuantityValue]] = None
    wall_water_mold: Optional[Union[dict, TextValue]] = None
    wastewater_type: Optional[Union[dict, TextValue]] = None
    water_cont_soil_meth: Optional[str] = None
    water_content: Optional[Union[str, List[str]]] = empty_list()
    water_current: Optional[Union[dict, QuantityValue]] = None
    water_cut: Optional[Union[dict, QuantityValue]] = None
    water_feat_size: Optional[Union[dict, QuantityValue]] = None
    water_feat_type: Optional[Union[str, "WaterFeatTypeEnum"]] = None
    water_prod_rate: Optional[Union[dict, QuantityValue]] = None
    water_temp_regm: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    watering_regm: Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]] = empty_list()
    weekday: Optional[Union[str, "WeekdayEnum"]] = None
    win: Optional[Union[dict, TextValue]] = None
    wind_direction: Optional[Union[dict, TextValue]] = None
    wind_speed: Optional[Union[dict, QuantityValue]] = None
    window_cond: Optional[Union[str, "WindowCondEnum"]] = None
    window_cover: Optional[Union[str, "WindowCoverEnum"]] = None
    window_horiz_pos: Optional[Union[str, "WindowHorizPosEnum"]] = None
    window_loc: Optional[Union[str, "WindowLocEnum"]] = None
    window_mat: Optional[Union[str, "WindowMatEnum"]] = None
    window_open_freq: Optional[Union[dict, TextValue]] = None
    window_size: Optional[Union[dict, TextValue]] = None
    window_status: Optional[Union[dict, TextValue]] = None
    window_type: Optional[Union[str, "WindowTypeEnum"]] = None
    window_vert_pos: Optional[Union[str, "WindowVertPosEnum"]] = None
    window_water_mold: Optional[Union[dict, TextValue]] = None
    xylene: Optional[Union[dict, QuantityValue]] = None
    zinc: Optional[Union[dict, QuantityValue]] = None
    add_date: Optional[str] = None
    community: Optional[str] = None
    habitat: Optional[str] = None
    host_name: Optional[str] = None
    location: Optional[str] = None
    mod_date: Optional[str] = None
    ncbi_taxonomy_name: Optional[str] = None
    proport_woa_temperature: Optional[str] = None
    salinity_category: Optional[str] = None
    sample_collection_site: Optional[str] = None
    soluble_iron_micromol: Optional[str] = None
    subsurface_depth: Optional[Union[dict, QuantityValue]] = None
    dna_absorb1: Optional[float] = None
    dna_absorb2: Optional[float] = None
    dna_collect_site: Optional[str] = None
    dna_concentration: Optional[float] = None
    dna_cont_type: Optional[Union[str, "JgiContTypeEnum"]] = None
    dna_container_id: Optional[str] = None
    dna_dnase: Optional[Union[str, "YesNoEnum"]] = None
    dna_isolate_meth: Optional[str] = None
    dna_organisms: Optional[str] = None
    dna_project_contact: Optional[str] = None
    dna_samp_id: Optional[str] = None
    dna_sample_format: Optional[Union[str, "DNASampleFormatEnum"]] = None
    dna_sample_name: Optional[str] = None
    dna_seq_project: Optional[str] = None
    dna_seq_project_pi: Optional[str] = None
    dna_seq_project_name: Optional[str] = None
    dna_volume: Optional[float] = None
    proposal_dna: Optional[str] = None
    dnase_rna: Optional[Union[str, "YesNoEnum"]] = None
    proposal_rna: Optional[str] = None
    rna_absorb1: Optional[float] = None
    rna_absorb2: Optional[float] = None
    rna_collect_site: Optional[str] = None
    rna_concentration: Optional[float] = None
    rna_cont_type: Optional[Union[str, "JgiContTypeEnum"]] = None
    rna_cont_well: Optional[str] = None
    rna_container_id: Optional[str] = None
    rna_isolate_meth: Optional[str] = None
    rna_organisms: Optional[str] = None
    rna_project_contact: Optional[str] = None
    rna_samp_id: Optional[str] = None
    rna_sample_format: Optional[Union[str, "RNASampleFormatEnum"]] = None
    rna_sample_name: Optional[str] = None
    rna_seq_project: Optional[str] = None
    rna_seq_project_pi: Optional[str] = None
    rna_seq_project_name: Optional[str] = None
    rna_volume: Optional[float] = None
    collection_date_inc: Optional[str] = None
    collection_time: Optional[str] = None
    collection_time_inc: Optional[str] = None
    experimental_factor_other: Optional[str] = None
    filter_method: Optional[str] = None
    isotope_exposure: Optional[str] = None
    micro_biomass_c_meth: Optional[str] = None
    micro_biomass_n_meth: Optional[str] = None
    microbial_biomass_c: Optional[str] = None
    microbial_biomass_n: Optional[str] = None
    non_microb_biomass: Optional[str] = None
    non_microb_biomass_method: Optional[str] = None
    org_nitro_method: Optional[str] = None
    other_treatment: Optional[str] = None
    start_date_inc: Optional[str] = None
    start_time_inc: Optional[str] = None
    project_id: Optional[str] = None
    replicate_number: Optional[str] = None
    sample_shipped: Optional[str] = None
    sample_type: Optional[Union[str, "SampleTypeEnum"]] = None
    technical_reps: Optional[str] = None
    analysis_type: Optional[Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]]] = empty_list()
    sample_link: Optional[Union[str, List[str]]] = empty_list()
    bulk_elect_conductivity: Optional[Union[dict, QuantityValue]] = None
    infiltrations: Optional[Union[str, List[str]]] = empty_list()
    alternative_identifiers: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiosampleId):
            self.id = BiosampleId(self.id)

        if self._is_empty(self.associated_studies):
            self.MissingRequiredField("associated_studies")
        if not isinstance(self.associated_studies, list):
            self.associated_studies = [self.associated_studies] if self.associated_studies is not None else []
        self.associated_studies = [v if isinstance(v, StudyId) else StudyId(v) for v in self.associated_studies]

        if self._is_empty(self.env_broad_scale):
            self.MissingRequiredField("env_broad_scale")
        if not isinstance(self.env_broad_scale, ControlledIdentifiedTermValue):
            self.env_broad_scale = ControlledIdentifiedTermValue(**as_dict(self.env_broad_scale))

        if self._is_empty(self.env_local_scale):
            self.MissingRequiredField("env_local_scale")
        if not isinstance(self.env_local_scale, ControlledIdentifiedTermValue):
            self.env_local_scale = ControlledIdentifiedTermValue(**as_dict(self.env_local_scale))

        if self._is_empty(self.env_medium):
            self.MissingRequiredField("env_medium")
        if not isinstance(self.env_medium, ControlledIdentifiedTermValue):
            self.env_medium = ControlledIdentifiedTermValue(**as_dict(self.env_medium))

        if not isinstance(self.biosample_categories, list):
            self.biosample_categories = [self.biosample_categories] if self.biosample_categories is not None else []
        self.biosample_categories = [v if isinstance(v, BiosampleCategoryEnum) else BiosampleCategoryEnum(v) for v in self.biosample_categories]

        if self.collected_from is not None and not isinstance(self.collected_from, FieldResearchSiteId):
            self.collected_from = FieldResearchSiteId(self.collected_from)

        if self.embargoed is not None and not isinstance(self.embargoed, Bool):
            self.embargoed = Bool(self.embargoed)

        if self.host_disease_stat is not None and not isinstance(self.host_disease_stat, TextValue):
            self.host_disease_stat = TextValue(**as_dict(self.host_disease_stat))

        if self.host_taxid is not None and not isinstance(self.host_taxid, ControlledIdentifiedTermValue):
            self.host_taxid = ControlledIdentifiedTermValue(**as_dict(self.host_taxid))

        if not isinstance(self.img_identifiers, list):
            self.img_identifiers = [self.img_identifiers] if self.img_identifiers is not None else []
        self.img_identifiers = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(v) for v in self.img_identifiers]

        if not isinstance(self.neon_biosample_identifiers, list):
            self.neon_biosample_identifiers = [self.neon_biosample_identifiers] if self.neon_biosample_identifiers is not None else []
        self.neon_biosample_identifiers = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(v) for v in self.neon_biosample_identifiers]

        if self.samp_name is not None and not isinstance(self.samp_name, str):
            self.samp_name = str(self.samp_name)

        if not isinstance(self.gold_biosample_identifiers, list):
            self.gold_biosample_identifiers = [self.gold_biosample_identifiers] if self.gold_biosample_identifiers is not None else []
        self.gold_biosample_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.gold_biosample_identifiers]

        if not isinstance(self.insdc_biosample_identifiers, list):
            self.insdc_biosample_identifiers = [self.insdc_biosample_identifiers] if self.insdc_biosample_identifiers is not None else []
        self.insdc_biosample_identifiers = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(v) for v in self.insdc_biosample_identifiers]

        if not isinstance(self.emsl_biosample_identifiers, list):
            self.emsl_biosample_identifiers = [self.emsl_biosample_identifiers] if self.emsl_biosample_identifiers is not None else []
        self.emsl_biosample_identifiers = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(v) for v in self.emsl_biosample_identifiers]

        if not isinstance(self.igsn_biosample_identifiers, list):
            self.igsn_biosample_identifiers = [self.igsn_biosample_identifiers] if self.igsn_biosample_identifiers is not None else []
        self.igsn_biosample_identifiers = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(v) for v in self.igsn_biosample_identifiers]

        if self.abs_air_humidity is not None and not isinstance(self.abs_air_humidity, QuantityValue):
            self.abs_air_humidity = QuantityValue(**as_dict(self.abs_air_humidity))

        if self.add_recov_method is not None and not isinstance(self.add_recov_method, TextValue):
            self.add_recov_method = TextValue(**as_dict(self.add_recov_method))

        if self.additional_info is not None and not isinstance(self.additional_info, TextValue):
            self.additional_info = TextValue(**as_dict(self.additional_info))

        if self.address is not None and not isinstance(self.address, TextValue):
            self.address = TextValue(**as_dict(self.address))

        if self.adj_room is not None and not isinstance(self.adj_room, TextValue):
            self.adj_room = TextValue(**as_dict(self.adj_room))

        if self.aero_struc is not None and not isinstance(self.aero_struc, TextValue):
            self.aero_struc = TextValue(**as_dict(self.aero_struc))

        if not isinstance(self.agrochem_addition, list):
            self.agrochem_addition = [self.agrochem_addition] if self.agrochem_addition is not None else []
        self.agrochem_addition = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.agrochem_addition]

        if not isinstance(self.air_PM_concen, list):
            self.air_PM_concen = [self.air_PM_concen] if self.air_PM_concen is not None else []
        self.air_PM_concen = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.air_PM_concen]

        if self.air_temp is not None and not isinstance(self.air_temp, QuantityValue):
            self.air_temp = QuantityValue(**as_dict(self.air_temp))

        if not isinstance(self.air_temp_regm, list):
            self.air_temp_regm = [self.air_temp_regm] if self.air_temp_regm is not None else []
        self.air_temp_regm = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.air_temp_regm]

        if self.al_sat is not None and not isinstance(self.al_sat, QuantityValue):
            self.al_sat = QuantityValue(**as_dict(self.al_sat))

        if self.al_sat_meth is not None and not isinstance(self.al_sat_meth, TextValue):
            self.al_sat_meth = TextValue(**as_dict(self.al_sat_meth))

        if self.alkalinity is not None and not isinstance(self.alkalinity, QuantityValue):
            self.alkalinity = QuantityValue(**as_dict(self.alkalinity))

        if self.alkalinity_method is not None and not isinstance(self.alkalinity_method, TextValue):
            self.alkalinity_method = TextValue(**as_dict(self.alkalinity_method))

        if self.alkyl_diethers is not None and not isinstance(self.alkyl_diethers, QuantityValue):
            self.alkyl_diethers = QuantityValue(**as_dict(self.alkyl_diethers))

        if self.alt is not None and not isinstance(self.alt, QuantityValue):
            self.alt = QuantityValue(**as_dict(self.alt))

        if self.aminopept_act is not None and not isinstance(self.aminopept_act, QuantityValue):
            self.aminopept_act = QuantityValue(**as_dict(self.aminopept_act))

        if self.ammonium is not None and not isinstance(self.ammonium, QuantityValue):
            self.ammonium = QuantityValue(**as_dict(self.ammonium))

        if self.ammonium_nitrogen is not None and not isinstance(self.ammonium_nitrogen, QuantityValue):
            self.ammonium_nitrogen = QuantityValue(**as_dict(self.ammonium_nitrogen))

        if self.amount_light is not None and not isinstance(self.amount_light, QuantityValue):
            self.amount_light = QuantityValue(**as_dict(self.amount_light))

        if self.ances_data is not None and not isinstance(self.ances_data, TextValue):
            self.ances_data = TextValue(**as_dict(self.ances_data))

        if self.annual_precpt is not None and not isinstance(self.annual_precpt, QuantityValue):
            self.annual_precpt = QuantityValue(**as_dict(self.annual_precpt))

        if self.annual_temp is not None and not isinstance(self.annual_temp, QuantityValue):
            self.annual_temp = QuantityValue(**as_dict(self.annual_temp))

        if not isinstance(self.antibiotic_regm, list):
            self.antibiotic_regm = [self.antibiotic_regm] if self.antibiotic_regm is not None else []
        self.antibiotic_regm = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.antibiotic_regm]

        if self.api is not None and not isinstance(self.api, QuantityValue):
            self.api = QuantityValue(**as_dict(self.api))

        if self.arch_struc is not None and not isinstance(self.arch_struc, ArchStrucEnum):
            self.arch_struc = ArchStrucEnum(self.arch_struc)

        if self.aromatics_pc is not None and not isinstance(self.aromatics_pc, TextValue):
            self.aromatics_pc = TextValue(**as_dict(self.aromatics_pc))

        if self.asphaltenes_pc is not None and not isinstance(self.asphaltenes_pc, TextValue):
            self.asphaltenes_pc = TextValue(**as_dict(self.asphaltenes_pc))

        if not isinstance(self.atmospheric_data, list):
            self.atmospheric_data = [self.atmospheric_data] if self.atmospheric_data is not None else []
        self.atmospheric_data = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.atmospheric_data]

        if self.avg_dew_point is not None and not isinstance(self.avg_dew_point, QuantityValue):
            self.avg_dew_point = QuantityValue(**as_dict(self.avg_dew_point))

        if self.avg_occup is not None and not isinstance(self.avg_occup, TextValue):
            self.avg_occup = TextValue(**as_dict(self.avg_occup))

        if self.avg_temp is not None and not isinstance(self.avg_temp, QuantityValue):
            self.avg_temp = QuantityValue(**as_dict(self.avg_temp))

        if self.bac_prod is not None and not isinstance(self.bac_prod, QuantityValue):
            self.bac_prod = QuantityValue(**as_dict(self.bac_prod))

        if self.bac_resp is not None and not isinstance(self.bac_resp, QuantityValue):
            self.bac_resp = QuantityValue(**as_dict(self.bac_resp))

        if self.bacteria_carb_prod is not None and not isinstance(self.bacteria_carb_prod, QuantityValue):
            self.bacteria_carb_prod = QuantityValue(**as_dict(self.bacteria_carb_prod))

        if self.barometric_press is not None and not isinstance(self.barometric_press, QuantityValue):
            self.barometric_press = QuantityValue(**as_dict(self.barometric_press))

        if self.basin is not None and not isinstance(self.basin, TextValue):
            self.basin = TextValue(**as_dict(self.basin))

        if self.bathroom_count is not None and not isinstance(self.bathroom_count, TextValue):
            self.bathroom_count = TextValue(**as_dict(self.bathroom_count))

        if self.bedroom_count is not None and not isinstance(self.bedroom_count, TextValue):
            self.bedroom_count = TextValue(**as_dict(self.bedroom_count))

        if self.benzene is not None and not isinstance(self.benzene, QuantityValue):
            self.benzene = QuantityValue(**as_dict(self.benzene))

        if self.biochem_oxygen_dem is not None and not isinstance(self.biochem_oxygen_dem, QuantityValue):
            self.biochem_oxygen_dem = QuantityValue(**as_dict(self.biochem_oxygen_dem))

        if self.biocide is not None and not isinstance(self.biocide, TextValue):
            self.biocide = TextValue(**as_dict(self.biocide))

        if self.biocide_admin_method is not None and not isinstance(self.biocide_admin_method, TextValue):
            self.biocide_admin_method = TextValue(**as_dict(self.biocide_admin_method))

        if self.biol_stat is not None and not isinstance(self.biol_stat, BiolStatEnum):
            self.biol_stat = BiolStatEnum(self.biol_stat)

        if not isinstance(self.biomass, list):
            self.biomass = [self.biomass] if self.biomass is not None else []
        self.biomass = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.biomass]

        if self.biotic_regm is not None and not isinstance(self.biotic_regm, TextValue):
            self.biotic_regm = TextValue(**as_dict(self.biotic_regm))

        if self.biotic_relationship is not None and not isinstance(self.biotic_relationship, BioticRelationshipEnum):
            self.biotic_relationship = BioticRelationshipEnum(self.biotic_relationship)

        if self.bishomohopanol is not None and not isinstance(self.bishomohopanol, QuantityValue):
            self.bishomohopanol = QuantityValue(**as_dict(self.bishomohopanol))

        if self.blood_press_diast is not None and not isinstance(self.blood_press_diast, QuantityValue):
            self.blood_press_diast = QuantityValue(**as_dict(self.blood_press_diast))

        if self.blood_press_syst is not None and not isinstance(self.blood_press_syst, QuantityValue):
            self.blood_press_syst = QuantityValue(**as_dict(self.blood_press_syst))

        if self.bromide is not None and not isinstance(self.bromide, QuantityValue):
            self.bromide = QuantityValue(**as_dict(self.bromide))

        if self.build_docs is not None and not isinstance(self.build_docs, BuildDocsEnum):
            self.build_docs = BuildDocsEnum(self.build_docs)

        if not isinstance(self.build_occup_type, list):
            self.build_occup_type = [self.build_occup_type] if self.build_occup_type is not None else []
        self.build_occup_type = [v if isinstance(v, BuildOccupTypeEnum) else BuildOccupTypeEnum(v) for v in self.build_occup_type]

        if self.building_setting is not None and not isinstance(self.building_setting, BuildingSettingEnum):
            self.building_setting = BuildingSettingEnum(self.building_setting)

        if self.built_struc_age is not None and not isinstance(self.built_struc_age, QuantityValue):
            self.built_struc_age = QuantityValue(**as_dict(self.built_struc_age))

        if self.built_struc_set is not None and not isinstance(self.built_struc_set, TextValue):
            self.built_struc_set = TextValue(**as_dict(self.built_struc_set))

        if self.built_struc_type is not None and not isinstance(self.built_struc_type, TextValue):
            self.built_struc_type = TextValue(**as_dict(self.built_struc_type))

        if self.calcium is not None and not isinstance(self.calcium, QuantityValue):
            self.calcium = QuantityValue(**as_dict(self.calcium))

        if self.carb_dioxide is not None and not isinstance(self.carb_dioxide, QuantityValue):
            self.carb_dioxide = QuantityValue(**as_dict(self.carb_dioxide))

        if self.carb_monoxide is not None and not isinstance(self.carb_monoxide, QuantityValue):
            self.carb_monoxide = QuantityValue(**as_dict(self.carb_monoxide))

        if self.carb_nitro_ratio is not None and not isinstance(self.carb_nitro_ratio, QuantityValue):
            self.carb_nitro_ratio = QuantityValue(**as_dict(self.carb_nitro_ratio))

        if self.ceil_area is not None and not isinstance(self.ceil_area, QuantityValue):
            self.ceil_area = QuantityValue(**as_dict(self.ceil_area))

        if self.ceil_cond is not None and not isinstance(self.ceil_cond, CeilCondEnum):
            self.ceil_cond = CeilCondEnum(self.ceil_cond)

        if self.ceil_finish_mat is not None and not isinstance(self.ceil_finish_mat, CeilFinishMatEnum):
            self.ceil_finish_mat = CeilFinishMatEnum(self.ceil_finish_mat)

        if self.ceil_struc is not None and not isinstance(self.ceil_struc, TextValue):
            self.ceil_struc = TextValue(**as_dict(self.ceil_struc))

        if self.ceil_texture is not None and not isinstance(self.ceil_texture, CeilTextureEnum):
            self.ceil_texture = CeilTextureEnum(self.ceil_texture)

        if self.ceil_thermal_mass is not None and not isinstance(self.ceil_thermal_mass, QuantityValue):
            self.ceil_thermal_mass = QuantityValue(**as_dict(self.ceil_thermal_mass))

        if self.ceil_type is not None and not isinstance(self.ceil_type, CeilTypeEnum):
            self.ceil_type = CeilTypeEnum(self.ceil_type)

        if self.ceil_water_mold is not None and not isinstance(self.ceil_water_mold, TextValue):
            self.ceil_water_mold = TextValue(**as_dict(self.ceil_water_mold))

        if not isinstance(self.chem_administration, list):
            self.chem_administration = [self.chem_administration] if self.chem_administration is not None else []
        self.chem_administration = [v if isinstance(v, ControlledTermValue) else ControlledTermValue(**as_dict(v)) for v in self.chem_administration]

        if not isinstance(self.chem_mutagen, list):
            self.chem_mutagen = [self.chem_mutagen] if self.chem_mutagen is not None else []
        self.chem_mutagen = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.chem_mutagen]

        if self.chem_oxygen_dem is not None and not isinstance(self.chem_oxygen_dem, QuantityValue):
            self.chem_oxygen_dem = QuantityValue(**as_dict(self.chem_oxygen_dem))

        if self.chem_treat_method is not None and not isinstance(self.chem_treat_method, str):
            self.chem_treat_method = str(self.chem_treat_method)

        if self.chem_treatment is not None and not isinstance(self.chem_treatment, TextValue):
            self.chem_treatment = TextValue(**as_dict(self.chem_treatment))

        if self.chloride is not None and not isinstance(self.chloride, QuantityValue):
            self.chloride = QuantityValue(**as_dict(self.chloride))

        if self.chlorophyll is not None and not isinstance(self.chlorophyll, QuantityValue):
            self.chlorophyll = QuantityValue(**as_dict(self.chlorophyll))

        if not isinstance(self.climate_environment, list):
            self.climate_environment = [self.climate_environment] if self.climate_environment is not None else []
        self.climate_environment = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.climate_environment]

        if self.collection_date is not None and not isinstance(self.collection_date, TimestampValue):
            self.collection_date = TimestampValue(**as_dict(self.collection_date))

        if self.conduc is not None and not isinstance(self.conduc, QuantityValue):
            self.conduc = QuantityValue(**as_dict(self.conduc))

        if self.cool_syst_id is not None and not isinstance(self.cool_syst_id, TextValue):
            self.cool_syst_id = TextValue(**as_dict(self.cool_syst_id))

        if self.core_field is not None and not isinstance(self.core_field, str):
            self.core_field = str(self.core_field)

        if self.crop_rotation is not None and not isinstance(self.crop_rotation, TextValue):
            self.crop_rotation = TextValue(**as_dict(self.crop_rotation))

        if self.cult_root_med is not None and not isinstance(self.cult_root_med, TextValue):
            self.cult_root_med = TextValue(**as_dict(self.cult_root_med))

        if self.cur_land_use is not None and not isinstance(self.cur_land_use, CurLandUseEnum):
            self.cur_land_use = CurLandUseEnum(self.cur_land_use)

        if self.cur_vegetation is not None and not isinstance(self.cur_vegetation, TextValue):
            self.cur_vegetation = TextValue(**as_dict(self.cur_vegetation))

        if self.cur_vegetation_meth is not None and not isinstance(self.cur_vegetation_meth, TextValue):
            self.cur_vegetation_meth = TextValue(**as_dict(self.cur_vegetation_meth))

        if self.date_last_rain is not None and not isinstance(self.date_last_rain, TimestampValue):
            self.date_last_rain = TimestampValue(**as_dict(self.date_last_rain))

        if self.density is not None and not isinstance(self.density, QuantityValue):
            self.density = QuantityValue(**as_dict(self.density))

        if self.depos_env is not None and not isinstance(self.depos_env, DeposEnvEnum):
            self.depos_env = DeposEnvEnum(self.depos_env)

        if self.depth is not None and not isinstance(self.depth, QuantityValue):
            self.depth = QuantityValue(**as_dict(self.depth))

        if self.dew_point is not None and not isinstance(self.dew_point, QuantityValue):
            self.dew_point = QuantityValue(**as_dict(self.dew_point))

        if not isinstance(self.diether_lipids, list):
            self.diether_lipids = [self.diether_lipids] if self.diether_lipids is not None else []
        self.diether_lipids = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.diether_lipids]

        if self.diss_carb_dioxide is not None and not isinstance(self.diss_carb_dioxide, QuantityValue):
            self.diss_carb_dioxide = QuantityValue(**as_dict(self.diss_carb_dioxide))

        if self.diss_hydrogen is not None and not isinstance(self.diss_hydrogen, QuantityValue):
            self.diss_hydrogen = QuantityValue(**as_dict(self.diss_hydrogen))

        if self.diss_inorg_carb is not None and not isinstance(self.diss_inorg_carb, QuantityValue):
            self.diss_inorg_carb = QuantityValue(**as_dict(self.diss_inorg_carb))

        if self.diss_inorg_nitro is not None and not isinstance(self.diss_inorg_nitro, QuantityValue):
            self.diss_inorg_nitro = QuantityValue(**as_dict(self.diss_inorg_nitro))

        if self.diss_inorg_phosp is not None and not isinstance(self.diss_inorg_phosp, QuantityValue):
            self.diss_inorg_phosp = QuantityValue(**as_dict(self.diss_inorg_phosp))

        if self.diss_iron is not None and not isinstance(self.diss_iron, QuantityValue):
            self.diss_iron = QuantityValue(**as_dict(self.diss_iron))

        if self.diss_org_carb is not None and not isinstance(self.diss_org_carb, QuantityValue):
            self.diss_org_carb = QuantityValue(**as_dict(self.diss_org_carb))

        if self.diss_org_nitro is not None and not isinstance(self.diss_org_nitro, QuantityValue):
            self.diss_org_nitro = QuantityValue(**as_dict(self.diss_org_nitro))

        if self.diss_oxygen is not None and not isinstance(self.diss_oxygen, QuantityValue):
            self.diss_oxygen = QuantityValue(**as_dict(self.diss_oxygen))

        if self.diss_oxygen_fluid is not None and not isinstance(self.diss_oxygen_fluid, QuantityValue):
            self.diss_oxygen_fluid = QuantityValue(**as_dict(self.diss_oxygen_fluid))

        if self.dna_cont_well is not None and not isinstance(self.dna_cont_well, str):
            self.dna_cont_well = str(self.dna_cont_well)

        if self.door_comp_type is not None and not isinstance(self.door_comp_type, DoorCompTypeEnum):
            self.door_comp_type = DoorCompTypeEnum(self.door_comp_type)

        if self.door_cond is not None and not isinstance(self.door_cond, DoorCondEnum):
            self.door_cond = DoorCondEnum(self.door_cond)

        if self.door_direct is not None and not isinstance(self.door_direct, DoorDirectEnum):
            self.door_direct = DoorDirectEnum(self.door_direct)

        if self.door_loc is not None and not isinstance(self.door_loc, DoorLocEnum):
            self.door_loc = DoorLocEnum(self.door_loc)

        if self.door_mat is not None and not isinstance(self.door_mat, DoorMatEnum):
            self.door_mat = DoorMatEnum(self.door_mat)

        if self.door_move is not None and not isinstance(self.door_move, DoorMoveEnum):
            self.door_move = DoorMoveEnum(self.door_move)

        if self.door_size is not None and not isinstance(self.door_size, QuantityValue):
            self.door_size = QuantityValue(**as_dict(self.door_size))

        if self.door_type is not None and not isinstance(self.door_type, DoorTypeEnum):
            self.door_type = DoorTypeEnum(self.door_type)

        if self.door_type_metal is not None and not isinstance(self.door_type_metal, DoorTypeMetalEnum):
            self.door_type_metal = DoorTypeMetalEnum(self.door_type_metal)

        if self.door_type_wood is not None and not isinstance(self.door_type_wood, DoorTypeWoodEnum):
            self.door_type_wood = DoorTypeWoodEnum(self.door_type_wood)

        if self.door_water_mold is not None and not isinstance(self.door_water_mold, TextValue):
            self.door_water_mold = TextValue(**as_dict(self.door_water_mold))

        if self.down_par is not None and not isinstance(self.down_par, QuantityValue):
            self.down_par = QuantityValue(**as_dict(self.down_par))

        if self.drainage_class is not None and not isinstance(self.drainage_class, DrainageClassEnum):
            self.drainage_class = DrainageClassEnum(self.drainage_class)

        if self.drawings is not None and not isinstance(self.drawings, DrawingsEnum):
            self.drawings = DrawingsEnum(self.drawings)

        if self.ecosystem is not None and not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self.ecosystem_category is not None and not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self.ecosystem_subtype is not None and not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self.ecosystem_type is not None and not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self.efficiency_percent is not None and not isinstance(self.efficiency_percent, QuantityValue):
            self.efficiency_percent = QuantityValue(**as_dict(self.efficiency_percent))

        if self.elev is not None and not isinstance(self.elev, float):
            self.elev = float(self.elev)

        if self.elevator is not None and not isinstance(self.elevator, TextValue):
            self.elevator = TextValue(**as_dict(self.elevator))

        if not isinstance(self.emulsions, list):
            self.emulsions = [self.emulsions] if self.emulsions is not None else []
        self.emulsions = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.emulsions]

        if self.env_package is not None and not isinstance(self.env_package, TextValue):
            self.env_package = TextValue(**as_dict(self.env_package))

        if self.environment_field is not None and not isinstance(self.environment_field, str):
            self.environment_field = str(self.environment_field)

        if self.escalator is not None and not isinstance(self.escalator, TextValue):
            self.escalator = TextValue(**as_dict(self.escalator))

        if self.ethylbenzene is not None and not isinstance(self.ethylbenzene, QuantityValue):
            self.ethylbenzene = QuantityValue(**as_dict(self.ethylbenzene))

        if self.exp_duct is not None and not isinstance(self.exp_duct, QuantityValue):
            self.exp_duct = QuantityValue(**as_dict(self.exp_duct))

        if self.exp_pipe is not None and not isinstance(self.exp_pipe, QuantityValue):
            self.exp_pipe = QuantityValue(**as_dict(self.exp_pipe))

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, ControlledTermValue):
            self.experimental_factor = ControlledTermValue(**as_dict(self.experimental_factor))

        if self.ext_door is not None and not isinstance(self.ext_door, TextValue):
            self.ext_door = TextValue(**as_dict(self.ext_door))

        if self.ext_wall_orient is not None and not isinstance(self.ext_wall_orient, ExtWallOrientEnum):
            self.ext_wall_orient = ExtWallOrientEnum(self.ext_wall_orient)

        if self.ext_window_orient is not None and not isinstance(self.ext_window_orient, ExtWindowOrientEnum):
            self.ext_window_orient = ExtWindowOrientEnum(self.ext_window_orient)

        if self.extreme_event is not None and not isinstance(self.extreme_event, str):
            self.extreme_event = str(self.extreme_event)

        if self.fao_class is not None and not isinstance(self.fao_class, FaoClassEnum):
            self.fao_class = FaoClassEnum(self.fao_class)

        if not isinstance(self.fertilizer_regm, list):
            self.fertilizer_regm = [self.fertilizer_regm] if self.fertilizer_regm is not None else []
        self.fertilizer_regm = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.fertilizer_regm]

        if self.field is not None and not isinstance(self.field, TextValue):
            self.field = TextValue(**as_dict(self.field))

        if not isinstance(self.filter_type, list):
            self.filter_type = [self.filter_type] if self.filter_type is not None else []
        self.filter_type = [v if isinstance(v, FilterTypeEnum) else FilterTypeEnum(v) for v in self.filter_type]

        if self.fire is not None and not isinstance(self.fire, str):
            self.fire = str(self.fire)

        if self.fireplace_type is not None and not isinstance(self.fireplace_type, TextValue):
            self.fireplace_type = TextValue(**as_dict(self.fireplace_type))

        if self.flooding is not None and not isinstance(self.flooding, str):
            self.flooding = str(self.flooding)

        if self.floor_age is not None and not isinstance(self.floor_age, QuantityValue):
            self.floor_age = QuantityValue(**as_dict(self.floor_age))

        if self.floor_area is not None and not isinstance(self.floor_area, QuantityValue):
            self.floor_area = QuantityValue(**as_dict(self.floor_area))

        if self.floor_cond is not None and not isinstance(self.floor_cond, FloorCondEnum):
            self.floor_cond = FloorCondEnum(self.floor_cond)

        if self.floor_count is not None and not isinstance(self.floor_count, TextValue):
            self.floor_count = TextValue(**as_dict(self.floor_count))

        if self.floor_finish_mat is not None and not isinstance(self.floor_finish_mat, FloorFinishMatEnum):
            self.floor_finish_mat = FloorFinishMatEnum(self.floor_finish_mat)

        if self.floor_struc is not None and not isinstance(self.floor_struc, FloorStrucEnum):
            self.floor_struc = FloorStrucEnum(self.floor_struc)

        if self.floor_thermal_mass is not None and not isinstance(self.floor_thermal_mass, QuantityValue):
            self.floor_thermal_mass = QuantityValue(**as_dict(self.floor_thermal_mass))

        if self.floor_water_mold is not None and not isinstance(self.floor_water_mold, FloorWaterMoldEnum):
            self.floor_water_mold = FloorWaterMoldEnum(self.floor_water_mold)

        if self.fluor is not None and not isinstance(self.fluor, QuantityValue):
            self.fluor = QuantityValue(**as_dict(self.fluor))

        if self.freq_clean is not None and not isinstance(self.freq_clean, QuantityValue):
            self.freq_clean = QuantityValue(**as_dict(self.freq_clean))

        if self.freq_cook is not None and not isinstance(self.freq_cook, QuantityValue):
            self.freq_cook = QuantityValue(**as_dict(self.freq_cook))

        if not isinstance(self.fungicide_regm, list):
            self.fungicide_regm = [self.fungicide_regm] if self.fungicide_regm is not None else []
        self.fungicide_regm = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.fungicide_regm]

        if self.furniture is not None and not isinstance(self.furniture, FurnitureEnum):
            self.furniture = FurnitureEnum(self.furniture)

        if not isinstance(self.gaseous_environment, list):
            self.gaseous_environment = [self.gaseous_environment] if self.gaseous_environment is not None else []
        self.gaseous_environment = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.gaseous_environment]

        if not isinstance(self.gaseous_substances, list):
            self.gaseous_substances = [self.gaseous_substances] if self.gaseous_substances is not None else []
        self.gaseous_substances = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.gaseous_substances]

        if self.gender_restroom is not None and not isinstance(self.gender_restroom, GenderRestroomEnum):
            self.gender_restroom = GenderRestroomEnum(self.gender_restroom)

        if self.genetic_mod is not None and not isinstance(self.genetic_mod, TextValue):
            self.genetic_mod = TextValue(**as_dict(self.genetic_mod))

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, TextValue):
            self.geo_loc_name = TextValue(**as_dict(self.geo_loc_name))

        if self.glucosidase_act is not None and not isinstance(self.glucosidase_act, QuantityValue):
            self.glucosidase_act = QuantityValue(**as_dict(self.glucosidase_act))

        if self.gravidity is not None and not isinstance(self.gravidity, TextValue):
            self.gravidity = TextValue(**as_dict(self.gravidity))

        if not isinstance(self.gravity, list):
            self.gravity = [self.gravity] if self.gravity is not None else []
        self.gravity = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.gravity]

        if self.growth_facil is not None and not isinstance(self.growth_facil, ControlledTermValue):
            self.growth_facil = ControlledTermValue(**as_dict(self.growth_facil))

        if self.growth_habit is not None and not isinstance(self.growth_habit, GrowthHabitEnum):
            self.growth_habit = GrowthHabitEnum(self.growth_habit)

        if not isinstance(self.growth_hormone_regm, list):
            self.growth_hormone_regm = [self.growth_hormone_regm] if self.growth_hormone_regm is not None else []
        self.growth_hormone_regm = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.growth_hormone_regm]

        if self.hall_count is not None and not isinstance(self.hall_count, TextValue):
            self.hall_count = TextValue(**as_dict(self.hall_count))

        if self.handidness is not None and not isinstance(self.handidness, HandidnessEnum):
            self.handidness = HandidnessEnum(self.handidness)

        if self.hc_produced is not None and not isinstance(self.hc_produced, HcProducedEnum):
            self.hc_produced = HcProducedEnum(self.hc_produced)

        if self.hcr is not None and not isinstance(self.hcr, HcrEnum):
            self.hcr = HcrEnum(self.hcr)

        if self.hcr_fw_salinity is not None and not isinstance(self.hcr_fw_salinity, QuantityValue):
            self.hcr_fw_salinity = QuantityValue(**as_dict(self.hcr_fw_salinity))

        if self.hcr_geol_age is not None and not isinstance(self.hcr_geol_age, HcrGeolAgeEnum):
            self.hcr_geol_age = HcrGeolAgeEnum(self.hcr_geol_age)

        if self.hcr_pressure is not None and not isinstance(self.hcr_pressure, TextValue):
            self.hcr_pressure = TextValue(**as_dict(self.hcr_pressure))

        if self.hcr_temp is not None and not isinstance(self.hcr_temp, TextValue):
            self.hcr_temp = TextValue(**as_dict(self.hcr_temp))

        if not isinstance(self.heat_cool_type, list):
            self.heat_cool_type = [self.heat_cool_type] if self.heat_cool_type is not None else []
        self.heat_cool_type = [v if isinstance(v, HeatCoolTypeEnum) else HeatCoolTypeEnum(v) for v in self.heat_cool_type]

        if self.heat_deliv_loc is not None and not isinstance(self.heat_deliv_loc, HeatDelivLocEnum):
            self.heat_deliv_loc = HeatDelivLocEnum(self.heat_deliv_loc)

        if self.heat_sys_deliv_meth is not None and not isinstance(self.heat_sys_deliv_meth, str):
            self.heat_sys_deliv_meth = str(self.heat_sys_deliv_meth)

        if self.heat_system_id is not None and not isinstance(self.heat_system_id, TextValue):
            self.heat_system_id = TextValue(**as_dict(self.heat_system_id))

        if not isinstance(self.heavy_metals, list):
            self.heavy_metals = [self.heavy_metals] if self.heavy_metals is not None else []
        self.heavy_metals = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.heavy_metals]

        self._normalize_inlined_as_dict(slot_name="heavy_metals_meth", slot_type=TextValue, key_name="type", keyed=False)

        if self.height_carper_fiber is not None and not isinstance(self.height_carper_fiber, QuantityValue):
            self.height_carper_fiber = QuantityValue(**as_dict(self.height_carper_fiber))

        if not isinstance(self.herbicide_regm, list):
            self.herbicide_regm = [self.herbicide_regm] if self.herbicide_regm is not None else []
        self.herbicide_regm = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.herbicide_regm]

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, TextValue):
            self.horizon_meth = TextValue(**as_dict(self.horizon_meth))

        if self.host_age is not None and not isinstance(self.host_age, QuantityValue):
            self.host_age = QuantityValue(**as_dict(self.host_age))

        if self.host_body_habitat is not None and not isinstance(self.host_body_habitat, TextValue):
            self.host_body_habitat = TextValue(**as_dict(self.host_body_habitat))

        if self.host_body_product is not None and not isinstance(self.host_body_product, ControlledTermValue):
            self.host_body_product = ControlledTermValue(**as_dict(self.host_body_product))

        if self.host_body_site is not None and not isinstance(self.host_body_site, ControlledTermValue):
            self.host_body_site = ControlledTermValue(**as_dict(self.host_body_site))

        if self.host_body_temp is not None and not isinstance(self.host_body_temp, QuantityValue):
            self.host_body_temp = QuantityValue(**as_dict(self.host_body_temp))

        if self.host_color is not None and not isinstance(self.host_color, TextValue):
            self.host_color = TextValue(**as_dict(self.host_color))

        if self.host_common_name is not None and not isinstance(self.host_common_name, TextValue):
            self.host_common_name = TextValue(**as_dict(self.host_common_name))

        if not isinstance(self.host_diet, list):
            self.host_diet = [self.host_diet] if self.host_diet is not None else []
        self.host_diet = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.host_diet]

        if self.host_dry_mass is not None and not isinstance(self.host_dry_mass, QuantityValue):
            self.host_dry_mass = QuantityValue(**as_dict(self.host_dry_mass))

        if not isinstance(self.host_family_relation, list):
            self.host_family_relation = [self.host_family_relation] if self.host_family_relation is not None else []
        self.host_family_relation = [v if isinstance(v, str) else str(v) for v in self.host_family_relation]

        if self.host_genotype is not None and not isinstance(self.host_genotype, TextValue):
            self.host_genotype = TextValue(**as_dict(self.host_genotype))

        if self.host_growth_cond is not None and not isinstance(self.host_growth_cond, TextValue):
            self.host_growth_cond = TextValue(**as_dict(self.host_growth_cond))

        if self.host_height is not None and not isinstance(self.host_height, QuantityValue):
            self.host_height = QuantityValue(**as_dict(self.host_height))

        if not isinstance(self.host_last_meal, list):
            self.host_last_meal = [self.host_last_meal] if self.host_last_meal is not None else []
        self.host_last_meal = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.host_last_meal]

        if self.host_length is not None and not isinstance(self.host_length, QuantityValue):
            self.host_length = QuantityValue(**as_dict(self.host_length))

        if self.host_life_stage is not None and not isinstance(self.host_life_stage, TextValue):
            self.host_life_stage = TextValue(**as_dict(self.host_life_stage))

        if self.host_phenotype is not None and not isinstance(self.host_phenotype, ControlledTermValue):
            self.host_phenotype = ControlledTermValue(**as_dict(self.host_phenotype))

        if self.host_sex is not None and not isinstance(self.host_sex, HostSexEnum):
            self.host_sex = HostSexEnum(self.host_sex)

        if self.host_shape is not None and not isinstance(self.host_shape, TextValue):
            self.host_shape = TextValue(**as_dict(self.host_shape))

        if self.host_subject_id is not None and not isinstance(self.host_subject_id, TextValue):
            self.host_subject_id = TextValue(**as_dict(self.host_subject_id))

        if not isinstance(self.host_subspecf_genlin, list):
            self.host_subspecf_genlin = [self.host_subspecf_genlin] if self.host_subspecf_genlin is not None else []
        self.host_subspecf_genlin = [v if isinstance(v, str) else str(v) for v in self.host_subspecf_genlin]

        if self.host_substrate is not None and not isinstance(self.host_substrate, TextValue):
            self.host_substrate = TextValue(**as_dict(self.host_substrate))

        if not isinstance(self.host_symbiont, list):
            self.host_symbiont = [self.host_symbiont] if self.host_symbiont is not None else []
        self.host_symbiont = [v if isinstance(v, str) else str(v) for v in self.host_symbiont]

        if self.host_taxid is not None and not isinstance(self.host_taxid, ControlledIdentifiedTermValue):
            self.host_taxid = ControlledIdentifiedTermValue(**as_dict(self.host_taxid))

        if self.host_tot_mass is not None and not isinstance(self.host_tot_mass, QuantityValue):
            self.host_tot_mass = QuantityValue(**as_dict(self.host_tot_mass))

        if self.host_wet_mass is not None and not isinstance(self.host_wet_mass, QuantityValue):
            self.host_wet_mass = QuantityValue(**as_dict(self.host_wet_mass))

        if self.humidity is not None and not isinstance(self.humidity, QuantityValue):
            self.humidity = QuantityValue(**as_dict(self.humidity))

        if not isinstance(self.humidity_regm, list):
            self.humidity_regm = [self.humidity_regm] if self.humidity_regm is not None else []
        self.humidity_regm = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.humidity_regm]

        if self.indoor_space is not None and not isinstance(self.indoor_space, IndoorSpaceEnum):
            self.indoor_space = IndoorSpaceEnum(self.indoor_space)

        if self.indoor_surf is not None and not isinstance(self.indoor_surf, IndoorSurfEnum):
            self.indoor_surf = IndoorSurfEnum(self.indoor_surf)

        if self.indust_eff_percent is not None and not isinstance(self.indust_eff_percent, QuantityValue):
            self.indust_eff_percent = QuantityValue(**as_dict(self.indust_eff_percent))

        if not isinstance(self.inorg_particles, list):
            self.inorg_particles = [self.inorg_particles] if self.inorg_particles is not None else []
        self.inorg_particles = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.inorg_particles]

        if self.inside_lux is not None and not isinstance(self.inside_lux, QuantityValue):
            self.inside_lux = QuantityValue(**as_dict(self.inside_lux))

        if self.int_wall_cond is not None and not isinstance(self.int_wall_cond, IntWallCondEnum):
            self.int_wall_cond = IntWallCondEnum(self.int_wall_cond)

        if self.investigation_field is not None and not isinstance(self.investigation_field, str):
            self.investigation_field = str(self.investigation_field)

        if self.iw_bt_date_well is not None and not isinstance(self.iw_bt_date_well, TimestampValue):
            self.iw_bt_date_well = TimestampValue(**as_dict(self.iw_bt_date_well))

        if self.iwf is not None and not isinstance(self.iwf, QuantityValue):
            self.iwf = QuantityValue(**as_dict(self.iwf))

        if self.last_clean is not None and not isinstance(self.last_clean, TimestampValue):
            self.last_clean = TimestampValue(**as_dict(self.last_clean))

        if self.lat_lon is not None and not isinstance(self.lat_lon, GeolocationValue):
            self.lat_lon = GeolocationValue(**as_dict(self.lat_lon))

        if self.lbc_thirty is not None and not isinstance(self.lbc_thirty, QuantityValue):
            self.lbc_thirty = QuantityValue(**as_dict(self.lbc_thirty))

        if self.lbceq is not None and not isinstance(self.lbceq, QuantityValue):
            self.lbceq = QuantityValue(**as_dict(self.lbceq))

        if self.light_intensity is not None and not isinstance(self.light_intensity, QuantityValue):
            self.light_intensity = QuantityValue(**as_dict(self.light_intensity))

        if self.light_regm is not None and not isinstance(self.light_regm, TextValue):
            self.light_regm = TextValue(**as_dict(self.light_regm))

        if not isinstance(self.light_type, list):
            self.light_type = [self.light_type] if self.light_type is not None else []
        self.light_type = [v if isinstance(v, LightTypeEnum) else LightTypeEnum(v) for v in self.light_type]

        if self.link_addit_analys is not None and not isinstance(self.link_addit_analys, TextValue):
            self.link_addit_analys = TextValue(**as_dict(self.link_addit_analys))

        if self.link_class_info is not None and not isinstance(self.link_class_info, TextValue):
            self.link_class_info = TextValue(**as_dict(self.link_class_info))

        if self.link_climate_info is not None and not isinstance(self.link_climate_info, TextValue):
            self.link_climate_info = TextValue(**as_dict(self.link_climate_info))

        if self.lithology is not None and not isinstance(self.lithology, LithologyEnum):
            self.lithology = LithologyEnum(self.lithology)

        if self.local_class is not None and not isinstance(self.local_class, TextValue):
            self.local_class = TextValue(**as_dict(self.local_class))

        if self.local_class_meth is not None and not isinstance(self.local_class_meth, TextValue):
            self.local_class_meth = TextValue(**as_dict(self.local_class_meth))

        if self.magnesium is not None and not isinstance(self.magnesium, QuantityValue):
            self.magnesium = QuantityValue(**as_dict(self.magnesium))

        if self.manganese is not None and not isinstance(self.manganese, QuantityValue):
            self.manganese = QuantityValue(**as_dict(self.manganese))

        if self.max_occup is not None and not isinstance(self.max_occup, QuantityValue):
            self.max_occup = QuantityValue(**as_dict(self.max_occup))

        if self.mean_frict_vel is not None and not isinstance(self.mean_frict_vel, QuantityValue):
            self.mean_frict_vel = QuantityValue(**as_dict(self.mean_frict_vel))

        if self.mean_peak_frict_vel is not None and not isinstance(self.mean_peak_frict_vel, QuantityValue):
            self.mean_peak_frict_vel = QuantityValue(**as_dict(self.mean_peak_frict_vel))

        if self.mech_struc is not None and not isinstance(self.mech_struc, MechStrucEnum):
            self.mech_struc = MechStrucEnum(self.mech_struc)

        if not isinstance(self.mechanical_damage, list):
            self.mechanical_damage = [self.mechanical_damage] if self.mechanical_damage is not None else []
        self.mechanical_damage = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.mechanical_damage]

        if self.methane is not None and not isinstance(self.methane, QuantityValue):
            self.methane = QuantityValue(**as_dict(self.methane))

        if self.micro_biomass_meth is not None and not isinstance(self.micro_biomass_meth, str):
            self.micro_biomass_meth = str(self.micro_biomass_meth)

        if self.microbial_biomass is not None and not isinstance(self.microbial_biomass, QuantityValue):
            self.microbial_biomass = QuantityValue(**as_dict(self.microbial_biomass))

        if not isinstance(self.mineral_nutr_regm, list):
            self.mineral_nutr_regm = [self.mineral_nutr_regm] if self.mineral_nutr_regm is not None else []
        self.mineral_nutr_regm = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.mineral_nutr_regm]

        if not isinstance(self.misc_param, list):
            self.misc_param = [self.misc_param] if self.misc_param is not None else []
        self.misc_param = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.misc_param]

        if not isinstance(self.n_alkanes, list):
            self.n_alkanes = [self.n_alkanes] if self.n_alkanes is not None else []
        self.n_alkanes = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.n_alkanes]

        if self.nitrate is not None and not isinstance(self.nitrate, QuantityValue):
            self.nitrate = QuantityValue(**as_dict(self.nitrate))

        if self.nitrate_nitrogen is not None and not isinstance(self.nitrate_nitrogen, QuantityValue):
            self.nitrate_nitrogen = QuantityValue(**as_dict(self.nitrate_nitrogen))

        if self.nitrite is not None and not isinstance(self.nitrite, QuantityValue):
            self.nitrite = QuantityValue(**as_dict(self.nitrite))

        if self.nitrite_nitrogen is not None and not isinstance(self.nitrite_nitrogen, QuantityValue):
            self.nitrite_nitrogen = QuantityValue(**as_dict(self.nitrite_nitrogen))

        if self.nitro is not None and not isinstance(self.nitro, QuantityValue):
            self.nitro = QuantityValue(**as_dict(self.nitro))

        if not isinstance(self.non_min_nutr_regm, list):
            self.non_min_nutr_regm = [self.non_min_nutr_regm] if self.non_min_nutr_regm is not None else []
        self.non_min_nutr_regm = [v if isinstance(v, str) else str(v) for v in self.non_min_nutr_regm]

        if self.nucleic_acid_sequence_source_field is not None and not isinstance(self.nucleic_acid_sequence_source_field, str):
            self.nucleic_acid_sequence_source_field = str(self.nucleic_acid_sequence_source_field)

        if self.number_pets is not None and not isinstance(self.number_pets, QuantityValue):
            self.number_pets = QuantityValue(**as_dict(self.number_pets))

        if self.number_plants is not None and not isinstance(self.number_plants, QuantityValue):
            self.number_plants = QuantityValue(**as_dict(self.number_plants))

        if self.number_resident is not None and not isinstance(self.number_resident, QuantityValue):
            self.number_resident = QuantityValue(**as_dict(self.number_resident))

        if self.occup_density_samp is not None and not isinstance(self.occup_density_samp, QuantityValue):
            self.occup_density_samp = QuantityValue(**as_dict(self.occup_density_samp))

        if self.occup_document is not None and not isinstance(self.occup_document, OccupDocumentEnum):
            self.occup_document = OccupDocumentEnum(self.occup_document)

        if self.occup_samp is not None and not isinstance(self.occup_samp, QuantityValue):
            self.occup_samp = QuantityValue(**as_dict(self.occup_samp))

        if self.org_carb is not None and not isinstance(self.org_carb, QuantityValue):
            self.org_carb = QuantityValue(**as_dict(self.org_carb))

        if self.org_count_qpcr_info is not None and not isinstance(self.org_count_qpcr_info, str):
            self.org_count_qpcr_info = str(self.org_count_qpcr_info)

        if self.org_matter is not None and not isinstance(self.org_matter, QuantityValue):
            self.org_matter = QuantityValue(**as_dict(self.org_matter))

        if self.org_nitro is not None and not isinstance(self.org_nitro, QuantityValue):
            self.org_nitro = QuantityValue(**as_dict(self.org_nitro))

        if not isinstance(self.org_particles, list):
            self.org_particles = [self.org_particles] if self.org_particles is not None else []
        self.org_particles = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.org_particles]

        if not isinstance(self.organism_count, list):
            self.organism_count = [self.organism_count] if self.organism_count is not None else []
        self.organism_count = [v if isinstance(v, QuantityValue) else QuantityValue(**as_dict(v)) for v in self.organism_count]

        if self.owc_tvdss is not None and not isinstance(self.owc_tvdss, QuantityValue):
            self.owc_tvdss = QuantityValue(**as_dict(self.owc_tvdss))

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, OxyStatSampEnum):
            self.oxy_stat_samp = OxyStatSampEnum(self.oxy_stat_samp)

        if self.oxygen is not None and not isinstance(self.oxygen, QuantityValue):
            self.oxygen = QuantityValue(**as_dict(self.oxygen))

        if self.part_org_carb is not None and not isinstance(self.part_org_carb, QuantityValue):
            self.part_org_carb = QuantityValue(**as_dict(self.part_org_carb))

        if self.part_org_nitro is not None and not isinstance(self.part_org_nitro, QuantityValue):
            self.part_org_nitro = QuantityValue(**as_dict(self.part_org_nitro))

        if not isinstance(self.particle_class, list):
            self.particle_class = [self.particle_class] if self.particle_class is not None else []
        self.particle_class = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.particle_class]

        if self.permeability is not None and not isinstance(self.permeability, TextValue):
            self.permeability = TextValue(**as_dict(self.permeability))

        if not isinstance(self.perturbation, list):
            self.perturbation = [self.perturbation] if self.perturbation is not None else []
        self.perturbation = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.perturbation]

        if not isinstance(self.pesticide_regm, list):
            self.pesticide_regm = [self.pesticide_regm] if self.pesticide_regm is not None else []
        self.pesticide_regm = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.pesticide_regm]

        if self.petroleum_hydrocarb is not None and not isinstance(self.petroleum_hydrocarb, QuantityValue):
            self.petroleum_hydrocarb = QuantityValue(**as_dict(self.petroleum_hydrocarb))

        if self.ph is not None and not isinstance(self.ph, float):
            self.ph = float(self.ph)

        if self.ph_meth is not None and not isinstance(self.ph_meth, TextValue):
            self.ph_meth = TextValue(**as_dict(self.ph_meth))

        if not isinstance(self.ph_regm, list):
            self.ph_regm = [self.ph_regm] if self.ph_regm is not None else []
        self.ph_regm = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.ph_regm]

        if not isinstance(self.phaeopigments, list):
            self.phaeopigments = [self.phaeopigments] if self.phaeopigments is not None else []
        self.phaeopigments = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.phaeopigments]

        if self.phosphate is not None and not isinstance(self.phosphate, QuantityValue):
            self.phosphate = QuantityValue(**as_dict(self.phosphate))

        if not isinstance(self.phosplipid_fatt_acid, list):
            self.phosplipid_fatt_acid = [self.phosplipid_fatt_acid] if self.phosplipid_fatt_acid is not None else []
        self.phosplipid_fatt_acid = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.phosplipid_fatt_acid]

        if self.photon_flux is not None and not isinstance(self.photon_flux, QuantityValue):
            self.photon_flux = QuantityValue(**as_dict(self.photon_flux))

        if self.plant_growth_med is not None and not isinstance(self.plant_growth_med, ControlledTermValue):
            self.plant_growth_med = ControlledTermValue(**as_dict(self.plant_growth_med))

        if self.plant_product is not None and not isinstance(self.plant_product, TextValue):
            self.plant_product = TextValue(**as_dict(self.plant_product))

        if self.plant_sex is not None and not isinstance(self.plant_sex, PlantSexEnum):
            self.plant_sex = PlantSexEnum(self.plant_sex)

        if self.plant_struc is not None and not isinstance(self.plant_struc, ControlledTermValue):
            self.plant_struc = ControlledTermValue(**as_dict(self.plant_struc))

        if not isinstance(self.pollutants, list):
            self.pollutants = [self.pollutants] if self.pollutants is not None else []
        self.pollutants = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.pollutants]

        if self.porosity is not None and not isinstance(self.porosity, TextValue):
            self.porosity = TextValue(**as_dict(self.porosity))

        if self.potassium is not None and not isinstance(self.potassium, QuantityValue):
            self.potassium = QuantityValue(**as_dict(self.potassium))

        if self.pour_point is not None and not isinstance(self.pour_point, QuantityValue):
            self.pour_point = QuantityValue(**as_dict(self.pour_point))

        if self.pre_treatment is not None and not isinstance(self.pre_treatment, TextValue):
            self.pre_treatment = TextValue(**as_dict(self.pre_treatment))

        if self.pres_animal_insect is not None and not isinstance(self.pres_animal_insect, str):
            self.pres_animal_insect = str(self.pres_animal_insect)

        if self.pressure is not None and not isinstance(self.pressure, QuantityValue):
            self.pressure = QuantityValue(**as_dict(self.pressure))

        if self.prev_land_use_meth is not None and not isinstance(self.prev_land_use_meth, str):
            self.prev_land_use_meth = str(self.prev_land_use_meth)

        if self.previous_land_use is not None and not isinstance(self.previous_land_use, TextValue):
            self.previous_land_use = TextValue(**as_dict(self.previous_land_use))

        if self.primary_prod is not None and not isinstance(self.primary_prod, QuantityValue):
            self.primary_prod = QuantityValue(**as_dict(self.primary_prod))

        if self.primary_treatment is not None and not isinstance(self.primary_treatment, TextValue):
            self.primary_treatment = TextValue(**as_dict(self.primary_treatment))

        if self.prod_rate is not None and not isinstance(self.prod_rate, QuantityValue):
            self.prod_rate = QuantityValue(**as_dict(self.prod_rate))

        if self.prod_start_date is not None and not isinstance(self.prod_start_date, TimestampValue):
            self.prod_start_date = TimestampValue(**as_dict(self.prod_start_date))

        if self.profile_position is not None and not isinstance(self.profile_position, ProfilePositionEnum):
            self.profile_position = ProfilePositionEnum(self.profile_position)

        if self.quad_pos is not None and not isinstance(self.quad_pos, QuadPosEnum):
            self.quad_pos = QuadPosEnum(self.quad_pos)

        if not isinstance(self.radiation_regm, list):
            self.radiation_regm = [self.radiation_regm] if self.radiation_regm is not None else []
        self.radiation_regm = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.radiation_regm]

        if not isinstance(self.rainfall_regm, list):
            self.rainfall_regm = [self.rainfall_regm] if self.rainfall_regm is not None else []
        self.rainfall_regm = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.rainfall_regm]

        if self.reactor_type is not None and not isinstance(self.reactor_type, TextValue):
            self.reactor_type = TextValue(**as_dict(self.reactor_type))

        if self.redox_potential is not None and not isinstance(self.redox_potential, QuantityValue):
            self.redox_potential = QuantityValue(**as_dict(self.redox_potential))

        if self.rel_air_humidity is not None and not isinstance(self.rel_air_humidity, QuantityValue):
            self.rel_air_humidity = QuantityValue(**as_dict(self.rel_air_humidity))

        if self.rel_humidity_out is not None and not isinstance(self.rel_humidity_out, QuantityValue):
            self.rel_humidity_out = QuantityValue(**as_dict(self.rel_humidity_out))

        if self.rel_samp_loc is not None and not isinstance(self.rel_samp_loc, RelSampLocEnum):
            self.rel_samp_loc = RelSampLocEnum(self.rel_samp_loc)

        if self.reservoir is not None and not isinstance(self.reservoir, TextValue):
            self.reservoir = TextValue(**as_dict(self.reservoir))

        if self.resins_pc is not None and not isinstance(self.resins_pc, TextValue):
            self.resins_pc = TextValue(**as_dict(self.resins_pc))

        if self.room_air_exch_rate is not None and not isinstance(self.room_air_exch_rate, QuantityValue):
            self.room_air_exch_rate = QuantityValue(**as_dict(self.room_air_exch_rate))

        if self.room_architec_elem is not None and not isinstance(self.room_architec_elem, str):
            self.room_architec_elem = str(self.room_architec_elem)

        if self.room_condt is not None and not isinstance(self.room_condt, RoomCondtEnum):
            self.room_condt = RoomCondtEnum(self.room_condt)

        if self.room_connected is not None and not isinstance(self.room_connected, RoomConnectedEnum):
            self.room_connected = RoomConnectedEnum(self.room_connected)

        if self.room_count is not None and not isinstance(self.room_count, TextValue):
            self.room_count = TextValue(**as_dict(self.room_count))

        if self.room_dim is not None and not isinstance(self.room_dim, TextValue):
            self.room_dim = TextValue(**as_dict(self.room_dim))

        if self.room_door_dist is not None and not isinstance(self.room_door_dist, TextValue):
            self.room_door_dist = TextValue(**as_dict(self.room_door_dist))

        if self.room_door_share is not None and not isinstance(self.room_door_share, TextValue):
            self.room_door_share = TextValue(**as_dict(self.room_door_share))

        if self.room_hallway is not None and not isinstance(self.room_hallway, TextValue):
            self.room_hallway = TextValue(**as_dict(self.room_hallway))

        if self.room_loc is not None and not isinstance(self.room_loc, RoomLocEnum):
            self.room_loc = RoomLocEnum(self.room_loc)

        if self.room_moist_dam_hist is not None and not isinstance(self.room_moist_dam_hist, int):
            self.room_moist_dam_hist = int(self.room_moist_dam_hist)

        if self.room_net_area is not None and not isinstance(self.room_net_area, TextValue):
            self.room_net_area = TextValue(**as_dict(self.room_net_area))

        if self.room_occup is not None and not isinstance(self.room_occup, QuantityValue):
            self.room_occup = QuantityValue(**as_dict(self.room_occup))

        if self.room_samp_pos is not None and not isinstance(self.room_samp_pos, RoomSampPosEnum):
            self.room_samp_pos = RoomSampPosEnum(self.room_samp_pos)

        if self.room_type is not None and not isinstance(self.room_type, RoomTypeEnum):
            self.room_type = RoomTypeEnum(self.room_type)

        if self.room_vol is not None and not isinstance(self.room_vol, TextValue):
            self.room_vol = TextValue(**as_dict(self.room_vol))

        if self.room_wall_share is not None and not isinstance(self.room_wall_share, TextValue):
            self.room_wall_share = TextValue(**as_dict(self.room_wall_share))

        if self.room_window_count is not None and not isinstance(self.room_window_count, int):
            self.room_window_count = int(self.room_window_count)

        if self.root_cond is not None and not isinstance(self.root_cond, TextValue):
            self.root_cond = TextValue(**as_dict(self.root_cond))

        if self.root_med_carbon is not None and not isinstance(self.root_med_carbon, TextValue):
            self.root_med_carbon = TextValue(**as_dict(self.root_med_carbon))

        if self.root_med_macronutr is not None and not isinstance(self.root_med_macronutr, TextValue):
            self.root_med_macronutr = TextValue(**as_dict(self.root_med_macronutr))

        if self.root_med_micronutr is not None and not isinstance(self.root_med_micronutr, TextValue):
            self.root_med_micronutr = TextValue(**as_dict(self.root_med_micronutr))

        if self.root_med_ph is not None and not isinstance(self.root_med_ph, QuantityValue):
            self.root_med_ph = QuantityValue(**as_dict(self.root_med_ph))

        if self.root_med_regl is not None and not isinstance(self.root_med_regl, TextValue):
            self.root_med_regl = TextValue(**as_dict(self.root_med_regl))

        if self.root_med_solid is not None and not isinstance(self.root_med_solid, TextValue):
            self.root_med_solid = TextValue(**as_dict(self.root_med_solid))

        if self.root_med_suppl is not None and not isinstance(self.root_med_suppl, TextValue):
            self.root_med_suppl = TextValue(**as_dict(self.root_med_suppl))

        if self.salinity is not None and not isinstance(self.salinity, QuantityValue):
            self.salinity = QuantityValue(**as_dict(self.salinity))

        if self.salinity_meth is not None and not isinstance(self.salinity_meth, TextValue):
            self.salinity_meth = TextValue(**as_dict(self.salinity_meth))

        if not isinstance(self.salt_regm, list):
            self.salt_regm = [self.salt_regm] if self.salt_regm is not None else []
        self.salt_regm = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.salt_regm]

        if self.samp_capt_status is not None and not isinstance(self.samp_capt_status, SampCaptStatusEnum):
            self.samp_capt_status = SampCaptStatusEnum(self.samp_capt_status)

        if self.samp_collec_device is not None and not isinstance(self.samp_collec_device, str):
            self.samp_collec_device = str(self.samp_collec_device)

        if self.samp_collec_method is not None and not isinstance(self.samp_collec_method, str):
            self.samp_collec_method = str(self.samp_collec_method)

        if self.samp_collect_point is not None and not isinstance(self.samp_collect_point, SampCollectPointEnum):
            self.samp_collect_point = SampCollectPointEnum(self.samp_collect_point)

        if self.samp_dis_stage is not None and not isinstance(self.samp_dis_stage, SampDisStageEnum):
            self.samp_dis_stage = SampDisStageEnum(self.samp_dis_stage)

        if self.samp_floor is not None and not isinstance(self.samp_floor, SampFloorEnum):
            self.samp_floor = SampFloorEnum(self.samp_floor)

        if self.samp_loc_corr_rate is not None and not isinstance(self.samp_loc_corr_rate, TextValue):
            self.samp_loc_corr_rate = TextValue(**as_dict(self.samp_loc_corr_rate))

        if self.samp_mat_process is not None and not isinstance(self.samp_mat_process, ControlledTermValue):
            self.samp_mat_process = ControlledTermValue(**as_dict(self.samp_mat_process))

        if self.samp_md is not None and not isinstance(self.samp_md, QuantityValue):
            self.samp_md = QuantityValue(**as_dict(self.samp_md))

        if self.samp_name is not None and not isinstance(self.samp_name, str):
            self.samp_name = str(self.samp_name)

        if self.samp_preserv is not None and not isinstance(self.samp_preserv, TextValue):
            self.samp_preserv = TextValue(**as_dict(self.samp_preserv))

        if self.samp_room_id is not None and not isinstance(self.samp_room_id, TextValue):
            self.samp_room_id = TextValue(**as_dict(self.samp_room_id))

        if self.samp_size is not None and not isinstance(self.samp_size, QuantityValue):
            self.samp_size = QuantityValue(**as_dict(self.samp_size))

        if not isinstance(self.samp_sort_meth, list):
            self.samp_sort_meth = [self.samp_sort_meth] if self.samp_sort_meth is not None else []
        self.samp_sort_meth = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.samp_sort_meth]

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, TextValue):
            self.samp_store_dur = TextValue(**as_dict(self.samp_store_dur))

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, TextValue):
            self.samp_store_loc = TextValue(**as_dict(self.samp_store_loc))

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, QuantityValue):
            self.samp_store_temp = QuantityValue(**as_dict(self.samp_store_temp))

        if self.samp_subtype is not None and not isinstance(self.samp_subtype, SampSubtypeEnum):
            self.samp_subtype = SampSubtypeEnum(self.samp_subtype)

        if self.samp_taxon_id is not None and not isinstance(self.samp_taxon_id, ControlledIdentifiedTermValue):
            self.samp_taxon_id = ControlledIdentifiedTermValue(**as_dict(self.samp_taxon_id))

        if self.samp_time_out is not None and not isinstance(self.samp_time_out, TextValue):
            self.samp_time_out = TextValue(**as_dict(self.samp_time_out))

        if self.samp_transport_cond is not None and not isinstance(self.samp_transport_cond, TextValue):
            self.samp_transport_cond = TextValue(**as_dict(self.samp_transport_cond))

        if self.samp_tvdss is not None and not isinstance(self.samp_tvdss, TextValue):
            self.samp_tvdss = TextValue(**as_dict(self.samp_tvdss))

        if self.samp_type is not None and not isinstance(self.samp_type, TextValue):
            self.samp_type = TextValue(**as_dict(self.samp_type))

        if self.samp_weather is not None and not isinstance(self.samp_weather, SampWeatherEnum):
            self.samp_weather = SampWeatherEnum(self.samp_weather)

        if self.samp_well_name is not None and not isinstance(self.samp_well_name, TextValue):
            self.samp_well_name = TextValue(**as_dict(self.samp_well_name))

        if self.saturates_pc is not None and not isinstance(self.saturates_pc, TextValue):
            self.saturates_pc = TextValue(**as_dict(self.saturates_pc))

        if self.season is not None and not isinstance(self.season, TextValue):
            self.season = TextValue(**as_dict(self.season))

        if not isinstance(self.season_environment, list):
            self.season_environment = [self.season_environment] if self.season_environment is not None else []
        self.season_environment = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.season_environment]

        if self.season_precpt is not None and not isinstance(self.season_precpt, QuantityValue):
            self.season_precpt = QuantityValue(**as_dict(self.season_precpt))

        if self.season_temp is not None and not isinstance(self.season_temp, QuantityValue):
            self.season_temp = QuantityValue(**as_dict(self.season_temp))

        if self.season_use is not None and not isinstance(self.season_use, SeasonUseEnum):
            self.season_use = SeasonUseEnum(self.season_use)

        if self.secondary_treatment is not None and not isinstance(self.secondary_treatment, TextValue):
            self.secondary_treatment = TextValue(**as_dict(self.secondary_treatment))

        if self.sediment_type is not None and not isinstance(self.sediment_type, SedimentTypeEnum):
            self.sediment_type = SedimentTypeEnum(self.sediment_type)

        if self.sequencing_field is not None and not isinstance(self.sequencing_field, str):
            self.sequencing_field = str(self.sequencing_field)

        if self.sewage_type is not None and not isinstance(self.sewage_type, TextValue):
            self.sewage_type = TextValue(**as_dict(self.sewage_type))

        if self.shad_dev_water_mold is not None and not isinstance(self.shad_dev_water_mold, str):
            self.shad_dev_water_mold = str(self.shad_dev_water_mold)

        if self.shading_device_cond is not None and not isinstance(self.shading_device_cond, ShadingDeviceCondEnum):
            self.shading_device_cond = ShadingDeviceCondEnum(self.shading_device_cond)

        if self.shading_device_loc is not None and not isinstance(self.shading_device_loc, TextValue):
            self.shading_device_loc = TextValue(**as_dict(self.shading_device_loc))

        if self.shading_device_mat is not None and not isinstance(self.shading_device_mat, TextValue):
            self.shading_device_mat = TextValue(**as_dict(self.shading_device_mat))

        if self.shading_device_type is not None and not isinstance(self.shading_device_type, ShadingDeviceTypeEnum):
            self.shading_device_type = ShadingDeviceTypeEnum(self.shading_device_type)

        if self.sieving is not None and not isinstance(self.sieving, TextValue):
            self.sieving = TextValue(**as_dict(self.sieving))

        if self.silicate is not None and not isinstance(self.silicate, QuantityValue):
            self.silicate = QuantityValue(**as_dict(self.silicate))

        if self.size_frac is not None and not isinstance(self.size_frac, TextValue):
            self.size_frac = TextValue(**as_dict(self.size_frac))

        if self.size_frac_low is not None and not isinstance(self.size_frac_low, QuantityValue):
            self.size_frac_low = QuantityValue(**as_dict(self.size_frac_low))

        if self.size_frac_up is not None and not isinstance(self.size_frac_up, QuantityValue):
            self.size_frac_up = QuantityValue(**as_dict(self.size_frac_up))

        if self.slope_aspect is not None and not isinstance(self.slope_aspect, QuantityValue):
            self.slope_aspect = QuantityValue(**as_dict(self.slope_aspect))

        if self.slope_gradient is not None and not isinstance(self.slope_gradient, QuantityValue):
            self.slope_gradient = QuantityValue(**as_dict(self.slope_gradient))

        if self.sludge_retent_time is not None and not isinstance(self.sludge_retent_time, QuantityValue):
            self.sludge_retent_time = QuantityValue(**as_dict(self.sludge_retent_time))

        if self.sodium is not None and not isinstance(self.sodium, QuantityValue):
            self.sodium = QuantityValue(**as_dict(self.sodium))

        if self.soil_horizon is not None and not isinstance(self.soil_horizon, SoilHorizonEnum):
            self.soil_horizon = SoilHorizonEnum(self.soil_horizon)

        if self.soil_text_measure is not None and not isinstance(self.soil_text_measure, QuantityValue):
            self.soil_text_measure = QuantityValue(**as_dict(self.soil_text_measure))

        if self.soil_texture_meth is not None and not isinstance(self.soil_texture_meth, str):
            self.soil_texture_meth = str(self.soil_texture_meth)

        if self.soil_type is not None and not isinstance(self.soil_type, TextValue):
            self.soil_type = TextValue(**as_dict(self.soil_type))

        if self.soil_type_meth is not None and not isinstance(self.soil_type_meth, TextValue):
            self.soil_type_meth = TextValue(**as_dict(self.soil_type_meth))

        if self.solar_irradiance is not None and not isinstance(self.solar_irradiance, QuantityValue):
            self.solar_irradiance = QuantityValue(**as_dict(self.solar_irradiance))

        if not isinstance(self.soluble_inorg_mat, list):
            self.soluble_inorg_mat = [self.soluble_inorg_mat] if self.soluble_inorg_mat is not None else []
        self.soluble_inorg_mat = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.soluble_inorg_mat]

        if not isinstance(self.soluble_org_mat, list):
            self.soluble_org_mat = [self.soluble_org_mat] if self.soluble_org_mat is not None else []
        self.soluble_org_mat = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.soluble_org_mat]

        if self.soluble_react_phosp is not None and not isinstance(self.soluble_react_phosp, QuantityValue):
            self.soluble_react_phosp = QuantityValue(**as_dict(self.soluble_react_phosp))

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, TextValue):
            self.source_mat_id = TextValue(**as_dict(self.source_mat_id))

        if self.space_typ_state is not None and not isinstance(self.space_typ_state, TextValue):
            self.space_typ_state = TextValue(**as_dict(self.space_typ_state))

        if self.specific is not None and not isinstance(self.specific, SpecificEnum):
            self.specific = SpecificEnum(self.specific)

        if self.specific_ecosystem is not None and not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if self.specific_humidity is not None and not isinstance(self.specific_humidity, QuantityValue):
            self.specific_humidity = QuantityValue(**as_dict(self.specific_humidity))

        if self.sr_dep_env is not None and not isinstance(self.sr_dep_env, SrDepEnvEnum):
            self.sr_dep_env = SrDepEnvEnum(self.sr_dep_env)

        if self.sr_geol_age is not None and not isinstance(self.sr_geol_age, SrGeolAgeEnum):
            self.sr_geol_age = SrGeolAgeEnum(self.sr_geol_age)

        if self.sr_kerog_type is not None and not isinstance(self.sr_kerog_type, SrKerogTypeEnum):
            self.sr_kerog_type = SrKerogTypeEnum(self.sr_kerog_type)

        if self.sr_lithology is not None and not isinstance(self.sr_lithology, SrLithologyEnum):
            self.sr_lithology = SrLithologyEnum(self.sr_lithology)

        if not isinstance(self.standing_water_regm, list):
            self.standing_water_regm = [self.standing_water_regm] if self.standing_water_regm is not None else []
        self.standing_water_regm = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.standing_water_regm]

        if self.store_cond is not None and not isinstance(self.store_cond, TextValue):
            self.store_cond = TextValue(**as_dict(self.store_cond))

        if not isinstance(self.substructure_type, list):
            self.substructure_type = [self.substructure_type] if self.substructure_type is not None else []
        self.substructure_type = [v if isinstance(v, SubstructureTypeEnum) else SubstructureTypeEnum(v) for v in self.substructure_type]

        if self.sulfate is not None and not isinstance(self.sulfate, QuantityValue):
            self.sulfate = QuantityValue(**as_dict(self.sulfate))

        if self.sulfate_fw is not None and not isinstance(self.sulfate_fw, QuantityValue):
            self.sulfate_fw = QuantityValue(**as_dict(self.sulfate_fw))

        if self.sulfide is not None and not isinstance(self.sulfide, QuantityValue):
            self.sulfide = QuantityValue(**as_dict(self.sulfide))

        if not isinstance(self.surf_air_cont, list):
            self.surf_air_cont = [self.surf_air_cont] if self.surf_air_cont is not None else []
        self.surf_air_cont = [v if isinstance(v, SurfAirContEnum) else SurfAirContEnum(v) for v in self.surf_air_cont]

        if self.surf_humidity is not None and not isinstance(self.surf_humidity, QuantityValue):
            self.surf_humidity = QuantityValue(**as_dict(self.surf_humidity))

        if self.surf_material is not None and not isinstance(self.surf_material, SurfMaterialEnum):
            self.surf_material = SurfMaterialEnum(self.surf_material)

        if self.surf_moisture is not None and not isinstance(self.surf_moisture, QuantityValue):
            self.surf_moisture = QuantityValue(**as_dict(self.surf_moisture))

        if self.surf_moisture_ph is not None and not isinstance(self.surf_moisture_ph, float):
            self.surf_moisture_ph = float(self.surf_moisture_ph)

        if self.surf_temp is not None and not isinstance(self.surf_temp, QuantityValue):
            self.surf_temp = QuantityValue(**as_dict(self.surf_temp))

        if self.suspend_part_matter is not None and not isinstance(self.suspend_part_matter, QuantityValue):
            self.suspend_part_matter = QuantityValue(**as_dict(self.suspend_part_matter))

        if not isinstance(self.suspend_solids, list):
            self.suspend_solids = [self.suspend_solids] if self.suspend_solids is not None else []
        self.suspend_solids = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.suspend_solids]

        if self.tan is not None and not isinstance(self.tan, QuantityValue):
            self.tan = QuantityValue(**as_dict(self.tan))

        if self.temp is not None and not isinstance(self.temp, QuantityValue):
            self.temp = QuantityValue(**as_dict(self.temp))

        if self.temp_out is not None and not isinstance(self.temp_out, QuantityValue):
            self.temp_out = QuantityValue(**as_dict(self.temp_out))

        if self.tertiary_treatment is not None and not isinstance(self.tertiary_treatment, TextValue):
            self.tertiary_treatment = TextValue(**as_dict(self.tertiary_treatment))

        if self.tidal_stage is not None and not isinstance(self.tidal_stage, TidalStageEnum):
            self.tidal_stage = TidalStageEnum(self.tidal_stage)

        if not isinstance(self.tillage, list):
            self.tillage = [self.tillage] if self.tillage is not None else []
        self.tillage = [v if isinstance(v, TillageEnum) else TillageEnum(v) for v in self.tillage]

        if self.tiss_cult_growth_med is not None and not isinstance(self.tiss_cult_growth_med, TextValue):
            self.tiss_cult_growth_med = TextValue(**as_dict(self.tiss_cult_growth_med))

        if self.toluene is not None and not isinstance(self.toluene, QuantityValue):
            self.toluene = QuantityValue(**as_dict(self.toluene))

        if self.tot_carb is not None and not isinstance(self.tot_carb, QuantityValue):
            self.tot_carb = QuantityValue(**as_dict(self.tot_carb))

        if self.tot_depth_water_col is not None and not isinstance(self.tot_depth_water_col, QuantityValue):
            self.tot_depth_water_col = QuantityValue(**as_dict(self.tot_depth_water_col))

        if self.tot_diss_nitro is not None and not isinstance(self.tot_diss_nitro, QuantityValue):
            self.tot_diss_nitro = QuantityValue(**as_dict(self.tot_diss_nitro))

        if self.tot_inorg_nitro is not None and not isinstance(self.tot_inorg_nitro, QuantityValue):
            self.tot_inorg_nitro = QuantityValue(**as_dict(self.tot_inorg_nitro))

        if self.tot_iron is not None and not isinstance(self.tot_iron, QuantityValue):
            self.tot_iron = QuantityValue(**as_dict(self.tot_iron))

        if self.tot_nitro is not None and not isinstance(self.tot_nitro, QuantityValue):
            self.tot_nitro = QuantityValue(**as_dict(self.tot_nitro))

        if self.tot_nitro_cont_meth is not None and not isinstance(self.tot_nitro_cont_meth, str):
            self.tot_nitro_cont_meth = str(self.tot_nitro_cont_meth)

        if self.tot_nitro_content is not None and not isinstance(self.tot_nitro_content, QuantityValue):
            self.tot_nitro_content = QuantityValue(**as_dict(self.tot_nitro_content))

        if self.tot_org_c_meth is not None and not isinstance(self.tot_org_c_meth, TextValue):
            self.tot_org_c_meth = TextValue(**as_dict(self.tot_org_c_meth))

        if self.tot_org_carb is not None and not isinstance(self.tot_org_carb, QuantityValue):
            self.tot_org_carb = QuantityValue(**as_dict(self.tot_org_carb))

        if self.tot_part_carb is not None and not isinstance(self.tot_part_carb, QuantityValue):
            self.tot_part_carb = QuantityValue(**as_dict(self.tot_part_carb))

        if self.tot_phosp is not None and not isinstance(self.tot_phosp, QuantityValue):
            self.tot_phosp = QuantityValue(**as_dict(self.tot_phosp))

        if self.tot_phosphate is not None and not isinstance(self.tot_phosphate, QuantityValue):
            self.tot_phosphate = QuantityValue(**as_dict(self.tot_phosphate))

        if self.tot_sulfur is not None and not isinstance(self.tot_sulfur, QuantityValue):
            self.tot_sulfur = QuantityValue(**as_dict(self.tot_sulfur))

        if self.train_line is not None and not isinstance(self.train_line, TrainLineEnum):
            self.train_line = TrainLineEnum(self.train_line)

        if self.train_stat_loc is not None and not isinstance(self.train_stat_loc, TrainStatLocEnum):
            self.train_stat_loc = TrainStatLocEnum(self.train_stat_loc)

        if self.train_stop_loc is not None and not isinstance(self.train_stop_loc, TrainStopLocEnum):
            self.train_stop_loc = TrainStopLocEnum(self.train_stop_loc)

        if self.turbidity is not None and not isinstance(self.turbidity, QuantityValue):
            self.turbidity = QuantityValue(**as_dict(self.turbidity))

        if self.tvdss_of_hcr_press is not None and not isinstance(self.tvdss_of_hcr_press, QuantityValue):
            self.tvdss_of_hcr_press = QuantityValue(**as_dict(self.tvdss_of_hcr_press))

        if self.tvdss_of_hcr_temp is not None and not isinstance(self.tvdss_of_hcr_temp, QuantityValue):
            self.tvdss_of_hcr_temp = QuantityValue(**as_dict(self.tvdss_of_hcr_temp))

        if self.typ_occup_density is not None and not isinstance(self.typ_occup_density, float):
            self.typ_occup_density = float(self.typ_occup_density)

        if self.ventilation_rate is not None and not isinstance(self.ventilation_rate, QuantityValue):
            self.ventilation_rate = QuantityValue(**as_dict(self.ventilation_rate))

        if self.ventilation_type is not None and not isinstance(self.ventilation_type, TextValue):
            self.ventilation_type = TextValue(**as_dict(self.ventilation_type))

        if self.vfa is not None and not isinstance(self.vfa, QuantityValue):
            self.vfa = QuantityValue(**as_dict(self.vfa))

        if self.vfa_fw is not None and not isinstance(self.vfa_fw, QuantityValue):
            self.vfa_fw = QuantityValue(**as_dict(self.vfa_fw))

        if self.vis_media is not None and not isinstance(self.vis_media, VisMediaEnum):
            self.vis_media = VisMediaEnum(self.vis_media)

        if self.viscosity is not None and not isinstance(self.viscosity, TextValue):
            self.viscosity = TextValue(**as_dict(self.viscosity))

        if not isinstance(self.volatile_org_comp, list):
            self.volatile_org_comp = [self.volatile_org_comp] if self.volatile_org_comp is not None else []
        self.volatile_org_comp = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.volatile_org_comp]

        if self.wall_area is not None and not isinstance(self.wall_area, QuantityValue):
            self.wall_area = QuantityValue(**as_dict(self.wall_area))

        if self.wall_const_type is not None and not isinstance(self.wall_const_type, WallConstTypeEnum):
            self.wall_const_type = WallConstTypeEnum(self.wall_const_type)

        if self.wall_finish_mat is not None and not isinstance(self.wall_finish_mat, WallFinishMatEnum):
            self.wall_finish_mat = WallFinishMatEnum(self.wall_finish_mat)

        if self.wall_height is not None and not isinstance(self.wall_height, QuantityValue):
            self.wall_height = QuantityValue(**as_dict(self.wall_height))

        if self.wall_loc is not None and not isinstance(self.wall_loc, WallLocEnum):
            self.wall_loc = WallLocEnum(self.wall_loc)

        if self.wall_surf_treatment is not None and not isinstance(self.wall_surf_treatment, WallSurfTreatmentEnum):
            self.wall_surf_treatment = WallSurfTreatmentEnum(self.wall_surf_treatment)

        if self.wall_texture is not None and not isinstance(self.wall_texture, WallTextureEnum):
            self.wall_texture = WallTextureEnum(self.wall_texture)

        if self.wall_thermal_mass is not None and not isinstance(self.wall_thermal_mass, QuantityValue):
            self.wall_thermal_mass = QuantityValue(**as_dict(self.wall_thermal_mass))

        if self.wall_water_mold is not None and not isinstance(self.wall_water_mold, TextValue):
            self.wall_water_mold = TextValue(**as_dict(self.wall_water_mold))

        if self.wastewater_type is not None and not isinstance(self.wastewater_type, TextValue):
            self.wastewater_type = TextValue(**as_dict(self.wastewater_type))

        if self.water_cont_soil_meth is not None and not isinstance(self.water_cont_soil_meth, str):
            self.water_cont_soil_meth = str(self.water_cont_soil_meth)

        if not isinstance(self.water_content, list):
            self.water_content = [self.water_content] if self.water_content is not None else []
        self.water_content = [v if isinstance(v, str) else str(v) for v in self.water_content]

        if self.water_current is not None and not isinstance(self.water_current, QuantityValue):
            self.water_current = QuantityValue(**as_dict(self.water_current))

        if self.water_cut is not None and not isinstance(self.water_cut, QuantityValue):
            self.water_cut = QuantityValue(**as_dict(self.water_cut))

        if self.water_feat_size is not None and not isinstance(self.water_feat_size, QuantityValue):
            self.water_feat_size = QuantityValue(**as_dict(self.water_feat_size))

        if self.water_feat_type is not None and not isinstance(self.water_feat_type, WaterFeatTypeEnum):
            self.water_feat_type = WaterFeatTypeEnum(self.water_feat_type)

        if self.water_prod_rate is not None and not isinstance(self.water_prod_rate, QuantityValue):
            self.water_prod_rate = QuantityValue(**as_dict(self.water_prod_rate))

        if not isinstance(self.water_temp_regm, list):
            self.water_temp_regm = [self.water_temp_regm] if self.water_temp_regm is not None else []
        self.water_temp_regm = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.water_temp_regm]

        if not isinstance(self.watering_regm, list):
            self.watering_regm = [self.watering_regm] if self.watering_regm is not None else []
        self.watering_regm = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.watering_regm]

        if self.weekday is not None and not isinstance(self.weekday, WeekdayEnum):
            self.weekday = WeekdayEnum(self.weekday)

        if self.win is not None and not isinstance(self.win, TextValue):
            self.win = TextValue(**as_dict(self.win))

        if self.wind_direction is not None and not isinstance(self.wind_direction, TextValue):
            self.wind_direction = TextValue(**as_dict(self.wind_direction))

        if self.wind_speed is not None and not isinstance(self.wind_speed, QuantityValue):
            self.wind_speed = QuantityValue(**as_dict(self.wind_speed))

        if self.window_cond is not None and not isinstance(self.window_cond, WindowCondEnum):
            self.window_cond = WindowCondEnum(self.window_cond)

        if self.window_cover is not None and not isinstance(self.window_cover, WindowCoverEnum):
            self.window_cover = WindowCoverEnum(self.window_cover)

        if self.window_horiz_pos is not None and not isinstance(self.window_horiz_pos, WindowHorizPosEnum):
            self.window_horiz_pos = WindowHorizPosEnum(self.window_horiz_pos)

        if self.window_loc is not None and not isinstance(self.window_loc, WindowLocEnum):
            self.window_loc = WindowLocEnum(self.window_loc)

        if self.window_mat is not None and not isinstance(self.window_mat, WindowMatEnum):
            self.window_mat = WindowMatEnum(self.window_mat)

        if self.window_open_freq is not None and not isinstance(self.window_open_freq, TextValue):
            self.window_open_freq = TextValue(**as_dict(self.window_open_freq))

        if self.window_size is not None and not isinstance(self.window_size, TextValue):
            self.window_size = TextValue(**as_dict(self.window_size))

        if self.window_status is not None and not isinstance(self.window_status, TextValue):
            self.window_status = TextValue(**as_dict(self.window_status))

        if self.window_type is not None and not isinstance(self.window_type, WindowTypeEnum):
            self.window_type = WindowTypeEnum(self.window_type)

        if self.window_vert_pos is not None and not isinstance(self.window_vert_pos, WindowVertPosEnum):
            self.window_vert_pos = WindowVertPosEnum(self.window_vert_pos)

        if self.window_water_mold is not None and not isinstance(self.window_water_mold, TextValue):
            self.window_water_mold = TextValue(**as_dict(self.window_water_mold))

        if self.xylene is not None and not isinstance(self.xylene, QuantityValue):
            self.xylene = QuantityValue(**as_dict(self.xylene))

        if self.zinc is not None and not isinstance(self.zinc, QuantityValue):
            self.zinc = QuantityValue(**as_dict(self.zinc))

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

        if not isinstance(self.air_temp_regm, list):
            self.air_temp_regm = [self.air_temp_regm] if self.air_temp_regm is not None else []
        self.air_temp_regm = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.air_temp_regm]

        if self.biotic_regm is not None and not isinstance(self.biotic_regm, TextValue):
            self.biotic_regm = TextValue(**as_dict(self.biotic_regm))

        if self.biotic_relationship is not None and not isinstance(self.biotic_relationship, BioticRelationshipEnum):
            self.biotic_relationship = BioticRelationshipEnum(self.biotic_relationship)

        if not isinstance(self.climate_environment, list):
            self.climate_environment = [self.climate_environment] if self.climate_environment is not None else []
        self.climate_environment = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.climate_environment]

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, ControlledTermValue):
            self.experimental_factor = ControlledTermValue(**as_dict(self.experimental_factor))

        if not isinstance(self.gaseous_environment, list):
            self.gaseous_environment = [self.gaseous_environment] if self.gaseous_environment is not None else []
        self.gaseous_environment = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.gaseous_environment]

        if self.growth_facil is not None and not isinstance(self.growth_facil, ControlledTermValue):
            self.growth_facil = ControlledTermValue(**as_dict(self.growth_facil))

        if not isinstance(self.humidity_regm, list):
            self.humidity_regm = [self.humidity_regm] if self.humidity_regm is not None else []
        self.humidity_regm = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.humidity_regm]

        if self.light_regm is not None and not isinstance(self.light_regm, TextValue):
            self.light_regm = TextValue(**as_dict(self.light_regm))

        if self.phosphate is not None and not isinstance(self.phosphate, QuantityValue):
            self.phosphate = QuantityValue(**as_dict(self.phosphate))

        if self.samp_collec_method is not None and not isinstance(self.samp_collec_method, str):
            self.samp_collec_method = str(self.samp_collec_method)

        if self.samp_size is not None and not isinstance(self.samp_size, QuantityValue):
            self.samp_size = QuantityValue(**as_dict(self.samp_size))

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, TextValue):
            self.source_mat_id = TextValue(**as_dict(self.source_mat_id))

        if not isinstance(self.watering_regm, list):
            self.watering_regm = [self.watering_regm] if self.watering_regm is not None else []
        self.watering_regm = [v if isinstance(v, TextValue) else TextValue(**as_dict(v)) for v in self.watering_regm]

        if self.dna_absorb1 is not None and not isinstance(self.dna_absorb1, float):
            self.dna_absorb1 = float(self.dna_absorb1)

        if self.dna_absorb2 is not None and not isinstance(self.dna_absorb2, float):
            self.dna_absorb2 = float(self.dna_absorb2)

        if self.dna_collect_site is not None and not isinstance(self.dna_collect_site, str):
            self.dna_collect_site = str(self.dna_collect_site)

        if self.dna_concentration is not None and not isinstance(self.dna_concentration, float):
            self.dna_concentration = float(self.dna_concentration)

        if self.dna_cont_type is not None and not isinstance(self.dna_cont_type, JgiContTypeEnum):
            self.dna_cont_type = JgiContTypeEnum(self.dna_cont_type)

        if self.dna_cont_well is not None and not isinstance(self.dna_cont_well, str):
            self.dna_cont_well = str(self.dna_cont_well)

        if self.dna_container_id is not None and not isinstance(self.dna_container_id, str):
            self.dna_container_id = str(self.dna_container_id)

        if self.dna_dnase is not None and not isinstance(self.dna_dnase, YesNoEnum):
            self.dna_dnase = YesNoEnum(self.dna_dnase)

        if self.dna_isolate_meth is not None and not isinstance(self.dna_isolate_meth, str):
            self.dna_isolate_meth = str(self.dna_isolate_meth)

        if self.dna_organisms is not None and not isinstance(self.dna_organisms, str):
            self.dna_organisms = str(self.dna_organisms)

        if self.dna_project_contact is not None and not isinstance(self.dna_project_contact, str):
            self.dna_project_contact = str(self.dna_project_contact)

        if self.dna_samp_id is not None and not isinstance(self.dna_samp_id, str):
            self.dna_samp_id = str(self.dna_samp_id)

        if self.dna_sample_format is not None and not isinstance(self.dna_sample_format, DNASampleFormatEnum):
            self.dna_sample_format = DNASampleFormatEnum(self.dna_sample_format)

        if self.dna_sample_name is not None and not isinstance(self.dna_sample_name, str):
            self.dna_sample_name = str(self.dna_sample_name)

        if self.dna_seq_project is not None and not isinstance(self.dna_seq_project, str):
            self.dna_seq_project = str(self.dna_seq_project)

        if self.dna_seq_project_pi is not None and not isinstance(self.dna_seq_project_pi, str):
            self.dna_seq_project_pi = str(self.dna_seq_project_pi)

        if self.dna_seq_project_name is not None and not isinstance(self.dna_seq_project_name, str):
            self.dna_seq_project_name = str(self.dna_seq_project_name)

        if self.dna_volume is not None and not isinstance(self.dna_volume, float):
            self.dna_volume = float(self.dna_volume)

        if self.proposal_dna is not None and not isinstance(self.proposal_dna, str):
            self.proposal_dna = str(self.proposal_dna)

        if self.dnase_rna is not None and not isinstance(self.dnase_rna, YesNoEnum):
            self.dnase_rna = YesNoEnum(self.dnase_rna)

        if self.proposal_rna is not None and not isinstance(self.proposal_rna, str):
            self.proposal_rna = str(self.proposal_rna)

        if self.rna_absorb1 is not None and not isinstance(self.rna_absorb1, float):
            self.rna_absorb1 = float(self.rna_absorb1)

        if self.rna_absorb2 is not None and not isinstance(self.rna_absorb2, float):
            self.rna_absorb2 = float(self.rna_absorb2)

        if self.rna_collect_site is not None and not isinstance(self.rna_collect_site, str):
            self.rna_collect_site = str(self.rna_collect_site)

        if self.rna_concentration is not None and not isinstance(self.rna_concentration, float):
            self.rna_concentration = float(self.rna_concentration)

        if self.rna_cont_type is not None and not isinstance(self.rna_cont_type, JgiContTypeEnum):
            self.rna_cont_type = JgiContTypeEnum(self.rna_cont_type)

        if self.rna_cont_well is not None and not isinstance(self.rna_cont_well, str):
            self.rna_cont_well = str(self.rna_cont_well)

        if self.rna_container_id is not None and not isinstance(self.rna_container_id, str):
            self.rna_container_id = str(self.rna_container_id)

        if self.rna_isolate_meth is not None and not isinstance(self.rna_isolate_meth, str):
            self.rna_isolate_meth = str(self.rna_isolate_meth)

        if self.rna_organisms is not None and not isinstance(self.rna_organisms, str):
            self.rna_organisms = str(self.rna_organisms)

        if self.rna_project_contact is not None and not isinstance(self.rna_project_contact, str):
            self.rna_project_contact = str(self.rna_project_contact)

        if self.rna_samp_id is not None and not isinstance(self.rna_samp_id, str):
            self.rna_samp_id = str(self.rna_samp_id)

        if self.rna_sample_format is not None and not isinstance(self.rna_sample_format, RNASampleFormatEnum):
            self.rna_sample_format = RNASampleFormatEnum(self.rna_sample_format)

        if self.rna_sample_name is not None and not isinstance(self.rna_sample_name, str):
            self.rna_sample_name = str(self.rna_sample_name)

        if self.rna_seq_project is not None and not isinstance(self.rna_seq_project, str):
            self.rna_seq_project = str(self.rna_seq_project)

        if self.rna_seq_project_pi is not None and not isinstance(self.rna_seq_project_pi, str):
            self.rna_seq_project_pi = str(self.rna_seq_project_pi)

        if self.rna_seq_project_name is not None and not isinstance(self.rna_seq_project_name, str):
            self.rna_seq_project_name = str(self.rna_seq_project_name)

        if self.rna_volume is not None and not isinstance(self.rna_volume, float):
            self.rna_volume = float(self.rna_volume)

        if self.collection_date_inc is not None and not isinstance(self.collection_date_inc, str):
            self.collection_date_inc = str(self.collection_date_inc)

        if self.collection_time is not None and not isinstance(self.collection_time, str):
            self.collection_time = str(self.collection_time)

        if self.collection_time_inc is not None and not isinstance(self.collection_time_inc, str):
            self.collection_time_inc = str(self.collection_time_inc)

        if self.experimental_factor_other is not None and not isinstance(self.experimental_factor_other, str):
            self.experimental_factor_other = str(self.experimental_factor_other)

        if self.filter_method is not None and not isinstance(self.filter_method, str):
            self.filter_method = str(self.filter_method)

        if self.isotope_exposure is not None and not isinstance(self.isotope_exposure, str):
            self.isotope_exposure = str(self.isotope_exposure)

        if self.micro_biomass_c_meth is not None and not isinstance(self.micro_biomass_c_meth, str):
            self.micro_biomass_c_meth = str(self.micro_biomass_c_meth)

        if self.micro_biomass_n_meth is not None and not isinstance(self.micro_biomass_n_meth, str):
            self.micro_biomass_n_meth = str(self.micro_biomass_n_meth)

        if self.microbial_biomass_c is not None and not isinstance(self.microbial_biomass_c, str):
            self.microbial_biomass_c = str(self.microbial_biomass_c)

        if self.microbial_biomass_n is not None and not isinstance(self.microbial_biomass_n, str):
            self.microbial_biomass_n = str(self.microbial_biomass_n)

        if self.non_microb_biomass is not None and not isinstance(self.non_microb_biomass, str):
            self.non_microb_biomass = str(self.non_microb_biomass)

        if self.non_microb_biomass_method is not None and not isinstance(self.non_microb_biomass_method, str):
            self.non_microb_biomass_method = str(self.non_microb_biomass_method)

        if self.org_nitro_method is not None and not isinstance(self.org_nitro_method, str):
            self.org_nitro_method = str(self.org_nitro_method)

        if self.other_treatment is not None and not isinstance(self.other_treatment, str):
            self.other_treatment = str(self.other_treatment)

        if self.start_date_inc is not None and not isinstance(self.start_date_inc, str):
            self.start_date_inc = str(self.start_date_inc)

        if self.start_time_inc is not None and not isinstance(self.start_time_inc, str):
            self.start_time_inc = str(self.start_time_inc)

        if self.project_id is not None and not isinstance(self.project_id, str):
            self.project_id = str(self.project_id)

        if self.replicate_number is not None and not isinstance(self.replicate_number, str):
            self.replicate_number = str(self.replicate_number)

        if self.sample_shipped is not None and not isinstance(self.sample_shipped, str):
            self.sample_shipped = str(self.sample_shipped)

        if self.sample_type is not None and not isinstance(self.sample_type, SampleTypeEnum):
            self.sample_type = SampleTypeEnum(self.sample_type)

        if self.technical_reps is not None and not isinstance(self.technical_reps, str):
            self.technical_reps = str(self.technical_reps)

        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

        if not isinstance(self.sample_link, list):
            self.sample_link = [self.sample_link] if self.sample_link is not None else []
        self.sample_link = [v if isinstance(v, str) else str(v) for v in self.sample_link]

        if self.bulk_elect_conductivity is not None and not isinstance(self.bulk_elect_conductivity, QuantityValue):
            self.bulk_elect_conductivity = QuantityValue(**as_dict(self.bulk_elect_conductivity))

        if not isinstance(self.infiltrations, list):
            self.infiltrations = [self.infiltrations] if self.infiltrations is not None else []
        self.infiltrations = [v if isinstance(v, str) else str(v) for v in self.infiltrations]

        if self.zinc is not None and not isinstance(self.zinc, QuantityValue):
            self.zinc = QuantityValue(**as_dict(self.zinc))

        if self.manganese is not None and not isinstance(self.manganese, QuantityValue):
            self.manganese = QuantityValue(**as_dict(self.manganese))

        if self.ammonium_nitrogen is not None and not isinstance(self.ammonium_nitrogen, QuantityValue):
            self.ammonium_nitrogen = QuantityValue(**as_dict(self.ammonium_nitrogen))

        if self.nitrate_nitrogen is not None and not isinstance(self.nitrate_nitrogen, QuantityValue):
            self.nitrate_nitrogen = QuantityValue(**as_dict(self.nitrate_nitrogen))

        if self.nitrite_nitrogen is not None and not isinstance(self.nitrite_nitrogen, QuantityValue):
            self.nitrite_nitrogen = QuantityValue(**as_dict(self.nitrite_nitrogen))

        if self.lbc_thirty is not None and not isinstance(self.lbc_thirty, QuantityValue):
            self.lbc_thirty = QuantityValue(**as_dict(self.lbc_thirty))

        if self.lbceq is not None and not isinstance(self.lbceq, QuantityValue):
            self.lbceq = QuantityValue(**as_dict(self.lbceq))

        if not isinstance(self.alternative_identifiers, list):
            self.alternative_identifiers = [self.alternative_identifiers] if self.alternative_identifiers is not None else []
        self.alternative_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.alternative_identifiers]

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class ProcessedSample(MaterialEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["ProcessedSample"]
    class_class_curie: ClassVar[str] = "nmdc:ProcessedSample"
    class_name: ClassVar[str] = "ProcessedSample"
    class_model_uri: ClassVar[URIRef] = NMDC.ProcessedSample

    id: Union[str, ProcessedSampleId] = None
    type: Union[str, URIorCURIE] = None
    biomaterial_purity: Optional[Union[dict, QuantityValue]] = None
    dna_absorb1: Optional[float] = None
    dna_concentration: Optional[float] = None
    external_database_identifiers: Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProcessedSampleId):
            self.id = ProcessedSampleId(self.id)

        if self.biomaterial_purity is not None and not isinstance(self.biomaterial_purity, QuantityValue):
            self.biomaterial_purity = QuantityValue(**as_dict(self.biomaterial_purity))

        if self.dna_absorb1 is not None and not isinstance(self.dna_absorb1, float):
            self.dna_absorb1 = float(self.dna_absorb1)

        if self.dna_concentration is not None and not isinstance(self.dna_concentration, float):
            self.dna_concentration = float(self.dna_concentration)

        if not isinstance(self.external_database_identifiers, list):
            self.external_database_identifiers = [self.external_database_identifiers] if self.external_database_identifiers is not None else []
        self.external_database_identifiers = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(v) for v in self.external_database_identifiers]

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class Site(MaterialEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["Site"]
    class_class_curie: ClassVar[str] = "nmdc:Site"
    class_name: ClassVar[str] = "Site"
    class_model_uri: ClassVar[URIRef] = NMDC.Site

    id: Union[str, SiteId] = None
    type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class FieldResearchSite(Site):
    """
    A site, outside of a laboratory, from which biosamples may be collected.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["FieldResearchSite"]
    class_class_curie: ClassVar[str] = "nmdc:FieldResearchSite"
    class_name: ClassVar[str] = "FieldResearchSite"
    class_model_uri: ClassVar[URIRef] = NMDC.FieldResearchSite

    id: Union[str, FieldResearchSiteId] = None
    type: Union[str, URIorCURIE] = None
    cur_vegetation: Optional[Union[dict, TextValue]] = None
    elev: Optional[float] = None
    geo_loc_name: Optional[Union[dict, TextValue]] = None
    habitat: Optional[str] = None
    lat_lon: Optional[Union[dict, GeolocationValue]] = None
    local_class: Optional[Union[dict, TextValue]] = None
    part_of: Optional[Union[Union[str, FieldResearchSiteId], List[Union[str, FieldResearchSiteId]]]] = empty_list()
    soil_type: Optional[Union[dict, TextValue]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FieldResearchSiteId):
            self.id = FieldResearchSiteId(self.id)

        if self.cur_vegetation is not None and not isinstance(self.cur_vegetation, TextValue):
            self.cur_vegetation = TextValue(**as_dict(self.cur_vegetation))

        if self.elev is not None and not isinstance(self.elev, float):
            self.elev = float(self.elev)

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, TextValue):
            self.geo_loc_name = TextValue(**as_dict(self.geo_loc_name))

        if self.habitat is not None and not isinstance(self.habitat, str):
            self.habitat = str(self.habitat)

        if self.lat_lon is not None and not isinstance(self.lat_lon, GeolocationValue):
            self.lat_lon = GeolocationValue(**as_dict(self.lat_lon))

        if self.local_class is not None and not isinstance(self.local_class, TextValue):
            self.local_class = TextValue(**as_dict(self.local_class))

        if not isinstance(self.part_of, list):
            self.part_of = [self.part_of] if self.part_of is not None else []
        self.part_of = [v if isinstance(v, FieldResearchSiteId) else FieldResearchSiteId(v) for v in self.part_of]

        if self.soil_type is not None and not isinstance(self.soil_type, TextValue):
            self.soil_type = TextValue(**as_dict(self.soil_type))

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class Instrument(MaterialEntity):
    """
    A material entity that is designed to perform a function in a scientific investigation, but is not a reagent.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["Instrument"]
    class_class_curie: ClassVar[str] = "nmdc:Instrument"
    class_name: ClassVar[str] = "Instrument"
    class_model_uri: ClassVar[URIRef] = NMDC.Instrument

    id: Union[str, InstrumentId] = None
    type: Union[str, URIorCURIE] = None
    vendor: Optional[Union[str, "InstrumentVendorEnum"]] = None
    model: Optional[Union[str, "InstrumentModelEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InstrumentId):
            self.id = InstrumentId(self.id)

        if self.vendor is not None and not isinstance(self.vendor, InstrumentVendorEnum):
            self.vendor = InstrumentVendorEnum(self.vendor)

        if self.model is not None and not isinstance(self.model, InstrumentModelEnum):
            self.model = InstrumentModelEnum(self.model)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class PlannedProcess(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000011"]
    class_class_curie: ClassVar[str] = "OBI:0000011"
    class_name: ClassVar[str] = "PlannedProcess"
    class_model_uri: ClassVar[URIRef] = NMDC.PlannedProcess

    id: Union[str, PlannedProcessId] = None
    type: Union[str, URIorCURIE] = None
    has_input: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()
    has_output: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()
    processing_institution: Optional[Union[str, "ProcessingInstitutionEnum"]] = None
    protocol_link: Optional[Union[dict, "Protocol"]] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    qc_status: Optional[Union[str, "StatusEnum"]] = None
    qc_comment: Optional[str] = None
    has_failure_categorization: Optional[Union[Union[dict, FailureCategorization], List[Union[dict, FailureCategorization]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
        self.has_input = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_input]

        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output] if self.has_output is not None else []
        self.has_output = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_output]

        if self.processing_institution is not None and not isinstance(self.processing_institution, ProcessingInstitutionEnum):
            self.processing_institution = ProcessingInstitutionEnum(self.processing_institution)

        if self.protocol_link is not None and not isinstance(self.protocol_link, Protocol):
            self.protocol_link = Protocol(**as_dict(self.protocol_link))

        if self.start_date is not None and not isinstance(self.start_date, str):
            self.start_date = str(self.start_date)

        if self.end_date is not None and not isinstance(self.end_date, str):
            self.end_date = str(self.end_date)

        if self.qc_status is not None and not isinstance(self.qc_status, StatusEnum):
            self.qc_status = StatusEnum(self.qc_status)

        if self.qc_comment is not None and not isinstance(self.qc_comment, str):
            self.qc_comment = str(self.qc_comment)

        if not isinstance(self.has_failure_categorization, list):
            self.has_failure_categorization = [self.has_failure_categorization] if self.has_failure_categorization is not None else []
        self.has_failure_categorization = [v if isinstance(v, FailureCategorization) else FailureCategorization(**as_dict(v)) for v in self.has_failure_categorization]

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class CollectingBiosamplesFromSite(PlannedProcess):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["CollectingBiosamplesFromSite"]
    class_class_curie: ClassVar[str] = "nmdc:CollectingBiosamplesFromSite"
    class_name: ClassVar[str] = "CollectingBiosamplesFromSite"
    class_model_uri: ClassVar[URIRef] = NMDC.CollectingBiosamplesFromSite

    id: Union[str, CollectingBiosamplesFromSiteId] = None
    type: Union[str, URIorCURIE] = None
    has_input: Union[Union[str, SiteId], List[Union[str, SiteId]]] = None
    has_output: Union[Union[str, BiosampleId], List[Union[str, BiosampleId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CollectingBiosamplesFromSiteId):
            self.id = CollectingBiosamplesFromSiteId(self.id)

        if self._is_empty(self.has_input):
            self.MissingRequiredField("has_input")
        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
        self.has_input = [v if isinstance(v, SiteId) else SiteId(v) for v in self.has_input]

        if self._is_empty(self.has_output):
            self.MissingRequiredField("has_output")
        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output] if self.has_output is not None else []
        self.has_output = [v if isinstance(v, BiosampleId) else BiosampleId(v) for v in self.has_output]

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class ProtocolExecution(PlannedProcess):
    """
    A PlannedProces that has PlannedProcess parts. Can be used to represent the case of someone following a Protocol.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["ProtocolExecution"]
    class_class_curie: ClassVar[str] = "nmdc:ProtocolExecution"
    class_name: ClassVar[str] = "ProtocolExecution"
    class_model_uri: ClassVar[URIRef] = NMDC.ProtocolExecution

    id: Union[str, ProtocolExecutionId] = None
    type: Union[str, URIorCURIE] = None
    has_process_parts: Union[Union[str, PlannedProcessId], List[Union[str, PlannedProcessId]]] = None
    protocol_execution_category: Union[str, "ProtocolCategoryEnum"] = None
    has_input: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()
    has_output: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProtocolExecutionId):
            self.id = ProtocolExecutionId(self.id)

        if self._is_empty(self.has_process_parts):
            self.MissingRequiredField("has_process_parts")
        if not isinstance(self.has_process_parts, list):
            self.has_process_parts = [self.has_process_parts] if self.has_process_parts is not None else []
        self.has_process_parts = [v if isinstance(v, PlannedProcessId) else PlannedProcessId(v) for v in self.has_process_parts]

        if self._is_empty(self.protocol_execution_category):
            self.MissingRequiredField("protocol_execution_category")
        if not isinstance(self.protocol_execution_category, ProtocolCategoryEnum):
            self.protocol_execution_category = ProtocolCategoryEnum(self.protocol_execution_category)

        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
        self.has_input = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_input]

        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output] if self.has_output is not None else []
        self.has_output = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_output]

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class StorageProcess(PlannedProcess):
    """
    A planned process with the objective to preserve and protect material entities by placing them in an identified
    location which may have a controlled environment.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["StorageProcess"]
    class_class_curie: ClassVar[str] = "nmdc:StorageProcess"
    class_name: ClassVar[str] = "StorageProcess"
    class_model_uri: ClassVar[URIRef] = NMDC.StorageProcess

    id: Union[str, StorageProcessId] = None
    type: Union[str, URIorCURIE] = None
    substances_used: Optional[Union[Union[dict, PortionOfSubstance], List[Union[dict, PortionOfSubstance]]]] = empty_list()
    contained_in: Optional[Union[str, "ContainerCategoryEnum"]] = None
    temperature: Optional[Union[dict, QuantityValue]] = None
    has_input: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()
    has_output: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StorageProcessId):
            self.id = StorageProcessId(self.id)

        if not isinstance(self.substances_used, list):
            self.substances_used = [self.substances_used] if self.substances_used is not None else []
        self.substances_used = [v if isinstance(v, PortionOfSubstance) else PortionOfSubstance(**as_dict(v)) for v in self.substances_used]

        if self.contained_in is not None and not isinstance(self.contained_in, ContainerCategoryEnum):
            self.contained_in = ContainerCategoryEnum(self.contained_in)

        if self.temperature is not None and not isinstance(self.temperature, QuantityValue):
            self.temperature = QuantityValue(**as_dict(self.temperature))

        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
        self.has_input = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_input]

        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output] if self.has_output is not None else []
        self.has_output = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_output]

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class MaterialProcessing(PlannedProcess):
    """
    A process that takes one or more samples as inputs and generates one or more samples as outputs.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["MaterialProcessing"]
    class_class_curie: ClassVar[str] = "nmdc:MaterialProcessing"
    class_name: ClassVar[str] = "MaterialProcessing"
    class_model_uri: ClassVar[URIRef] = NMDC.MaterialProcessing

    id: Union[str, MaterialProcessingId] = None
    type: Union[str, URIorCURIE] = None
    instrument_used: Optional[Union[Union[str, InstrumentId], List[Union[str, InstrumentId]]]] = empty_list()
    has_input: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()
    has_output: Optional[Union[Union[str, ProcessedSampleId], List[Union[str, ProcessedSampleId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.instrument_used, list):
            self.instrument_used = [self.instrument_used] if self.instrument_used is not None else []
        self.instrument_used = [v if isinstance(v, InstrumentId) else InstrumentId(v) for v in self.instrument_used]

        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
        self.has_input = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_input]

        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output] if self.has_output is not None else []
        self.has_output = [v if isinstance(v, ProcessedSampleId) else ProcessedSampleId(v) for v in self.has_output]

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class Pooling(MaterialProcessing):
    """
    physical combination of several instances of like material.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["Pooling"]
    class_class_curie: ClassVar[str] = "nmdc:Pooling"
    class_name: ClassVar[str] = "Pooling"
    class_model_uri: ClassVar[URIRef] = NMDC.Pooling

    id: Union[str, PoolingId] = None
    type: Union[str, URIorCURIE] = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_output: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PoolingId):
            self.id = PoolingId(self.id)

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

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class Extraction(MaterialProcessing):
    """
    A material separation in which a desired component of an input material is separated from the remainder.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["Extraction"]
    class_class_curie: ClassVar[str] = "nmdc:Extraction"
    class_name: ClassVar[str] = "Extraction"
    class_model_uri: ClassVar[URIRef] = NMDC.Extraction

    id: Union[str, ExtractionId] = None
    type: Union[str, URIorCURIE] = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_output: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    substances_used: Optional[Union[Union[dict, PortionOfSubstance], List[Union[dict, PortionOfSubstance]]]] = empty_list()
    extraction_targets: Optional[Union[Union[str, "ExtractionTargetEnum"], List[Union[str, "ExtractionTargetEnum"]]]] = empty_list()
    input_mass: Optional[Union[dict, QuantityValue]] = None
    volume: Optional[Union[dict, QuantityValue]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExtractionId):
            self.id = ExtractionId(self.id)

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

        if not isinstance(self.substances_used, list):
            self.substances_used = [self.substances_used] if self.substances_used is not None else []
        self.substances_used = [v if isinstance(v, PortionOfSubstance) else PortionOfSubstance(**as_dict(v)) for v in self.substances_used]

        if not isinstance(self.extraction_targets, list):
            self.extraction_targets = [self.extraction_targets] if self.extraction_targets is not None else []
        self.extraction_targets = [v if isinstance(v, ExtractionTargetEnum) else ExtractionTargetEnum(v) for v in self.extraction_targets]

        if self.input_mass is not None and not isinstance(self.input_mass, QuantityValue):
            self.input_mass = QuantityValue(**as_dict(self.input_mass))

        if self.volume is not None and not isinstance(self.volume, QuantityValue):
            self.volume = QuantityValue(**as_dict(self.volume))

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class LibraryPreparation(MaterialProcessing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["LibraryPreparation"]
    class_class_curie: ClassVar[str] = "nmdc:LibraryPreparation"
    class_name: ClassVar[str] = "LibraryPreparation"
    class_model_uri: ClassVar[URIRef] = NMDC.LibraryPreparation

    id: Union[str, LibraryPreparationId] = None
    type: Union[str, URIorCURIE] = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_output: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    library_preparation_kit: Optional[str] = None
    library_type: Optional[Union[str, "LibraryTypeEnum"]] = None
    pcr_cycles: Optional[int] = None
    nucl_acid_amp: Optional[Union[dict, TextValue]] = None
    pcr_cond: Optional[Union[dict, TextValue]] = None
    pcr_primers: Optional[Union[dict, TextValue]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LibraryPreparationId):
            self.id = LibraryPreparationId(self.id)

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

        if self.library_preparation_kit is not None and not isinstance(self.library_preparation_kit, str):
            self.library_preparation_kit = str(self.library_preparation_kit)

        if self.library_type is not None and not isinstance(self.library_type, LibraryTypeEnum):
            self.library_type = LibraryTypeEnum(self.library_type)

        if self.pcr_cycles is not None and not isinstance(self.pcr_cycles, int):
            self.pcr_cycles = int(self.pcr_cycles)

        if self.nucl_acid_amp is not None and not isinstance(self.nucl_acid_amp, TextValue):
            self.nucl_acid_amp = TextValue(**as_dict(self.nucl_acid_amp))

        if self.pcr_cond is not None and not isinstance(self.pcr_cond, TextValue):
            self.pcr_cond = TextValue(**as_dict(self.pcr_cond))

        if self.pcr_primers is not None and not isinstance(self.pcr_primers, TextValue):
            self.pcr_primers = TextValue(**as_dict(self.pcr_primers))

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class SubSamplingProcess(MaterialProcessing):
    """
    Separating a sample aliquot from the starting material for downstream activity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["SubSamplingProcess"]
    class_class_curie: ClassVar[str] = "nmdc:SubSamplingProcess"
    class_name: ClassVar[str] = "SubSamplingProcess"
    class_model_uri: ClassVar[URIRef] = NMDC.SubSamplingProcess

    id: Union[str, SubSamplingProcessId] = None
    type: Union[str, URIorCURIE] = None
    container_size: Optional[Union[dict, QuantityValue]] = None
    contained_in: Optional[Union[str, "ContainerCategoryEnum"]] = None
    temperature: Optional[Union[dict, QuantityValue]] = None
    volume: Optional[Union[dict, QuantityValue]] = None
    mass: Optional[Union[dict, QuantityValue]] = None
    sampled_portion: Optional[Union[Union[str, "SamplePortionEnum"], List[Union[str, "SamplePortionEnum"]]]] = empty_list()
    has_input: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()
    has_output: Optional[Union[Union[str, ProcessedSampleId], List[Union[str, ProcessedSampleId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SubSamplingProcessId):
            self.id = SubSamplingProcessId(self.id)

        if self.container_size is not None and not isinstance(self.container_size, QuantityValue):
            self.container_size = QuantityValue(**as_dict(self.container_size))

        if self.contained_in is not None and not isinstance(self.contained_in, ContainerCategoryEnum):
            self.contained_in = ContainerCategoryEnum(self.contained_in)

        if self.temperature is not None and not isinstance(self.temperature, QuantityValue):
            self.temperature = QuantityValue(**as_dict(self.temperature))

        if self.volume is not None and not isinstance(self.volume, QuantityValue):
            self.volume = QuantityValue(**as_dict(self.volume))

        if self.mass is not None and not isinstance(self.mass, QuantityValue):
            self.mass = QuantityValue(**as_dict(self.mass))

        if not isinstance(self.sampled_portion, list):
            self.sampled_portion = [self.sampled_portion] if self.sampled_portion is not None else []
        self.sampled_portion = [v if isinstance(v, SamplePortionEnum) else SamplePortionEnum(v) for v in self.sampled_portion]

        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
        self.has_input = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_input]

        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output] if self.has_output is not None else []
        self.has_output = [v if isinstance(v, ProcessedSampleId) else ProcessedSampleId(v) for v in self.has_output]

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class MixingProcess(MaterialProcessing):
    """
    The combining of components, particles or layers into a more homogeneous state.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["MixingProcess"]
    class_class_curie: ClassVar[str] = "nmdc:MixingProcess"
    class_name: ClassVar[str] = "MixingProcess"
    class_model_uri: ClassVar[URIRef] = NMDC.MixingProcess

    id: Union[str, MixingProcessId] = None
    type: Union[str, URIorCURIE] = None
    duration: Optional[Union[dict, QuantityValue]] = None
    has_input: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()
    has_output: Optional[Union[Union[str, ProcessedSampleId], List[Union[str, ProcessedSampleId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MixingProcessId):
            self.id = MixingProcessId(self.id)

        if self.duration is not None and not isinstance(self.duration, QuantityValue):
            self.duration = QuantityValue(**as_dict(self.duration))

        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
        self.has_input = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_input]

        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output] if self.has_output is not None else []
        self.has_output = [v if isinstance(v, ProcessedSampleId) else ProcessedSampleId(v) for v in self.has_output]

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class FiltrationProcess(MaterialProcessing):
    """
    The process of segregation of phases; e.g. the separation of suspended solids from a liquid or gas, usually by
    forcing a carrier gas or liquid through a porous medium.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["FiltrationProcess"]
    class_class_curie: ClassVar[str] = "nmdc:FiltrationProcess"
    class_name: ClassVar[str] = "FiltrationProcess"
    class_model_uri: ClassVar[URIRef] = NMDC.FiltrationProcess

    id: Union[str, FiltrationProcessId] = None
    type: Union[str, URIorCURIE] = None
    conditionings: Optional[Union[str, List[str]]] = empty_list()
    container_size: Optional[Union[dict, QuantityValue]] = None
    filter_material: Optional[str] = None
    filter_pore_size: Optional[Union[dict, QuantityValue]] = None
    filtration_category: Optional[str] = None
    is_pressurized: Optional[Union[bool, Bool]] = None
    separation_method: Optional[Union[str, "SeparationMethodEnum"]] = None
    volume: Optional[Union[dict, QuantityValue]] = None
    has_input: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()
    has_output: Optional[Union[Union[str, ProcessedSampleId], List[Union[str, ProcessedSampleId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FiltrationProcessId):
            self.id = FiltrationProcessId(self.id)

        if not isinstance(self.conditionings, list):
            self.conditionings = [self.conditionings] if self.conditionings is not None else []
        self.conditionings = [v if isinstance(v, str) else str(v) for v in self.conditionings]

        if self.container_size is not None and not isinstance(self.container_size, QuantityValue):
            self.container_size = QuantityValue(**as_dict(self.container_size))

        if self.filter_material is not None and not isinstance(self.filter_material, str):
            self.filter_material = str(self.filter_material)

        if self.filter_pore_size is not None and not isinstance(self.filter_pore_size, QuantityValue):
            self.filter_pore_size = QuantityValue(**as_dict(self.filter_pore_size))

        if self.filtration_category is not None and not isinstance(self.filtration_category, str):
            self.filtration_category = str(self.filtration_category)

        if self.is_pressurized is not None and not isinstance(self.is_pressurized, Bool):
            self.is_pressurized = Bool(self.is_pressurized)

        if self.separation_method is not None and not isinstance(self.separation_method, SeparationMethodEnum):
            self.separation_method = SeparationMethodEnum(self.separation_method)

        if self.volume is not None and not isinstance(self.volume, QuantityValue):
            self.volume = QuantityValue(**as_dict(self.volume))

        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
        self.has_input = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_input]

        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output] if self.has_output is not None else []
        self.has_output = [v if isinstance(v, ProcessedSampleId) else ProcessedSampleId(v) for v in self.has_output]

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class ChromatographicSeparationProcess(MaterialProcessing):
    """
    The process of using a selective partitioning of the analyte or interferent between two immiscible phases.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["ChromatographicSeparationProcess"]
    class_class_curie: ClassVar[str] = "nmdc:ChromatographicSeparationProcess"
    class_name: ClassVar[str] = "ChromatographicSeparationProcess"
    class_model_uri: ClassVar[URIRef] = NMDC.ChromatographicSeparationProcess

    id: Union[str, ChromatographicSeparationProcessId] = None
    type: Union[str, URIorCURIE] = None
    chromatographic_category: Optional[Union[str, "ChromatographicCategoryEnum"]] = None
    ordered_mobile_phases: Optional[Union[Union[dict, MobilePhaseSegment], List[Union[dict, MobilePhaseSegment]]]] = empty_list()
    stationary_phase: Optional[Union[str, "StationaryPhaseEnum"]] = None
    temperature: Optional[Union[dict, QuantityValue]] = None
    has_input: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()
    has_output: Optional[Union[Union[str, ProcessedSampleId], List[Union[str, ProcessedSampleId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChromatographicSeparationProcessId):
            self.id = ChromatographicSeparationProcessId(self.id)

        if self.chromatographic_category is not None and not isinstance(self.chromatographic_category, ChromatographicCategoryEnum):
            self.chromatographic_category = ChromatographicCategoryEnum(self.chromatographic_category)

        if not isinstance(self.ordered_mobile_phases, list):
            self.ordered_mobile_phases = [self.ordered_mobile_phases] if self.ordered_mobile_phases is not None else []
        self.ordered_mobile_phases = [v if isinstance(v, MobilePhaseSegment) else MobilePhaseSegment(**as_dict(v)) for v in self.ordered_mobile_phases]

        if self.stationary_phase is not None and not isinstance(self.stationary_phase, StationaryPhaseEnum):
            self.stationary_phase = StationaryPhaseEnum(self.stationary_phase)

        if self.temperature is not None and not isinstance(self.temperature, QuantityValue):
            self.temperature = QuantityValue(**as_dict(self.temperature))

        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
        self.has_input = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_input]

        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output] if self.has_output is not None else []
        self.has_output = [v if isinstance(v, ProcessedSampleId) else ProcessedSampleId(v) for v in self.has_output]

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class DissolvingProcess(MaterialProcessing):
    """
    A mixing step where a soluble component is mixed with a liquid component.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["DissolvingProcess"]
    class_class_curie: ClassVar[str] = "nmdc:DissolvingProcess"
    class_name: ClassVar[str] = "DissolvingProcess"
    class_model_uri: ClassVar[URIRef] = NMDC.DissolvingProcess

    id: Union[str, DissolvingProcessId] = None
    type: Union[str, URIorCURIE] = None
    duration: Optional[Union[dict, QuantityValue]] = None
    temperature: Optional[Union[dict, QuantityValue]] = None
    substances_used: Optional[Union[Union[dict, PortionOfSubstance], List[Union[dict, PortionOfSubstance]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DissolvingProcessId):
            self.id = DissolvingProcessId(self.id)

        if self.duration is not None and not isinstance(self.duration, QuantityValue):
            self.duration = QuantityValue(**as_dict(self.duration))

        if self.temperature is not None and not isinstance(self.temperature, QuantityValue):
            self.temperature = QuantityValue(**as_dict(self.temperature))

        if not isinstance(self.substances_used, list):
            self.substances_used = [self.substances_used] if self.substances_used is not None else []
        self.substances_used = [v if isinstance(v, PortionOfSubstance) else PortionOfSubstance(**as_dict(v)) for v in self.substances_used]

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class ChemicalConversionProcess(MaterialProcessing):
    """
    A process that results in the interconversion of chemical species by a reaction to transform the reagents into
    products.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["ChemicalConversionProcess"]
    class_class_curie: ClassVar[str] = "nmdc:ChemicalConversionProcess"
    class_name: ClassVar[str] = "ChemicalConversionProcess"
    class_model_uri: ClassVar[URIRef] = NMDC.ChemicalConversionProcess

    id: Union[str, ChemicalConversionProcessId] = None
    type: Union[str, URIorCURIE] = None
    chemical_conversion_category: Optional[Union[str, "ChemicalConversionCategoryEnum"]] = None
    duration: Optional[Union[dict, QuantityValue]] = None
    temperature: Optional[Union[dict, QuantityValue]] = None
    substances_used: Optional[Union[Union[dict, PortionOfSubstance], List[Union[dict, PortionOfSubstance]]]] = empty_list()
    substances_volume: Optional[Union[dict, QuantityValue]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalConversionProcessId):
            self.id = ChemicalConversionProcessId(self.id)

        if self.chemical_conversion_category is not None and not isinstance(self.chemical_conversion_category, ChemicalConversionCategoryEnum):
            self.chemical_conversion_category = ChemicalConversionCategoryEnum(self.chemical_conversion_category)

        if self.duration is not None and not isinstance(self.duration, QuantityValue):
            self.duration = QuantityValue(**as_dict(self.duration))

        if self.temperature is not None and not isinstance(self.temperature, QuantityValue):
            self.temperature = QuantityValue(**as_dict(self.temperature))

        if not isinstance(self.substances_used, list):
            self.substances_used = [self.substances_used] if self.substances_used is not None else []
        self.substances_used = [v if isinstance(v, PortionOfSubstance) else PortionOfSubstance(**as_dict(v)) for v in self.substances_used]

        if self.substances_volume is not None and not isinstance(self.substances_volume, QuantityValue):
            self.substances_volume = QuantityValue(**as_dict(self.substances_volume))

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class Protocol(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["Protocol"]
    class_class_curie: ClassVar[str] = "nmdc:Protocol"
    class_name: ClassVar[str] = "Protocol"
    class_model_uri: ClassVar[URIRef] = NMDC.Protocol

    type: Union[str, URIorCURIE] = None
    url: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class CreditAssociation(YAMLRoot):
    """
    This class supports binding associated researchers to studies. There will be at least a slot for a CRediT
    Contributor Role and for a person value. Specifically see the associated researchers tab on the
    NMDC_SampleMetadata-V4_CommentsForUpdates at
    https://docs.google.com/spreadsheets/d/1INlBo5eoqn2efn4H2P2i8rwRBtnbDVTqXrochJEAPko/edit#gid=0
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Association"]
    class_class_curie: ClassVar[str] = "prov:Association"
    class_name: ClassVar[str] = "CreditAssociation"
    class_model_uri: ClassVar[URIRef] = NMDC.CreditAssociation

    applies_to_person: Union[dict, PersonValue] = None
    applied_roles: Union[Union[str, "CreditEnum"], List[Union[str, "CreditEnum"]]] = None
    type: Union[str, URIorCURIE] = None

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

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)

        super().__post_init__(**kwargs)


@dataclass
class Doi(YAMLRoot):
    """
    A centrally registered identifier symbol used to uniquely identify objects given by the International DOI
    Foundation. The DOI system is particularly used for electronic documents.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["Doi"]
    class_class_curie: ClassVar[str] = "nmdc:Doi"
    class_name: ClassVar[str] = "Doi"
    class_model_uri: ClassVar[URIRef] = NMDC.Doi

    doi_value: Union[str, URIorCURIE] = None
    doi_category: Union[str, "DoiCategoryEnum"] = None
    type: Union[str, URIorCURIE] = None
    doi_provider: Optional[Union[str, "DoiProviderEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.doi_value):
            self.MissingRequiredField("doi_value")
        if not isinstance(self.doi_value, URIorCURIE):
            self.doi_value = URIorCURIE(self.doi_value)

        if self._is_empty(self.doi_category):
            self.MissingRequiredField("doi_category")
        if not isinstance(self.doi_category, DoiCategoryEnum):
            self.doi_category = DoiCategoryEnum(self.doi_category)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)

        if self.doi_provider is not None and not isinstance(self.doi_provider, DoiProviderEnum):
            self.doi_provider = DoiProviderEnum(self.doi_provider)

        super().__post_init__(**kwargs)


@dataclass
class Study(NamedThing):
    """
    A study summarizes the overall goal of a research initiative and outlines the key objective of its underlying
    projects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["Study"]
    class_class_curie: ClassVar[str] = "nmdc:Study"
    class_name: ClassVar[str] = "Study"
    class_model_uri: ClassVar[URIRef] = NMDC.Study

    id: Union[str, StudyId] = None
    type: Union[str, URIorCURIE] = None
    study_category: Union[str, "StudyCategoryEnum"] = None
    emsl_project_identifiers: Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]] = empty_list()
    gnps_task_identifiers: Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]] = empty_list()
    gold_study_identifiers: Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]] = empty_list()
    insdc_bioproject_identifiers: Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]] = empty_list()
    jgi_portal_study_identifiers: Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]] = empty_list()
    mgnify_project_identifiers: Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]] = empty_list()
    neon_study_identifiers: Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]] = empty_list()
    related_identifiers: Optional[str] = None
    alternative_descriptions: Optional[Union[str, List[str]]] = empty_list()
    alternative_names: Optional[Union[str, List[str]]] = empty_list()
    alternative_titles: Optional[Union[str, List[str]]] = empty_list()
    ecosystem: Optional[str] = None
    ecosystem_category: Optional[str] = None
    ecosystem_subtype: Optional[str] = None
    ecosystem_type: Optional[str] = None
    specific_ecosystem: Optional[str] = None
    associated_dois: Optional[Union[Union[dict, Doi], List[Union[dict, Doi]]]] = empty_list()
    funding_sources: Optional[Union[str, List[str]]] = empty_list()
    has_credit_associations: Optional[Union[Union[dict, CreditAssociation], List[Union[dict, CreditAssociation]]]] = empty_list()
    homepage_website: Optional[Union[str, List[str]]] = empty_list()
    notes: Optional[str] = None
    objective: Optional[str] = None
    part_of: Optional[Union[Union[str, StudyId], List[Union[str, StudyId]]]] = empty_list()
    principal_investigator: Optional[Union[dict, PersonValue]] = None
    protocol_link: Optional[Union[Union[dict, Protocol], List[Union[dict, Protocol]]]] = empty_list()
    study_image: Optional[Union[Union[dict, ImageValue], List[Union[dict, ImageValue]]]] = empty_list()
    title: Optional[str] = None
    websites: Optional[Union[str, List[str]]] = empty_list()
    name: Optional[str] = None
    description: Optional[str] = None
    alternative_identifiers: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StudyId):
            self.id = StudyId(self.id)

        if self._is_empty(self.study_category):
            self.MissingRequiredField("study_category")
        if not isinstance(self.study_category, StudyCategoryEnum):
            self.study_category = StudyCategoryEnum(self.study_category)

        if not isinstance(self.emsl_project_identifiers, list):
            self.emsl_project_identifiers = [self.emsl_project_identifiers] if self.emsl_project_identifiers is not None else []
        self.emsl_project_identifiers = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(v) for v in self.emsl_project_identifiers]

        if not isinstance(self.gnps_task_identifiers, list):
            self.gnps_task_identifiers = [self.gnps_task_identifiers] if self.gnps_task_identifiers is not None else []
        self.gnps_task_identifiers = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(v) for v in self.gnps_task_identifiers]

        if not isinstance(self.gold_study_identifiers, list):
            self.gold_study_identifiers = [self.gold_study_identifiers] if self.gold_study_identifiers is not None else []
        self.gold_study_identifiers = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(v) for v in self.gold_study_identifiers]

        if not isinstance(self.insdc_bioproject_identifiers, list):
            self.insdc_bioproject_identifiers = [self.insdc_bioproject_identifiers] if self.insdc_bioproject_identifiers is not None else []
        self.insdc_bioproject_identifiers = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(v) for v in self.insdc_bioproject_identifiers]

        if not isinstance(self.jgi_portal_study_identifiers, list):
            self.jgi_portal_study_identifiers = [self.jgi_portal_study_identifiers] if self.jgi_portal_study_identifiers is not None else []
        self.jgi_portal_study_identifiers = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(v) for v in self.jgi_portal_study_identifiers]

        if not isinstance(self.mgnify_project_identifiers, list):
            self.mgnify_project_identifiers = [self.mgnify_project_identifiers] if self.mgnify_project_identifiers is not None else []
        self.mgnify_project_identifiers = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(v) for v in self.mgnify_project_identifiers]

        if not isinstance(self.neon_study_identifiers, list):
            self.neon_study_identifiers = [self.neon_study_identifiers] if self.neon_study_identifiers is not None else []
        self.neon_study_identifiers = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(v) for v in self.neon_study_identifiers]

        if self.related_identifiers is not None and not isinstance(self.related_identifiers, str):
            self.related_identifiers = str(self.related_identifiers)

        if not isinstance(self.alternative_descriptions, list):
            self.alternative_descriptions = [self.alternative_descriptions] if self.alternative_descriptions is not None else []
        self.alternative_descriptions = [v if isinstance(v, str) else str(v) for v in self.alternative_descriptions]

        if not isinstance(self.alternative_names, list):
            self.alternative_names = [self.alternative_names] if self.alternative_names is not None else []
        self.alternative_names = [v if isinstance(v, str) else str(v) for v in self.alternative_names]

        if not isinstance(self.alternative_titles, list):
            self.alternative_titles = [self.alternative_titles] if self.alternative_titles is not None else []
        self.alternative_titles = [v if isinstance(v, str) else str(v) for v in self.alternative_titles]

        if self.ecosystem is not None and not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self.ecosystem_category is not None and not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self.ecosystem_subtype is not None and not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self.ecosystem_type is not None and not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self.specific_ecosystem is not None and not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if not isinstance(self.associated_dois, list):
            self.associated_dois = [self.associated_dois] if self.associated_dois is not None else []
        self.associated_dois = [v if isinstance(v, Doi) else Doi(**as_dict(v)) for v in self.associated_dois]

        if not isinstance(self.funding_sources, list):
            self.funding_sources = [self.funding_sources] if self.funding_sources is not None else []
        self.funding_sources = [v if isinstance(v, str) else str(v) for v in self.funding_sources]

        if not isinstance(self.has_credit_associations, list):
            self.has_credit_associations = [self.has_credit_associations] if self.has_credit_associations is not None else []
        self.has_credit_associations = [v if isinstance(v, CreditAssociation) else CreditAssociation(**as_dict(v)) for v in self.has_credit_associations]

        if not isinstance(self.homepage_website, list):
            self.homepage_website = [self.homepage_website] if self.homepage_website is not None else []
        self.homepage_website = [v if isinstance(v, str) else str(v) for v in self.homepage_website]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.objective is not None and not isinstance(self.objective, str):
            self.objective = str(self.objective)

        if not isinstance(self.part_of, list):
            self.part_of = [self.part_of] if self.part_of is not None else []
        self.part_of = [v if isinstance(v, StudyId) else StudyId(v) for v in self.part_of]

        if self.principal_investigator is not None and not isinstance(self.principal_investigator, PersonValue):
            self.principal_investigator = PersonValue(**as_dict(self.principal_investigator))

        if not isinstance(self.protocol_link, list):
            self.protocol_link = [self.protocol_link] if self.protocol_link is not None else []
        self.protocol_link = [v if isinstance(v, Protocol) else Protocol(**as_dict(v)) for v in self.protocol_link]

        if not isinstance(self.study_image, list):
            self.study_image = [self.study_image] if self.study_image is not None else []
        self.study_image = [v if isinstance(v, ImageValue) else ImageValue(**as_dict(v)) for v in self.study_image]

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.websites, list):
            self.websites = [self.websites] if self.websites is not None else []
        self.websites = [v if isinstance(v, str) else str(v) for v in self.websites]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.alternative_identifiers, list):
            self.alternative_identifiers = [self.alternative_identifiers] if self.alternative_identifiers is not None else []
        self.alternative_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.alternative_identifiers]

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class InformationObject(NamedThing):
    """
    Any data or knowledge that reduces uncertainty or enhances understanding about a system, process, or entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["InformationObject"]
    class_class_curie: ClassVar[str] = "nmdc:InformationObject"
    class_name: ClassVar[str] = "InformationObject"
    class_model_uri: ClassVar[URIRef] = NMDC.InformationObject

    id: Union[str, InformationObjectId] = None
    type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class Configuration(InformationObject):
    """
    A set of parameters that define the actions of a process and is shared among multiple instances of the process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["Configuration"]
    class_class_curie: ClassVar[str] = "nmdc:Configuration"
    class_name: ClassVar[str] = "Configuration"
    class_model_uri: ClassVar[URIRef] = NMDC.Configuration

    id: Union[str, ConfigurationId] = None
    type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class MassSpectrometryConfiguration(Configuration):
    """
    A set of parameters that define and control the actions of a mass spectrometry process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["MassSpectrometryConfiguration"]
    class_class_curie: ClassVar[str] = "nmdc:MassSpectrometryConfiguration"
    class_name: ClassVar[str] = "MassSpectrometryConfiguration"
    class_model_uri: ClassVar[URIRef] = NMDC.MassSpectrometryConfiguration

    id: Union[str, MassSpectrometryConfigurationId] = None
    type: Union[str, URIorCURIE] = None
    name: str = None
    description: str = None
    mass_spectrometry_acquisition_strategy: Optional[Union[str, "MassSpectrometryAcquisitionStrategyEnum"]] = None
    resolution_categories: Optional[Union[Union[str, "ResolutionCategoryEnum"], List[Union[str, "ResolutionCategoryEnum"]]]] = empty_list()
    mass_analyzers: Optional[Union[Union[str, "MassAnalyzerEnum"], List[Union[str, "MassAnalyzerEnum"]]]] = empty_list()
    ionization_source: Optional[Union[str, "IonizationSourceEnum"]] = None
    mass_spectrum_collection_modes: Optional[Union[Union[str, "MassSpectrumCollectionModeEnum"], List[Union[str, "MassSpectrumCollectionModeEnum"]]]] = empty_list()
    polarity_mode: Optional[Union[str, "PolarityModeEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MassSpectrometryConfigurationId):
            self.id = MassSpectrometryConfigurationId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.mass_spectrometry_acquisition_strategy is not None and not isinstance(self.mass_spectrometry_acquisition_strategy, MassSpectrometryAcquisitionStrategyEnum):
            self.mass_spectrometry_acquisition_strategy = MassSpectrometryAcquisitionStrategyEnum(self.mass_spectrometry_acquisition_strategy)

        if not isinstance(self.resolution_categories, list):
            self.resolution_categories = [self.resolution_categories] if self.resolution_categories is not None else []
        self.resolution_categories = [v if isinstance(v, ResolutionCategoryEnum) else ResolutionCategoryEnum(v) for v in self.resolution_categories]

        if not isinstance(self.mass_analyzers, list):
            self.mass_analyzers = [self.mass_analyzers] if self.mass_analyzers is not None else []
        self.mass_analyzers = [v if isinstance(v, MassAnalyzerEnum) else MassAnalyzerEnum(v) for v in self.mass_analyzers]

        if self.ionization_source is not None and not isinstance(self.ionization_source, IonizationSourceEnum):
            self.ionization_source = IonizationSourceEnum(self.ionization_source)

        if not isinstance(self.mass_spectrum_collection_modes, list):
            self.mass_spectrum_collection_modes = [self.mass_spectrum_collection_modes] if self.mass_spectrum_collection_modes is not None else []
        self.mass_spectrum_collection_modes = [v if isinstance(v, MassSpectrumCollectionModeEnum) else MassSpectrumCollectionModeEnum(v) for v in self.mass_spectrum_collection_modes]

        if self.polarity_mode is not None and not isinstance(self.polarity_mode, PolarityModeEnum):
            self.polarity_mode = PolarityModeEnum(self.polarity_mode)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class ChromatographyConfiguration(Configuration):
    """
    A set of parameters that define and control the actions of a chromatography process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["ChromatographyConfiguration"]
    class_class_curie: ClassVar[str] = "nmdc:ChromatographyConfiguration"
    class_name: ClassVar[str] = "ChromatographyConfiguration"
    class_model_uri: ClassVar[URIRef] = NMDC.ChromatographyConfiguration

    id: Union[str, ChromatographyConfigurationId] = None
    type: Union[str, URIorCURIE] = None
    name: str = None
    description: str = None
    chromatographic_category: Optional[Union[str, "ChromatographicCategoryEnum"]] = None
    ordered_mobile_phases: Optional[Union[Union[dict, MobilePhaseSegment], List[Union[dict, MobilePhaseSegment]]]] = empty_list()
    stationary_phase: Optional[Union[str, "StationaryPhaseEnum"]] = None
    temperature: Optional[Union[dict, QuantityValue]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChromatographyConfigurationId):
            self.id = ChromatographyConfigurationId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.chromatographic_category is not None and not isinstance(self.chromatographic_category, ChromatographicCategoryEnum):
            self.chromatographic_category = ChromatographicCategoryEnum(self.chromatographic_category)

        if not isinstance(self.ordered_mobile_phases, list):
            self.ordered_mobile_phases = [self.ordered_mobile_phases] if self.ordered_mobile_phases is not None else []
        self.ordered_mobile_phases = [v if isinstance(v, MobilePhaseSegment) else MobilePhaseSegment(**as_dict(v)) for v in self.ordered_mobile_phases]

        if self.stationary_phase is not None and not isinstance(self.stationary_phase, StationaryPhaseEnum):
            self.stationary_phase = StationaryPhaseEnum(self.stationary_phase)

        if self.temperature is not None and not isinstance(self.temperature, QuantityValue):
            self.temperature = QuantityValue(**as_dict(self.temperature))

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class DataObject(InformationObject):
    """
    An object that primarily consists of symbols that represent information. Files, records, and omics data are
    examples of data objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["DataObject"]
    class_class_curie: ClassVar[str] = "nmdc:DataObject"
    class_name: ClassVar[str] = "DataObject"
    class_model_uri: ClassVar[URIRef] = NMDC.DataObject

    id: Union[str, DataObjectId] = None
    type: Union[str, URIorCURIE] = None
    name: str = None
    description: str = None
    compression_type: Optional[str] = None
    data_category: Optional[Union[str, "DataCategoryEnum"]] = None
    data_object_type: Optional[Union[str, "FileTypeEnum"]] = None
    file_size_bytes: Optional[int] = None
    insdc_experiment_identifiers: Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]] = empty_list()
    md5_checksum: Optional[str] = None
    url: Optional[str] = None
    was_generated_by: Optional[Union[str, WorkflowExecutionId]] = None

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

        if self.compression_type is not None and not isinstance(self.compression_type, str):
            self.compression_type = str(self.compression_type)

        if self.data_category is not None and not isinstance(self.data_category, DataCategoryEnum):
            self.data_category = DataCategoryEnum(self.data_category)

        if self.data_object_type is not None and not isinstance(self.data_object_type, FileTypeEnum):
            self.data_object_type = FileTypeEnum(self.data_object_type)

        if self.file_size_bytes is not None and not isinstance(self.file_size_bytes, int):
            self.file_size_bytes = int(self.file_size_bytes)

        if not isinstance(self.insdc_experiment_identifiers, list):
            self.insdc_experiment_identifiers = [self.insdc_experiment_identifiers] if self.insdc_experiment_identifiers is not None else []
        self.insdc_experiment_identifiers = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(v) for v in self.insdc_experiment_identifiers]

        if self.md5_checksum is not None and not isinstance(self.md5_checksum, str):
            self.md5_checksum = str(self.md5_checksum)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        if self.was_generated_by is not None and not isinstance(self.was_generated_by, WorkflowExecutionId):
            self.was_generated_by = WorkflowExecutionId(self.was_generated_by)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class DataGeneration(PlannedProcess):
    """
    The methods and processes used to generate omics data from a biosample or organism.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["DataGeneration"]
    class_class_curie: ClassVar[str] = "nmdc:DataGeneration"
    class_name: ClassVar[str] = "DataGeneration"
    class_model_uri: ClassVar[URIRef] = NMDC.DataGeneration

    id: Union[str, DataGenerationId] = None
    type: Union[str, URIorCURIE] = None
    analyte_category: Union[str, "AnalyteCategoryEnum"] = None
    associated_studies: Union[Union[str, StudyId], List[Union[str, StudyId]]] = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    add_date: Optional[str] = None
    instrument_used: Optional[Union[Union[str, InstrumentId], List[Union[str, InstrumentId]]]] = empty_list()
    mod_date: Optional[str] = None
    part_of: Optional[Union[Union[str, DataGenerationId], List[Union[str, DataGenerationId]]]] = empty_list()
    principal_investigator: Optional[Union[dict, PersonValue]] = None
    has_output: Optional[Union[Union[str, DataObjectId], List[Union[str, DataObjectId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.analyte_category):
            self.MissingRequiredField("analyte_category")
        if not isinstance(self.analyte_category, AnalyteCategoryEnum):
            self.analyte_category = AnalyteCategoryEnum(self.analyte_category)

        if self._is_empty(self.associated_studies):
            self.MissingRequiredField("associated_studies")
        if not isinstance(self.associated_studies, list):
            self.associated_studies = [self.associated_studies] if self.associated_studies is not None else []
        self.associated_studies = [v if isinstance(v, StudyId) else StudyId(v) for v in self.associated_studies]

        if self._is_empty(self.has_input):
            self.MissingRequiredField("has_input")
        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
        self.has_input = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_input]

        if self.add_date is not None and not isinstance(self.add_date, str):
            self.add_date = str(self.add_date)

        if not isinstance(self.instrument_used, list):
            self.instrument_used = [self.instrument_used] if self.instrument_used is not None else []
        self.instrument_used = [v if isinstance(v, InstrumentId) else InstrumentId(v) for v in self.instrument_used]

        if self.mod_date is not None and not isinstance(self.mod_date, str):
            self.mod_date = str(self.mod_date)

        if not isinstance(self.part_of, list):
            self.part_of = [self.part_of] if self.part_of is not None else []
        self.part_of = [v if isinstance(v, DataGenerationId) else DataGenerationId(v) for v in self.part_of]

        if self.principal_investigator is not None and not isinstance(self.principal_investigator, PersonValue):
            self.principal_investigator = PersonValue(**as_dict(self.principal_investigator))

        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output] if self.has_output is not None else []
        self.has_output = [v if isinstance(v, DataObjectId) else DataObjectId(v) for v in self.has_output]

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class NucleotideSequencing(DataGeneration):
    """
    A DataGeneration in which the sequence of DNA or RNA molecules is generated.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["NucleotideSequencing"]
    class_class_curie: ClassVar[str] = "nmdc:NucleotideSequencing"
    class_name: ClassVar[str] = "NucleotideSequencing"
    class_model_uri: ClassVar[URIRef] = NMDC.NucleotideSequencing

    id: Union[str, NucleotideSequencingId] = None
    type: Union[str, URIorCURIE] = None
    analyte_category: Union[str, "AnalyteCategoryEnum"] = None
    associated_studies: Union[Union[str, StudyId], List[Union[str, StudyId]]] = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    gold_sequencing_project_identifiers: Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]] = empty_list()
    insdc_bioproject_identifiers: Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]] = empty_list()
    insdc_experiment_identifiers: Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]] = empty_list()
    ncbi_project_name: Optional[str] = None
    target_gene: Optional[Union[dict, TextValue]] = None
    target_subfragment: Optional[Union[dict, TextValue]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NucleotideSequencingId):
            self.id = NucleotideSequencingId(self.id)

        if not isinstance(self.gold_sequencing_project_identifiers, list):
            self.gold_sequencing_project_identifiers = [self.gold_sequencing_project_identifiers] if self.gold_sequencing_project_identifiers is not None else []
        self.gold_sequencing_project_identifiers = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(v) for v in self.gold_sequencing_project_identifiers]

        if not isinstance(self.insdc_bioproject_identifiers, list):
            self.insdc_bioproject_identifiers = [self.insdc_bioproject_identifiers] if self.insdc_bioproject_identifiers is not None else []
        self.insdc_bioproject_identifiers = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(v) for v in self.insdc_bioproject_identifiers]

        if not isinstance(self.insdc_experiment_identifiers, list):
            self.insdc_experiment_identifiers = [self.insdc_experiment_identifiers] if self.insdc_experiment_identifiers is not None else []
        self.insdc_experiment_identifiers = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(v) for v in self.insdc_experiment_identifiers]

        if self.ncbi_project_name is not None and not isinstance(self.ncbi_project_name, str):
            self.ncbi_project_name = str(self.ncbi_project_name)

        if self.target_gene is not None and not isinstance(self.target_gene, TextValue):
            self.target_gene = TextValue(**as_dict(self.target_gene))

        if self.target_subfragment is not None and not isinstance(self.target_subfragment, TextValue):
            self.target_subfragment = TextValue(**as_dict(self.target_subfragment))

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class MassSpectrometry(DataGeneration):
    """
    Spectrometry where the sample is converted into gaseous ions which are characterised by their mass-to-charge ratio
    and relative abundance.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["MassSpectrometry"]
    class_class_curie: ClassVar[str] = "nmdc:MassSpectrometry"
    class_name: ClassVar[str] = "MassSpectrometry"
    class_model_uri: ClassVar[URIRef] = NMDC.MassSpectrometry

    id: Union[str, MassSpectrometryId] = None
    type: Union[str, URIorCURIE] = None
    analyte_category: Union[str, "AnalyteCategoryEnum"] = None
    associated_studies: Union[Union[str, StudyId], List[Union[str, StudyId]]] = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    eluent_introduction_category: Optional[Union[str, "EluentIntroductionCategoryEnum"]] = None
    has_calibration: Optional[str] = None
    has_chromatography_configuration: Optional[Union[str, ChromatographyConfigurationId]] = None
    has_mass_spectrometry_configuration: Optional[Union[str, MassSpectrometryConfigurationId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MassSpectrometryId):
            self.id = MassSpectrometryId(self.id)

        if self.eluent_introduction_category is not None and not isinstance(self.eluent_introduction_category, EluentIntroductionCategoryEnum):
            self.eluent_introduction_category = EluentIntroductionCategoryEnum(self.eluent_introduction_category)

        if self.has_calibration is not None and not isinstance(self.has_calibration, str):
            self.has_calibration = str(self.has_calibration)

        if self.has_chromatography_configuration is not None and not isinstance(self.has_chromatography_configuration, ChromatographyConfigurationId):
            self.has_chromatography_configuration = ChromatographyConfigurationId(self.has_chromatography_configuration)

        if self.has_mass_spectrometry_configuration is not None and not isinstance(self.has_mass_spectrometry_configuration, MassSpectrometryConfigurationId):
            self.has_mass_spectrometry_configuration = MassSpectrometryConfigurationId(self.has_mass_spectrometry_configuration)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class WorkflowExecution(PlannedProcess):
    """
    Represents an instance of an execution of a particular workflow
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["WorkflowExecution"]
    class_class_curie: ClassVar[str] = "nmdc:WorkflowExecution"
    class_name: ClassVar[str] = "WorkflowExecution"
    class_model_uri: ClassVar[URIRef] = NMDC.WorkflowExecution

    id: Union[str, WorkflowExecutionId] = None
    type: Union[str, URIorCURIE] = None
    execution_resource: Union[str, "ExecutionResourceEnum"] = None
    git_url: str = None
    started_at_time: str = None
    was_informed_by: Union[str, DataGenerationId] = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    ended_at_time: Optional[str] = None
    version: Optional[str] = None
    has_output: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.execution_resource):
            self.MissingRequiredField("execution_resource")
        if not isinstance(self.execution_resource, ExecutionResourceEnum):
            self.execution_resource = ExecutionResourceEnum(self.execution_resource)

        if self._is_empty(self.git_url):
            self.MissingRequiredField("git_url")
        if not isinstance(self.git_url, str):
            self.git_url = str(self.git_url)

        if self._is_empty(self.started_at_time):
            self.MissingRequiredField("started_at_time")
        if not isinstance(self.started_at_time, str):
            self.started_at_time = str(self.started_at_time)

        if self._is_empty(self.was_informed_by):
            self.MissingRequiredField("was_informed_by")
        if not isinstance(self.was_informed_by, DataGenerationId):
            self.was_informed_by = DataGenerationId(self.was_informed_by)

        if self._is_empty(self.has_input):
            self.MissingRequiredField("has_input")
        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
        self.has_input = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_input]

        if self.ended_at_time is not None and not isinstance(self.ended_at_time, str):
            self.ended_at_time = str(self.ended_at_time)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output] if self.has_output is not None else []
        self.has_output = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_output]

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class MetagenomeAnnotation(WorkflowExecution):
    """
    A workflow execution activity that provides functional and structural annotation of assembled metagenome contigs
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["MetagenomeAnnotation"]
    class_class_curie: ClassVar[str] = "nmdc:MetagenomeAnnotation"
    class_name: ClassVar[str] = "MetagenomeAnnotation"
    class_model_uri: ClassVar[URIRef] = NMDC.MetagenomeAnnotation

    id: Union[str, MetagenomeAnnotationId] = None
    type: Union[str, URIorCURIE] = None
    execution_resource: Union[str, "ExecutionResourceEnum"] = None
    git_url: str = None
    started_at_time: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    img_identifiers: Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]] = empty_list()
    gold_analysis_project_identifiers: Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]] = empty_list()
    was_informed_by: Optional[Union[str, DataGenerationId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MetagenomeAnnotationId):
            self.id = MetagenomeAnnotationId(self.id)

        if not isinstance(self.img_identifiers, list):
            self.img_identifiers = [self.img_identifiers] if self.img_identifiers is not None else []
        self.img_identifiers = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(v) for v in self.img_identifiers]

        if not isinstance(self.gold_analysis_project_identifiers, list):
            self.gold_analysis_project_identifiers = [self.gold_analysis_project_identifiers] if self.gold_analysis_project_identifiers is not None else []
        self.gold_analysis_project_identifiers = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(v) for v in self.gold_analysis_project_identifiers]

        if self.was_informed_by is not None and not isinstance(self.was_informed_by, DataGenerationId):
            self.was_informed_by = DataGenerationId(self.was_informed_by)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class MetagenomeAssembly(WorkflowExecution):
    """
    A workflow execution activity that converts sequencing reads into an assembled metagenome.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["MetagenomeAssembly"]
    class_class_curie: ClassVar[str] = "nmdc:MetagenomeAssembly"
    class_name: ClassVar[str] = "MetagenomeAssembly"
    class_model_uri: ClassVar[URIRef] = NMDC.MetagenomeAssembly

    id: Union[str, MetagenomeAssemblyId] = None
    type: Union[str, URIorCURIE] = None
    execution_resource: Union[str, "ExecutionResourceEnum"] = None
    git_url: str = None
    started_at_time: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    was_informed_by: Union[str, DataGenerationId] = None
    asm_score: Optional[float] = None
    scaffolds: Optional[float] = None
    scaf_logsum: Optional[float] = None
    scaf_powsum: Optional[float] = None
    scaf_max: Optional[float] = None
    scaf_bp: Optional[float] = None
    scaf_n50: Optional[float] = None
    scaf_n90: Optional[float] = None
    scaf_l50: Optional[float] = None
    scaf_l90: Optional[float] = None
    scaf_n_gt50k: Optional[float] = None
    scaf_l_gt50k: Optional[float] = None
    scaf_pct_gt50k: Optional[float] = None
    contigs: Optional[float] = None
    contig_bp: Optional[float] = None
    ctg_n50: Optional[float] = None
    ctg_l50: Optional[float] = None
    ctg_n90: Optional[float] = None
    ctg_l90: Optional[float] = None
    ctg_logsum: Optional[float] = None
    ctg_powsum: Optional[float] = None
    ctg_max: Optional[float] = None
    gap_pct: Optional[float] = None
    gc_std: Optional[float] = None
    gc_avg: Optional[float] = None
    num_input_reads: Optional[float] = None
    num_aligned_reads: Optional[float] = None
    insdc_assembly_identifiers: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MetagenomeAssemblyId):
            self.id = MetagenomeAssemblyId(self.id)

        if self._is_empty(self.was_informed_by):
            self.MissingRequiredField("was_informed_by")
        if not isinstance(self.was_informed_by, DataGenerationId):
            self.was_informed_by = DataGenerationId(self.was_informed_by)

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

        if self.scaf_n50 is not None and not isinstance(self.scaf_n50, float):
            self.scaf_n50 = float(self.scaf_n50)

        if self.scaf_n90 is not None and not isinstance(self.scaf_n90, float):
            self.scaf_n90 = float(self.scaf_n90)

        if self.scaf_l50 is not None and not isinstance(self.scaf_l50, float):
            self.scaf_l50 = float(self.scaf_l50)

        if self.scaf_l90 is not None and not isinstance(self.scaf_l90, float):
            self.scaf_l90 = float(self.scaf_l90)

        if self.scaf_n_gt50k is not None and not isinstance(self.scaf_n_gt50k, float):
            self.scaf_n_gt50k = float(self.scaf_n_gt50k)

        if self.scaf_l_gt50k is not None and not isinstance(self.scaf_l_gt50k, float):
            self.scaf_l_gt50k = float(self.scaf_l_gt50k)

        if self.scaf_pct_gt50k is not None and not isinstance(self.scaf_pct_gt50k, float):
            self.scaf_pct_gt50k = float(self.scaf_pct_gt50k)

        if self.contigs is not None and not isinstance(self.contigs, float):
            self.contigs = float(self.contigs)

        if self.contig_bp is not None and not isinstance(self.contig_bp, float):
            self.contig_bp = float(self.contig_bp)

        if self.ctg_n50 is not None and not isinstance(self.ctg_n50, float):
            self.ctg_n50 = float(self.ctg_n50)

        if self.ctg_l50 is not None and not isinstance(self.ctg_l50, float):
            self.ctg_l50 = float(self.ctg_l50)

        if self.ctg_n90 is not None and not isinstance(self.ctg_n90, float):
            self.ctg_n90 = float(self.ctg_n90)

        if self.ctg_l90 is not None and not isinstance(self.ctg_l90, float):
            self.ctg_l90 = float(self.ctg_l90)

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

        if self.insdc_assembly_identifiers is not None and not isinstance(self.insdc_assembly_identifiers, str):
            self.insdc_assembly_identifiers = str(self.insdc_assembly_identifiers)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class MetatranscriptomeAssembly(WorkflowExecution):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["MetatranscriptomeAssembly"]
    class_class_curie: ClassVar[str] = "nmdc:MetatranscriptomeAssembly"
    class_name: ClassVar[str] = "MetatranscriptomeAssembly"
    class_model_uri: ClassVar[URIRef] = NMDC.MetatranscriptomeAssembly

    id: Union[str, MetatranscriptomeAssemblyId] = None
    type: Union[str, URIorCURIE] = None
    execution_resource: Union[str, "ExecutionResourceEnum"] = None
    git_url: str = None
    started_at_time: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    was_informed_by: Union[str, DataGenerationId] = None
    asm_score: Optional[float] = None
    scaffolds: Optional[float] = None
    scaf_logsum: Optional[float] = None
    scaf_powsum: Optional[float] = None
    scaf_max: Optional[float] = None
    scaf_bp: Optional[float] = None
    scaf_n50: Optional[float] = None
    scaf_n90: Optional[float] = None
    scaf_l50: Optional[float] = None
    scaf_l90: Optional[float] = None
    scaf_n_gt50k: Optional[float] = None
    scaf_l_gt50k: Optional[float] = None
    scaf_pct_gt50k: Optional[float] = None
    contigs: Optional[float] = None
    contig_bp: Optional[float] = None
    ctg_n50: Optional[float] = None
    ctg_l50: Optional[float] = None
    ctg_n90: Optional[float] = None
    ctg_l90: Optional[float] = None
    ctg_logsum: Optional[float] = None
    ctg_powsum: Optional[float] = None
    ctg_max: Optional[float] = None
    gap_pct: Optional[float] = None
    gc_std: Optional[float] = None
    gc_avg: Optional[float] = None
    num_input_reads: Optional[float] = None
    num_aligned_reads: Optional[float] = None
    insdc_assembly_identifiers: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MetatranscriptomeAssemblyId):
            self.id = MetatranscriptomeAssemblyId(self.id)

        if self._is_empty(self.was_informed_by):
            self.MissingRequiredField("was_informed_by")
        if not isinstance(self.was_informed_by, DataGenerationId):
            self.was_informed_by = DataGenerationId(self.was_informed_by)

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

        if self.scaf_n50 is not None and not isinstance(self.scaf_n50, float):
            self.scaf_n50 = float(self.scaf_n50)

        if self.scaf_n90 is not None and not isinstance(self.scaf_n90, float):
            self.scaf_n90 = float(self.scaf_n90)

        if self.scaf_l50 is not None and not isinstance(self.scaf_l50, float):
            self.scaf_l50 = float(self.scaf_l50)

        if self.scaf_l90 is not None and not isinstance(self.scaf_l90, float):
            self.scaf_l90 = float(self.scaf_l90)

        if self.scaf_n_gt50k is not None and not isinstance(self.scaf_n_gt50k, float):
            self.scaf_n_gt50k = float(self.scaf_n_gt50k)

        if self.scaf_l_gt50k is not None and not isinstance(self.scaf_l_gt50k, float):
            self.scaf_l_gt50k = float(self.scaf_l_gt50k)

        if self.scaf_pct_gt50k is not None and not isinstance(self.scaf_pct_gt50k, float):
            self.scaf_pct_gt50k = float(self.scaf_pct_gt50k)

        if self.contigs is not None and not isinstance(self.contigs, float):
            self.contigs = float(self.contigs)

        if self.contig_bp is not None and not isinstance(self.contig_bp, float):
            self.contig_bp = float(self.contig_bp)

        if self.ctg_n50 is not None and not isinstance(self.ctg_n50, float):
            self.ctg_n50 = float(self.ctg_n50)

        if self.ctg_l50 is not None and not isinstance(self.ctg_l50, float):
            self.ctg_l50 = float(self.ctg_l50)

        if self.ctg_n90 is not None and not isinstance(self.ctg_n90, float):
            self.ctg_n90 = float(self.ctg_n90)

        if self.ctg_l90 is not None and not isinstance(self.ctg_l90, float):
            self.ctg_l90 = float(self.ctg_l90)

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

        if self.insdc_assembly_identifiers is not None and not isinstance(self.insdc_assembly_identifiers, str):
            self.insdc_assembly_identifiers = str(self.insdc_assembly_identifiers)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class MetatranscriptomeAnnotation(WorkflowExecution):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["MetatranscriptomeAnnotation"]
    class_class_curie: ClassVar[str] = "nmdc:MetatranscriptomeAnnotation"
    class_name: ClassVar[str] = "MetatranscriptomeAnnotation"
    class_model_uri: ClassVar[URIRef] = NMDC.MetatranscriptomeAnnotation

    id: Union[str, MetatranscriptomeAnnotationId] = None
    type: Union[str, URIorCURIE] = None
    execution_resource: Union[str, "ExecutionResourceEnum"] = None
    git_url: str = None
    started_at_time: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    was_informed_by: Union[str, DataGenerationId] = None
    img_identifiers: Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]] = empty_list()
    gold_analysis_project_identifiers: Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]] = empty_list()
    has_output: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MetatranscriptomeAnnotationId):
            self.id = MetatranscriptomeAnnotationId(self.id)

        if self._is_empty(self.has_input):
            self.MissingRequiredField("has_input")
        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
        self.has_input = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_input]

        if self._is_empty(self.was_informed_by):
            self.MissingRequiredField("was_informed_by")
        if not isinstance(self.was_informed_by, DataGenerationId):
            self.was_informed_by = DataGenerationId(self.was_informed_by)

        if not isinstance(self.img_identifiers, list):
            self.img_identifiers = [self.img_identifiers] if self.img_identifiers is not None else []
        self.img_identifiers = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(v) for v in self.img_identifiers]

        if not isinstance(self.gold_analysis_project_identifiers, list):
            self.gold_analysis_project_identifiers = [self.gold_analysis_project_identifiers] if self.gold_analysis_project_identifiers is not None else []
        self.gold_analysis_project_identifiers = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(v) for v in self.gold_analysis_project_identifiers]

        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output] if self.has_output is not None else []
        self.has_output = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_output]

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class MetatranscriptomeAnalysis(WorkflowExecution):
    """
    A metatranscriptome activity that e.g. pools assembly and annotation activity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["MetatranscriptomeAnalysis"]
    class_class_curie: ClassVar[str] = "nmdc:MetatranscriptomeAnalysis"
    class_name: ClassVar[str] = "MetatranscriptomeAnalysis"
    class_model_uri: ClassVar[URIRef] = NMDC.MetatranscriptomeAnalysis

    id: Union[str, MetatranscriptomeAnalysisId] = None
    type: Union[str, URIorCURIE] = None
    execution_resource: Union[str, "ExecutionResourceEnum"] = None
    git_url: str = None
    started_at_time: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    was_informed_by: Union[str, DataGenerationId] = None
    img_identifiers: Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MetatranscriptomeAnalysisId):
            self.id = MetatranscriptomeAnalysisId(self.id)

        if self._is_empty(self.was_informed_by):
            self.MissingRequiredField("was_informed_by")
        if not isinstance(self.was_informed_by, DataGenerationId):
            self.was_informed_by = DataGenerationId(self.was_informed_by)

        if not isinstance(self.img_identifiers, list):
            self.img_identifiers = [self.img_identifiers] if self.img_identifiers is not None else []
        self.img_identifiers = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(v) for v in self.img_identifiers]

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class MagsAnalysis(WorkflowExecution):
    """
    A workflow execution activity that uses computational binning tools to group assembled contigs into genomes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["MagsAnalysis"]
    class_class_curie: ClassVar[str] = "nmdc:MagsAnalysis"
    class_name: ClassVar[str] = "MagsAnalysis"
    class_model_uri: ClassVar[URIRef] = NMDC.MagsAnalysis

    id: Union[str, MagsAnalysisId] = None
    type: Union[str, URIorCURIE] = None
    execution_resource: Union[str, "ExecutionResourceEnum"] = None
    git_url: str = None
    started_at_time: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    was_informed_by: Union[str, DataGenerationId] = None
    binned_contig_num: Optional[int] = None
    input_contig_num: Optional[int] = None
    low_depth_contig_num: Optional[int] = None
    mags_list: Optional[Union[Union[dict, MagBin], List[Union[dict, MagBin]]]] = empty_list()
    too_short_contig_num: Optional[int] = None
    unbinned_contig_num: Optional[int] = None
    img_identifiers: Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MagsAnalysisId):
            self.id = MagsAnalysisId(self.id)

        if self._is_empty(self.was_informed_by):
            self.MissingRequiredField("was_informed_by")
        if not isinstance(self.was_informed_by, DataGenerationId):
            self.was_informed_by = DataGenerationId(self.was_informed_by)

        if self.binned_contig_num is not None and not isinstance(self.binned_contig_num, int):
            self.binned_contig_num = int(self.binned_contig_num)

        if self.input_contig_num is not None and not isinstance(self.input_contig_num, int):
            self.input_contig_num = int(self.input_contig_num)

        if self.low_depth_contig_num is not None and not isinstance(self.low_depth_contig_num, int):
            self.low_depth_contig_num = int(self.low_depth_contig_num)

        if not isinstance(self.mags_list, list):
            self.mags_list = [self.mags_list] if self.mags_list is not None else []
        self.mags_list = [v if isinstance(v, MagBin) else MagBin(**as_dict(v)) for v in self.mags_list]

        if self.too_short_contig_num is not None and not isinstance(self.too_short_contig_num, int):
            self.too_short_contig_num = int(self.too_short_contig_num)

        if self.unbinned_contig_num is not None and not isinstance(self.unbinned_contig_num, int):
            self.unbinned_contig_num = int(self.unbinned_contig_num)

        if not isinstance(self.img_identifiers, list):
            self.img_identifiers = [self.img_identifiers] if self.img_identifiers is not None else []
        self.img_identifiers = [v if isinstance(v, ExternalIdentifier) else ExternalIdentifier(v) for v in self.img_identifiers]

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class MetagenomeSequencing(WorkflowExecution):
    """
    Initial sequencing activity that precedes any analysis. This activity has output(s) that are the raw sequencing
    data.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["MetagenomeSequencing"]
    class_class_curie: ClassVar[str] = "nmdc:MetagenomeSequencing"
    class_name: ClassVar[str] = "MetagenomeSequencing"
    class_model_uri: ClassVar[URIRef] = NMDC.MetagenomeSequencing

    id: Union[str, MetagenomeSequencingId] = None
    type: Union[str, URIorCURIE] = None
    execution_resource: Union[str, "ExecutionResourceEnum"] = None
    git_url: str = None
    started_at_time: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    was_informed_by: Union[str, DataGenerationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MetagenomeSequencingId):
            self.id = MetagenomeSequencingId(self.id)

        if self._is_empty(self.has_input):
            self.MissingRequiredField("has_input")
        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
        self.has_input = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_input]

        if self._is_empty(self.was_informed_by):
            self.MissingRequiredField("was_informed_by")
        if not isinstance(self.was_informed_by, DataGenerationId):
            self.was_informed_by = DataGenerationId(self.was_informed_by)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class ReadQcAnalysis(WorkflowExecution):
    """
    A workflow execution activity that performs quality control on raw Illumina reads including quality trimming,
    artifact removal, linker trimming, adapter trimming, spike-in removal, and human/cat/dog/mouse/microbe contaminant
    removal
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["ReadQcAnalysis"]
    class_class_curie: ClassVar[str] = "nmdc:ReadQcAnalysis"
    class_name: ClassVar[str] = "ReadQcAnalysis"
    class_model_uri: ClassVar[URIRef] = NMDC.ReadQcAnalysis

    id: Union[str, ReadQcAnalysisId] = None
    type: Union[str, URIorCURIE] = None
    execution_resource: Union[str, "ExecutionResourceEnum"] = None
    git_url: str = None
    started_at_time: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    was_informed_by: Union[str, DataGenerationId] = None
    input_base_count: Optional[float] = None
    input_read_bases: Optional[float] = None
    input_read_count: Optional[float] = None
    output_base_count: Optional[float] = None
    output_read_bases: Optional[float] = None
    output_read_count: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReadQcAnalysisId):
            self.id = ReadQcAnalysisId(self.id)

        if self._is_empty(self.was_informed_by):
            self.MissingRequiredField("was_informed_by")
        if not isinstance(self.was_informed_by, DataGenerationId):
            self.was_informed_by = DataGenerationId(self.was_informed_by)

        if self.input_base_count is not None and not isinstance(self.input_base_count, float):
            self.input_base_count = float(self.input_base_count)

        if self.input_read_bases is not None and not isinstance(self.input_read_bases, float):
            self.input_read_bases = float(self.input_read_bases)

        if self.input_read_count is not None and not isinstance(self.input_read_count, float):
            self.input_read_count = float(self.input_read_count)

        if self.output_base_count is not None and not isinstance(self.output_base_count, float):
            self.output_base_count = float(self.output_base_count)

        if self.output_read_bases is not None and not isinstance(self.output_read_bases, float):
            self.output_read_bases = float(self.output_read_bases)

        if self.output_read_count is not None and not isinstance(self.output_read_count, float):
            self.output_read_count = float(self.output_read_count)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class ReadBasedTaxonomyAnalysis(WorkflowExecution):
    """
    A workflow execution activity that performs taxonomy classification using sequencing reads
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["ReadBasedTaxonomyAnalysis"]
    class_class_curie: ClassVar[str] = "nmdc:ReadBasedTaxonomyAnalysis"
    class_name: ClassVar[str] = "ReadBasedTaxonomyAnalysis"
    class_model_uri: ClassVar[URIRef] = NMDC.ReadBasedTaxonomyAnalysis

    id: Union[str, ReadBasedTaxonomyAnalysisId] = None
    type: Union[str, URIorCURIE] = None
    execution_resource: Union[str, "ExecutionResourceEnum"] = None
    git_url: str = None
    started_at_time: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    was_informed_by: Union[str, DataGenerationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReadBasedTaxonomyAnalysisId):
            self.id = ReadBasedTaxonomyAnalysisId(self.id)

        if self._is_empty(self.was_informed_by):
            self.MissingRequiredField("was_informed_by")
        if not isinstance(self.was_informed_by, DataGenerationId):
            self.was_informed_by = DataGenerationId(self.was_informed_by)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class MetabolomicsAnalysis(WorkflowExecution):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["MetabolomicsAnalysis"]
    class_class_curie: ClassVar[str] = "nmdc:MetabolomicsAnalysis"
    class_name: ClassVar[str] = "MetabolomicsAnalysis"
    class_model_uri: ClassVar[URIRef] = NMDC.MetabolomicsAnalysis

    id: Union[str, MetabolomicsAnalysisId] = None
    type: Union[str, URIorCURIE] = None
    execution_resource: Union[str, "ExecutionResourceEnum"] = None
    git_url: str = None
    started_at_time: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    was_informed_by: Union[str, DataGenerationId] = None
    has_calibration: Optional[str] = None
    has_metabolite_identifications: Optional[Union[Union[dict, MetaboliteIdentification], List[Union[dict, MetaboliteIdentification]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MetabolomicsAnalysisId):
            self.id = MetabolomicsAnalysisId(self.id)

        if self._is_empty(self.was_informed_by):
            self.MissingRequiredField("was_informed_by")
        if not isinstance(self.was_informed_by, DataGenerationId):
            self.was_informed_by = DataGenerationId(self.was_informed_by)

        if self.has_calibration is not None and not isinstance(self.has_calibration, str):
            self.has_calibration = str(self.has_calibration)

        if not isinstance(self.has_metabolite_identifications, list):
            self.has_metabolite_identifications = [self.has_metabolite_identifications] if self.has_metabolite_identifications is not None else []
        self.has_metabolite_identifications = [v if isinstance(v, MetaboliteIdentification) else MetaboliteIdentification(**as_dict(v)) for v in self.has_metabolite_identifications]

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class MetaproteomicsAnalysis(WorkflowExecution):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["MetaproteomicsAnalysis"]
    class_class_curie: ClassVar[str] = "nmdc:MetaproteomicsAnalysis"
    class_name: ClassVar[str] = "MetaproteomicsAnalysis"
    class_model_uri: ClassVar[URIRef] = NMDC.MetaproteomicsAnalysis

    id: Union[str, MetaproteomicsAnalysisId] = None
    type: Union[str, URIorCURIE] = None
    execution_resource: Union[str, "ExecutionResourceEnum"] = None
    git_url: str = None
    started_at_time: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    was_informed_by: Union[str, DataGenerationId] = None
    has_peptide_quantifications: Optional[Union[Union[dict, PeptideQuantification], List[Union[dict, PeptideQuantification]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MetaproteomicsAnalysisId):
            self.id = MetaproteomicsAnalysisId(self.id)

        if self._is_empty(self.was_informed_by):
            self.MissingRequiredField("was_informed_by")
        if not isinstance(self.was_informed_by, DataGenerationId):
            self.was_informed_by = DataGenerationId(self.was_informed_by)

        self._normalize_inlined_as_dict(slot_name="has_peptide_quantifications", slot_type=PeptideQuantification, key_name="type", keyed=False)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class NomAnalysis(WorkflowExecution):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["NomAnalysis"]
    class_class_curie: ClassVar[str] = "nmdc:NomAnalysis"
    class_name: ClassVar[str] = "NomAnalysis"
    class_model_uri: ClassVar[URIRef] = NMDC.NomAnalysis

    id: Union[str, NomAnalysisId] = None
    type: Union[str, URIorCURIE] = None
    execution_resource: Union[str, "ExecutionResourceEnum"] = None
    git_url: str = None
    started_at_time: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    was_informed_by: Union[str, DataGenerationId] = None
    has_calibration: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NomAnalysisId):
            self.id = NomAnalysisId(self.id)

        if self._is_empty(self.was_informed_by):
            self.MissingRequiredField("was_informed_by")
        if not isinstance(self.was_informed_by, DataGenerationId):
            self.was_informed_by = DataGenerationId(self.was_informed_by)

        if self.has_calibration is not None and not isinstance(self.has_calibration, str):
            self.has_calibration = str(self.has_calibration)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


@dataclass
class CalibrationInformation(InformationObject):
    """
    A calibration object that is associated with a process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["CalibrationInformation"]
    class_class_curie: ClassVar[str] = "nmdc:CalibrationInformation"
    class_name: ClassVar[str] = "CalibrationInformation"
    class_model_uri: ClassVar[URIRef] = NMDC.CalibrationInformation

    id: Union[str, CalibrationInformationId] = None
    type: Union[str, URIorCURIE] = None
    internal_calibration: Union[bool, Bool] = None
    calibration_target: Union[str, "CalibrationTargetEnum"] = None
    calibration_object: Optional[Union[str, DataObjectId]] = None
    calibration_standard: Optional[Union[str, "CalibrationStandardEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CalibrationInformationId):
            self.id = CalibrationInformationId(self.id)

        if self._is_empty(self.internal_calibration):
            self.MissingRequiredField("internal_calibration")
        if not isinstance(self.internal_calibration, Bool):
            self.internal_calibration = Bool(self.internal_calibration)

        if self._is_empty(self.calibration_target):
            self.MissingRequiredField("calibration_target")
        if not isinstance(self.calibration_target, CalibrationTargetEnum):
            self.calibration_target = CalibrationTargetEnum(self.calibration_target)

        if self.calibration_object is not None and not isinstance(self.calibration_object, DataObjectId):
            self.calibration_object = DataObjectId(self.calibration_object)

        if self.calibration_standard is not None and not isinstance(self.calibration_standard, CalibrationStandardEnum):
            self.calibration_standard = CalibrationStandardEnum(self.calibration_standard)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_class_curie)


# Enumerations
class MassSpectrometryAcquisitionStrategyEnum(EnumDefinitionImpl):

    data_independent_acquisition = PermissibleValue(
        text="data_independent_acquisition",
        description="""['Data independent mass spectrometer acquisition method wherein the full mass range is fragmented. Examples of such an approach include MS^E, AIF, and bbCID.']""")
    data_dependent_acquisition = PermissibleValue(
        text="data_dependent_acquisition",
        description="""Mass spectrometer data acquisition method wherein MSn spectra are triggered based on the m/z of precursor ions detected in the same run.""")
    full_scan_only = PermissibleValue(
        text="full_scan_only",
        description="Mass spectrometer data acquisition method wherein only MS1 data are acquired.")

    _defn = EnumDefinition(
        name="MassSpectrometryAcquisitionStrategyEnum",
    )

class ResolutionCategoryEnum(EnumDefinitionImpl):

    high = PermissibleValue(
        text="high",
        description="higher than unit resolution")
    low = PermissibleValue(
        text="low",
        description="at unit resolution")

    _defn = EnumDefinition(
        name="ResolutionCategoryEnum",
    )

class MassAnalyzerEnum(EnumDefinitionImpl):

    time_of_flight = PermissibleValue(
        text="time_of_flight",
        description="""Instrument that separates ions by m/z in a field-free region after acceleration to a fixed acceleration energy.""")
    quadrupole = PermissibleValue(
        text="quadrupole",
        description="""A mass spectrometer that consists of four parallel rods whose centers form the corners of a square and whose opposing poles are connected. The voltage applied to the rods is a superposition of a static potential and a sinusoidal radio frequency potential. The motion of an ion in the x and y dimensions is described by the Matthieu equation whose solutions show that ions in a particular m/z range can be transmitted along the z axis.""")
    Orbitrap = PermissibleValue(
        text="Orbitrap",
        description="""An ion trapping device that consists of an outer barrel-like electrode and a coaxial inner spindle-like electrode that form an electrostatic field with quadro-logarithmic potential distribution. The frequency of harmonic oscillations of the orbitally trapped ions along the axis of the electrostatic field is independent of the ion velocity and is inversely proportional to the square root of m/z so that the trap can be used as a mass analyzer.""")
    ion_cyclotron_resonance = PermissibleValue(
        text="ion_cyclotron_resonance",
        description="""A mass spectrometer based on the principle of ion cyclotron resonance in which an ion in a magnetic field moves in a circular orbit at a frequency characteristic of its m/z value. Ions are coherently excited to a larger radius orbit using a pulse of radio frequency energy and their image charge is detected on receiver plates as a time domain signal. Fourier transformation of the time domain signal results in a frequency domain signal which is converted to a mass spectrum based in the inverse relationship between frequency and m/z.""")
    ion_trap = PermissibleValue(
        text="ion_trap",
        description="""A device for spatially confining ions using electric and magnetic fields alone or in combination.""")

    _defn = EnumDefinition(
        name="MassAnalyzerEnum",
    )

class IonizationSourceEnum(EnumDefinitionImpl):

    electrospray_ionization = PermissibleValue(text="electrospray_ionization")
    matrix_assisted_laser_desorption_ionization = PermissibleValue(text="matrix_assisted_laser_desorption_ionization")
    atmospheric_pressure_photo_ionization = PermissibleValue(text="atmospheric_pressure_photo_ionization")
    atmospheric_pressure_chemical_ionization = PermissibleValue(text="atmospheric_pressure_chemical_ionization")
    electron_ionization = PermissibleValue(text="electron_ionization")

    _defn = EnumDefinition(
        name="IonizationSourceEnum",
    )

class MassSpectrumCollectionModeEnum(EnumDefinitionImpl):

    full_profile = PermissibleValue(text="full_profile")
    reduced_profile = PermissibleValue(text="reduced_profile")
    centroid = PermissibleValue(text="centroid")

    _defn = EnumDefinition(
        name="MassSpectrumCollectionModeEnum",
    )

class PolarityModeEnum(EnumDefinitionImpl):

    positive = PermissibleValue(text="positive")
    negative = PermissibleValue(text="negative")

    _defn = EnumDefinition(
        name="PolarityModeEnum",
    )

class EluentIntroductionCategoryEnum(EnumDefinitionImpl):

    liquid_chromatography = PermissibleValue(
        text="liquid_chromatography",
        description="""The processed sample is introduced into the mass spectrometer through a liquid chromatography process.""")
    gas_chromatography = PermissibleValue(
        text="gas_chromatography",
        description="""The processed sample is introduced into the mass spectrometer through a gas chromatography process.""")
    direct_infusion_syringe = PermissibleValue(
        text="direct_infusion_syringe",
        description="""The processed sample is introduced into the mass spectrometer through a direct infusion process using a syringe.""")
    direct_infusion_autosampler = PermissibleValue(
        text="direct_infusion_autosampler",
        description="""The processed sample is introduced into the mass spectrometer through a direct infusion process using an autosampler.""")

    _defn = EnumDefinition(
        name="EluentIntroductionCategoryEnum",
    )

class LibraryTypeEnum(EnumDefinitionImpl):

    DNA = PermissibleValue(text="DNA")
    RNA = PermissibleValue(text="RNA")

    _defn = EnumDefinition(
        name="LibraryTypeEnum",
    )

class ContainerCategoryEnum(EnumDefinitionImpl):
    """
    The permitted types of containers used in processing metabolomic samples.
    """
    falcon_tube = PermissibleValue(text="falcon_tube")

    _defn = EnumDefinition(
        name="ContainerCategoryEnum",
        description="The permitted types of containers used in processing metabolomic samples.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "v-bottom_conical_tube",
            PermissibleValue(text="v-bottom_conical_tube"))

class SeparationMethodEnum(EnumDefinitionImpl):
    """
    The tool/substance used to separate or filter a solution or mixture.
    """
    ptfe_96_well_filter_plate = PermissibleValue(text="ptfe_96_well_filter_plate")
    syringe = PermissibleValue(text="syringe")

    _defn = EnumDefinition(
        name="SeparationMethodEnum",
        description="The tool/substance used to separate or filter a solution or mixture.",
    )

class StationaryPhaseEnum(EnumDefinitionImpl):
    """
    The type of stationary phase used in a chromatography process.
    """
    C18 = PermissibleValue(text="C18")
    C8 = PermissibleValue(text="C8")
    C4 = PermissibleValue(text="C4")
    C2 = PermissibleValue(text="C2")
    C1 = PermissibleValue(text="C1")
    C30 = PermissibleValue(text="C30")
    C60 = PermissibleValue(text="C60")
    CNT = PermissibleValue(text="CNT")
    CN = PermissibleValue(text="CN")
    Diol = PermissibleValue(text="Diol")
    HILIC = PermissibleValue(text="HILIC")
    NH2 = PermissibleValue(text="NH2")
    Phenyl = PermissibleValue(text="Phenyl")
    Polysiloxane = PermissibleValue(text="Polysiloxane")
    SAX = PermissibleValue(text="SAX")
    SCX = PermissibleValue(text="SCX")
    Silica = PermissibleValue(text="Silica")
    WCX = PermissibleValue(text="WCX")
    WAX = PermissibleValue(text="WAX")

    _defn = EnumDefinition(
        name="StationaryPhaseEnum",
        description="The type of stationary phase used in a chromatography process.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "BEH-HILIC",
            PermissibleValue(text="BEH-HILIC"))
        setattr(cls, "PS-DVB",
            PermissibleValue(text="PS-DVB"))
        setattr(cls, "ZIC-HILIC",
            PermissibleValue(text="ZIC-HILIC"))
        setattr(cls, "ZIC-pHILIC",
            PermissibleValue(text="ZIC-pHILIC"))
        setattr(cls, "ZIC-cHILIC",
            PermissibleValue(text="ZIC-cHILIC"))

class ProtocolCategoryEnum(EnumDefinitionImpl):
    """
    The possible protocols that may be followed for an assay.
    """
    mplex = PermissibleValue(text="mplex")
    derivatization = PermissibleValue(text="derivatization")
    filter_clean_up = PermissibleValue(text="filter_clean_up")
    organic_matter_extraction = PermissibleValue(text="organic_matter_extraction")
    solid_phase_extraction = PermissibleValue(text="solid_phase_extraction")
    phosphorus_extraction = PermissibleValue(text="phosphorus_extraction")
    ph_measurement = PermissibleValue(text="ph_measurement")
    respiration_measurement = PermissibleValue(text="respiration_measurement")
    texture_measurement = PermissibleValue(text="texture_measurement")
    dna_extraction = PermissibleValue(text="dna_extraction")
    phenol_chloroform_extraction = PermissibleValue(text="phenol_chloroform_extraction")

    _defn = EnumDefinition(
        name="ProtocolCategoryEnum",
        description="The possible protocols that may be followed for an assay.",
    )

class ChromatographicCategoryEnum(EnumDefinitionImpl):

    liquid_chromatography = PermissibleValue(text="liquid_chromatography")
    gas_chromatography = PermissibleValue(text="gas_chromatography")
    solid_phase_extraction = PermissibleValue(text="solid_phase_extraction")

    _defn = EnumDefinition(
        name="ChromatographicCategoryEnum",
    )

class SamplePortionEnum(EnumDefinitionImpl):

    supernatant = PermissibleValue(text="supernatant")
    pellet = PermissibleValue(text="pellet")
    organic_layer = PermissibleValue(text="organic_layer")
    aqueous_layer = PermissibleValue(text="aqueous_layer")
    non_polar_layer = PermissibleValue(text="non_polar_layer")

    _defn = EnumDefinition(
        name="SamplePortionEnum",
    )

class ChemicalConversionCategoryEnum(EnumDefinitionImpl):

    addition = PermissibleValue(text="addition")
    substitution = PermissibleValue(text="substitution")
    acid_base = PermissibleValue(text="acid_base")
    reduction_oxidation = PermissibleValue(text="reduction_oxidation")
    combustion = PermissibleValue(text="combustion")
    decomposition = PermissibleValue(text="decomposition")
    protease_cleavage = PermissibleValue(
        text="protease_cleavage",
        description="""an enzymatic cleavage which relies on an enzyme with protease activity to act on proteins and to produce polypeptides (protein fragments).""",
        meaning=OBI["0600056"])

    _defn = EnumDefinition(
        name="ChemicalConversionCategoryEnum",
    )

class BiosampleCategoryEnum(EnumDefinitionImpl):
    """
    Funding-based, sample location-based, or experimental method-based defined categories
    """
    LTER = PermissibleValue(
        text="LTER",
        meaning=None)
    SIP = PermissibleValue(text="SIP")
    SFA = PermissibleValue(
        text="SFA",
        description="""Science Focus Area projects funded through the Department of Energy Office of Science Biological and Environmental Research Program""",
        meaning=None)
    FICUS = PermissibleValue(
        text="FICUS",
        meaning=None)
    NEON = PermissibleValue(
        text="NEON",
        meaning=None)

    _defn = EnumDefinition(
        name="BiosampleCategoryEnum",
        description="Funding-based, sample location-based, or experimental method-based defined categories",
    )

class SubstanceRoleEnum(EnumDefinitionImpl):

    buffer = PermissibleValue(
        text="buffer",
        description="Maintains the pH of the solution within a specific range to stabilize analytes or reactions.",
        meaning=CHEBI["35225"])
    acid = PermissibleValue(
        text="acid",
        description="Donates a proton or accepts an electron pair in a chemical reaction.",
        meaning=CHEBI["37527"])
    base = PermissibleValue(
        text="base",
        description="Accepts a proton or donates an electron pair in a chemical reaction.",
        meaning=CHEBI["22695"])
    ms_proteolytic_enzyme = PermissibleValue(
        text="ms_proteolytic_enzyme",
        description="""Enzyme that catalyzes the hydrolysis of proteins and is used in mass spectrometry based proteomics""",
        meaning=MS["1002986"])
    solvent = PermissibleValue(
        text="solvent",
        description="Dissolves the sample or reagents to facilitate reactions or extraction.",
        meaning=CHEBI["46787"])
    surfactant = PermissibleValue(
        text="surfactant",
        description="Reduces surface tension and aids in the solubilization of substances.",
        meaning=CHEBI["35195"])
    derivatizing_agent = PermissibleValue(
        text="derivatizing_agent",
        description="Chemically modifies analytes to improve detection or separation.")
    solubilizing_agent = PermissibleValue(text="solubilizing_agent")

    _defn = EnumDefinition(
        name="SubstanceRoleEnum",
    )

class SampleStateEnum(EnumDefinitionImpl):

    solid = PermissibleValue(text="solid")
    liquid = PermissibleValue(text="liquid")
    gas = PermissibleValue(text="gas")

    _defn = EnumDefinition(
        name="SampleStateEnum",
    )

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
            PermissibleValue(text="semi-natural"))
        setattr(cls, "inbred line",
            PermissibleValue(text="inbred line"))
        setattr(cls, "breeder's line",
            PermissibleValue(text="breeder's line"))
        setattr(cls, "clonal selection",
            PermissibleValue(text="clonal selection"))

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
            PermissibleValue(text="free living"))

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
            PermissibleValue(text="building information model"))
        setattr(cls, "commissioning report",
            PermissibleValue(text="commissioning report"))
        setattr(cls, "complaint logs",
            PermissibleValue(text="complaint logs"))
        setattr(cls, "contract administration",
            PermissibleValue(text="contract administration"))
        setattr(cls, "cost estimate",
            PermissibleValue(text="cost estimate"))
        setattr(cls, "janitorial schedules or logs",
            PermissibleValue(text="janitorial schedules or logs"))
        setattr(cls, "maintenance plans",
            PermissibleValue(text="maintenance plans"))
        setattr(cls, "shop drawings",
            PermissibleValue(text="shop drawings"))
        setattr(cls, "ventilation system",
            PermissibleValue(text="ventilation system"))

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
            PermissibleValue(text="low rise"))
        setattr(cls, "high rise",
            PermissibleValue(text="high rise"))
        setattr(cls, "wood framed",
            PermissibleValue(text="wood framed"))
        setattr(cls, "health care",
            PermissibleValue(text="health care"))
        setattr(cls, "sports complex",
            PermissibleValue(text="sports complex"))

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
            PermissibleValue(text="visible wear"))
        setattr(cls, "needs repair",
            PermissibleValue(text="needs repair"))

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
            PermissibleValue(text="mineral fibre"))
        setattr(cls, "mineral wool/calcium silicate",
            PermissibleValue(text="mineral wool/calcium silicate"))

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
            PermissibleValue(text="crows feet"))
        setattr(cls, "crows-foot stomp",
            PermissibleValue(text="crows-foot stomp"))
        setattr(cls, "double skip",
            PermissibleValue(text="double skip"))
        setattr(cls, "hawk and trowel",
            PermissibleValue(text="hawk and trowel"))
        setattr(cls, "orange peel",
            PermissibleValue(text="orange peel"))
        setattr(cls, "rosebud stomp",
            PermissibleValue(text="rosebud stomp"))
        setattr(cls, "Santa-Fe texture",
            PermissibleValue(text="Santa-Fe texture"))
        setattr(cls, "skip trowel",
            PermissibleValue(text="skip trowel"))
        setattr(cls, "stomp knockdown",
            PermissibleValue(text="stomp knockdown"))

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
            PermissibleValue(text="barrel-shaped"))

class CurLandUseEnum(EnumDefinitionImpl):

    badlands = PermissibleValue(text="badlands")
    cities = PermissibleValue(text="cities")
    conifers = PermissibleValue(text="conifers")
    farmstead = PermissibleValue(text="farmstead")
    gravel = PermissibleValue(text="gravel")
    hardwoods = PermissibleValue(text="hardwoods")
    hayland = PermissibleValue(text="hayland")
    marshlands = PermissibleValue(text="marshlands")
    meadows = PermissibleValue(text="meadows")
    mudflats = PermissibleValue(text="mudflats")
    pastureland = PermissibleValue(text="pastureland")
    rainforest = PermissibleValue(text="rainforest")
    rangeland = PermissibleValue(text="rangeland")
    rock = PermissibleValue(text="rock")
    sand = PermissibleValue(text="sand")
    swamp = PermissibleValue(text="swamp")
    tropical = PermissibleValue(text="tropical")
    tundra = PermissibleValue(text="tundra")

    _defn = EnumDefinition(
        name="CurLandUseEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "crop trees",
            PermissibleValue(text="crop trees"))
        setattr(cls, "horticultural plants",
            PermissibleValue(text="horticultural plants"))
        setattr(cls, "industrial areas",
            PermissibleValue(text="industrial areas"))
        setattr(cls, "intermixed hardwood and conifers",
            PermissibleValue(text="intermixed hardwood and conifers"))
        setattr(cls, "mines/quarries",
            PermissibleValue(text="mines/quarries"))
        setattr(cls, "oil waste areas",
            PermissibleValue(text="oil waste areas"))
        setattr(cls, "permanent snow or ice",
            PermissibleValue(text="permanent snow or ice"))
        setattr(cls, "roads/railroads",
            PermissibleValue(text="roads/railroads"))
        setattr(cls, "row crops",
            PermissibleValue(text="row crops"))
        setattr(cls, "saline seeps",
            PermissibleValue(text="saline seeps"))
        setattr(cls, "salt flats",
            PermissibleValue(text="salt flats"))
        setattr(cls, "shrub crops",
            PermissibleValue(text="shrub crops"))
        setattr(cls, "shrub land",
            PermissibleValue(text="shrub land"))
        setattr(cls, "small grains",
            PermissibleValue(text="small grains"))
        setattr(cls, "successional shrub land",
            PermissibleValue(text="successional shrub land"))
        setattr(cls, "vegetable crops",
            PermissibleValue(text="vegetable crops"))
        setattr(cls, "vine crops",
            PermissibleValue(text="vine crops"))

class DeposEnvEnum(EnumDefinitionImpl):

    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="DeposEnvEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Continental - Alluvial",
            PermissibleValue(text="Continental - Alluvial"))
        setattr(cls, "Continental - Aeolian",
            PermissibleValue(text="Continental - Aeolian"))
        setattr(cls, "Continental - Fluvial",
            PermissibleValue(text="Continental - Fluvial"))
        setattr(cls, "Continental - Lacustrine",
            PermissibleValue(text="Continental - Lacustrine"))
        setattr(cls, "Transitional - Deltaic",
            PermissibleValue(text="Transitional - Deltaic"))
        setattr(cls, "Transitional - Tidal",
            PermissibleValue(text="Transitional - Tidal"))
        setattr(cls, "Transitional - Lagoonal",
            PermissibleValue(text="Transitional - Lagoonal"))
        setattr(cls, "Transitional - Beach",
            PermissibleValue(text="Transitional - Beach"))
        setattr(cls, "Transitional - Lake",
            PermissibleValue(text="Transitional - Lake"))
        setattr(cls, "Marine - Shallow",
            PermissibleValue(text="Marine - Shallow"))
        setattr(cls, "Marine - Deep",
            PermissibleValue(text="Marine - Deep"))
        setattr(cls, "Marine - Reef",
            PermissibleValue(text="Marine - Reef"))
        setattr(cls, "Other - Evaporite",
            PermissibleValue(text="Other - Evaporite"))
        setattr(cls, "Other - Glacial",
            PermissibleValue(text="Other - Glacial"))
        setattr(cls, "Other - Volcanic",
            PermissibleValue(text="Other - Volcanic"))

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
            PermissibleValue(text="metal covered"))

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
            PermissibleValue(text="needs repair"))
        setattr(cls, "visible wear",
            PermissibleValue(text="visible wear"))

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
            PermissibleValue(text="cellular PVC"))
        setattr(cls, "engineered plastic",
            PermissibleValue(text="engineered plastic"))
        setattr(cls, "thermoplastic alloy",
            PermissibleValue(text="thermoplastic alloy"))
        setattr(cls, "wood/plastic composite",
            PermissibleValue(text="wood/plastic composite"))

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
            PermissibleValue(text="rolling shutter"))

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
            PermissibleValue(text="corrugated steel"))
        setattr(cls, "rolling shutters",
            PermissibleValue(text="rolling shutters"))
        setattr(cls, "steel plate",
            PermissibleValue(text="steel plate"))

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
            PermissibleValue(text="bettened and ledged"))
        setattr(cls, "ledged and braced",
            PermissibleValue(text="ledged and braced"))
        setattr(cls, "ledged and framed",
            PermissibleValue(text="ledged and framed"))
        setattr(cls, "ledged, braced and frame",
            PermissibleValue(text="ledged, braced and frame"))
        setattr(cls, "framed and paneled",
            PermissibleValue(text="framed and paneled"))
        setattr(cls, "glashed or sash",
            PermissibleValue(text="glashed or sash"))
        setattr(cls, "wire gauged",
            PermissibleValue(text="wire gauged"))

class DrainageClassEnum(EnumDefinitionImpl):

    poorly = PermissibleValue(text="poorly")
    well = PermissibleValue(text="well")

    _defn = EnumDefinition(
        name="DrainageClassEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "very poorly",
            PermissibleValue(text="very poorly"))
        setattr(cls, "somewhat poorly",
            PermissibleValue(text="somewhat poorly"))
        setattr(cls, "moderately well",
            PermissibleValue(text="moderately well"))
        setattr(cls, "excessively drained",
            PermissibleValue(text="excessively drained"))

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
            PermissibleValue(text="as built"))
        setattr(cls, "building navigation map",
            PermissibleValue(text="building navigation map"))

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
            PermissibleValue(text="particulate air filter"))
        setattr(cls, "chemical air filter",
            PermissibleValue(text="chemical air filter"))
        setattr(cls, "low-MERV pleated media",
            PermissibleValue(text="low-MERV pleated media"))
        setattr(cls, "gas-phase or ultraviolet air treatments",
            PermissibleValue(text="gas-phase or ultraviolet air treatments"))

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
            PermissibleValue(text="visible wear"))
        setattr(cls, "needs repair",
            PermissibleValue(text="needs repair"))

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
            PermissibleValue(text="wood strip or parquet"))
        setattr(cls, "laminate wood",
            PermissibleValue(text="laminate wood"))
        setattr(cls, "vinyl composition tile",
            PermissibleValue(text="vinyl composition tile"))
        setattr(cls, "sheet vinyl",
            PermissibleValue(text="sheet vinyl"))
        setattr(cls, "clear finish",
            PermissibleValue(text="clear finish"))
        setattr(cls, "none or unfinished",
            PermissibleValue(text="none or unfinished"))

class FloorStrucEnum(EnumDefinitionImpl):

    balcony = PermissibleValue(text="balcony")
    concrete = PermissibleValue(text="concrete")

    _defn = EnumDefinition(
        name="FloorStrucEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "floating floor",
            PermissibleValue(text="floating floor"))
        setattr(cls, "glass floor",
            PermissibleValue(text="glass floor"))
        setattr(cls, "raised floor",
            PermissibleValue(text="raised floor"))
        setattr(cls, "sprung floor",
            PermissibleValue(text="sprung floor"))
        setattr(cls, "wood-framed",
            PermissibleValue(text="wood-framed"))

class FloorWaterMoldEnum(EnumDefinitionImpl):

    condensation = PermissibleValue(text="condensation")

    _defn = EnumDefinition(
        name="FloorWaterMoldEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "mold odor",
            PermissibleValue(text="mold odor"))
        setattr(cls, "wet floor",
            PermissibleValue(text="wet floor"))
        setattr(cls, "water stains",
            PermissibleValue(text="water stains"))
        setattr(cls, "wall discoloration",
            PermissibleValue(text="wall discoloration"))
        setattr(cls, "floor discoloration",
            PermissibleValue(text="floor discoloration"))
        setattr(cls, "ceiling discoloration",
            PermissibleValue(text="ceiling discoloration"))
        setattr(cls, "peeling paint or wallpaper",
            PermissibleValue(text="peeling paint or wallpaper"))
        setattr(cls, "bulging walls",
            PermissibleValue(text="bulging walls"))

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
            PermissibleValue(text="all gender"))
        setattr(cls, "gender neurtral",
            PermissibleValue(text="gender neurtral"))
        setattr(cls, "male and female",
            PermissibleValue(text="male and female"))

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
            PermissibleValue(text="semi-erect"))

class HandidnessEnum(EnumDefinitionImpl):

    ambidexterity = PermissibleValue(text="ambidexterity")

    _defn = EnumDefinition(
        name="HandidnessEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "left handedness",
            PermissibleValue(text="left handedness"))
        setattr(cls, "mixed-handedness",
            PermissibleValue(text="mixed-handedness"))
        setattr(cls, "right handedness",
            PermissibleValue(text="right handedness"))

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
            PermissibleValue(text="Gas-Condensate"))
        setattr(cls, "Coalbed Methane",
            PermissibleValue(text="Coalbed Methane"))

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
            PermissibleValue(text="Oil Reservoir"))
        setattr(cls, "Gas Reservoir",
            PermissibleValue(text="Gas Reservoir"))
        setattr(cls, "Oil Sand",
            PermissibleValue(text="Oil Sand"))
        setattr(cls, "Tight Oil Reservoir",
            PermissibleValue(text="Tight Oil Reservoir"))
        setattr(cls, "Tight Gas Reservoir",
            PermissibleValue(text="Tight Gas Reservoir"))

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
            PermissibleValue(text="radiant system"))
        setattr(cls, "heat pump",
            PermissibleValue(text="heat pump"))
        setattr(cls, "forced air system",
            PermissibleValue(text="forced air system"))
        setattr(cls, "steam forced heat",
            PermissibleValue(text="steam forced heat"))
        setattr(cls, "wood stove",
            PermissibleValue(text="wood stove"))

class HeatDelivLocEnum(EnumDefinitionImpl):

    north = PermissibleValue(text="north")
    south = PermissibleValue(text="south")
    east = PermissibleValue(text="east")
    west = PermissibleValue(text="west")

    _defn = EnumDefinition(
        name="HeatDelivLocEnum",
    )

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
            PermissibleValue(text="locker room"))

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
            PermissibleValue(text="counter top"))
        setattr(cls, "vent cover",
            PermissibleValue(text="vent cover"))

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
            PermissibleValue(text="visible wear"))
        setattr(cls, "needs repair",
            PermissibleValue(text="needs repair"))

class LightTypeEnum(EnumDefinitionImpl):

    none = PermissibleValue(text="none")

    _defn = EnumDefinition(
        name="LightTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "natural light",
            PermissibleValue(text="natural light"))
        setattr(cls, "electric light",
            PermissibleValue(text="electric light"))
        setattr(cls, "desk lamp",
            PermissibleValue(text="desk lamp"))
        setattr(cls, "flourescent lights",
            PermissibleValue(text="flourescent lights"))

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
            PermissibleValue(text="automated count"))
        setattr(cls, "manual count",
            PermissibleValue(text="manual count"))

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
            PermissibleValue(text="other artificial liquid medium"))
        setattr(cls, "other artificial solid medium",
            PermissibleValue(text="other artificial solid medium"))
        setattr(cls, "peat moss",
            PermissibleValue(text="peat moss"))

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
            PermissibleValue(text="North side"))
        setattr(cls, "West side",
            PermissibleValue(text="West side"))
        setattr(cls, "South side",
            PermissibleValue(text="South side"))
        setattr(cls, "East side",
            PermissibleValue(text="East side"))

class RelSampLocEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="RelSampLocEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "edge of car",
            PermissibleValue(text="edge of car"))
        setattr(cls, "center of car",
            PermissibleValue(text="center of car"))
        setattr(cls, "under a seat",
            PermissibleValue(text="under a seat"))

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
            PermissibleValue(text="visible wear"))
        setattr(cls, "needs repair",
            PermissibleValue(text="needs repair"))
        setattr(cls, "visible signs of mold/mildew",
            PermissibleValue(text="visible signs of mold/mildew"))

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
            PermissibleValue(text="conference room"))
        setattr(cls, "examining room",
            PermissibleValue(text="examining room"))
        setattr(cls, "mail room",
            PermissibleValue(text="mail room"))

class RoomLocEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="RoomLocEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "corner room",
            PermissibleValue(text="corner room"))
        setattr(cls, "interior room",
            PermissibleValue(text="interior room"))
        setattr(cls, "exterior wall",
            PermissibleValue(text="exterior wall"))

class RoomSampPosEnum(EnumDefinitionImpl):

    center = PermissibleValue(text="center")

    _defn = EnumDefinition(
        name="RoomSampPosEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "north corner",
            PermissibleValue(text="north corner"))
        setattr(cls, "south corner",
            PermissibleValue(text="south corner"))
        setattr(cls, "west corner",
            PermissibleValue(text="west corner"))
        setattr(cls, "east corner",
            PermissibleValue(text="east corner"))
        setattr(cls, "northeast corner",
            PermissibleValue(text="northeast corner"))
        setattr(cls, "northwest corner",
            PermissibleValue(text="northwest corner"))
        setattr(cls, "southeast corner",
            PermissibleValue(text="southeast corner"))
        setattr(cls, "southwest corner",
            PermissibleValue(text="southwest corner"))

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
            PermissibleValue(text="conference room"))
        setattr(cls, "examining room",
            PermissibleValue(text="examining room"))
        setattr(cls, "mail room",
            PermissibleValue(text="mail room"))
        setattr(cls, "private office",
            PermissibleValue(text="private office"))
        setattr(cls, "open office",
            PermissibleValue(text="open office"))
        setattr(cls, ",restroom",
            PermissibleValue(text=",restroom"))
        setattr(cls, "mechanical or electrical room",
            PermissibleValue(text="mechanical or electrical room"))
        setattr(cls, "data center",
            PermissibleValue(text="data center"))

class SampCaptStatusEnum(EnumDefinitionImpl):

    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="SampCaptStatusEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "active surveillance in response to an outbreak",
            PermissibleValue(text="active surveillance in response to an outbreak"))
        setattr(cls, "active surveillance not initiated by an outbreak",
            PermissibleValue(text="active surveillance not initiated by an outbreak"))
        setattr(cls, "farm sample",
            PermissibleValue(text="farm sample"))
        setattr(cls, "market sample",
            PermissibleValue(text="market sample"))

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
            PermissibleValue(text="test well"))
        setattr(cls, "drilling rig",
            PermissibleValue(text="drilling rig"))
        setattr(cls, "storage tank",
            PermissibleValue(text="storage tank"))

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
            PermissibleValue(text="growth and reproduction"))

class SampFloorEnum(EnumDefinitionImpl):

    basement = PermissibleValue(text="basement")
    lobby = PermissibleValue(text="lobby")

    _defn = EnumDefinition(
        name="SampFloorEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "1st floor",
            PermissibleValue(text="1st floor"))
        setattr(cls, "2nd floor",
            PermissibleValue(text="2nd floor"))

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
            PermissibleValue(text="oil phase"))
        setattr(cls, "water phase",
            PermissibleValue(text="water phase"))
        setattr(cls, "not applicable",
            PermissibleValue(text="not applicable"))

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
            PermissibleValue(text="clear sky"))

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
            PermissibleValue(text="needs repair"))
        setattr(cls, "visible wear",
            PermissibleValue(text="visible wear"))

class ShadingDeviceTypeEnum(EnumDefinitionImpl):

    tree = PermissibleValue(text="tree")
    trellis = PermissibleValue(text="trellis")

    _defn = EnumDefinition(
        name="ShadingDeviceTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "bahama shutters",
            PermissibleValue(text="bahama shutters"))
        setattr(cls, "exterior roll blind",
            PermissibleValue(text="exterior roll blind"))
        setattr(cls, "gambrel awning",
            PermissibleValue(text="gambrel awning"))
        setattr(cls, "hood awning",
            PermissibleValue(text="hood awning"))
        setattr(cls, "porchroller awning",
            PermissibleValue(text="porchroller awning"))
        setattr(cls, "sarasota shutters",
            PermissibleValue(text="sarasota shutters"))
        setattr(cls, "slatted aluminum",
            PermissibleValue(text="slatted aluminum"))
        setattr(cls, "solid aluminum awning",
            PermissibleValue(text="solid aluminum awning"))
        setattr(cls, "sun screen",
            PermissibleValue(text="sun screen"))
        setattr(cls, "venetian awning",
            PermissibleValue(text="venetian awning"))

class SoilHorizonEnum(EnumDefinitionImpl):

    Permafrost = PermissibleValue(text="Permafrost")

    _defn = EnumDefinition(
        name="SoilHorizonEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "O horizon",
            PermissibleValue(text="O horizon"))
        setattr(cls, "A horizon",
            PermissibleValue(text="A horizon"))
        setattr(cls, "E horizon",
            PermissibleValue(text="E horizon"))
        setattr(cls, "B horizon",
            PermissibleValue(text="B horizon"))
        setattr(cls, "C horizon",
            PermissibleValue(text="C horizon"))
        setattr(cls, "R layer",
            PermissibleValue(text="R layer"))
        setattr(cls, "M horizon",
            PermissibleValue(text="M horizon"))

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
            PermissibleValue(text="as built"))

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
            PermissibleValue(text="Type I"))
        setattr(cls, "Type II",
            PermissibleValue(text="Type II"))
        setattr(cls, "Type III",
            PermissibleValue(text="Type III"))
        setattr(cls, "Type IV",
            PermissibleValue(text="Type IV"))

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
            PermissibleValue(text="slab on grade"))

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
            PermissibleValue(text="organic matter"))
        setattr(cls, "particulate matter",
            PermissibleValue(text="particulate matter"))
        setattr(cls, "volatile organic compounds",
            PermissibleValue(text="volatile organic compounds"))
        setattr(cls, "biological contaminants",
            PermissibleValue(text="biological contaminants"))

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
            PermissibleValue(text="cinder blocks"))
        setattr(cls, "hay bales",
            PermissibleValue(text="hay bales"))
        setattr(cls, "stainless steel",
            PermissibleValue(text="stainless steel"))

class TidalStageEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="TidalStageEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "low tide",
            PermissibleValue(text="low tide"))
        setattr(cls, "ebb tide",
            PermissibleValue(text="ebb tide"))
        setattr(cls, "flood tide",
            PermissibleValue(text="flood tide"))
        setattr(cls, "high tide",
            PermissibleValue(text="high tide"))

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
            PermissibleValue(text="cutting disc"))
        setattr(cls, "ridge till",
            PermissibleValue(text="ridge till"))
        setattr(cls, "strip tillage",
            PermissibleValue(text="strip tillage"))
        setattr(cls, "zonal tillage",
            PermissibleValue(text="zonal tillage"))
        setattr(cls, "disc plough",
            PermissibleValue(text="disc plough"))

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
            PermissibleValue(text="south station above ground"))
        setattr(cls, "south station underground",
            PermissibleValue(text="south station underground"))
        setattr(cls, "south station amtrak",
            PermissibleValue(text="south station amtrak"))
        setattr(cls, "forest hills",
            PermissibleValue(text="forest hills"))

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
            PermissibleValue(text="commonly of the building"))
        setattr(cls, "site context (adjacent buildings, vegetation, terrain, streets)",
            PermissibleValue(text="site context (adjacent buildings, vegetation, terrain, streets)"))
        setattr(cls, "3D scans",
            PermissibleValue(text="3D scans"))

class WallConstTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="WallConstTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "frame construction",
            PermissibleValue(text="frame construction"))
        setattr(cls, "joisted masonry",
            PermissibleValue(text="joisted masonry"))
        setattr(cls, "light noncombustible",
            PermissibleValue(text="light noncombustible"))
        setattr(cls, "masonry noncombustible",
            PermissibleValue(text="masonry noncombustible"))
        setattr(cls, "modified fire resistive",
            PermissibleValue(text="modified fire resistive"))
        setattr(cls, "fire resistive",
            PermissibleValue(text="fire resistive"))

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
            PermissibleValue(text="gypsum plaster"))
        setattr(cls, "veneer plaster",
            PermissibleValue(text="veneer plaster"))
        setattr(cls, "gypsum board",
            PermissibleValue(text="gypsum board"))
        setattr(cls, "stone facing",
            PermissibleValue(text="stone facing"))
        setattr(cls, "acoustical treatment",
            PermissibleValue(text="acoustical treatment"))

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
            PermissibleValue(text="wall paper"))
        setattr(cls, "no treatment",
            PermissibleValue(text="no treatment"))

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
            PermissibleValue(text="crows feet"))
        setattr(cls, "crows-foot stomp",
            PermissibleValue(text="crows-foot stomp"))
        setattr(cls, "",
            PermissibleValue(text=""))
        setattr(cls, "double skip",
            PermissibleValue(text="double skip"))
        setattr(cls, "hawk and trowel",
            PermissibleValue(text="hawk and trowel"))
        setattr(cls, "orange peel",
            PermissibleValue(text="orange peel"))
        setattr(cls, "rosebud stomp",
            PermissibleValue(text="rosebud stomp"))
        setattr(cls, "Santa-Fe texture",
            PermissibleValue(text="Santa-Fe texture"))
        setattr(cls, "skip trowel",
            PermissibleValue(text="skip trowel"))
        setattr(cls, "stomp knockdown",
            PermissibleValue(text="stomp knockdown"))

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
            PermissibleValue(text="standing feature"))

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
            PermissibleValue(text="needs repair"))
        setattr(cls, "visible wear",
            PermissibleValue(text="visible wear"))

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
            PermissibleValue(text="single-hung sash window"))
        setattr(cls, "horizontal sash window",
            PermissibleValue(text="horizontal sash window"))
        setattr(cls, "fixed window",
            PermissibleValue(text="fixed window"))

class WindowVertPosEnum(EnumDefinitionImpl):

    bottom = PermissibleValue(text="bottom")
    middle = PermissibleValue(text="middle")
    top = PermissibleValue(text="top")
    low = PermissibleValue(text="low")
    high = PermissibleValue(text="high")

    _defn = EnumDefinition(
        name="WindowVertPosEnum",
    )

class CreditEnum(EnumDefinitionImpl):

    Conceptualization = PermissibleValue(
        text="Conceptualization",
        description="Conceptualization")
    Investigation = PermissibleValue(
        text="Investigation",
        description="Investigation")
    Methodology = PermissibleValue(
        text="Methodology",
        description="Methodology")
    Resources = PermissibleValue(
        text="Resources",
        description="Resources")
    Software = PermissibleValue(
        text="Software",
        description="Software")
    Supervision = PermissibleValue(
        text="Supervision",
        description="Supervision")
    Validation = PermissibleValue(
        text="Validation",
        description="Validation")
    Visualization = PermissibleValue(
        text="Visualization",
        description="Visualization")
    Submitter = PermissibleValue(
        text="Submitter",
        description="the person(s) who enter study and biosample metadata into the NMDC submission portal",
        meaning=EFO["0001741"])

    _defn = EnumDefinition(
        name="CreditEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Data curation",
            PermissibleValue(
                text="Data curation",
                description="Data curation"))
        setattr(cls, "Formal Analysis",
            PermissibleValue(
                text="Formal Analysis",
                description="Formal Analysis"))
        setattr(cls, "Funding acquisition",
            PermissibleValue(
                text="Funding acquisition",
                description="Funding acquisition"))
        setattr(cls, "Project administration",
            PermissibleValue(
                text="Project administration",
                description="Project administration"))
        setattr(cls, "Writing original draft",
            PermissibleValue(
                text="Writing original draft",
                description="Writing – original draft"))
        setattr(cls, "Writing review and editing",
            PermissibleValue(
                text="Writing review and editing",
                description="Writing – review & editing"))
        setattr(cls, "Principal Investigator",
            PermissibleValue(
                text="Principal Investigator",
                description="principal investigator role",
                meaning=OBI["0000103"]))

class StudyCategoryEnum(EnumDefinitionImpl):

    research_study = PermissibleValue(
        text="research_study",
        description="A detailed examination, analysis, or critical inspection of a hypothesis-driven experiment.")
    consortium = PermissibleValue(
        text="consortium",
        description="""A group formed to undertake a venture that is beyond the capabilities of the individual members. Each member of the consortium brings a high level of expertise in a specific area to ensure the successful completion of the project.""")

    _defn = EnumDefinition(
        name="StudyCategoryEnum",
    )

class InstrumentModelEnum(EnumDefinitionImpl):

    exploris_21T = PermissibleValue(text="exploris_21T")
    exploris_240 = PermissibleValue(text="exploris_240")
    exploris_480 = PermissibleValue(text="exploris_480")
    ltq_orbitrap_velos = PermissibleValue(text="ltq_orbitrap_velos")
    orbitrap_fusion_lumos = PermissibleValue(text="orbitrap_fusion_lumos")
    orbitrap_eclipse_tribid = PermissibleValue(text="orbitrap_eclipse_tribid")
    orbitrap_q_exactive = PermissibleValue(text="orbitrap_q_exactive")
    solarix_7T = PermissibleValue(text="solarix_7T")
    solarix_12T = PermissibleValue(text="solarix_12T")
    solarix_15T = PermissibleValue(text="solarix_15T")
    agilent_8890A = PermissibleValue(text="agilent_8890A")
    agilent_7980A = PermissibleValue(text="agilent_7980A")
    vortex_genie_2 = PermissibleValue(text="vortex_genie_2")
    novaseq = PermissibleValue(text="novaseq")
    novaseq_6000 = PermissibleValue(
        text="novaseq_6000",
        meaning=OBI["0002630"])
    hiseq = PermissibleValue(text="hiseq")
    hiseq_1000 = PermissibleValue(
        text="hiseq_1000",
        meaning=OBI["0002022"])
    hiseq_1500 = PermissibleValue(
        text="hiseq_1500",
        meaning=OBI["0003386"])
    hiseq_2000 = PermissibleValue(
        text="hiseq_2000",
        meaning=OBI["0002001"])
    hiseq_2500 = PermissibleValue(
        text="hiseq_2500",
        meaning=OBI["0002002"])
    hiseq_3000 = PermissibleValue(
        text="hiseq_3000",
        meaning=OBI["0002048"])
    hiseq_4000 = PermissibleValue(
        text="hiseq_4000",
        meaning=OBI["0002049"])
    hiseq_x_ten = PermissibleValue(
        text="hiseq_x_ten",
        meaning=OBI["0002129"])
    miniseq = PermissibleValue(
        text="miniseq",
        meaning=OBI["0003114"])
    nextseq_1000 = PermissibleValue(
        text="nextseq_1000",
        meaning=OBI["0003606"])
    miseq = PermissibleValue(
        text="miseq",
        meaning=OBI["0002003"])
    nextseq_500 = PermissibleValue(
        text="nextseq_500",
        meaning=OBI["0002021"])
    nextseq_550 = PermissibleValue(
        text="nextseq_550",
        meaning=OBI["0003387"])
    gridion = PermissibleValue(
        text="gridion",
        meaning=OBI["0002751"])
    minion = PermissibleValue(
        text="minion",
        meaning=OBI["0002750"])
    promethion = PermissibleValue(
        text="promethion",
        meaning=OBI["0002752"])
    rs_II = PermissibleValue(
        text="rs_II",
        meaning=OBI["0002012"])
    sequel = PermissibleValue(
        text="sequel",
        meaning=OBI["0002632"])
    sequel_II = PermissibleValue(
        text="sequel_II",
        meaning=OBI["0002633"])
    revio = PermissibleValue(text="revio")

    _defn = EnumDefinition(
        name="InstrumentModelEnum",
    )

class InstrumentVendorEnum(EnumDefinitionImpl):

    waters = PermissibleValue(text="waters")
    agilent = PermissibleValue(text="agilent")
    bruker = PermissibleValue(text="bruker")
    thermo_fisher = PermissibleValue(text="thermo_fisher")
    vwr = PermissibleValue(text="vwr")
    perkin_elmer = PermissibleValue(text="perkin_elmer")
    gilson = PermissibleValue(text="gilson")
    scientific_industries = PermissibleValue(text="scientific_industries")
    illumina = PermissibleValue(
        text="illumina",
        meaning=OBI["0000759"])
    pacbio = PermissibleValue(
        text="pacbio",
        meaning=OBI["0001856"])
    oxford_nanopore = PermissibleValue(
        text="oxford_nanopore",
        meaning=OBI["0002755"])
    pnnl = PermissibleValue(text="pnnl")

    _defn = EnumDefinition(
        name="InstrumentVendorEnum",
    )

class FailureWhatEnum(EnumDefinitionImpl):
    """
    The permitted values for describing where a failure occurred during processing in the lab during analysis
    workflows.
    """
    low_read_count = PermissibleValue(
        text="low_read_count",
        description="Number of output reads is not sufficient to continue to the next analysis step.")
    malformed_data = PermissibleValue(
        text="malformed_data",
        description="Workflow failure reading input or writing the output file(s).")
    assembly_size_too_small = PermissibleValue(
        text="assembly_size_too_small",
        description="""The size of the metagenome or metatranscriptome assembly is too small to proceed to the next analysis workflow.""")
    no_valid_data_generated = PermissibleValue(
        text="no_valid_data_generated",
        description="""A process ran but did not produce any output. Ie binning ran but did not produce any medium or high quality bins.""")
    other = PermissibleValue(
        text="other",
        description="""A lab process or analysis workflow has failed in a way that has not been captured by the available values yet. Please use slot 'qc_comment' to specify details.""")

    _defn = EnumDefinition(
        name="FailureWhatEnum",
        description="""The permitted values for describing where a failure occurred during processing in the lab during analysis workflows.""",
    )

class FailureWhereEnum(EnumDefinitionImpl):
    """
    The permitted values for describing where in the process, either a lab or analysis workflow step, the failure
    occurred.
    """
    NucleotideSequencing = PermissibleValue(
        text="NucleotideSequencing",
        description="A failure has occurred during nucleotide sequencing, a data generation process.")
    Pooling = PermissibleValue(
        text="Pooling",
        description="A failure has occurred in pooling, a lab process.")
    Extraction = PermissibleValue(
        text="Extraction",
        description="A failure has occurred in extraction, a lab process.")
    LibraryPreparation = PermissibleValue(
        text="LibraryPreparation",
        description="A failure has occurred in library preparation, a lab process.")
    MetagenomeAssembly = PermissibleValue(
        text="MetagenomeAssembly",
        description="A failure has occurred in metagenome assembly, a workflow process.")
    MetatranscriptomeAnalysis = PermissibleValue(
        text="MetatranscriptomeAnalysis",
        description="A failure has occurred in metatranscriptome analysis, a workflow process.")
    MagsAnalysis = PermissibleValue(
        text="MagsAnalysis",
        description="""A failure has occurred in binning, a workflow process to generate metagenome-assembled genomes (MAGS).""")
    ReadQcAnalysis = PermissibleValue(
        text="ReadQcAnalysis",
        description="A failure has occurred in read qc, a workflow process.")
    ReadBasedTaxonomyAnalysis = PermissibleValue(
        text="ReadBasedTaxonomyAnalysis",
        description="A failure has occurred in reads based taxonomy, a workflow process.")
    MetagenomeAnnotation = PermissibleValue(
        text="MetagenomeAnnotation",
        description="A failure has occurred in annotation, a workflow process.")

    _defn = EnumDefinition(
        name="FailureWhereEnum",
        description="""The permitted values for describing where in the process, either a lab or analysis workflow step, the failure occurred.""",
    )

class ExecutionResourceEnum(EnumDefinitionImpl):

    EMSL = PermissibleValue(
        text="EMSL",
        description="Environmental Molecular Sciences Laboratory")
    JGI = PermissibleValue(
        text="JGI",
        description="Joint Genome Institute")

    _defn = EnumDefinition(
        name="ExecutionResourceEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "NERSC-Cori",
            PermissibleValue(
                text="NERSC-Cori",
                description="NERSC Cori supercomputer"))
        setattr(cls, "NERSC-Perlmutter",
            PermissibleValue(
                text="NERSC-Perlmutter",
                description="NERSC Perlmutter supercomputer"))
        setattr(cls, "EMSL-RZR",
            PermissibleValue(
                text="EMSL-RZR",
                description="Environmental Molecular Sciences Laboratory RZR cluster"))
        setattr(cls, "LANL-B-div",
            PermissibleValue(
                text="LANL-B-div",
                description="LANL Bioscience Division"))

class FileTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="FileTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Metagenome Raw Reads",
            PermissibleValue(
                text="Metagenome Raw Reads",
                description="Interleaved paired-end raw sequencing data"))
        setattr(cls, "Metagenome Raw Read 1",
            PermissibleValue(
                text="Metagenome Raw Read 1",
                description="Read 1 raw sequencing data, aka forward reads"))
        setattr(cls, "Metagenome Raw Read 2",
            PermissibleValue(
                text="Metagenome Raw Read 2",
                description="Read 2 raw sequencing data, aka reverse reads"))
        setattr(cls, "FT ICR-MS Analysis Results",
            PermissibleValue(
                text="FT ICR-MS Analysis Results",
                description="FT ICR-MS-based molecular formula assignment results table"))
        setattr(cls, "GC-MS Metabolomics Results",
            PermissibleValue(
                text="GC-MS Metabolomics Results",
                description="GC-MS-based metabolite assignment results table"))
        setattr(cls, "Metaproteomics Workflow Statistics",
            PermissibleValue(
                text="Metaproteomics Workflow Statistics",
                description="Aggregate workflow statistics file"))
        setattr(cls, "Protein Report",
            PermissibleValue(
                text="Protein Report",
                description="Filtered protein report file"))
        setattr(cls, "Peptide Report",
            PermissibleValue(
                text="Peptide Report",
                description="Filtered peptide report file"))
        setattr(cls, "Unfiltered Metaproteomics Results",
            PermissibleValue(
                text="Unfiltered Metaproteomics Results",
                description="MSGFjobs and MASIC output file"))
        setattr(cls, "Read Count and RPKM",
            PermissibleValue(
                text="Read Count and RPKM",
                description="Annotation read count and RPKM per feature JSON"))
        setattr(cls, "QC non-rRNA R2",
            PermissibleValue(
                text="QC non-rRNA R2",
                description="QC removed rRNA reads (R2) fastq"))
        setattr(cls, "QC non-rRNA R1",
            PermissibleValue(
                text="QC non-rRNA R1",
                description="QC removed rRNA reads (R1) fastq"))
        setattr(cls, "Metagenome Bins",
            PermissibleValue(
                text="Metagenome Bins",
                description="Metagenome bin contigs fasta"))
        setattr(cls, "Metagenome HQMQ Bins Compression File",
            PermissibleValue(
                text="Metagenome HQMQ Bins Compression File",
                description="""Compressed file containing high qulaity and medium quality metagenome bins and associated files"""))
        setattr(cls, "Metagenome LQ Bins Compression File",
            PermissibleValue(
                text="Metagenome LQ Bins Compression File",
                description="Compressed file containing low quality metagenome bins and associated files"))
        setattr(cls, "Metagenome Bins Info File",
            PermissibleValue(
                text="Metagenome Bins Info File",
                description="File containing version information on the binning workflow"))
        setattr(cls, "CheckM Statistics",
            PermissibleValue(
                text="CheckM Statistics",
                description="CheckM statistics report"))
        setattr(cls, "Metagenome Bins Heatmap",
            PermissibleValue(
                text="Metagenome Bins Heatmap",
                description="""The Heatmap presents the pdf file containing the KO analysis results for metagenome bins"""))
        setattr(cls, "Metagenome Bins Barplot",
            PermissibleValue(
                text="Metagenome Bins Barplot",
                description="""The Bar chart presents the pdf file containing the KO analysis results for metagenome bins"""))
        setattr(cls, "Metagenome Bins Krona Plot",
            PermissibleValue(
                text="Metagenome Bins Krona Plot",
                description="""The Krona plot presents the HTML file containing the KO analysis results for metagenome bins"""))
        setattr(cls, "Read Based Analysis Info File",
            PermissibleValue(
                text="Read Based Analysis Info File",
                description="File containing reads based analysis information"))
        setattr(cls, "GTDBTK Bacterial Summary",
            PermissibleValue(
                text="GTDBTK Bacterial Summary",
                description="GTDBTK bacterial summary"))
        setattr(cls, "GTDBTK Archaeal Summary",
            PermissibleValue(
                text="GTDBTK Archaeal Summary",
                description="GTDBTK archaeal summary"))
        setattr(cls, "GOTTCHA2 Krona Plot",
            PermissibleValue(
                text="GOTTCHA2 Krona Plot",
                description="GOTTCHA2 krona plot HTML file"))
        setattr(cls, "GOTTCHA2 Classification Report",
            PermissibleValue(
                text="GOTTCHA2 Classification Report",
                description="GOTTCHA2 classification report file"))
        setattr(cls, "GOTTCHA2 Report Full",
            PermissibleValue(
                text="GOTTCHA2 Report Full",
                description="GOTTCHA2 report file"))
        setattr(cls, "Kraken2 Krona Plot",
            PermissibleValue(
                text="Kraken2 Krona Plot",
                description="Kraken2 krona plot HTML file"))
        setattr(cls, "Centrifuge Krona Plot",
            PermissibleValue(
                text="Centrifuge Krona Plot",
                description="Centrifuge krona plot HTML file"))
        setattr(cls, "Centrifuge output report file",
            PermissibleValue(
                text="Centrifuge output report file",
                description="Centrifuge output report file"))
        setattr(cls, "Kraken2 Classification Report",
            PermissibleValue(
                text="Kraken2 Classification Report",
                description="Kraken2 output report file"))
        setattr(cls, "Kraken2 Taxonomic Classification",
            PermissibleValue(
                text="Kraken2 Taxonomic Classification",
                description="Kraken2 output read classification file"))
        setattr(cls, "Centrifuge Classification Report",
            PermissibleValue(
                text="Centrifuge Classification Report",
                description="Centrifuge output report file"))
        setattr(cls, "Centrifuge Taxonomic Classification",
            PermissibleValue(
                text="Centrifuge Taxonomic Classification",
                description="Centrifuge output read classification file"))
        setattr(cls, "Structural Annotation GFF",
            PermissibleValue(
                text="Structural Annotation GFF",
                description="GFF3 format file with structural annotations"))
        setattr(cls, "Structural Annotation Stats Json",
            PermissibleValue(
                text="Structural Annotation Stats Json",
                description="Structural annotations stats json"))
        setattr(cls, "Functional Annotation GFF",
            PermissibleValue(
                text="Functional Annotation GFF",
                description="GFF3 format file with functional annotations"))
        setattr(cls, "Annotation Info File",
            PermissibleValue(
                text="Annotation Info File",
                description="File containing annotation info"))
        setattr(cls, "Annotation Amino Acid FASTA",
            PermissibleValue(
                text="Annotation Amino Acid FASTA",
                description="FASTA amino acid file for annotated proteins"))
        setattr(cls, "Annotation Enzyme Commission",
            PermissibleValue(
                text="Annotation Enzyme Commission",
                description="Tab delimited file for EC annotation"))
        setattr(cls, "Annotation KEGG Orthology",
            PermissibleValue(
                text="Annotation KEGG Orthology",
                description="Tab delimited file for KO annotation"))
        setattr(cls, "Assembly Info File",
            PermissibleValue(
                text="Assembly Info File",
                description="File containing assembly info"))
        setattr(cls, "Assembly Coverage BAM",
            PermissibleValue(
                text="Assembly Coverage BAM",
                description="Sorted bam file of reads mapping back to the final assembly"))
        setattr(cls, "Assembly AGP",
            PermissibleValue(
                text="Assembly AGP",
                description="An AGP format file that describes the assembly"))
        setattr(cls, "Assembly Scaffolds",
            PermissibleValue(
                text="Assembly Scaffolds",
                description="Final assembly scaffolds fasta"))
        setattr(cls, "Assembly Contigs",
            PermissibleValue(
                text="Assembly Contigs",
                description="Final assembly contigs fasta"))
        setattr(cls, "Assembly Coverage Stats",
            PermissibleValue(
                text="Assembly Coverage Stats",
                description="Assembled contigs coverage information"))
        setattr(cls, "Contig Mapping File",
            PermissibleValue(
                text="Contig Mapping File",
                description="Contig mappings between contigs and scaffolds"))
        setattr(cls, "Error Corrected Reads",
            PermissibleValue(
                text="Error Corrected Reads",
                description="Error corrected reads fastq"))
        setattr(cls, "Filtered Sequencing Reads",
            PermissibleValue(
                text="Filtered Sequencing Reads",
                description="Reads QC result fastq (clean data)"))
        setattr(cls, "Read Filtering Info File",
            PermissibleValue(
                text="Read Filtering Info File",
                description="File containing read filtering information"))
        setattr(cls, "QC Statistics Extended",
            PermissibleValue(
                text="QC Statistics Extended",
                description="Extended report including methods and results for read filtering"))
        setattr(cls, "QC Statistics",
            PermissibleValue(
                text="QC Statistics",
                description="Reads QC summary statistics"))
        setattr(cls, "TIGRFam Annotation GFF",
            PermissibleValue(
                text="TIGRFam Annotation GFF",
                description="GFF3 format file with TIGRfam"))
        setattr(cls, "CRT Annotation GFF",
            PermissibleValue(
                text="CRT Annotation GFF",
                description="GFF3 format file with CRT"))
        setattr(cls, "Genemark Annotation GFF",
            PermissibleValue(
                text="Genemark Annotation GFF",
                description="GFF3 format file with Genemark"))
        setattr(cls, "Prodigal Annotation GFF",
            PermissibleValue(
                text="Prodigal Annotation GFF",
                description="GFF3 format file with Prodigal"))
        setattr(cls, "TRNA Annotation GFF",
            PermissibleValue(
                text="TRNA Annotation GFF",
                description="GFF3 format file with TRNA"))
        setattr(cls, "Misc Annotation GFF",
            PermissibleValue(
                text="Misc Annotation GFF",
                description="GFF3 format file with Misc"))
        setattr(cls, "RFAM Annotation GFF",
            PermissibleValue(
                text="RFAM Annotation GFF",
                description="GFF3 format file with RFAM"))
        setattr(cls, "TMRNA Annotation GFF",
            PermissibleValue(
                text="TMRNA Annotation GFF",
                description="GFF3 format file with TMRNA"))
        setattr(cls, "Crispr Terms",
            PermissibleValue(
                text="Crispr Terms",
                description="Crispr Terms"))
        setattr(cls, "Product Names",
            PermissibleValue(
                text="Product Names",
                description="Product names file"))
        setattr(cls, "Gene Phylogeny tsv",
            PermissibleValue(
                text="Gene Phylogeny tsv",
                description="Gene Phylogeny tsv"))
        setattr(cls, "Scaffold Lineage tsv",
            PermissibleValue(
                text="Scaffold Lineage tsv",
                description="phylogeny at the scaffold level"))
        setattr(cls, "Clusters of Orthologous Groups (COG) Annotation GFF",
            PermissibleValue(
                text="Clusters of Orthologous Groups (COG) Annotation GFF",
                description="GFF3 format file with COGs"))
        setattr(cls, "KO_EC Annotation GFF",
            PermissibleValue(
                text="KO_EC Annotation GFF",
                description="GFF3 format file with KO_EC"))
        setattr(cls, "CATH FunFams (Functional Families) Annotation GFF",
            PermissibleValue(
                text="CATH FunFams (Functional Families) Annotation GFF",
                description="GFF3 format file with CATH FunFams"))
        setattr(cls, "SUPERFam Annotation GFF",
            PermissibleValue(
                text="SUPERFam Annotation GFF",
                description="GFF3 format file with SUPERFam"))
        setattr(cls, "SMART Annotation GFF",
            PermissibleValue(
                text="SMART Annotation GFF",
                description="GFF3 format file with SMART"))
        setattr(cls, "Pfam Annotation GFF",
            PermissibleValue(
                text="Pfam Annotation GFF",
                description="GFF3 format file with Pfam"))
        setattr(cls, "Annotation Statistics",
            PermissibleValue(
                text="Annotation Statistics",
                description="Annotation statistics report"))
        setattr(cls, "Direct Infusion FT ICR-MS Raw Data",
            PermissibleValue(
                text="Direct Infusion FT ICR-MS Raw Data",
                description="""Direct infusion 21 Tesla Fourier Transform ion cyclotron resonance mass spectrometry raw data acquired in broadband full scan mode"""))
        setattr(cls, "LC-DDA-MS/MS Raw Data",
            PermissibleValue(
                text="LC-DDA-MS/MS Raw Data",
                description="Liquid chromatographically separated MS1 and Data-Dependent MS2 binary instrument file"))
        setattr(cls, "Configuration toml",
            PermissibleValue(
                text="Configuration toml",
                description="""A configuration toml file used by various programs to store settings that are specific to their respective software."""))
        setattr(cls, "LC-MS Lipidomics Results",
            PermissibleValue(
                text="LC-MS Lipidomics Results",
                description="LC-MS-based lipid assignment results table."))
        setattr(cls, "Contaminants Amino Acid FASTA",
            PermissibleValue(
                text="Contaminants Amino Acid FASTA",
                description="FASTA amino acid file for contaminant proteins commonly observed in proteomics data."))
        setattr(cls, "Analysis Tool Parameter File",
            PermissibleValue(
                text="Analysis Tool Parameter File",
                description="""A configuration file used by a single computational software tool that stores settings that are specific to that tool."""))
        setattr(cls, "Workflow Operation Summary",
            PermissibleValue(
                text="Workflow Operation Summary",
                description="""A human readable record of analysis steps applied during an instance of a workflow operation."""))

class DoiProviderEnum(EnumDefinitionImpl):

    emsl = PermissibleValue(
        text="emsl",
        meaning=None)
    jgi = PermissibleValue(
        text="jgi",
        meaning=None)
    kbase = PermissibleValue(
        text="kbase",
        meaning=None)
    osti = PermissibleValue(
        text="osti",
        meaning=None)
    ess_dive = PermissibleValue(
        text="ess_dive",
        meaning=None)
    massive = PermissibleValue(text="massive")
    gsc = PermissibleValue(text="gsc")
    zenodo = PermissibleValue(text="zenodo")
    edi = PermissibleValue(
        text="edi",
        meaning=None)

    _defn = EnumDefinition(
        name="DoiProviderEnum",
    )

class DoiCategoryEnum(EnumDefinitionImpl):

    award_doi = PermissibleValue(
        text="award_doi",
        description="A type of DOI that resolves to a funding authority.")
    dataset_doi = PermissibleValue(
        text="dataset_doi",
        description="A type of DOI that resolves to generated data.")
    publication_doi = PermissibleValue(
        text="publication_doi",
        description="A type of DOI that resolves to a publication.")
    data_management_plan_doi = PermissibleValue(
        text="data_management_plan_doi",
        description="A type of DOI that resolves to a data management plan.")

    _defn = EnumDefinition(
        name="DoiCategoryEnum",
    )

class StatusEnum(EnumDefinitionImpl):

    fail = PermissibleValue(text="fail")

    _defn = EnumDefinition(
        name="StatusEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "pass",
            PermissibleValue(text="pass"))

class AnalyteCategoryEnum(EnumDefinitionImpl):

    metagenome = PermissibleValue(text="metagenome")
    metatranscriptome = PermissibleValue(text="metatranscriptome")
    metaproteome = PermissibleValue(text="metaproteome")
    metabolome = PermissibleValue(text="metabolome")
    lipidome = PermissibleValue(text="lipidome")
    nom = PermissibleValue(text="nom")

    _defn = EnumDefinition(
        name="AnalyteCategoryEnum",
    )

class DirectInfusionEnum(EnumDefinitionImpl):

    direct_infusion = PermissibleValue(text="direct_infusion")
    autosampler = PermissibleValue(text="autosampler")

    _defn = EnumDefinition(
        name="DirectInfusionEnum",
    )

class ExtractionTargetEnum(EnumDefinitionImpl):

    DNA = PermissibleValue(text="DNA")
    RNA = PermissibleValue(text="RNA")
    metabolite = PermissibleValue(text="metabolite")
    protein = PermissibleValue(text="protein")
    lipid = PermissibleValue(text="lipid")

    _defn = EnumDefinition(
        name="ExtractionTargetEnum",
    )

class ProcessingInstitutionEnum(EnumDefinitionImpl):

    UCSD = PermissibleValue(
        text="UCSD",
        meaning=None)
    JGI = PermissibleValue(
        text="JGI",
        meaning=None)
    EMSL = PermissibleValue(
        text="EMSL",
        meaning=None)
    Battelle = PermissibleValue(
        text="Battelle",
        meaning=None)
    ANL = PermissibleValue(
        text="ANL",
        meaning=None)
    UCD_Genome_Center = PermissibleValue(
        text="UCD_Genome_Center",
        meaning=None)

    _defn = EnumDefinition(
        name="ProcessingInstitutionEnum",
    )

class DataCategoryEnum(EnumDefinitionImpl):

    instrument_data = PermissibleValue(
        text="instrument_data",
        description="Data generated by a DataGeneration PlannedProcess")
    processed_data = PermissibleValue(
        text="processed_data",
        description="Data generated by a WorkflowExecution PlannedProcess")
    workflow_parameter_data = PermissibleValue(
        text="workflow_parameter_data",
        description="Data used as input into a workflow providing workflow specification.")

    _defn = EnumDefinition(
        name="DataCategoryEnum",
    )

class SampleTypeEnum(EnumDefinitionImpl):

    soil = PermissibleValue(text="soil")
    sediment = PermissibleValue(text="sediment")
    water = PermissibleValue(text="water")

    _defn = EnumDefinition(
        name="SampleTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "soil - water extract",
            PermissibleValue(text="soil - water extract"))
        setattr(cls, "plant associated",
            PermissibleValue(text="plant associated"))

class DNASampleFormatEnum(EnumDefinitionImpl):

    DNAStable = PermissibleValue(text="DNAStable")
    Ethanol = PermissibleValue(text="Ethanol")
    PBS = PermissibleValue(text="PBS")
    Pellet = PermissibleValue(text="Pellet")
    RNAStable = PermissibleValue(text="RNAStable")
    TE = PermissibleValue(text="TE")
    Water = PermissibleValue(text="Water")

    _defn = EnumDefinition(
        name="DNASampleFormatEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "10 mM Tris-HCl",
            PermissibleValue(text="10 mM Tris-HCl"))
        setattr(cls, "Low EDTA TE",
            PermissibleValue(text="Low EDTA TE"))
        setattr(cls, "MDA reaction buffer",
            PermissibleValue(text="MDA reaction buffer"))
        setattr(cls, "Gentegra-DNA",
            PermissibleValue(text="Gentegra-DNA"))
        setattr(cls, "Gentegra-RNA",
            PermissibleValue(text="Gentegra-RNA"))

class JgiContTypeEnum(EnumDefinitionImpl):

    plate = PermissibleValue(text="plate")
    tube = PermissibleValue(text="tube")

    _defn = EnumDefinition(
        name="JgiContTypeEnum",
    )

class YesNoEnum(EnumDefinitionImpl):
    """
    replaces DnaDnaseEnum and DnaseRnaEnum
    """
    no = PermissibleValue(text="no")
    yes = PermissibleValue(text="yes")

    _defn = EnumDefinition(
        name="YesNoEnum",
        description="replaces DnaDnaseEnum and DnaseRnaEnum",
    )

class RNASampleFormatEnum(EnumDefinitionImpl):

    DNAStable = PermissibleValue(text="DNAStable")
    Ethanol = PermissibleValue(text="Ethanol")
    PBS = PermissibleValue(text="PBS")
    Pellet = PermissibleValue(text="Pellet")
    RNAStable = PermissibleValue(text="RNAStable")
    TE = PermissibleValue(text="TE")
    Water = PermissibleValue(text="Water")

    _defn = EnumDefinition(
        name="RNASampleFormatEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "10 mM Tris-HCl",
            PermissibleValue(text="10 mM Tris-HCl"))
        setattr(cls, "Low EDTA TE",
            PermissibleValue(text="Low EDTA TE"))
        setattr(cls, "MDA reaction buffer",
            PermissibleValue(text="MDA reaction buffer"))
        setattr(cls, "Gentegra-DNA",
            PermissibleValue(text="Gentegra-DNA"))
        setattr(cls, "Gentegra-RNA",
            PermissibleValue(text="Gentegra-RNA"))

class AnalysisTypeEnum(EnumDefinitionImpl):

    metabolomics = PermissibleValue(text="metabolomics")
    metagenomics = PermissibleValue(
        text="metagenomics",
        description="Standard short-read metagenomic sequencing")
    metagenomics_long_read = PermissibleValue(
        text="metagenomics_long_read",
        description="Long-read metagenomic sequencing")
    metaproteomics = PermissibleValue(text="metaproteomics")
    metatranscriptomics = PermissibleValue(text="metatranscriptomics")

    _defn = EnumDefinition(
        name="AnalysisTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "natural organic matter",
            PermissibleValue(text="natural organic matter"))

class CalibrationTargetEnum(EnumDefinitionImpl):

    mass = PermissibleValue(text="mass")
    retention_time = PermissibleValue(text="retention_time")
    retention_index = PermissibleValue(text="retention_index")

    _defn = EnumDefinition(
        name="CalibrationTargetEnum",
    )

class CalibrationStandardEnum(EnumDefinitionImpl):

    fames = PermissibleValue(text="fames")
    alkanes = PermissibleValue(text="alkanes")

    _defn = EnumDefinition(
        name="CalibrationStandardEnum",
    )

# Slots
class slots:
    pass

slots.polarity_mode = Slot(uri=NMDC.polarity_mode, name="polarity_mode", curie=NMDC.curie('polarity_mode'),
                   model_uri=NMDC.polarity_mode, domain=None, range=Optional[Union[str, "PolarityModeEnum"]])

slots.mass_spectrum_collection_modes = Slot(uri=NMDC.mass_spectrum_collection_modes, name="mass_spectrum_collection_modes", curie=NMDC.curie('mass_spectrum_collection_modes'),
                   model_uri=NMDC.mass_spectrum_collection_modes, domain=None, range=Optional[Union[Union[str, "MassSpectrumCollectionModeEnum"], List[Union[str, "MassSpectrumCollectionModeEnum"]]]])

slots.ionization_source = Slot(uri=NMDC.ionization_source, name="ionization_source", curie=NMDC.curie('ionization_source'),
                   model_uri=NMDC.ionization_source, domain=None, range=Optional[Union[str, "IonizationSourceEnum"]])

slots.mass_analyzers = Slot(uri=NMDC.mass_analyzers, name="mass_analyzers", curie=NMDC.curie('mass_analyzers'),
                   model_uri=NMDC.mass_analyzers, domain=None, range=Optional[Union[Union[str, "MassAnalyzerEnum"], List[Union[str, "MassAnalyzerEnum"]]]])

slots.resolution_categories = Slot(uri=NMDC.resolution_categories, name="resolution_categories", curie=NMDC.curie('resolution_categories'),
                   model_uri=NMDC.resolution_categories, domain=None, range=Optional[Union[Union[str, "ResolutionCategoryEnum"], List[Union[str, "ResolutionCategoryEnum"]]]])

slots.mass_spectrometry_acquisition_strategy = Slot(uri=NMDC.mass_spectrometry_acquisition_strategy, name="mass_spectrometry_acquisition_strategy", curie=NMDC.curie('mass_spectrometry_acquisition_strategy'),
                   model_uri=NMDC.mass_spectrometry_acquisition_strategy, domain=None, range=Optional[Union[str, "MassSpectrometryAcquisitionStrategyEnum"]])

slots.eluent_introduction_category = Slot(uri=NMDC.eluent_introduction_category, name="eluent_introduction_category", curie=NMDC.curie('eluent_introduction_category'),
                   model_uri=NMDC.eluent_introduction_category, domain=None, range=Optional[Union[str, "EluentIntroductionCategoryEnum"]])

slots.has_mass_spectrometry_configuration = Slot(uri=NMDC.has_mass_spectrometry_configuration, name="has_mass_spectrometry_configuration", curie=NMDC.curie('has_mass_spectrometry_configuration'),
                   model_uri=NMDC.has_mass_spectrometry_configuration, domain=None, range=Optional[Union[str, MassSpectrometryConfigurationId]])

slots.has_chromatography_configuration = Slot(uri=NMDC.has_chromatography_configuration, name="has_chromatography_configuration", curie=NMDC.curie('has_chromatography_configuration'),
                   model_uri=NMDC.has_chromatography_configuration, domain=None, range=Optional[Union[str, ChromatographyConfigurationId]])

slots.metagenome_annotation_id = Slot(uri=NMDC.metagenome_annotation_id, name="metagenome_annotation_id", curie=NMDC.curie('metagenome_annotation_id'),
                   model_uri=NMDC.metagenome_annotation_id, domain=None, range=Union[str, WorkflowExecutionId])

slots.gene_function_id = Slot(uri=NMDC.gene_function_id, name="gene_function_id", curie=NMDC.curie('gene_function_id'),
                   model_uri=NMDC.gene_function_id, domain=None, range=Union[str, URIorCURIE])

slots.count = Slot(uri=NMDC.count, name="count", curie=NMDC.curie('count'),
                   model_uri=NMDC.count, domain=None, range=int)

slots.functional_annotation_agg = Slot(uri=NMDC.functional_annotation_agg, name="functional_annotation_agg", curie=NMDC.curie('functional_annotation_agg'),
                   model_uri=NMDC.functional_annotation_agg, domain=None, range=Optional[Union[Union[dict, FunctionalAnnotationAggMember], List[Union[dict, FunctionalAnnotationAggMember]]]])

slots.ecosystem_path_id = Slot(uri=NMDC.ecosystem_path_id, name="ecosystem_path_id", curie=NMDC.curie('ecosystem_path_id'),
                   model_uri=NMDC.ecosystem_path_id, domain=None, range=Optional[str])

slots.sample_collection_year = Slot(uri=NMDC.sample_collection_year, name="sample_collection_year", curie=NMDC.curie('sample_collection_year'),
                   model_uri=NMDC.sample_collection_year, domain=None, range=Optional[int])

slots.sample_collection_month = Slot(uri=NMDC.sample_collection_month, name="sample_collection_month", curie=NMDC.curie('sample_collection_month'),
                   model_uri=NMDC.sample_collection_month, domain=None, range=Optional[str])

slots.library_preparation_kit = Slot(uri=NMDC.library_preparation_kit, name="library_preparation_kit", curie=NMDC.curie('library_preparation_kit'),
                   model_uri=NMDC.library_preparation_kit, domain=None, range=Optional[str])

slots.pcr_cycles = Slot(uri=NMDC.pcr_cycles, name="pcr_cycles", curie=NMDC.curie('pcr_cycles'),
                   model_uri=NMDC.pcr_cycles, domain=None, range=Optional[int])

slots.input_mass = Slot(uri=NMDC.input_mass, name="input_mass", curie=NMDC.curie('input_mass'),
                   model_uri=NMDC.input_mass, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.library_type = Slot(uri=NMDC.library_type, name="library_type", curie=NMDC.curie('library_type'),
                   model_uri=NMDC.library_type, domain=None, range=Optional[Union[str, "LibraryTypeEnum"]])

slots.date_created = Slot(uri=NMDC.date_created, name="date_created", curie=NMDC.curie('date_created'),
                   model_uri=NMDC.date_created, domain=None, range=Optional[str])

slots.etl_software_version = Slot(uri=NMDC.etl_software_version, name="etl_software_version", curie=NMDC.curie('etl_software_version'),
                   model_uri=NMDC.etl_software_version, domain=None, range=Optional[str])

slots.object_set = Slot(uri=NMDC.object_set, name="object_set", curie=NMDC.curie('object_set'),
                   model_uri=NMDC.object_set, domain=None, range=Optional[Union[str, List[str]]])

slots.chemical_entity_set = Slot(uri=NMDC.chemical_entity_set, name="chemical_entity_set", curie=NMDC.curie('chemical_entity_set'),
                   model_uri=NMDC.chemical_entity_set, domain=None, range=Optional[Union[Dict[Union[str, ChemicalEntityId], Union[dict, ChemicalEntity]], List[Union[dict, ChemicalEntity]]]])

slots.biosample_set = Slot(uri=NMDC.biosample_set, name="biosample_set", curie=NMDC.curie('biosample_set'),
                   model_uri=NMDC.biosample_set, domain=None, range=Optional[Union[Dict[Union[str, BiosampleId], Union[dict, Biosample]], List[Union[dict, Biosample]]]])

slots.study_set = Slot(uri=NMDC.study_set, name="study_set", curie=NMDC.curie('study_set'),
                   model_uri=NMDC.study_set, domain=None, range=Optional[Union[Dict[Union[str, StudyId], Union[dict, Study]], List[Union[dict, Study]]]])

slots.field_research_site_set = Slot(uri=NMDC.field_research_site_set, name="field_research_site_set", curie=NMDC.curie('field_research_site_set'),
                   model_uri=NMDC.field_research_site_set, domain=None, range=Optional[Union[Dict[Union[str, FieldResearchSiteId], Union[dict, FieldResearchSite]], List[Union[dict, FieldResearchSite]]]])

slots.collecting_biosamples_from_site_set = Slot(uri=NMDC.collecting_biosamples_from_site_set, name="collecting_biosamples_from_site_set", curie=NMDC.curie('collecting_biosamples_from_site_set'),
                   model_uri=NMDC.collecting_biosamples_from_site_set, domain=None, range=Optional[Union[Dict[Union[str, CollectingBiosamplesFromSiteId], Union[dict, CollectingBiosamplesFromSite]], List[Union[dict, CollectingBiosamplesFromSite]]]])

slots.data_object_set = Slot(uri=NMDC.data_object_set, name="data_object_set", curie=NMDC.curie('data_object_set'),
                   model_uri=NMDC.data_object_set, domain=None, range=Optional[Union[Dict[Union[str, DataObjectId], Union[dict, DataObject]], List[Union[dict, DataObject]]]])

slots.genome_feature_set = Slot(uri=NMDC.genome_feature_set, name="genome_feature_set", curie=NMDC.curie('genome_feature_set'),
                   model_uri=NMDC.genome_feature_set, domain=None, range=Optional[Union[Union[dict, GenomeFeature], List[Union[dict, GenomeFeature]]]])

slots.functional_annotation_set = Slot(uri=NMDC.functional_annotation_set, name="functional_annotation_set", curie=NMDC.curie('functional_annotation_set'),
                   model_uri=NMDC.functional_annotation_set, domain=None, range=Optional[Union[Union[dict, FunctionalAnnotation], List[Union[dict, FunctionalAnnotation]]]])

slots.workflow_execution_set = Slot(uri=NMDC.workflow_execution_set, name="workflow_execution_set", curie=NMDC.curie('workflow_execution_set'),
                   model_uri=NMDC.workflow_execution_set, domain=None, range=Optional[Union[Dict[Union[str, WorkflowExecutionId], Union[dict, WorkflowExecution]], List[Union[dict, WorkflowExecution]]]])

slots.data_generation_set = Slot(uri=NMDC.data_generation_set, name="data_generation_set", curie=NMDC.curie('data_generation_set'),
                   model_uri=NMDC.data_generation_set, domain=None, range=Optional[Union[Dict[Union[str, DataGenerationId], Union[dict, DataGeneration]], List[Union[dict, DataGeneration]]]])

slots.processed_sample_set = Slot(uri=NMDC.processed_sample_set, name="processed_sample_set", curie=NMDC.curie('processed_sample_set'),
                   model_uri=NMDC.processed_sample_set, domain=None, range=Optional[Union[Dict[Union[str, ProcessedSampleId], Union[dict, ProcessedSample]], List[Union[dict, ProcessedSample]]]])

slots.instrument_set = Slot(uri=NMDC.instrument_set, name="instrument_set", curie=NMDC.curie('instrument_set'),
                   model_uri=NMDC.instrument_set, domain=None, range=Optional[Union[Dict[Union[str, InstrumentId], Union[dict, Instrument]], List[Union[dict, Instrument]]]])

slots.calibration_set = Slot(uri=NMDC.calibration_set, name="calibration_set", curie=NMDC.curie('calibration_set'),
                   model_uri=NMDC.calibration_set, domain=None, range=Optional[Union[Dict[Union[str, CalibrationInformationId], Union[dict, CalibrationInformation]], List[Union[dict, CalibrationInformation]]]])

slots.configuration_set = Slot(uri=NMDC.configuration_set, name="configuration_set", curie=NMDC.curie('configuration_set'),
                   model_uri=NMDC.configuration_set, domain=None, range=Optional[Union[Dict[Union[str, ConfigurationId], Union[dict, Configuration]], List[Union[dict, Configuration]]]])

slots.protocol_execution_set = Slot(uri=NMDC.protocol_execution_set, name="protocol_execution_set", curie=NMDC.curie('protocol_execution_set'),
                   model_uri=NMDC.protocol_execution_set, domain=None, range=Optional[Union[Dict[Union[str, ProtocolExecutionId], Union[dict, ProtocolExecution]], List[Union[dict, ProtocolExecution]]]])

slots.storage_process_set = Slot(uri=NMDC.storage_process_set, name="storage_process_set", curie=NMDC.curie('storage_process_set'),
                   model_uri=NMDC.storage_process_set, domain=None, range=Optional[Union[Dict[Union[str, StorageProcessId], Union[dict, StorageProcess]], List[Union[dict, StorageProcess]]]])

slots.material_processing_set = Slot(uri=NMDC.material_processing_set, name="material_processing_set", curie=NMDC.curie('material_processing_set'),
                   model_uri=NMDC.material_processing_set, domain=None, range=Optional[Union[Dict[Union[str, MaterialProcessingId], Union[dict, MaterialProcessing]], List[Union[dict, MaterialProcessing]]]])

slots.sample_collection_day = Slot(uri=NMDC.sample_collection_day, name="sample_collection_day", curie=NMDC.curie('sample_collection_day'),
                   model_uri=NMDC.sample_collection_day, domain=None, range=Optional[int])

slots.sample_collection_hour = Slot(uri=NMDC.sample_collection_hour, name="sample_collection_hour", curie=NMDC.curie('sample_collection_hour'),
                   model_uri=NMDC.sample_collection_hour, domain=None, range=Optional[int])

slots.sample_collection_minute = Slot(uri=NMDC.sample_collection_minute, name="sample_collection_minute", curie=NMDC.curie('sample_collection_minute'),
                   model_uri=NMDC.sample_collection_minute, domain=None, range=Optional[int])

slots.biogas_temperature = Slot(uri=NMDC.biogas_temperature, name="biogas_temperature", curie=NMDC.curie('biogas_temperature'),
                   model_uri=NMDC.biogas_temperature, domain=None, range=Optional[str])

slots.soil_annual_season_temp = Slot(uri=NMDC.soil_annual_season_temp, name="soil_annual_season_temp", curie=NMDC.curie('soil_annual_season_temp'),
                   model_uri=NMDC.soil_annual_season_temp, domain=None, range=Optional[str])

slots.biogas_retention_time = Slot(uri=NMDC.biogas_retention_time, name="biogas_retention_time", curie=NMDC.curie('biogas_retention_time'),
                   model_uri=NMDC.biogas_retention_time, domain=None, range=Optional[str])

slots.completion_date = Slot(uri=NMDC.completion_date, name="completion_date", curie=NMDC.curie('completion_date'),
                   model_uri=NMDC.completion_date, domain=None, range=Optional[str])

slots.container_size = Slot(uri=NMDC.container_size, name="container_size", curie=NMDC.curie('container_size'),
                   model_uri=NMDC.container_size, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.protocol_execution_category = Slot(uri=NMDC.protocol_execution_category, name="protocol_execution_category", curie=NMDC.curie('protocol_execution_category'),
                   model_uri=NMDC.protocol_execution_category, domain=None, range=Union[str, "ProtocolCategoryEnum"])

slots.has_process_parts = Slot(uri=NMDC.has_process_parts, name="has_process_parts", curie=NMDC.curie('has_process_parts'),
                   model_uri=NMDC.has_process_parts, domain=None, range=Union[Union[str, PlannedProcessId], List[Union[str, PlannedProcessId]]])

slots.filter_material = Slot(uri=NMDC.filter_material, name="filter_material", curie=NMDC.curie('filter_material'),
                   model_uri=NMDC.filter_material, domain=None, range=Optional[str])

slots.filter_pore_size = Slot(uri=NMDC.filter_pore_size, name="filter_pore_size", curie=NMDC.curie('filter_pore_size'),
                   model_uri=NMDC.filter_pore_size, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.conditionings = Slot(uri=NMDC.conditionings, name="conditionings", curie=NMDC.curie('conditionings'),
                   model_uri=NMDC.conditionings, domain=None, range=Optional[Union[str, List[str]]])

slots.separation_method = Slot(uri=NMDC.separation_method, name="separation_method", curie=NMDC.curie('separation_method'),
                   model_uri=NMDC.separation_method, domain=None, range=Optional[Union[str, "SeparationMethodEnum"]])

slots.filtration_category = Slot(uri=NMDC.filtration_category, name="filtration_category", curie=NMDC.curie('filtration_category'),
                   model_uri=NMDC.filtration_category, domain=None, range=Optional[str])

slots.material_component_separation = Slot(uri=NMDC.material_component_separation, name="material_component_separation", curie=NMDC.curie('material_component_separation'),
                   model_uri=NMDC.material_component_separation, domain=None, range=Optional[str])

slots.value = Slot(uri=NMDC.value, name="value", curie=NMDC.curie('value'),
                   model_uri=NMDC.value, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.modifier_substance = Slot(uri=NMDC.modifier_substance, name="modifier_substance", curie=NMDC.curie('modifier_substance'),
                   model_uri=NMDC.modifier_substance, domain=None, range=Optional[str])

slots.is_pressurized = Slot(uri=NMDC.is_pressurized, name="is_pressurized", curie=NMDC.curie('is_pressurized'),
                   model_uri=NMDC.is_pressurized, domain=None, range=Optional[Union[bool, Bool]])

slots.contained_in = Slot(uri=NMDC.contained_in, name="contained_in", curie=NMDC.curie('contained_in'),
                   model_uri=NMDC.contained_in, domain=None, range=Optional[Union[str, "ContainerCategoryEnum"]])

slots.input_volume = Slot(uri=NMDC.input_volume, name="input_volume", curie=NMDC.curie('input_volume'),
                   model_uri=NMDC.input_volume, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.ordered_mobile_phases = Slot(uri=NMDC.ordered_mobile_phases, name="ordered_mobile_phases", curie=NMDC.curie('ordered_mobile_phases'),
                   model_uri=NMDC.ordered_mobile_phases, domain=None, range=Optional[Union[Union[dict, MobilePhaseSegment], List[Union[dict, MobilePhaseSegment]]]])

slots.stationary_phase = Slot(uri=NMDC.stationary_phase, name="stationary_phase", curie=NMDC.curie('stationary_phase'),
                   model_uri=NMDC.stationary_phase, domain=None, range=Optional[Union[str, "StationaryPhaseEnum"]])

slots.chromatographic_category = Slot(uri=NMDC.chromatographic_category, name="chromatographic_category", curie=NMDC.curie('chromatographic_category'),
                   model_uri=NMDC.chromatographic_category, domain=None, range=Optional[Union[str, "ChromatographicCategoryEnum"]])

slots.sampled_portion = Slot(uri=NMDC.sampled_portion, name="sampled_portion", curie=NMDC.curie('sampled_portion'),
                   model_uri=NMDC.sampled_portion, domain=None, range=Optional[Union[Union[str, "SamplePortionEnum"], List[Union[str, "SamplePortionEnum"]]]])

slots.chemical_conversion_category = Slot(uri=NMDC.chemical_conversion_category, name="chemical_conversion_category", curie=NMDC.curie('chemical_conversion_category'),
                   model_uri=NMDC.chemical_conversion_category, domain=None, range=Optional[Union[str, "ChemicalConversionCategoryEnum"]])

slots.substances_volume = Slot(uri=NMDC.substances_volume, name="substances_volume", curie=NMDC.curie('substances_volume'),
                   model_uri=NMDC.substances_volume, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.biosample_categories = Slot(uri=NMDC.biosample_categories, name="biosample_categories", curie=NMDC.curie('biosample_categories'),
                   model_uri=NMDC.biosample_categories, domain=None, range=Optional[Union[Union[str, "BiosampleCategoryEnum"], List[Union[str, "BiosampleCategoryEnum"]]]])

slots.collected_from = Slot(uri=NMDC.collected_from, name="collected_from", curie=NMDC.curie('collected_from'),
                   model_uri=NMDC.collected_from, domain=None, range=Optional[Union[str, FieldResearchSiteId]])

slots.bulk_elect_conductivity = Slot(uri=NMDC.bulk_elect_conductivity, name="bulk_elect_conductivity", curie=NMDC.curie('bulk_elect_conductivity'),
                   model_uri=NMDC.bulk_elect_conductivity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.subsurface_depth = Slot(uri=NMDC.subsurface_depth, name="subsurface_depth", curie=NMDC.curie('subsurface_depth'),
                   model_uri=NMDC.subsurface_depth, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.env_package = Slot(uri=NMDC.env_package, name="env_package", curie=NMDC.curie('env_package'),
                   model_uri=NMDC.env_package, domain=None, range=Optional[Union[dict, TextValue]])

slots.zinc = Slot(uri=NMDC.zinc, name="zinc", curie=NMDC.curie('zinc'),
                   model_uri=NMDC.zinc, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.manganese = Slot(uri=NMDC.manganese, name="manganese", curie=NMDC.curie('manganese'),
                   model_uri=NMDC.manganese, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.ammonium_nitrogen = Slot(uri=NMDC.ammonium_nitrogen, name="ammonium_nitrogen", curie=NMDC.curie('ammonium_nitrogen'),
                   model_uri=NMDC.ammonium_nitrogen, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.nitrate_nitrogen = Slot(uri=NMDC.nitrate_nitrogen, name="nitrate_nitrogen", curie=NMDC.curie('nitrate_nitrogen'),
                   model_uri=NMDC.nitrate_nitrogen, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.nitrite_nitrogen = Slot(uri=NMDC.nitrite_nitrogen, name="nitrite_nitrogen", curie=NMDC.curie('nitrite_nitrogen'),
                   model_uri=NMDC.nitrite_nitrogen, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.lbc_thirty = Slot(uri=NMDC.lbc_thirty, name="lbc_thirty", curie=NMDC.curie('lbc_thirty'),
                   model_uri=NMDC.lbc_thirty, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.lbceq = Slot(uri=NMDC.lbceq, name="lbceq", curie=NMDC.curie('lbceq'),
                   model_uri=NMDC.lbceq, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.dna_absorb1 = Slot(uri=NMDC.dna_absorb1, name="dna_absorb1", curie=NMDC.curie('dna_absorb1'),
                   model_uri=NMDC.dna_absorb1, domain=None, range=Optional[float])

slots.dna_absorb2 = Slot(uri=NMDC.dna_absorb2, name="dna_absorb2", curie=NMDC.curie('dna_absorb2'),
                   model_uri=NMDC.dna_absorb2, domain=None, range=Optional[float])

slots.mass = Slot(uri=NMDC.mass, name="mass", curie=NMDC.curie('mass'),
                   model_uri=NMDC.mass, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.substances_used = Slot(uri=NMDC.substances_used, name="substances_used", curie=NMDC.curie('substances_used'),
                   model_uri=NMDC.substances_used, domain=None, range=Optional[Union[Union[dict, PortionOfSubstance], List[Union[dict, PortionOfSubstance]]]])

slots.known_as = Slot(uri=NMDC.known_as, name="known_as", curie=NMDC.curie('known_as'),
                   model_uri=NMDC.known_as, domain=None, range=Optional[Union[str, ChemicalEntityId]])

slots.substance_role = Slot(uri=NMDC.substance_role, name="substance_role", curie=NMDC.curie('substance_role'),
                   model_uri=NMDC.substance_role, domain=None, range=Optional[Union[str, "SubstanceRoleEnum"]])

slots.concentration = Slot(uri=NMDC.concentration, name="concentration", curie=NMDC.curie('concentration'),
                   model_uri=NMDC.concentration, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.source_concentration = Slot(uri=NMDC.source_concentration, name="source_concentration", curie=NMDC.curie('source_concentration'),
                   model_uri=NMDC.source_concentration, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.final_concentration = Slot(uri=NMDC.final_concentration, name="final_concentration", curie=NMDC.curie('final_concentration'),
                   model_uri=NMDC.final_concentration, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.duration = Slot(uri=NMDC.duration, name="duration", curie=NMDC.curie('duration'),
                   model_uri=NMDC.duration, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.temperature = Slot(uri=NMDC.temperature, name="temperature", curie=NMDC.curie('temperature'),
                   model_uri=NMDC.temperature, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.total_bases = Slot(uri=NMDC.total_bases, name="total_bases", curie=NMDC.curie('total_bases'),
                   model_uri=NMDC.total_bases, domain=None, range=Optional[int])

slots.members_id = Slot(uri=NMDC.members_id, name="members_id", curie=NMDC.curie('members_id'),
                   model_uri=NMDC.members_id, domain=None, range=Optional[str])

slots.bin_name = Slot(uri=NMDC.bin_name, name="bin_name", curie=NMDC.curie('bin_name'),
                   model_uri=NMDC.bin_name, domain=None, range=Optional[str])

slots.number_of_contig = Slot(uri=NMDC.number_of_contig, name="number_of_contig", curie=NMDC.curie('number_of_contig'),
                   model_uri=NMDC.number_of_contig, domain=None, range=Optional[int])

slots.completeness = Slot(uri=NMDC.completeness, name="completeness", curie=NMDC.curie('completeness'),
                   model_uri=NMDC.completeness, domain=None, range=Optional[float])

slots.contamination = Slot(uri=NMDC.contamination, name="contamination", curie=NMDC.curie('contamination'),
                   model_uri=NMDC.contamination, domain=None, range=Optional[float])

slots.gene_count = Slot(uri=NMDC.gene_count, name="gene_count", curie=NMDC.curie('gene_count'),
                   model_uri=NMDC.gene_count, domain=None, range=Optional[int])

slots.bin_quality = Slot(uri=NMDC.bin_quality, name="bin_quality", curie=NMDC.curie('bin_quality'),
                   model_uri=NMDC.bin_quality, domain=None, range=Optional[str])

slots.num_16s = Slot(uri=NMDC.num_16s, name="num_16s", curie=NMDC.curie('num_16s'),
                   model_uri=NMDC.num_16s, domain=None, range=Optional[int])

slots.num_5s = Slot(uri=NMDC.num_5s, name="num_5s", curie=NMDC.curie('num_5s'),
                   model_uri=NMDC.num_5s, domain=None, range=Optional[int])

slots.num_23s = Slot(uri=NMDC.num_23s, name="num_23s", curie=NMDC.curie('num_23s'),
                   model_uri=NMDC.num_23s, domain=None, range=Optional[int])

slots.num_t_rna = Slot(uri=NMDC.num_t_rna, name="num_t_rna", curie=NMDC.curie('num_t_rna'),
                   model_uri=NMDC.num_t_rna, domain=None, range=Optional[int])

slots.gtdbtk_domain = Slot(uri=NMDC.gtdbtk_domain, name="gtdbtk_domain", curie=NMDC.curie('gtdbtk_domain'),
                   model_uri=NMDC.gtdbtk_domain, domain=None, range=Optional[str])

slots.gtdbtk_phylum = Slot(uri=NMDC.gtdbtk_phylum, name="gtdbtk_phylum", curie=NMDC.curie('gtdbtk_phylum'),
                   model_uri=NMDC.gtdbtk_phylum, domain=None, range=Optional[str])

slots.gtdbtk_class = Slot(uri=NMDC.gtdbtk_class, name="gtdbtk_class", curie=NMDC.curie('gtdbtk_class'),
                   model_uri=NMDC.gtdbtk_class, domain=None, range=Optional[str])

slots.gtdbtk_order = Slot(uri=NMDC.gtdbtk_order, name="gtdbtk_order", curie=NMDC.curie('gtdbtk_order'),
                   model_uri=NMDC.gtdbtk_order, domain=None, range=Optional[str])

slots.gtdbtk_family = Slot(uri=NMDC.gtdbtk_family, name="gtdbtk_family", curie=NMDC.curie('gtdbtk_family'),
                   model_uri=NMDC.gtdbtk_family, domain=None, range=Optional[str])

slots.gtdbtk_genus = Slot(uri=NMDC.gtdbtk_genus, name="gtdbtk_genus", curie=NMDC.curie('gtdbtk_genus'),
                   model_uri=NMDC.gtdbtk_genus, domain=None, range=Optional[str])

slots.gtdbtk_species = Slot(uri=NMDC.gtdbtk_species, name="gtdbtk_species", curie=NMDC.curie('gtdbtk_species'),
                   model_uri=NMDC.gtdbtk_species, domain=None, range=Optional[str])

slots.highest_similarity_score = Slot(uri=NMDC.highest_similarity_score, name="highest_similarity_score", curie=NMDC.curie('highest_similarity_score'),
                   model_uri=NMDC.highest_similarity_score, domain=None, range=Optional[float])

slots.metabolite_identified = Slot(uri=NMDC.metabolite_identified, name="metabolite_identified", curie=NMDC.curie('metabolite_identified'),
                   model_uri=NMDC.metabolite_identified, domain=None, range=Optional[Union[str, ChemicalEntityId]])

slots.all_proteins = Slot(uri=NMDC.all_proteins, name="all_proteins", curie=NMDC.curie('all_proteins'),
                   model_uri=NMDC.all_proteins, domain=None, range=Optional[Union[Union[str, GeneProductId], List[Union[str, GeneProductId]]]])

slots.best_protein = Slot(uri=NMDC.best_protein, name="best_protein", curie=NMDC.curie('best_protein'),
                   model_uri=NMDC.best_protein, domain=None, range=Optional[Union[str, GeneProductId]])

slots.min_q_value = Slot(uri=NMDC.min_q_value, name="min_q_value", curie=NMDC.curie('min_q_value'),
                   model_uri=NMDC.min_q_value, domain=None, range=Optional[float])

slots.peptide_sequence = Slot(uri=NMDC.peptide_sequence, name="peptide_sequence", curie=NMDC.curie('peptide_sequence'),
                   model_uri=NMDC.peptide_sequence, domain=None, range=Optional[str])

slots.peptide_spectral_count = Slot(uri=NMDC.peptide_spectral_count, name="peptide_spectral_count", curie=NMDC.curie('peptide_spectral_count'),
                   model_uri=NMDC.peptide_spectral_count, domain=None, range=Optional[int])

slots.peptide_sum_masic_abundance = Slot(uri=NMDC.peptide_sum_masic_abundance, name="peptide_sum_masic_abundance", curie=NMDC.curie('peptide_sum_masic_abundance'),
                   model_uri=NMDC.peptide_sum_masic_abundance, domain=None, range=Optional[int])

slots.chemical_formula = Slot(uri=NMDC.chemical_formula, name="chemical_formula", curie=NMDC.curie('chemical_formula'),
                   model_uri=NMDC.chemical_formula, domain=None, range=Optional[str])

slots.inchi_key = Slot(uri=NMDC.inchi_key, name="inchi_key", curie=NMDC.curie('inchi_key'),
                   model_uri=NMDC.inchi_key, domain=None, range=Optional[str])

slots.inchi = Slot(uri=NMDC.inchi, name="inchi", curie=NMDC.curie('inchi'),
                   model_uri=NMDC.inchi, domain=None, range=Optional[str])

slots.peptide_sequence_count = Slot(uri=NMDC.peptide_sequence_count, name="peptide_sequence_count", curie=NMDC.curie('peptide_sequence_count'),
                   model_uri=NMDC.peptide_sequence_count, domain=None, range=Optional[int])

slots.protein_spectral_count = Slot(uri=NMDC.protein_spectral_count, name="protein_spectral_count", curie=NMDC.curie('protein_spectral_count'),
                   model_uri=NMDC.protein_spectral_count, domain=None, range=Optional[int])

slots.protein_sum_masic_abundance = Slot(uri=NMDC.protein_sum_masic_abundance, name="protein_sum_masic_abundance", curie=NMDC.curie('protein_sum_masic_abundance'),
                   model_uri=NMDC.protein_sum_masic_abundance, domain=None, range=Optional[int])

slots.smiles = Slot(uri=NMDC.smiles, name="smiles", curie=NMDC.curie('smiles'),
                   model_uri=NMDC.smiles, domain=None, range=Optional[Union[str, List[str]]])

slots.volume = Slot(uri=NMDC.volume, name="volume", curie=NMDC.curie('volume'),
                   model_uri=NMDC.volume, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.sample_state_information = Slot(uri=NMDC.sample_state_information, name="sample_state_information", curie=NMDC.curie('sample_state_information'),
                   model_uri=NMDC.sample_state_information, domain=None, range=Optional[Union[str, "SampleStateEnum"]])

slots.feature_category = Slot(uri=NMDC.feature_category, name="feature_category", curie=NMDC.curie('feature_category'),
                   model_uri=NMDC.feature_category, domain=None, range=Optional[Union[dict, ControlledIdentifiedTermValue]])

slots.subject = Slot(uri=NMDC.subject, name="subject", curie=NMDC.curie('subject'),
                   model_uri=NMDC.subject, domain=None, range=Optional[Union[str, GeneProductId]])

slots.has_function = Slot(uri=NMDC.has_function, name="has_function", curie=NMDC.curie('has_function'),
                   model_uri=NMDC.has_function, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(KEGG_PATHWAY:\w{2,4}\d{5}|KEGG.REACTION:R\d+|RHEA:\d{5}|MetaCyc:[A-Za-z0-9+_.%-:]+|EC:\d{1,2}(\.\d{0,3}){0,3}|GO:\d{7}|MetaNetX:(MNXR\d+|EMPTY)|SEED:\w+|KEGG\.ORTHOLOGY:K\d+|EGGNOG:\w+|PFAM:PF\d{5}|TIGRFAM:TIGR\d+|SUPFAM:\w+|CATH:[1-6]\.[0-9]+\.[0-9]+\.[0-9]+|PANTHER.FAMILY:PTHR\d{5}(\:SF\d{1,3})?)$'))

slots.gff_coordinate = Slot(uri=NMDC.gff_coordinate, name="gff_coordinate", curie=NMDC.curie('gff_coordinate'),
                   model_uri=NMDC.gff_coordinate, domain=None, range=Optional[int])

slots.seqid = Slot(uri=NMDC.seqid, name="seqid", curie=NMDC.curie('seqid'),
                   model_uri=NMDC.seqid, domain=None, range=Optional[str])

slots.strand = Slot(uri=NMDC.strand, name="strand", curie=NMDC.curie('strand'),
                   model_uri=NMDC.strand, domain=None, range=Optional[str])

slots.encodes = Slot(uri=NMDC.encodes, name="encodes", curie=NMDC.curie('encodes'),
                   model_uri=NMDC.encodes, domain=None, range=Optional[Union[str, GeneProductId]])

slots.end = Slot(uri=NMDC.end, name="end", curie=NMDC.curie('end'),
                   model_uri=NMDC.end, domain=None, range=Optional[int])

slots.feature_type = Slot(uri=NMDC.feature_type, name="feature_type", curie=NMDC.curie('feature_type'),
                   model_uri=NMDC.feature_type, domain=None, range=Optional[str])

slots.phase = Slot(uri=NMDC.phase, name="phase", curie=NMDC.curie('phase'),
                   model_uri=NMDC.phase, domain=None, range=Optional[int])

slots.start = Slot(uri=NMDC.start, name="start", curie=NMDC.curie('start'),
                   model_uri=NMDC.start, domain=None, range=Optional[int])

slots.biomaterial_purity = Slot(uri=NMDC.biomaterial_purity, name="biomaterial_purity", curie=NMDC.curie('biomaterial_purity'),
                   model_uri=NMDC.biomaterial_purity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.term = Slot(uri=NMDC.term, name="term", curie=NMDC.curie('term'),
                   model_uri=NMDC.term, domain=None, range=Optional[Union[dict, OntologyClass]])

slots.img_identifiers = Slot(uri=NMDC.img_identifiers, name="img_identifiers", curie=NMDC.curie('img_identifiers'),
                   model_uri=NMDC.img_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^img\.taxon:[a-zA-Z0-9_][a-zA-Z0-9_\/\.]*$'))

slots.igsn_identifiers = Slot(uri=NMDC.igsn_identifiers, name="igsn_identifiers", curie=NMDC.curie('igsn_identifiers'),
                   model_uri=NMDC.igsn_identifiers, domain=None, range=Optional[str])

slots.gold_identifiers = Slot(uri=NMDC.gold_identifiers, name="gold_identifiers", curie=NMDC.curie('gold_identifiers'),
                   model_uri=NMDC.gold_identifiers, domain=None, range=Optional[str])

slots.emsl_identifiers = Slot(uri=NMDC.emsl_identifiers, name="emsl_identifiers", curie=NMDC.curie('emsl_identifiers'),
                   model_uri=NMDC.emsl_identifiers, domain=None, range=Optional[str])

slots.mgnify_identifiers = Slot(uri=NMDC.mgnify_identifiers, name="mgnify_identifiers", curie=NMDC.curie('mgnify_identifiers'),
                   model_uri=NMDC.mgnify_identifiers, domain=None, range=Optional[str])

slots.insdc_identifiers = Slot(uri=NMDC.insdc_identifiers, name="insdc_identifiers", curie=NMDC.curie('insdc_identifiers'),
                   model_uri=NMDC.insdc_identifiers, domain=None, range=Optional[str])

slots.neon_identifiers = Slot(uri=NMDC.neon_identifiers, name="neon_identifiers", curie=NMDC.curie('neon_identifiers'),
                   model_uri=NMDC.neon_identifiers, domain=None, range=Optional[str])

slots.jgi_portal_identifiers = Slot(uri=NMDC.jgi_portal_identifiers, name="jgi_portal_identifiers", curie=NMDC.curie('jgi_portal_identifiers'),
                   model_uri=NMDC.jgi_portal_identifiers, domain=None, range=Optional[str])

slots.gnps_identifiers = Slot(uri=NMDC.gnps_identifiers, name="gnps_identifiers", curie=NMDC.curie('gnps_identifiers'),
                   model_uri=NMDC.gnps_identifiers, domain=None, range=Optional[str])

slots.study_identifiers = Slot(uri=NMDC.study_identifiers, name="study_identifiers", curie=NMDC.curie('study_identifiers'),
                   model_uri=NMDC.study_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$'))

slots.jgi_portal_study_identifiers = Slot(uri=NMDC.jgi_portal_study_identifiers, name="jgi_portal_study_identifiers", curie=NMDC.curie('jgi_portal_study_identifiers'),
                   model_uri=NMDC.jgi_portal_study_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^jgi.proposal:\d+$'))

slots.neon_study_identifiers = Slot(uri=NMDC.neon_study_identifiers, name="neon_study_identifiers", curie=NMDC.curie('neon_study_identifiers'),
                   model_uri=NMDC.neon_study_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$'))

slots.insdc_sra_ena_study_identifiers = Slot(uri=NMDC.insdc_sra_ena_study_identifiers, name="insdc_sra_ena_study_identifiers", curie=NMDC.curie('insdc_sra_ena_study_identifiers'),
                   model_uri=NMDC.insdc_sra_ena_study_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^insdc.sra:(E|D|S)RP[0-9]{6,}$'))

slots.insdc_bioproject_identifiers = Slot(uri=NMDC.insdc_bioproject_identifiers, name="insdc_bioproject_identifiers", curie=NMDC.curie('insdc_bioproject_identifiers'),
                   model_uri=NMDC.insdc_bioproject_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^bioproject:PRJ[DEN][A-Z][0-9]+$'))

slots.gold_study_identifiers = Slot(uri=NMDC.gold_study_identifiers, name="gold_study_identifiers", curie=NMDC.curie('gold_study_identifiers'),
                   model_uri=NMDC.gold_study_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^gold:Gs[0-9]+$'))

slots.mgnify_project_identifiers = Slot(uri=NMDC.mgnify_project_identifiers, name="mgnify_project_identifiers", curie=NMDC.curie('mgnify_project_identifiers'),
                   model_uri=NMDC.mgnify_project_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^mgnify.proj:[A-Z]+[0-9]+$'))

slots.gnps_task_identifiers = Slot(uri=NMDC.gnps_task_identifiers, name="gnps_task_identifiers", curie=NMDC.curie('gnps_task_identifiers'),
                   model_uri=NMDC.gnps_task_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^gnps\.task:[a-f0-9]+$'))

slots.emsl_project_identifiers = Slot(uri=NMDC.emsl_project_identifiers, name="emsl_project_identifiers", curie=NMDC.curie('emsl_project_identifiers'),
                   model_uri=NMDC.emsl_project_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^emsl\.project:[0-9]{5}$'))

slots.biosample_identifiers = Slot(uri=NMDC.biosample_identifiers, name="biosample_identifiers", curie=NMDC.curie('biosample_identifiers'),
                   model_uri=NMDC.biosample_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$'))

slots.neon_biosample_identifiers = Slot(uri=NMDC.neon_biosample_identifiers, name="neon_biosample_identifiers", curie=NMDC.curie('neon_biosample_identifiers'),
                   model_uri=NMDC.neon_biosample_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$'))

slots.gold_biosample_identifiers = Slot(uri=NMDC.gold_biosample_identifiers, name="gold_biosample_identifiers", curie=NMDC.curie('gold_biosample_identifiers'),
                   model_uri=NMDC.gold_biosample_identifiers, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]],
                   pattern=re.compile(r'^gold:Gb[0-9]+$'))

slots.insdc_biosample_identifiers = Slot(uri=NMDC.insdc_biosample_identifiers, name="insdc_biosample_identifiers", curie=NMDC.curie('insdc_biosample_identifiers'),
                   model_uri=NMDC.insdc_biosample_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^biosample:SAM[NED]([A-Z])?[0-9]+$'))

slots.insdc_secondary_sample_identifiers = Slot(uri=NMDC.insdc_secondary_sample_identifiers, name="insdc_secondary_sample_identifiers", curie=NMDC.curie('insdc_secondary_sample_identifiers'),
                   model_uri=NMDC.insdc_secondary_sample_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^biosample:(E|D|S)RS[0-9]{6,}$'))

slots.emsl_biosample_identifiers = Slot(uri=NMDC.emsl_biosample_identifiers, name="emsl_biosample_identifiers", curie=NMDC.curie('emsl_biosample_identifiers'),
                   model_uri=NMDC.emsl_biosample_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$'))

slots.igsn_biosample_identifiers = Slot(uri=NMDC.igsn_biosample_identifiers, name="igsn_biosample_identifiers", curie=NMDC.curie('igsn_biosample_identifiers'),
                   model_uri=NMDC.igsn_biosample_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$'))

slots.omics_processing_identifiers = Slot(uri=NMDC.omics_processing_identifiers, name="omics_processing_identifiers", curie=NMDC.curie('omics_processing_identifiers'),
                   model_uri=NMDC.omics_processing_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$'))

slots.gold_sequencing_project_identifiers = Slot(uri=NMDC.gold_sequencing_project_identifiers, name="gold_sequencing_project_identifiers", curie=NMDC.curie('gold_sequencing_project_identifiers'),
                   model_uri=NMDC.gold_sequencing_project_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^gold:Gp[0-9]+$'))

slots.insdc_experiment_identifiers = Slot(uri=NMDC.insdc_experiment_identifiers, name="insdc_experiment_identifiers", curie=NMDC.curie('insdc_experiment_identifiers'),
                   model_uri=NMDC.insdc_experiment_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^insdc.sra:(E|D|S)RX[0-9]{6,}$'))

slots.analysis_identifiers = Slot(uri=NMDC.analysis_identifiers, name="analysis_identifiers", curie=NMDC.curie('analysis_identifiers'),
                   model_uri=NMDC.analysis_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$'))

slots.gold_analysis_project_identifiers = Slot(uri=NMDC.gold_analysis_project_identifiers, name="gold_analysis_project_identifiers", curie=NMDC.curie('gold_analysis_project_identifiers'),
                   model_uri=NMDC.gold_analysis_project_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^gold:Ga[0-9]+$'))

slots.jgi_portal_analysis_project_identifiers = Slot(uri=NMDC.jgi_portal_analysis_project_identifiers, name="jgi_portal_analysis_project_identifiers", curie=NMDC.curie('jgi_portal_analysis_project_identifiers'),
                   model_uri=NMDC.jgi_portal_analysis_project_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^jgi.analysis:[0-9]+$'))

slots.insdc_analysis_identifiers = Slot(uri=NMDC.insdc_analysis_identifiers, name="insdc_analysis_identifiers", curie=NMDC.curie('insdc_analysis_identifiers'),
                   model_uri=NMDC.insdc_analysis_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^insdc.sra:(E|D|S)RR[0-9]{6,}$'))

slots.mgnify_analysis_identifiers = Slot(uri=NMDC.mgnify_analysis_identifiers, name="mgnify_analysis_identifiers", curie=NMDC.curie('mgnify_analysis_identifiers'),
                   model_uri=NMDC.mgnify_analysis_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$'))

slots.assembly_identifiers = Slot(uri=NMDC.assembly_identifiers, name="assembly_identifiers", curie=NMDC.curie('assembly_identifiers'),
                   model_uri=NMDC.assembly_identifiers, domain=None, range=Optional[str])

slots.insdc_assembly_identifiers = Slot(uri=NMDC.insdc_assembly_identifiers, name="insdc_assembly_identifiers", curie=NMDC.curie('insdc_assembly_identifiers'),
                   model_uri=NMDC.insdc_assembly_identifiers, domain=None, range=Optional[str],
                   pattern=re.compile(r'^insdc.sra:[A-Z]+[0-9]+(\.[0-9]+)?$'))

slots.abs_air_humidity = Slot(uri=MIXS['0000122'], name="abs_air_humidity", curie=MIXS.curie('0000122'),
                   model_uri=NMDC.abs_air_humidity, domain=None, range=Optional[Union[dict, QuantityValue]])

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
                   model_uri=NMDC.agrochem_addition, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.air_PM_concen = Slot(uri=MIXS['0000108'], name="air_PM_concen", curie=MIXS.curie('0000108'),
                   model_uri=NMDC.air_PM_concen, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.air_temp = Slot(uri=MIXS['0000124'], name="air_temp", curie=MIXS.curie('0000124'),
                   model_uri=NMDC.air_temp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.air_temp_regm = Slot(uri=MIXS['0000551'], name="air_temp_regm", curie=MIXS.curie('0000551'),
                   model_uri=NMDC.air_temp_regm, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

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
                   model_uri=NMDC.antibiotic_regm, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.api = Slot(uri=MIXS['0000157'], name="api", curie=MIXS.curie('0000157'),
                   model_uri=NMDC.api, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.arch_struc = Slot(uri=MIXS['0000774'], name="arch_struc", curie=MIXS.curie('0000774'),
                   model_uri=NMDC.arch_struc, domain=None, range=Optional[Union[str, "ArchStrucEnum"]])

slots.aromatics_pc = Slot(uri=MIXS['0000133'], name="aromatics_pc", curie=MIXS.curie('0000133'),
                   model_uri=NMDC.aromatics_pc, domain=None, range=Optional[Union[dict, TextValue]])

slots.asphaltenes_pc = Slot(uri=MIXS['0000135'], name="asphaltenes_pc", curie=MIXS.curie('0000135'),
                   model_uri=NMDC.asphaltenes_pc, domain=None, range=Optional[Union[dict, TextValue]])

slots.atmospheric_data = Slot(uri=MIXS['0001097'], name="atmospheric_data", curie=MIXS.curie('0001097'),
                   model_uri=NMDC.atmospheric_data, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

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
                   model_uri=NMDC.biocide_admin_method, domain=None, range=Optional[Union[dict, TextValue]])

slots.biol_stat = Slot(uri=MIXS['0000858'], name="biol_stat", curie=MIXS.curie('0000858'),
                   model_uri=NMDC.biol_stat, domain=None, range=Optional[Union[str, "BiolStatEnum"]])

slots.biomass = Slot(uri=MIXS['0000174'], name="biomass", curie=MIXS.curie('0000174'),
                   model_uri=NMDC.biomass, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.biotic_regm = Slot(uri=MIXS['0001038'], name="biotic_regm", curie=MIXS.curie('0001038'),
                   model_uri=NMDC.biotic_regm, domain=None, range=Optional[Union[dict, TextValue]])

slots.biotic_relationship = Slot(uri=MIXS['0000028'], name="biotic_relationship", curie=MIXS.curie('0000028'),
                   model_uri=NMDC.biotic_relationship, domain=None, range=Optional[Union[str, "BioticRelationshipEnum"]])

slots.bishomohopanol = Slot(uri=MIXS['0000175'], name="bishomohopanol", curie=MIXS.curie('0000175'),
                   model_uri=NMDC.bishomohopanol, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.blood_press_diast = Slot(uri=MIXS['0000258'], name="blood_press_diast", curie=MIXS.curie('0000258'),
                   model_uri=NMDC.blood_press_diast, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.blood_press_syst = Slot(uri=MIXS['0000259'], name="blood_press_syst", curie=MIXS.curie('0000259'),
                   model_uri=NMDC.blood_press_syst, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.bromide = Slot(uri=MIXS['0000176'], name="bromide", curie=MIXS.curie('0000176'),
                   model_uri=NMDC.bromide, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.build_docs = Slot(uri=MIXS['0000787'], name="build_docs", curie=MIXS.curie('0000787'),
                   model_uri=NMDC.build_docs, domain=None, range=Optional[Union[str, "BuildDocsEnum"]])

slots.build_occup_type = Slot(uri=MIXS['0000761'], name="build_occup_type", curie=MIXS.curie('0000761'),
                   model_uri=NMDC.build_occup_type, domain=None, range=Optional[Union[Union[str, "BuildOccupTypeEnum"], List[Union[str, "BuildOccupTypeEnum"]]]])

slots.building_setting = Slot(uri=MIXS['0000768'], name="building_setting", curie=MIXS.curie('0000768'),
                   model_uri=NMDC.building_setting, domain=None, range=Optional[Union[str, "BuildingSettingEnum"]])

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
                   model_uri=NMDC.ceil_cond, domain=None, range=Optional[Union[str, "CeilCondEnum"]])

slots.ceil_finish_mat = Slot(uri=MIXS['0000780'], name="ceil_finish_mat", curie=MIXS.curie('0000780'),
                   model_uri=NMDC.ceil_finish_mat, domain=None, range=Optional[Union[str, "CeilFinishMatEnum"]])

slots.ceil_struc = Slot(uri=MIXS['0000782'], name="ceil_struc", curie=MIXS.curie('0000782'),
                   model_uri=NMDC.ceil_struc, domain=None, range=Optional[Union[dict, TextValue]])

slots.ceil_texture = Slot(uri=MIXS['0000783'], name="ceil_texture", curie=MIXS.curie('0000783'),
                   model_uri=NMDC.ceil_texture, domain=None, range=Optional[Union[str, "CeilTextureEnum"]])

slots.ceil_thermal_mass = Slot(uri=MIXS['0000143'], name="ceil_thermal_mass", curie=MIXS.curie('0000143'),
                   model_uri=NMDC.ceil_thermal_mass, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.ceil_type = Slot(uri=MIXS['0000784'], name="ceil_type", curie=MIXS.curie('0000784'),
                   model_uri=NMDC.ceil_type, domain=None, range=Optional[Union[str, "CeilTypeEnum"]])

slots.ceil_water_mold = Slot(uri=MIXS['0000781'], name="ceil_water_mold", curie=MIXS.curie('0000781'),
                   model_uri=NMDC.ceil_water_mold, domain=None, range=Optional[Union[dict, TextValue]])

slots.chem_administration = Slot(uri=MIXS['0000751'], name="chem_administration", curie=MIXS.curie('0000751'),
                   model_uri=NMDC.chem_administration, domain=None, range=Optional[Union[Union[dict, ControlledTermValue], List[Union[dict, ControlledTermValue]]]])

slots.chem_mutagen = Slot(uri=MIXS['0000555'], name="chem_mutagen", curie=MIXS.curie('0000555'),
                   model_uri=NMDC.chem_mutagen, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.chem_oxygen_dem = Slot(uri=MIXS['0000656'], name="chem_oxygen_dem", curie=MIXS.curie('0000656'),
                   model_uri=NMDC.chem_oxygen_dem, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.chem_treat_method = Slot(uri=MIXS['0000457'], name="chem_treat_method", curie=MIXS.curie('0000457'),
                   model_uri=NMDC.chem_treat_method, domain=None, range=Optional[str])

slots.chem_treatment = Slot(uri=MIXS['0001012'], name="chem_treatment", curie=MIXS.curie('0001012'),
                   model_uri=NMDC.chem_treatment, domain=None, range=Optional[Union[dict, TextValue]])

slots.chimera_check = Slot(uri=MIXS['0000052'], name="chimera_check", curie=MIXS.curie('0000052'),
                   model_uri=NMDC.chimera_check, domain=None, range=Optional[Union[dict, TextValue]])

slots.chloride = Slot(uri=MIXS['0000429'], name="chloride", curie=MIXS.curie('0000429'),
                   model_uri=NMDC.chloride, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.chlorophyll = Slot(uri=MIXS['0000177'], name="chlorophyll", curie=MIXS.curie('0000177'),
                   model_uri=NMDC.chlorophyll, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.climate_environment = Slot(uri=MIXS['0001040'], name="climate_environment", curie=MIXS.curie('0001040'),
                   model_uri=NMDC.climate_environment, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

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
                   model_uri=NMDC.cur_land_use, domain=None, range=Optional[Union[str, "CurLandUseEnum"]])

slots.cur_vegetation = Slot(uri=MIXS['0000312'], name="cur_vegetation", curie=MIXS.curie('0000312'),
                   model_uri=NMDC.cur_vegetation, domain=None, range=Optional[Union[dict, TextValue]])

slots.cur_vegetation_meth = Slot(uri=MIXS['0000314'], name="cur_vegetation_meth", curie=MIXS.curie('0000314'),
                   model_uri=NMDC.cur_vegetation_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.date_last_rain = Slot(uri=MIXS['0000786'], name="date_last_rain", curie=MIXS.curie('0000786'),
                   model_uri=NMDC.date_last_rain, domain=None, range=Optional[Union[dict, TimestampValue]])

slots.density = Slot(uri=MIXS['0000435'], name="density", curie=MIXS.curie('0000435'),
                   model_uri=NMDC.density, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.depos_env = Slot(uri=MIXS['0000992'], name="depos_env", curie=MIXS.curie('0000992'),
                   model_uri=NMDC.depos_env, domain=None, range=Optional[Union[str, "DeposEnvEnum"]])

slots.depth = Slot(uri=MIXS['0000018'], name="depth", curie=MIXS.curie('0000018'),
                   model_uri=NMDC.depth, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.dew_point = Slot(uri=MIXS['0000129'], name="dew_point", curie=MIXS.curie('0000129'),
                   model_uri=NMDC.dew_point, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.diether_lipids = Slot(uri=MIXS['0000178'], name="diether_lipids", curie=MIXS.curie('0000178'),
                   model_uri=NMDC.diether_lipids, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

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
                   model_uri=NMDC.door_comp_type, domain=None, range=Optional[Union[str, "DoorCompTypeEnum"]])

slots.door_cond = Slot(uri=MIXS['0000788'], name="door_cond", curie=MIXS.curie('0000788'),
                   model_uri=NMDC.door_cond, domain=None, range=Optional[Union[str, "DoorCondEnum"]])

slots.door_direct = Slot(uri=MIXS['0000789'], name="door_direct", curie=MIXS.curie('0000789'),
                   model_uri=NMDC.door_direct, domain=None, range=Optional[Union[str, "DoorDirectEnum"]])

slots.door_loc = Slot(uri=MIXS['0000790'], name="door_loc", curie=MIXS.curie('0000790'),
                   model_uri=NMDC.door_loc, domain=None, range=Optional[Union[str, "DoorLocEnum"]])

slots.door_mat = Slot(uri=MIXS['0000791'], name="door_mat", curie=MIXS.curie('0000791'),
                   model_uri=NMDC.door_mat, domain=None, range=Optional[Union[str, "DoorMatEnum"]])

slots.door_move = Slot(uri=MIXS['0000792'], name="door_move", curie=MIXS.curie('0000792'),
                   model_uri=NMDC.door_move, domain=None, range=Optional[Union[str, "DoorMoveEnum"]])

slots.door_size = Slot(uri=MIXS['0000158'], name="door_size", curie=MIXS.curie('0000158'),
                   model_uri=NMDC.door_size, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.door_type = Slot(uri=MIXS['0000794'], name="door_type", curie=MIXS.curie('0000794'),
                   model_uri=NMDC.door_type, domain=None, range=Optional[Union[str, "DoorTypeEnum"]])

slots.door_type_metal = Slot(uri=MIXS['0000796'], name="door_type_metal", curie=MIXS.curie('0000796'),
                   model_uri=NMDC.door_type_metal, domain=None, range=Optional[Union[str, "DoorTypeMetalEnum"]])

slots.door_type_wood = Slot(uri=MIXS['0000797'], name="door_type_wood", curie=MIXS.curie('0000797'),
                   model_uri=NMDC.door_type_wood, domain=None, range=Optional[Union[str, "DoorTypeWoodEnum"]])

slots.door_water_mold = Slot(uri=MIXS['0000793'], name="door_water_mold", curie=MIXS.curie('0000793'),
                   model_uri=NMDC.door_water_mold, domain=None, range=Optional[Union[dict, TextValue]])

slots.down_par = Slot(uri=MIXS['0000703'], name="down_par", curie=MIXS.curie('0000703'),
                   model_uri=NMDC.down_par, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.drainage_class = Slot(uri=MIXS['0001085'], name="drainage_class", curie=MIXS.curie('0001085'),
                   model_uri=NMDC.drainage_class, domain=None, range=Optional[Union[str, "DrainageClassEnum"]])

slots.drawings = Slot(uri=MIXS['0000798'], name="drawings", curie=MIXS.curie('0000798'),
                   model_uri=NMDC.drawings, domain=None, range=Optional[Union[str, "DrawingsEnum"]])

slots.efficiency_percent = Slot(uri=MIXS['0000657'], name="efficiency_percent", curie=MIXS.curie('0000657'),
                   model_uri=NMDC.efficiency_percent, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.elev = Slot(uri=MIXS['0000093'], name="elev", curie=MIXS.curie('0000093'),
                   model_uri=NMDC.elev, domain=None, range=Optional[float])

slots.elevator = Slot(uri=MIXS['0000799'], name="elevator", curie=MIXS.curie('0000799'),
                   model_uri=NMDC.elevator, domain=None, range=Optional[Union[dict, TextValue]])

slots.emulsions = Slot(uri=MIXS['0000660'], name="emulsions", curie=MIXS.curie('0000660'),
                   model_uri=NMDC.emulsions, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.env_broad_scale = Slot(uri=MIXS['0000012'], name="env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=NMDC.env_broad_scale, domain=None, range=Optional[Union[dict, ControlledIdentifiedTermValue]])

slots.env_local_scale = Slot(uri=MIXS['0000013'], name="env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=NMDC.env_local_scale, domain=None, range=Optional[Union[dict, ControlledIdentifiedTermValue]])

slots.env_medium = Slot(uri=MIXS['0000014'], name="env_medium", curie=MIXS.curie('0000014'),
                   model_uri=NMDC.env_medium, domain=None, range=Optional[Union[dict, ControlledIdentifiedTermValue]])

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

slots.ext_door = Slot(uri=MIXS['0000170'], name="ext_door", curie=MIXS.curie('0000170'),
                   model_uri=NMDC.ext_door, domain=None, range=Optional[Union[dict, TextValue]])

slots.ext_wall_orient = Slot(uri=MIXS['0000817'], name="ext_wall_orient", curie=MIXS.curie('0000817'),
                   model_uri=NMDC.ext_wall_orient, domain=None, range=Optional[Union[str, "ExtWallOrientEnum"]])

slots.ext_window_orient = Slot(uri=MIXS['0000818'], name="ext_window_orient", curie=MIXS.curie('0000818'),
                   model_uri=NMDC.ext_window_orient, domain=None, range=Optional[Union[str, "ExtWindowOrientEnum"]])

slots.extreme_event = Slot(uri=MIXS['0000320'], name="extreme_event", curie=MIXS.curie('0000320'),
                   model_uri=NMDC.extreme_event, domain=None, range=Optional[str])

slots.fao_class = Slot(uri=MIXS['0001083'], name="fao_class", curie=MIXS.curie('0001083'),
                   model_uri=NMDC.fao_class, domain=None, range=Optional[Union[str, "FaoClassEnum"]])

slots.fertilizer_regm = Slot(uri=MIXS['0000556'], name="fertilizer_regm", curie=MIXS.curie('0000556'),
                   model_uri=NMDC.fertilizer_regm, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.field = Slot(uri=MIXS['0000291'], name="field", curie=MIXS.curie('0000291'),
                   model_uri=NMDC.field, domain=None, range=Optional[Union[dict, TextValue]])

slots.filter_type = Slot(uri=MIXS['0000765'], name="filter_type", curie=MIXS.curie('0000765'),
                   model_uri=NMDC.filter_type, domain=None, range=Optional[Union[Union[str, "FilterTypeEnum"], List[Union[str, "FilterTypeEnum"]]]])

slots.fire = Slot(uri=MIXS['0001086'], name="fire", curie=MIXS.curie('0001086'),
                   model_uri=NMDC.fire, domain=None, range=Optional[str])

slots.fireplace_type = Slot(uri=MIXS['0000802'], name="fireplace_type", curie=MIXS.curie('0000802'),
                   model_uri=NMDC.fireplace_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.flooding = Slot(uri=MIXS['0000319'], name="flooding", curie=MIXS.curie('0000319'),
                   model_uri=NMDC.flooding, domain=None, range=Optional[str])

slots.floor_age = Slot(uri=MIXS['0000164'], name="floor_age", curie=MIXS.curie('0000164'),
                   model_uri=NMDC.floor_age, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.floor_area = Slot(uri=MIXS['0000165'], name="floor_area", curie=MIXS.curie('0000165'),
                   model_uri=NMDC.floor_area, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.floor_cond = Slot(uri=MIXS['0000803'], name="floor_cond", curie=MIXS.curie('0000803'),
                   model_uri=NMDC.floor_cond, domain=None, range=Optional[Union[str, "FloorCondEnum"]])

slots.floor_count = Slot(uri=MIXS['0000225'], name="floor_count", curie=MIXS.curie('0000225'),
                   model_uri=NMDC.floor_count, domain=None, range=Optional[Union[dict, TextValue]])

slots.floor_finish_mat = Slot(uri=MIXS['0000804'], name="floor_finish_mat", curie=MIXS.curie('0000804'),
                   model_uri=NMDC.floor_finish_mat, domain=None, range=Optional[Union[str, "FloorFinishMatEnum"]])

slots.floor_struc = Slot(uri=MIXS['0000806'], name="floor_struc", curie=MIXS.curie('0000806'),
                   model_uri=NMDC.floor_struc, domain=None, range=Optional[Union[str, "FloorStrucEnum"]])

slots.floor_thermal_mass = Slot(uri=MIXS['0000166'], name="floor_thermal_mass", curie=MIXS.curie('0000166'),
                   model_uri=NMDC.floor_thermal_mass, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.floor_water_mold = Slot(uri=MIXS['0000805'], name="floor_water_mold", curie=MIXS.curie('0000805'),
                   model_uri=NMDC.floor_water_mold, domain=None, range=Optional[Union[str, "FloorWaterMoldEnum"]])

slots.fluor = Slot(uri=MIXS['0000704'], name="fluor", curie=MIXS.curie('0000704'),
                   model_uri=NMDC.fluor, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.freq_clean = Slot(uri=MIXS['0000226'], name="freq_clean", curie=MIXS.curie('0000226'),
                   model_uri=NMDC.freq_clean, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.freq_cook = Slot(uri=MIXS['0000227'], name="freq_cook", curie=MIXS.curie('0000227'),
                   model_uri=NMDC.freq_cook, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.fungicide_regm = Slot(uri=MIXS['0000557'], name="fungicide_regm", curie=MIXS.curie('0000557'),
                   model_uri=NMDC.fungicide_regm, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.furniture = Slot(uri=MIXS['0000807'], name="furniture", curie=MIXS.curie('0000807'),
                   model_uri=NMDC.furniture, domain=None, range=Optional[Union[str, "FurnitureEnum"]])

slots.gaseous_environment = Slot(uri=MIXS['0000558'], name="gaseous_environment", curie=MIXS.curie('0000558'),
                   model_uri=NMDC.gaseous_environment, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.gaseous_substances = Slot(uri=MIXS['0000661'], name="gaseous_substances", curie=MIXS.curie('0000661'),
                   model_uri=NMDC.gaseous_substances, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.gender_restroom = Slot(uri=MIXS['0000808'], name="gender_restroom", curie=MIXS.curie('0000808'),
                   model_uri=NMDC.gender_restroom, domain=None, range=Optional[Union[str, "GenderRestroomEnum"]])

slots.genetic_mod = Slot(uri=MIXS['0000859'], name="genetic_mod", curie=MIXS.curie('0000859'),
                   model_uri=NMDC.genetic_mod, domain=None, range=Optional[Union[dict, TextValue]])

slots.geo_loc_name = Slot(uri=MIXS['0000010'], name="geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=NMDC.geo_loc_name, domain=None, range=Optional[Union[dict, TextValue]])

slots.glucosidase_act = Slot(uri=MIXS['0000137'], name="glucosidase_act", curie=MIXS.curie('0000137'),
                   model_uri=NMDC.glucosidase_act, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.gravidity = Slot(uri=MIXS['0000875'], name="gravidity", curie=MIXS.curie('0000875'),
                   model_uri=NMDC.gravidity, domain=None, range=Optional[Union[dict, TextValue]])

slots.gravity = Slot(uri=MIXS['0000559'], name="gravity", curie=MIXS.curie('0000559'),
                   model_uri=NMDC.gravity, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.growth_facil = Slot(uri=MIXS['0001043'], name="growth_facil", curie=MIXS.curie('0001043'),
                   model_uri=NMDC.growth_facil, domain=None, range=Optional[Union[dict, ControlledTermValue]])

slots.growth_habit = Slot(uri=MIXS['0001044'], name="growth_habit", curie=MIXS.curie('0001044'),
                   model_uri=NMDC.growth_habit, domain=None, range=Optional[Union[str, "GrowthHabitEnum"]])

slots.growth_hormone_regm = Slot(uri=MIXS['0000560'], name="growth_hormone_regm", curie=MIXS.curie('0000560'),
                   model_uri=NMDC.growth_hormone_regm, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.hall_count = Slot(uri=MIXS['0000228'], name="hall_count", curie=MIXS.curie('0000228'),
                   model_uri=NMDC.hall_count, domain=None, range=Optional[Union[dict, TextValue]])

slots.handidness = Slot(uri=MIXS['0000809'], name="handidness", curie=MIXS.curie('0000809'),
                   model_uri=NMDC.handidness, domain=None, range=Optional[Union[str, "HandidnessEnum"]])

slots.hc_produced = Slot(uri=MIXS['0000989'], name="hc_produced", curie=MIXS.curie('0000989'),
                   model_uri=NMDC.hc_produced, domain=None, range=Optional[Union[str, "HcProducedEnum"]])

slots.hcr = Slot(uri=MIXS['0000988'], name="hcr", curie=MIXS.curie('0000988'),
                   model_uri=NMDC.hcr, domain=None, range=Optional[Union[str, "HcrEnum"]])

slots.hcr_fw_salinity = Slot(uri=MIXS['0000406'], name="hcr_fw_salinity", curie=MIXS.curie('0000406'),
                   model_uri=NMDC.hcr_fw_salinity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.hcr_geol_age = Slot(uri=MIXS['0000993'], name="hcr_geol_age", curie=MIXS.curie('0000993'),
                   model_uri=NMDC.hcr_geol_age, domain=None, range=Optional[Union[str, "HcrGeolAgeEnum"]])

slots.hcr_pressure = Slot(uri=MIXS['0000395'], name="hcr_pressure", curie=MIXS.curie('0000395'),
                   model_uri=NMDC.hcr_pressure, domain=None, range=Optional[Union[dict, TextValue]])

slots.hcr_temp = Slot(uri=MIXS['0000393'], name="hcr_temp", curie=MIXS.curie('0000393'),
                   model_uri=NMDC.hcr_temp, domain=None, range=Optional[Union[dict, TextValue]])

slots.heat_cool_type = Slot(uri=MIXS['0000766'], name="heat_cool_type", curie=MIXS.curie('0000766'),
                   model_uri=NMDC.heat_cool_type, domain=None, range=Optional[Union[Union[str, "HeatCoolTypeEnum"], List[Union[str, "HeatCoolTypeEnum"]]]])

slots.heat_deliv_loc = Slot(uri=MIXS['0000810'], name="heat_deliv_loc", curie=MIXS.curie('0000810'),
                   model_uri=NMDC.heat_deliv_loc, domain=None, range=Optional[Union[str, "HeatDelivLocEnum"]])

slots.heat_sys_deliv_meth = Slot(uri=MIXS['0000812'], name="heat_sys_deliv_meth", curie=MIXS.curie('0000812'),
                   model_uri=NMDC.heat_sys_deliv_meth, domain=None, range=Optional[str])

slots.heat_system_id = Slot(uri=MIXS['0000833'], name="heat_system_id", curie=MIXS.curie('0000833'),
                   model_uri=NMDC.heat_system_id, domain=None, range=Optional[Union[dict, TextValue]])

slots.heavy_metals = Slot(uri=MIXS['0000652'], name="heavy_metals", curie=MIXS.curie('0000652'),
                   model_uri=NMDC.heavy_metals, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.heavy_metals_meth = Slot(uri=MIXS['0000343'], name="heavy_metals_meth", curie=MIXS.curie('0000343'),
                   model_uri=NMDC.heavy_metals_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.height_carper_fiber = Slot(uri=MIXS['0000167'], name="height_carper_fiber", curie=MIXS.curie('0000167'),
                   model_uri=NMDC.height_carper_fiber, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.herbicide_regm = Slot(uri=MIXS['0000561'], name="herbicide_regm", curie=MIXS.curie('0000561'),
                   model_uri=NMDC.herbicide_regm, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

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
                   model_uri=NMDC.host_diet, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.host_disease_stat = Slot(uri=MIXS['0000031'], name="host_disease_stat", curie=MIXS.curie('0000031'),
                   model_uri=NMDC.host_disease_stat, domain=None, range=Optional[Union[dict, TextValue]])

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
                   model_uri=NMDC.host_last_meal, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.host_length = Slot(uri=MIXS['0000256'], name="host_length", curie=MIXS.curie('0000256'),
                   model_uri=NMDC.host_length, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.host_life_stage = Slot(uri=MIXS['0000251'], name="host_life_stage", curie=MIXS.curie('0000251'),
                   model_uri=NMDC.host_life_stage, domain=None, range=Optional[Union[dict, TextValue]])

slots.host_phenotype = Slot(uri=MIXS['0000874'], name="host_phenotype", curie=MIXS.curie('0000874'),
                   model_uri=NMDC.host_phenotype, domain=None, range=Optional[Union[dict, ControlledTermValue]])

slots.host_sex = Slot(uri=MIXS['0000811'], name="host_sex", curie=MIXS.curie('0000811'),
                   model_uri=NMDC.host_sex, domain=None, range=Optional[Union[str, "HostSexEnum"]])

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
                   model_uri=NMDC.host_taxid, domain=None, range=Optional[Union[dict, ControlledIdentifiedTermValue]])

slots.host_tot_mass = Slot(uri=MIXS['0000263'], name="host_tot_mass", curie=MIXS.curie('0000263'),
                   model_uri=NMDC.host_tot_mass, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.host_wet_mass = Slot(uri=MIXS['0000567'], name="host_wet_mass", curie=MIXS.curie('0000567'),
                   model_uri=NMDC.host_wet_mass, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.humidity = Slot(uri=MIXS['0000100'], name="humidity", curie=MIXS.curie('0000100'),
                   model_uri=NMDC.humidity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.humidity_regm = Slot(uri=MIXS['0000568'], name="humidity_regm", curie=MIXS.curie('0000568'),
                   model_uri=NMDC.humidity_regm, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.indoor_space = Slot(uri=MIXS['0000763'], name="indoor_space", curie=MIXS.curie('0000763'),
                   model_uri=NMDC.indoor_space, domain=None, range=Optional[Union[str, "IndoorSpaceEnum"]])

slots.indoor_surf = Slot(uri=MIXS['0000764'], name="indoor_surf", curie=MIXS.curie('0000764'),
                   model_uri=NMDC.indoor_surf, domain=None, range=Optional[Union[str, "IndoorSurfEnum"]])

slots.indust_eff_percent = Slot(uri=MIXS['0000662'], name="indust_eff_percent", curie=MIXS.curie('0000662'),
                   model_uri=NMDC.indust_eff_percent, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.inorg_particles = Slot(uri=MIXS['0000664'], name="inorg_particles", curie=MIXS.curie('0000664'),
                   model_uri=NMDC.inorg_particles, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.inside_lux = Slot(uri=MIXS['0000168'], name="inside_lux", curie=MIXS.curie('0000168'),
                   model_uri=NMDC.inside_lux, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.int_wall_cond = Slot(uri=MIXS['0000813'], name="int_wall_cond", curie=MIXS.curie('0000813'),
                   model_uri=NMDC.int_wall_cond, domain=None, range=Optional[Union[str, "IntWallCondEnum"]])

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
                   model_uri=NMDC.light_regm, domain=None, range=Optional[Union[dict, TextValue]])

slots.light_type = Slot(uri=MIXS['0000769'], name="light_type", curie=MIXS.curie('0000769'),
                   model_uri=NMDC.light_type, domain=None, range=Optional[Union[Union[str, "LightTypeEnum"], List[Union[str, "LightTypeEnum"]]]])

slots.link_addit_analys = Slot(uri=MIXS['0000340'], name="link_addit_analys", curie=MIXS.curie('0000340'),
                   model_uri=NMDC.link_addit_analys, domain=None, range=Optional[Union[dict, TextValue]])

slots.link_class_info = Slot(uri=MIXS['0000329'], name="link_class_info", curie=MIXS.curie('0000329'),
                   model_uri=NMDC.link_class_info, domain=None, range=Optional[Union[dict, TextValue]])

slots.link_climate_info = Slot(uri=MIXS['0000328'], name="link_climate_info", curie=MIXS.curie('0000328'),
                   model_uri=NMDC.link_climate_info, domain=None, range=Optional[Union[dict, TextValue]])

slots.lithology = Slot(uri=MIXS['0000990'], name="lithology", curie=MIXS.curie('0000990'),
                   model_uri=NMDC.lithology, domain=None, range=Optional[Union[str, "LithologyEnum"]])

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
                   model_uri=NMDC.mech_struc, domain=None, range=Optional[Union[str, "MechStrucEnum"]])

slots.mechanical_damage = Slot(uri=MIXS['0001052'], name="mechanical_damage", curie=MIXS.curie('0001052'),
                   model_uri=NMDC.mechanical_damage, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.methane = Slot(uri=MIXS['0000101'], name="methane", curie=MIXS.curie('0000101'),
                   model_uri=NMDC.methane, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.micro_biomass_meth = Slot(uri=MIXS['0000339'], name="micro_biomass_meth", curie=MIXS.curie('0000339'),
                   model_uri=NMDC.micro_biomass_meth, domain=None, range=Optional[str])

slots.microbial_biomass = Slot(uri=MIXS['0000650'], name="microbial_biomass", curie=MIXS.curie('0000650'),
                   model_uri=NMDC.microbial_biomass, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.mineral_nutr_regm = Slot(uri=MIXS['0000570'], name="mineral_nutr_regm", curie=MIXS.curie('0000570'),
                   model_uri=NMDC.mineral_nutr_regm, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.misc_param = Slot(uri=MIXS['0000752'], name="misc_param", curie=MIXS.curie('0000752'),
                   model_uri=NMDC.misc_param, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.n_alkanes = Slot(uri=MIXS['0000503'], name="n_alkanes", curie=MIXS.curie('0000503'),
                   model_uri=NMDC.n_alkanes, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

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
                   model_uri=NMDC.occup_document, domain=None, range=Optional[Union[str, "OccupDocumentEnum"]])

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
                   model_uri=NMDC.org_particles, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.organism_count = Slot(uri=MIXS['0000103'], name="organism_count", curie=MIXS.curie('0000103'),
                   model_uri=NMDC.organism_count, domain=None, range=Optional[Union[Union[dict, QuantityValue], List[Union[dict, QuantityValue]]]])

slots.owc_tvdss = Slot(uri=MIXS['0000405'], name="owc_tvdss", curie=MIXS.curie('0000405'),
                   model_uri=NMDC.owc_tvdss, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.oxy_stat_samp = Slot(uri=MIXS['0000753'], name="oxy_stat_samp", curie=MIXS.curie('0000753'),
                   model_uri=NMDC.oxy_stat_samp, domain=None, range=Optional[Union[str, "OxyStatSampEnum"]])

slots.oxygen = Slot(uri=MIXS['0000104'], name="oxygen", curie=MIXS.curie('0000104'),
                   model_uri=NMDC.oxygen, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.part_org_carb = Slot(uri=MIXS['0000515'], name="part_org_carb", curie=MIXS.curie('0000515'),
                   model_uri=NMDC.part_org_carb, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.part_org_nitro = Slot(uri=MIXS['0000719'], name="part_org_nitro", curie=MIXS.curie('0000719'),
                   model_uri=NMDC.part_org_nitro, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.particle_class = Slot(uri=MIXS['0000206'], name="particle_class", curie=MIXS.curie('0000206'),
                   model_uri=NMDC.particle_class, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.pcr_cond = Slot(uri=MIXS['0000049'], name="pcr_cond", curie=MIXS.curie('0000049'),
                   model_uri=NMDC.pcr_cond, domain=None, range=Optional[Union[dict, TextValue]])

slots.pcr_primers = Slot(uri=MIXS['0000046'], name="pcr_primers", curie=MIXS.curie('0000046'),
                   model_uri=NMDC.pcr_primers, domain=None, range=Optional[Union[dict, TextValue]])

slots.permeability = Slot(uri=MIXS['0000404'], name="permeability", curie=MIXS.curie('0000404'),
                   model_uri=NMDC.permeability, domain=None, range=Optional[Union[dict, TextValue]])

slots.perturbation = Slot(uri=MIXS['0000754'], name="perturbation", curie=MIXS.curie('0000754'),
                   model_uri=NMDC.perturbation, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.pesticide_regm = Slot(uri=MIXS['0000573'], name="pesticide_regm", curie=MIXS.curie('0000573'),
                   model_uri=NMDC.pesticide_regm, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.petroleum_hydrocarb = Slot(uri=MIXS['0000516'], name="petroleum_hydrocarb", curie=MIXS.curie('0000516'),
                   model_uri=NMDC.petroleum_hydrocarb, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.ph = Slot(uri=MIXS['0001001'], name="ph", curie=MIXS.curie('0001001'),
                   model_uri=NMDC.ph, domain=None, range=Optional[float])

slots.ph_meth = Slot(uri=MIXS['0001106'], name="ph_meth", curie=MIXS.curie('0001106'),
                   model_uri=NMDC.ph_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.ph_regm = Slot(uri=MIXS['0001056'], name="ph_regm", curie=MIXS.curie('0001056'),
                   model_uri=NMDC.ph_regm, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.phaeopigments = Slot(uri=MIXS['0000180'], name="phaeopigments", curie=MIXS.curie('0000180'),
                   model_uri=NMDC.phaeopigments, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.phosphate = Slot(uri=MIXS['0000505'], name="phosphate", curie=MIXS.curie('0000505'),
                   model_uri=NMDC.phosphate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.phosplipid_fatt_acid = Slot(uri=MIXS['0000181'], name="phosplipid_fatt_acid", curie=MIXS.curie('0000181'),
                   model_uri=NMDC.phosplipid_fatt_acid, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.photon_flux = Slot(uri=MIXS['0000725'], name="photon_flux", curie=MIXS.curie('0000725'),
                   model_uri=NMDC.photon_flux, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.plant_growth_med = Slot(uri=MIXS['0001057'], name="plant_growth_med", curie=MIXS.curie('0001057'),
                   model_uri=NMDC.plant_growth_med, domain=None, range=Optional[Union[dict, ControlledTermValue]])

slots.plant_product = Slot(uri=MIXS['0001058'], name="plant_product", curie=MIXS.curie('0001058'),
                   model_uri=NMDC.plant_product, domain=None, range=Optional[Union[dict, TextValue]])

slots.plant_sex = Slot(uri=MIXS['0001059'], name="plant_sex", curie=MIXS.curie('0001059'),
                   model_uri=NMDC.plant_sex, domain=None, range=Optional[Union[str, "PlantSexEnum"]])

slots.plant_struc = Slot(uri=MIXS['0001060'], name="plant_struc", curie=MIXS.curie('0001060'),
                   model_uri=NMDC.plant_struc, domain=None, range=Optional[Union[dict, ControlledTermValue]])

slots.pollutants = Slot(uri=MIXS['0000107'], name="pollutants", curie=MIXS.curie('0000107'),
                   model_uri=NMDC.pollutants, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.pool_dna_extracts = Slot(uri=MIXS['0000325'], name="pool_dna_extracts", curie=MIXS.curie('0000325'),
                   model_uri=NMDC.pool_dna_extracts, domain=None, range=Optional[Union[dict, TextValue]])

slots.porosity = Slot(uri=MIXS['0000211'], name="porosity", curie=MIXS.curie('0000211'),
                   model_uri=NMDC.porosity, domain=None, range=Optional[Union[dict, TextValue]])

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

slots.primary_prod = Slot(uri=MIXS['0000728'], name="primary_prod", curie=MIXS.curie('0000728'),
                   model_uri=NMDC.primary_prod, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.primary_treatment = Slot(uri=MIXS['0000349'], name="primary_treatment", curie=MIXS.curie('0000349'),
                   model_uri=NMDC.primary_treatment, domain=None, range=Optional[Union[dict, TextValue]])

slots.prod_rate = Slot(uri=MIXS['0000452'], name="prod_rate", curie=MIXS.curie('0000452'),
                   model_uri=NMDC.prod_rate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.prod_start_date = Slot(uri=MIXS['0001008'], name="prod_start_date", curie=MIXS.curie('0001008'),
                   model_uri=NMDC.prod_start_date, domain=None, range=Optional[Union[dict, TimestampValue]])

slots.profile_position = Slot(uri=MIXS['0001084'], name="profile_position", curie=MIXS.curie('0001084'),
                   model_uri=NMDC.profile_position, domain=None, range=Optional[Union[str, "ProfilePositionEnum"]])

slots.quad_pos = Slot(uri=MIXS['0000820'], name="quad_pos", curie=MIXS.curie('0000820'),
                   model_uri=NMDC.quad_pos, domain=None, range=Optional[Union[str, "QuadPosEnum"]])

slots.radiation_regm = Slot(uri=MIXS['0000575'], name="radiation_regm", curie=MIXS.curie('0000575'),
                   model_uri=NMDC.radiation_regm, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.rainfall_regm = Slot(uri=MIXS['0000576'], name="rainfall_regm", curie=MIXS.curie('0000576'),
                   model_uri=NMDC.rainfall_regm, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.reactor_type = Slot(uri=MIXS['0000350'], name="reactor_type", curie=MIXS.curie('0000350'),
                   model_uri=NMDC.reactor_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.redox_potential = Slot(uri=MIXS['0000182'], name="redox_potential", curie=MIXS.curie('0000182'),
                   model_uri=NMDC.redox_potential, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.rel_air_humidity = Slot(uri=MIXS['0000121'], name="rel_air_humidity", curie=MIXS.curie('0000121'),
                   model_uri=NMDC.rel_air_humidity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.rel_humidity_out = Slot(uri=MIXS['0000188'], name="rel_humidity_out", curie=MIXS.curie('0000188'),
                   model_uri=NMDC.rel_humidity_out, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.rel_samp_loc = Slot(uri=MIXS['0000821'], name="rel_samp_loc", curie=MIXS.curie('0000821'),
                   model_uri=NMDC.rel_samp_loc, domain=None, range=Optional[Union[str, "RelSampLocEnum"]])

slots.reservoir = Slot(uri=MIXS['0000303'], name="reservoir", curie=MIXS.curie('0000303'),
                   model_uri=NMDC.reservoir, domain=None, range=Optional[Union[dict, TextValue]])

slots.resins_pc = Slot(uri=MIXS['0000134'], name="resins_pc", curie=MIXS.curie('0000134'),
                   model_uri=NMDC.resins_pc, domain=None, range=Optional[Union[dict, TextValue]])

slots.room_air_exch_rate = Slot(uri=MIXS['0000169'], name="room_air_exch_rate", curie=MIXS.curie('0000169'),
                   model_uri=NMDC.room_air_exch_rate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.room_architec_elem = Slot(uri=MIXS['0000233'], name="room_architec_elem", curie=MIXS.curie('0000233'),
                   model_uri=NMDC.room_architec_elem, domain=None, range=Optional[str])

slots.room_condt = Slot(uri=MIXS['0000822'], name="room_condt", curie=MIXS.curie('0000822'),
                   model_uri=NMDC.room_condt, domain=None, range=Optional[Union[str, "RoomCondtEnum"]])

slots.room_connected = Slot(uri=MIXS['0000826'], name="room_connected", curie=MIXS.curie('0000826'),
                   model_uri=NMDC.room_connected, domain=None, range=Optional[Union[str, "RoomConnectedEnum"]])

slots.room_count = Slot(uri=MIXS['0000234'], name="room_count", curie=MIXS.curie('0000234'),
                   model_uri=NMDC.room_count, domain=None, range=Optional[Union[dict, TextValue]])

slots.room_dim = Slot(uri=MIXS['0000192'], name="room_dim", curie=MIXS.curie('0000192'),
                   model_uri=NMDC.room_dim, domain=None, range=Optional[Union[dict, TextValue]])

slots.room_door_dist = Slot(uri=MIXS['0000193'], name="room_door_dist", curie=MIXS.curie('0000193'),
                   model_uri=NMDC.room_door_dist, domain=None, range=Optional[Union[dict, TextValue]])

slots.room_door_share = Slot(uri=MIXS['0000242'], name="room_door_share", curie=MIXS.curie('0000242'),
                   model_uri=NMDC.room_door_share, domain=None, range=Optional[Union[dict, TextValue]])

slots.room_hallway = Slot(uri=MIXS['0000238'], name="room_hallway", curie=MIXS.curie('0000238'),
                   model_uri=NMDC.room_hallway, domain=None, range=Optional[Union[dict, TextValue]])

slots.room_loc = Slot(uri=MIXS['0000823'], name="room_loc", curie=MIXS.curie('0000823'),
                   model_uri=NMDC.room_loc, domain=None, range=Optional[Union[str, "RoomLocEnum"]])

slots.room_moist_dam_hist = Slot(uri=MIXS['0000235'], name="room_moist_dam_hist", curie=MIXS.curie('0000235'),
                   model_uri=NMDC.room_moist_dam_hist, domain=None, range=Optional[int])

slots.room_net_area = Slot(uri=MIXS['0000194'], name="room_net_area", curie=MIXS.curie('0000194'),
                   model_uri=NMDC.room_net_area, domain=None, range=Optional[Union[dict, TextValue]])

slots.room_occup = Slot(uri=MIXS['0000236'], name="room_occup", curie=MIXS.curie('0000236'),
                   model_uri=NMDC.room_occup, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.room_samp_pos = Slot(uri=MIXS['0000824'], name="room_samp_pos", curie=MIXS.curie('0000824'),
                   model_uri=NMDC.room_samp_pos, domain=None, range=Optional[Union[str, "RoomSampPosEnum"]])

slots.room_type = Slot(uri=MIXS['0000825'], name="room_type", curie=MIXS.curie('0000825'),
                   model_uri=NMDC.room_type, domain=None, range=Optional[Union[str, "RoomTypeEnum"]])

slots.room_vol = Slot(uri=MIXS['0000195'], name="room_vol", curie=MIXS.curie('0000195'),
                   model_uri=NMDC.room_vol, domain=None, range=Optional[Union[dict, TextValue]])

slots.room_wall_share = Slot(uri=MIXS['0000243'], name="room_wall_share", curie=MIXS.curie('0000243'),
                   model_uri=NMDC.room_wall_share, domain=None, range=Optional[Union[dict, TextValue]])

slots.room_window_count = Slot(uri=MIXS['0000237'], name="room_window_count", curie=MIXS.curie('0000237'),
                   model_uri=NMDC.room_window_count, domain=None, range=Optional[int])

slots.root_cond = Slot(uri=MIXS['0001061'], name="root_cond", curie=MIXS.curie('0001061'),
                   model_uri=NMDC.root_cond, domain=None, range=Optional[Union[dict, TextValue]])

slots.root_med_carbon = Slot(uri=MIXS['0000577'], name="root_med_carbon", curie=MIXS.curie('0000577'),
                   model_uri=NMDC.root_med_carbon, domain=None, range=Optional[Union[dict, TextValue]])

slots.root_med_macronutr = Slot(uri=MIXS['0000578'], name="root_med_macronutr", curie=MIXS.curie('0000578'),
                   model_uri=NMDC.root_med_macronutr, domain=None, range=Optional[Union[dict, TextValue]])

slots.root_med_micronutr = Slot(uri=MIXS['0000579'], name="root_med_micronutr", curie=MIXS.curie('0000579'),
                   model_uri=NMDC.root_med_micronutr, domain=None, range=Optional[Union[dict, TextValue]])

slots.root_med_ph = Slot(uri=MIXS['0001062'], name="root_med_ph", curie=MIXS.curie('0001062'),
                   model_uri=NMDC.root_med_ph, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.root_med_regl = Slot(uri=MIXS['0000581'], name="root_med_regl", curie=MIXS.curie('0000581'),
                   model_uri=NMDC.root_med_regl, domain=None, range=Optional[Union[dict, TextValue]])

slots.root_med_solid = Slot(uri=MIXS['0001063'], name="root_med_solid", curie=MIXS.curie('0001063'),
                   model_uri=NMDC.root_med_solid, domain=None, range=Optional[Union[dict, TextValue]])

slots.root_med_suppl = Slot(uri=MIXS['0000580'], name="root_med_suppl", curie=MIXS.curie('0000580'),
                   model_uri=NMDC.root_med_suppl, domain=None, range=Optional[Union[dict, TextValue]])

slots.salinity = Slot(uri=MIXS['0000183'], name="salinity", curie=MIXS.curie('0000183'),
                   model_uri=NMDC.salinity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.salinity_meth = Slot(uri=MIXS['0000341'], name="salinity_meth", curie=MIXS.curie('0000341'),
                   model_uri=NMDC.salinity_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.salt_regm = Slot(uri=MIXS['0000582'], name="salt_regm", curie=MIXS.curie('0000582'),
                   model_uri=NMDC.salt_regm, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.samp_capt_status = Slot(uri=MIXS['0000860'], name="samp_capt_status", curie=MIXS.curie('0000860'),
                   model_uri=NMDC.samp_capt_status, domain=None, range=Optional[Union[str, "SampCaptStatusEnum"]])

slots.samp_collec_device = Slot(uri=MIXS['0000002'], name="samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=NMDC.samp_collec_device, domain=None, range=Optional[str])

slots.samp_collec_method = Slot(uri=MIXS['0001225'], name="samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=NMDC.samp_collec_method, domain=None, range=Optional[str])

slots.samp_collect_point = Slot(uri=MIXS['0001015'], name="samp_collect_point", curie=MIXS.curie('0001015'),
                   model_uri=NMDC.samp_collect_point, domain=None, range=Optional[Union[str, "SampCollectPointEnum"]])

slots.samp_dis_stage = Slot(uri=MIXS['0000249'], name="samp_dis_stage", curie=MIXS.curie('0000249'),
                   model_uri=NMDC.samp_dis_stage, domain=None, range=Optional[Union[str, "SampDisStageEnum"]])

slots.samp_floor = Slot(uri=MIXS['0000828'], name="samp_floor", curie=MIXS.curie('0000828'),
                   model_uri=NMDC.samp_floor, domain=None, range=Optional[Union[str, "SampFloorEnum"]])

slots.samp_loc_corr_rate = Slot(uri=MIXS['0000136'], name="samp_loc_corr_rate", curie=MIXS.curie('0000136'),
                   model_uri=NMDC.samp_loc_corr_rate, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_mat_process = Slot(uri=MIXS['0000016'], name="samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=NMDC.samp_mat_process, domain=None, range=Optional[Union[dict, ControlledTermValue]])

slots.samp_md = Slot(uri=MIXS['0000413'], name="samp_md", curie=MIXS.curie('0000413'),
                   model_uri=NMDC.samp_md, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samp_name = Slot(uri=MIXS['0001107'], name="samp_name", curie=MIXS.curie('0001107'),
                   model_uri=NMDC.samp_name, domain=None, range=Optional[str])

slots.samp_preserv = Slot(uri=MIXS['0000463'], name="samp_preserv", curie=MIXS.curie('0000463'),
                   model_uri=NMDC.samp_preserv, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_room_id = Slot(uri=MIXS['0000244'], name="samp_room_id", curie=MIXS.curie('0000244'),
                   model_uri=NMDC.samp_room_id, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_size = Slot(uri=MIXS['0000001'], name="samp_size", curie=MIXS.curie('0000001'),
                   model_uri=NMDC.samp_size, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samp_sort_meth = Slot(uri=MIXS['0000216'], name="samp_sort_meth", curie=MIXS.curie('0000216'),
                   model_uri=NMDC.samp_sort_meth, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.samp_store_dur = Slot(uri=MIXS['0000116'], name="samp_store_dur", curie=MIXS.curie('0000116'),
                   model_uri=NMDC.samp_store_dur, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_store_loc = Slot(uri=MIXS['0000755'], name="samp_store_loc", curie=MIXS.curie('0000755'),
                   model_uri=NMDC.samp_store_loc, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_store_temp = Slot(uri=MIXS['0000110'], name="samp_store_temp", curie=MIXS.curie('0000110'),
                   model_uri=NMDC.samp_store_temp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samp_subtype = Slot(uri=MIXS['0000999'], name="samp_subtype", curie=MIXS.curie('0000999'),
                   model_uri=NMDC.samp_subtype, domain=None, range=Optional[Union[str, "SampSubtypeEnum"]])

slots.samp_taxon_id = Slot(uri=MIXS['0001320'], name="samp_taxon_id", curie=MIXS.curie('0001320'),
                   model_uri=NMDC.samp_taxon_id, domain=None, range=Optional[Union[dict, ControlledIdentifiedTermValue]])

slots.samp_time_out = Slot(uri=MIXS['0000196'], name="samp_time_out", curie=MIXS.curie('0000196'),
                   model_uri=NMDC.samp_time_out, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_transport_cond = Slot(uri=MIXS['0000410'], name="samp_transport_cond", curie=MIXS.curie('0000410'),
                   model_uri=NMDC.samp_transport_cond, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_tvdss = Slot(uri=MIXS['0000409'], name="samp_tvdss", curie=MIXS.curie('0000409'),
                   model_uri=NMDC.samp_tvdss, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_type = Slot(uri=MIXS['0000998'], name="samp_type", curie=MIXS.curie('0000998'),
                   model_uri=NMDC.samp_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_vol_we_dna_ext = Slot(uri=MIXS['0000111'], name="samp_vol_we_dna_ext", curie=MIXS.curie('0000111'),
                   model_uri=NMDC.samp_vol_we_dna_ext, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samp_weather = Slot(uri=MIXS['0000827'], name="samp_weather", curie=MIXS.curie('0000827'),
                   model_uri=NMDC.samp_weather, domain=None, range=Optional[Union[str, "SampWeatherEnum"]])

slots.samp_well_name = Slot(uri=MIXS['0000296'], name="samp_well_name", curie=MIXS.curie('0000296'),
                   model_uri=NMDC.samp_well_name, domain=None, range=Optional[Union[dict, TextValue]])

slots.saturates_pc = Slot(uri=MIXS['0000131'], name="saturates_pc", curie=MIXS.curie('0000131'),
                   model_uri=NMDC.saturates_pc, domain=None, range=Optional[Union[dict, TextValue]])

slots.season = Slot(uri=MIXS['0000829'], name="season", curie=MIXS.curie('0000829'),
                   model_uri=NMDC.season, domain=None, range=Optional[Union[dict, TextValue]])

slots.season_environment = Slot(uri=MIXS['0001068'], name="season_environment", curie=MIXS.curie('0001068'),
                   model_uri=NMDC.season_environment, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.season_precpt = Slot(uri=MIXS['0000645'], name="season_precpt", curie=MIXS.curie('0000645'),
                   model_uri=NMDC.season_precpt, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.season_temp = Slot(uri=MIXS['0000643'], name="season_temp", curie=MIXS.curie('0000643'),
                   model_uri=NMDC.season_temp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.season_use = Slot(uri=MIXS['0000830'], name="season_use", curie=MIXS.curie('0000830'),
                   model_uri=NMDC.season_use, domain=None, range=Optional[Union[str, "SeasonUseEnum"]])

slots.secondary_treatment = Slot(uri=MIXS['0000351'], name="secondary_treatment", curie=MIXS.curie('0000351'),
                   model_uri=NMDC.secondary_treatment, domain=None, range=Optional[Union[dict, TextValue]])

slots.sediment_type = Slot(uri=MIXS['0001078'], name="sediment_type", curie=MIXS.curie('0001078'),
                   model_uri=NMDC.sediment_type, domain=None, range=Optional[Union[str, "SedimentTypeEnum"]])

slots.seq_meth = Slot(uri=MIXS['0000050'], name="seq_meth", curie=MIXS.curie('0000050'),
                   model_uri=NMDC.seq_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.seq_quality_check = Slot(uri=MIXS['0000051'], name="seq_quality_check", curie=MIXS.curie('0000051'),
                   model_uri=NMDC.seq_quality_check, domain=None, range=Optional[Union[dict, TextValue]])

slots.sewage_type = Slot(uri=MIXS['0000215'], name="sewage_type", curie=MIXS.curie('0000215'),
                   model_uri=NMDC.sewage_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.shad_dev_water_mold = Slot(uri=MIXS['0000834'], name="shad_dev_water_mold", curie=MIXS.curie('0000834'),
                   model_uri=NMDC.shad_dev_water_mold, domain=None, range=Optional[str])

slots.shading_device_cond = Slot(uri=MIXS['0000831'], name="shading_device_cond", curie=MIXS.curie('0000831'),
                   model_uri=NMDC.shading_device_cond, domain=None, range=Optional[Union[str, "ShadingDeviceCondEnum"]])

slots.shading_device_loc = Slot(uri=MIXS['0000832'], name="shading_device_loc", curie=MIXS.curie('0000832'),
                   model_uri=NMDC.shading_device_loc, domain=None, range=Optional[Union[dict, TextValue]])

slots.shading_device_mat = Slot(uri=MIXS['0000245'], name="shading_device_mat", curie=MIXS.curie('0000245'),
                   model_uri=NMDC.shading_device_mat, domain=None, range=Optional[Union[dict, TextValue]])

slots.shading_device_type = Slot(uri=MIXS['0000835'], name="shading_device_type", curie=MIXS.curie('0000835'),
                   model_uri=NMDC.shading_device_type, domain=None, range=Optional[Union[str, "ShadingDeviceTypeEnum"]])

slots.sieving = Slot(uri=MIXS['0000322'], name="sieving", curie=MIXS.curie('0000322'),
                   model_uri=NMDC.sieving, domain=None, range=Optional[Union[dict, TextValue]])

slots.silicate = Slot(uri=MIXS['0000184'], name="silicate", curie=MIXS.curie('0000184'),
                   model_uri=NMDC.silicate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.size_frac = Slot(uri=MIXS['0000017'], name="size_frac", curie=MIXS.curie('0000017'),
                   model_uri=NMDC.size_frac, domain=None, range=Optional[Union[dict, TextValue]])

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
                   model_uri=NMDC.soluble_inorg_mat, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.soluble_org_mat = Slot(uri=MIXS['0000673'], name="soluble_org_mat", curie=MIXS.curie('0000673'),
                   model_uri=NMDC.soluble_org_mat, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.soluble_react_phosp = Slot(uri=MIXS['0000738'], name="soluble_react_phosp", curie=MIXS.curie('0000738'),
                   model_uri=NMDC.soluble_react_phosp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.source_mat_id = Slot(uri=MIXS['0000026'], name="source_mat_id", curie=MIXS.curie('0000026'),
                   model_uri=NMDC.source_mat_id, domain=None, range=Optional[Union[dict, TextValue]])

slots.space_typ_state = Slot(uri=MIXS['0000770'], name="space_typ_state", curie=MIXS.curie('0000770'),
                   model_uri=NMDC.space_typ_state, domain=None, range=Optional[Union[dict, TextValue]])

slots.specific = Slot(uri=MIXS['0000836'], name="specific", curie=MIXS.curie('0000836'),
                   model_uri=NMDC.specific, domain=None, range=Optional[Union[str, "SpecificEnum"]])

slots.specific_humidity = Slot(uri=MIXS['0000214'], name="specific_humidity", curie=MIXS.curie('0000214'),
                   model_uri=NMDC.specific_humidity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.sr_dep_env = Slot(uri=MIXS['0000996'], name="sr_dep_env", curie=MIXS.curie('0000996'),
                   model_uri=NMDC.sr_dep_env, domain=None, range=Optional[Union[str, "SrDepEnvEnum"]])

slots.sr_geol_age = Slot(uri=MIXS['0000997'], name="sr_geol_age", curie=MIXS.curie('0000997'),
                   model_uri=NMDC.sr_geol_age, domain=None, range=Optional[Union[str, "SrGeolAgeEnum"]])

slots.sr_kerog_type = Slot(uri=MIXS['0000994'], name="sr_kerog_type", curie=MIXS.curie('0000994'),
                   model_uri=NMDC.sr_kerog_type, domain=None, range=Optional[Union[str, "SrKerogTypeEnum"]])

slots.sr_lithology = Slot(uri=MIXS['0000995'], name="sr_lithology", curie=MIXS.curie('0000995'),
                   model_uri=NMDC.sr_lithology, domain=None, range=Optional[Union[str, "SrLithologyEnum"]])

slots.standing_water_regm = Slot(uri=MIXS['0001069'], name="standing_water_regm", curie=MIXS.curie('0001069'),
                   model_uri=NMDC.standing_water_regm, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.store_cond = Slot(uri=MIXS['0000327'], name="store_cond", curie=MIXS.curie('0000327'),
                   model_uri=NMDC.store_cond, domain=None, range=Optional[Union[dict, TextValue]])

slots.substructure_type = Slot(uri=MIXS['0000767'], name="substructure_type", curie=MIXS.curie('0000767'),
                   model_uri=NMDC.substructure_type, domain=None, range=Optional[Union[Union[str, "SubstructureTypeEnum"], List[Union[str, "SubstructureTypeEnum"]]]])

slots.sulfate = Slot(uri=MIXS['0000423'], name="sulfate", curie=MIXS.curie('0000423'),
                   model_uri=NMDC.sulfate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.sulfate_fw = Slot(uri=MIXS['0000407'], name="sulfate_fw", curie=MIXS.curie('0000407'),
                   model_uri=NMDC.sulfate_fw, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.sulfide = Slot(uri=MIXS['0000424'], name="sulfide", curie=MIXS.curie('0000424'),
                   model_uri=NMDC.sulfide, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.surf_air_cont = Slot(uri=MIXS['0000759'], name="surf_air_cont", curie=MIXS.curie('0000759'),
                   model_uri=NMDC.surf_air_cont, domain=None, range=Optional[Union[Union[str, "SurfAirContEnum"], List[Union[str, "SurfAirContEnum"]]]])

slots.surf_humidity = Slot(uri=MIXS['0000123'], name="surf_humidity", curie=MIXS.curie('0000123'),
                   model_uri=NMDC.surf_humidity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.surf_material = Slot(uri=MIXS['0000758'], name="surf_material", curie=MIXS.curie('0000758'),
                   model_uri=NMDC.surf_material, domain=None, range=Optional[Union[str, "SurfMaterialEnum"]])

slots.surf_moisture = Slot(uri=MIXS['0000128'], name="surf_moisture", curie=MIXS.curie('0000128'),
                   model_uri=NMDC.surf_moisture, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.surf_moisture_ph = Slot(uri=MIXS['0000760'], name="surf_moisture_ph", curie=MIXS.curie('0000760'),
                   model_uri=NMDC.surf_moisture_ph, domain=None, range=Optional[float])

slots.surf_temp = Slot(uri=MIXS['0000125'], name="surf_temp", curie=MIXS.curie('0000125'),
                   model_uri=NMDC.surf_temp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.suspend_part_matter = Slot(uri=MIXS['0000741'], name="suspend_part_matter", curie=MIXS.curie('0000741'),
                   model_uri=NMDC.suspend_part_matter, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.suspend_solids = Slot(uri=MIXS['0000150'], name="suspend_solids", curie=MIXS.curie('0000150'),
                   model_uri=NMDC.suspend_solids, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

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

slots.tidal_stage = Slot(uri=MIXS['0000750'], name="tidal_stage", curie=MIXS.curie('0000750'),
                   model_uri=NMDC.tidal_stage, domain=None, range=Optional[Union[str, "TidalStageEnum"]])

slots.tillage = Slot(uri=MIXS['0001081'], name="tillage", curie=MIXS.curie('0001081'),
                   model_uri=NMDC.tillage, domain=None, range=Optional[Union[Union[str, "TillageEnum"], List[Union[str, "TillageEnum"]]]])

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
                   model_uri=NMDC.train_line, domain=None, range=Optional[Union[str, "TrainLineEnum"]])

slots.train_stat_loc = Slot(uri=MIXS['0000838'], name="train_stat_loc", curie=MIXS.curie('0000838'),
                   model_uri=NMDC.train_stat_loc, domain=None, range=Optional[Union[str, "TrainStatLocEnum"]])

slots.train_stop_loc = Slot(uri=MIXS['0000839'], name="train_stop_loc", curie=MIXS.curie('0000839'),
                   model_uri=NMDC.train_stop_loc, domain=None, range=Optional[Union[str, "TrainStopLocEnum"]])

slots.turbidity = Slot(uri=MIXS['0000191'], name="turbidity", curie=MIXS.curie('0000191'),
                   model_uri=NMDC.turbidity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tvdss_of_hcr_press = Slot(uri=MIXS['0000397'], name="tvdss_of_hcr_press", curie=MIXS.curie('0000397'),
                   model_uri=NMDC.tvdss_of_hcr_press, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tvdss_of_hcr_temp = Slot(uri=MIXS['0000394'], name="tvdss_of_hcr_temp", curie=MIXS.curie('0000394'),
                   model_uri=NMDC.tvdss_of_hcr_temp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.typ_occup_density = Slot(uri=MIXS['0000771'], name="typ_occup_density", curie=MIXS.curie('0000771'),
                   model_uri=NMDC.typ_occup_density, domain=None, range=Optional[float])

slots.ventilation_rate = Slot(uri=MIXS['0000114'], name="ventilation_rate", curie=MIXS.curie('0000114'),
                   model_uri=NMDC.ventilation_rate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.ventilation_type = Slot(uri=MIXS['0000756'], name="ventilation_type", curie=MIXS.curie('0000756'),
                   model_uri=NMDC.ventilation_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.vfa = Slot(uri=MIXS['0000152'], name="vfa", curie=MIXS.curie('0000152'),
                   model_uri=NMDC.vfa, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.vfa_fw = Slot(uri=MIXS['0000408'], name="vfa_fw", curie=MIXS.curie('0000408'),
                   model_uri=NMDC.vfa_fw, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.vis_media = Slot(uri=MIXS['0000840'], name="vis_media", curie=MIXS.curie('0000840'),
                   model_uri=NMDC.vis_media, domain=None, range=Optional[Union[str, "VisMediaEnum"]])

slots.viscosity = Slot(uri=MIXS['0000126'], name="viscosity", curie=MIXS.curie('0000126'),
                   model_uri=NMDC.viscosity, domain=None, range=Optional[Union[dict, TextValue]])

slots.volatile_org_comp = Slot(uri=MIXS['0000115'], name="volatile_org_comp", curie=MIXS.curie('0000115'),
                   model_uri=NMDC.volatile_org_comp, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.wall_area = Slot(uri=MIXS['0000198'], name="wall_area", curie=MIXS.curie('0000198'),
                   model_uri=NMDC.wall_area, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.wall_const_type = Slot(uri=MIXS['0000841'], name="wall_const_type", curie=MIXS.curie('0000841'),
                   model_uri=NMDC.wall_const_type, domain=None, range=Optional[Union[str, "WallConstTypeEnum"]])

slots.wall_finish_mat = Slot(uri=MIXS['0000842'], name="wall_finish_mat", curie=MIXS.curie('0000842'),
                   model_uri=NMDC.wall_finish_mat, domain=None, range=Optional[Union[str, "WallFinishMatEnum"]])

slots.wall_height = Slot(uri=MIXS['0000221'], name="wall_height", curie=MIXS.curie('0000221'),
                   model_uri=NMDC.wall_height, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.wall_loc = Slot(uri=MIXS['0000843'], name="wall_loc", curie=MIXS.curie('0000843'),
                   model_uri=NMDC.wall_loc, domain=None, range=Optional[Union[str, "WallLocEnum"]])

slots.wall_surf_treatment = Slot(uri=MIXS['0000845'], name="wall_surf_treatment", curie=MIXS.curie('0000845'),
                   model_uri=NMDC.wall_surf_treatment, domain=None, range=Optional[Union[str, "WallSurfTreatmentEnum"]])

slots.wall_texture = Slot(uri=MIXS['0000846'], name="wall_texture", curie=MIXS.curie('0000846'),
                   model_uri=NMDC.wall_texture, domain=None, range=Optional[Union[str, "WallTextureEnum"]])

slots.wall_thermal_mass = Slot(uri=MIXS['0000222'], name="wall_thermal_mass", curie=MIXS.curie('0000222'),
                   model_uri=NMDC.wall_thermal_mass, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.wall_water_mold = Slot(uri=MIXS['0000844'], name="wall_water_mold", curie=MIXS.curie('0000844'),
                   model_uri=NMDC.wall_water_mold, domain=None, range=Optional[Union[dict, TextValue]])

slots.wastewater_type = Slot(uri=MIXS['0000353'], name="wastewater_type", curie=MIXS.curie('0000353'),
                   model_uri=NMDC.wastewater_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.water_cont_soil_meth = Slot(uri=MIXS['0000323'], name="water_cont_soil_meth", curie=MIXS.curie('0000323'),
                   model_uri=NMDC.water_cont_soil_meth, domain=None, range=Optional[str])

slots.water_content = Slot(uri=MIXS['0000185'], name="water_content", curie=MIXS.curie('0000185'),
                   model_uri=NMDC.water_content, domain=None, range=Optional[str])

slots.water_current = Slot(uri=MIXS['0000203'], name="water_current", curie=MIXS.curie('0000203'),
                   model_uri=NMDC.water_current, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.water_cut = Slot(uri=MIXS['0000454'], name="water_cut", curie=MIXS.curie('0000454'),
                   model_uri=NMDC.water_cut, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.water_feat_size = Slot(uri=MIXS['0000223'], name="water_feat_size", curie=MIXS.curie('0000223'),
                   model_uri=NMDC.water_feat_size, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.water_feat_type = Slot(uri=MIXS['0000847'], name="water_feat_type", curie=MIXS.curie('0000847'),
                   model_uri=NMDC.water_feat_type, domain=None, range=Optional[Union[str, "WaterFeatTypeEnum"]])

slots.water_prod_rate = Slot(uri=MIXS['0000453'], name="water_prod_rate", curie=MIXS.curie('0000453'),
                   model_uri=NMDC.water_prod_rate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.water_temp_regm = Slot(uri=MIXS['0000590'], name="water_temp_regm", curie=MIXS.curie('0000590'),
                   model_uri=NMDC.water_temp_regm, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.watering_regm = Slot(uri=MIXS['0000591'], name="watering_regm", curie=MIXS.curie('0000591'),
                   model_uri=NMDC.watering_regm, domain=None, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.weekday = Slot(uri=MIXS['0000848'], name="weekday", curie=MIXS.curie('0000848'),
                   model_uri=NMDC.weekday, domain=None, range=Optional[Union[str, "WeekdayEnum"]])

slots.win = Slot(uri=MIXS['0000297'], name="win", curie=MIXS.curie('0000297'),
                   model_uri=NMDC.win, domain=None, range=Optional[Union[dict, TextValue]])

slots.wind_direction = Slot(uri=MIXS['0000757'], name="wind_direction", curie=MIXS.curie('0000757'),
                   model_uri=NMDC.wind_direction, domain=None, range=Optional[Union[dict, TextValue]])

slots.wind_speed = Slot(uri=MIXS['0000118'], name="wind_speed", curie=MIXS.curie('0000118'),
                   model_uri=NMDC.wind_speed, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.window_cond = Slot(uri=MIXS['0000849'], name="window_cond", curie=MIXS.curie('0000849'),
                   model_uri=NMDC.window_cond, domain=None, range=Optional[Union[str, "WindowCondEnum"]])

slots.window_cover = Slot(uri=MIXS['0000850'], name="window_cover", curie=MIXS.curie('0000850'),
                   model_uri=NMDC.window_cover, domain=None, range=Optional[Union[str, "WindowCoverEnum"]])

slots.window_horiz_pos = Slot(uri=MIXS['0000851'], name="window_horiz_pos", curie=MIXS.curie('0000851'),
                   model_uri=NMDC.window_horiz_pos, domain=None, range=Optional[Union[str, "WindowHorizPosEnum"]])

slots.window_loc = Slot(uri=MIXS['0000852'], name="window_loc", curie=MIXS.curie('0000852'),
                   model_uri=NMDC.window_loc, domain=None, range=Optional[Union[str, "WindowLocEnum"]])

slots.window_mat = Slot(uri=MIXS['0000853'], name="window_mat", curie=MIXS.curie('0000853'),
                   model_uri=NMDC.window_mat, domain=None, range=Optional[Union[str, "WindowMatEnum"]])

slots.window_open_freq = Slot(uri=MIXS['0000246'], name="window_open_freq", curie=MIXS.curie('0000246'),
                   model_uri=NMDC.window_open_freq, domain=None, range=Optional[Union[dict, TextValue]])

slots.window_size = Slot(uri=MIXS['0000224'], name="window_size", curie=MIXS.curie('0000224'),
                   model_uri=NMDC.window_size, domain=None, range=Optional[Union[dict, TextValue]])

slots.window_status = Slot(uri=MIXS['0000855'], name="window_status", curie=MIXS.curie('0000855'),
                   model_uri=NMDC.window_status, domain=None, range=Optional[Union[dict, TextValue]])

slots.window_type = Slot(uri=MIXS['0000856'], name="window_type", curie=MIXS.curie('0000856'),
                   model_uri=NMDC.window_type, domain=None, range=Optional[Union[str, "WindowTypeEnum"]])

slots.window_vert_pos = Slot(uri=MIXS['0000857'], name="window_vert_pos", curie=MIXS.curie('0000857'),
                   model_uri=NMDC.window_vert_pos, domain=None, range=Optional[Union[str, "WindowVertPosEnum"]])

slots.window_water_mold = Slot(uri=MIXS['0000854'], name="window_water_mold", curie=MIXS.curie('0000854'),
                   model_uri=NMDC.window_water_mold, domain=None, range=Optional[Union[dict, TextValue]])

slots.xylene = Slot(uri=MIXS['0000156'], name="xylene", curie=MIXS.curie('0000156'),
                   model_uri=NMDC.xylene, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.core_field = Slot(uri=NMDC.core_field, name="core field", curie=NMDC.curie('core_field'),
                   model_uri=NMDC.core_field, domain=None, range=Optional[str])

slots.environment_field = Slot(uri=NMDC.environment_field, name="environment field", curie=NMDC.curie('environment_field'),
                   model_uri=NMDC.environment_field, domain=None, range=Optional[str])

slots.investigation_field = Slot(uri=NMDC.investigation_field, name="investigation field", curie=NMDC.curie('investigation_field'),
                   model_uri=NMDC.investigation_field, domain=None, range=Optional[str])

slots.nucleic_acid_sequence_source_field = Slot(uri=NMDC.nucleic_acid_sequence_source_field, name="nucleic acid sequence source field", curie=NMDC.curie('nucleic_acid_sequence_source_field'),
                   model_uri=NMDC.nucleic_acid_sequence_source_field, domain=None, range=Optional[str])

slots.sequencing_field = Slot(uri=NMDC.sequencing_field, name="sequencing field", curie=NMDC.curie('sequencing_field'),
                   model_uri=NMDC.sequencing_field, domain=None, range=Optional[str])

slots.associated_studies = Slot(uri=NMDC.associated_studies, name="associated_studies", curie=NMDC.curie('associated_studies'),
                   model_uri=NMDC.associated_studies, domain=None, range=Union[Union[str, StudyId], List[Union[str, StudyId]]],
                   pattern=re.compile(r'^(nmdc):sty-([0-9][a-z]{0,6}[0-9])-([A-Za-z0-9]{1,})$'))

slots.part_of = Slot(uri=DCTERMS.isPartOf, name="part_of", curie=DCTERMS.curie('isPartOf'),
                   model_uri=NMDC.part_of, domain=None, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.was_informed_by = Slot(uri=NMDC.was_informed_by, name="was_informed_by", curie=NMDC.curie('was_informed_by'),
                   model_uri=NMDC.was_informed_by, domain=None, range=Optional[Union[str, DataGenerationId]], mappings = [PROV["wasInformedBy"]])

slots.principal_investigator = Slot(uri=NMDC.principal_investigator, name="principal_investigator", curie=NMDC.curie('principal_investigator'),
                   model_uri=NMDC.principal_investigator, domain=None, range=Optional[Union[dict, PersonValue]])

slots.was_generated_by = Slot(uri=NMDC.was_generated_by, name="was_generated_by", curie=NMDC.curie('was_generated_by'),
                   model_uri=NMDC.was_generated_by, domain=None, range=Optional[Union[str, WorkflowExecutionId]], mappings = [PROV["wasGeneratedBy"]])

slots.associated_dois = Slot(uri=NMDC.associated_dois, name="associated_dois", curie=NMDC.curie('associated_dois'),
                   model_uri=NMDC.associated_dois, domain=None, range=Optional[Union[Union[dict, Doi], List[Union[dict, Doi]]]])

slots.has_credit_associations = Slot(uri=PROV.qualifiedAssociation, name="has_credit_associations", curie=PROV.curie('qualifiedAssociation'),
                   model_uri=NMDC.has_credit_associations, domain=None, range=Optional[Union[Union[dict, CreditAssociation], List[Union[dict, CreditAssociation]]]])

slots.protocol_link = Slot(uri=NMDC.protocol_link, name="protocol_link", curie=NMDC.curie('protocol_link'),
                   model_uri=NMDC.protocol_link, domain=None, range=Optional[Union[dict, Protocol]])

slots.study_category = Slot(uri=NMDC.study_category, name="study_category", curie=NMDC.curie('study_category'),
                   model_uri=NMDC.study_category, domain=None, range=Union[str, "StudyCategoryEnum"])

slots.study_image = Slot(uri=NMDC.study_image, name="study_image", curie=NMDC.curie('study_image'),
                   model_uri=NMDC.study_image, domain=None, range=Optional[Union[Union[dict, ImageValue], List[Union[dict, ImageValue]]]])

slots.applies_to_person = Slot(uri=NMDC.applies_to_person, name="applies_to_person", curie=NMDC.curie('applies_to_person'),
                   model_uri=NMDC.applies_to_person, domain=None, range=Union[dict, PersonValue])

slots.applied_roles = Slot(uri=NMDC.applied_roles, name="applied_roles", curie=NMDC.curie('applied_roles'),
                   model_uri=NMDC.applied_roles, domain=None, range=Union[Union[str, "CreditEnum"], List[Union[str, "CreditEnum"]]])

slots.has_input = Slot(uri=NMDC.has_input, name="has_input", curie=NMDC.curie('has_input'),
                   model_uri=NMDC.has_input, domain=None, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_output = Slot(uri=NMDC.has_output, name="has_output", curie=NMDC.curie('has_output'),
                   model_uri=NMDC.has_output, domain=None, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.instrument_used = Slot(uri=NMDC.instrument_used, name="instrument_used", curie=NMDC.curie('instrument_used'),
                   model_uri=NMDC.instrument_used, domain=None, range=Optional[Union[Union[str, InstrumentId], List[Union[str, InstrumentId]]]])

slots.model = Slot(uri=NMDC.model, name="model", curie=NMDC.curie('model'),
                   model_uri=NMDC.model, domain=None, range=Optional[Union[str, "InstrumentModelEnum"]])

slots.vendor = Slot(uri=NMDC.vendor, name="vendor", curie=NMDC.curie('vendor'),
                   model_uri=NMDC.vendor, domain=None, range=Optional[Union[str, "InstrumentVendorEnum"]])

slots.has_failure_categorization = Slot(uri=NMDC.has_failure_categorization, name="has_failure_categorization", curie=NMDC.curie('has_failure_categorization'),
                   model_uri=NMDC.has_failure_categorization, domain=None, range=Optional[Union[Union[dict, FailureCategorization], List[Union[dict, FailureCategorization]]]])

slots.qc_failure_where = Slot(uri=NMDC.qc_failure_where, name="qc_failure_where", curie=NMDC.curie('qc_failure_where'),
                   model_uri=NMDC.qc_failure_where, domain=None, range=Optional[Union[str, "FailureWhereEnum"]])

slots.qc_failure_what = Slot(uri=NMDC.qc_failure_what, name="qc_failure_what", curie=NMDC.curie('qc_failure_what'),
                   model_uri=NMDC.qc_failure_what, domain=None, range=Optional[Union[str, "FailureWhatEnum"]])

slots.qc_comment = Slot(uri=NMDC.qc_comment, name="qc_comment", curie=NMDC.curie('qc_comment'),
                   model_uri=NMDC.qc_comment, domain=None, range=Optional[str])

slots.objective = Slot(uri=NMDC.objective, name="objective", curie=NMDC.curie('objective'),
                   model_uri=NMDC.objective, domain=None, range=Optional[str], mappings = [SIO["000337"]])

slots.md5_checksum = Slot(uri=NMDC.md5_checksum, name="md5_checksum", curie=NMDC.curie('md5_checksum'),
                   model_uri=NMDC.md5_checksum, domain=None, range=Optional[str])

slots.data_object_type = Slot(uri=NMDC.data_object_type, name="data_object_type", curie=NMDC.curie('data_object_type'),
                   model_uri=NMDC.data_object_type, domain=None, range=Optional[Union[str, "FileTypeEnum"]])

slots.data_category = Slot(uri=NMDC.data_category, name="data_category", curie=NMDC.curie('data_category'),
                   model_uri=NMDC.data_category, domain=None, range=Optional[Union[str, "DataCategoryEnum"]])

slots.compression_type = Slot(uri=NMDC.compression_type, name="compression_type", curie=NMDC.curie('compression_type'),
                   model_uri=NMDC.compression_type, domain=None, range=Optional[str])

slots.started_at_time = Slot(uri=NMDC.started_at_time, name="started_at_time", curie=NMDC.curie('started_at_time'),
                   model_uri=NMDC.started_at_time, domain=None, range=Optional[str], mappings = [PROV["startedAtTime"]],
                   pattern=re.compile(r'^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$'))

slots.ended_at_time = Slot(uri=NMDC.ended_at_time, name="ended_at_time", curie=NMDC.curie('ended_at_time'),
                   model_uri=NMDC.ended_at_time, domain=None, range=Optional[str], mappings = [PROV["endedAtTime"]],
                   pattern=re.compile(r'^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$'))

slots.git_url = Slot(uri=NMDC.git_url, name="git_url", curie=NMDC.curie('git_url'),
                   model_uri=NMDC.git_url, domain=None, range=Optional[str])

slots.execution_resource = Slot(uri=NMDC.execution_resource, name="execution_resource", curie=NMDC.curie('execution_resource'),
                   model_uri=NMDC.execution_resource, domain=None, range=Optional[Union[str, "ExecutionResourceEnum"]])

slots.websites = Slot(uri=NMDC.websites, name="websites", curie=NMDC.curie('websites'),
                   model_uri=NMDC.websites, domain=None, range=Optional[Union[str, List[str]]],
                   pattern=re.compile(r'^[Hh][Tt][Tt][Pp][Ss]?:\/\/(?!.*[Dd][Oo][Ii]\.[Oo][Rr][Gg]).*$'))

slots.homepage_website = Slot(uri=NMDC.homepage_website, name="homepage_website", curie=NMDC.curie('homepage_website'),
                   model_uri=NMDC.homepage_website, domain=None, range=Optional[Union[str, List[str]]],
                   pattern=re.compile(r'^[Hh][Tt][Tt][Pp][Ss]?:\/\/(?!.*[Dd][Oo][Ii]\.[Oo][Rr][Gg]).*$'))

slots.profile_image_url = Slot(uri=NMDC.profile_image_url, name="profile_image_url", curie=NMDC.curie('profile_image_url'),
                   model_uri=NMDC.profile_image_url, domain=None, range=Optional[str])

slots.orcid = Slot(uri=NMDC.orcid, name="orcid", curie=NMDC.curie('orcid'),
                   model_uri=NMDC.orcid, domain=None, range=Optional[str])

slots.email = Slot(uri=SCHEMA.email, name="email", curie=SCHEMA.curie('email'),
                   model_uri=NMDC.email, domain=None, range=Optional[str])

slots.display_order = Slot(uri=NMDC.display_order, name="display_order", curie=NMDC.curie('display_order'),
                   model_uri=NMDC.display_order, domain=None, range=Optional[int])

slots.url = Slot(uri=NMDC.url, name="url", curie=NMDC.curie('url'),
                   model_uri=NMDC.url, domain=None, range=Optional[str])

slots.language = Slot(uri=NMDC.language, name="language", curie=NMDC.curie('language'),
                   model_uri=NMDC.language, domain=None, range=Optional[str])

slots.has_raw_value = Slot(uri=NMDC.has_raw_value, name="has_raw_value", curie=NMDC.curie('has_raw_value'),
                   model_uri=NMDC.has_raw_value, domain=None, range=Optional[str])

slots.has_unit = Slot(uri=NMDC.has_unit, name="has_unit", curie=NMDC.curie('has_unit'),
                   model_uri=NMDC.has_unit, domain=None, range=Optional[str], mappings = [QUD["unit"], SCHEMA["unitCode"]])

slots.has_numeric_value = Slot(uri=NMDC.has_numeric_value, name="has_numeric_value", curie=NMDC.curie('has_numeric_value'),
                   model_uri=NMDC.has_numeric_value, domain=None, range=Optional[Decimal], mappings = [QUD["quantityValue"], SCHEMA["value"]])

slots.has_minimum_numeric_value = Slot(uri=NMDC.has_minimum_numeric_value, name="has_minimum_numeric_value", curie=NMDC.curie('has_minimum_numeric_value'),
                   model_uri=NMDC.has_minimum_numeric_value, domain=None, range=Optional[Decimal])

slots.has_maximum_numeric_value = Slot(uri=NMDC.has_maximum_numeric_value, name="has_maximum_numeric_value", curie=NMDC.curie('has_maximum_numeric_value'),
                   model_uri=NMDC.has_maximum_numeric_value, domain=None, range=Optional[Decimal])

slots.has_boolean_value = Slot(uri=NMDC.has_boolean_value, name="has_boolean_value", curie=NMDC.curie('has_boolean_value'),
                   model_uri=NMDC.has_boolean_value, domain=None, range=Optional[Union[bool, Bool]])

slots.latitude = Slot(uri=WGS84.lat, name="latitude", curie=WGS84.curie('lat'),
                   model_uri=NMDC.latitude, domain=None, range=Optional[float], mappings = [SCHEMA["latitude"]])

slots.longitude = Slot(uri=WGS84.long, name="longitude", curie=WGS84.curie('long'),
                   model_uri=NMDC.longitude, domain=None, range=Optional[float], mappings = [SCHEMA["longitude"]])

slots.infiltrations = Slot(uri=NMDC.infiltrations, name="infiltrations", curie=NMDC.curie('infiltrations'),
                   model_uri=NMDC.infiltrations, domain=None, range=Optional[Union[str, List[str]]],
                   pattern=re.compile(r'^(?:[0-9]|[1-9][0-9]|9[0-9]|0[0-9]|0[0-5][0-9]):[0-5][0-9]:[0-5][0-9]$'))

slots.soluble_iron_micromol = Slot(uri=NMDC.soluble_iron_micromol, name="soluble_iron_micromol", curie=NMDC.curie('soluble_iron_micromol'),
                   model_uri=NMDC.soluble_iron_micromol, domain=None, range=Optional[str])

slots.sample_collection_site = Slot(uri=NMDC.sample_collection_site, name="sample_collection_site", curie=NMDC.curie('sample_collection_site'),
                   model_uri=NMDC.sample_collection_site, domain=None, range=Optional[str])

slots.salinity_category = Slot(uri=NMDC.salinity_category, name="salinity_category", curie=NMDC.curie('salinity_category'),
                   model_uri=NMDC.salinity_category, domain=None, range=Optional[str])

slots.proport_woa_temperature = Slot(uri=NMDC.proport_woa_temperature, name="proport_woa_temperature", curie=NMDC.curie('proport_woa_temperature'),
                   model_uri=NMDC.proport_woa_temperature, domain=None, range=Optional[str])

slots.location = Slot(uri=NMDC.location, name="location", curie=NMDC.curie('location'),
                   model_uri=NMDC.location, domain=None, range=Optional[str])

slots.host_name = Slot(uri=NMDC.host_name, name="host_name", curie=NMDC.curie('host_name'),
                   model_uri=NMDC.host_name, domain=None, range=Optional[str])

slots.community = Slot(uri=NMDC.community, name="community", curie=NMDC.curie('community'),
                   model_uri=NMDC.community, domain=None, range=Optional[str])

slots.embargoed = Slot(uri=NMDC.embargoed, name="embargoed", curie=NMDC.curie('embargoed'),
                   model_uri=NMDC.embargoed, domain=None, range=Optional[Union[bool, Bool]])

slots.habitat = Slot(uri=NMDC.habitat, name="habitat", curie=NMDC.curie('habitat'),
                   model_uri=NMDC.habitat, domain=None, range=Optional[str])

slots.version = Slot(uri=NMDC.version, name="version", curie=NMDC.curie('version'),
                   model_uri=NMDC.version, domain=None, range=Optional[str])

slots.doi_value = Slot(uri=NMDC.doi_value, name="doi_value", curie=NMDC.curie('doi_value'),
                   model_uri=NMDC.doi_value, domain=None, range=Union[str, URIorCURIE],
                   pattern=re.compile(r'^doi:10.\d{2,9}/.*$'))

slots.doi_provider = Slot(uri=NMDC.doi_provider, name="doi_provider", curie=NMDC.curie('doi_provider'),
                   model_uri=NMDC.doi_provider, domain=None, range=Optional[Union[str, "DoiProviderEnum"]])

slots.doi_category = Slot(uri=NMDC.doi_category, name="doi_category", curie=NMDC.curie('doi_category'),
                   model_uri=NMDC.doi_category, domain=None, range=Union[str, "DoiCategoryEnum"])

slots.related_identifiers = Slot(uri=NMDC.related_identifiers, name="related_identifiers", curie=NMDC.curie('related_identifiers'),
                   model_uri=NMDC.related_identifiers, domain=None, range=Optional[str])

slots.notes = Slot(uri=NMDC.notes, name="notes", curie=NMDC.curie('notes'),
                   model_uri=NMDC.notes, domain=None, range=Optional[str])

slots.funding_sources = Slot(uri=NMDC.funding_sources, name="funding_sources", curie=NMDC.curie('funding_sources'),
                   model_uri=NMDC.funding_sources, domain=None, range=Optional[Union[str, List[str]]])

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

slots.add_date = Slot(uri=NMDC.add_date, name="add_date", curie=NMDC.curie('add_date'),
                   model_uri=NMDC.add_date, domain=None, range=Optional[str])

slots.mod_date = Slot(uri=NMDC.mod_date, name="mod_date", curie=NMDC.curie('mod_date'),
                   model_uri=NMDC.mod_date, domain=None, range=Optional[str])

slots.ncbi_taxonomy_name = Slot(uri=NMDC.ncbi_taxonomy_name, name="ncbi_taxonomy_name", curie=NMDC.curie('ncbi_taxonomy_name'),
                   model_uri=NMDC.ncbi_taxonomy_name, domain=None, range=Optional[str])

slots.ncbi_project_name = Slot(uri=NMDC.ncbi_project_name, name="ncbi_project_name", curie=NMDC.curie('ncbi_project_name'),
                   model_uri=NMDC.ncbi_project_name, domain=None, range=Optional[str])

slots.processing_institution = Slot(uri=NMDC.processing_institution, name="processing_institution", curie=NMDC.curie('processing_institution'),
                   model_uri=NMDC.processing_institution, domain=None, range=Optional[Union[str, "ProcessingInstitutionEnum"]])

slots.qc_status = Slot(uri=NMDC.qc_status, name="qc_status", curie=NMDC.curie('qc_status'),
                   model_uri=NMDC.qc_status, domain=None, range=Optional[Union[str, "StatusEnum"]])

slots.file_size_bytes = Slot(uri=NMDC.file_size_bytes, name="file_size_bytes", curie=NMDC.curie('file_size_bytes'),
                   model_uri=NMDC.file_size_bytes, domain=None, range=Optional[int])

slots.analyte_category = Slot(uri=NMDC.analyte_category, name="analyte_category", curie=NMDC.curie('analyte_category'),
                   model_uri=NMDC.analyte_category, domain=None, range=Union[str, "AnalyteCategoryEnum"])

slots.direct_infusion_category = Slot(uri=NMDC.direct_infusion_category, name="direct_infusion_category", curie=NMDC.curie('direct_infusion_category'),
                   model_uri=NMDC.direct_infusion_category, domain=None, range=Optional[Union[str, "DirectInfusionEnum"]])

slots.type = Slot(uri=RDF.type, name="type", curie=RDF.curie('type'),
                   model_uri=NMDC.type, domain=None, range=Union[str, URIorCURIE])

slots.external_database_identifiers = Slot(uri=NMDC.external_database_identifiers, name="external_database_identifiers", curie=NMDC.curie('external_database_identifiers'),
                   model_uri=NMDC.external_database_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$'))

slots.dna_concentration = Slot(uri=NMDC.dna_concentration, name="dna_concentration", curie=NMDC.curie('dna_concentration'),
                   model_uri=NMDC.dna_concentration, domain=None, range=Optional[float])

slots.extraction_targets = Slot(uri=NMDC.extraction_targets, name="extraction_targets", curie=NMDC.curie('extraction_targets'),
                   model_uri=NMDC.extraction_targets, domain=None, range=Optional[Union[Union[str, "ExtractionTargetEnum"], List[Union[str, "ExtractionTargetEnum"]]]])

slots.id = Slot(uri=NMDC.id, name="id", curie=NMDC.curie('id'),
                   model_uri=NMDC.id, domain=None, range=URIRef,
                   pattern=re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$'))

slots.name = Slot(uri=NMDC.name, name="name", curie=NMDC.curie('name'),
                   model_uri=NMDC.name, domain=None, range=Optional[str])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=NMDC.description, domain=None, range=Optional[str])

slots.title = Slot(uri=NMDC.title, name="title", curie=NMDC.curie('title'),
                   model_uri=NMDC.title, domain=None, range=Optional[str])

slots.alternative_titles = Slot(uri=NMDC.alternative_titles, name="alternative_titles", curie=NMDC.curie('alternative_titles'),
                   model_uri=NMDC.alternative_titles, domain=None, range=Optional[Union[str, List[str]]])

slots.alternative_names = Slot(uri=NMDC.alternative_names, name="alternative_names", curie=NMDC.curie('alternative_names'),
                   model_uri=NMDC.alternative_names, domain=None, range=Optional[Union[str, List[str]]])

slots.alternative_descriptions = Slot(uri=NMDC.alternative_descriptions, name="alternative_descriptions", curie=NMDC.curie('alternative_descriptions'),
                   model_uri=NMDC.alternative_descriptions, domain=None, range=Optional[Union[str, List[str]]])

slots.alternative_identifiers = Slot(uri=NMDC.alternative_identifiers, name="alternative_identifiers", curie=NMDC.curie('alternative_identifiers'),
                   model_uri=NMDC.alternative_identifiers, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]],
                   pattern=re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$'))

slots.start_date = Slot(uri=NMDC.start_date, name="start_date", curie=NMDC.curie('start_date'),
                   model_uri=NMDC.start_date, domain=None, range=Optional[str])

slots.end_date = Slot(uri=NMDC.end_date, name="end_date", curie=NMDC.curie('end_date'),
                   model_uri=NMDC.end_date, domain=None, range=Optional[str])

slots.emsl_store_temp = Slot(uri=NMDC.emsl_store_temp, name="emsl_store_temp", curie=NMDC.curie('emsl_store_temp'),
                   model_uri=NMDC.emsl_store_temp, domain=None, range=Optional[str])

slots.project_id = Slot(uri=NMDC.project_id, name="project_id", curie=NMDC.curie('project_id'),
                   model_uri=NMDC.project_id, domain=None, range=Optional[str])

slots.replicate_number = Slot(uri=NMDC.replicate_number, name="replicate_number", curie=NMDC.curie('replicate_number'),
                   model_uri=NMDC.replicate_number, domain=None, range=Optional[str])

slots.sample_shipped = Slot(uri=NMDC.sample_shipped, name="sample_shipped", curie=NMDC.curie('sample_shipped'),
                   model_uri=NMDC.sample_shipped, domain=None, range=Optional[str])

slots.sample_type = Slot(uri=NMDC.sample_type, name="sample_type", curie=NMDC.curie('sample_type'),
                   model_uri=NMDC.sample_type, domain=None, range=Optional[Union[str, "SampleTypeEnum"]])

slots.technical_reps = Slot(uri=NMDC.technical_reps, name="technical_reps", curie=NMDC.curie('technical_reps'),
                   model_uri=NMDC.technical_reps, domain=None, range=Optional[str])

slots.dna_collect_site = Slot(uri=NMDC.dna_collect_site, name="dna_collect_site", curie=NMDC.curie('dna_collect_site'),
                   model_uri=NMDC.dna_collect_site, domain=None, range=Optional[str])

slots.dna_cont_type = Slot(uri=NMDC.dna_cont_type, name="dna_cont_type", curie=NMDC.curie('dna_cont_type'),
                   model_uri=NMDC.dna_cont_type, domain=None, range=Optional[Union[str, "JgiContTypeEnum"]])

slots.dna_cont_well = Slot(uri=NMDC.dna_cont_well, name="dna_cont_well", curie=NMDC.curie('dna_cont_well'),
                   model_uri=NMDC.dna_cont_well, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?!A1$|A12$|H1$|H12$)(([A-H][1-9])|([A-H]1[0-2]))$'))

slots.dna_container_id = Slot(uri=NMDC.dna_container_id, name="dna_container_id", curie=NMDC.curie('dna_container_id'),
                   model_uri=NMDC.dna_container_id, domain=None, range=Optional[str])

slots.dna_dnase = Slot(uri=NMDC.dna_dnase, name="dna_dnase", curie=NMDC.curie('dna_dnase'),
                   model_uri=NMDC.dna_dnase, domain=None, range=Optional[Union[str, "YesNoEnum"]])

slots.dna_isolate_meth = Slot(uri=NMDC.dna_isolate_meth, name="dna_isolate_meth", curie=NMDC.curie('dna_isolate_meth'),
                   model_uri=NMDC.dna_isolate_meth, domain=None, range=Optional[str])

slots.dna_organisms = Slot(uri=NMDC.dna_organisms, name="dna_organisms", curie=NMDC.curie('dna_organisms'),
                   model_uri=NMDC.dna_organisms, domain=None, range=Optional[str])

slots.dna_project_contact = Slot(uri=NMDC.dna_project_contact, name="dna_project_contact", curie=NMDC.curie('dna_project_contact'),
                   model_uri=NMDC.dna_project_contact, domain=None, range=Optional[str])

slots.dna_samp_id = Slot(uri=NMDC.dna_samp_id, name="dna_samp_id", curie=NMDC.curie('dna_samp_id'),
                   model_uri=NMDC.dna_samp_id, domain=None, range=Optional[str])

slots.dna_sample_format = Slot(uri=NMDC.dna_sample_format, name="dna_sample_format", curie=NMDC.curie('dna_sample_format'),
                   model_uri=NMDC.dna_sample_format, domain=None, range=Optional[Union[str, "DNASampleFormatEnum"]])

slots.dna_sample_name = Slot(uri=NMDC.dna_sample_name, name="dna_sample_name", curie=NMDC.curie('dna_sample_name'),
                   model_uri=NMDC.dna_sample_name, domain=None, range=Optional[str])

slots.dna_seq_project = Slot(uri=NMDC.dna_seq_project, name="dna_seq_project", curie=NMDC.curie('dna_seq_project'),
                   model_uri=NMDC.dna_seq_project, domain=None, range=Optional[str])

slots.dna_seq_project_pi = Slot(uri=NMDC.dna_seq_project_pi, name="dna_seq_project_pi", curie=NMDC.curie('dna_seq_project_pi'),
                   model_uri=NMDC.dna_seq_project_pi, domain=None, range=Optional[str])

slots.dna_seq_project_name = Slot(uri=NMDC.dna_seq_project_name, name="dna_seq_project_name", curie=NMDC.curie('dna_seq_project_name'),
                   model_uri=NMDC.dna_seq_project_name, domain=None, range=Optional[str])

slots.dna_volume = Slot(uri=NMDC.dna_volume, name="dna_volume", curie=NMDC.curie('dna_volume'),
                   model_uri=NMDC.dna_volume, domain=None, range=Optional[float])

slots.proposal_dna = Slot(uri=NMDC.proposal_dna, name="proposal_dna", curie=NMDC.curie('proposal_dna'),
                   model_uri=NMDC.proposal_dna, domain=None, range=Optional[str])

slots.dnase_rna = Slot(uri=NMDC.dnase_rna, name="dnase_rna", curie=NMDC.curie('dnase_rna'),
                   model_uri=NMDC.dnase_rna, domain=None, range=Optional[Union[str, "YesNoEnum"]])

slots.proposal_rna = Slot(uri=NMDC.proposal_rna, name="proposal_rna", curie=NMDC.curie('proposal_rna'),
                   model_uri=NMDC.proposal_rna, domain=None, range=Optional[str])

slots.rna_absorb1 = Slot(uri=NMDC.rna_absorb1, name="rna_absorb1", curie=NMDC.curie('rna_absorb1'),
                   model_uri=NMDC.rna_absorb1, domain=None, range=Optional[float])

slots.rna_absorb2 = Slot(uri=NMDC.rna_absorb2, name="rna_absorb2", curie=NMDC.curie('rna_absorb2'),
                   model_uri=NMDC.rna_absorb2, domain=None, range=Optional[float])

slots.rna_collect_site = Slot(uri=NMDC.rna_collect_site, name="rna_collect_site", curie=NMDC.curie('rna_collect_site'),
                   model_uri=NMDC.rna_collect_site, domain=None, range=Optional[str])

slots.rna_concentration = Slot(uri=NMDC.rna_concentration, name="rna_concentration", curie=NMDC.curie('rna_concentration'),
                   model_uri=NMDC.rna_concentration, domain=None, range=Optional[float])

slots.rna_cont_type = Slot(uri=NMDC.rna_cont_type, name="rna_cont_type", curie=NMDC.curie('rna_cont_type'),
                   model_uri=NMDC.rna_cont_type, domain=None, range=Optional[Union[str, "JgiContTypeEnum"]])

slots.rna_cont_well = Slot(uri=NMDC.rna_cont_well, name="rna_cont_well", curie=NMDC.curie('rna_cont_well'),
                   model_uri=NMDC.rna_cont_well, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?!A1$|A12$|H1$|H12$)(([A-H][1-9])|([A-H]1[0-2]))$'))

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
                   model_uri=NMDC.rna_sample_format, domain=None, range=Optional[Union[str, "RNASampleFormatEnum"]])

slots.rna_sample_name = Slot(uri=NMDC.rna_sample_name, name="rna_sample_name", curie=NMDC.curie('rna_sample_name'),
                   model_uri=NMDC.rna_sample_name, domain=None, range=Optional[str])

slots.rna_seq_project = Slot(uri=NMDC.rna_seq_project, name="rna_seq_project", curie=NMDC.curie('rna_seq_project'),
                   model_uri=NMDC.rna_seq_project, domain=None, range=Optional[str])

slots.rna_seq_project_pi = Slot(uri=NMDC.rna_seq_project_pi, name="rna_seq_project_pi", curie=NMDC.curie('rna_seq_project_pi'),
                   model_uri=NMDC.rna_seq_project_pi, domain=None, range=Optional[str])

slots.rna_seq_project_name = Slot(uri=NMDC.rna_seq_project_name, name="rna_seq_project_name", curie=NMDC.curie('rna_seq_project_name'),
                   model_uri=NMDC.rna_seq_project_name, domain=None, range=Optional[str])

slots.rna_volume = Slot(uri=NMDC.rna_volume, name="rna_volume", curie=NMDC.curie('rna_volume'),
                   model_uri=NMDC.rna_volume, domain=None, range=Optional[float])

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

slots.analysis_type = Slot(uri=NMDC.analysis_type, name="analysis_type", curie=NMDC.curie('analysis_type'),
                   model_uri=NMDC.analysis_type, domain=None, range=Optional[Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]]])

slots.sample_link = Slot(uri=NMDC.sample_link, name="sample_link", curie=NMDC.curie('sample_link'),
                   model_uri=NMDC.sample_link, domain=None, range=Optional[Union[str, List[str]]])

slots.metagenome_assembly_parameter = Slot(uri=NMDC.metagenome_assembly_parameter, name="metagenome_assembly_parameter", curie=NMDC.curie('metagenome_assembly_parameter'),
                   model_uri=NMDC.metagenome_assembly_parameter, domain=None, range=Optional[str])

slots.has_peptide_quantifications = Slot(uri=NMDC.has_peptide_quantifications, name="has_peptide_quantifications", curie=NMDC.curie('has_peptide_quantifications'),
                   model_uri=NMDC.has_peptide_quantifications, domain=None, range=Optional[Union[Union[dict, PeptideQuantification], List[Union[dict, PeptideQuantification]]]])

slots.asm_score = Slot(uri=NMDC.asm_score, name="asm_score", curie=NMDC.curie('asm_score'),
                   model_uri=NMDC.asm_score, domain=None, range=Optional[float])

slots.scaffolds = Slot(uri=NMDC.scaffolds, name="scaffolds", curie=NMDC.curie('scaffolds'),
                   model_uri=NMDC.scaffolds, domain=None, range=Optional[float])

slots.scaf_logsum = Slot(uri=NMDC.scaf_logsum, name="scaf_logsum", curie=NMDC.curie('scaf_logsum'),
                   model_uri=NMDC.scaf_logsum, domain=None, range=Optional[float])

slots.scaf_powsum = Slot(uri=NMDC.scaf_powsum, name="scaf_powsum", curie=NMDC.curie('scaf_powsum'),
                   model_uri=NMDC.scaf_powsum, domain=None, range=Optional[float])

slots.scaf_max = Slot(uri=NMDC.scaf_max, name="scaf_max", curie=NMDC.curie('scaf_max'),
                   model_uri=NMDC.scaf_max, domain=None, range=Optional[float])

slots.scaf_bp = Slot(uri=NMDC.scaf_bp, name="scaf_bp", curie=NMDC.curie('scaf_bp'),
                   model_uri=NMDC.scaf_bp, domain=None, range=Optional[float])

slots.scaf_n50 = Slot(uri=NMDC.scaf_n50, name="scaf_n50", curie=NMDC.curie('scaf_n50'),
                   model_uri=NMDC.scaf_n50, domain=None, range=Optional[float])

slots.scaf_n90 = Slot(uri=NMDC.scaf_n90, name="scaf_n90", curie=NMDC.curie('scaf_n90'),
                   model_uri=NMDC.scaf_n90, domain=None, range=Optional[float])

slots.scaf_l50 = Slot(uri=NMDC.scaf_l50, name="scaf_l50", curie=NMDC.curie('scaf_l50'),
                   model_uri=NMDC.scaf_l50, domain=None, range=Optional[float])

slots.scaf_l90 = Slot(uri=NMDC.scaf_l90, name="scaf_l90", curie=NMDC.curie('scaf_l90'),
                   model_uri=NMDC.scaf_l90, domain=None, range=Optional[float])

slots.scaf_n_gt50k = Slot(uri=NMDC.scaf_n_gt50k, name="scaf_n_gt50k", curie=NMDC.curie('scaf_n_gt50k'),
                   model_uri=NMDC.scaf_n_gt50k, domain=None, range=Optional[float])

slots.scaf_l_gt50k = Slot(uri=NMDC.scaf_l_gt50k, name="scaf_l_gt50k", curie=NMDC.curie('scaf_l_gt50k'),
                   model_uri=NMDC.scaf_l_gt50k, domain=None, range=Optional[float])

slots.scaf_pct_gt50k = Slot(uri=NMDC.scaf_pct_gt50k, name="scaf_pct_gt50k", curie=NMDC.curie('scaf_pct_gt50k'),
                   model_uri=NMDC.scaf_pct_gt50k, domain=None, range=Optional[float])

slots.contigs = Slot(uri=NMDC.contigs, name="contigs", curie=NMDC.curie('contigs'),
                   model_uri=NMDC.contigs, domain=None, range=Optional[float])

slots.contig_bp = Slot(uri=NMDC.contig_bp, name="contig_bp", curie=NMDC.curie('contig_bp'),
                   model_uri=NMDC.contig_bp, domain=None, range=Optional[float])

slots.ctg_n50 = Slot(uri=NMDC.ctg_n50, name="ctg_n50", curie=NMDC.curie('ctg_n50'),
                   model_uri=NMDC.ctg_n50, domain=None, range=Optional[float])

slots.ctg_l50 = Slot(uri=NMDC.ctg_l50, name="ctg_l50", curie=NMDC.curie('ctg_l50'),
                   model_uri=NMDC.ctg_l50, domain=None, range=Optional[float])

slots.ctg_n90 = Slot(uri=NMDC.ctg_n90, name="ctg_n90", curie=NMDC.curie('ctg_n90'),
                   model_uri=NMDC.ctg_n90, domain=None, range=Optional[float])

slots.ctg_l90 = Slot(uri=NMDC.ctg_l90, name="ctg_l90", curie=NMDC.curie('ctg_l90'),
                   model_uri=NMDC.ctg_l90, domain=None, range=Optional[float])

slots.ctg_logsum = Slot(uri=NMDC.ctg_logsum, name="ctg_logsum", curie=NMDC.curie('ctg_logsum'),
                   model_uri=NMDC.ctg_logsum, domain=None, range=Optional[float])

slots.ctg_powsum = Slot(uri=NMDC.ctg_powsum, name="ctg_powsum", curie=NMDC.curie('ctg_powsum'),
                   model_uri=NMDC.ctg_powsum, domain=None, range=Optional[float])

slots.ctg_max = Slot(uri=NMDC.ctg_max, name="ctg_max", curie=NMDC.curie('ctg_max'),
                   model_uri=NMDC.ctg_max, domain=None, range=Optional[float])

slots.gap_pct = Slot(uri=NMDC.gap_pct, name="gap_pct", curie=NMDC.curie('gap_pct'),
                   model_uri=NMDC.gap_pct, domain=None, range=Optional[float])

slots.gc_std = Slot(uri=NMDC.gc_std, name="gc_std", curie=NMDC.curie('gc_std'),
                   model_uri=NMDC.gc_std, domain=None, range=Optional[float])

slots.gc_avg = Slot(uri=NMDC.gc_avg, name="gc_avg", curie=NMDC.curie('gc_avg'),
                   model_uri=NMDC.gc_avg, domain=None, range=Optional[float])

slots.num_input_reads = Slot(uri=NMDC.num_input_reads, name="num_input_reads", curie=NMDC.curie('num_input_reads'),
                   model_uri=NMDC.num_input_reads, domain=None, range=Optional[float])

slots.num_aligned_reads = Slot(uri=NMDC.num_aligned_reads, name="num_aligned_reads", curie=NMDC.curie('num_aligned_reads'),
                   model_uri=NMDC.num_aligned_reads, domain=None, range=Optional[float])

slots.read_qc_analysis_statistic = Slot(uri=NMDC.read_qc_analysis_statistic, name="read_qc_analysis_statistic", curie=NMDC.curie('read_qc_analysis_statistic'),
                   model_uri=NMDC.read_qc_analysis_statistic, domain=None, range=Optional[str])

slots.mags_list = Slot(uri=NMDC.mags_list, name="mags_list", curie=NMDC.curie('mags_list'),
                   model_uri=NMDC.mags_list, domain=None, range=Optional[Union[Union[dict, MagBin], List[Union[dict, MagBin]]]])

slots.too_short_contig_num = Slot(uri=NMDC.too_short_contig_num, name="too_short_contig_num", curie=NMDC.curie('too_short_contig_num'),
                   model_uri=NMDC.too_short_contig_num, domain=None, range=Optional[int])

slots.binned_contig_num = Slot(uri=NMDC.binned_contig_num, name="binned_contig_num", curie=NMDC.curie('binned_contig_num'),
                   model_uri=NMDC.binned_contig_num, domain=None, range=Optional[int])

slots.input_contig_num = Slot(uri=NMDC.input_contig_num, name="input_contig_num", curie=NMDC.curie('input_contig_num'),
                   model_uri=NMDC.input_contig_num, domain=None, range=Optional[int])

slots.unbinned_contig_num = Slot(uri=NMDC.unbinned_contig_num, name="unbinned_contig_num", curie=NMDC.curie('unbinned_contig_num'),
                   model_uri=NMDC.unbinned_contig_num, domain=None, range=Optional[int])

slots.low_depth_contig_num = Slot(uri=NMDC.low_depth_contig_num, name="low_depth_contig_num", curie=NMDC.curie('low_depth_contig_num'),
                   model_uri=NMDC.low_depth_contig_num, domain=None, range=Optional[int])

slots.input_read_count = Slot(uri=NMDC.input_read_count, name="input_read_count", curie=NMDC.curie('input_read_count'),
                   model_uri=NMDC.input_read_count, domain=None, range=Optional[float])

slots.input_base_count = Slot(uri=NMDC.input_base_count, name="input_base_count", curie=NMDC.curie('input_base_count'),
                   model_uri=NMDC.input_base_count, domain=None, range=Optional[float])

slots.output_read_count = Slot(uri=NMDC.output_read_count, name="output_read_count", curie=NMDC.curie('output_read_count'),
                   model_uri=NMDC.output_read_count, domain=None, range=Optional[float])

slots.output_base_count = Slot(uri=NMDC.output_base_count, name="output_base_count", curie=NMDC.curie('output_base_count'),
                   model_uri=NMDC.output_base_count, domain=None, range=Optional[float])

slots.output_read_bases = Slot(uri=NMDC.output_read_bases, name="output_read_bases", curie=NMDC.curie('output_read_bases'),
                   model_uri=NMDC.output_read_bases, domain=None, range=Optional[float])

slots.input_read_bases = Slot(uri=NMDC.input_read_bases, name="input_read_bases", curie=NMDC.curie('input_read_bases'),
                   model_uri=NMDC.input_read_bases, domain=None, range=Optional[float])

slots.has_calibration = Slot(uri=NMDC.has_calibration, name="has_calibration", curie=NMDC.curie('has_calibration'),
                   model_uri=NMDC.has_calibration, domain=None, range=Optional[str])

slots.calibration_object = Slot(uri=NMDC.calibration_object, name="calibration_object", curie=NMDC.curie('calibration_object'),
                   model_uri=NMDC.calibration_object, domain=None, range=Optional[Union[str, DataObjectId]])

slots.internal_calibration = Slot(uri=NMDC.internal_calibration, name="internal_calibration", curie=NMDC.curie('internal_calibration'),
                   model_uri=NMDC.internal_calibration, domain=None, range=Optional[Union[bool, Bool]])

slots.calibration_target = Slot(uri=NMDC.calibration_target, name="calibration_target", curie=NMDC.curie('calibration_target'),
                   model_uri=NMDC.calibration_target, domain=None, range=Optional[Union[str, "CalibrationTargetEnum"]])

slots.calibration_standard = Slot(uri=NMDC.calibration_standard, name="calibration_standard", curie=NMDC.curie('calibration_standard'),
                   model_uri=NMDC.calibration_standard, domain=None, range=Optional[Union[str, "CalibrationStandardEnum"]])

slots.has_metabolite_identifications = Slot(uri=NMDC.has_metabolite_identifications, name="has_metabolite_identifications", curie=NMDC.curie('has_metabolite_identifications'),
                   model_uri=NMDC.has_metabolite_identifications, domain=None, range=Optional[Union[Union[dict, MetaboliteIdentification], List[Union[dict, MetaboliteIdentification]]]])

slots.NucleotideSequencing_id = Slot(uri=NMDC.id, name="NucleotideSequencing_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.NucleotideSequencing_id, domain=NucleotideSequencing, range=Union[str, NucleotideSequencingId],
                   pattern=re.compile(r'.*'))

slots.MassSpectrometry_id = Slot(uri=NMDC.id, name="MassSpectrometry_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.MassSpectrometry_id, domain=MassSpectrometry, range=Union[str, MassSpectrometryId],
                   pattern=re.compile(r'.*'))

slots.MassSpectrometry_has_calibration = Slot(uri=NMDC.has_calibration, name="MassSpectrometry_has_calibration", curie=NMDC.curie('has_calibration'),
                   model_uri=NMDC.MassSpectrometry_has_calibration, domain=MassSpectrometry, range=Optional[str],
                   pattern=re.compile(r'.*'))

slots.MassSpectrometry_has_chromatography_configuration = Slot(uri=NMDC.has_chromatography_configuration, name="MassSpectrometry_has_chromatography_configuration", curie=NMDC.curie('has_chromatography_configuration'),
                   model_uri=NMDC.MassSpectrometry_has_chromatography_configuration, domain=MassSpectrometry, range=Optional[Union[str, ChromatographyConfigurationId]],
                   pattern=re.compile(r'.*'))

slots.MassSpectrometry_has_mass_spectrometry_configuration = Slot(uri=NMDC.has_mass_spectrometry_configuration, name="MassSpectrometry_has_mass_spectrometry_configuration", curie=NMDC.curie('has_mass_spectrometry_configuration'),
                   model_uri=NMDC.MassSpectrometry_has_mass_spectrometry_configuration, domain=MassSpectrometry, range=Optional[Union[str, MassSpectrometryConfigurationId]],
                   pattern=re.compile(r'.*'))

slots.MassSpectrometryConfiguration_name = Slot(uri=NMDC.name, name="MassSpectrometryConfiguration_name", curie=NMDC.curie('name'),
                   model_uri=NMDC.MassSpectrometryConfiguration_name, domain=MassSpectrometryConfiguration, range=str)

slots.MassSpectrometryConfiguration_description = Slot(uri=DCTERMS.description, name="MassSpectrometryConfiguration_description", curie=DCTERMS.curie('description'),
                   model_uri=NMDC.MassSpectrometryConfiguration_description, domain=MassSpectrometryConfiguration, range=str)

slots.MassSpectrometryConfiguration_id = Slot(uri=NMDC.id, name="MassSpectrometryConfiguration_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.MassSpectrometryConfiguration_id, domain=MassSpectrometryConfiguration, range=Union[str, MassSpectrometryConfigurationId],
                   pattern=re.compile(r'.*'))

slots.ChromatographyConfiguration_name = Slot(uri=NMDC.name, name="ChromatographyConfiguration_name", curie=NMDC.curie('name'),
                   model_uri=NMDC.ChromatographyConfiguration_name, domain=ChromatographyConfiguration, range=str)

slots.ChromatographyConfiguration_description = Slot(uri=DCTERMS.description, name="ChromatographyConfiguration_description", curie=DCTERMS.curie('description'),
                   model_uri=NMDC.ChromatographyConfiguration_description, domain=ChromatographyConfiguration, range=str)

slots.ChromatographyConfiguration_id = Slot(uri=NMDC.id, name="ChromatographyConfiguration_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.ChromatographyConfiguration_id, domain=ChromatographyConfiguration, range=Union[str, ChromatographyConfigurationId],
                   pattern=re.compile(r'.*'))

slots.FunctionalAnnotationAggMember_metagenome_annotation_id = Slot(uri=NMDC.metagenome_annotation_id, name="FunctionalAnnotationAggMember_metagenome_annotation_id", curie=NMDC.curie('metagenome_annotation_id'),
                   model_uri=NMDC.FunctionalAnnotationAggMember_metagenome_annotation_id, domain=FunctionalAnnotationAggMember, range=Union[str, WorkflowExecutionId],
                   pattern=re.compile(r'.*'))

slots.Pooling_has_input = Slot(uri=NMDC.has_input, name="Pooling_has_input", curie=NMDC.curie('has_input'),
                   model_uri=NMDC.Pooling_has_input, domain=Pooling, range=Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]],
                   pattern=re.compile(r'.*'))

slots.Pooling_has_output = Slot(uri=NMDC.has_output, name="Pooling_has_output", curie=NMDC.curie('has_output'),
                   model_uri=NMDC.Pooling_has_output, domain=Pooling, range=Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]],
                   pattern=re.compile(r'.*'))

slots.Pooling_id = Slot(uri=NMDC.id, name="Pooling_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.Pooling_id, domain=Pooling, range=Union[str, PoolingId],
                   pattern=re.compile(r'.*'))

slots.Extraction_has_input = Slot(uri=NMDC.has_input, name="Extraction_has_input", curie=NMDC.curie('has_input'),
                   model_uri=NMDC.Extraction_has_input, domain=Extraction, range=Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]],
                   pattern=re.compile(r'.*'))

slots.Extraction_has_output = Slot(uri=NMDC.has_output, name="Extraction_has_output", curie=NMDC.curie('has_output'),
                   model_uri=NMDC.Extraction_has_output, domain=Extraction, range=Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]],
                   pattern=re.compile(r'.*'))

slots.Extraction_id = Slot(uri=NMDC.id, name="Extraction_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.Extraction_id, domain=Extraction, range=Union[str, ExtractionId],
                   pattern=re.compile(r'.*'))

slots.Extraction_volume = Slot(uri=NMDC.volume, name="Extraction_volume", curie=NMDC.curie('volume'),
                   model_uri=NMDC.Extraction_volume, domain=Extraction, range=Optional[Union[dict, QuantityValue]])

slots.LibraryPreparation_has_input = Slot(uri=NMDC.has_input, name="LibraryPreparation_has_input", curie=NMDC.curie('has_input'),
                   model_uri=NMDC.LibraryPreparation_has_input, domain=LibraryPreparation, range=Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]],
                   pattern=re.compile(r'.*'))

slots.LibraryPreparation_has_output = Slot(uri=NMDC.has_output, name="LibraryPreparation_has_output", curie=NMDC.curie('has_output'),
                   model_uri=NMDC.LibraryPreparation_has_output, domain=LibraryPreparation, range=Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]],
                   pattern=re.compile(r'.*'))

slots.LibraryPreparation_id = Slot(uri=NMDC.id, name="LibraryPreparation_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.LibraryPreparation_id, domain=LibraryPreparation, range=Union[str, LibraryPreparationId],
                   pattern=re.compile(r'.*'))

slots.LibraryPreparation_pcr_cond = Slot(uri=MIXS['0000049'], name="LibraryPreparation_pcr_cond", curie=MIXS.curie('0000049'),
                   model_uri=NMDC.LibraryPreparation_pcr_cond, domain=LibraryPreparation, range=Optional[Union[dict, TextValue]])

slots.CollectingBiosamplesFromSite_has_input = Slot(uri=NMDC.has_input, name="CollectingBiosamplesFromSite_has_input", curie=NMDC.curie('has_input'),
                   model_uri=NMDC.CollectingBiosamplesFromSite_has_input, domain=CollectingBiosamplesFromSite, range=Union[Union[str, SiteId], List[Union[str, SiteId]]],
                   pattern=re.compile(r'.*'))

slots.CollectingBiosamplesFromSite_has_output = Slot(uri=NMDC.has_output, name="CollectingBiosamplesFromSite_has_output", curie=NMDC.curie('has_output'),
                   model_uri=NMDC.CollectingBiosamplesFromSite_has_output, domain=CollectingBiosamplesFromSite, range=Union[Union[str, BiosampleId], List[Union[str, BiosampleId]]],
                   pattern=re.compile(r'.*'))

slots.CollectingBiosamplesFromSite_id = Slot(uri=NMDC.id, name="CollectingBiosamplesFromSite_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.CollectingBiosamplesFromSite_id, domain=CollectingBiosamplesFromSite, range=Union[str, CollectingBiosamplesFromSiteId],
                   pattern=re.compile(r'.*'))

slots.ProtocolExecution_id = Slot(uri=NMDC.id, name="ProtocolExecution_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.ProtocolExecution_id, domain=ProtocolExecution, range=Union[str, ProtocolExecutionId],
                   pattern=re.compile(r'.*'))

slots.ProtocolExecution_has_input = Slot(uri=NMDC.has_input, name="ProtocolExecution_has_input", curie=NMDC.curie('has_input'),
                   model_uri=NMDC.ProtocolExecution_has_input, domain=ProtocolExecution, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]],
                   pattern=re.compile(r'.*'))

slots.ProtocolExecution_has_output = Slot(uri=NMDC.has_output, name="ProtocolExecution_has_output", curie=NMDC.curie('has_output'),
                   model_uri=NMDC.ProtocolExecution_has_output, domain=ProtocolExecution, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]],
                   pattern=re.compile(r'.*'))

slots.ProtocolExecution_has_process_parts = Slot(uri=NMDC.has_process_parts, name="ProtocolExecution_has_process_parts", curie=NMDC.curie('has_process_parts'),
                   model_uri=NMDC.ProtocolExecution_has_process_parts, domain=ProtocolExecution, range=Union[Union[str, PlannedProcessId], List[Union[str, PlannedProcessId]]],
                   pattern=re.compile(r'.*'))

slots.SubSamplingProcess_id = Slot(uri=NMDC.id, name="SubSamplingProcess_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.SubSamplingProcess_id, domain=SubSamplingProcess, range=Union[str, SubSamplingProcessId],
                   pattern=re.compile(r'.*'))

slots.SubSamplingProcess_volume = Slot(uri=NMDC.volume, name="SubSamplingProcess_volume", curie=NMDC.curie('volume'),
                   model_uri=NMDC.SubSamplingProcess_volume, domain=SubSamplingProcess, range=Optional[Union[dict, QuantityValue]])

slots.SubSamplingProcess_mass = Slot(uri=NMDC.mass, name="SubSamplingProcess_mass", curie=NMDC.curie('mass'),
                   model_uri=NMDC.SubSamplingProcess_mass, domain=SubSamplingProcess, range=Optional[Union[dict, QuantityValue]])

slots.SubSamplingProcess_has_input = Slot(uri=NMDC.has_input, name="SubSamplingProcess_has_input", curie=NMDC.curie('has_input'),
                   model_uri=NMDC.SubSamplingProcess_has_input, domain=SubSamplingProcess, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]],
                   pattern=re.compile(r'.*'))

slots.SubSamplingProcess_has_output = Slot(uri=NMDC.has_output, name="SubSamplingProcess_has_output", curie=NMDC.curie('has_output'),
                   model_uri=NMDC.SubSamplingProcess_has_output, domain=SubSamplingProcess, range=Optional[Union[Union[str, ProcessedSampleId], List[Union[str, ProcessedSampleId]]]],
                   pattern=re.compile(r'.*'))

slots.MixingProcess_id = Slot(uri=NMDC.id, name="MixingProcess_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.MixingProcess_id, domain=MixingProcess, range=Union[str, MixingProcessId],
                   pattern=re.compile(r'.*'))

slots.MixingProcess_has_input = Slot(uri=NMDC.has_input, name="MixingProcess_has_input", curie=NMDC.curie('has_input'),
                   model_uri=NMDC.MixingProcess_has_input, domain=MixingProcess, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]],
                   pattern=re.compile(r'.*'))

slots.MixingProcess_has_output = Slot(uri=NMDC.has_output, name="MixingProcess_has_output", curie=NMDC.curie('has_output'),
                   model_uri=NMDC.MixingProcess_has_output, domain=MixingProcess, range=Optional[Union[Union[str, ProcessedSampleId], List[Union[str, ProcessedSampleId]]]],
                   pattern=re.compile(r'.*'))

slots.FiltrationProcess_id = Slot(uri=NMDC.id, name="FiltrationProcess_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.FiltrationProcess_id, domain=FiltrationProcess, range=Union[str, FiltrationProcessId],
                   pattern=re.compile(r'.*'))

slots.FiltrationProcess_volume = Slot(uri=NMDC.volume, name="FiltrationProcess_volume", curie=NMDC.curie('volume'),
                   model_uri=NMDC.FiltrationProcess_volume, domain=FiltrationProcess, range=Optional[Union[dict, QuantityValue]])

slots.FiltrationProcess_has_input = Slot(uri=NMDC.has_input, name="FiltrationProcess_has_input", curie=NMDC.curie('has_input'),
                   model_uri=NMDC.FiltrationProcess_has_input, domain=FiltrationProcess, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]],
                   pattern=re.compile(r'.*'))

slots.FiltrationProcess_has_output = Slot(uri=NMDC.has_output, name="FiltrationProcess_has_output", curie=NMDC.curie('has_output'),
                   model_uri=NMDC.FiltrationProcess_has_output, domain=FiltrationProcess, range=Optional[Union[Union[str, ProcessedSampleId], List[Union[str, ProcessedSampleId]]]],
                   pattern=re.compile(r'.*'))

slots.StorageProcess_substances_used = Slot(uri=NMDC.substances_used, name="StorageProcess_substances_used", curie=NMDC.curie('substances_used'),
                   model_uri=NMDC.StorageProcess_substances_used, domain=StorageProcess, range=Optional[Union[Union[dict, PortionOfSubstance], List[Union[dict, PortionOfSubstance]]]])

slots.StorageProcess_id = Slot(uri=NMDC.id, name="StorageProcess_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.StorageProcess_id, domain=StorageProcess, range=Union[str, StorageProcessId],
                   pattern=re.compile(r'.*'))

slots.StorageProcess_has_input = Slot(uri=NMDC.has_input, name="StorageProcess_has_input", curie=NMDC.curie('has_input'),
                   model_uri=NMDC.StorageProcess_has_input, domain=StorageProcess, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]],
                   pattern=re.compile(r'.*'))

slots.StorageProcess_has_output = Slot(uri=NMDC.has_output, name="StorageProcess_has_output", curie=NMDC.curie('has_output'),
                   model_uri=NMDC.StorageProcess_has_output, domain=StorageProcess, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]],
                   pattern=re.compile(r'.*'))

slots.ChromatographicSeparationProcess_id = Slot(uri=NMDC.id, name="ChromatographicSeparationProcess_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.ChromatographicSeparationProcess_id, domain=ChromatographicSeparationProcess, range=Union[str, ChromatographicSeparationProcessId],
                   pattern=re.compile(r'.*'))

slots.ChromatographicSeparationProcess_has_input = Slot(uri=NMDC.has_input, name="ChromatographicSeparationProcess_has_input", curie=NMDC.curie('has_input'),
                   model_uri=NMDC.ChromatographicSeparationProcess_has_input, domain=ChromatographicSeparationProcess, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]],
                   pattern=re.compile(r'.*'))

slots.ChromatographicSeparationProcess_has_output = Slot(uri=NMDC.has_output, name="ChromatographicSeparationProcess_has_output", curie=NMDC.curie('has_output'),
                   model_uri=NMDC.ChromatographicSeparationProcess_has_output, domain=ChromatographicSeparationProcess, range=Optional[Union[Union[str, ProcessedSampleId], List[Union[str, ProcessedSampleId]]]],
                   pattern=re.compile(r'.*'))

slots.DissolvingProcess_id = Slot(uri=NMDC.id, name="DissolvingProcess_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.DissolvingProcess_id, domain=DissolvingProcess, range=Union[str, DissolvingProcessId],
                   pattern=re.compile(r'.*'))

slots.ChemicalConversionProcess_id = Slot(uri=NMDC.id, name="ChemicalConversionProcess_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.ChemicalConversionProcess_id, domain=ChemicalConversionProcess, range=Union[str, ChemicalConversionProcessId],
                   pattern=re.compile(r'.*'))

slots.MetagenomeAnnotation_id = Slot(uri=NMDC.id, name="MetagenomeAnnotation_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.MetagenomeAnnotation_id, domain=MetagenomeAnnotation, range=Union[str, MetagenomeAnnotationId],
                   pattern=re.compile(r'.*'))

slots.MetagenomeAnnotation_img_identifiers = Slot(uri=NMDC.img_identifiers, name="MetagenomeAnnotation_img_identifiers", curie=NMDC.curie('img_identifiers'),
                   model_uri=NMDC.MetagenomeAnnotation_img_identifiers, domain=MetagenomeAnnotation, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^img\.taxon:[a-zA-Z0-9_][a-zA-Z0-9_\/\.]*$'))

slots.MetagenomeAnnotation_was_informed_by = Slot(uri=NMDC.was_informed_by, name="MetagenomeAnnotation_was_informed_by", curie=NMDC.curie('was_informed_by'),
                   model_uri=NMDC.MetagenomeAnnotation_was_informed_by, domain=MetagenomeAnnotation, range=Optional[Union[str, DataGenerationId]], mappings = [PROV["wasInformedBy"]],
                   pattern=re.compile(r'.*'))

slots.MetagenomeAnnotation_gold_analysis_project_identifiers = Slot(uri=NMDC.gold_analysis_project_identifiers, name="MetagenomeAnnotation_gold_analysis_project_identifiers", curie=NMDC.curie('gold_analysis_project_identifiers'),
                   model_uri=NMDC.MetagenomeAnnotation_gold_analysis_project_identifiers, domain=MetagenomeAnnotation, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'.*'))

slots.FieldResearchSite_id = Slot(uri=NMDC.id, name="FieldResearchSite_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.FieldResearchSite_id, domain=FieldResearchSite, range=Union[str, FieldResearchSiteId],
                   pattern=re.compile(r'.*'))

slots.FieldResearchSite_part_of = Slot(uri=DCTERMS.isPartOf, name="FieldResearchSite_part_of", curie=DCTERMS.curie('isPartOf'),
                   model_uri=NMDC.FieldResearchSite_part_of, domain=FieldResearchSite, range=Optional[Union[Union[str, FieldResearchSiteId], List[Union[str, FieldResearchSiteId]]]],
                   pattern=re.compile(r'.*'))

slots.Biosample_collected_from = Slot(uri=NMDC.collected_from, name="Biosample_collected_from", curie=NMDC.curie('collected_from'),
                   model_uri=NMDC.Biosample_collected_from, domain=Biosample, range=Optional[Union[str, FieldResearchSiteId]],
                   pattern=re.compile(r'.*'))

slots.Biosample_elev = Slot(uri=MIXS['0000093'], name="Biosample_elev", curie=MIXS.curie('0000093'),
                   model_uri=NMDC.Biosample_elev, domain=Biosample, range=Optional[float])

slots.Biosample_id = Slot(uri=NMDC.id, name="Biosample_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.Biosample_id, domain=Biosample, range=Union[str, BiosampleId],
                   pattern=re.compile(r'.*'))

slots.Biosample_gold_biosample_identifiers = Slot(uri=NMDC.gold_biosample_identifiers, name="Biosample_gold_biosample_identifiers", curie=NMDC.curie('gold_biosample_identifiers'),
                   model_uri=NMDC.Biosample_gold_biosample_identifiers, domain=Biosample, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]],
                   pattern=re.compile(r'^gold:Gb[0-9]+$'))

slots.Biosample_alternative_identifiers = Slot(uri=NMDC.alternative_identifiers, name="Biosample_alternative_identifiers", curie=NMDC.curie('alternative_identifiers'),
                   model_uri=NMDC.Biosample_alternative_identifiers, domain=Biosample, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]],
                   pattern=re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$'))

slots.Biosample_lat_lon = Slot(uri=MIXS['0000009'], name="Biosample_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=NMDC.Biosample_lat_lon, domain=Biosample, range=Optional[Union[dict, GeolocationValue]])

slots.Biosample_env_broad_scale = Slot(uri=MIXS['0000012'], name="Biosample_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=NMDC.Biosample_env_broad_scale, domain=Biosample, range=Union[dict, ControlledIdentifiedTermValue])

slots.Biosample_env_local_scale = Slot(uri=MIXS['0000013'], name="Biosample_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=NMDC.Biosample_env_local_scale, domain=Biosample, range=Union[dict, ControlledIdentifiedTermValue])

slots.Biosample_env_medium = Slot(uri=MIXS['0000014'], name="Biosample_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=NMDC.Biosample_env_medium, domain=Biosample, range=Union[dict, ControlledIdentifiedTermValue])

slots.Biosample_associated_studies = Slot(uri=NMDC.associated_studies, name="Biosample_associated_studies", curie=NMDC.curie('associated_studies'),
                   model_uri=NMDC.Biosample_associated_studies, domain=Biosample, range=Union[Union[str, StudyId], List[Union[str, StudyId]]],
                   pattern=re.compile(r'.*'))

slots.Biosample_fire = Slot(uri=MIXS['0001086'], name="Biosample_fire", curie=MIXS.curie('0001086'),
                   model_uri=NMDC.Biosample_fire, domain=Biosample, range=Optional[str],
                   pattern=re.compile(r'.*'))

slots.Biosample_flooding = Slot(uri=MIXS['0000319'], name="Biosample_flooding", curie=MIXS.curie('0000319'),
                   model_uri=NMDC.Biosample_flooding, domain=Biosample, range=Optional[str])

slots.Biosample_extreme_event = Slot(uri=MIXS['0000320'], name="Biosample_extreme_event", curie=MIXS.curie('0000320'),
                   model_uri=NMDC.Biosample_extreme_event, domain=Biosample, range=Optional[str])

slots.Biosample_slope_aspect = Slot(uri=MIXS['0000647'], name="Biosample_slope_aspect", curie=MIXS.curie('0000647'),
                   model_uri=NMDC.Biosample_slope_aspect, domain=Biosample, range=Optional[Union[dict, QuantityValue]])

slots.Biosample_slope_gradient = Slot(uri=MIXS['0000646'], name="Biosample_slope_gradient", curie=MIXS.curie('0000646'),
                   model_uri=NMDC.Biosample_slope_gradient, domain=Biosample, range=Optional[Union[dict, QuantityValue]])

slots.Biosample_al_sat = Slot(uri=MIXS['0000607'], name="Biosample_al_sat", curie=MIXS.curie('0000607'),
                   model_uri=NMDC.Biosample_al_sat, domain=Biosample, range=Optional[Union[dict, QuantityValue]])

slots.Biosample_al_sat_meth = Slot(uri=MIXS['0000324'], name="Biosample_al_sat_meth", curie=MIXS.curie('0000324'),
                   model_uri=NMDC.Biosample_al_sat_meth, domain=Biosample, range=Optional[Union[dict, TextValue]])

slots.Biosample_annual_precpt = Slot(uri=MIXS['0000644'], name="Biosample_annual_precpt", curie=MIXS.curie('0000644'),
                   model_uri=NMDC.Biosample_annual_precpt, domain=Biosample, range=Optional[Union[dict, QuantityValue]])

slots.Biosample_cur_vegetation = Slot(uri=MIXS['0000312'], name="Biosample_cur_vegetation", curie=MIXS.curie('0000312'),
                   model_uri=NMDC.Biosample_cur_vegetation, domain=Biosample, range=Optional[Union[dict, TextValue]])

slots.Biosample_cur_vegetation_meth = Slot(uri=MIXS['0000314'], name="Biosample_cur_vegetation_meth", curie=MIXS.curie('0000314'),
                   model_uri=NMDC.Biosample_cur_vegetation_meth, domain=Biosample, range=Optional[Union[dict, TextValue]])

slots.Biosample_heavy_metals = Slot(uri=MIXS['0000652'], name="Biosample_heavy_metals", curie=MIXS.curie('0000652'),
                   model_uri=NMDC.Biosample_heavy_metals, domain=Biosample, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.Biosample_heavy_metals_meth = Slot(uri=MIXS['0000343'], name="Biosample_heavy_metals_meth", curie=MIXS.curie('0000343'),
                   model_uri=NMDC.Biosample_heavy_metals_meth, domain=Biosample, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.Biosample_season_precpt = Slot(uri=MIXS['0000645'], name="Biosample_season_precpt", curie=MIXS.curie('0000645'),
                   model_uri=NMDC.Biosample_season_precpt, domain=Biosample, range=Optional[Union[dict, QuantityValue]])

slots.Biosample_water_cont_soil_meth = Slot(uri=MIXS['0000323'], name="Biosample_water_cont_soil_meth", curie=MIXS.curie('0000323'),
                   model_uri=NMDC.Biosample_water_cont_soil_meth, domain=Biosample, range=Optional[str])

slots.Biosample_water_content = Slot(uri=MIXS['0000185'], name="Biosample_water_content", curie=MIXS.curie('0000185'),
                   model_uri=NMDC.Biosample_water_content, domain=Biosample, range=Optional[Union[str, List[str]]])

slots.Biosample_ph_meth = Slot(uri=MIXS['0001106'], name="Biosample_ph_meth", curie=MIXS.curie('0001106'),
                   model_uri=NMDC.Biosample_ph_meth, domain=Biosample, range=Optional[Union[dict, TextValue]])

slots.Biosample_tot_carb = Slot(uri=MIXS['0000525'], name="Biosample_tot_carb", curie=MIXS.curie('0000525'),
                   model_uri=NMDC.Biosample_tot_carb, domain=Biosample, range=Optional[Union[dict, QuantityValue]])

slots.Biosample_tot_nitro_cont_meth = Slot(uri=MIXS['0000338'], name="Biosample_tot_nitro_cont_meth", curie=MIXS.curie('0000338'),
                   model_uri=NMDC.Biosample_tot_nitro_cont_meth, domain=Biosample, range=Optional[str])

slots.Biosample_tot_nitro_content = Slot(uri=MIXS['0000530'], name="Biosample_tot_nitro_content", curie=MIXS.curie('0000530'),
                   model_uri=NMDC.Biosample_tot_nitro_content, domain=Biosample, range=Optional[Union[dict, QuantityValue]])

slots.Biosample_tot_org_c_meth = Slot(uri=MIXS['0000337'], name="Biosample_tot_org_c_meth", curie=MIXS.curie('0000337'),
                   model_uri=NMDC.Biosample_tot_org_c_meth, domain=Biosample, range=Optional[Union[dict, TextValue]])

slots.Biosample_tot_org_carb = Slot(uri=MIXS['0000533'], name="Biosample_tot_org_carb", curie=MIXS.curie('0000533'),
                   model_uri=NMDC.Biosample_tot_org_carb, domain=Biosample, range=Optional[Union[dict, QuantityValue]])

slots.Biosample_salinity_meth = Slot(uri=MIXS['0000341'], name="Biosample_salinity_meth", curie=MIXS.curie('0000341'),
                   model_uri=NMDC.Biosample_salinity_meth, domain=Biosample, range=Optional[Union[dict, TextValue]])

slots.Biosample_sieving = Slot(uri=MIXS['0000322'], name="Biosample_sieving", curie=MIXS.curie('0000322'),
                   model_uri=NMDC.Biosample_sieving, domain=Biosample, range=Optional[Union[dict, TextValue]])

slots.Biosample_climate_environment = Slot(uri=MIXS['0001040'], name="Biosample_climate_environment", curie=MIXS.curie('0001040'),
                   model_uri=NMDC.Biosample_climate_environment, domain=Biosample, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.Biosample_gaseous_environment = Slot(uri=MIXS['0000558'], name="Biosample_gaseous_environment", curie=MIXS.curie('0000558'),
                   model_uri=NMDC.Biosample_gaseous_environment, domain=Biosample, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.Biosample_watering_regm = Slot(uri=MIXS['0000591'], name="Biosample_watering_regm", curie=MIXS.curie('0000591'),
                   model_uri=NMDC.Biosample_watering_regm, domain=Biosample, range=Optional[Union[Union[dict, TextValue], List[Union[dict, TextValue]]]])

slots.Biosample_source_mat_id = Slot(uri=MIXS['0000026'], name="Biosample_source_mat_id", curie=MIXS.curie('0000026'),
                   model_uri=NMDC.Biosample_source_mat_id, domain=Biosample, range=Optional[Union[dict, TextValue]])

slots.MaterialProcessing_has_input = Slot(uri=NMDC.has_input, name="MaterialProcessing_has_input", curie=NMDC.curie('has_input'),
                   model_uri=NMDC.MaterialProcessing_has_input, domain=MaterialProcessing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]],
                   pattern=re.compile(r'.*'))

slots.MaterialProcessing_has_output = Slot(uri=NMDC.has_output, name="MaterialProcessing_has_output", curie=NMDC.curie('has_output'),
                   model_uri=NMDC.MaterialProcessing_has_output, domain=MaterialProcessing, range=Optional[Union[Union[str, ProcessedSampleId], List[Union[str, ProcessedSampleId]]]],
                   pattern=re.compile(r'.*'))

slots.ProcessedSample_id = Slot(uri=NMDC.id, name="ProcessedSample_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.ProcessedSample_id, domain=ProcessedSample, range=Union[str, ProcessedSampleId],
                   pattern=re.compile(r'.*'))

slots.ProteinQuantification_best_protein = Slot(uri=NMDC.best_protein, name="ProteinQuantification_best_protein", curie=NMDC.curie('best_protein'),
                   model_uri=NMDC.ProteinQuantification_best_protein, domain=ProteinQuantification, range=Optional[Union[str, GeneProductId]])

slots.ProteinQuantification_all_proteins = Slot(uri=NMDC.all_proteins, name="ProteinQuantification_all_proteins", curie=NMDC.curie('all_proteins'),
                   model_uri=NMDC.ProteinQuantification_all_proteins, domain=ProteinQuantification, range=Optional[Union[Union[str, GeneProductId], List[Union[str, GeneProductId]]]])

slots.GenomeFeature_seqid = Slot(uri=NMDC.seqid, name="GenomeFeature_seqid", curie=NMDC.curie('seqid'),
                   model_uri=NMDC.GenomeFeature_seqid, domain=GenomeFeature, range=str)

slots.GenomeFeature_start = Slot(uri=NMDC.start, name="GenomeFeature_start", curie=NMDC.curie('start'),
                   model_uri=NMDC.GenomeFeature_start, domain=GenomeFeature, range=int)

slots.GenomeFeature_end = Slot(uri=NMDC.end, name="GenomeFeature_end", curie=NMDC.curie('end'),
                   model_uri=NMDC.GenomeFeature_end, domain=GenomeFeature, range=int)

slots.FunctionalAnnotation_has_function = Slot(uri=NMDC.has_function, name="FunctionalAnnotation_has_function", curie=NMDC.curie('has_function'),
                   model_uri=NMDC.FunctionalAnnotation_has_function, domain=FunctionalAnnotation, range=Optional[str],
                   pattern=re.compile(r'^(KEGG_PATHWAY:\w{2,4}\d{5}|KEGG.REACTION:R\d+|RHEA:\d{5}|MetaCyc:[A-Za-z0-9+_.%-:]+|EC:\d{1,2}(\.\d{0,3}){0,3}|GO:\d{7}|MetaNetX:(MNXR\d+|EMPTY)|SEED:\w+|KEGG\.ORTHOLOGY:K\d+|EGGNOG:\w+|PFAM:PF\d{5}|TIGRFAM:TIGR\d+|SUPFAM:\w+|CATH:[1-6]\.[0-9]+\.[0-9]+\.[0-9]+|PANTHER.FAMILY:PTHR\d{5}(\:SF\d{1,3})?)$'))

slots.FunctionalAnnotation_was_generated_by = Slot(uri=NMDC.was_generated_by, name="FunctionalAnnotation_was_generated_by", curie=NMDC.curie('was_generated_by'),
                   model_uri=NMDC.FunctionalAnnotation_was_generated_by, domain=FunctionalAnnotation, range=Optional[Union[str, MetagenomeAnnotationId]], mappings = [PROV["wasGeneratedBy"]],
                   pattern=re.compile(r'.*'))

slots.QuantityValue_has_raw_value = Slot(uri=NMDC.has_raw_value, name="QuantityValue_has_raw_value", curie=NMDC.curie('has_raw_value'),
                   model_uri=NMDC.QuantityValue_has_raw_value, domain=QuantityValue, range=Optional[str])

slots.QuantityValue_has_unit = Slot(uri=NMDC.has_unit, name="QuantityValue_has_unit", curie=NMDC.curie('has_unit'),
                   model_uri=NMDC.QuantityValue_has_unit, domain=QuantityValue, range=Optional[str], mappings = [QUD["unit"], SCHEMA["unitCode"]])

slots.QuantityValue_has_numeric_value = Slot(uri=NMDC.has_numeric_value, name="QuantityValue_has_numeric_value", curie=NMDC.curie('has_numeric_value'),
                   model_uri=NMDC.QuantityValue_has_numeric_value, domain=QuantityValue, range=Optional[Decimal], mappings = [QUD["quantityValue"], SCHEMA["value"]])

slots.PersonValue_orcid = Slot(uri=NMDC.orcid, name="PersonValue_orcid", curie=NMDC.curie('orcid'),
                   model_uri=NMDC.PersonValue_orcid, domain=PersonValue, range=Optional[str])

slots.PersonValue_email = Slot(uri=SCHEMA.email, name="PersonValue_email", curie=SCHEMA.curie('email'),
                   model_uri=NMDC.PersonValue_email, domain=PersonValue, range=Optional[str])

slots.PersonValue_has_raw_value = Slot(uri=NMDC.has_raw_value, name="PersonValue_has_raw_value", curie=NMDC.curie('has_raw_value'),
                   model_uri=NMDC.PersonValue_has_raw_value, domain=PersonValue, range=Optional[str])

slots.PersonValue_name = Slot(uri=NMDC.name, name="PersonValue_name", curie=NMDC.curie('name'),
                   model_uri=NMDC.PersonValue_name, domain=PersonValue, range=Optional[str])

slots.ControlledIdentifiedTermValue_term = Slot(uri=NMDC.term, name="ControlledIdentifiedTermValue_term", curie=NMDC.curie('term'),
                   model_uri=NMDC.ControlledIdentifiedTermValue_term, domain=ControlledIdentifiedTermValue, range=Union[dict, "OntologyClass"])

slots.GeolocationValue_has_raw_value = Slot(uri=NMDC.has_raw_value, name="GeolocationValue_has_raw_value", curie=NMDC.curie('has_raw_value'),
                   model_uri=NMDC.GeolocationValue_has_raw_value, domain=GeolocationValue, range=Optional[str])

slots.GeolocationValue_latitude = Slot(uri=WGS84.lat, name="GeolocationValue_latitude", curie=WGS84.curie('lat'),
                   model_uri=NMDC.GeolocationValue_latitude, domain=GeolocationValue, range=float, mappings = [SCHEMA["latitude"]])

slots.GeolocationValue_longitude = Slot(uri=WGS84.long, name="GeolocationValue_longitude", curie=WGS84.curie('long'),
                   model_uri=NMDC.GeolocationValue_longitude, domain=GeolocationValue, range=float, mappings = [SCHEMA["longitude"]])

slots.OntologyClass_id = Slot(uri=NMDC.id, name="OntologyClass_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.OntologyClass_id, domain=OntologyClass, range=Union[str, OntologyClassId],
                   pattern=re.compile(r'.*'))

slots.Instrument_id = Slot(uri=NMDC.id, name="Instrument_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.Instrument_id, domain=Instrument, range=Union[str, InstrumentId],
                   pattern=re.compile(r'.*'))

slots.Study_id = Slot(uri=NMDC.id, name="Study_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.Study_id, domain=Study, range=Union[str, StudyId],
                   pattern=re.compile(r'.*'))

slots.Study_name = Slot(uri=NMDC.name, name="Study_name", curie=NMDC.curie('name'),
                   model_uri=NMDC.Study_name, domain=Study, range=Optional[str])

slots.Study_websites = Slot(uri=NMDC.websites, name="Study_websites", curie=NMDC.curie('websites'),
                   model_uri=NMDC.Study_websites, domain=Study, range=Optional[Union[str, List[str]]],
                   pattern=re.compile(r'^[Hh][Tt][Tt][Pp][Ss]?:\/\/(?!.*[Dd][Oo][Ii]\.[Oo][Rr][Gg]).*$'))

slots.Study_homepage_website = Slot(uri=NMDC.homepage_website, name="Study_homepage_website", curie=NMDC.curie('homepage_website'),
                   model_uri=NMDC.Study_homepage_website, domain=Study, range=Optional[Union[str, List[str]]],
                   pattern=re.compile(r'^[Hh][Tt][Tt][Pp][Ss]?:\/\/(?!.*[Dd][Oo][Ii]\.[Oo][Rr][Gg]).*$'))

slots.Study_description = Slot(uri=DCTERMS.description, name="Study_description", curie=DCTERMS.curie('description'),
                   model_uri=NMDC.Study_description, domain=Study, range=Optional[str])

slots.Study_notes = Slot(uri=NMDC.notes, name="Study_notes", curie=NMDC.curie('notes'),
                   model_uri=NMDC.Study_notes, domain=Study, range=Optional[str])

slots.Study_alternative_identifiers = Slot(uri=NMDC.alternative_identifiers, name="Study_alternative_identifiers", curie=NMDC.curie('alternative_identifiers'),
                   model_uri=NMDC.Study_alternative_identifiers, domain=Study, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]],
                   pattern=re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$'))

slots.Study_alternative_names = Slot(uri=NMDC.alternative_names, name="Study_alternative_names", curie=NMDC.curie('alternative_names'),
                   model_uri=NMDC.Study_alternative_names, domain=Study, range=Optional[Union[str, List[str]]])

slots.Study_related_identifiers = Slot(uri=NMDC.related_identifiers, name="Study_related_identifiers", curie=NMDC.curie('related_identifiers'),
                   model_uri=NMDC.Study_related_identifiers, domain=Study, range=Optional[str])

slots.Study_insdc_bioproject_identifiers = Slot(uri=NMDC.insdc_bioproject_identifiers, name="Study_insdc_bioproject_identifiers", curie=NMDC.curie('insdc_bioproject_identifiers'),
                   model_uri=NMDC.Study_insdc_bioproject_identifiers, domain=Study, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^bioproject:PRJ[DEN][A-Z][0-9]+$'))

slots.Study_part_of = Slot(uri=DCTERMS.isPartOf, name="Study_part_of", curie=DCTERMS.curie('isPartOf'),
                   model_uri=NMDC.Study_part_of, domain=Study, range=Optional[Union[Union[str, StudyId], List[Union[str, StudyId]]]],
                   pattern=re.compile(r'.*'))

slots.Study_protocol_link = Slot(uri=NMDC.protocol_link, name="Study_protocol_link", curie=NMDC.curie('protocol_link'),
                   model_uri=NMDC.Study_protocol_link, domain=Study, range=Optional[Union[Union[dict, Protocol], List[Union[dict, Protocol]]]])

slots.DataObject_name = Slot(uri=NMDC.name, name="DataObject_name", curie=NMDC.curie('name'),
                   model_uri=NMDC.DataObject_name, domain=DataObject, range=str)

slots.DataObject_description = Slot(uri=DCTERMS.description, name="DataObject_description", curie=DCTERMS.curie('description'),
                   model_uri=NMDC.DataObject_description, domain=DataObject, range=str)

slots.DataObject_id = Slot(uri=NMDC.id, name="DataObject_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.DataObject_id, domain=DataObject, range=Union[str, DataObjectId],
                   pattern=re.compile(r'.*'))

slots.DataObject_was_generated_by = Slot(uri=NMDC.was_generated_by, name="DataObject_was_generated_by", curie=NMDC.curie('was_generated_by'),
                   model_uri=NMDC.DataObject_was_generated_by, domain=DataObject, range=Optional[Union[str, WorkflowExecutionId]], mappings = [PROV["wasGeneratedBy"]],
                   pattern=re.compile(r'.*'))

slots.DataGeneration_has_input = Slot(uri=NMDC.has_input, name="DataGeneration_has_input", curie=NMDC.curie('has_input'),
                   model_uri=NMDC.DataGeneration_has_input, domain=DataGeneration, range=Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]],
                   pattern=re.compile(r'.*'))

slots.DataGeneration_associated_studies = Slot(uri=NMDC.associated_studies, name="DataGeneration_associated_studies", curie=NMDC.curie('associated_studies'),
                   model_uri=NMDC.DataGeneration_associated_studies, domain=DataGeneration, range=Union[Union[str, StudyId], List[Union[str, StudyId]]],
                   pattern=re.compile(r'.*'))

slots.DataGeneration_has_output = Slot(uri=NMDC.has_output, name="DataGeneration_has_output", curie=NMDC.curie('has_output'),
                   model_uri=NMDC.DataGeneration_has_output, domain=DataGeneration, range=Optional[Union[Union[str, DataObjectId], List[Union[str, DataObjectId]]]],
                   pattern=re.compile(r'.*'))

slots.DataGeneration_part_of = Slot(uri=DCTERMS.isPartOf, name="DataGeneration_part_of", curie=DCTERMS.curie('isPartOf'),
                   model_uri=NMDC.DataGeneration_part_of, domain=DataGeneration, range=Optional[Union[Union[str, DataGenerationId], List[Union[str, DataGenerationId]]]],
                   pattern=re.compile(r'.*'))

slots.WorkflowExecution_started_at_time = Slot(uri=NMDC.started_at_time, name="WorkflowExecution_started_at_time", curie=NMDC.curie('started_at_time'),
                   model_uri=NMDC.WorkflowExecution_started_at_time, domain=WorkflowExecution, range=str, mappings = [PROV["startedAtTime"]],
                   pattern=re.compile(r'^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$'))

slots.WorkflowExecution_git_url = Slot(uri=NMDC.git_url, name="WorkflowExecution_git_url", curie=NMDC.curie('git_url'),
                   model_uri=NMDC.WorkflowExecution_git_url, domain=WorkflowExecution, range=str)

slots.WorkflowExecution_has_input = Slot(uri=NMDC.has_input, name="WorkflowExecution_has_input", curie=NMDC.curie('has_input'),
                   model_uri=NMDC.WorkflowExecution_has_input, domain=WorkflowExecution, range=Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]],
                   pattern=re.compile(r'.*'))

slots.WorkflowExecution_has_output = Slot(uri=NMDC.has_output, name="WorkflowExecution_has_output", curie=NMDC.curie('has_output'),
                   model_uri=NMDC.WorkflowExecution_has_output, domain=WorkflowExecution, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]],
                   pattern=re.compile(r'.*'))

slots.WorkflowExecution_execution_resource = Slot(uri=NMDC.execution_resource, name="WorkflowExecution_execution_resource", curie=NMDC.curie('execution_resource'),
                   model_uri=NMDC.WorkflowExecution_execution_resource, domain=WorkflowExecution, range=Union[str, "ExecutionResourceEnum"])

slots.WorkflowExecution_was_informed_by = Slot(uri=NMDC.was_informed_by, name="WorkflowExecution_was_informed_by", curie=NMDC.curie('was_informed_by'),
                   model_uri=NMDC.WorkflowExecution_was_informed_by, domain=WorkflowExecution, range=Union[str, DataGenerationId], mappings = [PROV["wasInformedBy"]])

slots.MetagenomeAssembly_id = Slot(uri=NMDC.id, name="MetagenomeAssembly_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.MetagenomeAssembly_id, domain=MetagenomeAssembly, range=Union[str, MetagenomeAssemblyId],
                   pattern=re.compile(r'.*'))

slots.MetagenomeAssembly_was_informed_by = Slot(uri=NMDC.was_informed_by, name="MetagenomeAssembly_was_informed_by", curie=NMDC.curie('was_informed_by'),
                   model_uri=NMDC.MetagenomeAssembly_was_informed_by, domain=MetagenomeAssembly, range=Union[str, DataGenerationId], mappings = [PROV["wasInformedBy"]],
                   pattern=re.compile(r'.*'))

slots.MetatranscriptomeAssembly_id = Slot(uri=NMDC.id, name="MetatranscriptomeAssembly_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.MetatranscriptomeAssembly_id, domain=MetatranscriptomeAssembly, range=Union[str, MetatranscriptomeAssemblyId],
                   pattern=re.compile(r'.*'))

slots.MetatranscriptomeAssembly_was_informed_by = Slot(uri=NMDC.was_informed_by, name="MetatranscriptomeAssembly_was_informed_by", curie=NMDC.curie('was_informed_by'),
                   model_uri=NMDC.MetatranscriptomeAssembly_was_informed_by, domain=MetatranscriptomeAssembly, range=Union[str, DataGenerationId], mappings = [PROV["wasInformedBy"]],
                   pattern=re.compile(r'.*'))

slots.MetatranscriptomeAnnotation_id = Slot(uri=NMDC.id, name="MetatranscriptomeAnnotation_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.MetatranscriptomeAnnotation_id, domain=MetatranscriptomeAnnotation, range=Union[str, MetatranscriptomeAnnotationId],
                   pattern=re.compile(r'.*'))

slots.MetatranscriptomeAnnotation_img_identifiers = Slot(uri=NMDC.img_identifiers, name="MetatranscriptomeAnnotation_img_identifiers", curie=NMDC.curie('img_identifiers'),
                   model_uri=NMDC.MetatranscriptomeAnnotation_img_identifiers, domain=MetatranscriptomeAnnotation, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^img\.taxon:[a-zA-Z0-9_][a-zA-Z0-9_\/\.]*$'))

slots.MetatranscriptomeAnnotation_has_input = Slot(uri=NMDC.has_input, name="MetatranscriptomeAnnotation_has_input", curie=NMDC.curie('has_input'),
                   model_uri=NMDC.MetatranscriptomeAnnotation_has_input, domain=MetatranscriptomeAnnotation, range=Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]],
                   pattern=re.compile(r'.*'))

slots.MetatranscriptomeAnnotation_has_output = Slot(uri=NMDC.has_output, name="MetatranscriptomeAnnotation_has_output", curie=NMDC.curie('has_output'),
                   model_uri=NMDC.MetatranscriptomeAnnotation_has_output, domain=MetatranscriptomeAnnotation, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]],
                   pattern=re.compile(r'.*'))

slots.MetatranscriptomeAnnotation_was_informed_by = Slot(uri=NMDC.was_informed_by, name="MetatranscriptomeAnnotation_was_informed_by", curie=NMDC.curie('was_informed_by'),
                   model_uri=NMDC.MetatranscriptomeAnnotation_was_informed_by, domain=MetatranscriptomeAnnotation, range=Union[str, DataGenerationId], mappings = [PROV["wasInformedBy"]],
                   pattern=re.compile(r'.*'))

slots.MetatranscriptomeAnnotation_gold_analysis_project_identifiers = Slot(uri=NMDC.gold_analysis_project_identifiers, name="MetatranscriptomeAnnotation_gold_analysis_project_identifiers", curie=NMDC.curie('gold_analysis_project_identifiers'),
                   model_uri=NMDC.MetatranscriptomeAnnotation_gold_analysis_project_identifiers, domain=MetatranscriptomeAnnotation, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'.*'))

slots.MetatranscriptomeAnalysis_id = Slot(uri=NMDC.id, name="MetatranscriptomeAnalysis_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.MetatranscriptomeAnalysis_id, domain=MetatranscriptomeAnalysis, range=Union[str, MetatranscriptomeAnalysisId],
                   pattern=re.compile(r'.*'))

slots.MetatranscriptomeAnalysis_img_identifiers = Slot(uri=NMDC.img_identifiers, name="MetatranscriptomeAnalysis_img_identifiers", curie=NMDC.curie('img_identifiers'),
                   model_uri=NMDC.MetatranscriptomeAnalysis_img_identifiers, domain=MetatranscriptomeAnalysis, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^img\.taxon:[a-zA-Z0-9_][a-zA-Z0-9_\/\.]*$'))

slots.MetatranscriptomeAnalysis_was_informed_by = Slot(uri=NMDC.was_informed_by, name="MetatranscriptomeAnalysis_was_informed_by", curie=NMDC.curie('was_informed_by'),
                   model_uri=NMDC.MetatranscriptomeAnalysis_was_informed_by, domain=MetatranscriptomeAnalysis, range=Union[str, DataGenerationId], mappings = [PROV["wasInformedBy"]],
                   pattern=re.compile(r'.*'))

slots.MagsAnalysis_id = Slot(uri=NMDC.id, name="MagsAnalysis_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.MagsAnalysis_id, domain=MagsAnalysis, range=Union[str, MagsAnalysisId],
                   pattern=re.compile(r'.*'))

slots.MagsAnalysis_img_identifiers = Slot(uri=NMDC.img_identifiers, name="MagsAnalysis_img_identifiers", curie=NMDC.curie('img_identifiers'),
                   model_uri=NMDC.MagsAnalysis_img_identifiers, domain=MagsAnalysis, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^img\.taxon:[a-zA-Z0-9_][a-zA-Z0-9_\/\.]*$'))

slots.MagsAnalysis_was_informed_by = Slot(uri=NMDC.was_informed_by, name="MagsAnalysis_was_informed_by", curie=NMDC.curie('was_informed_by'),
                   model_uri=NMDC.MagsAnalysis_was_informed_by, domain=MagsAnalysis, range=Union[str, DataGenerationId], mappings = [PROV["wasInformedBy"]],
                   pattern=re.compile(r'.*'))

slots.MetagenomeSequencing_id = Slot(uri=NMDC.id, name="MetagenomeSequencing_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.MetagenomeSequencing_id, domain=MetagenomeSequencing, range=Union[str, MetagenomeSequencingId],
                   pattern=re.compile(r'.*'))

slots.MetagenomeSequencing_has_input = Slot(uri=NMDC.has_input, name="MetagenomeSequencing_has_input", curie=NMDC.curie('has_input'),
                   model_uri=NMDC.MetagenomeSequencing_has_input, domain=MetagenomeSequencing, range=Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]],
                   pattern=re.compile(r'.*'))

slots.MetagenomeSequencing_was_informed_by = Slot(uri=NMDC.was_informed_by, name="MetagenomeSequencing_was_informed_by", curie=NMDC.curie('was_informed_by'),
                   model_uri=NMDC.MetagenomeSequencing_was_informed_by, domain=MetagenomeSequencing, range=Union[str, DataGenerationId], mappings = [PROV["wasInformedBy"]],
                   pattern=re.compile(r'.*'))

slots.ReadQcAnalysis_id = Slot(uri=NMDC.id, name="ReadQcAnalysis_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.ReadQcAnalysis_id, domain=ReadQcAnalysis, range=Union[str, ReadQcAnalysisId],
                   pattern=re.compile(r'.*'))

slots.ReadQcAnalysis_was_informed_by = Slot(uri=NMDC.was_informed_by, name="ReadQcAnalysis_was_informed_by", curie=NMDC.curie('was_informed_by'),
                   model_uri=NMDC.ReadQcAnalysis_was_informed_by, domain=ReadQcAnalysis, range=Union[str, DataGenerationId], mappings = [PROV["wasInformedBy"]],
                   pattern=re.compile(r'.*'))

slots.ReadBasedTaxonomyAnalysis_id = Slot(uri=NMDC.id, name="ReadBasedTaxonomyAnalysis_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.ReadBasedTaxonomyAnalysis_id, domain=ReadBasedTaxonomyAnalysis, range=Union[str, ReadBasedTaxonomyAnalysisId],
                   pattern=re.compile(r'.*'))

slots.ReadBasedTaxonomyAnalysis_was_informed_by = Slot(uri=NMDC.was_informed_by, name="ReadBasedTaxonomyAnalysis_was_informed_by", curie=NMDC.curie('was_informed_by'),
                   model_uri=NMDC.ReadBasedTaxonomyAnalysis_was_informed_by, domain=ReadBasedTaxonomyAnalysis, range=Union[str, DataGenerationId], mappings = [PROV["wasInformedBy"]],
                   pattern=re.compile(r'.*'))

slots.MetabolomicsAnalysis_id = Slot(uri=NMDC.id, name="MetabolomicsAnalysis_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.MetabolomicsAnalysis_id, domain=MetabolomicsAnalysis, range=Union[str, MetabolomicsAnalysisId],
                   pattern=re.compile(r'.*'))

slots.MetabolomicsAnalysis_was_informed_by = Slot(uri=NMDC.was_informed_by, name="MetabolomicsAnalysis_was_informed_by", curie=NMDC.curie('was_informed_by'),
                   model_uri=NMDC.MetabolomicsAnalysis_was_informed_by, domain=MetabolomicsAnalysis, range=Union[str, DataGenerationId], mappings = [PROV["wasInformedBy"]],
                   pattern=re.compile(r'.*'))

slots.MetaproteomicsAnalysis_id = Slot(uri=NMDC.id, name="MetaproteomicsAnalysis_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.MetaproteomicsAnalysis_id, domain=MetaproteomicsAnalysis, range=Union[str, MetaproteomicsAnalysisId],
                   pattern=re.compile(r'.*'))

slots.MetaproteomicsAnalysis_was_informed_by = Slot(uri=NMDC.was_informed_by, name="MetaproteomicsAnalysis_was_informed_by", curie=NMDC.curie('was_informed_by'),
                   model_uri=NMDC.MetaproteomicsAnalysis_was_informed_by, domain=MetaproteomicsAnalysis, range=Union[str, DataGenerationId], mappings = [PROV["wasInformedBy"]],
                   pattern=re.compile(r'.*'))

slots.NomAnalysis_id = Slot(uri=NMDC.id, name="NomAnalysis_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.NomAnalysis_id, domain=NomAnalysis, range=Union[str, NomAnalysisId],
                   pattern=re.compile(r'.*'))

slots.NomAnalysis_was_informed_by = Slot(uri=NMDC.was_informed_by, name="NomAnalysis_was_informed_by", curie=NMDC.curie('was_informed_by'),
                   model_uri=NMDC.NomAnalysis_was_informed_by, domain=NomAnalysis, range=Union[str, DataGenerationId], mappings = [PROV["wasInformedBy"]],
                   pattern=re.compile(r'.*'))

slots.CalibrationInformation_internal_calibration = Slot(uri=NMDC.internal_calibration, name="CalibrationInformation_internal_calibration", curie=NMDC.curie('internal_calibration'),
                   model_uri=NMDC.CalibrationInformation_internal_calibration, domain=CalibrationInformation, range=Union[bool, Bool])

slots.CalibrationInformation_calibration_target = Slot(uri=NMDC.calibration_target, name="CalibrationInformation_calibration_target", curie=NMDC.curie('calibration_target'),
                   model_uri=NMDC.CalibrationInformation_calibration_target, domain=CalibrationInformation, range=Union[str, "CalibrationTargetEnum"])

slots.CalibrationInformation_id = Slot(uri=NMDC.id, name="CalibrationInformation_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.CalibrationInformation_id, domain=CalibrationInformation, range=Union[str, CalibrationInformationId],
                   pattern=re.compile(r'.*'))
