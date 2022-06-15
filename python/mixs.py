# Auto generated from mixs.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-06-15T10:43:10
# Schema: mixs-schema
#
# id: https://microbiomedata/schema/mixs
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
MIXS = CurieNamespace('MIXS', 'https://w3id.org/gensc/')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
PR = CurieNamespace('PR', 'http://purl.obolibrary.org/obo/PR_')
PUBCHEM_COMPOUND = CurieNamespace('PUBCHEM_COMPOUND', 'http://identifiers.org/pubchem.compound/')
UNIPROTKB = CurieNamespace('UniProtKB', 'http://example.org/UNKNOWN/UniProtKB/')
BIOLINK = CurieNamespace('biolink', 'http://example.org/UNKNOWN/biolink/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
GTPO = CurieNamespace('gtpo', 'http://example.org/UNKNOWN/gtpo/')
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
DEFAULT_ = CurieNamespace('', 'https://microbiomedata/schema/mixs/')


# Types
class Bytes(int):
    """ An integer value that corresponds to a size in bytes """
    type_class_uri = XSD.int
    type_class_curie = "xsd:int"
    type_name = "bytes"
    type_model_uri = URIRef("https://microbiomedata/schema/mixs/Bytes")


class DecimalDegree(float):
    """ A decimal degree expresses latitude or longitude as decimal fractions. """
    type_class_uri = XSD.decimal
    type_class_curie = "xsd:decimal"
    type_name = "decimal degree"
    type_model_uri = URIRef("https://microbiomedata/schema/mixs/DecimalDegree")


class LanguageCode(str):
    """ A language code conforming to ISO_639-1 """
    type_class_uri = XSD.language
    type_class_curie = "xsd:language"
    type_name = "language code"
    type_model_uri = URIRef("https://microbiomedata/schema/mixs/LanguageCode")


class Unit(str):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "unit"
    type_model_uri = URIRef("https://microbiomedata/schema/mixs/Unit")


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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/mixs/NamedThing")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/mixs/OntologyClass")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/mixs/EnvironmentalMaterialTerm")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/mixs/AttributeValue")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/mixs/QuantityValue")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/mixs/ImageValue")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/mixs/PersonValue")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/mixs/Person")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/mixs/MAGBin")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/mixs/Instrument")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/mixs/MetaboliteQuantification")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/mixs/PeptideQuantification")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/mixs/ProteinQuantification")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/mixs/ChemicalEntity")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/mixs/GeneProduct")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/mixs/TextValue")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/mixs/UrlValue")


class TimestampValue(AttributeValue):
    """
    A value that is a timestamp. The range should be ISO-8601
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.TimestampValue
    class_class_curie: ClassVar[str] = "nmdc:TimestampValue"
    class_name: ClassVar[str] = "timestamp value"
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/mixs/TimestampValue")


@dataclass
class IntegerValue(AttributeValue):
    """
    A value that is an integer
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.IntegerValue
    class_class_curie: ClassVar[str] = "nmdc:IntegerValue"
    class_name: ClassVar[str] = "integer value"
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/mixs/IntegerValue")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/mixs/BooleanValue")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/mixs/ControlledTermValue")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/mixs/GeolocationValue")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/mixs/Activity")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/mixs/Agent")

    acted_on_behalf_of: Optional[Union[dict, "Agent"]] = None
    was_informed_by: Optional[Union[str, ActivityId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.acted_on_behalf_of is not None and not isinstance(self.acted_on_behalf_of, Agent):
            self.acted_on_behalf_of = Agent(**as_dict(self.acted_on_behalf_of))

        if self.was_informed_by is not None and not isinstance(self.was_informed_by, ActivityId):
            self.was_informed_by = ActivityId(self.was_informed_by)

        super().__post_init__(**kwargs)


# Enumerations
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

slots.abs_air_humidity = Slot(uri=MIXS['0000122'], name="abs_air_humidity", curie=MIXS.curie('0000122'),
                   model_uri=DEFAULT_.abs_air_humidity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.core_field = Slot(uri=DEFAULT_.core_field, name="core field", curie=DEFAULT_.curie('core_field'),
                   model_uri=DEFAULT_.core_field, domain=None, range=Optional[str])

slots.add_recov_method = Slot(uri=MIXS['0001009'], name="add_recov_method", curie=MIXS.curie('0001009'),
                   model_uri=DEFAULT_.add_recov_method, domain=None, range=Optional[Union[dict, TextValue]])

slots.additional_info = Slot(uri=MIXS['0000300'], name="additional_info", curie=MIXS.curie('0000300'),
                   model_uri=DEFAULT_.additional_info, domain=None, range=Optional[Union[dict, TextValue]])

slots.address = Slot(uri=MIXS['0000218'], name="address", curie=MIXS.curie('0000218'),
                   model_uri=DEFAULT_.address, domain=None, range=Optional[Union[dict, TextValue]])

slots.adj_room = Slot(uri=MIXS['0000219'], name="adj_room", curie=MIXS.curie('0000219'),
                   model_uri=DEFAULT_.adj_room, domain=None, range=Optional[Union[dict, TextValue]])

slots.aero_struc = Slot(uri=MIXS['0000773'], name="aero_struc", curie=MIXS.curie('0000773'),
                   model_uri=DEFAULT_.aero_struc, domain=None, range=Optional[Union[dict, TextValue]])

slots.agrochem_addition = Slot(uri=MIXS['0000639'], name="agrochem_addition", curie=MIXS.curie('0000639'),
                   model_uri=DEFAULT_.agrochem_addition, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.air_temp = Slot(uri=MIXS['0000124'], name="air_temp", curie=MIXS.curie('0000124'),
                   model_uri=DEFAULT_.air_temp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.air_temp_regm = Slot(uri=MIXS['0000551'], name="air_temp_regm", curie=MIXS.curie('0000551'),
                   model_uri=DEFAULT_.air_temp_regm, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.al_sat = Slot(uri=MIXS['0000607'], name="al_sat", curie=MIXS.curie('0000607'),
                   model_uri=DEFAULT_.al_sat, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.al_sat_meth = Slot(uri=MIXS['0000324'], name="al_sat_meth", curie=MIXS.curie('0000324'),
                   model_uri=DEFAULT_.al_sat_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.alkalinity = Slot(uri=MIXS['0000421'], name="alkalinity", curie=MIXS.curie('0000421'),
                   model_uri=DEFAULT_.alkalinity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.alkalinity_method = Slot(uri=MIXS['0000298'], name="alkalinity_method", curie=MIXS.curie('0000298'),
                   model_uri=DEFAULT_.alkalinity_method, domain=None, range=Optional[Union[dict, TextValue]])

slots.alkyl_diethers = Slot(uri=MIXS['0000490'], name="alkyl_diethers", curie=MIXS.curie('0000490'),
                   model_uri=DEFAULT_.alkyl_diethers, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.alt = Slot(uri=MIXS['0000094'], name="alt", curie=MIXS.curie('0000094'),
                   model_uri=DEFAULT_.alt, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.environment_field = Slot(uri=DEFAULT_.environment_field, name="environment field", curie=DEFAULT_.curie('environment_field'),
                   model_uri=DEFAULT_.environment_field, domain=None, range=Optional[str])

slots.aminopept_act = Slot(uri=MIXS['0000172'], name="aminopept_act", curie=MIXS.curie('0000172'),
                   model_uri=DEFAULT_.aminopept_act, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.ammonium = Slot(uri=MIXS['0000427'], name="ammonium", curie=MIXS.curie('0000427'),
                   model_uri=DEFAULT_.ammonium, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.amount_light = Slot(uri=MIXS['0000140'], name="amount_light", curie=MIXS.curie('0000140'),
                   model_uri=DEFAULT_.amount_light, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.ances_data = Slot(uri=MIXS['0000247'], name="ances_data", curie=MIXS.curie('0000247'),
                   model_uri=DEFAULT_.ances_data, domain=None, range=Optional[Union[dict, TextValue]])

slots.annual_precpt = Slot(uri=MIXS['0000644'], name="annual_precpt", curie=MIXS.curie('0000644'),
                   model_uri=DEFAULT_.annual_precpt, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.annual_temp = Slot(uri=MIXS['0000642'], name="annual_temp", curie=MIXS.curie('0000642'),
                   model_uri=DEFAULT_.annual_temp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.antibiotic_regm = Slot(uri=MIXS['0000553'], name="antibiotic_regm", curie=MIXS.curie('0000553'),
                   model_uri=DEFAULT_.antibiotic_regm, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.api = Slot(uri=MIXS['0000157'], name="api", curie=MIXS.curie('0000157'),
                   model_uri=DEFAULT_.api, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.arch_struc = Slot(uri=MIXS['0000774'], name="arch_struc", curie=MIXS.curie('0000774'),
                   model_uri=DEFAULT_.arch_struc, domain=None, range=Optional[Union[dict, TextValue]])

slots.aromatics_pc = Slot(uri=MIXS['0000133'], name="aromatics_pc", curie=MIXS.curie('0000133'),
                   model_uri=DEFAULT_.aromatics_pc, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.asphaltenes_pc = Slot(uri=MIXS['0000135'], name="asphaltenes_pc", curie=MIXS.curie('0000135'),
                   model_uri=DEFAULT_.asphaltenes_pc, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.atmospheric_data = Slot(uri=MIXS['0001097'], name="atmospheric_data", curie=MIXS.curie('0001097'),
                   model_uri=DEFAULT_.atmospheric_data, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.avg_dew_point = Slot(uri=MIXS['0000141'], name="avg_dew_point", curie=MIXS.curie('0000141'),
                   model_uri=DEFAULT_.avg_dew_point, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.avg_occup = Slot(uri=MIXS['0000775'], name="avg_occup", curie=MIXS.curie('0000775'),
                   model_uri=DEFAULT_.avg_occup, domain=None, range=Optional[Union[dict, TextValue]])

slots.avg_temp = Slot(uri=MIXS['0000142'], name="avg_temp", curie=MIXS.curie('0000142'),
                   model_uri=DEFAULT_.avg_temp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.bac_prod = Slot(uri=MIXS['0000683'], name="bac_prod", curie=MIXS.curie('0000683'),
                   model_uri=DEFAULT_.bac_prod, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.bac_resp = Slot(uri=MIXS['0000684'], name="bac_resp", curie=MIXS.curie('0000684'),
                   model_uri=DEFAULT_.bac_resp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.bacteria_carb_prod = Slot(uri=MIXS['0000173'], name="bacteria_carb_prod", curie=MIXS.curie('0000173'),
                   model_uri=DEFAULT_.bacteria_carb_prod, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.barometric_press = Slot(uri=MIXS['0000096'], name="barometric_press", curie=MIXS.curie('0000096'),
                   model_uri=DEFAULT_.barometric_press, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.basin = Slot(uri=MIXS['0000290'], name="basin", curie=MIXS.curie('0000290'),
                   model_uri=DEFAULT_.basin, domain=None, range=Optional[Union[dict, TextValue]])

slots.bathroom_count = Slot(uri=MIXS['0000776'], name="bathroom_count", curie=MIXS.curie('0000776'),
                   model_uri=DEFAULT_.bathroom_count, domain=None, range=Optional[Union[dict, TextValue]])

slots.bedroom_count = Slot(uri=MIXS['0000777'], name="bedroom_count", curie=MIXS.curie('0000777'),
                   model_uri=DEFAULT_.bedroom_count, domain=None, range=Optional[Union[dict, TextValue]])

slots.benzene = Slot(uri=MIXS['0000153'], name="benzene", curie=MIXS.curie('0000153'),
                   model_uri=DEFAULT_.benzene, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.biochem_oxygen_dem = Slot(uri=MIXS['0000653'], name="biochem_oxygen_dem", curie=MIXS.curie('0000653'),
                   model_uri=DEFAULT_.biochem_oxygen_dem, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.biocide = Slot(uri=MIXS['0001011'], name="biocide", curie=MIXS.curie('0001011'),
                   model_uri=DEFAULT_.biocide, domain=None, range=Optional[Union[dict, TextValue]])

slots.biocide_admin_method = Slot(uri=MIXS['0000456'], name="biocide_admin_method", curie=MIXS.curie('0000456'),
                   model_uri=DEFAULT_.biocide_admin_method, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.biol_stat = Slot(uri=MIXS['0000858'], name="biol_stat", curie=MIXS.curie('0000858'),
                   model_uri=DEFAULT_.biol_stat, domain=None, range=Optional[Union[dict, TextValue]])

slots.biomass = Slot(uri=MIXS['0000174'], name="biomass", curie=MIXS.curie('0000174'),
                   model_uri=DEFAULT_.biomass, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.biotic_regm = Slot(uri=MIXS['0001038'], name="biotic_regm", curie=MIXS.curie('0001038'),
                   model_uri=DEFAULT_.biotic_regm, domain=None, range=Optional[Union[dict, TextValue]])

slots.biotic_relationship = Slot(uri=MIXS['0000028'], name="biotic_relationship", curie=MIXS.curie('0000028'),
                   model_uri=DEFAULT_.biotic_relationship, domain=None, range=Optional[Union[dict, TextValue]])

slots.nucleic_acid_sequence_source_field = Slot(uri=DEFAULT_.nucleic_acid_sequence_source_field, name="nucleic acid sequence source field", curie=DEFAULT_.curie('nucleic_acid_sequence_source_field'),
                   model_uri=DEFAULT_.nucleic_acid_sequence_source_field, domain=None, range=Optional[str])

slots.bishomohopanol = Slot(uri=MIXS['0000175'], name="bishomohopanol", curie=MIXS.curie('0000175'),
                   model_uri=DEFAULT_.bishomohopanol, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.blood_press_diast = Slot(uri=MIXS['0000258'], name="blood_press_diast", curie=MIXS.curie('0000258'),
                   model_uri=DEFAULT_.blood_press_diast, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.blood_press_syst = Slot(uri=MIXS['0000259'], name="blood_press_syst", curie=MIXS.curie('0000259'),
                   model_uri=DEFAULT_.blood_press_syst, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.bromide = Slot(uri=MIXS['0000176'], name="bromide", curie=MIXS.curie('0000176'),
                   model_uri=DEFAULT_.bromide, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.build_docs = Slot(uri=MIXS['0000787'], name="build_docs", curie=MIXS.curie('0000787'),
                   model_uri=DEFAULT_.build_docs, domain=None, range=Optional[Union[dict, TextValue]])

slots.build_occup_type = Slot(uri=MIXS['0000761'], name="build_occup_type", curie=MIXS.curie('0000761'),
                   model_uri=DEFAULT_.build_occup_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.building_setting = Slot(uri=MIXS['0000768'], name="building_setting", curie=MIXS.curie('0000768'),
                   model_uri=DEFAULT_.building_setting, domain=None, range=Optional[Union[dict, TextValue]])

slots.built_struc_age = Slot(uri=MIXS['0000145'], name="built_struc_age", curie=MIXS.curie('0000145'),
                   model_uri=DEFAULT_.built_struc_age, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.built_struc_set = Slot(uri=MIXS['0000778'], name="built_struc_set", curie=MIXS.curie('0000778'),
                   model_uri=DEFAULT_.built_struc_set, domain=None, range=Optional[Union[dict, TextValue]])

slots.built_struc_type = Slot(uri=MIXS['0000721'], name="built_struc_type", curie=MIXS.curie('0000721'),
                   model_uri=DEFAULT_.built_struc_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.calcium = Slot(uri=MIXS['0000432'], name="calcium", curie=MIXS.curie('0000432'),
                   model_uri=DEFAULT_.calcium, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.carb_dioxide = Slot(uri=MIXS['0000097'], name="carb_dioxide", curie=MIXS.curie('0000097'),
                   model_uri=DEFAULT_.carb_dioxide, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.carb_monoxide = Slot(uri=MIXS['0000098'], name="carb_monoxide", curie=MIXS.curie('0000098'),
                   model_uri=DEFAULT_.carb_monoxide, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.carb_nitro_ratio = Slot(uri=MIXS['0000310'], name="carb_nitro_ratio", curie=MIXS.curie('0000310'),
                   model_uri=DEFAULT_.carb_nitro_ratio, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.ceil_area = Slot(uri=MIXS['0000148'], name="ceil_area", curie=MIXS.curie('0000148'),
                   model_uri=DEFAULT_.ceil_area, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.ceil_cond = Slot(uri=MIXS['0000779'], name="ceil_cond", curie=MIXS.curie('0000779'),
                   model_uri=DEFAULT_.ceil_cond, domain=None, range=Optional[Union[dict, TextValue]])

slots.ceil_finish_mat = Slot(uri=MIXS['0000780'], name="ceil_finish_mat", curie=MIXS.curie('0000780'),
                   model_uri=DEFAULT_.ceil_finish_mat, domain=None, range=Optional[Union[dict, TextValue]])

slots.ceil_struc = Slot(uri=MIXS['0000782'], name="ceil_struc", curie=MIXS.curie('0000782'),
                   model_uri=DEFAULT_.ceil_struc, domain=None, range=Optional[Union[dict, TextValue]])

slots.ceil_texture = Slot(uri=MIXS['0000783'], name="ceil_texture", curie=MIXS.curie('0000783'),
                   model_uri=DEFAULT_.ceil_texture, domain=None, range=Optional[Union[dict, TextValue]])

slots.ceil_thermal_mass = Slot(uri=MIXS['0000143'], name="ceil_thermal_mass", curie=MIXS.curie('0000143'),
                   model_uri=DEFAULT_.ceil_thermal_mass, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.ceil_type = Slot(uri=MIXS['0000784'], name="ceil_type", curie=MIXS.curie('0000784'),
                   model_uri=DEFAULT_.ceil_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.ceil_water_mold = Slot(uri=MIXS['0000781'], name="ceil_water_mold", curie=MIXS.curie('0000781'),
                   model_uri=DEFAULT_.ceil_water_mold, domain=None, range=Optional[Union[dict, TextValue]])

slots.chem_administration = Slot(uri=MIXS['0000751'], name="chem_administration", curie=MIXS.curie('0000751'),
                   model_uri=DEFAULT_.chem_administration, domain=None, range=Optional[Union[dict, ControlledTermValue]])

slots.chem_mutagen = Slot(uri=MIXS['0000555'], name="chem_mutagen", curie=MIXS.curie('0000555'),
                   model_uri=DEFAULT_.chem_mutagen, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.chem_oxygen_dem = Slot(uri=MIXS['0000656'], name="chem_oxygen_dem", curie=MIXS.curie('0000656'),
                   model_uri=DEFAULT_.chem_oxygen_dem, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.chem_treat_method = Slot(uri=MIXS['0000457'], name="chem_treat_method", curie=MIXS.curie('0000457'),
                   model_uri=DEFAULT_.chem_treat_method, domain=None, range=Optional[str])

slots.chem_treatment = Slot(uri=MIXS['0001012'], name="chem_treatment", curie=MIXS.curie('0001012'),
                   model_uri=DEFAULT_.chem_treatment, domain=None, range=Optional[Union[dict, TextValue]])

slots.chimera_check = Slot(uri=MIXS['0000052'], name="chimera_check", curie=MIXS.curie('0000052'),
                   model_uri=DEFAULT_.chimera_check, domain=None, range=Optional[Union[dict, TextValue]])

slots.sequencing_field = Slot(uri=DEFAULT_.sequencing_field, name="sequencing field", curie=DEFAULT_.curie('sequencing_field'),
                   model_uri=DEFAULT_.sequencing_field, domain=None, range=Optional[str])

slots.chloride = Slot(uri=MIXS['0000429'], name="chloride", curie=MIXS.curie('0000429'),
                   model_uri=DEFAULT_.chloride, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.chlorophyll = Slot(uri=MIXS['0000177'], name="chlorophyll", curie=MIXS.curie('0000177'),
                   model_uri=DEFAULT_.chlorophyll, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.climate_environment = Slot(uri=MIXS['0001040'], name="climate_environment", curie=MIXS.curie('0001040'),
                   model_uri=DEFAULT_.climate_environment, domain=None, range=Optional[Union[dict, TextValue]])

slots.collection_date = Slot(uri=MIXS['0000011'], name="collection_date", curie=MIXS.curie('0000011'),
                   model_uri=DEFAULT_.collection_date, domain=None, range=Optional[Union[dict, TimestampValue]])

slots.conduc = Slot(uri=MIXS['0000692'], name="conduc", curie=MIXS.curie('0000692'),
                   model_uri=DEFAULT_.conduc, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cool_syst_id = Slot(uri=MIXS['0000785'], name="cool_syst_id", curie=MIXS.curie('0000785'),
                   model_uri=DEFAULT_.cool_syst_id, domain=None, range=Optional[Union[dict, TextValue]])

slots.crop_rotation = Slot(uri=MIXS['0000318'], name="crop_rotation", curie=MIXS.curie('0000318'),
                   model_uri=DEFAULT_.crop_rotation, domain=None, range=Optional[Union[dict, TextValue]])

slots.cult_root_med = Slot(uri=MIXS['0001041'], name="cult_root_med", curie=MIXS.curie('0001041'),
                   model_uri=DEFAULT_.cult_root_med, domain=None, range=Optional[Union[dict, TextValue]])

slots.cur_land_use = Slot(uri=MIXS['0001080'], name="cur_land_use", curie=MIXS.curie('0001080'),
                   model_uri=DEFAULT_.cur_land_use, domain=None, range=Optional[Union[dict, TextValue]])

slots.cur_vegetation = Slot(uri=MIXS['0000312'], name="cur_vegetation", curie=MIXS.curie('0000312'),
                   model_uri=DEFAULT_.cur_vegetation, domain=None, range=Optional[Union[dict, TextValue]])

slots.cur_vegetation_meth = Slot(uri=MIXS['0000314'], name="cur_vegetation_meth", curie=MIXS.curie('0000314'),
                   model_uri=DEFAULT_.cur_vegetation_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.date_last_rain = Slot(uri=MIXS['0000786'], name="date_last_rain", curie=MIXS.curie('0000786'),
                   model_uri=DEFAULT_.date_last_rain, domain=None, range=Optional[Union[dict, TimestampValue]])

slots.density = Slot(uri=MIXS['0000435'], name="density", curie=MIXS.curie('0000435'),
                   model_uri=DEFAULT_.density, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.depos_env = Slot(uri=MIXS['0000992'], name="depos_env", curie=MIXS.curie('0000992'),
                   model_uri=DEFAULT_.depos_env, domain=None, range=Optional[Union[dict, TextValue]])

slots.depth = Slot(uri=MIXS['0000018'], name="depth", curie=MIXS.curie('0000018'),
                   model_uri=DEFAULT_.depth, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.dew_point = Slot(uri=MIXS['0000129'], name="dew_point", curie=MIXS.curie('0000129'),
                   model_uri=DEFAULT_.dew_point, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.diether_lipids = Slot(uri=MIXS['0000178'], name="diether_lipids", curie=MIXS.curie('0000178'),
                   model_uri=DEFAULT_.diether_lipids, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.diss_carb_dioxide = Slot(uri=MIXS['0000436'], name="diss_carb_dioxide", curie=MIXS.curie('0000436'),
                   model_uri=DEFAULT_.diss_carb_dioxide, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.diss_hydrogen = Slot(uri=MIXS['0000179'], name="diss_hydrogen", curie=MIXS.curie('0000179'),
                   model_uri=DEFAULT_.diss_hydrogen, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.diss_inorg_carb = Slot(uri=MIXS['0000434'], name="diss_inorg_carb", curie=MIXS.curie('0000434'),
                   model_uri=DEFAULT_.diss_inorg_carb, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.diss_inorg_nitro = Slot(uri=MIXS['0000698'], name="diss_inorg_nitro", curie=MIXS.curie('0000698'),
                   model_uri=DEFAULT_.diss_inorg_nitro, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.diss_inorg_phosp = Slot(uri=MIXS['0000106'], name="diss_inorg_phosp", curie=MIXS.curie('0000106'),
                   model_uri=DEFAULT_.diss_inorg_phosp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.diss_iron = Slot(uri=MIXS['0000139'], name="diss_iron", curie=MIXS.curie('0000139'),
                   model_uri=DEFAULT_.diss_iron, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.diss_org_carb = Slot(uri=MIXS['0000433'], name="diss_org_carb", curie=MIXS.curie('0000433'),
                   model_uri=DEFAULT_.diss_org_carb, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.diss_org_nitro = Slot(uri=MIXS['0000162'], name="diss_org_nitro", curie=MIXS.curie('0000162'),
                   model_uri=DEFAULT_.diss_org_nitro, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.diss_oxygen = Slot(uri=MIXS['0000119'], name="diss_oxygen", curie=MIXS.curie('0000119'),
                   model_uri=DEFAULT_.diss_oxygen, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.diss_oxygen_fluid = Slot(uri=MIXS['0000438'], name="diss_oxygen_fluid", curie=MIXS.curie('0000438'),
                   model_uri=DEFAULT_.diss_oxygen_fluid, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.door_comp_type = Slot(uri=MIXS['0000795'], name="door_comp_type", curie=MIXS.curie('0000795'),
                   model_uri=DEFAULT_.door_comp_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.door_cond = Slot(uri=MIXS['0000788'], name="door_cond", curie=MIXS.curie('0000788'),
                   model_uri=DEFAULT_.door_cond, domain=None, range=Optional[Union[dict, TextValue]])

slots.door_direct = Slot(uri=MIXS['0000789'], name="door_direct", curie=MIXS.curie('0000789'),
                   model_uri=DEFAULT_.door_direct, domain=None, range=Optional[Union[dict, TextValue]])

slots.door_loc = Slot(uri=MIXS['0000790'], name="door_loc", curie=MIXS.curie('0000790'),
                   model_uri=DEFAULT_.door_loc, domain=None, range=Optional[Union[dict, TextValue]])

slots.door_mat = Slot(uri=MIXS['0000791'], name="door_mat", curie=MIXS.curie('0000791'),
                   model_uri=DEFAULT_.door_mat, domain=None, range=Optional[Union[dict, TextValue]])

slots.door_move = Slot(uri=MIXS['0000792'], name="door_move", curie=MIXS.curie('0000792'),
                   model_uri=DEFAULT_.door_move, domain=None, range=Optional[Union[dict, TextValue]])

slots.door_size = Slot(uri=MIXS['0000158'], name="door_size", curie=MIXS.curie('0000158'),
                   model_uri=DEFAULT_.door_size, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.door_type = Slot(uri=MIXS['0000794'], name="door_type", curie=MIXS.curie('0000794'),
                   model_uri=DEFAULT_.door_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.door_type_metal = Slot(uri=MIXS['0000796'], name="door_type_metal", curie=MIXS.curie('0000796'),
                   model_uri=DEFAULT_.door_type_metal, domain=None, range=Optional[Union[dict, TextValue]])

slots.door_type_wood = Slot(uri=MIXS['0000797'], name="door_type_wood", curie=MIXS.curie('0000797'),
                   model_uri=DEFAULT_.door_type_wood, domain=None, range=Optional[Union[dict, TextValue]])

slots.door_water_mold = Slot(uri=MIXS['0000793'], name="door_water_mold", curie=MIXS.curie('0000793'),
                   model_uri=DEFAULT_.door_water_mold, domain=None, range=Optional[Union[dict, TextValue]])

slots.down_par = Slot(uri=MIXS['0000703'], name="down_par", curie=MIXS.curie('0000703'),
                   model_uri=DEFAULT_.down_par, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.drainage_class = Slot(uri=MIXS['0001085'], name="drainage_class", curie=MIXS.curie('0001085'),
                   model_uri=DEFAULT_.drainage_class, domain=None, range=Optional[Union[dict, TextValue]])

slots.drawings = Slot(uri=MIXS['0000798'], name="drawings", curie=MIXS.curie('0000798'),
                   model_uri=DEFAULT_.drawings, domain=None, range=Optional[Union[dict, TextValue]])

slots.efficiency_percent = Slot(uri=MIXS['0000657'], name="efficiency_percent", curie=MIXS.curie('0000657'),
                   model_uri=DEFAULT_.efficiency_percent, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.elev = Slot(uri=MIXS['0000093'], name="elev", curie=MIXS.curie('0000093'),
                   model_uri=DEFAULT_.elev, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.elevator = Slot(uri=MIXS['0000799'], name="elevator", curie=MIXS.curie('0000799'),
                   model_uri=DEFAULT_.elevator, domain=None, range=Optional[Union[dict, TextValue]])

slots.emulsions = Slot(uri=MIXS['0000660'], name="emulsions", curie=MIXS.curie('0000660'),
                   model_uri=DEFAULT_.emulsions, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.env_broad_scale = Slot(uri=MIXS['0000012'], name="env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=DEFAULT_.env_broad_scale, domain=None, range=Optional[Union[dict, ControlledTermValue]])

slots.env_local_scale = Slot(uri=MIXS['0000013'], name="env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=DEFAULT_.env_local_scale, domain=None, range=Optional[Union[dict, ControlledTermValue]])

slots.env_medium = Slot(uri=MIXS['0000014'], name="env_medium", curie=MIXS.curie('0000014'),
                   model_uri=DEFAULT_.env_medium, domain=None, range=Optional[Union[dict, ControlledTermValue]])

slots.escalator = Slot(uri=MIXS['0000800'], name="escalator", curie=MIXS.curie('0000800'),
                   model_uri=DEFAULT_.escalator, domain=None, range=Optional[Union[dict, TextValue]])

slots.ethylbenzene = Slot(uri=MIXS['0000155'], name="ethylbenzene", curie=MIXS.curie('0000155'),
                   model_uri=DEFAULT_.ethylbenzene, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.exp_duct = Slot(uri=MIXS['0000144'], name="exp_duct", curie=MIXS.curie('0000144'),
                   model_uri=DEFAULT_.exp_duct, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.exp_pipe = Slot(uri=MIXS['0000220'], name="exp_pipe", curie=MIXS.curie('0000220'),
                   model_uri=DEFAULT_.exp_pipe, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimental_factor = Slot(uri=MIXS['0000008'], name="experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=DEFAULT_.experimental_factor, domain=None, range=Optional[Union[dict, ControlledTermValue]])

slots.investigation_field = Slot(uri=DEFAULT_.investigation_field, name="investigation field", curie=DEFAULT_.curie('investigation_field'),
                   model_uri=DEFAULT_.investigation_field, domain=None, range=Optional[str])

slots.ext_door = Slot(uri=MIXS['0000170'], name="ext_door", curie=MIXS.curie('0000170'),
                   model_uri=DEFAULT_.ext_door, domain=None, range=Optional[Union[dict, TextValue]])

slots.ext_wall_orient = Slot(uri=MIXS['0000817'], name="ext_wall_orient", curie=MIXS.curie('0000817'),
                   model_uri=DEFAULT_.ext_wall_orient, domain=None, range=Optional[Union[dict, TextValue]])

slots.ext_window_orient = Slot(uri=MIXS['0000818'], name="ext_window_orient", curie=MIXS.curie('0000818'),
                   model_uri=DEFAULT_.ext_window_orient, domain=None, range=Optional[Union[dict, TextValue]])

slots.extreme_event = Slot(uri=MIXS['0000320'], name="extreme_event", curie=MIXS.curie('0000320'),
                   model_uri=DEFAULT_.extreme_event, domain=None, range=Optional[Union[dict, TimestampValue]])

slots.fao_class = Slot(uri=MIXS['0001083'], name="fao_class", curie=MIXS.curie('0001083'),
                   model_uri=DEFAULT_.fao_class, domain=None, range=Optional[Union[dict, TextValue]])

slots.fertilizer_regm = Slot(uri=MIXS['0000556'], name="fertilizer_regm", curie=MIXS.curie('0000556'),
                   model_uri=DEFAULT_.fertilizer_regm, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.field = Slot(uri=MIXS['0000291'], name="field", curie=MIXS.curie('0000291'),
                   model_uri=DEFAULT_.field, domain=None, range=Optional[Union[dict, TextValue]])

slots.filter_type = Slot(uri=MIXS['0000765'], name="filter_type", curie=MIXS.curie('0000765'),
                   model_uri=DEFAULT_.filter_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.fire = Slot(uri=MIXS['0001086'], name="fire", curie=MIXS.curie('0001086'),
                   model_uri=DEFAULT_.fire, domain=None, range=Optional[Union[dict, TimestampValue]])

slots.fireplace_type = Slot(uri=MIXS['0000802'], name="fireplace_type", curie=MIXS.curie('0000802'),
                   model_uri=DEFAULT_.fireplace_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.flooding = Slot(uri=MIXS['0000319'], name="flooding", curie=MIXS.curie('0000319'),
                   model_uri=DEFAULT_.flooding, domain=None, range=Optional[Union[dict, TimestampValue]])

slots.floor_age = Slot(uri=MIXS['0000164'], name="floor_age", curie=MIXS.curie('0000164'),
                   model_uri=DEFAULT_.floor_age, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.floor_area = Slot(uri=MIXS['0000165'], name="floor_area", curie=MIXS.curie('0000165'),
                   model_uri=DEFAULT_.floor_area, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.floor_cond = Slot(uri=MIXS['0000803'], name="floor_cond", curie=MIXS.curie('0000803'),
                   model_uri=DEFAULT_.floor_cond, domain=None, range=Optional[Union[dict, TextValue]])

slots.floor_count = Slot(uri=MIXS['0000225'], name="floor_count", curie=MIXS.curie('0000225'),
                   model_uri=DEFAULT_.floor_count, domain=None, range=Optional[Union[dict, TextValue]])

slots.floor_finish_mat = Slot(uri=MIXS['0000804'], name="floor_finish_mat", curie=MIXS.curie('0000804'),
                   model_uri=DEFAULT_.floor_finish_mat, domain=None, range=Optional[Union[dict, TextValue]])

slots.floor_struc = Slot(uri=MIXS['0000806'], name="floor_struc", curie=MIXS.curie('0000806'),
                   model_uri=DEFAULT_.floor_struc, domain=None, range=Optional[Union[dict, TextValue]])

slots.floor_thermal_mass = Slot(uri=MIXS['0000166'], name="floor_thermal_mass", curie=MIXS.curie('0000166'),
                   model_uri=DEFAULT_.floor_thermal_mass, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.floor_water_mold = Slot(uri=MIXS['0000805'], name="floor_water_mold", curie=MIXS.curie('0000805'),
                   model_uri=DEFAULT_.floor_water_mold, domain=None, range=Optional[Union[dict, TextValue]])

slots.fluor = Slot(uri=MIXS['0000704'], name="fluor", curie=MIXS.curie('0000704'),
                   model_uri=DEFAULT_.fluor, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.freq_clean = Slot(uri=MIXS['0000226'], name="freq_clean", curie=MIXS.curie('0000226'),
                   model_uri=DEFAULT_.freq_clean, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.freq_cook = Slot(uri=MIXS['0000227'], name="freq_cook", curie=MIXS.curie('0000227'),
                   model_uri=DEFAULT_.freq_cook, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.fungicide_regm = Slot(uri=MIXS['0000557'], name="fungicide_regm", curie=MIXS.curie('0000557'),
                   model_uri=DEFAULT_.fungicide_regm, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.furniture = Slot(uri=MIXS['0000807'], name="furniture", curie=MIXS.curie('0000807'),
                   model_uri=DEFAULT_.furniture, domain=None, range=Optional[Union[dict, TextValue]])

slots.gaseous_environment = Slot(uri=MIXS['0000558'], name="gaseous_environment", curie=MIXS.curie('0000558'),
                   model_uri=DEFAULT_.gaseous_environment, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.gaseous_substances = Slot(uri=MIXS['0000661'], name="gaseous_substances", curie=MIXS.curie('0000661'),
                   model_uri=DEFAULT_.gaseous_substances, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.gender_restroom = Slot(uri=MIXS['0000808'], name="gender_restroom", curie=MIXS.curie('0000808'),
                   model_uri=DEFAULT_.gender_restroom, domain=None, range=Optional[Union[dict, TextValue]])

slots.genetic_mod = Slot(uri=MIXS['0000859'], name="genetic_mod", curie=MIXS.curie('0000859'),
                   model_uri=DEFAULT_.genetic_mod, domain=None, range=Optional[Union[dict, TextValue]])

slots.geo_loc_name = Slot(uri=MIXS['0000010'], name="geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=DEFAULT_.geo_loc_name, domain=None, range=Optional[Union[dict, TextValue]])

slots.glucosidase_act = Slot(uri=MIXS['0000137'], name="glucosidase_act", curie=MIXS.curie('0000137'),
                   model_uri=DEFAULT_.glucosidase_act, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.gravidity = Slot(uri=MIXS['0000875'], name="gravidity", curie=MIXS.curie('0000875'),
                   model_uri=DEFAULT_.gravidity, domain=None, range=Optional[Union[dict, TextValue]])

slots.gravity = Slot(uri=MIXS['0000559'], name="gravity", curie=MIXS.curie('0000559'),
                   model_uri=DEFAULT_.gravity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.growth_facil = Slot(uri=MIXS['0001043'], name="growth_facil", curie=MIXS.curie('0001043'),
                   model_uri=DEFAULT_.growth_facil, domain=None, range=Optional[Union[dict, ControlledTermValue]])

slots.growth_habit = Slot(uri=MIXS['0001044'], name="growth_habit", curie=MIXS.curie('0001044'),
                   model_uri=DEFAULT_.growth_habit, domain=None, range=Optional[Union[dict, TextValue]])

slots.growth_hormone_regm = Slot(uri=MIXS['0000560'], name="growth_hormone_regm", curie=MIXS.curie('0000560'),
                   model_uri=DEFAULT_.growth_hormone_regm, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.hall_count = Slot(uri=MIXS['0000228'], name="hall_count", curie=MIXS.curie('0000228'),
                   model_uri=DEFAULT_.hall_count, domain=None, range=Optional[Union[dict, TextValue]])

slots.handidness = Slot(uri=MIXS['0000809'], name="handidness", curie=MIXS.curie('0000809'),
                   model_uri=DEFAULT_.handidness, domain=None, range=Optional[Union[dict, TextValue]])

slots.hc_produced = Slot(uri=MIXS['0000989'], name="hc_produced", curie=MIXS.curie('0000989'),
                   model_uri=DEFAULT_.hc_produced, domain=None, range=Optional[Union[dict, TextValue]])

slots.hcr = Slot(uri=MIXS['0000988'], name="hcr", curie=MIXS.curie('0000988'),
                   model_uri=DEFAULT_.hcr, domain=None, range=Optional[Union[dict, TextValue]])

slots.hcr_fw_salinity = Slot(uri=MIXS['0000406'], name="hcr_fw_salinity", curie=MIXS.curie('0000406'),
                   model_uri=DEFAULT_.hcr_fw_salinity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.hcr_geol_age = Slot(uri=MIXS['0000993'], name="hcr_geol_age", curie=MIXS.curie('0000993'),
                   model_uri=DEFAULT_.hcr_geol_age, domain=None, range=Optional[Union[dict, TextValue]])

slots.hcr_pressure = Slot(uri=MIXS['0000395'], name="hcr_pressure", curie=MIXS.curie('0000395'),
                   model_uri=DEFAULT_.hcr_pressure, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.hcr_temp = Slot(uri=MIXS['0000393'], name="hcr_temp", curie=MIXS.curie('0000393'),
                   model_uri=DEFAULT_.hcr_temp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.heat_cool_type = Slot(uri=MIXS['0000766'], name="heat_cool_type", curie=MIXS.curie('0000766'),
                   model_uri=DEFAULT_.heat_cool_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.heat_deliv_loc = Slot(uri=MIXS['0000810'], name="heat_deliv_loc", curie=MIXS.curie('0000810'),
                   model_uri=DEFAULT_.heat_deliv_loc, domain=None, range=Optional[Union[dict, TextValue]])

slots.heat_sys_deliv_meth = Slot(uri=MIXS['0000812'], name="heat_sys_deliv_meth", curie=MIXS.curie('0000812'),
                   model_uri=DEFAULT_.heat_sys_deliv_meth, domain=None, range=Optional[str])

slots.heat_system_id = Slot(uri=MIXS['0000833'], name="heat_system_id", curie=MIXS.curie('0000833'),
                   model_uri=DEFAULT_.heat_system_id, domain=None, range=Optional[Union[dict, TextValue]])

slots.heavy_metals = Slot(uri=MIXS['0000652'], name="heavy_metals", curie=MIXS.curie('0000652'),
                   model_uri=DEFAULT_.heavy_metals, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.heavy_metals_meth = Slot(uri=MIXS['0000343'], name="heavy_metals_meth", curie=MIXS.curie('0000343'),
                   model_uri=DEFAULT_.heavy_metals_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.height_carper_fiber = Slot(uri=MIXS['0000167'], name="height_carper_fiber", curie=MIXS.curie('0000167'),
                   model_uri=DEFAULT_.height_carper_fiber, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.herbicide_regm = Slot(uri=MIXS['0000561'], name="herbicide_regm", curie=MIXS.curie('0000561'),
                   model_uri=DEFAULT_.herbicide_regm, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.horizon = Slot(uri=MIXS['0001082'], name="horizon", curie=MIXS.curie('0001082'),
                   model_uri=DEFAULT_.horizon, domain=None, range=Optional[Union[dict, TextValue]])

slots.horizon_meth = Slot(uri=MIXS['0000321'], name="horizon_meth", curie=MIXS.curie('0000321'),
                   model_uri=DEFAULT_.horizon_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.host_age = Slot(uri=MIXS['0000255'], name="host_age", curie=MIXS.curie('0000255'),
                   model_uri=DEFAULT_.host_age, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.host_body_habitat = Slot(uri=MIXS['0000866'], name="host_body_habitat", curie=MIXS.curie('0000866'),
                   model_uri=DEFAULT_.host_body_habitat, domain=None, range=Optional[Union[dict, TextValue]])

slots.host_body_product = Slot(uri=MIXS['0000888'], name="host_body_product", curie=MIXS.curie('0000888'),
                   model_uri=DEFAULT_.host_body_product, domain=None, range=Optional[Union[dict, ControlledTermValue]])

slots.host_body_site = Slot(uri=MIXS['0000867'], name="host_body_site", curie=MIXS.curie('0000867'),
                   model_uri=DEFAULT_.host_body_site, domain=None, range=Optional[Union[dict, ControlledTermValue]])

slots.host_body_temp = Slot(uri=MIXS['0000274'], name="host_body_temp", curie=MIXS.curie('0000274'),
                   model_uri=DEFAULT_.host_body_temp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.host_color = Slot(uri=MIXS['0000260'], name="host_color", curie=MIXS.curie('0000260'),
                   model_uri=DEFAULT_.host_color, domain=None, range=Optional[Union[dict, TextValue]])

slots.host_common_name = Slot(uri=MIXS['0000248'], name="host_common_name", curie=MIXS.curie('0000248'),
                   model_uri=DEFAULT_.host_common_name, domain=None, range=Optional[Union[dict, TextValue]])

slots.host_diet = Slot(uri=MIXS['0000869'], name="host_diet", curie=MIXS.curie('0000869'),
                   model_uri=DEFAULT_.host_diet, domain=None, range=Optional[Union[dict, TextValue]])

slots.host_dry_mass = Slot(uri=MIXS['0000257'], name="host_dry_mass", curie=MIXS.curie('0000257'),
                   model_uri=DEFAULT_.host_dry_mass, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.host_family_relation = Slot(uri=MIXS['0000872'], name="host_family_relation", curie=MIXS.curie('0000872'),
                   model_uri=DEFAULT_.host_family_relation, domain=None, range=Optional[Union[str, List[str]]])

slots.host_genotype = Slot(uri=MIXS['0000365'], name="host_genotype", curie=MIXS.curie('0000365'),
                   model_uri=DEFAULT_.host_genotype, domain=None, range=Optional[Union[dict, TextValue]])

slots.host_growth_cond = Slot(uri=MIXS['0000871'], name="host_growth_cond", curie=MIXS.curie('0000871'),
                   model_uri=DEFAULT_.host_growth_cond, domain=None, range=Optional[Union[dict, TextValue]])

slots.host_height = Slot(uri=MIXS['0000264'], name="host_height", curie=MIXS.curie('0000264'),
                   model_uri=DEFAULT_.host_height, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.host_last_meal = Slot(uri=MIXS['0000870'], name="host_last_meal", curie=MIXS.curie('0000870'),
                   model_uri=DEFAULT_.host_last_meal, domain=None, range=Optional[Union[dict, TextValue]])

slots.host_length = Slot(uri=MIXS['0000256'], name="host_length", curie=MIXS.curie('0000256'),
                   model_uri=DEFAULT_.host_length, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.host_life_stage = Slot(uri=MIXS['0000251'], name="host_life_stage", curie=MIXS.curie('0000251'),
                   model_uri=DEFAULT_.host_life_stage, domain=None, range=Optional[Union[dict, TextValue]])

slots.host_phenotype = Slot(uri=MIXS['0000874'], name="host_phenotype", curie=MIXS.curie('0000874'),
                   model_uri=DEFAULT_.host_phenotype, domain=None, range=Optional[Union[dict, ControlledTermValue]])

slots.host_sex = Slot(uri=MIXS['0000811'], name="host_sex", curie=MIXS.curie('0000811'),
                   model_uri=DEFAULT_.host_sex, domain=None, range=Optional[Union[dict, TextValue]])

slots.host_shape = Slot(uri=MIXS['0000261'], name="host_shape", curie=MIXS.curie('0000261'),
                   model_uri=DEFAULT_.host_shape, domain=None, range=Optional[Union[dict, TextValue]])

slots.host_subject_id = Slot(uri=MIXS['0000861'], name="host_subject_id", curie=MIXS.curie('0000861'),
                   model_uri=DEFAULT_.host_subject_id, domain=None, range=Optional[Union[dict, TextValue]])

slots.host_subspecf_genlin = Slot(uri=MIXS['0001318'], name="host_subspecf_genlin", curie=MIXS.curie('0001318'),
                   model_uri=DEFAULT_.host_subspecf_genlin, domain=None, range=Optional[Union[str, List[str]]])

slots.host_substrate = Slot(uri=MIXS['0000252'], name="host_substrate", curie=MIXS.curie('0000252'),
                   model_uri=DEFAULT_.host_substrate, domain=None, range=Optional[Union[dict, TextValue]])

slots.host_symbiont = Slot(uri=MIXS['0001298'], name="host_symbiont", curie=MIXS.curie('0001298'),
                   model_uri=DEFAULT_.host_symbiont, domain=None, range=Optional[Union[str, List[str]]])

slots.host_taxid = Slot(uri=MIXS['0000250'], name="host_taxid", curie=MIXS.curie('0000250'),
                   model_uri=DEFAULT_.host_taxid, domain=None, range=Optional[Union[dict, TextValue]])

slots.host_tot_mass = Slot(uri=MIXS['0000263'], name="host_tot_mass", curie=MIXS.curie('0000263'),
                   model_uri=DEFAULT_.host_tot_mass, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.host_wet_mass = Slot(uri=MIXS['0000567'], name="host_wet_mass", curie=MIXS.curie('0000567'),
                   model_uri=DEFAULT_.host_wet_mass, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.humidity = Slot(uri=MIXS['0000100'], name="humidity", curie=MIXS.curie('0000100'),
                   model_uri=DEFAULT_.humidity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.humidity_regm = Slot(uri=MIXS['0000568'], name="humidity_regm", curie=MIXS.curie('0000568'),
                   model_uri=DEFAULT_.humidity_regm, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.indoor_space = Slot(uri=MIXS['0000763'], name="indoor_space", curie=MIXS.curie('0000763'),
                   model_uri=DEFAULT_.indoor_space, domain=None, range=Optional[Union[dict, TextValue]])

slots.indoor_surf = Slot(uri=MIXS['0000764'], name="indoor_surf", curie=MIXS.curie('0000764'),
                   model_uri=DEFAULT_.indoor_surf, domain=None, range=Optional[Union[dict, TextValue]])

slots.indust_eff_percent = Slot(uri=MIXS['0000662'], name="indust_eff_percent", curie=MIXS.curie('0000662'),
                   model_uri=DEFAULT_.indust_eff_percent, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.inorg_particles = Slot(uri=MIXS['0000664'], name="inorg_particles", curie=MIXS.curie('0000664'),
                   model_uri=DEFAULT_.inorg_particles, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.inside_lux = Slot(uri=MIXS['0000168'], name="inside_lux", curie=MIXS.curie('0000168'),
                   model_uri=DEFAULT_.inside_lux, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.int_wall_cond = Slot(uri=MIXS['0000813'], name="int_wall_cond", curie=MIXS.curie('0000813'),
                   model_uri=DEFAULT_.int_wall_cond, domain=None, range=Optional[Union[dict, TextValue]])

slots.iw_bt_date_well = Slot(uri=MIXS['0001010'], name="iw_bt_date_well", curie=MIXS.curie('0001010'),
                   model_uri=DEFAULT_.iw_bt_date_well, domain=None, range=Optional[Union[dict, TimestampValue]])

slots.iwf = Slot(uri=MIXS['0000455'], name="iwf", curie=MIXS.curie('0000455'),
                   model_uri=DEFAULT_.iwf, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.last_clean = Slot(uri=MIXS['0000814'], name="last_clean", curie=MIXS.curie('0000814'),
                   model_uri=DEFAULT_.last_clean, domain=None, range=Optional[Union[dict, TimestampValue]])

slots.lat_lon = Slot(uri=MIXS['0000009'], name="lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=DEFAULT_.lat_lon, domain=None, range=Optional[Union[dict, GeolocationValue]])

slots.light_intensity = Slot(uri=MIXS['0000706'], name="light_intensity", curie=MIXS.curie('0000706'),
                   model_uri=DEFAULT_.light_intensity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.light_regm = Slot(uri=MIXS['0000569'], name="light_regm", curie=MIXS.curie('0000569'),
                   model_uri=DEFAULT_.light_regm, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.light_type = Slot(uri=MIXS['0000769'], name="light_type", curie=MIXS.curie('0000769'),
                   model_uri=DEFAULT_.light_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.link_addit_analys = Slot(uri=MIXS['0000340'], name="link_addit_analys", curie=MIXS.curie('0000340'),
                   model_uri=DEFAULT_.link_addit_analys, domain=None, range=Optional[Union[dict, TextValue]])

slots.link_class_info = Slot(uri=MIXS['0000329'], name="link_class_info", curie=MIXS.curie('0000329'),
                   model_uri=DEFAULT_.link_class_info, domain=None, range=Optional[Union[dict, TextValue]])

slots.link_climate_info = Slot(uri=MIXS['0000328'], name="link_climate_info", curie=MIXS.curie('0000328'),
                   model_uri=DEFAULT_.link_climate_info, domain=None, range=Optional[Union[dict, TextValue]])

slots.lithology = Slot(uri=MIXS['0000990'], name="lithology", curie=MIXS.curie('0000990'),
                   model_uri=DEFAULT_.lithology, domain=None, range=Optional[Union[dict, TextValue]])

slots.local_class = Slot(uri=MIXS['0000330'], name="local_class", curie=MIXS.curie('0000330'),
                   model_uri=DEFAULT_.local_class, domain=None, range=Optional[Union[dict, TextValue]])

slots.local_class_meth = Slot(uri=MIXS['0000331'], name="local_class_meth", curie=MIXS.curie('0000331'),
                   model_uri=DEFAULT_.local_class_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.magnesium = Slot(uri=MIXS['0000431'], name="magnesium", curie=MIXS.curie('0000431'),
                   model_uri=DEFAULT_.magnesium, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.max_occup = Slot(uri=MIXS['0000229'], name="max_occup", curie=MIXS.curie('0000229'),
                   model_uri=DEFAULT_.max_occup, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.mean_frict_vel = Slot(uri=MIXS['0000498'], name="mean_frict_vel", curie=MIXS.curie('0000498'),
                   model_uri=DEFAULT_.mean_frict_vel, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.mean_peak_frict_vel = Slot(uri=MIXS['0000502'], name="mean_peak_frict_vel", curie=MIXS.curie('0000502'),
                   model_uri=DEFAULT_.mean_peak_frict_vel, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.mech_struc = Slot(uri=MIXS['0000815'], name="mech_struc", curie=MIXS.curie('0000815'),
                   model_uri=DEFAULT_.mech_struc, domain=None, range=Optional[Union[dict, TextValue]])

slots.mechanical_damage = Slot(uri=MIXS['0001052'], name="mechanical_damage", curie=MIXS.curie('0001052'),
                   model_uri=DEFAULT_.mechanical_damage, domain=None, range=Optional[Union[dict, TextValue]])

slots.methane = Slot(uri=MIXS['0000101'], name="methane", curie=MIXS.curie('0000101'),
                   model_uri=DEFAULT_.methane, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.micro_biomass_meth = Slot(uri=MIXS['0000339'], name="micro_biomass_meth", curie=MIXS.curie('0000339'),
                   model_uri=DEFAULT_.micro_biomass_meth, domain=None, range=Optional[str])

slots.microbial_biomass = Slot(uri=MIXS['0000650'], name="microbial_biomass", curie=MIXS.curie('0000650'),
                   model_uri=DEFAULT_.microbial_biomass, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.microbial_biomass_meth = Slot(uri=MIXS['0000339'], name="microbial_biomass_meth", curie=MIXS.curie('0000339'),
                   model_uri=DEFAULT_.microbial_biomass_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.mineral_nutr_regm = Slot(uri=MIXS['0000570'], name="mineral_nutr_regm", curie=MIXS.curie('0000570'),
                   model_uri=DEFAULT_.mineral_nutr_regm, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.misc_param = Slot(uri=MIXS['0000752'], name="misc_param", curie=MIXS.curie('0000752'),
                   model_uri=DEFAULT_.misc_param, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.n_alkanes = Slot(uri=MIXS['0000503'], name="n_alkanes", curie=MIXS.curie('0000503'),
                   model_uri=DEFAULT_.n_alkanes, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.nitrate = Slot(uri=MIXS['0000425'], name="nitrate", curie=MIXS.curie('0000425'),
                   model_uri=DEFAULT_.nitrate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.nitrite = Slot(uri=MIXS['0000426'], name="nitrite", curie=MIXS.curie('0000426'),
                   model_uri=DEFAULT_.nitrite, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.nitro = Slot(uri=MIXS['0000504'], name="nitro", curie=MIXS.curie('0000504'),
                   model_uri=DEFAULT_.nitro, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.non_min_nutr_regm = Slot(uri=MIXS['0000571'], name="non_min_nutr_regm", curie=MIXS.curie('0000571'),
                   model_uri=DEFAULT_.non_min_nutr_regm, domain=None, range=Optional[Union[str, List[str]]])

slots.nucl_acid_amp = Slot(uri=MIXS['0000038'], name="nucl_acid_amp", curie=MIXS.curie('0000038'),
                   model_uri=DEFAULT_.nucl_acid_amp, domain=None, range=Optional[Union[dict, TextValue]])

slots.nucl_acid_ext = Slot(uri=MIXS['0000037'], name="nucl_acid_ext", curie=MIXS.curie('0000037'),
                   model_uri=DEFAULT_.nucl_acid_ext, domain=None, range=Optional[Union[dict, TextValue]])

slots.number_pets = Slot(uri=MIXS['0000231'], name="number_pets", curie=MIXS.curie('0000231'),
                   model_uri=DEFAULT_.number_pets, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.number_plants = Slot(uri=MIXS['0000230'], name="number_plants", curie=MIXS.curie('0000230'),
                   model_uri=DEFAULT_.number_plants, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.number_resident = Slot(uri=MIXS['0000232'], name="number_resident", curie=MIXS.curie('0000232'),
                   model_uri=DEFAULT_.number_resident, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.occup_density_samp = Slot(uri=MIXS['0000217'], name="occup_density_samp", curie=MIXS.curie('0000217'),
                   model_uri=DEFAULT_.occup_density_samp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.occup_document = Slot(uri=MIXS['0000816'], name="occup_document", curie=MIXS.curie('0000816'),
                   model_uri=DEFAULT_.occup_document, domain=None, range=Optional[Union[dict, TextValue]])

slots.occup_samp = Slot(uri=MIXS['0000772'], name="occup_samp", curie=MIXS.curie('0000772'),
                   model_uri=DEFAULT_.occup_samp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.org_carb = Slot(uri=MIXS['0000508'], name="org_carb", curie=MIXS.curie('0000508'),
                   model_uri=DEFAULT_.org_carb, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.org_count_qpcr_info = Slot(uri=MIXS['0000099'], name="org_count_qpcr_info", curie=MIXS.curie('0000099'),
                   model_uri=DEFAULT_.org_count_qpcr_info, domain=None, range=Optional[str])

slots.org_matter = Slot(uri=MIXS['0000204'], name="org_matter", curie=MIXS.curie('0000204'),
                   model_uri=DEFAULT_.org_matter, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.org_nitro = Slot(uri=MIXS['0000205'], name="org_nitro", curie=MIXS.curie('0000205'),
                   model_uri=DEFAULT_.org_nitro, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.org_particles = Slot(uri=MIXS['0000665'], name="org_particles", curie=MIXS.curie('0000665'),
                   model_uri=DEFAULT_.org_particles, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.organism_count = Slot(uri=MIXS['0000103'], name="organism_count", curie=MIXS.curie('0000103'),
                   model_uri=DEFAULT_.organism_count, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.owc_tvdss = Slot(uri=MIXS['0000405'], name="owc_tvdss", curie=MIXS.curie('0000405'),
                   model_uri=DEFAULT_.owc_tvdss, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.oxy_stat_samp = Slot(uri=MIXS['0000753'], name="oxy_stat_samp", curie=MIXS.curie('0000753'),
                   model_uri=DEFAULT_.oxy_stat_samp, domain=None, range=Optional[Union[dict, TextValue]])

slots.oxygen = Slot(uri=MIXS['0000104'], name="oxygen", curie=MIXS.curie('0000104'),
                   model_uri=DEFAULT_.oxygen, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.part_org_carb = Slot(uri=MIXS['0000515'], name="part_org_carb", curie=MIXS.curie('0000515'),
                   model_uri=DEFAULT_.part_org_carb, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.part_org_nitro = Slot(uri=MIXS['0000719'], name="part_org_nitro", curie=MIXS.curie('0000719'),
                   model_uri=DEFAULT_.part_org_nitro, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.particle_class = Slot(uri=MIXS['0000206'], name="particle_class", curie=MIXS.curie('0000206'),
                   model_uri=DEFAULT_.particle_class, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.pcr_cond = Slot(uri=MIXS['0000049'], name="pcr_cond", curie=MIXS.curie('0000049'),
                   model_uri=DEFAULT_.pcr_cond, domain=None, range=Optional[Union[dict, TextValue]])

slots.pcr_primers = Slot(uri=MIXS['0000046'], name="pcr_primers", curie=MIXS.curie('0000046'),
                   model_uri=DEFAULT_.pcr_primers, domain=None, range=Optional[Union[dict, TextValue]])

slots.permeability = Slot(uri=MIXS['0000404'], name="permeability", curie=MIXS.curie('0000404'),
                   model_uri=DEFAULT_.permeability, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.perturbation = Slot(uri=MIXS['0000754'], name="perturbation", curie=MIXS.curie('0000754'),
                   model_uri=DEFAULT_.perturbation, domain=None, range=Optional[Union[dict, TextValue]])

slots.pesticide_regm = Slot(uri=MIXS['0000573'], name="pesticide_regm", curie=MIXS.curie('0000573'),
                   model_uri=DEFAULT_.pesticide_regm, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.petroleum_hydrocarb = Slot(uri=MIXS['0000516'], name="petroleum_hydrocarb", curie=MIXS.curie('0000516'),
                   model_uri=DEFAULT_.petroleum_hydrocarb, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.ph = Slot(uri=MIXS['0001001'], name="ph", curie=MIXS.curie('0001001'),
                   model_uri=DEFAULT_.ph, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.ph_meth = Slot(uri=MIXS['0001106'], name="ph_meth", curie=MIXS.curie('0001106'),
                   model_uri=DEFAULT_.ph_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.ph_regm = Slot(uri=MIXS['0001056'], name="ph_regm", curie=MIXS.curie('0001056'),
                   model_uri=DEFAULT_.ph_regm, domain=None, range=Optional[Union[dict, TextValue]])

slots.phaeopigments = Slot(uri=MIXS['0000180'], name="phaeopigments", curie=MIXS.curie('0000180'),
                   model_uri=DEFAULT_.phaeopigments, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.phosphate = Slot(uri=MIXS['0000505'], name="phosphate", curie=MIXS.curie('0000505'),
                   model_uri=DEFAULT_.phosphate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.phosplipid_fatt_acid = Slot(uri=MIXS['0000181'], name="phosplipid_fatt_acid", curie=MIXS.curie('0000181'),
                   model_uri=DEFAULT_.phosplipid_fatt_acid, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.photon_flux = Slot(uri=MIXS['0000725'], name="photon_flux", curie=MIXS.curie('0000725'),
                   model_uri=DEFAULT_.photon_flux, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.plant_growth_med = Slot(uri=MIXS['0001057'], name="plant_growth_med", curie=MIXS.curie('0001057'),
                   model_uri=DEFAULT_.plant_growth_med, domain=None, range=Optional[Union[dict, ControlledTermValue]])

slots.plant_product = Slot(uri=MIXS['0001058'], name="plant_product", curie=MIXS.curie('0001058'),
                   model_uri=DEFAULT_.plant_product, domain=None, range=Optional[Union[dict, TextValue]])

slots.plant_sex = Slot(uri=MIXS['0001059'], name="plant_sex", curie=MIXS.curie('0001059'),
                   model_uri=DEFAULT_.plant_sex, domain=None, range=Optional[Union[dict, TextValue]])

slots.plant_struc = Slot(uri=MIXS['0001060'], name="plant_struc", curie=MIXS.curie('0001060'),
                   model_uri=DEFAULT_.plant_struc, domain=None, range=Optional[Union[dict, ControlledTermValue]])

slots.pollutants = Slot(uri=MIXS['0000107'], name="pollutants", curie=MIXS.curie('0000107'),
                   model_uri=DEFAULT_.pollutants, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.pool_dna_extracts = Slot(uri=MIXS['0000325'], name="pool_dna_extracts", curie=MIXS.curie('0000325'),
                   model_uri=DEFAULT_.pool_dna_extracts, domain=None, range=Optional[Union[dict, TextValue]])

slots.porosity = Slot(uri=MIXS['0000211'], name="porosity", curie=MIXS.curie('0000211'),
                   model_uri=DEFAULT_.porosity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.potassium = Slot(uri=MIXS['0000430'], name="potassium", curie=MIXS.curie('0000430'),
                   model_uri=DEFAULT_.potassium, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.pour_point = Slot(uri=MIXS['0000127'], name="pour_point", curie=MIXS.curie('0000127'),
                   model_uri=DEFAULT_.pour_point, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.pre_treatment = Slot(uri=MIXS['0000348'], name="pre_treatment", curie=MIXS.curie('0000348'),
                   model_uri=DEFAULT_.pre_treatment, domain=None, range=Optional[Union[dict, TextValue]])

slots.pres_animal_insect = Slot(uri=MIXS['0000819'], name="pres_animal_insect", curie=MIXS.curie('0000819'),
                   model_uri=DEFAULT_.pres_animal_insect, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(cat|dog|rodent|snake|other);\d+$'))

slots.pressure = Slot(uri=MIXS['0000412'], name="pressure", curie=MIXS.curie('0000412'),
                   model_uri=DEFAULT_.pressure, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.prev_land_use_meth = Slot(uri=MIXS['0000316'], name="prev_land_use_meth", curie=MIXS.curie('0000316'),
                   model_uri=DEFAULT_.prev_land_use_meth, domain=None, range=Optional[str])

slots.previous_land_use = Slot(uri=MIXS['0000315'], name="previous_land_use", curie=MIXS.curie('0000315'),
                   model_uri=DEFAULT_.previous_land_use, domain=None, range=Optional[Union[dict, TextValue]])

slots.previous_land_use_meth = Slot(uri=MIXS['0000316'], name="previous_land_use_meth", curie=MIXS.curie('0000316'),
                   model_uri=DEFAULT_.previous_land_use_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.primary_prod = Slot(uri=MIXS['0000728'], name="primary_prod", curie=MIXS.curie('0000728'),
                   model_uri=DEFAULT_.primary_prod, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.primary_treatment = Slot(uri=MIXS['0000349'], name="primary_treatment", curie=MIXS.curie('0000349'),
                   model_uri=DEFAULT_.primary_treatment, domain=None, range=Optional[Union[dict, TextValue]])

slots.prod_rate = Slot(uri=MIXS['0000452'], name="prod_rate", curie=MIXS.curie('0000452'),
                   model_uri=DEFAULT_.prod_rate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.prod_start_date = Slot(uri=MIXS['0001008'], name="prod_start_date", curie=MIXS.curie('0001008'),
                   model_uri=DEFAULT_.prod_start_date, domain=None, range=Optional[Union[dict, TimestampValue]])

slots.profile_position = Slot(uri=MIXS['0001084'], name="profile_position", curie=MIXS.curie('0001084'),
                   model_uri=DEFAULT_.profile_position, domain=None, range=Optional[Union[dict, TextValue]])

slots.quad_pos = Slot(uri=MIXS['0000820'], name="quad_pos", curie=MIXS.curie('0000820'),
                   model_uri=DEFAULT_.quad_pos, domain=None, range=Optional[Union[dict, TextValue]])

slots.radiation_regm = Slot(uri=MIXS['0000575'], name="radiation_regm", curie=MIXS.curie('0000575'),
                   model_uri=DEFAULT_.radiation_regm, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.rainfall_regm = Slot(uri=MIXS['0000576'], name="rainfall_regm", curie=MIXS.curie('0000576'),
                   model_uri=DEFAULT_.rainfall_regm, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.reactor_type = Slot(uri=MIXS['0000350'], name="reactor_type", curie=MIXS.curie('0000350'),
                   model_uri=DEFAULT_.reactor_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.redox_potential = Slot(uri=MIXS['0000182'], name="redox_potential", curie=MIXS.curie('0000182'),
                   model_uri=DEFAULT_.redox_potential, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.rel_air_humidity = Slot(uri=MIXS['0000121'], name="rel_air_humidity", curie=MIXS.curie('0000121'),
                   model_uri=DEFAULT_.rel_air_humidity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.rel_humidity_out = Slot(uri=MIXS['0000188'], name="rel_humidity_out", curie=MIXS.curie('0000188'),
                   model_uri=DEFAULT_.rel_humidity_out, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.rel_samp_loc = Slot(uri=MIXS['0000821'], name="rel_samp_loc", curie=MIXS.curie('0000821'),
                   model_uri=DEFAULT_.rel_samp_loc, domain=None, range=Optional[Union[dict, TextValue]])

slots.rel_to_oxygen = Slot(uri=MIXS['0000015'], name="rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=DEFAULT_.rel_to_oxygen, domain=None, range=Optional[Union[dict, TextValue]])

slots.reservoir = Slot(uri=MIXS['0000303'], name="reservoir", curie=MIXS.curie('0000303'),
                   model_uri=DEFAULT_.reservoir, domain=None, range=Optional[Union[dict, TextValue]])

slots.resins_pc = Slot(uri=MIXS['0000134'], name="resins_pc", curie=MIXS.curie('0000134'),
                   model_uri=DEFAULT_.resins_pc, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.room_air_exch_rate = Slot(uri=MIXS['0000169'], name="room_air_exch_rate", curie=MIXS.curie('0000169'),
                   model_uri=DEFAULT_.room_air_exch_rate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.room_architec_elem = Slot(uri=MIXS['0000233'], name="room_architec_elem", curie=MIXS.curie('0000233'),
                   model_uri=DEFAULT_.room_architec_elem, domain=None, range=Optional[str])

slots.room_condt = Slot(uri=MIXS['0000822'], name="room_condt", curie=MIXS.curie('0000822'),
                   model_uri=DEFAULT_.room_condt, domain=None, range=Optional[Union[dict, TextValue]])

slots.room_connected = Slot(uri=MIXS['0000826'], name="room_connected", curie=MIXS.curie('0000826'),
                   model_uri=DEFAULT_.room_connected, domain=None, range=Optional[Union[dict, TextValue]])

slots.room_count = Slot(uri=MIXS['0000234'], name="room_count", curie=MIXS.curie('0000234'),
                   model_uri=DEFAULT_.room_count, domain=None, range=Optional[Union[dict, TextValue]])

slots.room_dim = Slot(uri=MIXS['0000192'], name="room_dim", curie=MIXS.curie('0000192'),
                   model_uri=DEFAULT_.room_dim, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.room_door_dist = Slot(uri=MIXS['0000193'], name="room_door_dist", curie=MIXS.curie('0000193'),
                   model_uri=DEFAULT_.room_door_dist, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.room_door_share = Slot(uri=MIXS['0000242'], name="room_door_share", curie=MIXS.curie('0000242'),
                   model_uri=DEFAULT_.room_door_share, domain=None, range=Optional[Union[dict, TextValue]])

slots.room_hallway = Slot(uri=MIXS['0000238'], name="room_hallway", curie=MIXS.curie('0000238'),
                   model_uri=DEFAULT_.room_hallway, domain=None, range=Optional[Union[dict, TextValue]])

slots.room_loc = Slot(uri=MIXS['0000823'], name="room_loc", curie=MIXS.curie('0000823'),
                   model_uri=DEFAULT_.room_loc, domain=None, range=Optional[Union[dict, TextValue]])

slots.room_moist_dam_hist = Slot(uri=MIXS['0000235'], name="room_moist_dam_hist", curie=MIXS.curie('0000235'),
                   model_uri=DEFAULT_.room_moist_dam_hist, domain=None, range=Optional[int])

slots.room_net_area = Slot(uri=MIXS['0000194'], name="room_net_area", curie=MIXS.curie('0000194'),
                   model_uri=DEFAULT_.room_net_area, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.room_occup = Slot(uri=MIXS['0000236'], name="room_occup", curie=MIXS.curie('0000236'),
                   model_uri=DEFAULT_.room_occup, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.room_samp_pos = Slot(uri=MIXS['0000824'], name="room_samp_pos", curie=MIXS.curie('0000824'),
                   model_uri=DEFAULT_.room_samp_pos, domain=None, range=Optional[Union[dict, TextValue]])

slots.room_type = Slot(uri=MIXS['0000825'], name="room_type", curie=MIXS.curie('0000825'),
                   model_uri=DEFAULT_.room_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.room_vol = Slot(uri=MIXS['0000195'], name="room_vol", curie=MIXS.curie('0000195'),
                   model_uri=DEFAULT_.room_vol, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.room_wall_share = Slot(uri=MIXS['0000243'], name="room_wall_share", curie=MIXS.curie('0000243'),
                   model_uri=DEFAULT_.room_wall_share, domain=None, range=Optional[Union[dict, TextValue]])

slots.room_window_count = Slot(uri=MIXS['0000237'], name="room_window_count", curie=MIXS.curie('0000237'),
                   model_uri=DEFAULT_.room_window_count, domain=None, range=Optional[Union[dict, TextValue]])

slots.root_cond = Slot(uri=MIXS['0001061'], name="root_cond", curie=MIXS.curie('0001061'),
                   model_uri=DEFAULT_.root_cond, domain=None, range=Optional[Union[dict, TextValue]])

slots.root_med_carbon = Slot(uri=MIXS['0000577'], name="root_med_carbon", curie=MIXS.curie('0000577'),
                   model_uri=DEFAULT_.root_med_carbon, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.root_med_macronutr = Slot(uri=MIXS['0000578'], name="root_med_macronutr", curie=MIXS.curie('0000578'),
                   model_uri=DEFAULT_.root_med_macronutr, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.root_med_micronutr = Slot(uri=MIXS['0000579'], name="root_med_micronutr", curie=MIXS.curie('0000579'),
                   model_uri=DEFAULT_.root_med_micronutr, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.root_med_ph = Slot(uri=MIXS['0001062'], name="root_med_ph", curie=MIXS.curie('0001062'),
                   model_uri=DEFAULT_.root_med_ph, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.root_med_regl = Slot(uri=MIXS['0000581'], name="root_med_regl", curie=MIXS.curie('0000581'),
                   model_uri=DEFAULT_.root_med_regl, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.root_med_solid = Slot(uri=MIXS['0001063'], name="root_med_solid", curie=MIXS.curie('0001063'),
                   model_uri=DEFAULT_.root_med_solid, domain=None, range=Optional[Union[dict, TextValue]])

slots.root_med_suppl = Slot(uri=MIXS['0000580'], name="root_med_suppl", curie=MIXS.curie('0000580'),
                   model_uri=DEFAULT_.root_med_suppl, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.salinity = Slot(uri=MIXS['0000183'], name="salinity", curie=MIXS.curie('0000183'),
                   model_uri=DEFAULT_.salinity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.salinity_meth = Slot(uri=MIXS['0000341'], name="salinity_meth", curie=MIXS.curie('0000341'),
                   model_uri=DEFAULT_.salinity_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.salt_regm = Slot(uri=MIXS['0000582'], name="salt_regm", curie=MIXS.curie('0000582'),
                   model_uri=DEFAULT_.salt_regm, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samp_capt_status = Slot(uri=MIXS['0000860'], name="samp_capt_status", curie=MIXS.curie('0000860'),
                   model_uri=DEFAULT_.samp_capt_status, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_collec_device = Slot(uri=MIXS['0000002'], name="samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=DEFAULT_.samp_collec_device, domain=None, range=Optional[str])

slots.samp_collec_method = Slot(uri=MIXS['0001225'], name="samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=DEFAULT_.samp_collec_method, domain=None, range=Optional[str])

slots.samp_collect_device = Slot(uri=MIXS['0000002'], name="samp_collect_device", curie=MIXS.curie('0000002'),
                   model_uri=DEFAULT_.samp_collect_device, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_collect_point = Slot(uri=MIXS['0001015'], name="samp_collect_point", curie=MIXS.curie('0001015'),
                   model_uri=DEFAULT_.samp_collect_point, domain=None, range=Optional[Union[str, "SampCollectPointEnum"]])

slots.samp_dis_stage = Slot(uri=MIXS['0000249'], name="samp_dis_stage", curie=MIXS.curie('0000249'),
                   model_uri=DEFAULT_.samp_dis_stage, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_floor = Slot(uri=MIXS['0000828'], name="samp_floor", curie=MIXS.curie('0000828'),
                   model_uri=DEFAULT_.samp_floor, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_loc_corr_rate = Slot(uri=MIXS['0000136'], name="samp_loc_corr_rate", curie=MIXS.curie('0000136'),
                   model_uri=DEFAULT_.samp_loc_corr_rate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samp_mat_process = Slot(uri=MIXS['0000016'], name="samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=DEFAULT_.samp_mat_process, domain=None, range=Optional[Union[dict, ControlledTermValue]])

slots.samp_md = Slot(uri=MIXS['0000413'], name="samp_md", curie=MIXS.curie('0000413'),
                   model_uri=DEFAULT_.samp_md, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samp_name = Slot(uri=MIXS['0001107'], name="samp_name", curie=MIXS.curie('0001107'),
                   model_uri=DEFAULT_.samp_name, domain=None, range=Optional[str])

slots.samp_preserv = Slot(uri=MIXS['0000463'], name="samp_preserv", curie=MIXS.curie('0000463'),
                   model_uri=DEFAULT_.samp_preserv, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samp_room_id = Slot(uri=MIXS['0000244'], name="samp_room_id", curie=MIXS.curie('0000244'),
                   model_uri=DEFAULT_.samp_room_id, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_size = Slot(uri=MIXS['0000001'], name="samp_size", curie=MIXS.curie('0000001'),
                   model_uri=DEFAULT_.samp_size, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samp_sort_meth = Slot(uri=MIXS['0000216'], name="samp_sort_meth", curie=MIXS.curie('0000216'),
                   model_uri=DEFAULT_.samp_sort_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_store_dur = Slot(uri=MIXS['0000116'], name="samp_store_dur", curie=MIXS.curie('0000116'),
                   model_uri=DEFAULT_.samp_store_dur, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_store_loc = Slot(uri=MIXS['0000755'], name="samp_store_loc", curie=MIXS.curie('0000755'),
                   model_uri=DEFAULT_.samp_store_loc, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_store_temp = Slot(uri=MIXS['0000110'], name="samp_store_temp", curie=MIXS.curie('0000110'),
                   model_uri=DEFAULT_.samp_store_temp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samp_subtype = Slot(uri=MIXS['0000999'], name="samp_subtype", curie=MIXS.curie('0000999'),
                   model_uri=DEFAULT_.samp_subtype, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_time_out = Slot(uri=MIXS['0000196'], name="samp_time_out", curie=MIXS.curie('0000196'),
                   model_uri=DEFAULT_.samp_time_out, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_transport_cond = Slot(uri=MIXS['0000410'], name="samp_transport_cond", curie=MIXS.curie('0000410'),
                   model_uri=DEFAULT_.samp_transport_cond, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samp_tvdss = Slot(uri=MIXS['0000409'], name="samp_tvdss", curie=MIXS.curie('0000409'),
                   model_uri=DEFAULT_.samp_tvdss, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samp_type = Slot(uri=MIXS['0000998'], name="samp_type", curie=MIXS.curie('0000998'),
                   model_uri=DEFAULT_.samp_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_vol_we_dna_ext = Slot(uri=MIXS['0000111'], name="samp_vol_we_dna_ext", curie=MIXS.curie('0000111'),
                   model_uri=DEFAULT_.samp_vol_we_dna_ext, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samp_weather = Slot(uri=MIXS['0000827'], name="samp_weather", curie=MIXS.curie('0000827'),
                   model_uri=DEFAULT_.samp_weather, domain=None, range=Optional[Union[dict, TextValue]])

slots.samp_well_name = Slot(uri=MIXS['0000296'], name="samp_well_name", curie=MIXS.curie('0000296'),
                   model_uri=DEFAULT_.samp_well_name, domain=None, range=Optional[Union[dict, TextValue]])

slots.saturates_pc = Slot(uri=MIXS['0000131'], name="saturates_pc", curie=MIXS.curie('0000131'),
                   model_uri=DEFAULT_.saturates_pc, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.season = Slot(uri=MIXS['0000829'], name="season", curie=MIXS.curie('0000829'),
                   model_uri=DEFAULT_.season, domain=None, range=Optional[Union[dict, TextValue]])

slots.season_environment = Slot(uri=MIXS['0001068'], name="season_environment", curie=MIXS.curie('0001068'),
                   model_uri=DEFAULT_.season_environment, domain=None, range=Optional[Union[dict, TextValue]])

slots.season_precpt = Slot(uri=MIXS['0000645'], name="season_precpt", curie=MIXS.curie('0000645'),
                   model_uri=DEFAULT_.season_precpt, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.season_temp = Slot(uri=MIXS['0000643'], name="season_temp", curie=MIXS.curie('0000643'),
                   model_uri=DEFAULT_.season_temp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.season_use = Slot(uri=MIXS['0000830'], name="season_use", curie=MIXS.curie('0000830'),
                   model_uri=DEFAULT_.season_use, domain=None, range=Optional[Union[dict, TextValue]])

slots.secondary_treatment = Slot(uri=MIXS['0000351'], name="secondary_treatment", curie=MIXS.curie('0000351'),
                   model_uri=DEFAULT_.secondary_treatment, domain=None, range=Optional[Union[dict, TextValue]])

slots.sediment_type = Slot(uri=MIXS['0001078'], name="sediment_type", curie=MIXS.curie('0001078'),
                   model_uri=DEFAULT_.sediment_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.seq_meth = Slot(uri=MIXS['0000050'], name="seq_meth", curie=MIXS.curie('0000050'),
                   model_uri=DEFAULT_.seq_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.seq_quality_check = Slot(uri=MIXS['0000051'], name="seq_quality_check", curie=MIXS.curie('0000051'),
                   model_uri=DEFAULT_.seq_quality_check, domain=None, range=Optional[Union[dict, TextValue]])

slots.sewage_type = Slot(uri=MIXS['0000215'], name="sewage_type", curie=MIXS.curie('0000215'),
                   model_uri=DEFAULT_.sewage_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.shad_dev_water_mold = Slot(uri=MIXS['0000834'], name="shad_dev_water_mold", curie=MIXS.curie('0000834'),
                   model_uri=DEFAULT_.shad_dev_water_mold, domain=None, range=Optional[str])

slots.shading_device_cond = Slot(uri=MIXS['0000831'], name="shading_device_cond", curie=MIXS.curie('0000831'),
                   model_uri=DEFAULT_.shading_device_cond, domain=None, range=Optional[Union[dict, TextValue]])

slots.shading_device_loc = Slot(uri=MIXS['0000832'], name="shading_device_loc", curie=MIXS.curie('0000832'),
                   model_uri=DEFAULT_.shading_device_loc, domain=None, range=Optional[Union[dict, TextValue]])

slots.shading_device_mat = Slot(uri=MIXS['0000245'], name="shading_device_mat", curie=MIXS.curie('0000245'),
                   model_uri=DEFAULT_.shading_device_mat, domain=None, range=Optional[Union[dict, TextValue]])

slots.shading_device_type = Slot(uri=MIXS['0000835'], name="shading_device_type", curie=MIXS.curie('0000835'),
                   model_uri=DEFAULT_.shading_device_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.sieving = Slot(uri=MIXS['0000322'], name="sieving", curie=MIXS.curie('0000322'),
                   model_uri=DEFAULT_.sieving, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.silicate = Slot(uri=MIXS['0000184'], name="silicate", curie=MIXS.curie('0000184'),
                   model_uri=DEFAULT_.silicate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.size_frac = Slot(uri=MIXS['0000017'], name="size_frac", curie=MIXS.curie('0000017'),
                   model_uri=DEFAULT_.size_frac, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.size_frac_low = Slot(uri=MIXS['0000735'], name="size_frac_low", curie=MIXS.curie('0000735'),
                   model_uri=DEFAULT_.size_frac_low, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.size_frac_up = Slot(uri=MIXS['0000736'], name="size_frac_up", curie=MIXS.curie('0000736'),
                   model_uri=DEFAULT_.size_frac_up, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.slope_aspect = Slot(uri=MIXS['0000647'], name="slope_aspect", curie=MIXS.curie('0000647'),
                   model_uri=DEFAULT_.slope_aspect, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.slope_gradient = Slot(uri=MIXS['0000646'], name="slope_gradient", curie=MIXS.curie('0000646'),
                   model_uri=DEFAULT_.slope_gradient, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.sludge_retent_time = Slot(uri=MIXS['0000669'], name="sludge_retent_time", curie=MIXS.curie('0000669'),
                   model_uri=DEFAULT_.sludge_retent_time, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.sodium = Slot(uri=MIXS['0000428'], name="sodium", curie=MIXS.curie('0000428'),
                   model_uri=DEFAULT_.sodium, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.soil_horizon = Slot(uri=MIXS['0001082'], name="soil_horizon", curie=MIXS.curie('0001082'),
                   model_uri=DEFAULT_.soil_horizon, domain=None, range=Optional[Union[str, "SoilHorizonEnum"]])

slots.soil_text_measure = Slot(uri=MIXS['0000335'], name="soil_text_measure", curie=MIXS.curie('0000335'),
                   model_uri=DEFAULT_.soil_text_measure, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.soil_texture_meth = Slot(uri=MIXS['0000336'], name="soil_texture_meth", curie=MIXS.curie('0000336'),
                   model_uri=DEFAULT_.soil_texture_meth, domain=None, range=Optional[str])

slots.soil_type = Slot(uri=MIXS['0000332'], name="soil_type", curie=MIXS.curie('0000332'),
                   model_uri=DEFAULT_.soil_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.soil_type_meth = Slot(uri=MIXS['0000334'], name="soil_type_meth", curie=MIXS.curie('0000334'),
                   model_uri=DEFAULT_.soil_type_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.solar_irradiance = Slot(uri=MIXS['0000112'], name="solar_irradiance", curie=MIXS.curie('0000112'),
                   model_uri=DEFAULT_.solar_irradiance, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.soluble_inorg_mat = Slot(uri=MIXS['0000672'], name="soluble_inorg_mat", curie=MIXS.curie('0000672'),
                   model_uri=DEFAULT_.soluble_inorg_mat, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.soluble_org_mat = Slot(uri=MIXS['0000673'], name="soluble_org_mat", curie=MIXS.curie('0000673'),
                   model_uri=DEFAULT_.soluble_org_mat, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.soluble_react_phosp = Slot(uri=MIXS['0000738'], name="soluble_react_phosp", curie=MIXS.curie('0000738'),
                   model_uri=DEFAULT_.soluble_react_phosp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.source_mat_id = Slot(uri=MIXS['0000026'], name="source_mat_id", curie=MIXS.curie('0000026'),
                   model_uri=DEFAULT_.source_mat_id, domain=None, range=Optional[Union[dict, TextValue]])

slots.space_typ_state = Slot(uri=MIXS['0000770'], name="space_typ_state", curie=MIXS.curie('0000770'),
                   model_uri=DEFAULT_.space_typ_state, domain=None, range=Optional[Union[dict, TextValue]])

slots.specific = Slot(uri=MIXS['0000836'], name="specific", curie=MIXS.curie('0000836'),
                   model_uri=DEFAULT_.specific, domain=None, range=Optional[Union[dict, TextValue]])

slots.specific_humidity = Slot(uri=MIXS['0000214'], name="specific_humidity", curie=MIXS.curie('0000214'),
                   model_uri=DEFAULT_.specific_humidity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.sr_dep_env = Slot(uri=MIXS['0000996'], name="sr_dep_env", curie=MIXS.curie('0000996'),
                   model_uri=DEFAULT_.sr_dep_env, domain=None, range=Optional[Union[dict, TextValue]])

slots.sr_geol_age = Slot(uri=MIXS['0000997'], name="sr_geol_age", curie=MIXS.curie('0000997'),
                   model_uri=DEFAULT_.sr_geol_age, domain=None, range=Optional[Union[dict, TextValue]])

slots.sr_kerog_type = Slot(uri=MIXS['0000994'], name="sr_kerog_type", curie=MIXS.curie('0000994'),
                   model_uri=DEFAULT_.sr_kerog_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.sr_lithology = Slot(uri=MIXS['0000995'], name="sr_lithology", curie=MIXS.curie('0000995'),
                   model_uri=DEFAULT_.sr_lithology, domain=None, range=Optional[Union[dict, TextValue]])

slots.standing_water_regm = Slot(uri=MIXS['0001069'], name="standing_water_regm", curie=MIXS.curie('0001069'),
                   model_uri=DEFAULT_.standing_water_regm, domain=None, range=Optional[Union[dict, TextValue]])

slots.store_cond = Slot(uri=MIXS['0000327'], name="store_cond", curie=MIXS.curie('0000327'),
                   model_uri=DEFAULT_.store_cond, domain=None, range=Optional[Union[dict, TextValue]])

slots.substructure_type = Slot(uri=MIXS['0000767'], name="substructure_type", curie=MIXS.curie('0000767'),
                   model_uri=DEFAULT_.substructure_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.sulfate = Slot(uri=MIXS['0000423'], name="sulfate", curie=MIXS.curie('0000423'),
                   model_uri=DEFAULT_.sulfate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.sulfate_fw = Slot(uri=MIXS['0000407'], name="sulfate_fw", curie=MIXS.curie('0000407'),
                   model_uri=DEFAULT_.sulfate_fw, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.sulfide = Slot(uri=MIXS['0000424'], name="sulfide", curie=MIXS.curie('0000424'),
                   model_uri=DEFAULT_.sulfide, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.surf_air_cont = Slot(uri=MIXS['0000759'], name="surf_air_cont", curie=MIXS.curie('0000759'),
                   model_uri=DEFAULT_.surf_air_cont, domain=None, range=Optional[Union[dict, TextValue]])

slots.surf_humidity = Slot(uri=MIXS['0000123'], name="surf_humidity", curie=MIXS.curie('0000123'),
                   model_uri=DEFAULT_.surf_humidity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.surf_material = Slot(uri=MIXS['0000758'], name="surf_material", curie=MIXS.curie('0000758'),
                   model_uri=DEFAULT_.surf_material, domain=None, range=Optional[Union[dict, TextValue]])

slots.surf_moisture = Slot(uri=MIXS['0000128'], name="surf_moisture", curie=MIXS.curie('0000128'),
                   model_uri=DEFAULT_.surf_moisture, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.surf_moisture_ph = Slot(uri=MIXS['0000760'], name="surf_moisture_ph", curie=MIXS.curie('0000760'),
                   model_uri=DEFAULT_.surf_moisture_ph, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.surf_temp = Slot(uri=MIXS['0000125'], name="surf_temp", curie=MIXS.curie('0000125'),
                   model_uri=DEFAULT_.surf_temp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.suspend_part_matter = Slot(uri=MIXS['0000741'], name="suspend_part_matter", curie=MIXS.curie('0000741'),
                   model_uri=DEFAULT_.suspend_part_matter, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.suspend_solids = Slot(uri=MIXS['0000150'], name="suspend_solids", curie=MIXS.curie('0000150'),
                   model_uri=DEFAULT_.suspend_solids, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tan = Slot(uri=MIXS['0000120'], name="tan", curie=MIXS.curie('0000120'),
                   model_uri=DEFAULT_.tan, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.target_gene = Slot(uri=MIXS['0000044'], name="target_gene", curie=MIXS.curie('0000044'),
                   model_uri=DEFAULT_.target_gene, domain=None, range=Optional[Union[dict, TextValue]])

slots.target_subfragment = Slot(uri=MIXS['0000045'], name="target_subfragment", curie=MIXS.curie('0000045'),
                   model_uri=DEFAULT_.target_subfragment, domain=None, range=Optional[Union[dict, TextValue]])

slots.temp = Slot(uri=MIXS['0000113'], name="temp", curie=MIXS.curie('0000113'),
                   model_uri=DEFAULT_.temp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.temp_out = Slot(uri=MIXS['0000197'], name="temp_out", curie=MIXS.curie('0000197'),
                   model_uri=DEFAULT_.temp_out, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tertiary_treatment = Slot(uri=MIXS['0000352'], name="tertiary_treatment", curie=MIXS.curie('0000352'),
                   model_uri=DEFAULT_.tertiary_treatment, domain=None, range=Optional[Union[dict, TextValue]])

slots.texture = Slot(uri=MIXS['0000335'], name="texture", curie=MIXS.curie('0000335'),
                   model_uri=DEFAULT_.texture, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.texture_meth = Slot(uri=MIXS['0000336'], name="texture_meth", curie=MIXS.curie('0000336'),
                   model_uri=DEFAULT_.texture_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.tidal_stage = Slot(uri=MIXS['0000750'], name="tidal_stage", curie=MIXS.curie('0000750'),
                   model_uri=DEFAULT_.tidal_stage, domain=None, range=Optional[Union[dict, TextValue]])

slots.tillage = Slot(uri=MIXS['0001081'], name="tillage", curie=MIXS.curie('0001081'),
                   model_uri=DEFAULT_.tillage, domain=None, range=Optional[Union[dict, TextValue]])

slots.tiss_cult_growth_med = Slot(uri=MIXS['0001070'], name="tiss_cult_growth_med", curie=MIXS.curie('0001070'),
                   model_uri=DEFAULT_.tiss_cult_growth_med, domain=None, range=Optional[Union[dict, TextValue]])

slots.toluene = Slot(uri=MIXS['0000154'], name="toluene", curie=MIXS.curie('0000154'),
                   model_uri=DEFAULT_.toluene, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tot_carb = Slot(uri=MIXS['0000525'], name="tot_carb", curie=MIXS.curie('0000525'),
                   model_uri=DEFAULT_.tot_carb, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tot_depth_water_col = Slot(uri=MIXS['0000634'], name="tot_depth_water_col", curie=MIXS.curie('0000634'),
                   model_uri=DEFAULT_.tot_depth_water_col, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tot_diss_nitro = Slot(uri=MIXS['0000744'], name="tot_diss_nitro", curie=MIXS.curie('0000744'),
                   model_uri=DEFAULT_.tot_diss_nitro, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tot_inorg_nitro = Slot(uri=MIXS['0000745'], name="tot_inorg_nitro", curie=MIXS.curie('0000745'),
                   model_uri=DEFAULT_.tot_inorg_nitro, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tot_iron = Slot(uri=MIXS['0000105'], name="tot_iron", curie=MIXS.curie('0000105'),
                   model_uri=DEFAULT_.tot_iron, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tot_nitro = Slot(uri=MIXS['0000102'], name="tot_nitro", curie=MIXS.curie('0000102'),
                   model_uri=DEFAULT_.tot_nitro, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tot_nitro_cont_meth = Slot(uri=MIXS['0000338'], name="tot_nitro_cont_meth", curie=MIXS.curie('0000338'),
                   model_uri=DEFAULT_.tot_nitro_cont_meth, domain=None, range=Optional[str])

slots.tot_nitro_content = Slot(uri=MIXS['0000530'], name="tot_nitro_content", curie=MIXS.curie('0000530'),
                   model_uri=DEFAULT_.tot_nitro_content, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tot_org_c_meth = Slot(uri=MIXS['0000337'], name="tot_org_c_meth", curie=MIXS.curie('0000337'),
                   model_uri=DEFAULT_.tot_org_c_meth, domain=None, range=Optional[Union[dict, TextValue]])

slots.tot_org_carb = Slot(uri=MIXS['0000533'], name="tot_org_carb", curie=MIXS.curie('0000533'),
                   model_uri=DEFAULT_.tot_org_carb, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tot_part_carb = Slot(uri=MIXS['0000747'], name="tot_part_carb", curie=MIXS.curie('0000747'),
                   model_uri=DEFAULT_.tot_part_carb, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tot_phosp = Slot(uri=MIXS['0000117'], name="tot_phosp", curie=MIXS.curie('0000117'),
                   model_uri=DEFAULT_.tot_phosp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tot_phosphate = Slot(uri=MIXS['0000689'], name="tot_phosphate", curie=MIXS.curie('0000689'),
                   model_uri=DEFAULT_.tot_phosphate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tot_sulfur = Slot(uri=MIXS['0000419'], name="tot_sulfur", curie=MIXS.curie('0000419'),
                   model_uri=DEFAULT_.tot_sulfur, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.train_line = Slot(uri=MIXS['0000837'], name="train_line", curie=MIXS.curie('0000837'),
                   model_uri=DEFAULT_.train_line, domain=None, range=Optional[Union[dict, TextValue]])

slots.train_stat_loc = Slot(uri=MIXS['0000838'], name="train_stat_loc", curie=MIXS.curie('0000838'),
                   model_uri=DEFAULT_.train_stat_loc, domain=None, range=Optional[Union[dict, TextValue]])

slots.train_stop_loc = Slot(uri=MIXS['0000839'], name="train_stop_loc", curie=MIXS.curie('0000839'),
                   model_uri=DEFAULT_.train_stop_loc, domain=None, range=Optional[Union[dict, TextValue]])

slots.turbidity = Slot(uri=MIXS['0000191'], name="turbidity", curie=MIXS.curie('0000191'),
                   model_uri=DEFAULT_.turbidity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tvdss_of_hcr_press = Slot(uri=MIXS['0000397'], name="tvdss_of_hcr_press", curie=MIXS.curie('0000397'),
                   model_uri=DEFAULT_.tvdss_of_hcr_press, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tvdss_of_hcr_temp = Slot(uri=MIXS['0000394'], name="tvdss_of_hcr_temp", curie=MIXS.curie('0000394'),
                   model_uri=DEFAULT_.tvdss_of_hcr_temp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.typ_occup_density = Slot(uri=MIXS['0000771'], name="typ_occup_density", curie=MIXS.curie('0000771'),
                   model_uri=DEFAULT_.typ_occup_density, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.ventilation_rate = Slot(uri=MIXS['0000114'], name="ventilation_rate", curie=MIXS.curie('0000114'),
                   model_uri=DEFAULT_.ventilation_rate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.ventilation_type = Slot(uri=MIXS['0000756'], name="ventilation_type", curie=MIXS.curie('0000756'),
                   model_uri=DEFAULT_.ventilation_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.vfa = Slot(uri=MIXS['0000152'], name="vfa", curie=MIXS.curie('0000152'),
                   model_uri=DEFAULT_.vfa, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.vfa_fw = Slot(uri=MIXS['0000408'], name="vfa_fw", curie=MIXS.curie('0000408'),
                   model_uri=DEFAULT_.vfa_fw, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.vis_media = Slot(uri=MIXS['0000840'], name="vis_media", curie=MIXS.curie('0000840'),
                   model_uri=DEFAULT_.vis_media, domain=None, range=Optional[Union[dict, TextValue]])

slots.viscosity = Slot(uri=MIXS['0000126'], name="viscosity", curie=MIXS.curie('0000126'),
                   model_uri=DEFAULT_.viscosity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.volatile_org_comp = Slot(uri=MIXS['0000115'], name="volatile_org_comp", curie=MIXS.curie('0000115'),
                   model_uri=DEFAULT_.volatile_org_comp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.wall_area = Slot(uri=MIXS['0000198'], name="wall_area", curie=MIXS.curie('0000198'),
                   model_uri=DEFAULT_.wall_area, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.wall_const_type = Slot(uri=MIXS['0000841'], name="wall_const_type", curie=MIXS.curie('0000841'),
                   model_uri=DEFAULT_.wall_const_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.wall_finish_mat = Slot(uri=MIXS['0000842'], name="wall_finish_mat", curie=MIXS.curie('0000842'),
                   model_uri=DEFAULT_.wall_finish_mat, domain=None, range=Optional[Union[dict, TextValue]])

slots.wall_height = Slot(uri=MIXS['0000221'], name="wall_height", curie=MIXS.curie('0000221'),
                   model_uri=DEFAULT_.wall_height, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.wall_loc = Slot(uri=MIXS['0000843'], name="wall_loc", curie=MIXS.curie('0000843'),
                   model_uri=DEFAULT_.wall_loc, domain=None, range=Optional[Union[dict, TextValue]])

slots.wall_surf_treatment = Slot(uri=MIXS['0000845'], name="wall_surf_treatment", curie=MIXS.curie('0000845'),
                   model_uri=DEFAULT_.wall_surf_treatment, domain=None, range=Optional[Union[dict, TextValue]])

slots.wall_texture = Slot(uri=MIXS['0000846'], name="wall_texture", curie=MIXS.curie('0000846'),
                   model_uri=DEFAULT_.wall_texture, domain=None, range=Optional[Union[dict, TextValue]])

slots.wall_thermal_mass = Slot(uri=MIXS['0000222'], name="wall_thermal_mass", curie=MIXS.curie('0000222'),
                   model_uri=DEFAULT_.wall_thermal_mass, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.wall_water_mold = Slot(uri=MIXS['0000844'], name="wall_water_mold", curie=MIXS.curie('0000844'),
                   model_uri=DEFAULT_.wall_water_mold, domain=None, range=Optional[Union[dict, TextValue]])

slots.wastewater_type = Slot(uri=MIXS['0000353'], name="wastewater_type", curie=MIXS.curie('0000353'),
                   model_uri=DEFAULT_.wastewater_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.water_cont_soil_meth = Slot(uri=MIXS['0000323'], name="water_cont_soil_meth", curie=MIXS.curie('0000323'),
                   model_uri=DEFAULT_.water_cont_soil_meth, domain=None, range=Optional[str])

slots.water_content = Slot(uri=MIXS['0000185'], name="water_content", curie=MIXS.curie('0000185'),
                   model_uri=DEFAULT_.water_content, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.water_current = Slot(uri=MIXS['0000203'], name="water_current", curie=MIXS.curie('0000203'),
                   model_uri=DEFAULT_.water_current, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.water_cut = Slot(uri=MIXS['0000454'], name="water_cut", curie=MIXS.curie('0000454'),
                   model_uri=DEFAULT_.water_cut, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.water_feat_size = Slot(uri=MIXS['0000223'], name="water_feat_size", curie=MIXS.curie('0000223'),
                   model_uri=DEFAULT_.water_feat_size, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.water_feat_type = Slot(uri=MIXS['0000847'], name="water_feat_type", curie=MIXS.curie('0000847'),
                   model_uri=DEFAULT_.water_feat_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.water_prod_rate = Slot(uri=MIXS['0000453'], name="water_prod_rate", curie=MIXS.curie('0000453'),
                   model_uri=DEFAULT_.water_prod_rate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.water_temp_regm = Slot(uri=MIXS['0000590'], name="water_temp_regm", curie=MIXS.curie('0000590'),
                   model_uri=DEFAULT_.water_temp_regm, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.watering_regm = Slot(uri=MIXS['0000591'], name="watering_regm", curie=MIXS.curie('0000591'),
                   model_uri=DEFAULT_.watering_regm, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.weekday = Slot(uri=MIXS['0000848'], name="weekday", curie=MIXS.curie('0000848'),
                   model_uri=DEFAULT_.weekday, domain=None, range=Optional[Union[dict, TextValue]])

slots.win = Slot(uri=MIXS['0000297'], name="win", curie=MIXS.curie('0000297'),
                   model_uri=DEFAULT_.win, domain=None, range=Optional[Union[dict, TextValue]])

slots.wind_direction = Slot(uri=MIXS['0000757'], name="wind_direction", curie=MIXS.curie('0000757'),
                   model_uri=DEFAULT_.wind_direction, domain=None, range=Optional[Union[dict, TextValue]])

slots.wind_speed = Slot(uri=MIXS['0000118'], name="wind_speed", curie=MIXS.curie('0000118'),
                   model_uri=DEFAULT_.wind_speed, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.window_cond = Slot(uri=MIXS['0000849'], name="window_cond", curie=MIXS.curie('0000849'),
                   model_uri=DEFAULT_.window_cond, domain=None, range=Optional[Union[dict, TextValue]])

slots.window_cover = Slot(uri=MIXS['0000850'], name="window_cover", curie=MIXS.curie('0000850'),
                   model_uri=DEFAULT_.window_cover, domain=None, range=Optional[Union[dict, TextValue]])

slots.window_horiz_pos = Slot(uri=MIXS['0000851'], name="window_horiz_pos", curie=MIXS.curie('0000851'),
                   model_uri=DEFAULT_.window_horiz_pos, domain=None, range=Optional[Union[dict, TextValue]])

slots.window_loc = Slot(uri=MIXS['0000852'], name="window_loc", curie=MIXS.curie('0000852'),
                   model_uri=DEFAULT_.window_loc, domain=None, range=Optional[Union[dict, TextValue]])

slots.window_mat = Slot(uri=MIXS['0000853'], name="window_mat", curie=MIXS.curie('0000853'),
                   model_uri=DEFAULT_.window_mat, domain=None, range=Optional[Union[dict, TextValue]])

slots.window_open_freq = Slot(uri=MIXS['0000246'], name="window_open_freq", curie=MIXS.curie('0000246'),
                   model_uri=DEFAULT_.window_open_freq, domain=None, range=Optional[Union[dict, TextValue]])

slots.window_size = Slot(uri=MIXS['0000224'], name="window_size", curie=MIXS.curie('0000224'),
                   model_uri=DEFAULT_.window_size, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.window_status = Slot(uri=MIXS['0000855'], name="window_status", curie=MIXS.curie('0000855'),
                   model_uri=DEFAULT_.window_status, domain=None, range=Optional[Union[dict, TextValue]])

slots.window_type = Slot(uri=MIXS['0000856'], name="window_type", curie=MIXS.curie('0000856'),
                   model_uri=DEFAULT_.window_type, domain=None, range=Optional[Union[dict, TextValue]])

slots.window_vert_pos = Slot(uri=MIXS['0000857'], name="window_vert_pos", curie=MIXS.curie('0000857'),
                   model_uri=DEFAULT_.window_vert_pos, domain=None, range=Optional[Union[dict, TextValue]])

slots.window_water_mold = Slot(uri=MIXS['0000854'], name="window_water_mold", curie=MIXS.curie('0000854'),
                   model_uri=DEFAULT_.window_water_mold, domain=None, range=Optional[Union[dict, TextValue]])

slots.xylene = Slot(uri=MIXS['0000156'], name="xylene", curie=MIXS.curie('0000156'),
                   model_uri=DEFAULT_.xylene, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.env_package = Slot(uri=DEFAULT_.env_package, name="env_package", curie=DEFAULT_.curie('env_package'),
                   model_uri=DEFAULT_.env_package, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.env_package],
                   pattern=re.compile(r'[air|built environment|host\-associated|human\-associated|human\-skin|human\-oral|human\-gut|human\-vaginal|hydrocarbon resources\-cores|hydrocarbon resources\-fluids\/swabs|microbial mat\/biofilm|misc environment|plant\-associated|sediment|soil|wastewater\/sludge|water]'))

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
