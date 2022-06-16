# Auto generated from annotation.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-06-15T10:43:01
# Schema: NMDC-Annotation
#
# id: https://microbiomedata/schema/annotation
# description: This module in the schema is for representing annotations including functional annotations of
#              proteins and other gene products, as well as controlled terms for describing things like
#              metabolites
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
version = None

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
HMDB = CurieNamespace('HMDB', 'http://identifiers.org/hmdb/')
KEGG_COMPOUND = CurieNamespace('KEGG_COMPOUND', 'http://identifiers.org/kegg.compound/')
KEGG_ORTHOLOGY = CurieNamespace('KEGG_ORTHOLOGY', 'http://identifiers.org/kegg.orthology/')
KEGG_PATHWAY = CurieNamespace('KEGG_PATHWAY', 'http://identifiers.org/kegg.pathway/')
KEGG_REACTION = CurieNamespace('KEGG_REACTION', 'http://identifiers.org/kegg.reaction/')
MESH = CurieNamespace('MESH', 'http://identifiers.org/mesh/')
METACYC = CurieNamespace('MetaCyc', 'http://example.org/UNKNOWN/MetaCyc/')
METANETX = CurieNamespace('MetaNetX', 'http://example.org/UNKNOWN/MetaNetX/')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
PANTHER_FAMILY = CurieNamespace('PANTHER_FAMILY', 'http://identifiers.org/panther.family/')
PFAM = CurieNamespace('PFAM', 'http://identifiers.org/pfam/')
PR = CurieNamespace('PR', 'http://purl.obolibrary.org/obo/PR_')
PUBCHEM_COMPOUND = CurieNamespace('PUBCHEM_COMPOUND', 'http://identifiers.org/pubchem.compound/')
RHEA = CurieNamespace('RHEA', 'http://identifiers.org/rhea/')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
RETRORULES = CurieNamespace('RetroRules', 'http://example.org/UNKNOWN/RetroRules/')
SEED = CurieNamespace('SEED', 'http://identifiers.org/seed/')
SUPFAM = CurieNamespace('SUPFAM', 'http://identifiers.org/supfam/')
TIGRFAM = CurieNamespace('TIGRFAM', 'http://identifiers.org/tigrfam/')
UNIPROTKB = CurieNamespace('UniProtKB', 'http://example.org/UNKNOWN/UniProtKB/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
GTPO = CurieNamespace('gtpo', 'http://example.org/UNKNOWN/gtpo/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NMDC = CurieNamespace('nmdc', 'https://microbiomedata/meta/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
QUD = CurieNamespace('qud', 'http://qudt.org/1.1/schema/qudt#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SIO = CurieNamespace('sio', 'http://semanticscience.org/resource/SIO_')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
WGS = CurieNamespace('wgs', 'http://www.w3.org/2003/01/geo/wgs84_pos')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CurieNamespace('', 'https://microbiomedata/schema/annotation/')


# Types
class Bytes(int):
    """ An integer value that corresponds to a size in bytes """
    type_class_uri = XSD.int
    type_class_curie = "xsd:int"
    type_name = "bytes"
    type_model_uri = URIRef("https://microbiomedata/schema/annotation/Bytes")


class DecimalDegree(float):
    """ A decimal degree expresses latitude or longitude as decimal fractions. """
    type_class_uri = XSD.decimal
    type_class_curie = "xsd:decimal"
    type_name = "decimal degree"
    type_model_uri = URIRef("https://microbiomedata/schema/annotation/DecimalDegree")


class LanguageCode(str):
    """ A language code conforming to ISO_639-1 """
    type_class_uri = XSD.language
    type_class_curie = "xsd:language"
    type_name = "language code"
    type_model_uri = URIRef("https://microbiomedata/schema/annotation/LanguageCode")


class Unit(str):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "unit"
    type_model_uri = URIRef("https://microbiomedata/schema/annotation/Unit")


class ExternalIdentifier(Uriorcurie):
    """ A CURIE representing an external identifier """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "external identifier"
    type_model_uri = URIRef("https://microbiomedata/schema/annotation/ExternalIdentifier")


# Class references
class ActivityId(extended_str):
    pass


class NamedThingId(extended_str):
    pass


class OntologyClassId(NamedThingId):
    pass


class FunctionalAnnotationTermId(OntologyClassId):
    pass


class PathwayId(FunctionalAnnotationTermId):
    pass


class ReactionId(FunctionalAnnotationTermId):
    pass


class OrthologyGroupId(FunctionalAnnotationTermId):
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


@dataclass
class GenomeFeature(YAMLRoot):
    """
    A feature localized to an interval along a genome
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/GenomeFeature")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "genome feature"
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/GenomeFeature")

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
class ReactionParticipant(YAMLRoot):
    """
    Instances of this link a reaction to a chemical entity participant
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/ReactionParticipant")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "reaction participant"
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/ReactionParticipant")

    chemical: Optional[Union[str, ChemicalEntityId]] = None
    stoichiometry: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.chemical is not None and not isinstance(self.chemical, ChemicalEntityId):
            self.chemical = ChemicalEntityId(self.chemical)

        if self.stoichiometry is not None and not isinstance(self.stoichiometry, int):
            self.stoichiometry = int(self.stoichiometry)

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/FunctionalAnnotation")

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


@dataclass
class Activity(YAMLRoot):
    """
    a provence-generating activity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.Activity
    class_class_curie: ClassVar[str] = "nmdc:Activity"
    class_name: ClassVar[str] = "activity"
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/Activity")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/Agent")

    acted_on_behalf_of: Optional[Union[dict, "Agent"]] = None
    was_informed_by: Optional[Union[str, ActivityId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.acted_on_behalf_of is not None and not isinstance(self.acted_on_behalf_of, Agent):
            self.acted_on_behalf_of = Agent(**as_dict(self.acted_on_behalf_of))

        if self.was_informed_by is not None and not isinstance(self.was_informed_by, ActivityId):
            self.was_informed_by = ActivityId(self.was_informed_by)

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/NamedThing")

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
class OntologyClass(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.OntologyClass
    class_class_curie: ClassVar[str] = "nmdc:OntologyClass"
    class_name: ClassVar[str] = "ontology class"
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/OntologyClass")

    id: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/FunctionalAnnotationTerm")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/Pathway")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/Reaction")

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
class OrthologyGroup(FunctionalAnnotationTerm):
    """
    A set of genes or gene products in which all members are orthologous
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/OrthologyGroup")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "orthology group"
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/OrthologyGroup")

    id: Union[str, OrthologyGroupId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrthologyGroupId):
            self.id = OrthologyGroupId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EnvironmentalMaterialTerm(OntologyClass):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.EnvironmentalMaterialTerm
    class_class_curie: ClassVar[str] = "nmdc:EnvironmentalMaterialTerm"
    class_name: ClassVar[str] = "environmental material term"
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/EnvironmentalMaterialTerm")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/AttributeValue")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/QuantityValue")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/ImageValue")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/PersonValue")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/Person")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/MAGBin")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/Instrument")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/MetaboliteQuantification")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/PeptideQuantification")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/ProteinQuantification")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/ChemicalEntity")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/GeneProduct")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/TextValue")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/UrlValue")


class TimestampValue(AttributeValue):
    """
    A value that is a timestamp. The range should be ISO-8601
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.TimestampValue
    class_class_curie: ClassVar[str] = "nmdc:TimestampValue"
    class_name: ClassVar[str] = "timestamp value"
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/TimestampValue")


@dataclass
class IntegerValue(AttributeValue):
    """
    A value that is an integer
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.IntegerValue
    class_class_curie: ClassVar[str] = "nmdc:IntegerValue"
    class_name: ClassVar[str] = "integer value"
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/IntegerValue")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/BooleanValue")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/ControlledTermValue")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/GeolocationValue")

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
class WorkflowExecutionActivity(Activity):
    """
    Represents an instance of an execution of a particular workflow
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/workflow_execution_activity/WorkflowExecutionActivity")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "workflow execution activity"
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/WorkflowExecutionActivity")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/MetagenomeAssembly")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/MetatranscriptomeAssembly")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/MetagenomeAnnotationActivity")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/MetatranscriptomeAnnotationActivity")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/MetatranscriptomeActivity")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/MAGsAnalysisActivity")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/ReadQCAnalysisActivity")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/ReadBasedAnalysisActivity")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/MetabolomicsAnalysisActivity")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/MetaproteomicsAnalysisActivity")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/annotation/NomAnalysisActivity")

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


# Enumerations


# Slots
class slots:
    pass

slots.subject = Slot(uri=DEFAULT_.subject, name="subject", curie=DEFAULT_.curie('subject'),
                   model_uri=DEFAULT_.subject, domain=None, range=Optional[Union[str, GeneProductId]])

slots.has_function = Slot(uri=DEFAULT_.has_function, name="has function", curie=DEFAULT_.curie('has_function'),
                   model_uri=DEFAULT_.has_function, domain=None, range=Optional[str])

slots.has_participants = Slot(uri=DEFAULT_.has_participants, name="has participants", curie=DEFAULT_.curie('has_participants'),
                   model_uri=DEFAULT_.has_participants, domain=None, range=Optional[str])

slots.gff_coordinate = Slot(uri=DEFAULT_.gff_coordinate, name="gff coordinate", curie=DEFAULT_.curie('gff_coordinate'),
                   model_uri=DEFAULT_.gff_coordinate, domain=None, range=Optional[int])

slots.started_at_time = Slot(uri=NMDC.started_at_time, name="started at time", curie=NMDC.curie('started_at_time'),
                   model_uri=DEFAULT_.started_at_time, domain=None, range=Optional[Union[str, XSDDateTime]], mappings = [PROV.startedAtTime],
                   pattern=re.compile(r'^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$'))

slots.ended_at_time = Slot(uri=NMDC.ended_at_time, name="ended at time", curie=NMDC.curie('ended_at_time'),
                   model_uri=DEFAULT_.ended_at_time, domain=None, range=Optional[Union[str, XSDDateTime]], mappings = [PROV.endedAtTime],
                   pattern=re.compile(r'^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$'))

slots.was_informed_by = Slot(uri=NMDC.was_informed_by, name="was informed by", curie=NMDC.curie('was_informed_by'),
                   model_uri=DEFAULT_.was_informed_by, domain=None, range=Optional[Union[str, ActivityId]], mappings = [PROV.wasInformedBy])

slots.was_associated_with = Slot(uri=NMDC.was_associated_with, name="was associated with", curie=NMDC.curie('was_associated_with'),
                   model_uri=DEFAULT_.was_associated_with, domain=None, range=Optional[Union[dict, Agent]], mappings = [PROV.wasAssociatedWith])

slots.acted_on_behalf_of = Slot(uri=NMDC.acted_on_behalf_of, name="acted on behalf of", curie=NMDC.curie('acted_on_behalf_of'),
                   model_uri=DEFAULT_.acted_on_behalf_of, domain=None, range=Optional[Union[dict, Agent]], mappings = [PROV.actedOnBehalfOf])

slots.was_generated_by = Slot(uri=NMDC.was_generated_by, name="was generated by", curie=NMDC.curie('was_generated_by'),
                   model_uri=DEFAULT_.was_generated_by, domain=None, range=Optional[Union[str, ActivityId]], mappings = [PROV.wasGeneratedBy])

slots.used = Slot(uri=NMDC.used, name="used", curie=NMDC.curie('used'),
                   model_uri=DEFAULT_.used, domain=Activity, range=Optional[str], mappings = [PROV.used])

slots.language = Slot(uri=NMDC.language, name="language", curie=NMDC.curie('language'),
                   model_uri=DEFAULT_.language, domain=None, range=Optional[str])

slots.attribute = Slot(uri=NMDC.attribute, name="attribute", curie=NMDC.curie('attribute'),
                   model_uri=DEFAULT_.attribute, domain=None, range=Optional[str])

slots.has_raw_value = Slot(uri=NMDC.has_raw_value, name="has raw value", curie=NMDC.curie('has_raw_value'),
                   model_uri=DEFAULT_.has_raw_value, domain=AttributeValue, range=Optional[str])

slots.has_unit = Slot(uri=NMDC.has_unit, name="has unit", curie=NMDC.curie('has_unit'),
                   model_uri=DEFAULT_.has_unit, domain=None, range=Optional[str], mappings = [QUD.unit, SCHEMA.unitCode])

slots.has_numeric_value = Slot(uri=NMDC.has_numeric_value, name="has numeric value", curie=NMDC.curie('has_numeric_value'),
                   model_uri=DEFAULT_.has_numeric_value, domain=None, range=Optional[float], mappings = [QUD.quantityValue, SCHEMA.value])

slots.has_minimum_numeric_value = Slot(uri=NMDC.has_minimum_numeric_value, name="has minimum numeric value", curie=NMDC.curie('has_minimum_numeric_value'),
                   model_uri=DEFAULT_.has_minimum_numeric_value, domain=None, range=Optional[float])

slots.has_maximum_numeric_value = Slot(uri=NMDC.has_maximum_numeric_value, name="has maximum numeric value", curie=NMDC.curie('has_maximum_numeric_value'),
                   model_uri=DEFAULT_.has_maximum_numeric_value, domain=None, range=Optional[float])

slots.has_boolean_value = Slot(uri=NMDC.has_boolean_value, name="has boolean value", curie=NMDC.curie('has_boolean_value'),
                   model_uri=DEFAULT_.has_boolean_value, domain=None, range=Optional[Union[bool, Bool]])

slots.latitude = Slot(uri=WGS.lat, name="latitude", curie=WGS.curie('lat'),
                   model_uri=DEFAULT_.latitude, domain=GeolocationValue, range=Optional[float], mappings = [SCHEMA.latitude])

slots.longitude = Slot(uri=WGS.long, name="longitude", curie=WGS.curie('long'),
                   model_uri=DEFAULT_.longitude, domain=GeolocationValue, range=Optional[float], mappings = [SCHEMA.longitude])

slots.term = Slot(uri=RDF.type, name="term", curie=RDF.curie('type'),
                   model_uri=DEFAULT_.term, domain=ControlledTermValue, range=Optional[Union[dict, OntologyClass]])

slots.orcid = Slot(uri=NMDC.orcid, name="orcid", curie=NMDC.curie('orcid'),
                   model_uri=DEFAULT_.orcid, domain=PersonValue, range=Optional[str])

slots.email = Slot(uri=SCHEMA.email, name="email", curie=SCHEMA.curie('email'),
                   model_uri=DEFAULT_.email, domain=None, range=Optional[str])

slots.alternate_emails = Slot(uri=NMDC.alternate_emails, name="alternate emails", curie=NMDC.curie('alternate_emails'),
                   model_uri=DEFAULT_.alternate_emails, domain=None, range=Optional[str])

slots.profile_image_url = Slot(uri=NMDC.profile_image_url, name="profile image url", curie=NMDC.curie('profile_image_url'),
                   model_uri=DEFAULT_.profile_image_url, domain=PersonValue, range=Optional[str])

slots.has_input = Slot(uri=NMDC.has_input, name="has input", curie=NMDC.curie('has_input'),
                   model_uri=DEFAULT_.has_input, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_output = Slot(uri=NMDC.has_output, name="has output", curie=NMDC.curie('has_output'),
                   model_uri=DEFAULT_.has_output, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.part_of = Slot(uri=DCTERMS.isPartOf, name="part of", curie=DCTERMS.curie('isPartOf'),
                   model_uri=DEFAULT_.part_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.execution_resource = Slot(uri=NMDC.execution_resource, name="execution resource", curie=NMDC.curie('execution_resource'),
                   model_uri=DEFAULT_.execution_resource, domain=None, range=Optional[str])

slots.url = Slot(uri=NMDC.url, name="url", curie=NMDC.curie('url'),
                   model_uri=DEFAULT_.url, domain=None, range=Optional[str])

slots.display_order = Slot(uri=NMDC.display_order, name="display order", curie=NMDC.curie('display_order'),
                   model_uri=DEFAULT_.display_order, domain=None, range=Optional[str])

slots.git_url = Slot(uri=NMDC.git_url, name="git url", curie=NMDC.curie('git_url'),
                   model_uri=DEFAULT_.git_url, domain=None, range=Optional[str])

slots.file_size_bytes = Slot(uri=NMDC.file_size_bytes, name="file size bytes", curie=NMDC.curie('file_size_bytes'),
                   model_uri=DEFAULT_.file_size_bytes, domain=None, range=Optional[int])

slots.md5_checksum = Slot(uri=NMDC.md5_checksum, name="md5 checksum", curie=NMDC.curie('md5_checksum'),
                   model_uri=DEFAULT_.md5_checksum, domain=None, range=Optional[str])

slots.abstract = Slot(uri=NMDC.abstract, name="abstract", curie=NMDC.curie('abstract'),
                   model_uri=DEFAULT_.abstract, domain=None, range=Optional[str])

slots.keywords = Slot(uri=NMDC.keywords, name="keywords", curie=NMDC.curie('keywords'),
                   model_uri=DEFAULT_.keywords, domain=None, range=Optional[Union[str, List[str]]], mappings = [DCTERMS.subject])

slots.objective = Slot(uri=NMDC.objective, name="objective", curie=NMDC.curie('objective'),
                   model_uri=DEFAULT_.objective, domain=None, range=Optional[str], mappings = [SIO["000337"]])

slots.websites = Slot(uri=NMDC.websites, name="websites", curie=NMDC.curie('websites'),
                   model_uri=DEFAULT_.websites, domain=None, range=Optional[Union[str, List[str]]])

slots.publications = Slot(uri=NMDC.publications, name="publications", curie=NMDC.curie('publications'),
                   model_uri=DEFAULT_.publications, domain=None, range=Optional[Union[str, List[str]]])

slots.metagenome_assembly_parameter = Slot(uri="str(uriorcurie)", name="metagenome assembly parameter", curie=None,
                   model_uri=DEFAULT_.metagenome_assembly_parameter, domain=None, range=Optional[str])

slots.asm_score = Slot(uri="str(uriorcurie)", name="asm_score", curie=None,
                   model_uri=DEFAULT_.asm_score, domain=None, range=Optional[float])

slots.scaffolds = Slot(uri="str(uriorcurie)", name="scaffolds", curie=None,
                   model_uri=DEFAULT_.scaffolds, domain=None, range=Optional[float])

slots.scaf_logsum = Slot(uri="str(uriorcurie)", name="scaf_logsum", curie=None,
                   model_uri=DEFAULT_.scaf_logsum, domain=None, range=Optional[float])

slots.scaf_powsum = Slot(uri="str(uriorcurie)", name="scaf_powsum", curie=None,
                   model_uri=DEFAULT_.scaf_powsum, domain=None, range=Optional[float])

slots.scaf_max = Slot(uri="str(uriorcurie)", name="scaf_max", curie=None,
                   model_uri=DEFAULT_.scaf_max, domain=None, range=Optional[float])

slots.scaf_bp = Slot(uri="str(uriorcurie)", name="scaf_bp", curie=None,
                   model_uri=DEFAULT_.scaf_bp, domain=None, range=Optional[float])

slots.scaf_N50 = Slot(uri="str(uriorcurie)", name="scaf_N50", curie=None,
                   model_uri=DEFAULT_.scaf_N50, domain=None, range=Optional[float])

slots.scaf_N90 = Slot(uri="str(uriorcurie)", name="scaf_N90", curie=None,
                   model_uri=DEFAULT_.scaf_N90, domain=None, range=Optional[float])

slots.scaf_L50 = Slot(uri="str(uriorcurie)", name="scaf_L50", curie=None,
                   model_uri=DEFAULT_.scaf_L50, domain=None, range=Optional[float])

slots.scaf_L90 = Slot(uri="str(uriorcurie)", name="scaf_L90", curie=None,
                   model_uri=DEFAULT_.scaf_L90, domain=None, range=Optional[float])

slots.scaf_n_gt50K = Slot(uri="str(uriorcurie)", name="scaf_n_gt50K", curie=None,
                   model_uri=DEFAULT_.scaf_n_gt50K, domain=None, range=Optional[float])

slots.scaf_l_gt50K = Slot(uri="str(uriorcurie)", name="scaf_l_gt50K", curie=None,
                   model_uri=DEFAULT_.scaf_l_gt50K, domain=None, range=Optional[float])

slots.scaf_pct_gt50K = Slot(uri="str(uriorcurie)", name="scaf_pct_gt50K", curie=None,
                   model_uri=DEFAULT_.scaf_pct_gt50K, domain=None, range=Optional[float])

slots.contigs = Slot(uri="str(uriorcurie)", name="contigs", curie=None,
                   model_uri=DEFAULT_.contigs, domain=None, range=Optional[float])

slots.contig_bp = Slot(uri="str(uriorcurie)", name="contig_bp", curie=None,
                   model_uri=DEFAULT_.contig_bp, domain=None, range=Optional[float])

slots.ctg_N50 = Slot(uri="str(uriorcurie)", name="ctg_N50", curie=None,
                   model_uri=DEFAULT_.ctg_N50, domain=None, range=Optional[float])

slots.ctg_L50 = Slot(uri="str(uriorcurie)", name="ctg_L50", curie=None,
                   model_uri=DEFAULT_.ctg_L50, domain=None, range=Optional[float])

slots.ctg_N90 = Slot(uri="str(uriorcurie)", name="ctg_N90", curie=None,
                   model_uri=DEFAULT_.ctg_N90, domain=None, range=Optional[float])

slots.ctg_L90 = Slot(uri="str(uriorcurie)", name="ctg_L90", curie=None,
                   model_uri=DEFAULT_.ctg_L90, domain=None, range=Optional[float])

slots.ctg_logsum = Slot(uri="str(uriorcurie)", name="ctg_logsum", curie=None,
                   model_uri=DEFAULT_.ctg_logsum, domain=None, range=Optional[float])

slots.ctg_powsum = Slot(uri="str(uriorcurie)", name="ctg_powsum", curie=None,
                   model_uri=DEFAULT_.ctg_powsum, domain=None, range=Optional[float])

slots.ctg_max = Slot(uri="str(uriorcurie)", name="ctg_max", curie=None,
                   model_uri=DEFAULT_.ctg_max, domain=None, range=Optional[float])

slots.gap_pct = Slot(uri="str(uriorcurie)", name="gap_pct", curie=None,
                   model_uri=DEFAULT_.gap_pct, domain=None, range=Optional[float])

slots.gc_std = Slot(uri="str(uriorcurie)", name="gc_std", curie=None,
                   model_uri=DEFAULT_.gc_std, domain=None, range=Optional[float])

slots.gc_avg = Slot(uri="str(uriorcurie)", name="gc_avg", curie=None,
                   model_uri=DEFAULT_.gc_avg, domain=None, range=Optional[float])

slots.num_input_reads = Slot(uri="str(uriorcurie)", name="num_input_reads", curie=None,
                   model_uri=DEFAULT_.num_input_reads, domain=None, range=Optional[float])

slots.num_aligned_reads = Slot(uri="str(uriorcurie)", name="num_aligned_reads", curie=None,
                   model_uri=DEFAULT_.num_aligned_reads, domain=None, range=Optional[float])

slots.read_QC_analysis_statistic = Slot(uri="str(uriorcurie)", name="read QC analysis statistic", curie=None,
                   model_uri=DEFAULT_.read_QC_analysis_statistic, domain=None, range=Optional[str])

slots.mags_list = Slot(uri="str(uriorcurie)", name="mags list", curie=None,
                   model_uri=DEFAULT_.mags_list, domain=None, range=Optional[Union[Union[dict, MAGBin], List[Union[dict, MAGBin]]]])

slots.too_short_contig_num = Slot(uri="str(uriorcurie)", name="too short contig num", curie=None,
                   model_uri=DEFAULT_.too_short_contig_num, domain=None, range=Optional[int])

slots.binned_contig_num = Slot(uri="str(uriorcurie)", name="binned contig num", curie=None,
                   model_uri=DEFAULT_.binned_contig_num, domain=None, range=Optional[int])

slots.input_contig_num = Slot(uri="str(uriorcurie)", name="input contig num", curie=None,
                   model_uri=DEFAULT_.input_contig_num, domain=None, range=Optional[int])

slots.unbinned_contig_num = Slot(uri="str(uriorcurie)", name="unbinned contig num", curie=None,
                   model_uri=DEFAULT_.unbinned_contig_num, domain=None, range=Optional[int])

slots.lowDepth_contig_num = Slot(uri="str(uriorcurie)", name="lowDepth contig num", curie=None,
                   model_uri=DEFAULT_.lowDepth_contig_num, domain=None, range=Optional[int])

slots.input_read_count = Slot(uri="str(uriorcurie)", name="input read count", curie=None,
                   model_uri=DEFAULT_.input_read_count, domain=None, range=Optional[float])

slots.input_base_count = Slot(uri="str(uriorcurie)", name="input base count", curie=None,
                   model_uri=DEFAULT_.input_base_count, domain=None, range=Optional[float])

slots.output_read_count = Slot(uri="str(uriorcurie)", name="output read count", curie=None,
                   model_uri=DEFAULT_.output_read_count, domain=None, range=Optional[float])

slots.output_base_count = Slot(uri="str(uriorcurie)", name="output base count", curie=None,
                   model_uri=DEFAULT_.output_base_count, domain=None, range=Optional[float])

slots.id = Slot(uri=NMDC.id, name="id", curie=NMDC.curie('id'),
                   model_uri=DEFAULT_.id, domain=None, range=URIRef)

slots.name = Slot(uri=NMDC.name, name="name", curie=NMDC.curie('name'),
                   model_uri=DEFAULT_.name, domain=None, range=Optional[str])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=DEFAULT_.description, domain=None, range=Optional[str])

slots.type = Slot(uri=NMDC.type, name="type", curie=NMDC.curie('type'),
                   model_uri=DEFAULT_.type, domain=None, range=Optional[str])

slots.title = Slot(uri=NMDC.title, name="title", curie=NMDC.curie('title'),
                   model_uri=DEFAULT_.title, domain=None, range=Optional[str])

slots.alternative_titles = Slot(uri=NMDC.alternative_titles, name="alternative titles", curie=NMDC.curie('alternative_titles'),
                   model_uri=DEFAULT_.alternative_titles, domain=None, range=Optional[Union[str, List[str]]])

slots.alternative_names = Slot(uri=NMDC.alternative_names, name="alternative names", curie=NMDC.curie('alternative_names'),
                   model_uri=DEFAULT_.alternative_names, domain=None, range=Optional[Union[str, List[str]]])

slots.alternative_descriptions = Slot(uri=NMDC.alternative_descriptions, name="alternative descriptions", curie=NMDC.curie('alternative_descriptions'),
                   model_uri=DEFAULT_.alternative_descriptions, domain=None, range=Optional[Union[str, List[str]]])

slots.alternative_identifiers = Slot(uri=NMDC.alternative_identifiers, name="alternative identifiers", curie=NMDC.curie('alternative_identifiers'),
                   model_uri=DEFAULT_.alternative_identifiers, domain=None, range=Optional[Union[str, List[str]]])

slots.external_database_identifiers = Slot(uri=NMDC.external_database_identifiers, name="external database identifiers", curie=NMDC.curie('external_database_identifiers'),
                   model_uri=DEFAULT_.external_database_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]])

slots.GOLD_identifiers = Slot(uri=NMDC.GOLD_identifiers, name="GOLD identifiers", curie=NMDC.curie('GOLD_identifiers'),
                   model_uri=DEFAULT_.GOLD_identifiers, domain=None, range=Optional[str])

slots.MGnify_identifiers = Slot(uri=NMDC.MGnify_identifiers, name="MGnify identifiers", curie=NMDC.curie('MGnify_identifiers'),
                   model_uri=DEFAULT_.MGnify_identifiers, domain=None, range=Optional[str])

slots.INSDC_identifiers = Slot(uri=NMDC.INSDC_identifiers, name="INSDC identifiers", curie=NMDC.curie('INSDC_identifiers'),
                   model_uri=DEFAULT_.INSDC_identifiers, domain=None, range=Optional[str])

slots.study_identifiers = Slot(uri=NMDC.study_identifiers, name="study identifiers", curie=NMDC.curie('study_identifiers'),
                   model_uri=DEFAULT_.study_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]])

slots.INSDC_SRA_ENA_study_identifiers = Slot(uri=NMDC.INSDC_SRA_ENA_study_identifiers, name="INSDC SRA ENA study identifiers", curie=NMDC.curie('INSDC_SRA_ENA_study_identifiers'),
                   model_uri=DEFAULT_.INSDC_SRA_ENA_study_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^insdc.sra:(E|D|S)RP[0-9]{6,}$'))

slots.INSDC_bioproject_identifiers = Slot(uri=NMDC.INSDC_bioproject_identifiers, name="INSDC bioproject identifiers", curie=NMDC.curie('INSDC_bioproject_identifiers'),
                   model_uri=DEFAULT_.INSDC_bioproject_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^bioproject:PRJ[DEN][A-Z][0-9]+$'))

slots.GOLD_study_identifiers = Slot(uri=NMDC.GOLD_study_identifiers, name="GOLD study identifiers", curie=NMDC.curie('GOLD_study_identifiers'),
                   model_uri=DEFAULT_.GOLD_study_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^GOLD:Gs[0-9]+$'))

slots.MGnify_project_identifiers = Slot(uri=NMDC.MGnify_project_identifiers, name="MGnify project identifiers", curie=NMDC.curie('MGnify_project_identifiers'),
                   model_uri=DEFAULT_.MGnify_project_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^mgnify.proj:[A-Z]+[0-9]+$'))

slots.sample_identifiers = Slot(uri=NMDC.sample_identifiers, name="sample identifiers", curie=NMDC.curie('sample_identifiers'),
                   model_uri=DEFAULT_.sample_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]])

slots.GOLD_sample_identifiers = Slot(uri=NMDC.GOLD_sample_identifiers, name="GOLD sample identifiers", curie=NMDC.curie('GOLD_sample_identifiers'),
                   model_uri=DEFAULT_.GOLD_sample_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^GOLD:Gb[0-9]+$'))

slots.INSDC_biosample_identifiers = Slot(uri=NMDC.INSDC_biosample_identifiers, name="INSDC biosample identifiers", curie=NMDC.curie('INSDC_biosample_identifiers'),
                   model_uri=DEFAULT_.INSDC_biosample_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^biosample:SAM[NED]([A-Z])?[0-9]+$'))

slots.INSDC_secondary_sample_identifiers = Slot(uri=NMDC.INSDC_secondary_sample_identifiers, name="INSDC secondary sample identifiers", curie=NMDC.curie('INSDC_secondary_sample_identifiers'),
                   model_uri=DEFAULT_.INSDC_secondary_sample_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^biosample:(E|D|S)RS[0-9]{6,}$'))

slots.omics_processing_identifiers = Slot(uri=NMDC.omics_processing_identifiers, name="omics processing identifiers", curie=NMDC.curie('omics_processing_identifiers'),
                   model_uri=DEFAULT_.omics_processing_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]])

slots.GOLD_sequencing_project_identifiers = Slot(uri=NMDC.GOLD_sequencing_project_identifiers, name="GOLD sequencing project identifiers", curie=NMDC.curie('GOLD_sequencing_project_identifiers'),
                   model_uri=DEFAULT_.GOLD_sequencing_project_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^GOLD:Gp[0-9]+$'))

slots.INSDC_experiment_identifiers = Slot(uri=NMDC.INSDC_experiment_identifiers, name="INSDC experiment identifiers", curie=NMDC.curie('INSDC_experiment_identifiers'),
                   model_uri=DEFAULT_.INSDC_experiment_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^insdc.sra:(E|D|S)RX[0-9]{6,}$'))

slots.analysis_identifiers = Slot(uri=NMDC.analysis_identifiers, name="analysis identifiers", curie=NMDC.curie('analysis_identifiers'),
                   model_uri=DEFAULT_.analysis_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]])

slots.GOLD_analysis_project_identifiers = Slot(uri=NMDC.GOLD_analysis_project_identifiers, name="GOLD analysis project identifiers", curie=NMDC.curie('GOLD_analysis_project_identifiers'),
                   model_uri=DEFAULT_.GOLD_analysis_project_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^GOLD:Ga[0-9]+$'))

slots.INSDC_analysis_identifiers = Slot(uri=NMDC.INSDC_analysis_identifiers, name="INSDC analysis identifiers", curie=NMDC.curie('INSDC_analysis_identifiers'),
                   model_uri=DEFAULT_.INSDC_analysis_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]],
                   pattern=re.compile(r'^insdc.sra:(E|D|S)RR[0-9]{6,}$'))

slots.MGnify_analysis_identifiers = Slot(uri=NMDC.MGnify_analysis_identifiers, name="MGnify analysis identifiers", curie=NMDC.curie('MGnify_analysis_identifiers'),
                   model_uri=DEFAULT_.MGnify_analysis_identifiers, domain=None, range=Optional[Union[Union[str, ExternalIdentifier], List[Union[str, ExternalIdentifier]]]])

slots.assembly_identifiers = Slot(uri=NMDC.assembly_identifiers, name="assembly identifiers", curie=NMDC.curie('assembly_identifiers'),
                   model_uri=DEFAULT_.assembly_identifiers, domain=None, range=Optional[str])

slots.INSDC_assembly_identifiers = Slot(uri=NMDC.INSDC_assembly_identifiers, name="INSDC assembly identifiers", curie=NMDC.curie('INSDC_assembly_identifiers'),
                   model_uri=DEFAULT_.INSDC_assembly_identifiers, domain=None, range=Optional[str],
                   pattern=re.compile(r'^insdc.sra:[A-Z]+[0-9]+(\.[0-9]+)?$'))

slots.mAGBin__bin_name = Slot(uri=DEFAULT_.bin_name, name="mAGBin__bin_name", curie=DEFAULT_.curie('bin_name'),
                   model_uri=DEFAULT_.mAGBin__bin_name, domain=None, range=Optional[str])

slots.mAGBin__number_of_contig = Slot(uri=DEFAULT_.number_of_contig, name="mAGBin__number_of_contig", curie=DEFAULT_.curie('number_of_contig'),
                   model_uri=DEFAULT_.mAGBin__number_of_contig, domain=None, range=Optional[int])

slots.mAGBin__completeness = Slot(uri=DEFAULT_.completeness, name="mAGBin__completeness", curie=DEFAULT_.curie('completeness'),
                   model_uri=DEFAULT_.mAGBin__completeness, domain=None, range=Optional[float])

slots.mAGBin__contamination = Slot(uri=DEFAULT_.contamination, name="mAGBin__contamination", curie=DEFAULT_.curie('contamination'),
                   model_uri=DEFAULT_.mAGBin__contamination, domain=None, range=Optional[float])

slots.mAGBin__gene_count = Slot(uri=DEFAULT_.gene_count, name="mAGBin__gene_count", curie=DEFAULT_.curie('gene_count'),
                   model_uri=DEFAULT_.mAGBin__gene_count, domain=None, range=Optional[int])

slots.mAGBin__bin_quality = Slot(uri=DEFAULT_.bin_quality, name="mAGBin__bin_quality", curie=DEFAULT_.curie('bin_quality'),
                   model_uri=DEFAULT_.mAGBin__bin_quality, domain=None, range=Optional[str])

slots.mAGBin__num_16s = Slot(uri=DEFAULT_.num_16s, name="mAGBin__num_16s", curie=DEFAULT_.curie('num_16s'),
                   model_uri=DEFAULT_.mAGBin__num_16s, domain=None, range=Optional[int])

slots.mAGBin__num_5s = Slot(uri=DEFAULT_.num_5s, name="mAGBin__num_5s", curie=DEFAULT_.curie('num_5s'),
                   model_uri=DEFAULT_.mAGBin__num_5s, domain=None, range=Optional[int])

slots.mAGBin__num_23s = Slot(uri=DEFAULT_.num_23s, name="mAGBin__num_23s", curie=DEFAULT_.curie('num_23s'),
                   model_uri=DEFAULT_.mAGBin__num_23s, domain=None, range=Optional[int])

slots.mAGBin__num_tRNA = Slot(uri=DEFAULT_.num_tRNA, name="mAGBin__num_tRNA", curie=DEFAULT_.curie('num_tRNA'),
                   model_uri=DEFAULT_.mAGBin__num_tRNA, domain=None, range=Optional[int])

slots.mAGBin__gtdbtk_domain = Slot(uri=DEFAULT_.gtdbtk_domain, name="mAGBin__gtdbtk_domain", curie=DEFAULT_.curie('gtdbtk_domain'),
                   model_uri=DEFAULT_.mAGBin__gtdbtk_domain, domain=None, range=Optional[str])

slots.mAGBin__gtdbtk_phylum = Slot(uri=DEFAULT_.gtdbtk_phylum, name="mAGBin__gtdbtk_phylum", curie=DEFAULT_.curie('gtdbtk_phylum'),
                   model_uri=DEFAULT_.mAGBin__gtdbtk_phylum, domain=None, range=Optional[str])

slots.mAGBin__gtdbtk_class = Slot(uri=DEFAULT_.gtdbtk_class, name="mAGBin__gtdbtk_class", curie=DEFAULT_.curie('gtdbtk_class'),
                   model_uri=DEFAULT_.mAGBin__gtdbtk_class, domain=None, range=Optional[str])

slots.mAGBin__gtdbtk_order = Slot(uri=DEFAULT_.gtdbtk_order, name="mAGBin__gtdbtk_order", curie=DEFAULT_.curie('gtdbtk_order'),
                   model_uri=DEFAULT_.mAGBin__gtdbtk_order, domain=None, range=Optional[str])

slots.mAGBin__gtdbtk_family = Slot(uri=DEFAULT_.gtdbtk_family, name="mAGBin__gtdbtk_family", curie=DEFAULT_.curie('gtdbtk_family'),
                   model_uri=DEFAULT_.mAGBin__gtdbtk_family, domain=None, range=Optional[str])

slots.mAGBin__gtdbtk_genus = Slot(uri=DEFAULT_.gtdbtk_genus, name="mAGBin__gtdbtk_genus", curie=DEFAULT_.curie('gtdbtk_genus'),
                   model_uri=DEFAULT_.mAGBin__gtdbtk_genus, domain=None, range=Optional[str])

slots.mAGBin__gtdbtk_species = Slot(uri=DEFAULT_.gtdbtk_species, name="mAGBin__gtdbtk_species", curie=DEFAULT_.curie('gtdbtk_species'),
                   model_uri=DEFAULT_.mAGBin__gtdbtk_species, domain=None, range=Optional[str])

slots.seqid = Slot(uri=DEFAULT_.seqid, name="seqid", curie=DEFAULT_.curie('seqid'),
                   model_uri=DEFAULT_.seqid, domain=None, range=str)

slots.start = Slot(uri=DEFAULT_.start, name="start", curie=DEFAULT_.curie('start'),
                   model_uri=DEFAULT_.start, domain=None, range=int)

slots.end = Slot(uri=DEFAULT_.end, name="end", curie=DEFAULT_.curie('end'),
                   model_uri=DEFAULT_.end, domain=None, range=int)

slots.strand = Slot(uri=DEFAULT_.strand, name="strand", curie=DEFAULT_.curie('strand'),
                   model_uri=DEFAULT_.strand, domain=None, range=Optional[str])

slots.phase = Slot(uri=DEFAULT_.phase, name="phase", curie=DEFAULT_.curie('phase'),
                   model_uri=DEFAULT_.phase, domain=None, range=Optional[int])

slots.encodes = Slot(uri=DEFAULT_.encodes, name="encodes", curie=DEFAULT_.curie('encodes'),
                   model_uri=DEFAULT_.encodes, domain=None, range=Optional[Union[str, GeneProductId]])

slots.feature_type = Slot(uri=DEFAULT_.feature_type, name="feature type", curie=DEFAULT_.curie('feature_type'),
                   model_uri=DEFAULT_.feature_type, domain=None, range=Optional[str])

slots.has_part = Slot(uri=DEFAULT_.has_part, name="has_part", curie=DEFAULT_.curie('has_part'),
                   model_uri=DEFAULT_.has_part, domain=None, range=Optional[Union[Union[str, ReactionId], List[Union[str, ReactionId]]]])

slots.left_participants = Slot(uri=DEFAULT_.left_participants, name="left participants", curie=DEFAULT_.curie('left_participants'),
                   model_uri=DEFAULT_.left_participants, domain=None, range=Optional[Union[Union[dict, ReactionParticipant], List[Union[dict, ReactionParticipant]]]])

slots.right_participants = Slot(uri=DEFAULT_.right_participants, name="right participants", curie=DEFAULT_.curie('right_participants'),
                   model_uri=DEFAULT_.right_participants, domain=None, range=Optional[Union[Union[dict, ReactionParticipant], List[Union[dict, ReactionParticipant]]]])

slots.direction = Slot(uri=DEFAULT_.direction, name="direction", curie=DEFAULT_.curie('direction'),
                   model_uri=DEFAULT_.direction, domain=None, range=Optional[str])

slots.smarts_string = Slot(uri=DEFAULT_.smarts_string, name="smarts string", curie=DEFAULT_.curie('smarts_string'),
                   model_uri=DEFAULT_.smarts_string, domain=None, range=Optional[str])

slots.is_diastereoselective = Slot(uri=DEFAULT_.is_diastereoselective, name="is diastereoselective", curie=DEFAULT_.curie('is_diastereoselective'),
                   model_uri=DEFAULT_.is_diastereoselective, domain=None, range=Optional[Union[bool, Bool]])

slots.is_stereo = Slot(uri=DEFAULT_.is_stereo, name="is stereo", curie=DEFAULT_.curie('is_stereo'),
                   model_uri=DEFAULT_.is_stereo, domain=None, range=Optional[Union[bool, Bool]])

slots.is_balanced = Slot(uri=DEFAULT_.is_balanced, name="is balanced", curie=DEFAULT_.curie('is_balanced'),
                   model_uri=DEFAULT_.is_balanced, domain=None, range=Optional[Union[bool, Bool]])

slots.is_transport = Slot(uri=DEFAULT_.is_transport, name="is transport", curie=DEFAULT_.curie('is_transport'),
                   model_uri=DEFAULT_.is_transport, domain=None, range=Optional[Union[bool, Bool]])

slots.is_fully_characterized = Slot(uri=DEFAULT_.is_fully_characterized, name="is fully characterized", curie=DEFAULT_.curie('is_fully_characterized'),
                   model_uri=DEFAULT_.is_fully_characterized, domain=None, range=Optional[Union[bool, Bool]])

slots.chemical = Slot(uri=DEFAULT_.chemical, name="chemical", curie=DEFAULT_.curie('chemical'),
                   model_uri=DEFAULT_.chemical, domain=None, range=Optional[Union[str, ChemicalEntityId]])

slots.stoichiometry = Slot(uri=DEFAULT_.stoichiometry, name="stoichiometry", curie=DEFAULT_.curie('stoichiometry'),
                   model_uri=DEFAULT_.stoichiometry, domain=None, range=Optional[int])

slots.metabolite_quantified = Slot(uri=DEFAULT_.metabolite_quantified, name="metabolite quantified", curie=DEFAULT_.curie('metabolite_quantified'),
                   model_uri=DEFAULT_.metabolite_quantified, domain=None, range=Optional[Union[str, ChemicalEntityId]])

slots.highest_similarity_score = Slot(uri=DEFAULT_.highest_similarity_score, name="highest similarity score", curie=DEFAULT_.curie('highest_similarity_score'),
                   model_uri=DEFAULT_.highest_similarity_score, domain=None, range=Optional[float])

slots.peptide_sequence = Slot(uri=DEFAULT_.peptide_sequence, name="peptide sequence", curie=DEFAULT_.curie('peptide_sequence'),
                   model_uri=DEFAULT_.peptide_sequence, domain=None, range=Optional[str])

slots.best_protein = Slot(uri=DEFAULT_.best_protein, name="best protein", curie=DEFAULT_.curie('best_protein'),
                   model_uri=DEFAULT_.best_protein, domain=None, range=Optional[Union[str, GeneProductId]])

slots.all_proteins = Slot(uri=DEFAULT_.all_proteins, name="all proteins", curie=DEFAULT_.curie('all_proteins'),
                   model_uri=DEFAULT_.all_proteins, domain=None, range=Optional[Union[Union[str, GeneProductId], List[Union[str, GeneProductId]]]])

slots.min_q_value = Slot(uri=DEFAULT_.min_q_value, name="min_q_value", curie=DEFAULT_.curie('min_q_value'),
                   model_uri=DEFAULT_.min_q_value, domain=None, range=Optional[float])

slots.peptide_spectral_count = Slot(uri=DEFAULT_.peptide_spectral_count, name="peptide_spectral_count", curie=DEFAULT_.curie('peptide_spectral_count'),
                   model_uri=DEFAULT_.peptide_spectral_count, domain=None, range=Optional[int])

slots.peptide_sum_masic_abundance = Slot(uri=DEFAULT_.peptide_sum_masic_abundance, name="peptide_sum_masic_abundance", curie=DEFAULT_.curie('peptide_sum_masic_abundance'),
                   model_uri=DEFAULT_.peptide_sum_masic_abundance, domain=None, range=Optional[int])

slots.peptide_sequence_count = Slot(uri=DEFAULT_.peptide_sequence_count, name="peptide_sequence_count", curie=DEFAULT_.curie('peptide_sequence_count'),
                   model_uri=DEFAULT_.peptide_sequence_count, domain=None, range=Optional[int])

slots.protein_spectral_count = Slot(uri=DEFAULT_.protein_spectral_count, name="protein_spectral_count", curie=DEFAULT_.curie('protein_spectral_count'),
                   model_uri=DEFAULT_.protein_spectral_count, domain=None, range=Optional[int])

slots.protein_sum_masic_abundance = Slot(uri=DEFAULT_.protein_sum_masic_abundance, name="protein_sum_masic_abundance", curie=DEFAULT_.curie('protein_sum_masic_abundance'),
                   model_uri=DEFAULT_.protein_sum_masic_abundance, domain=None, range=Optional[int])

slots.inchi = Slot(uri=DEFAULT_.inchi, name="inchi", curie=DEFAULT_.curie('inchi'),
                   model_uri=DEFAULT_.inchi, domain=None, range=Optional[str])

slots.inchi_key = Slot(uri=DEFAULT_.inchi_key, name="inchi key", curie=DEFAULT_.curie('inchi_key'),
                   model_uri=DEFAULT_.inchi_key, domain=None, range=Optional[str])

slots.smiles = Slot(uri=DEFAULT_.smiles, name="smiles", curie=DEFAULT_.curie('smiles'),
                   model_uri=DEFAULT_.smiles, domain=None, range=Optional[Union[str, List[str]]])

slots.chemical_formula = Slot(uri=DEFAULT_.chemical_formula, name="chemical formula", curie=DEFAULT_.curie('chemical_formula'),
                   model_uri=DEFAULT_.chemical_formula, domain=None, range=Optional[str])

slots.input_read_bases = Slot(uri=DEFAULT_.input_read_bases, name="input_read_bases", curie=DEFAULT_.curie('input_read_bases'),
                   model_uri=DEFAULT_.input_read_bases, domain=None, range=Optional[float])

slots.output_read_bases = Slot(uri=DEFAULT_.output_read_bases, name="output_read_bases", curie=DEFAULT_.curie('output_read_bases'),
                   model_uri=DEFAULT_.output_read_bases, domain=None, range=Optional[float])

slots.has_metabolite_quantifications = Slot(uri=DEFAULT_.has_metabolite_quantifications, name="has metabolite quantifications", curie=DEFAULT_.curie('has_metabolite_quantifications'),
                   model_uri=DEFAULT_.has_metabolite_quantifications, domain=None, range=Optional[Union[Union[dict, MetaboliteQuantification], List[Union[dict, MetaboliteQuantification]]]])

slots.has_calibration = Slot(uri=DEFAULT_.has_calibration, name="has calibration", curie=DEFAULT_.curie('has_calibration'),
                   model_uri=DEFAULT_.has_calibration, domain=None, range=Optional[str])

slots.has_peptide_quantifications = Slot(uri=DEFAULT_.has_peptide_quantifications, name="has peptide quantifications", curie=DEFAULT_.curie('has_peptide_quantifications'),
                   model_uri=DEFAULT_.has_peptide_quantifications, domain=None, range=Optional[Union[Union[dict, PeptideQuantification], List[Union[dict, PeptideQuantification]]]])

slots.genome_feature_seqid = Slot(uri=DEFAULT_.seqid, name="genome feature_seqid", curie=DEFAULT_.curie('seqid'),
                   model_uri=DEFAULT_.genome_feature_seqid, domain=GenomeFeature, range=str)

slots.genome_feature_type = Slot(uri=RDF.type, name="genome feature_type", curie=RDF.curie('type'),
                   model_uri=DEFAULT_.genome_feature_type, domain=GenomeFeature, range=Optional[Union[str, OntologyClassId]])

slots.genome_feature_start = Slot(uri=DEFAULT_.start, name="genome feature_start", curie=DEFAULT_.curie('start'),
                   model_uri=DEFAULT_.genome_feature_start, domain=GenomeFeature, range=int)

slots.genome_feature_end = Slot(uri=DEFAULT_.end, name="genome feature_end", curie=DEFAULT_.curie('end'),
                   model_uri=DEFAULT_.genome_feature_end, domain=GenomeFeature, range=int)

slots.genome_feature_strand = Slot(uri=DEFAULT_.strand, name="genome feature_strand", curie=DEFAULT_.curie('strand'),
                   model_uri=DEFAULT_.genome_feature_strand, domain=GenomeFeature, range=Optional[str])

slots.genome_feature_phase = Slot(uri=DEFAULT_.phase, name="genome feature_phase", curie=DEFAULT_.curie('phase'),
                   model_uri=DEFAULT_.genome_feature_phase, domain=GenomeFeature, range=Optional[int])

slots.genome_feature_encodes = Slot(uri=DEFAULT_.encodes, name="genome feature_encodes", curie=DEFAULT_.curie('encodes'),
                   model_uri=DEFAULT_.genome_feature_encodes, domain=GenomeFeature, range=Optional[Union[str, GeneProductId]])

slots.genome_feature_feature_type = Slot(uri=DEFAULT_.feature_type, name="genome feature_feature type", curie=DEFAULT_.curie('feature_type'),
                   model_uri=DEFAULT_.genome_feature_feature_type, domain=GenomeFeature, range=Optional[str])

slots.pathway_has_part = Slot(uri=DEFAULT_.has_part, name="pathway_has_part", curie=DEFAULT_.curie('has_part'),
                   model_uri=DEFAULT_.pathway_has_part, domain=Pathway, range=Optional[Union[Union[str, ReactionId], List[Union[str, ReactionId]]]])

slots.reaction_left_participants = Slot(uri=DEFAULT_.left_participants, name="reaction_left participants", curie=DEFAULT_.curie('left_participants'),
                   model_uri=DEFAULT_.reaction_left_participants, domain=Reaction, range=Optional[Union[Union[dict, "ReactionParticipant"], List[Union[dict, "ReactionParticipant"]]]])

slots.reaction_right_participants = Slot(uri=DEFAULT_.right_participants, name="reaction_right participants", curie=DEFAULT_.curie('right_participants'),
                   model_uri=DEFAULT_.reaction_right_participants, domain=Reaction, range=Optional[Union[Union[dict, "ReactionParticipant"], List[Union[dict, "ReactionParticipant"]]]])

slots.reaction_direction = Slot(uri=DEFAULT_.direction, name="reaction_direction", curie=DEFAULT_.curie('direction'),
                   model_uri=DEFAULT_.reaction_direction, domain=Reaction, range=Optional[str])

slots.reaction_smarts_string = Slot(uri=DEFAULT_.smarts_string, name="reaction_smarts string", curie=DEFAULT_.curie('smarts_string'),
                   model_uri=DEFAULT_.reaction_smarts_string, domain=Reaction, range=Optional[str])

slots.reaction_is_diastereoselective = Slot(uri=DEFAULT_.is_diastereoselective, name="reaction_is diastereoselective", curie=DEFAULT_.curie('is_diastereoselective'),
                   model_uri=DEFAULT_.reaction_is_diastereoselective, domain=Reaction, range=Optional[Union[bool, Bool]])

slots.reaction_is_stereo = Slot(uri=DEFAULT_.is_stereo, name="reaction_is stereo", curie=DEFAULT_.curie('is_stereo'),
                   model_uri=DEFAULT_.reaction_is_stereo, domain=Reaction, range=Optional[Union[bool, Bool]])

slots.reaction_is_balanced = Slot(uri=DEFAULT_.is_balanced, name="reaction_is balanced", curie=DEFAULT_.curie('is_balanced'),
                   model_uri=DEFAULT_.reaction_is_balanced, domain=Reaction, range=Optional[Union[bool, Bool]])

slots.reaction_is_transport = Slot(uri=DEFAULT_.is_transport, name="reaction_is transport", curie=DEFAULT_.curie('is_transport'),
                   model_uri=DEFAULT_.reaction_is_transport, domain=Reaction, range=Optional[Union[bool, Bool]])

slots.reaction_is_fully_characterized = Slot(uri=DEFAULT_.is_fully_characterized, name="reaction_is fully characterized", curie=DEFAULT_.curie('is_fully_characterized'),
                   model_uri=DEFAULT_.reaction_is_fully_characterized, domain=Reaction, range=Optional[Union[bool, Bool]])

slots.reaction_participant_chemical = Slot(uri=DEFAULT_.chemical, name="reaction participant_chemical", curie=DEFAULT_.curie('chemical'),
                   model_uri=DEFAULT_.reaction_participant_chemical, domain=ReactionParticipant, range=Optional[Union[str, ChemicalEntityId]])

slots.reaction_participant_stoichiometry = Slot(uri=DEFAULT_.stoichiometry, name="reaction participant_stoichiometry", curie=DEFAULT_.curie('stoichiometry'),
                   model_uri=DEFAULT_.reaction_participant_stoichiometry, domain=ReactionParticipant, range=Optional[int])

slots.functional_annotation_has_function = Slot(uri=DEFAULT_.has_function, name="functional annotation_has function", curie=DEFAULT_.curie('has_function'),
                   model_uri=DEFAULT_.functional_annotation_has_function, domain=FunctionalAnnotation, range=Optional[str],
                   pattern=re.compile(r'^(KEGG.PATHWAY:\w{2,4}\d{5}|KEGG.REACTION:R\d+|RHEA:\d{5}|MetaCyc:[A-Za-z0-9+_.%-:]+|EC:\d{1,2}(\.\d{0,3}){0,3}|GO:\d{7}|MetaNetX:(MNXR\d+|EMPTY)|SEED:\w+|KEGG\.ORTHOLOGY:K\d+|EGGNOG:\w+|PFAM:PF\d{5}|TIGRFAM:TIGR\d+|SUPFAM:\w+|CATH:[1-6]\.[0-9]+\.[0-9]+\.[0-9]+|PANTHER.FAMILY:PTHR\d{5}(\:SF\d{1,3})?)$'))

slots.functional_annotation_type = Slot(uri=NMDC.type, name="functional annotation_type", curie=NMDC.curie('type'),
                   model_uri=DEFAULT_.functional_annotation_type, domain=FunctionalAnnotation, range=Optional[Union[str, OntologyClassId]])

slots.functional_annotation_was_generated_by = Slot(uri=NMDC.was_generated_by, name="functional annotation_was generated by", curie=NMDC.curie('was_generated_by'),
                   model_uri=DEFAULT_.functional_annotation_was_generated_by, domain=FunctionalAnnotation, range=Optional[Union[str, MetagenomeAnnotationActivityId]], mappings = [PROV.wasGeneratedBy])

slots.attribute_value_type = Slot(uri=NMDC.type, name="attribute value_type", curie=NMDC.curie('type'),
                   model_uri=DEFAULT_.attribute_value_type, domain=AttributeValue, range=Optional[str])

slots.quantity_value_has_raw_value = Slot(uri=NMDC.has_raw_value, name="quantity value_has raw value", curie=NMDC.curie('has_raw_value'),
                   model_uri=DEFAULT_.quantity_value_has_raw_value, domain=QuantityValue, range=Optional[str])

slots.quantity_value_has_unit = Slot(uri=NMDC.has_unit, name="quantity value_has unit", curie=NMDC.curie('has_unit'),
                   model_uri=DEFAULT_.quantity_value_has_unit, domain=QuantityValue, range=Optional[str], mappings = [QUD.unit, SCHEMA.unitCode])

slots.quantity_value_has_numeric_value = Slot(uri=NMDC.has_numeric_value, name="quantity value_has numeric value", curie=NMDC.curie('has_numeric_value'),
                   model_uri=DEFAULT_.quantity_value_has_numeric_value, domain=QuantityValue, range=Optional[float], mappings = [QUD.quantityValue, SCHEMA.value])

slots.person_value_orcid = Slot(uri=NMDC.orcid, name="person value_orcid", curie=NMDC.curie('orcid'),
                   model_uri=DEFAULT_.person_value_orcid, domain=PersonValue, range=Optional[str])

slots.person_value_email = Slot(uri=SCHEMA.email, name="person value_email", curie=SCHEMA.curie('email'),
                   model_uri=DEFAULT_.person_value_email, domain=PersonValue, range=Optional[str])

slots.person_value_has_raw_value = Slot(uri=NMDC.has_raw_value, name="person value_has raw value", curie=NMDC.curie('has_raw_value'),
                   model_uri=DEFAULT_.person_value_has_raw_value, domain=PersonValue, range=Optional[str])

slots.person_value_name = Slot(uri=NMDC.name, name="person value_name", curie=NMDC.curie('name'),
                   model_uri=DEFAULT_.person_value_name, domain=PersonValue, range=Optional[str])

slots.person_id = Slot(uri=NMDC.id, name="person_id", curie=NMDC.curie('id'),
                   model_uri=DEFAULT_.person_id, domain=Person, range=Union[str, PersonId])

slots.metabolite_quantification_metabolite_quantified = Slot(uri=DEFAULT_.metabolite_quantified, name="metabolite quantification_metabolite quantified", curie=DEFAULT_.curie('metabolite_quantified'),
                   model_uri=DEFAULT_.metabolite_quantification_metabolite_quantified, domain=MetaboliteQuantification, range=Optional[Union[str, ChemicalEntityId]])

slots.metabolite_quantification_highest_similarity_score = Slot(uri=DEFAULT_.highest_similarity_score, name="metabolite quantification_highest similarity score", curie=DEFAULT_.curie('highest_similarity_score'),
                   model_uri=DEFAULT_.metabolite_quantification_highest_similarity_score, domain=MetaboliteQuantification, range=Optional[float])

slots.peptide_quantification_peptide_sequence = Slot(uri=DEFAULT_.peptide_sequence, name="peptide quantification_peptide sequence", curie=DEFAULT_.curie('peptide_sequence'),
                   model_uri=DEFAULT_.peptide_quantification_peptide_sequence, domain=PeptideQuantification, range=Optional[str])

slots.peptide_quantification_best_protein = Slot(uri=DEFAULT_.best_protein, name="peptide quantification_best protein", curie=DEFAULT_.curie('best_protein'),
                   model_uri=DEFAULT_.peptide_quantification_best_protein, domain=PeptideQuantification, range=Optional[Union[str, GeneProductId]])

slots.peptide_quantification_all_proteins = Slot(uri=DEFAULT_.all_proteins, name="peptide quantification_all proteins", curie=DEFAULT_.curie('all_proteins'),
                   model_uri=DEFAULT_.peptide_quantification_all_proteins, domain=PeptideQuantification, range=Optional[Union[Union[str, GeneProductId], List[Union[str, GeneProductId]]]])

slots.peptide_quantification_min_q_value = Slot(uri=DEFAULT_.min_q_value, name="peptide quantification_min_q_value", curie=DEFAULT_.curie('min_q_value'),
                   model_uri=DEFAULT_.peptide_quantification_min_q_value, domain=PeptideQuantification, range=Optional[float])

slots.peptide_quantification_peptide_spectral_count = Slot(uri=DEFAULT_.peptide_spectral_count, name="peptide quantification_peptide_spectral_count", curie=DEFAULT_.curie('peptide_spectral_count'),
                   model_uri=DEFAULT_.peptide_quantification_peptide_spectral_count, domain=PeptideQuantification, range=Optional[int])

slots.peptide_quantification_peptide_sum_masic_abundance = Slot(uri=DEFAULT_.peptide_sum_masic_abundance, name="peptide quantification_peptide_sum_masic_abundance", curie=DEFAULT_.curie('peptide_sum_masic_abundance'),
                   model_uri=DEFAULT_.peptide_quantification_peptide_sum_masic_abundance, domain=PeptideQuantification, range=Optional[int])

slots.protein_quantification_best_protein = Slot(uri=DEFAULT_.best_protein, name="protein quantification_best protein", curie=DEFAULT_.curie('best_protein'),
                   model_uri=DEFAULT_.protein_quantification_best_protein, domain=ProteinQuantification, range=Optional[Union[str, GeneProductId]])

slots.protein_quantification_all_proteins = Slot(uri=DEFAULT_.all_proteins, name="protein quantification_all proteins", curie=DEFAULT_.curie('all_proteins'),
                   model_uri=DEFAULT_.protein_quantification_all_proteins, domain=ProteinQuantification, range=Optional[Union[Union[str, GeneProductId], List[Union[str, GeneProductId]]]])

slots.protein_quantification_peptide_sequence_count = Slot(uri=DEFAULT_.peptide_sequence_count, name="protein quantification_peptide_sequence_count", curie=DEFAULT_.curie('peptide_sequence_count'),
                   model_uri=DEFAULT_.protein_quantification_peptide_sequence_count, domain=ProteinQuantification, range=Optional[int])

slots.protein_quantification_protein_spectral_count = Slot(uri=DEFAULT_.protein_spectral_count, name="protein quantification_protein_spectral_count", curie=DEFAULT_.curie('protein_spectral_count'),
                   model_uri=DEFAULT_.protein_quantification_protein_spectral_count, domain=ProteinQuantification, range=Optional[int])

slots.protein_quantification_protein_sum_masic_abundance = Slot(uri=DEFAULT_.protein_sum_masic_abundance, name="protein quantification_protein_sum_masic_abundance", curie=DEFAULT_.curie('protein_sum_masic_abundance'),
                   model_uri=DEFAULT_.protein_quantification_protein_sum_masic_abundance, domain=ProteinQuantification, range=Optional[int])

slots.chemical_entity_inchi = Slot(uri=DEFAULT_.inchi, name="chemical entity_inchi", curie=DEFAULT_.curie('inchi'),
                   model_uri=DEFAULT_.chemical_entity_inchi, domain=ChemicalEntity, range=Optional[str])

slots.chemical_entity_inchi_key = Slot(uri=DEFAULT_.inchi_key, name="chemical entity_inchi key", curie=DEFAULT_.curie('inchi_key'),
                   model_uri=DEFAULT_.chemical_entity_inchi_key, domain=ChemicalEntity, range=Optional[str])

slots.chemical_entity_smiles = Slot(uri=DEFAULT_.smiles, name="chemical entity_smiles", curie=DEFAULT_.curie('smiles'),
                   model_uri=DEFAULT_.chemical_entity_smiles, domain=ChemicalEntity, range=Optional[Union[str, List[str]]])

slots.chemical_entity_chemical_formula = Slot(uri=DEFAULT_.chemical_formula, name="chemical entity_chemical formula", curie=DEFAULT_.curie('chemical_formula'),
                   model_uri=DEFAULT_.chemical_entity_chemical_formula, domain=ChemicalEntity, range=Optional[str])

slots.geolocation_value_has_raw_value = Slot(uri=NMDC.has_raw_value, name="geolocation value_has raw value", curie=NMDC.curie('has_raw_value'),
                   model_uri=DEFAULT_.geolocation_value_has_raw_value, domain=GeolocationValue, range=Optional[str])

slots.workflow_execution_activity_was_associated_with = Slot(uri=NMDC.was_associated_with, name="workflow execution activity_was associated with", curie=NMDC.curie('was_associated_with'),
                   model_uri=DEFAULT_.workflow_execution_activity_was_associated_with, domain=WorkflowExecutionActivity, range=Optional[Union[str, WorkflowExecutionActivityId]], mappings = [PROV.wasAssociatedWith])

slots.workflow_execution_activity_started_at_time = Slot(uri=NMDC.started_at_time, name="workflow execution activity_started at time", curie=NMDC.curie('started_at_time'),
                   model_uri=DEFAULT_.workflow_execution_activity_started_at_time, domain=WorkflowExecutionActivity, range=Union[str, XSDDateTime], mappings = [PROV.startedAtTime],
                   pattern=re.compile(r'^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$'))

slots.workflow_execution_activity_ended_at_time = Slot(uri=NMDC.ended_at_time, name="workflow execution activity_ended at time", curie=NMDC.curie('ended_at_time'),
                   model_uri=DEFAULT_.workflow_execution_activity_ended_at_time, domain=WorkflowExecutionActivity, range=Union[str, XSDDateTime], mappings = [PROV.endedAtTime],
                   pattern=re.compile(r'^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$'))

slots.workflow_execution_activity_git_url = Slot(uri=NMDC.git_url, name="workflow execution activity_git url", curie=NMDC.curie('git_url'),
                   model_uri=DEFAULT_.workflow_execution_activity_git_url, domain=WorkflowExecutionActivity, range=str)

slots.workflow_execution_activity_has_input = Slot(uri=NMDC.has_input, name="workflow execution activity_has input", curie=NMDC.curie('has_input'),
                   model_uri=DEFAULT_.workflow_execution_activity_has_input, domain=WorkflowExecutionActivity, range=Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]])

slots.workflow_execution_activity_has_output = Slot(uri=NMDC.has_output, name="workflow execution activity_has output", curie=NMDC.curie('has_output'),
                   model_uri=DEFAULT_.workflow_execution_activity_has_output, domain=WorkflowExecutionActivity, range=Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]])

slots.workflow_execution_activity_was_informed_by = Slot(uri=NMDC.was_informed_by, name="workflow execution activity_was informed by", curie=NMDC.curie('was_informed_by'),
                   model_uri=DEFAULT_.workflow_execution_activity_was_informed_by, domain=WorkflowExecutionActivity, range=Union[str, ActivityId], mappings = [PROV.wasInformedBy])

slots.workflow_execution_activity_execution_resource = Slot(uri=NMDC.execution_resource, name="workflow execution activity_execution resource", curie=NMDC.curie('execution_resource'),
                   model_uri=DEFAULT_.workflow_execution_activity_execution_resource, domain=WorkflowExecutionActivity, range=str)

slots.workflow_execution_activity_type = Slot(uri=NMDC.type, name="workflow execution activity_type", curie=NMDC.curie('type'),
                   model_uri=DEFAULT_.workflow_execution_activity_type, domain=WorkflowExecutionActivity, range=str)

slots.read_QC_analysis_activity_input_read_bases = Slot(uri=DEFAULT_.input_read_bases, name="read QC analysis activity_input_read_bases", curie=DEFAULT_.curie('input_read_bases'),
                   model_uri=DEFAULT_.read_QC_analysis_activity_input_read_bases, domain=ReadQCAnalysisActivity, range=Optional[float])

slots.read_QC_analysis_activity_output_read_bases = Slot(uri=DEFAULT_.output_read_bases, name="read QC analysis activity_output_read_bases", curie=DEFAULT_.curie('output_read_bases'),
                   model_uri=DEFAULT_.read_QC_analysis_activity_output_read_bases, domain=ReadQCAnalysisActivity, range=Optional[float])

slots.read_QC_analysis_activity_has_input = Slot(uri=NMDC.has_input, name="read QC analysis activity_has input", curie=NMDC.curie('has_input'),
                   model_uri=DEFAULT_.read_QC_analysis_activity_has_input, domain=ReadQCAnalysisActivity, range=Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]])

slots.read_QC_analysis_activity_has_output = Slot(uri=NMDC.has_output, name="read QC analysis activity_has output", curie=NMDC.curie('has_output'),
                   model_uri=DEFAULT_.read_QC_analysis_activity_has_output, domain=ReadQCAnalysisActivity, range=Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]])

slots.metabolomics_analysis_activity_used = Slot(uri=NMDC.used, name="metabolomics analysis activity_used", curie=NMDC.curie('used'),
                   model_uri=DEFAULT_.metabolomics_analysis_activity_used, domain=MetabolomicsAnalysisActivity, range=Optional[Union[str, InstrumentId]], mappings = [PROV.used])

slots.metabolomics_analysis_activity_has_metabolite_quantifications = Slot(uri=DEFAULT_.has_metabolite_quantifications, name="metabolomics analysis activity_has metabolite quantifications", curie=DEFAULT_.curie('has_metabolite_quantifications'),
                   model_uri=DEFAULT_.metabolomics_analysis_activity_has_metabolite_quantifications, domain=MetabolomicsAnalysisActivity, range=Optional[Union[Union[dict, MetaboliteQuantification], List[Union[dict, MetaboliteQuantification]]]])

slots.metabolomics_analysis_activity_has_calibration = Slot(uri=DEFAULT_.has_calibration, name="metabolomics analysis activity_has calibration", curie=DEFAULT_.curie('has_calibration'),
                   model_uri=DEFAULT_.metabolomics_analysis_activity_has_calibration, domain=MetabolomicsAnalysisActivity, range=Optional[str])

slots.metaproteomics_analysis_activity_used = Slot(uri=NMDC.used, name="metaproteomics analysis activity_used", curie=NMDC.curie('used'),
                   model_uri=DEFAULT_.metaproteomics_analysis_activity_used, domain=MetaproteomicsAnalysisActivity, range=Optional[Union[str, InstrumentId]], mappings = [PROV.used])

slots.metaproteomics_analysis_activity_has_peptide_quantifications = Slot(uri=DEFAULT_.has_peptide_quantifications, name="metaproteomics analysis activity_has peptide quantifications", curie=DEFAULT_.curie('has_peptide_quantifications'),
                   model_uri=DEFAULT_.metaproteomics_analysis_activity_has_peptide_quantifications, domain=MetaproteomicsAnalysisActivity, range=Optional[Union[Union[dict, PeptideQuantification], List[Union[dict, PeptideQuantification]]]])

slots.nom_analysis_activity_used = Slot(uri=NMDC.used, name="nom analysis activity_used", curie=NMDC.curie('used'),
                   model_uri=DEFAULT_.nom_analysis_activity_used, domain=NomAnalysisActivity, range=Optional[Union[str, InstrumentId]], mappings = [PROV.used])

slots.nom_analysis_activity_has_calibration = Slot(uri=DEFAULT_.has_calibration, name="nom analysis activity_has calibration", curie=DEFAULT_.curie('has_calibration'),
                   model_uri=DEFAULT_.nom_analysis_activity_has_calibration, domain=NomAnalysisActivity, range=Optional[str])
