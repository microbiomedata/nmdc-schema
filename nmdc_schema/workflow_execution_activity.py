# Auto generated from workflow_execution_activity.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-12-14T15:01:25
# Schema: NMDC-Workflow-Execution
#
# id: https://microbiomedata/schema/workflow_execution_activity
# description:
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
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
CHEMBL_COMPOUND = CurieNamespace('CHEMBL_COMPOUND', 'http://identifiers.org/chembl.compound/')
DRUGBANK = CurieNamespace('DRUGBANK', 'http://identifiers.org/drugbank/')
HMDB = CurieNamespace('HMDB', 'http://identifiers.org/hmdb/')
KEGG_COMPOUND = CurieNamespace('KEGG_COMPOUND', 'http://identifiers.org/kegg.compound/')
MESH = CurieNamespace('MESH', 'http://identifiers.org/mesh/')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
PR = CurieNamespace('PR', 'http://purl.obolibrary.org/obo/PR_')
PUBCHEM_COMPOUND = CurieNamespace('PUBCHEM_COMPOUND', 'http://identifiers.org/pubchem.compound/')
UNIPROTKB = CurieNamespace('UniProtKB', 'https://identifiers.org/uniprot/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
GTPO = CurieNamespace('gtpo', 'https://unknown.to.linter.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NMDC = CurieNamespace('nmdc', 'https://w3id.org/nmdc/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
QUD = CurieNamespace('qud', 'http://qudt.org/1.1/schema/qudt#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SIO = CurieNamespace('sio', 'http://semanticscience.org/resource/SIO_')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
WGS84 = CurieNamespace('wgs84', 'http://www.w3.org/2003/01/geo/wgs84_pos#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = NMDC


# Types
class ExternalIdentifier(Uriorcurie):
    """ A CURIE representing an external identifier """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "external identifier"
    type_model_uri = NMDC.ExternalIdentifier


class Bytes(int):
    """ An integer value that corresponds to a size in bytes """
    type_class_uri = XSD.long
    type_class_curie = "xsd:long"
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


# Class references
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


class MagsAnalysisActivityId(WorkflowExecutionActivityId):
    pass


class ReadQcAnalysisActivityId(WorkflowExecutionActivityId):
    pass


class ReadBasedTaxonomyAnalysisActivityId(WorkflowExecutionActivityId):
    pass


class MetabolomicsAnalysisActivityId(WorkflowExecutionActivityId):
    pass


class MetaproteomicsAnalysisActivityId(WorkflowExecutionActivityId):
    pass


class NomAnalysisActivityId(WorkflowExecutionActivityId):
    pass


class NamedThingId(extended_str):
    pass


class MaterialEntityId(NamedThingId):
    pass


class AnalyticalSampleId(MaterialEntityId):
    pass


class SiteId(MaterialEntityId):
    pass


class PlannedProcessId(NamedThingId):
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


@dataclass
class Activity(YAMLRoot):
    """
    a provence-generating activity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.Activity
    class_class_curie: ClassVar[str] = "nmdc:Activity"
    class_name: ClassVar[str] = "Activity"
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
class WorkflowExecutionActivity(Activity):
    """
    Represents an instance of an execution of a particular workflow
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.WorkflowExecutionActivity
    class_class_curie: ClassVar[str] = "nmdc:WorkflowExecutionActivity"
    class_name: ClassVar[str] = "WorkflowExecutionActivity"
    class_model_uri: ClassVar[URIRef] = NMDC.WorkflowExecutionActivity

    id: Union[str, WorkflowExecutionActivityId] = None
    execution_resource: str = None
    git_url: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_output: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    started_at_time: Union[str, XSDDateTime] = None
    ended_at_time: Union[str, XSDDateTime] = None
    was_informed_by: Union[str, ActivityId] = None
    part_of: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()
    type: Optional[str] = None
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

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.was_associated_with is not None and not isinstance(self.was_associated_with, WorkflowExecutionActivityId):
            self.was_associated_with = WorkflowExecutionActivityId(self.was_associated_with)

        super().__post_init__(**kwargs)


@dataclass
class MetagenomeAssembly(WorkflowExecutionActivity):
    """
    A workflow execution activity that converts sequencing reads into an assembled metagenome.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.MetagenomeAssembly
    class_class_curie: ClassVar[str] = "nmdc:MetagenomeAssembly"
    class_name: ClassVar[str] = "MetagenomeAssembly"
    class_model_uri: ClassVar[URIRef] = NMDC.MetagenomeAssembly

    id: Union[str, MetagenomeAssemblyId] = None
    execution_resource: str = None
    git_url: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_output: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    started_at_time: Union[str, XSDDateTime] = None
    ended_at_time: Union[str, XSDDateTime] = None
    was_informed_by: Union[str, ActivityId] = None
    type: Optional[str] = None
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

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

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


@dataclass
class MetatranscriptomeAssembly(WorkflowExecutionActivity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.MetatranscriptomeAssembly
    class_class_curie: ClassVar[str] = "nmdc:MetatranscriptomeAssembly"
    class_name: ClassVar[str] = "MetatranscriptomeAssembly"
    class_model_uri: ClassVar[URIRef] = NMDC.MetatranscriptomeAssembly

    id: Union[str, MetatranscriptomeAssemblyId] = None
    execution_resource: str = None
    git_url: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_output: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    started_at_time: Union[str, XSDDateTime] = None
    ended_at_time: Union[str, XSDDateTime] = None
    was_informed_by: Union[str, ActivityId] = None
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


@dataclass
class MetagenomeAnnotationActivity(WorkflowExecutionActivity):
    """
    A workflow execution activity that provides functional and structural annotation of assembled metagenome contigs
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.MetagenomeAnnotationActivity
    class_class_curie: ClassVar[str] = "nmdc:MetagenomeAnnotationActivity"
    class_name: ClassVar[str] = "MetagenomeAnnotationActivity"
    class_model_uri: ClassVar[URIRef] = NMDC.MetagenomeAnnotationActivity

    id: Union[str, MetagenomeAnnotationActivityId] = None
    execution_resource: str = None
    git_url: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_output: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    started_at_time: Union[str, XSDDateTime] = None
    ended_at_time: Union[str, XSDDateTime] = None
    was_informed_by: Union[str, ActivityId] = None
    type: Optional[str] = None
    gold_analysis_project_identifiers: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MetagenomeAnnotationActivityId):
            self.id = MetagenomeAnnotationActivityId(self.id)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.gold_analysis_project_identifiers, list):
            self.gold_analysis_project_identifiers = [self.gold_analysis_project_identifiers] if self.gold_analysis_project_identifiers is not None else []
        self.gold_analysis_project_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.gold_analysis_project_identifiers]

        super().__post_init__(**kwargs)


@dataclass
class MetatranscriptomeAnnotationActivity(WorkflowExecutionActivity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.MetatranscriptomeAnnotationActivity
    class_class_curie: ClassVar[str] = "nmdc:MetatranscriptomeAnnotationActivity"
    class_name: ClassVar[str] = "MetatranscriptomeAnnotationActivity"
    class_model_uri: ClassVar[URIRef] = NMDC.MetatranscriptomeAnnotationActivity

    id: Union[str, MetatranscriptomeAnnotationActivityId] = None
    execution_resource: str = None
    git_url: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_output: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    started_at_time: Union[str, XSDDateTime] = None
    ended_at_time: Union[str, XSDDateTime] = None
    was_informed_by: Union[str, ActivityId] = None
    type: Optional[str] = None
    gold_analysis_project_identifiers: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MetatranscriptomeAnnotationActivityId):
            self.id = MetatranscriptomeAnnotationActivityId(self.id)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.gold_analysis_project_identifiers, list):
            self.gold_analysis_project_identifiers = [self.gold_analysis_project_identifiers] if self.gold_analysis_project_identifiers is not None else []
        self.gold_analysis_project_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.gold_analysis_project_identifiers]

        super().__post_init__(**kwargs)


@dataclass
class MetatranscriptomeActivity(WorkflowExecutionActivity):
    """
    A metatranscriptome activity that e.g. pools assembly and annotation activity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.MetatranscriptomeActivity
    class_class_curie: ClassVar[str] = "nmdc:MetatranscriptomeActivity"
    class_name: ClassVar[str] = "MetatranscriptomeActivity"
    class_model_uri: ClassVar[URIRef] = NMDC.MetatranscriptomeActivity

    id: Union[str, MetatranscriptomeActivityId] = None
    execution_resource: str = None
    git_url: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_output: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    started_at_time: Union[str, XSDDateTime] = None
    ended_at_time: Union[str, XSDDateTime] = None
    was_informed_by: Union[str, ActivityId] = None
    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MetatranscriptomeActivityId):
            self.id = MetatranscriptomeActivityId(self.id)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass
class MagsAnalysisActivity(WorkflowExecutionActivity):
    """
    A workflow execution activity that uses computational binning tools to group assembled contigs into genomes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.MagsAnalysisActivity
    class_class_curie: ClassVar[str] = "nmdc:MagsAnalysisActivity"
    class_name: ClassVar[str] = "MagsAnalysisActivity"
    class_model_uri: ClassVar[URIRef] = NMDC.MagsAnalysisActivity

    id: Union[str, MagsAnalysisActivityId] = None
    execution_resource: str = None
    git_url: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_output: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    started_at_time: Union[str, XSDDateTime] = None
    ended_at_time: Union[str, XSDDateTime] = None
    was_informed_by: Union[str, ActivityId] = None
    type: Optional[str] = None
    input_contig_num: Optional[int] = None
    binned_contig_num: Optional[int] = None
    too_short_contig_num: Optional[int] = None
    low_depth_contig_num: Optional[int] = None
    unbinned_contig_num: Optional[int] = None
    mags_list: Optional[Union[Union[dict, "MagBin"], List[Union[dict, "MagBin"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MagsAnalysisActivityId):
            self.id = MagsAnalysisActivityId(self.id)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.input_contig_num is not None and not isinstance(self.input_contig_num, int):
            self.input_contig_num = int(self.input_contig_num)

        if self.binned_contig_num is not None and not isinstance(self.binned_contig_num, int):
            self.binned_contig_num = int(self.binned_contig_num)

        if self.too_short_contig_num is not None and not isinstance(self.too_short_contig_num, int):
            self.too_short_contig_num = int(self.too_short_contig_num)

        if self.low_depth_contig_num is not None and not isinstance(self.low_depth_contig_num, int):
            self.low_depth_contig_num = int(self.low_depth_contig_num)

        if self.unbinned_contig_num is not None and not isinstance(self.unbinned_contig_num, int):
            self.unbinned_contig_num = int(self.unbinned_contig_num)

        if not isinstance(self.mags_list, list):
            self.mags_list = [self.mags_list] if self.mags_list is not None else []
        self.mags_list = [v if isinstance(v, MagBin) else MagBin(**as_dict(v)) for v in self.mags_list]

        super().__post_init__(**kwargs)


@dataclass
class ReadQcAnalysisActivity(WorkflowExecutionActivity):
    """
    A workflow execution activity that performs quality control on raw Illumina reads including quality trimming,
    artifact removal, linker trimming, adapter trimming, spike-in removal, and human/cat/dog/mouse/microbe contaminant
    removal
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.ReadQcAnalysisActivity
    class_class_curie: ClassVar[str] = "nmdc:ReadQcAnalysisActivity"
    class_name: ClassVar[str] = "ReadQcAnalysisActivity"
    class_model_uri: ClassVar[URIRef] = NMDC.ReadQcAnalysisActivity

    id: Union[str, ReadQcAnalysisActivityId] = None
    execution_resource: str = None
    git_url: str = None
    started_at_time: Union[str, XSDDateTime] = None
    ended_at_time: Union[str, XSDDateTime] = None
    was_informed_by: Union[str, ActivityId] = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_output: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    type: Optional[str] = None
    input_read_count: Optional[float] = None
    input_base_count: Optional[float] = None
    output_read_count: Optional[float] = None
    output_base_count: Optional[float] = None
    input_read_bases: Optional[float] = None
    output_read_bases: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReadQcAnalysisActivityId):
            self.id = ReadQcAnalysisActivityId(self.id)

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

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

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
class ReadBasedTaxonomyAnalysisActivity(WorkflowExecutionActivity):
    """
    A workflow execution activity that performs taxonomy classification using sequencing reads
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.ReadBasedTaxonomyAnalysisActivity
    class_class_curie: ClassVar[str] = "nmdc:ReadBasedTaxonomyAnalysisActivity"
    class_name: ClassVar[str] = "ReadBasedTaxonomyAnalysisActivity"
    class_model_uri: ClassVar[URIRef] = NMDC.ReadBasedTaxonomyAnalysisActivity

    id: Union[str, ReadBasedTaxonomyAnalysisActivityId] = None
    execution_resource: str = None
    git_url: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_output: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    started_at_time: Union[str, XSDDateTime] = None
    ended_at_time: Union[str, XSDDateTime] = None
    was_informed_by: Union[str, ActivityId] = None
    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReadBasedTaxonomyAnalysisActivityId):
            self.id = ReadBasedTaxonomyAnalysisActivityId(self.id)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass
class MetabolomicsAnalysisActivity(WorkflowExecutionActivity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.MetabolomicsAnalysisActivity
    class_class_curie: ClassVar[str] = "nmdc:MetabolomicsAnalysisActivity"
    class_name: ClassVar[str] = "MetabolomicsAnalysisActivity"
    class_model_uri: ClassVar[URIRef] = NMDC.MetabolomicsAnalysisActivity

    id: Union[str, MetabolomicsAnalysisActivityId] = None
    execution_resource: str = None
    git_url: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_output: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    started_at_time: Union[str, XSDDateTime] = None
    ended_at_time: Union[str, XSDDateTime] = None
    was_informed_by: Union[str, ActivityId] = None
    type: Optional[str] = None
    used: Optional[Union[str, InstrumentId]] = None
    has_metabolite_quantifications: Optional[Union[Union[dict, "MetaboliteQuantification"], List[Union[dict, "MetaboliteQuantification"]]]] = empty_list()
    has_calibration: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MetabolomicsAnalysisActivityId):
            self.id = MetabolomicsAnalysisActivityId(self.id)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

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

    class_class_uri: ClassVar[URIRef] = NMDC.MetaproteomicsAnalysisActivity
    class_class_curie: ClassVar[str] = "nmdc:MetaproteomicsAnalysisActivity"
    class_name: ClassVar[str] = "MetaproteomicsAnalysisActivity"
    class_model_uri: ClassVar[URIRef] = NMDC.MetaproteomicsAnalysisActivity

    id: Union[str, MetaproteomicsAnalysisActivityId] = None
    execution_resource: str = None
    git_url: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_output: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    started_at_time: Union[str, XSDDateTime] = None
    ended_at_time: Union[str, XSDDateTime] = None
    was_informed_by: Union[str, ActivityId] = None
    type: Optional[str] = None
    used: Optional[Union[str, InstrumentId]] = None
    has_peptide_quantifications: Optional[Union[Union[dict, "PeptideQuantification"], List[Union[dict, "PeptideQuantification"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MetaproteomicsAnalysisActivityId):
            self.id = MetaproteomicsAnalysisActivityId(self.id)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.used is not None and not isinstance(self.used, InstrumentId):
            self.used = InstrumentId(self.used)

        if not isinstance(self.has_peptide_quantifications, list):
            self.has_peptide_quantifications = [self.has_peptide_quantifications] if self.has_peptide_quantifications is not None else []
        self.has_peptide_quantifications = [v if isinstance(v, PeptideQuantification) else PeptideQuantification(**as_dict(v)) for v in self.has_peptide_quantifications]

        super().__post_init__(**kwargs)


@dataclass
class NomAnalysisActivity(WorkflowExecutionActivity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.NomAnalysisActivity
    class_class_curie: ClassVar[str] = "nmdc:NomAnalysisActivity"
    class_name: ClassVar[str] = "NomAnalysisActivity"
    class_model_uri: ClassVar[URIRef] = NMDC.NomAnalysisActivity

    id: Union[str, NomAnalysisActivityId] = None
    execution_resource: str = None
    git_url: str = None
    has_input: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_output: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    started_at_time: Union[str, XSDDateTime] = None
    ended_at_time: Union[str, XSDDateTime] = None
    was_informed_by: Union[str, ActivityId] = None
    type: Optional[str] = None
    used: Optional[Union[str, InstrumentId]] = None
    has_calibration: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NomAnalysisActivityId):
            self.id = NomAnalysisActivityId(self.id)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.used is not None and not isinstance(self.used, InstrumentId):
            self.used = InstrumentId(self.used)

        if self.has_calibration is not None and not isinstance(self.has_calibration, str):
            self.has_calibration = str(self.has_calibration)

        super().__post_init__(**kwargs)


@dataclass
class Agent(YAMLRoot):
    """
    a provence-generating agent
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.Agent
    class_class_curie: ClassVar[str] = "nmdc:Agent"
    class_name: ClassVar[str] = "Agent"
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
class NamedThing(YAMLRoot):
    """
    a databased entity or concept/class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.NamedThing
    class_class_curie: ClassVar[str] = "nmdc:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
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
class MaterialEntity(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.MaterialEntity
    class_class_curie: ClassVar[str] = "nmdc:MaterialEntity"
    class_name: ClassVar[str] = "MaterialEntity"
    class_model_uri: ClassVar[URIRef] = NMDC.MaterialEntity

    id: Union[str, MaterialEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialEntityId):
            self.id = MaterialEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class AnalyticalSample(MaterialEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.AnalyticalSample
    class_class_curie: ClassVar[str] = "nmdc:AnalyticalSample"
    class_name: ClassVar[str] = "AnalyticalSample"
    class_model_uri: ClassVar[URIRef] = NMDC.AnalyticalSample

    id: Union[str, AnalyticalSampleId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnalyticalSampleId):
            self.id = AnalyticalSampleId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Site(MaterialEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.Site
    class_class_curie: ClassVar[str] = "nmdc:Site"
    class_name: ClassVar[str] = "Site"
    class_model_uri: ClassVar[URIRef] = NMDC.Site

    id: Union[str, SiteId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SiteId):
            self.id = SiteId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class PlannedProcess(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000011"]
    class_class_curie: ClassVar[str] = "OBI:0000011"
    class_name: ClassVar[str] = "PlannedProcess"
    class_model_uri: ClassVar[URIRef] = NMDC.PlannedProcess

    id: Union[str, PlannedProcessId] = None
    has_inputs: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()
    has_outputs: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()
    participating_agent: Optional[Union[dict, Agent]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlannedProcessId):
            self.id = PlannedProcessId(self.id)

        if not isinstance(self.has_inputs, list):
            self.has_inputs = [self.has_inputs] if self.has_inputs is not None else []
        self.has_inputs = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_inputs]

        if not isinstance(self.has_outputs, list):
            self.has_outputs = [self.has_outputs] if self.has_outputs is not None else []
        self.has_outputs = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_outputs]

        if self.participating_agent is not None and not isinstance(self.participating_agent, Agent):
            self.participating_agent = Agent(**as_dict(self.participating_agent))

        super().__post_init__(**kwargs)


@dataclass
class OntologyClass(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.OntologyClass
    class_class_curie: ClassVar[str] = "nmdc:OntologyClass"
    class_name: ClassVar[str] = "OntologyClass"
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
    class_name: ClassVar[str] = "EnvironmentalMaterialTerm"
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
    class_name: ClassVar[str] = "AttributeValue"
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
    class_name: ClassVar[str] = "QuantityValue"
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
    class_name: ClassVar[str] = "ImageValue"
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
    class_name: ClassVar[str] = "PersonValue"
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
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = NMDC.Person

    id: Union[str, PersonId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MagBin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.MagBin
    class_class_curie: ClassVar[str] = "nmdc:MagBin"
    class_name: ClassVar[str] = "MagBin"
    class_model_uri: ClassVar[URIRef] = NMDC.MagBin

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
    num_t_rna: Optional[int] = None
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

        if self.num_t_rna is not None and not isinstance(self.num_t_rna, int):
            self.num_t_rna = int(self.num_t_rna)

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
    class_name: ClassVar[str] = "Instrument"
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
    class_name: ClassVar[str] = "MetaboliteQuantification"
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
    class_name: ClassVar[str] = "PeptideQuantification"
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
    class_name: ClassVar[str] = "ProteinQuantification"
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
    class_name: ClassVar[str] = "ChemicalEntity"
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
    class_name: ClassVar[str] = "GeneProduct"
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
    class_name: ClassVar[str] = "TextValue"
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
    class_name: ClassVar[str] = "UrlValue"
    class_model_uri: ClassVar[URIRef] = NMDC.UrlValue


class TimestampValue(AttributeValue):
    """
    A value that is a timestamp. The range should be ISO-8601
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.TimestampValue
    class_class_curie: ClassVar[str] = "nmdc:TimestampValue"
    class_name: ClassVar[str] = "TimestampValue"
    class_model_uri: ClassVar[URIRef] = NMDC.TimestampValue


@dataclass
class IntegerValue(AttributeValue):
    """
    A value that is an integer
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.IntegerValue
    class_class_curie: ClassVar[str] = "nmdc:IntegerValue"
    class_name: ClassVar[str] = "IntegerValue"
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
    class_name: ClassVar[str] = "BooleanValue"
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
    class_name: ClassVar[str] = "ControlledTermValue"
    class_model_uri: ClassVar[URIRef] = NMDC.ControlledTermValue

    term: Optional[Union[dict, OntologyClass]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.term is not None and not isinstance(self.term, OntologyClass):
            self.term = OntologyClass(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass
class ControlledIdentifiedTermValue(ControlledTermValue):
    """
    A controlled term or class from an ontology, requiring the presence of term with an id
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.ControlledIdentifiedTermValue
    class_class_curie: ClassVar[str] = "nmdc:ControlledIdentifiedTermValue"
    class_name: ClassVar[str] = "ControlledIdentifiedTermValue"
    class_model_uri: ClassVar[URIRef] = NMDC.ControlledIdentifiedTermValue

    term: Union[dict, OntologyClass] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.term):
            self.MissingRequiredField("term")
        if not isinstance(self.term, OntologyClass):
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
    class_name: ClassVar[str] = "GeolocationValue"
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


# Enumerations


# Slots
class slots:
    pass

slots.metagenome_assembly_parameter = Slot(uri=NMDC.metagenome_assembly_parameter, name="metagenome_assembly_parameter", curie=NMDC.curie('metagenome_assembly_parameter'),
                   model_uri=NMDC.metagenome_assembly_parameter, domain=None, range=Optional[str])

slots.has_peptide_quantifications = Slot(uri=NMDC.has_peptide_quantifications, name="has_peptide_quantifications", curie=NMDC.curie('has_peptide_quantifications'),
                   model_uri=NMDC.has_peptide_quantifications, domain=None, range=Optional[str])

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

slots.has_calibration = Slot(uri=NMDC.has_calibration, name="has_calibration", curie=NMDC.curie('has_calibration'),
                   model_uri=NMDC.has_calibration, domain=None, range=Optional[str])

slots.has_metabolite_quantifications = Slot(uri=NMDC.has_metabolite_quantifications, name="has_metabolite_quantifications", curie=NMDC.curie('has_metabolite_quantifications'),
                   model_uri=NMDC.has_metabolite_quantifications, domain=None, range=Optional[str])

slots.input_read_bases = Slot(uri=NMDC.input_read_bases, name="input_read_bases", curie=NMDC.curie('input_read_bases'),
                   model_uri=NMDC.input_read_bases, domain=None, range=Optional[str])

slots.output_read_bases = Slot(uri=NMDC.output_read_bases, name="output_read_bases", curie=NMDC.curie('output_read_bases'),
                   model_uri=NMDC.output_read_bases, domain=None, range=Optional[str])

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

slots.alternative_titles = Slot(uri=NMDC.alternative_titles, name="alternative_titles", curie=NMDC.curie('alternative_titles'),
                   model_uri=NMDC.alternative_titles, domain=None, range=Optional[Union[str, List[str]]])

slots.alternative_names = Slot(uri=NMDC.alternative_names, name="alternative_names", curie=NMDC.curie('alternative_names'),
                   model_uri=NMDC.alternative_names, domain=None, range=Optional[Union[str, List[str]]])

slots.alternative_descriptions = Slot(uri=NMDC.alternative_descriptions, name="alternative_descriptions", curie=NMDC.curie('alternative_descriptions'),
                   model_uri=NMDC.alternative_descriptions, domain=None, range=Optional[Union[str, List[str]]])

slots.alternative_identifiers = Slot(uri=NMDC.alternative_identifiers, name="alternative_identifiers", curie=NMDC.curie('alternative_identifiers'),
                   model_uri=NMDC.alternative_identifiers, domain=None, range=Optional[Union[str, List[str]]])

slots.external_database_identifiers = Slot(uri=NMDC.external_database_identifiers, name="external_database_identifiers", curie=NMDC.curie('external_database_identifiers'),
                   model_uri=NMDC.external_database_identifiers, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.gold_identifiers = Slot(uri=NMDC.gold_identifiers, name="gold_identifiers", curie=NMDC.curie('gold_identifiers'),
                   model_uri=NMDC.gold_identifiers, domain=None, range=Optional[str])

slots.mgnify_identifiers = Slot(uri=NMDC.mgnify_identifiers, name="mgnify_identifiers", curie=NMDC.curie('mgnify_identifiers'),
                   model_uri=NMDC.mgnify_identifiers, domain=None, range=Optional[str])

slots.insdc_identifiers = Slot(uri=NMDC.insdc_identifiers, name="insdc_identifiers", curie=NMDC.curie('insdc_identifiers'),
                   model_uri=NMDC.insdc_identifiers, domain=None, range=Optional[str])

slots.study_identifiers = Slot(uri=NMDC.study_identifiers, name="study_identifiers", curie=NMDC.curie('study_identifiers'),
                   model_uri=NMDC.study_identifiers, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.insdc_sra_ena_study_identifiers = Slot(uri=NMDC.insdc_sra_ena_study_identifiers, name="insdc_sra_ena_study_identifiers", curie=NMDC.curie('insdc_sra_ena_study_identifiers'),
                   model_uri=NMDC.insdc_sra_ena_study_identifiers, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]],
                   pattern=re.compile(r'^insdc.sra:(E|D|S)RP[0-9]{6,}$'))

slots.insdc_bioproject_identifiers = Slot(uri=NMDC.insdc_bioproject_identifiers, name="insdc_bioproject_identifiers", curie=NMDC.curie('insdc_bioproject_identifiers'),
                   model_uri=NMDC.insdc_bioproject_identifiers, domain=None, range=Optional[str],
                   pattern=re.compile(r'^bioproject:PRJ[DEN][A-Z][0-9]+$'))

slots.gold_study_identifiers = Slot(uri=NMDC.gold_study_identifiers, name="gold_study_identifiers", curie=NMDC.curie('gold_study_identifiers'),
                   model_uri=NMDC.gold_study_identifiers, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]],
                   pattern=re.compile(r'^GOLD:Gs[0-9]+$'))

slots.mgnify_project_identifiers = Slot(uri=NMDC.mgnify_project_identifiers, name="mgnify_project_identifiers", curie=NMDC.curie('mgnify_project_identifiers'),
                   model_uri=NMDC.mgnify_project_identifiers, domain=None, range=Optional[str],
                   pattern=re.compile(r'^mgnify.proj:[A-Z]+[0-9]+$'))

slots.biosample_identifiers = Slot(uri=NMDC.biosample_identifiers, name="biosample_identifiers", curie=NMDC.curie('biosample_identifiers'),
                   model_uri=NMDC.biosample_identifiers, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.gold_biosample_identifiers = Slot(uri=NMDC.gold_biosample_identifiers, name="gold_biosample_identifiers", curie=NMDC.curie('gold_biosample_identifiers'),
                   model_uri=NMDC.gold_biosample_identifiers, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]],
                   pattern=re.compile(r'^GOLD:Gb[0-9]+$'))

slots.insdc_biosample_identifiers = Slot(uri=NMDC.insdc_biosample_identifiers, name="insdc_biosample_identifiers", curie=NMDC.curie('insdc_biosample_identifiers'),
                   model_uri=NMDC.insdc_biosample_identifiers, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]],
                   pattern=re.compile(r'^biosample:SAM[NED]([A-Z])?[0-9]+$'))

slots.insdc_secondary_sample_identifiers = Slot(uri=NMDC.insdc_secondary_sample_identifiers, name="insdc_secondary_sample_identifiers", curie=NMDC.curie('insdc_secondary_sample_identifiers'),
                   model_uri=NMDC.insdc_secondary_sample_identifiers, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]],
                   pattern=re.compile(r'^biosample:(E|D|S)RS[0-9]{6,}$'))

slots.omics_processing_identifiers = Slot(uri=NMDC.omics_processing_identifiers, name="omics_processing_identifiers", curie=NMDC.curie('omics_processing_identifiers'),
                   model_uri=NMDC.omics_processing_identifiers, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.gold_sequencing_project_identifiers = Slot(uri=NMDC.gold_sequencing_project_identifiers, name="gold_sequencing_project_identifiers", curie=NMDC.curie('gold_sequencing_project_identifiers'),
                   model_uri=NMDC.gold_sequencing_project_identifiers, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]],
                   pattern=re.compile(r'^GOLD:Gp[0-9]+$'))

slots.insdc_experiment_identifiers = Slot(uri=NMDC.insdc_experiment_identifiers, name="insdc_experiment_identifiers", curie=NMDC.curie('insdc_experiment_identifiers'),
                   model_uri=NMDC.insdc_experiment_identifiers, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]],
                   pattern=re.compile(r'^insdc.sra:(E|D|S)RX[0-9]{6,}$'))

slots.analysis_identifiers = Slot(uri=NMDC.analysis_identifiers, name="analysis_identifiers", curie=NMDC.curie('analysis_identifiers'),
                   model_uri=NMDC.analysis_identifiers, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.gold_analysis_project_identifiers = Slot(uri=NMDC.gold_analysis_project_identifiers, name="gold_analysis_project_identifiers", curie=NMDC.curie('gold_analysis_project_identifiers'),
                   model_uri=NMDC.gold_analysis_project_identifiers, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]],
                   pattern=re.compile(r'^GOLD:Ga[0-9]+$'))

slots.insdc_analysis_identifiers = Slot(uri=NMDC.insdc_analysis_identifiers, name="insdc_analysis_identifiers", curie=NMDC.curie('insdc_analysis_identifiers'),
                   model_uri=NMDC.insdc_analysis_identifiers, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]],
                   pattern=re.compile(r'^insdc.sra:(E|D|S)RR[0-9]{6,}$'))

slots.mgnify_analysis_identifiers = Slot(uri=NMDC.mgnify_analysis_identifiers, name="mgnify_analysis_identifiers", curie=NMDC.curie('mgnify_analysis_identifiers'),
                   model_uri=NMDC.mgnify_analysis_identifiers, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.assembly_identifiers = Slot(uri=NMDC.assembly_identifiers, name="assembly_identifiers", curie=NMDC.curie('assembly_identifiers'),
                   model_uri=NMDC.assembly_identifiers, domain=None, range=Optional[str])

slots.insdc_assembly_identifiers = Slot(uri=NMDC.insdc_assembly_identifiers, name="insdc_assembly_identifiers", curie=NMDC.curie('insdc_assembly_identifiers'),
                   model_uri=NMDC.insdc_assembly_identifiers, domain=None, range=Optional[str],
                   pattern=re.compile(r'^insdc.sra:[A-Z]+[0-9]+(\.[0-9]+)?$'))

slots.started_at_time = Slot(uri=NMDC.started_at_time, name="started_at_time", curie=NMDC.curie('started_at_time'),
                   model_uri=NMDC.started_at_time, domain=None, range=Optional[Union[str, XSDDateTime]], mappings = [PROV.startedAtTime],
                   pattern=re.compile(r'^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$'))

slots.ended_at_time = Slot(uri=NMDC.ended_at_time, name="ended_at_time", curie=NMDC.curie('ended_at_time'),
                   model_uri=NMDC.ended_at_time, domain=None, range=Optional[Union[str, XSDDateTime]], mappings = [PROV.endedAtTime],
                   pattern=re.compile(r'^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$'))

slots.was_informed_by = Slot(uri=NMDC.was_informed_by, name="was_informed_by", curie=NMDC.curie('was_informed_by'),
                   model_uri=NMDC.was_informed_by, domain=None, range=Optional[Union[str, ActivityId]], mappings = [PROV.wasInformedBy])

slots.was_associated_with = Slot(uri=NMDC.was_associated_with, name="was_associated_with", curie=NMDC.curie('was_associated_with'),
                   model_uri=NMDC.was_associated_with, domain=None, range=Optional[Union[dict, Agent]], mappings = [PROV.wasAssociatedWith])

slots.acted_on_behalf_of = Slot(uri=NMDC.acted_on_behalf_of, name="acted_on_behalf_of", curie=NMDC.curie('acted_on_behalf_of'),
                   model_uri=NMDC.acted_on_behalf_of, domain=None, range=Optional[Union[dict, Agent]], mappings = [PROV.actedOnBehalfOf])

slots.was_generated_by = Slot(uri=NMDC.was_generated_by, name="was_generated_by", curie=NMDC.curie('was_generated_by'),
                   model_uri=NMDC.was_generated_by, domain=None, range=Optional[Union[str, ActivityId]], mappings = [PROV.wasGeneratedBy])

slots.used = Slot(uri=NMDC.used, name="used", curie=NMDC.curie('used'),
                   model_uri=NMDC.used, domain=Activity, range=Optional[str], mappings = [PROV.used])

slots.has_inputs = Slot(uri=NMDC.has_inputs, name="has_inputs", curie=NMDC.curie('has_inputs'),
                   model_uri=NMDC.has_inputs, domain=PlannedProcess, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_outputs = Slot(uri=NMDC.has_outputs, name="has_outputs", curie=NMDC.curie('has_outputs'),
                   model_uri=NMDC.has_outputs, domain=PlannedProcess, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.participating_agent = Slot(uri=NMDC.participating_agent, name="participating_agent", curie=NMDC.curie('participating_agent'),
                   model_uri=NMDC.participating_agent, domain=PlannedProcess, range=Optional[Union[dict, Agent]])

slots.language = Slot(uri=NMDC.language, name="language", curie=NMDC.curie('language'),
                   model_uri=NMDC.language, domain=None, range=Optional[str])

slots.attribute = Slot(uri=NMDC.attribute, name="attribute", curie=NMDC.curie('attribute'),
                   model_uri=NMDC.attribute, domain=None, range=Optional[str])

slots.has_raw_value = Slot(uri=NMDC.has_raw_value, name="has_raw_value", curie=NMDC.curie('has_raw_value'),
                   model_uri=NMDC.has_raw_value, domain=AttributeValue, range=Optional[str])

slots.has_unit = Slot(uri=NMDC.has_unit, name="has_unit", curie=NMDC.curie('has_unit'),
                   model_uri=NMDC.has_unit, domain=None, range=Optional[str], mappings = [QUD.unit, SCHEMA.unitCode])

slots.has_numeric_value = Slot(uri=NMDC.has_numeric_value, name="has_numeric_value", curie=NMDC.curie('has_numeric_value'),
                   model_uri=NMDC.has_numeric_value, domain=None, range=Optional[float], mappings = [QUD.quantityValue, SCHEMA.value])

slots.has_minimum_numeric_value = Slot(uri=NMDC.has_minimum_numeric_value, name="has_minimum_numeric_value", curie=NMDC.curie('has_minimum_numeric_value'),
                   model_uri=NMDC.has_minimum_numeric_value, domain=None, range=Optional[float])

slots.has_maximum_numeric_value = Slot(uri=NMDC.has_maximum_numeric_value, name="has_maximum_numeric_value", curie=NMDC.curie('has_maximum_numeric_value'),
                   model_uri=NMDC.has_maximum_numeric_value, domain=None, range=Optional[float])

slots.has_boolean_value = Slot(uri=NMDC.has_boolean_value, name="has_boolean_value", curie=NMDC.curie('has_boolean_value'),
                   model_uri=NMDC.has_boolean_value, domain=None, range=Optional[Union[bool, Bool]])

slots.latitude = Slot(uri=WGS84.lat, name="latitude", curie=WGS84.curie('lat'),
                   model_uri=NMDC.latitude, domain=GeolocationValue, range=Optional[float], mappings = [SCHEMA.latitude])

slots.longitude = Slot(uri=WGS84.long, name="longitude", curie=WGS84.curie('long'),
                   model_uri=NMDC.longitude, domain=GeolocationValue, range=Optional[float], mappings = [SCHEMA.longitude])

slots.term = Slot(uri=NMDC.term, name="term", curie=NMDC.curie('term'),
                   model_uri=NMDC.term, domain=ControlledTermValue, range=Optional[Union[dict, OntologyClass]])

slots.orcid = Slot(uri=NMDC.orcid, name="orcid", curie=NMDC.curie('orcid'),
                   model_uri=NMDC.orcid, domain=PersonValue, range=Optional[str])

slots.email = Slot(uri=SCHEMA.email, name="email", curie=SCHEMA.curie('email'),
                   model_uri=NMDC.email, domain=None, range=Optional[str])

slots.alternate_emails = Slot(uri=NMDC.alternate_emails, name="alternate_emails", curie=NMDC.curie('alternate_emails'),
                   model_uri=NMDC.alternate_emails, domain=None, range=Optional[str])

slots.profile_image_url = Slot(uri=NMDC.profile_image_url, name="profile_image_url", curie=NMDC.curie('profile_image_url'),
                   model_uri=NMDC.profile_image_url, domain=PersonValue, range=Optional[str])

slots.has_input = Slot(uri=NMDC.has_input, name="has_input", curie=NMDC.curie('has_input'),
                   model_uri=NMDC.has_input, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_output = Slot(uri=NMDC.has_output, name="has_output", curie=NMDC.curie('has_output'),
                   model_uri=NMDC.has_output, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.part_of = Slot(uri=DCTERMS.isPartOf, name="part_of", curie=DCTERMS.curie('isPartOf'),
                   model_uri=NMDC.part_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.execution_resource = Slot(uri=NMDC.execution_resource, name="execution_resource", curie=NMDC.curie('execution_resource'),
                   model_uri=NMDC.execution_resource, domain=None, range=Optional[str])

slots.url = Slot(uri=NMDC.url, name="url", curie=NMDC.curie('url'),
                   model_uri=NMDC.url, domain=None, range=Optional[str])

slots.display_order = Slot(uri=NMDC.display_order, name="display_order", curie=NMDC.curie('display_order'),
                   model_uri=NMDC.display_order, domain=None, range=Optional[str])

slots.git_url = Slot(uri=NMDC.git_url, name="git_url", curie=NMDC.curie('git_url'),
                   model_uri=NMDC.git_url, domain=None, range=Optional[str])

slots.file_size_bytes = Slot(uri=NMDC.file_size_bytes, name="file_size_bytes", curie=NMDC.curie('file_size_bytes'),
                   model_uri=NMDC.file_size_bytes, domain=None, range=Optional[int])

slots.md5_checksum = Slot(uri=NMDC.md5_checksum, name="md5_checksum", curie=NMDC.curie('md5_checksum'),
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

slots.all_proteins = Slot(uri=NMDC.all_proteins, name="all_proteins", curie=NMDC.curie('all_proteins'),
                   model_uri=NMDC.all_proteins, domain=None, range=Optional[str])

slots.best_protein = Slot(uri=NMDC.best_protein, name="best_protein", curie=NMDC.curie('best_protein'),
                   model_uri=NMDC.best_protein, domain=None, range=Optional[str])

slots.chemical_formula = Slot(uri=NMDC.chemical_formula, name="chemical_formula", curie=NMDC.curie('chemical_formula'),
                   model_uri=NMDC.chemical_formula, domain=None, range=Optional[str])

slots.inchi_key = Slot(uri=NMDC.inchi_key, name="inchi_key", curie=NMDC.curie('inchi_key'),
                   model_uri=NMDC.inchi_key, domain=None, range=Optional[str])

slots.inchi = Slot(uri=NMDC.inchi, name="inchi", curie=NMDC.curie('inchi'),
                   model_uri=NMDC.inchi, domain=None, range=Optional[str])

slots.min_q_value = Slot(uri=NMDC.min_q_value, name="min_q_value", curie=NMDC.curie('min_q_value'),
                   model_uri=NMDC.min_q_value, domain=None, range=Optional[str])

slots.peptide_sequence = Slot(uri=NMDC.peptide_sequence, name="peptide_sequence", curie=NMDC.curie('peptide_sequence'),
                   model_uri=NMDC.peptide_sequence, domain=None, range=Optional[str])

slots.peptide_sequence_count = Slot(uri=NMDC.peptide_sequence_count, name="peptide_sequence_count", curie=NMDC.curie('peptide_sequence_count'),
                   model_uri=NMDC.peptide_sequence_count, domain=None, range=Optional[str])

slots.peptide_spectral_count = Slot(uri=NMDC.peptide_spectral_count, name="peptide_spectral_count", curie=NMDC.curie('peptide_spectral_count'),
                   model_uri=NMDC.peptide_spectral_count, domain=None, range=Optional[str])

slots.peptide_sum_masic_abundance = Slot(uri=NMDC.peptide_sum_masic_abundance, name="peptide_sum_masic_abundance", curie=NMDC.curie('peptide_sum_masic_abundance'),
                   model_uri=NMDC.peptide_sum_masic_abundance, domain=None, range=Optional[str])

slots.protein_spectral_count = Slot(uri=NMDC.protein_spectral_count, name="protein_spectral_count", curie=NMDC.curie('protein_spectral_count'),
                   model_uri=NMDC.protein_spectral_count, domain=None, range=Optional[str])

slots.protein_sum_masic_abundance = Slot(uri=NMDC.protein_sum_masic_abundance, name="protein_sum_masic_abundance", curie=NMDC.curie('protein_sum_masic_abundance'),
                   model_uri=NMDC.protein_sum_masic_abundance, domain=None, range=Optional[str])

slots.smiles = Slot(uri=NMDC.smiles, name="smiles", curie=NMDC.curie('smiles'),
                   model_uri=NMDC.smiles, domain=None, range=Optional[str])

slots.metabolite_quantified = Slot(uri=NMDC.metabolite_quantified, name="metabolite_quantified", curie=NMDC.curie('metabolite_quantified'),
                   model_uri=NMDC.metabolite_quantified, domain=None, range=Optional[str])

slots.highest_similarity_score = Slot(uri=NMDC.highest_similarity_score, name="highest_similarity_score", curie=NMDC.curie('highest_similarity_score'),
                   model_uri=NMDC.highest_similarity_score, domain=None, range=Optional[str])

slots.magBin__bin_name = Slot(uri=NMDC.bin_name, name="magBin__bin_name", curie=NMDC.curie('bin_name'),
                   model_uri=NMDC.magBin__bin_name, domain=None, range=Optional[str])

slots.magBin__number_of_contig = Slot(uri=NMDC.number_of_contig, name="magBin__number_of_contig", curie=NMDC.curie('number_of_contig'),
                   model_uri=NMDC.magBin__number_of_contig, domain=None, range=Optional[int])

slots.magBin__completeness = Slot(uri=NMDC.completeness, name="magBin__completeness", curie=NMDC.curie('completeness'),
                   model_uri=NMDC.magBin__completeness, domain=None, range=Optional[float])

slots.magBin__contamination = Slot(uri=NMDC.contamination, name="magBin__contamination", curie=NMDC.curie('contamination'),
                   model_uri=NMDC.magBin__contamination, domain=None, range=Optional[float])

slots.magBin__gene_count = Slot(uri=NMDC.gene_count, name="magBin__gene_count", curie=NMDC.curie('gene_count'),
                   model_uri=NMDC.magBin__gene_count, domain=None, range=Optional[int])

slots.magBin__bin_quality = Slot(uri=NMDC.bin_quality, name="magBin__bin_quality", curie=NMDC.curie('bin_quality'),
                   model_uri=NMDC.magBin__bin_quality, domain=None, range=Optional[str])

slots.magBin__num_16s = Slot(uri=NMDC.num_16s, name="magBin__num_16s", curie=NMDC.curie('num_16s'),
                   model_uri=NMDC.magBin__num_16s, domain=None, range=Optional[int])

slots.magBin__num_5s = Slot(uri=NMDC.num_5s, name="magBin__num_5s", curie=NMDC.curie('num_5s'),
                   model_uri=NMDC.magBin__num_5s, domain=None, range=Optional[int])

slots.magBin__num_23s = Slot(uri=NMDC.num_23s, name="magBin__num_23s", curie=NMDC.curie('num_23s'),
                   model_uri=NMDC.magBin__num_23s, domain=None, range=Optional[int])

slots.magBin__num_t_rna = Slot(uri=NMDC.num_t_rna, name="magBin__num_t_rna", curie=NMDC.curie('num_t_rna'),
                   model_uri=NMDC.magBin__num_t_rna, domain=None, range=Optional[int])

slots.magBin__gtdbtk_domain = Slot(uri=NMDC.gtdbtk_domain, name="magBin__gtdbtk_domain", curie=NMDC.curie('gtdbtk_domain'),
                   model_uri=NMDC.magBin__gtdbtk_domain, domain=None, range=Optional[str])

slots.magBin__gtdbtk_phylum = Slot(uri=NMDC.gtdbtk_phylum, name="magBin__gtdbtk_phylum", curie=NMDC.curie('gtdbtk_phylum'),
                   model_uri=NMDC.magBin__gtdbtk_phylum, domain=None, range=Optional[str])

slots.magBin__gtdbtk_class = Slot(uri=NMDC.gtdbtk_class, name="magBin__gtdbtk_class", curie=NMDC.curie('gtdbtk_class'),
                   model_uri=NMDC.magBin__gtdbtk_class, domain=None, range=Optional[str])

slots.magBin__gtdbtk_order = Slot(uri=NMDC.gtdbtk_order, name="magBin__gtdbtk_order", curie=NMDC.curie('gtdbtk_order'),
                   model_uri=NMDC.magBin__gtdbtk_order, domain=None, range=Optional[str])

slots.magBin__gtdbtk_family = Slot(uri=NMDC.gtdbtk_family, name="magBin__gtdbtk_family", curie=NMDC.curie('gtdbtk_family'),
                   model_uri=NMDC.magBin__gtdbtk_family, domain=None, range=Optional[str])

slots.magBin__gtdbtk_genus = Slot(uri=NMDC.gtdbtk_genus, name="magBin__gtdbtk_genus", curie=NMDC.curie('gtdbtk_genus'),
                   model_uri=NMDC.magBin__gtdbtk_genus, domain=None, range=Optional[str])

slots.magBin__gtdbtk_species = Slot(uri=NMDC.gtdbtk_species, name="magBin__gtdbtk_species", curie=NMDC.curie('gtdbtk_species'),
                   model_uri=NMDC.magBin__gtdbtk_species, domain=None, range=Optional[str])

slots.WorkflowExecutionActivity_was_associated_with = Slot(uri=NMDC.was_associated_with, name="WorkflowExecutionActivity_was_associated_with", curie=NMDC.curie('was_associated_with'),
                   model_uri=NMDC.WorkflowExecutionActivity_was_associated_with, domain=WorkflowExecutionActivity, range=Optional[Union[str, WorkflowExecutionActivityId]], mappings = [PROV.wasAssociatedWith])

slots.WorkflowExecutionActivity_started_at_time = Slot(uri=NMDC.started_at_time, name="WorkflowExecutionActivity_started_at_time", curie=NMDC.curie('started_at_time'),
                   model_uri=NMDC.WorkflowExecutionActivity_started_at_time, domain=WorkflowExecutionActivity, range=Union[str, XSDDateTime], mappings = [PROV.startedAtTime],
                   pattern=re.compile(r'^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$'))

slots.WorkflowExecutionActivity_ended_at_time = Slot(uri=NMDC.ended_at_time, name="WorkflowExecutionActivity_ended_at_time", curie=NMDC.curie('ended_at_time'),
                   model_uri=NMDC.WorkflowExecutionActivity_ended_at_time, domain=WorkflowExecutionActivity, range=Union[str, XSDDateTime], mappings = [PROV.endedAtTime],
                   pattern=re.compile(r'^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$'))

slots.WorkflowExecutionActivity_git_url = Slot(uri=NMDC.git_url, name="WorkflowExecutionActivity_git_url", curie=NMDC.curie('git_url'),
                   model_uri=NMDC.WorkflowExecutionActivity_git_url, domain=WorkflowExecutionActivity, range=str)

slots.WorkflowExecutionActivity_has_input = Slot(uri=NMDC.has_input, name="WorkflowExecutionActivity_has_input", curie=NMDC.curie('has_input'),
                   model_uri=NMDC.WorkflowExecutionActivity_has_input, domain=WorkflowExecutionActivity, range=Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]])

slots.WorkflowExecutionActivity_has_output = Slot(uri=NMDC.has_output, name="WorkflowExecutionActivity_has_output", curie=NMDC.curie('has_output'),
                   model_uri=NMDC.WorkflowExecutionActivity_has_output, domain=WorkflowExecutionActivity, range=Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]])

slots.WorkflowExecutionActivity_was_informed_by = Slot(uri=NMDC.was_informed_by, name="WorkflowExecutionActivity_was_informed_by", curie=NMDC.curie('was_informed_by'),
                   model_uri=NMDC.WorkflowExecutionActivity_was_informed_by, domain=WorkflowExecutionActivity, range=Union[str, ActivityId], mappings = [PROV.wasInformedBy])

slots.WorkflowExecutionActivity_execution_resource = Slot(uri=NMDC.execution_resource, name="WorkflowExecutionActivity_execution_resource", curie=NMDC.curie('execution_resource'),
                   model_uri=NMDC.WorkflowExecutionActivity_execution_resource, domain=WorkflowExecutionActivity, range=str)

slots.WorkflowExecutionActivity_type = Slot(uri=NMDC.type, name="WorkflowExecutionActivity_type", curie=NMDC.curie('type'),
                   model_uri=NMDC.WorkflowExecutionActivity_type, domain=WorkflowExecutionActivity, range=Optional[str])

slots.ReadQcAnalysisActivity_input_read_bases = Slot(uri=NMDC.input_read_bases, name="ReadQcAnalysisActivity_input_read_bases", curie=NMDC.curie('input_read_bases'),
                   model_uri=NMDC.ReadQcAnalysisActivity_input_read_bases, domain=ReadQcAnalysisActivity, range=Optional[float])

slots.ReadQcAnalysisActivity_output_read_bases = Slot(uri=NMDC.output_read_bases, name="ReadQcAnalysisActivity_output_read_bases", curie=NMDC.curie('output_read_bases'),
                   model_uri=NMDC.ReadQcAnalysisActivity_output_read_bases, domain=ReadQcAnalysisActivity, range=Optional[float])

slots.ReadQcAnalysisActivity_has_input = Slot(uri=NMDC.has_input, name="ReadQcAnalysisActivity_has_input", curie=NMDC.curie('has_input'),
                   model_uri=NMDC.ReadQcAnalysisActivity_has_input, domain=ReadQcAnalysisActivity, range=Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]])

slots.ReadQcAnalysisActivity_has_output = Slot(uri=NMDC.has_output, name="ReadQcAnalysisActivity_has_output", curie=NMDC.curie('has_output'),
                   model_uri=NMDC.ReadQcAnalysisActivity_has_output, domain=ReadQcAnalysisActivity, range=Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]])

slots.MetabolomicsAnalysisActivity_used = Slot(uri=NMDC.used, name="MetabolomicsAnalysisActivity_used", curie=NMDC.curie('used'),
                   model_uri=NMDC.MetabolomicsAnalysisActivity_used, domain=MetabolomicsAnalysisActivity, range=Optional[Union[str, InstrumentId]], mappings = [PROV.used])

slots.MetabolomicsAnalysisActivity_has_metabolite_quantifications = Slot(uri=NMDC.has_metabolite_quantifications, name="MetabolomicsAnalysisActivity_has_metabolite_quantifications", curie=NMDC.curie('has_metabolite_quantifications'),
                   model_uri=NMDC.MetabolomicsAnalysisActivity_has_metabolite_quantifications, domain=MetabolomicsAnalysisActivity, range=Optional[Union[Union[dict, "MetaboliteQuantification"], List[Union[dict, "MetaboliteQuantification"]]]])

slots.MetabolomicsAnalysisActivity_has_calibration = Slot(uri=NMDC.has_calibration, name="MetabolomicsAnalysisActivity_has_calibration", curie=NMDC.curie('has_calibration'),
                   model_uri=NMDC.MetabolomicsAnalysisActivity_has_calibration, domain=MetabolomicsAnalysisActivity, range=Optional[str])

slots.MetaproteomicsAnalysisActivity_used = Slot(uri=NMDC.used, name="MetaproteomicsAnalysisActivity_used", curie=NMDC.curie('used'),
                   model_uri=NMDC.MetaproteomicsAnalysisActivity_used, domain=MetaproteomicsAnalysisActivity, range=Optional[Union[str, InstrumentId]], mappings = [PROV.used])

slots.MetaproteomicsAnalysisActivity_has_peptide_quantifications = Slot(uri=NMDC.has_peptide_quantifications, name="MetaproteomicsAnalysisActivity_has_peptide_quantifications", curie=NMDC.curie('has_peptide_quantifications'),
                   model_uri=NMDC.MetaproteomicsAnalysisActivity_has_peptide_quantifications, domain=MetaproteomicsAnalysisActivity, range=Optional[Union[Union[dict, "PeptideQuantification"], List[Union[dict, "PeptideQuantification"]]]])

slots.NomAnalysisActivity_used = Slot(uri=NMDC.used, name="NomAnalysisActivity_used", curie=NMDC.curie('used'),
                   model_uri=NMDC.NomAnalysisActivity_used, domain=NomAnalysisActivity, range=Optional[Union[str, InstrumentId]], mappings = [PROV.used])

slots.NomAnalysisActivity_has_calibration = Slot(uri=NMDC.has_calibration, name="NomAnalysisActivity_has_calibration", curie=NMDC.curie('has_calibration'),
                   model_uri=NMDC.NomAnalysisActivity_has_calibration, domain=NomAnalysisActivity, range=Optional[str])

slots.AttributeValue_type = Slot(uri=NMDC.type, name="AttributeValue_type", curie=NMDC.curie('type'),
                   model_uri=NMDC.AttributeValue_type, domain=AttributeValue, range=Optional[str])

slots.QuantityValue_has_raw_value = Slot(uri=NMDC.has_raw_value, name="QuantityValue_has_raw_value", curie=NMDC.curie('has_raw_value'),
                   model_uri=NMDC.QuantityValue_has_raw_value, domain=QuantityValue, range=Optional[str])

slots.QuantityValue_has_unit = Slot(uri=NMDC.has_unit, name="QuantityValue_has_unit", curie=NMDC.curie('has_unit'),
                   model_uri=NMDC.QuantityValue_has_unit, domain=QuantityValue, range=Optional[str], mappings = [QUD.unit, SCHEMA.unitCode])

slots.QuantityValue_has_numeric_value = Slot(uri=NMDC.has_numeric_value, name="QuantityValue_has_numeric_value", curie=NMDC.curie('has_numeric_value'),
                   model_uri=NMDC.QuantityValue_has_numeric_value, domain=QuantityValue, range=Optional[float], mappings = [QUD.quantityValue, SCHEMA.value])

slots.PersonValue_orcid = Slot(uri=NMDC.orcid, name="PersonValue_orcid", curie=NMDC.curie('orcid'),
                   model_uri=NMDC.PersonValue_orcid, domain=PersonValue, range=Optional[str])

slots.PersonValue_email = Slot(uri=SCHEMA.email, name="PersonValue_email", curie=SCHEMA.curie('email'),
                   model_uri=NMDC.PersonValue_email, domain=PersonValue, range=Optional[str])

slots.PersonValue_has_raw_value = Slot(uri=NMDC.has_raw_value, name="PersonValue_has_raw_value", curie=NMDC.curie('has_raw_value'),
                   model_uri=NMDC.PersonValue_has_raw_value, domain=PersonValue, range=Optional[str])

slots.PersonValue_name = Slot(uri=NMDC.name, name="PersonValue_name", curie=NMDC.curie('name'),
                   model_uri=NMDC.PersonValue_name, domain=PersonValue, range=Optional[str])

slots.Person_id = Slot(uri=NMDC.id, name="Person_id", curie=NMDC.curie('id'),
                   model_uri=NMDC.Person_id, domain=Person, range=Union[str, PersonId])

slots.MetaboliteQuantification_metabolite_quantified = Slot(uri=NMDC.metabolite_quantified, name="MetaboliteQuantification_metabolite_quantified", curie=NMDC.curie('metabolite_quantified'),
                   model_uri=NMDC.MetaboliteQuantification_metabolite_quantified, domain=MetaboliteQuantification, range=Optional[Union[str, ChemicalEntityId]])

slots.MetaboliteQuantification_highest_similarity_score = Slot(uri=NMDC.highest_similarity_score, name="MetaboliteQuantification_highest_similarity_score", curie=NMDC.curie('highest_similarity_score'),
                   model_uri=NMDC.MetaboliteQuantification_highest_similarity_score, domain=MetaboliteQuantification, range=Optional[float])

slots.PeptideQuantification_peptide_sequence = Slot(uri=NMDC.peptide_sequence, name="PeptideQuantification_peptide_sequence", curie=NMDC.curie('peptide_sequence'),
                   model_uri=NMDC.PeptideQuantification_peptide_sequence, domain=PeptideQuantification, range=Optional[str])

slots.PeptideQuantification_best_protein = Slot(uri=NMDC.best_protein, name="PeptideQuantification_best_protein", curie=NMDC.curie('best_protein'),
                   model_uri=NMDC.PeptideQuantification_best_protein, domain=PeptideQuantification, range=Optional[Union[str, GeneProductId]])

slots.PeptideQuantification_all_proteins = Slot(uri=NMDC.all_proteins, name="PeptideQuantification_all_proteins", curie=NMDC.curie('all_proteins'),
                   model_uri=NMDC.PeptideQuantification_all_proteins, domain=PeptideQuantification, range=Optional[Union[Union[str, GeneProductId], List[Union[str, GeneProductId]]]])

slots.PeptideQuantification_min_q_value = Slot(uri=NMDC.min_q_value, name="PeptideQuantification_min_q_value", curie=NMDC.curie('min_q_value'),
                   model_uri=NMDC.PeptideQuantification_min_q_value, domain=PeptideQuantification, range=Optional[float])

slots.PeptideQuantification_peptide_spectral_count = Slot(uri=NMDC.peptide_spectral_count, name="PeptideQuantification_peptide_spectral_count", curie=NMDC.curie('peptide_spectral_count'),
                   model_uri=NMDC.PeptideQuantification_peptide_spectral_count, domain=PeptideQuantification, range=Optional[int])

slots.PeptideQuantification_peptide_sum_masic_abundance = Slot(uri=NMDC.peptide_sum_masic_abundance, name="PeptideQuantification_peptide_sum_masic_abundance", curie=NMDC.curie('peptide_sum_masic_abundance'),
                   model_uri=NMDC.PeptideQuantification_peptide_sum_masic_abundance, domain=PeptideQuantification, range=Optional[int])

slots.ProteinQuantification_best_protein = Slot(uri=NMDC.best_protein, name="ProteinQuantification_best_protein", curie=NMDC.curie('best_protein'),
                   model_uri=NMDC.ProteinQuantification_best_protein, domain=ProteinQuantification, range=Optional[Union[str, GeneProductId]])

slots.ProteinQuantification_all_proteins = Slot(uri=NMDC.all_proteins, name="ProteinQuantification_all_proteins", curie=NMDC.curie('all_proteins'),
                   model_uri=NMDC.ProteinQuantification_all_proteins, domain=ProteinQuantification, range=Optional[Union[Union[str, GeneProductId], List[Union[str, GeneProductId]]]])

slots.ProteinQuantification_peptide_sequence_count = Slot(uri=NMDC.peptide_sequence_count, name="ProteinQuantification_peptide_sequence_count", curie=NMDC.curie('peptide_sequence_count'),
                   model_uri=NMDC.ProteinQuantification_peptide_sequence_count, domain=ProteinQuantification, range=Optional[int])

slots.ProteinQuantification_protein_spectral_count = Slot(uri=NMDC.protein_spectral_count, name="ProteinQuantification_protein_spectral_count", curie=NMDC.curie('protein_spectral_count'),
                   model_uri=NMDC.ProteinQuantification_protein_spectral_count, domain=ProteinQuantification, range=Optional[int])

slots.ProteinQuantification_protein_sum_masic_abundance = Slot(uri=NMDC.protein_sum_masic_abundance, name="ProteinQuantification_protein_sum_masic_abundance", curie=NMDC.curie('protein_sum_masic_abundance'),
                   model_uri=NMDC.ProteinQuantification_protein_sum_masic_abundance, domain=ProteinQuantification, range=Optional[int])

slots.ChemicalEntity_inchi = Slot(uri=NMDC.inchi, name="ChemicalEntity_inchi", curie=NMDC.curie('inchi'),
                   model_uri=NMDC.ChemicalEntity_inchi, domain=ChemicalEntity, range=Optional[str])

slots.ChemicalEntity_inchi_key = Slot(uri=NMDC.inchi_key, name="ChemicalEntity_inchi_key", curie=NMDC.curie('inchi_key'),
                   model_uri=NMDC.ChemicalEntity_inchi_key, domain=ChemicalEntity, range=Optional[str])

slots.ChemicalEntity_smiles = Slot(uri=NMDC.smiles, name="ChemicalEntity_smiles", curie=NMDC.curie('smiles'),
                   model_uri=NMDC.ChemicalEntity_smiles, domain=ChemicalEntity, range=Optional[Union[str, List[str]]])

slots.ChemicalEntity_chemical_formula = Slot(uri=NMDC.chemical_formula, name="ChemicalEntity_chemical_formula", curie=NMDC.curie('chemical_formula'),
                   model_uri=NMDC.ChemicalEntity_chemical_formula, domain=ChemicalEntity, range=Optional[str])

slots.ControlledIdentifiedTermValue_term = Slot(uri=NMDC.term, name="ControlledIdentifiedTermValue_term", curie=NMDC.curie('term'),
                   model_uri=NMDC.ControlledIdentifiedTermValue_term, domain=ControlledIdentifiedTermValue, range=Union[dict, OntologyClass])

slots.GeolocationValue_has_raw_value = Slot(uri=NMDC.has_raw_value, name="GeolocationValue_has_raw_value", curie=NMDC.curie('has_raw_value'),
                   model_uri=NMDC.GeolocationValue_has_raw_value, domain=GeolocationValue, range=Optional[str])
