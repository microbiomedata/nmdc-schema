# Auto generated from core.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-06-15T10:43:31
# Schema: NMDC-Core
#
# id: https://microbiomedata/schema/core
# description: Schema for National Microbiome Data Collaborative (NMDC), Core Types
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
from linkml_runtime.linkml_model.types import Boolean, Datetime, Double, Float, Integer, String
from linkml_runtime.utils.metamodelcore import Bool, XSDDateTime

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
MS = CurieNamespace('MS', 'http://purl.obolibrary.org/obo/MS_')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
PR = CurieNamespace('PR', 'http://purl.obolibrary.org/obo/PR_')
PUBCHEM_COMPOUND = CurieNamespace('PUBCHEM_COMPOUND', 'http://identifiers.org/pubchem.compound/')
UNIPROTKB = CurieNamespace('UniProtKB', 'http://example.org/UNKNOWN/UniProtKB/')
BIOLINK = CurieNamespace('biolink', 'http://example.org/UNKNOWN/biolink/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
GTPO = CurieNamespace('gtpo', 'http://example.org/UNKNOWN/gtpo/')
IGSNVOC = CurieNamespace('igsnvoc', 'https://igsn.org/voc/v1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MIXS = CurieNamespace('mixs', 'https://w3id.org/gensc/')
NMDC = CurieNamespace('nmdc', 'https://microbiomedata/meta/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
QUD = CurieNamespace('qud', 'http://qudt.org/1.1/schema/qudt#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
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


# Class references
class NamedThingId(extended_str):
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


# Enumerations


# Slots
class slots:
    pass

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
