# Auto generated from mixs_legacy.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-05-06T11:21:59
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


# Slots
class slots:
    pass

slots.submitted_to_insdc = Slot(uri=DEFAULT_.submitted_to_insdc, name="submitted_to_insdc", curie=DEFAULT_.curie('submitted_to_insdc'),
                   model_uri=DEFAULT_.submitted_to_insdc, domain=None, range=Optional[Union[dict, BooleanValue]], mappings = [MIXS.submitted_to_insdc],
                   pattern=re.compile(r'[true|false]'))

slots.investigation_type = Slot(uri=DEFAULT_.investigation_type, name="investigation_type", curie=DEFAULT_.curie('investigation_type'),
                   model_uri=DEFAULT_.investigation_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.investigation_type],
                   pattern=re.compile(r'[eukaryote|bacteria_archaea|plasmid|virus|organelle|metagenome|metatranscriptome|mimarks\-survey|mimarks\-specimen|misag|mimag|miuvig]'))

slots.project_name = Slot(uri=DEFAULT_.project_name, name="project_name", curie=DEFAULT_.curie('project_name'),
                   model_uri=DEFAULT_.project_name, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.project_name])

slots.experimental_factor = Slot(uri=DEFAULT_.experimental_factor, name="experimental_factor", curie=DEFAULT_.curie('experimental_factor'),
                   model_uri=DEFAULT_.experimental_factor, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.experimental_factor])

slots.lat_lon = Slot(uri=DEFAULT_.lat_lon, name="lat_lon", curie=DEFAULT_.curie('lat_lon'),
                   model_uri=DEFAULT_.lat_lon, domain=None, range=Optional[Union[dict, GeolocationValue]], mappings = [MIXS.lat_lon],
                   pattern=re.compile(r'\d+[.\d+] \d+[.\d+]'))

slots.depth = Slot(uri=DEFAULT_.depth, name="depth", curie=DEFAULT_.curie('depth'),
                   model_uri=DEFAULT_.depth, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.depth])

slots.alt = Slot(uri=DEFAULT_.alt, name="alt", curie=DEFAULT_.curie('alt'),
                   model_uri=DEFAULT_.alt, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.alt],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.elev = Slot(uri=DEFAULT_.elev, name="elev", curie=DEFAULT_.curie('elev'),
                   model_uri=DEFAULT_.elev, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.elev],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.geo_loc_name = Slot(uri=DEFAULT_.geo_loc_name, name="geo_loc_name", curie=DEFAULT_.curie('geo_loc_name'),
                   model_uri=DEFAULT_.geo_loc_name, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.geo_loc_name])

slots.collection_date = Slot(uri=DEFAULT_.collection_date, name="collection_date", curie=DEFAULT_.curie('collection_date'),
                   model_uri=DEFAULT_.collection_date, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.collection_date])

slots.env_broad_scale = Slot(uri=DEFAULT_.env_broad_scale, name="env_broad_scale", curie=DEFAULT_.curie('env_broad_scale'),
                   model_uri=DEFAULT_.env_broad_scale, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.env_broad_scale],
                   pattern=re.compile(r'.* \S+:\S+'))

slots.env_local_scale = Slot(uri=DEFAULT_.env_local_scale, name="env_local_scale", curie=DEFAULT_.curie('env_local_scale'),
                   model_uri=DEFAULT_.env_local_scale, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.env_local_scale],
                   pattern=re.compile(r'.* \S+:\S+'))

slots.env_medium = Slot(uri=DEFAULT_.env_medium, name="env_medium", curie=DEFAULT_.curie('env_medium'),
                   model_uri=DEFAULT_.env_medium, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.env_medium],
                   pattern=re.compile(r'.* \S+:\S+'))

slots.env_package = Slot(uri=DEFAULT_.env_package, name="env_package", curie=DEFAULT_.curie('env_package'),
                   model_uri=DEFAULT_.env_package, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.env_package],
                   pattern=re.compile(r'[air|built environment|host\-associated|human\-associated|human\-skin|human\-oral|human\-gut|human\-vaginal|hydrocarbon resources\-cores|hydrocarbon resources\-fluids\/swabs|microbial mat\/biofilm|misc environment|plant\-associated|sediment|soil|wastewater\/sludge|water]'))

slots.subspecf_gen_lin = Slot(uri=DEFAULT_.subspecf_gen_lin, name="subspecf_gen_lin", curie=DEFAULT_.curie('subspecf_gen_lin'),
                   model_uri=DEFAULT_.subspecf_gen_lin, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.subspecf_gen_lin])

slots.ploidy = Slot(uri=DEFAULT_.ploidy, name="ploidy", curie=DEFAULT_.curie('ploidy'),
                   model_uri=DEFAULT_.ploidy, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.ploidy],
                   pattern=re.compile(r'.* \S+:\S+'))

slots.num_replicons = Slot(uri=DEFAULT_.num_replicons, name="num_replicons", curie=DEFAULT_.curie('num_replicons'),
                   model_uri=DEFAULT_.num_replicons, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.num_replicons])

slots.extrachrom_elements = Slot(uri=DEFAULT_.extrachrom_elements, name="extrachrom_elements", curie=DEFAULT_.curie('extrachrom_elements'),
                   model_uri=DEFAULT_.extrachrom_elements, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.extrachrom_elements])

slots.estimated_size = Slot(uri=DEFAULT_.estimated_size, name="estimated_size", curie=DEFAULT_.curie('estimated_size'),
                   model_uri=DEFAULT_.estimated_size, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.estimated_size])

slots.ref_biomaterial = Slot(uri=DEFAULT_.ref_biomaterial, name="ref_biomaterial", curie=DEFAULT_.curie('ref_biomaterial'),
                   model_uri=DEFAULT_.ref_biomaterial, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ref_biomaterial])

slots.source_mat_id = Slot(uri=DEFAULT_.source_mat_id, name="source_mat_id", curie=DEFAULT_.curie('source_mat_id'),
                   model_uri=DEFAULT_.source_mat_id, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.source_mat_id])

slots.pathogenicity = Slot(uri=DEFAULT_.pathogenicity, name="pathogenicity", curie=DEFAULT_.curie('pathogenicity'),
                   model_uri=DEFAULT_.pathogenicity, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.pathogenicity])

slots.biotic_relationship = Slot(uri=DEFAULT_.biotic_relationship, name="biotic_relationship", curie=DEFAULT_.curie('biotic_relationship'),
                   model_uri=DEFAULT_.biotic_relationship, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.biotic_relationship],
                   pattern=re.compile(r'[free living|parasitism|commensalism|symbiotic|mutualism]'))

slots.specific_host = Slot(uri=DEFAULT_.specific_host, name="specific_host", curie=DEFAULT_.curie('specific_host'),
                   model_uri=DEFAULT_.specific_host, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.specific_host])

slots.host_spec_range = Slot(uri=DEFAULT_.host_spec_range, name="host_spec_range", curie=DEFAULT_.curie('host_spec_range'),
                   model_uri=DEFAULT_.host_spec_range, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_spec_range])

slots.health_disease_stat = Slot(uri=DEFAULT_.health_disease_stat, name="health_disease_stat", curie=DEFAULT_.curie('health_disease_stat'),
                   model_uri=DEFAULT_.health_disease_stat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.health_disease_stat],
                   pattern=re.compile(r'[healthy|diseased|dead|disease\-free|undetermined|recovering|resolving|pre\-existing condition|pathological|life threatening|congenital]'))

slots.trophic_level = Slot(uri=DEFAULT_.trophic_level, name="trophic_level", curie=DEFAULT_.curie('trophic_level'),
                   model_uri=DEFAULT_.trophic_level, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.trophic_level],
                   pattern=re.compile(r'[autotroph|carboxydotroph|chemoautotroph|chemoheterotroph|chemolithoautotroph|chemolithotroph|chemoorganoheterotroph|chemoorganotroph|chemosynthetic|chemotroph|copiotroph|diazotroph|facultative|autotroph|heterotroph|lithoautotroph|lithoheterotroph|lithotroph|methanotroph|methylotroph|mixotroph|obligate|chemoautolithotroph|oligotroph|organoheterotroph|organotroph|photoautotroph|photoheterotroph|photolithoautotroph|photolithotroph|photosynthetic|phototroph]'))

slots.propagation = Slot(uri=DEFAULT_.propagation, name="propagation", curie=DEFAULT_.curie('propagation'),
                   model_uri=DEFAULT_.propagation, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.propagation])

slots.encoded_traits = Slot(uri=DEFAULT_.encoded_traits, name="encoded_traits", curie=DEFAULT_.curie('encoded_traits'),
                   model_uri=DEFAULT_.encoded_traits, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.encoded_traits])

slots.rel_to_oxygen = Slot(uri=DEFAULT_.rel_to_oxygen, name="rel_to_oxygen", curie=DEFAULT_.curie('rel_to_oxygen'),
                   model_uri=DEFAULT_.rel_to_oxygen, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.rel_to_oxygen],
                   pattern=re.compile(r'[aerobe|anaerobe|facultative|microaerophilic|microanaerobe|obligate aerobe|obligate anaerobe]'))

slots.isol_growth_condt = Slot(uri=DEFAULT_.isol_growth_condt, name="isol_growth_condt", curie=DEFAULT_.curie('isol_growth_condt'),
                   model_uri=DEFAULT_.isol_growth_condt, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.isol_growth_condt])

slots.samp_collect_device = Slot(uri=DEFAULT_.samp_collect_device, name="samp_collect_device", curie=DEFAULT_.curie('samp_collect_device'),
                   model_uri=DEFAULT_.samp_collect_device, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_collect_device])

slots.samp_mat_process = Slot(uri=DEFAULT_.samp_mat_process, name="samp_mat_process", curie=DEFAULT_.curie('samp_mat_process'),
                   model_uri=DEFAULT_.samp_mat_process, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.samp_mat_process])

slots.size_frac = Slot(uri=DEFAULT_.size_frac, name="size_frac", curie=DEFAULT_.curie('size_frac'),
                   model_uri=DEFAULT_.size_frac, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.size_frac],
                   pattern=re.compile(r'\d+[.\d+]\-\d+[.\d+] \S+'))

slots.samp_size = Slot(uri=DEFAULT_.samp_size, name="samp_size", curie=DEFAULT_.curie('samp_size'),
                   model_uri=DEFAULT_.samp_size, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.samp_size],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.source_uvig = Slot(uri=DEFAULT_.source_uvig, name="source_uvig", curie=DEFAULT_.curie('source_uvig'),
                   model_uri=DEFAULT_.source_uvig, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.source_uvig],
                   pattern=re.compile(r'[metagenome (not viral targeted)|viral fraction metagenome (virome)|sequence\-targeted metagenome|metatranscriptome (not viral targeted)|viral fraction RNA metagenome (RNA virome)|sequence\-targeted RNA metagenome|microbial single amplified genome (SAG)|viral single amplified genome (vSAG)|isolate microbial genome|other]'))

slots.virus_enrich_appr = Slot(uri=DEFAULT_.virus_enrich_appr, name="virus_enrich_appr", curie=DEFAULT_.curie('virus_enrich_appr'),
                   model_uri=DEFAULT_.virus_enrich_appr, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.virus_enrich_appr],
                   pattern=re.compile(r'[filtration|ultrafiltration|centrifugation|ultracentrifugation|PEG Precipitation|FeCl Precipitation|CsCl density gradient|DNAse|RNAse|targeted sequence capture|other|none]'))

slots.nucl_acid_ext = Slot(uri=DEFAULT_.nucl_acid_ext, name="nucl_acid_ext", curie=DEFAULT_.curie('nucl_acid_ext'),
                   model_uri=DEFAULT_.nucl_acid_ext, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.nucl_acid_ext])

slots.nucl_acid_amp = Slot(uri=DEFAULT_.nucl_acid_amp, name="nucl_acid_amp", curie=DEFAULT_.curie('nucl_acid_amp'),
                   model_uri=DEFAULT_.nucl_acid_amp, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.nucl_acid_amp])

slots.lib_size = Slot(uri=DEFAULT_.lib_size, name="lib_size", curie=DEFAULT_.curie('lib_size'),
                   model_uri=DEFAULT_.lib_size, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.lib_size])

slots.lib_reads_seqd = Slot(uri=DEFAULT_.lib_reads_seqd, name="lib_reads_seqd", curie=DEFAULT_.curie('lib_reads_seqd'),
                   model_uri=DEFAULT_.lib_reads_seqd, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.lib_reads_seqd])

slots.lib_layout = Slot(uri=DEFAULT_.lib_layout, name="lib_layout", curie=DEFAULT_.curie('lib_layout'),
                   model_uri=DEFAULT_.lib_layout, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.lib_layout],
                   pattern=re.compile(r'[paired|single|vector|other]'))

slots.lib_vector = Slot(uri=DEFAULT_.lib_vector, name="lib_vector", curie=DEFAULT_.curie('lib_vector'),
                   model_uri=DEFAULT_.lib_vector, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.lib_vector])

slots.lib_screen = Slot(uri=DEFAULT_.lib_screen, name="lib_screen", curie=DEFAULT_.curie('lib_screen'),
                   model_uri=DEFAULT_.lib_screen, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.lib_screen])

slots.target_gene = Slot(uri=DEFAULT_.target_gene, name="target_gene", curie=DEFAULT_.curie('target_gene'),
                   model_uri=DEFAULT_.target_gene, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.target_gene])

slots.target_subfragment = Slot(uri=DEFAULT_.target_subfragment, name="target_subfragment", curie=DEFAULT_.curie('target_subfragment'),
                   model_uri=DEFAULT_.target_subfragment, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.target_subfragment])

slots.pcr_primers = Slot(uri=DEFAULT_.pcr_primers, name="pcr_primers", curie=DEFAULT_.curie('pcr_primers'),
                   model_uri=DEFAULT_.pcr_primers, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.pcr_primers])

slots.mid = Slot(uri=DEFAULT_.mid, name="mid", curie=DEFAULT_.curie('mid'),
                   model_uri=DEFAULT_.mid, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.mid])

slots.adapters = Slot(uri=DEFAULT_.adapters, name="adapters", curie=DEFAULT_.curie('adapters'),
                   model_uri=DEFAULT_.adapters, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.adapters])

slots.pcr_cond = Slot(uri=DEFAULT_.pcr_cond, name="pcr_cond", curie=DEFAULT_.curie('pcr_cond'),
                   model_uri=DEFAULT_.pcr_cond, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.pcr_cond],
                   pattern=re.compile(r'initial denaturation:degrees_minutes;annealing:degrees_minutes;elongation:degrees_minutes;final elongation:degrees_minutes;total cycles'))

slots.seq_meth = Slot(uri=DEFAULT_.seq_meth, name="seq_meth", curie=DEFAULT_.curie('seq_meth'),
                   model_uri=DEFAULT_.seq_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.seq_meth],
                   pattern=re.compile(r'[MinION|GridION|PromethION|454 GS|454 GS 20|454 GS FLX|454 GS FLX+|454 GS FLX Titanium|454 GS Junior|Illumina Genome Analyzer|Illumina Genome Analyzer II|Illumina Genome Analyzer IIx|Illumina HiSeq 4000|Illumina HiSeq 3000|Illumina HiSeq 2500|Illumina HiSeq 2000|Illumina HiSeq 1500|Illumina HiSeq 1000|Illumina HiScanSQ|Illumina MiSeq|Illumina HiSeq X Five|Illumina HiSeq X Ten|Illumina NextSeq 500|Illumina NextSeq 550|AB SOLiD System|AB SOLiD System 2.0|AB SOLiD System 3.0|AB SOLiD 3 Plus System|AB SOLiD 4 System|AB SOLiD 4hq System|AB SOLiD PI System|AB 5500 Genetic Analyzer|AB 5500xl Genetic Analyzer|AB 5500xl\-W Genetic Analysis System|Ion Torrent PGM|Ion Torrent Proton|Ion Torrent S5|Ion Torrent S5 XL|PacBio RS|PacBio RS II|Sequel|AB 3730xL Genetic Analyzer|AB 3730 Genetic Analyzer|AB 3500xL Genetic Analyzer|AB 3500 Genetic Analyzer|AB 3130xL Genetic Analyzer|AB 3130 Genetic Analyzer|AB 310 Genetic Analyzer|BGISEQ\-500]'))

slots.seq_quality_check = Slot(uri=DEFAULT_.seq_quality_check, name="seq_quality_check", curie=DEFAULT_.curie('seq_quality_check'),
                   model_uri=DEFAULT_.seq_quality_check, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.seq_quality_check],
                   pattern=re.compile(r'[none|manually edited]'))

slots.chimera_check = Slot(uri=DEFAULT_.chimera_check, name="chimera_check", curie=DEFAULT_.curie('chimera_check'),
                   model_uri=DEFAULT_.chimera_check, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.chimera_check])

slots.tax_ident = Slot(uri=DEFAULT_.tax_ident, name="tax_ident", curie=DEFAULT_.curie('tax_ident'),
                   model_uri=DEFAULT_.tax_ident, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.tax_ident],
                   pattern=re.compile(r'[16S rRNA gene|multi\-marker approach|other]'))

slots.assembly_qual = Slot(uri=DEFAULT_.assembly_qual, name="assembly_qual", curie=DEFAULT_.curie('assembly_qual'),
                   model_uri=DEFAULT_.assembly_qual, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.assembly_qual],
                   pattern=re.compile(r'[Finished genome|High\-quality draft genome|Medium\-quality draft genome|Low\-quality draft genome|Genome fragment(s)]'))

slots.assembly_name = Slot(uri=DEFAULT_.assembly_name, name="assembly_name", curie=DEFAULT_.curie('assembly_name'),
                   model_uri=DEFAULT_.assembly_name, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.assembly_name])

slots.assembly_software = Slot(uri=DEFAULT_.assembly_software, name="assembly_software", curie=DEFAULT_.curie('assembly_software'),
                   model_uri=DEFAULT_.assembly_software, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.assembly_software])

slots.annot = Slot(uri=DEFAULT_.annot, name="annot", curie=DEFAULT_.curie('annot'),
                   model_uri=DEFAULT_.annot, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.annot])

slots.number_contig = Slot(uri=DEFAULT_.number_contig, name="number_contig", curie=DEFAULT_.curie('number_contig'),
                   model_uri=DEFAULT_.number_contig, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.number_contig])

slots.feat_pred = Slot(uri=DEFAULT_.feat_pred, name="feat_pred", curie=DEFAULT_.curie('feat_pred'),
                   model_uri=DEFAULT_.feat_pred, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.feat_pred])

slots.ref_db = Slot(uri=DEFAULT_.ref_db, name="ref_db", curie=DEFAULT_.curie('ref_db'),
                   model_uri=DEFAULT_.ref_db, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ref_db])

slots.sim_search_meth = Slot(uri=DEFAULT_.sim_search_meth, name="sim_search_meth", curie=DEFAULT_.curie('sim_search_meth'),
                   model_uri=DEFAULT_.sim_search_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.sim_search_meth])

slots.tax_class = Slot(uri=DEFAULT_.tax_class, name="tax_class", curie=DEFAULT_.curie('tax_class'),
                   model_uri=DEFAULT_.tax_class, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.tax_class])

slots._16s_recover = Slot(uri=DEFAULT_._16s_recover, name="_16s_recover", curie=DEFAULT_.curie('_16s_recover'),
                   model_uri=DEFAULT_._16s_recover, domain=None, range=Optional[Union[dict, BooleanValue]], mappings = [MIXS._16s_recover],
                   pattern=re.compile(r'[true|false]'))

slots._16s_recover_software = Slot(uri=DEFAULT_._16s_recover_software, name="_16s_recover_software", curie=DEFAULT_.curie('_16s_recover_software'),
                   model_uri=DEFAULT_._16s_recover_software, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS._16s_recover_software])

slots.trnas = Slot(uri=DEFAULT_.trnas, name="trnas", curie=DEFAULT_.curie('trnas'),
                   model_uri=DEFAULT_.trnas, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.trnas])

slots.trna_ext_software = Slot(uri=DEFAULT_.trna_ext_software, name="trna_ext_software", curie=DEFAULT_.curie('trna_ext_software'),
                   model_uri=DEFAULT_.trna_ext_software, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.trna_ext_software])

slots.compl_score = Slot(uri=DEFAULT_.compl_score, name="compl_score", curie=DEFAULT_.curie('compl_score'),
                   model_uri=DEFAULT_.compl_score, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.compl_score])

slots.compl_software = Slot(uri=DEFAULT_.compl_software, name="compl_software", curie=DEFAULT_.curie('compl_software'),
                   model_uri=DEFAULT_.compl_software, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.compl_software])

slots.compl_appr = Slot(uri=DEFAULT_.compl_appr, name="compl_appr", curie=DEFAULT_.curie('compl_appr'),
                   model_uri=DEFAULT_.compl_appr, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.compl_appr],
                   pattern=re.compile(r'[marker gene|reference based|other]'))

slots.contam_score = Slot(uri=DEFAULT_.contam_score, name="contam_score", curie=DEFAULT_.curie('contam_score'),
                   model_uri=DEFAULT_.contam_score, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.contam_score],
                   pattern=re.compile(r'\d+[.\d+] percentage'))

slots.contam_screen_input = Slot(uri=DEFAULT_.contam_screen_input, name="contam_screen_input", curie=DEFAULT_.curie('contam_screen_input'),
                   model_uri=DEFAULT_.contam_screen_input, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.contam_screen_input],
                   pattern=re.compile(r'[reads| contigs]'))

slots.contam_screen_param = Slot(uri=DEFAULT_.contam_screen_param, name="contam_screen_param", curie=DEFAULT_.curie('contam_screen_param'),
                   model_uri=DEFAULT_.contam_screen_param, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.contam_screen_param])

slots.decontam_software = Slot(uri=DEFAULT_.decontam_software, name="decontam_software", curie=DEFAULT_.curie('decontam_software'),
                   model_uri=DEFAULT_.decontam_software, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.decontam_software],
                   pattern=re.compile(r'[checkm\/refinem|anvi\'o|prodege|bbtools:decontaminate.sh|acdc|combination]'))

slots.sort_tech = Slot(uri=DEFAULT_.sort_tech, name="sort_tech", curie=DEFAULT_.curie('sort_tech'),
                   model_uri=DEFAULT_.sort_tech, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.sort_tech],
                   pattern=re.compile(r'[flow cytometric cell sorting|microfluidics|lazer\-tweezing|optical manipulation|micromanipulation|other]'))

slots.single_cell_lysis_appr = Slot(uri=DEFAULT_.single_cell_lysis_appr, name="single_cell_lysis_appr", curie=DEFAULT_.curie('single_cell_lysis_appr'),
                   model_uri=DEFAULT_.single_cell_lysis_appr, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.single_cell_lysis_appr],
                   pattern=re.compile(r'[chemical|enzymatic|physical|combination]'))

slots.single_cell_lysis_prot = Slot(uri=DEFAULT_.single_cell_lysis_prot, name="single_cell_lysis_prot", curie=DEFAULT_.curie('single_cell_lysis_prot'),
                   model_uri=DEFAULT_.single_cell_lysis_prot, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.single_cell_lysis_prot])

slots.wga_amp_appr = Slot(uri=DEFAULT_.wga_amp_appr, name="wga_amp_appr", curie=DEFAULT_.curie('wga_amp_appr'),
                   model_uri=DEFAULT_.wga_amp_appr, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.wga_amp_appr],
                   pattern=re.compile(r'[pcr based|mda based]'))

slots.wga_amp_kit = Slot(uri=DEFAULT_.wga_amp_kit, name="wga_amp_kit", curie=DEFAULT_.curie('wga_amp_kit'),
                   model_uri=DEFAULT_.wga_amp_kit, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.wga_amp_kit])

slots.bin_param = Slot(uri=DEFAULT_.bin_param, name="bin_param", curie=DEFAULT_.curie('bin_param'),
                   model_uri=DEFAULT_.bin_param, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.bin_param],
                   pattern=re.compile(r'[homology search|kmer|coverage|codon usage|combination]'))

slots.bin_software = Slot(uri=DEFAULT_.bin_software, name="bin_software", curie=DEFAULT_.curie('bin_software'),
                   model_uri=DEFAULT_.bin_software, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.bin_software],
                   pattern=re.compile(r'[metabat|maxbin|concoct|groupm|esom|metawatt|combination|other]'))

slots.reassembly_bin = Slot(uri=DEFAULT_.reassembly_bin, name="reassembly_bin", curie=DEFAULT_.curie('reassembly_bin'),
                   model_uri=DEFAULT_.reassembly_bin, domain=None, range=Optional[Union[dict, BooleanValue]], mappings = [MIXS.reassembly_bin],
                   pattern=re.compile(r'[true|false]'))

slots.mag_cov_software = Slot(uri=DEFAULT_.mag_cov_software, name="mag_cov_software", curie=DEFAULT_.curie('mag_cov_software'),
                   model_uri=DEFAULT_.mag_cov_software, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.mag_cov_software],
                   pattern=re.compile(r'[bwa|bbmap|bowtie|other]'))

slots.vir_ident_software = Slot(uri=DEFAULT_.vir_ident_software, name="vir_ident_software", curie=DEFAULT_.curie('vir_ident_software'),
                   model_uri=DEFAULT_.vir_ident_software, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.vir_ident_software])

slots.pred_genome_type = Slot(uri=DEFAULT_.pred_genome_type, name="pred_genome_type", curie=DEFAULT_.curie('pred_genome_type'),
                   model_uri=DEFAULT_.pred_genome_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.pred_genome_type],
                   pattern=re.compile(r'[DNA|dsDNA|ssDNA|RNA|dsRNA|ssRNA|ssRNA (+)|ssRNA (\-)|mixed|uncharacterized]'))

slots.pred_genome_struc = Slot(uri=DEFAULT_.pred_genome_struc, name="pred_genome_struc", curie=DEFAULT_.curie('pred_genome_struc'),
                   model_uri=DEFAULT_.pred_genome_struc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.pred_genome_struc],
                   pattern=re.compile(r'[segmented|non\-segmented|undetermined]'))

slots.detec_type = Slot(uri=DEFAULT_.detec_type, name="detec_type", curie=DEFAULT_.curie('detec_type'),
                   model_uri=DEFAULT_.detec_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.detec_type],
                   pattern=re.compile(r'[independent sequence (UViG)|provirus (UpViG)]'))

slots.votu_class_appr = Slot(uri=DEFAULT_.votu_class_appr, name="votu_class_appr", curie=DEFAULT_.curie('votu_class_appr'),
                   model_uri=DEFAULT_.votu_class_appr, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.votu_class_appr])

slots.votu_seq_comp_appr = Slot(uri=DEFAULT_.votu_seq_comp_appr, name="votu_seq_comp_appr", curie=DEFAULT_.curie('votu_seq_comp_appr'),
                   model_uri=DEFAULT_.votu_seq_comp_appr, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.votu_seq_comp_appr])

slots.votu_db = Slot(uri=DEFAULT_.votu_db, name="votu_db", curie=DEFAULT_.curie('votu_db'),
                   model_uri=DEFAULT_.votu_db, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.votu_db])

slots.host_pred_appr = Slot(uri=DEFAULT_.host_pred_appr, name="host_pred_appr", curie=DEFAULT_.curie('host_pred_appr'),
                   model_uri=DEFAULT_.host_pred_appr, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_pred_appr],
                   pattern=re.compile(r'[provirus|host sequence similarity|CRISPR spacer match|kmer similarity|co\-occurrence|combination|other]'))

slots.host_pred_est_acc = Slot(uri=DEFAULT_.host_pred_est_acc, name="host_pred_est_acc", curie=DEFAULT_.curie('host_pred_est_acc'),
                   model_uri=DEFAULT_.host_pred_est_acc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_pred_est_acc])

slots.mixs_url = Slot(uri=DEFAULT_.mixs_url, name="mixs_url", curie=DEFAULT_.curie('mixs_url'),
                   model_uri=DEFAULT_.mixs_url, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.mixs_url])

slots.sop = Slot(uri=DEFAULT_.sop, name="sop", curie=DEFAULT_.curie('sop'),
                   model_uri=DEFAULT_.sop, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.sop])

slots.barometric_press = Slot(uri=DEFAULT_.barometric_press, name="barometric_press", curie=DEFAULT_.curie('barometric_press'),
                   model_uri=DEFAULT_.barometric_press, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.barometric_press],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.carb_dioxide = Slot(uri=DEFAULT_.carb_dioxide, name="carb_dioxide", curie=DEFAULT_.curie('carb_dioxide'),
                   model_uri=DEFAULT_.carb_dioxide, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.carb_dioxide],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.carb_monoxide = Slot(uri=DEFAULT_.carb_monoxide, name="carb_monoxide", curie=DEFAULT_.curie('carb_monoxide'),
                   model_uri=DEFAULT_.carb_monoxide, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.carb_monoxide],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.chem_administration = Slot(uri=DEFAULT_.chem_administration, name="chem_administration", curie=DEFAULT_.curie('chem_administration'),
                   model_uri=DEFAULT_.chem_administration, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.chem_administration])

slots.humidity = Slot(uri=DEFAULT_.humidity, name="humidity", curie=DEFAULT_.curie('humidity'),
                   model_uri=DEFAULT_.humidity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.humidity],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.methane = Slot(uri=DEFAULT_.methane, name="methane", curie=DEFAULT_.curie('methane'),
                   model_uri=DEFAULT_.methane, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.methane],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.misc_param = Slot(uri=DEFAULT_.misc_param, name="misc_param", curie=DEFAULT_.curie('misc_param'),
                   model_uri=DEFAULT_.misc_param, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.misc_param])

slots.organism_count = Slot(uri=DEFAULT_.organism_count, name="organism_count", curie=DEFAULT_.curie('organism_count'),
                   model_uri=DEFAULT_.organism_count, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.organism_count])

slots.oxygen = Slot(uri=DEFAULT_.oxygen, name="oxygen", curie=DEFAULT_.curie('oxygen'),
                   model_uri=DEFAULT_.oxygen, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.oxygen],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.oxy_stat_samp = Slot(uri=DEFAULT_.oxy_stat_samp, name="oxy_stat_samp", curie=DEFAULT_.curie('oxy_stat_samp'),
                   model_uri=DEFAULT_.oxy_stat_samp, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.oxy_stat_samp],
                   pattern=re.compile(r'[aerobic|anaerobic|other]'))

slots.perturbation = Slot(uri=DEFAULT_.perturbation, name="perturbation", curie=DEFAULT_.curie('perturbation'),
                   model_uri=DEFAULT_.perturbation, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.perturbation])

slots.pollutants = Slot(uri=DEFAULT_.pollutants, name="pollutants", curie=DEFAULT_.curie('pollutants'),
                   model_uri=DEFAULT_.pollutants, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.pollutants])

slots.resp_part_matter = Slot(uri=DEFAULT_.resp_part_matter, name="resp_part_matter", curie=DEFAULT_.curie('resp_part_matter'),
                   model_uri=DEFAULT_.resp_part_matter, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.resp_part_matter])

slots.samp_salinity = Slot(uri=DEFAULT_.samp_salinity, name="samp_salinity", curie=DEFAULT_.curie('samp_salinity'),
                   model_uri=DEFAULT_.samp_salinity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.samp_salinity],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.samp_store_dur = Slot(uri=DEFAULT_.samp_store_dur, name="samp_store_dur", curie=DEFAULT_.curie('samp_store_dur'),
                   model_uri=DEFAULT_.samp_store_dur, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_store_dur])

slots.samp_store_loc = Slot(uri=DEFAULT_.samp_store_loc, name="samp_store_loc", curie=DEFAULT_.curie('samp_store_loc'),
                   model_uri=DEFAULT_.samp_store_loc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_store_loc])

slots.samp_store_temp = Slot(uri=DEFAULT_.samp_store_temp, name="samp_store_temp", curie=DEFAULT_.curie('samp_store_temp'),
                   model_uri=DEFAULT_.samp_store_temp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.samp_store_temp],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.samp_vol_we_dna_ext = Slot(uri=DEFAULT_.samp_vol_we_dna_ext, name="samp_vol_we_dna_ext", curie=DEFAULT_.curie('samp_vol_we_dna_ext'),
                   model_uri=DEFAULT_.samp_vol_we_dna_ext, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.samp_vol_we_dna_ext],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.solar_irradiance = Slot(uri=DEFAULT_.solar_irradiance, name="solar_irradiance", curie=DEFAULT_.curie('solar_irradiance'),
                   model_uri=DEFAULT_.solar_irradiance, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.solar_irradiance],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.temp = Slot(uri=DEFAULT_.temp, name="temp", curie=DEFAULT_.curie('temp'),
                   model_uri=DEFAULT_.temp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.temp],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.ventilation_rate = Slot(uri=DEFAULT_.ventilation_rate, name="ventilation_rate", curie=DEFAULT_.curie('ventilation_rate'),
                   model_uri=DEFAULT_.ventilation_rate, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.ventilation_rate],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.ventilation_type = Slot(uri=DEFAULT_.ventilation_type, name="ventilation_type", curie=DEFAULT_.curie('ventilation_type'),
                   model_uri=DEFAULT_.ventilation_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ventilation_type])

slots.volatile_org_comp = Slot(uri=DEFAULT_.volatile_org_comp, name="volatile_org_comp", curie=DEFAULT_.curie('volatile_org_comp'),
                   model_uri=DEFAULT_.volatile_org_comp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.volatile_org_comp])

slots.wind_direction = Slot(uri=DEFAULT_.wind_direction, name="wind_direction", curie=DEFAULT_.curie('wind_direction'),
                   model_uri=DEFAULT_.wind_direction, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.wind_direction])

slots.wind_speed = Slot(uri=DEFAULT_.wind_speed, name="wind_speed", curie=DEFAULT_.curie('wind_speed'),
                   model_uri=DEFAULT_.wind_speed, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.wind_speed],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.surf_material = Slot(uri=DEFAULT_.surf_material, name="surf_material", curie=DEFAULT_.curie('surf_material'),
                   model_uri=DEFAULT_.surf_material, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.surf_material],
                   pattern=re.compile(r'[concrete|wood|stone|tile|plastic|glass|vinyl|metal|carpet|stainless steel|paint|cinder blocks|hay bales|stucco|adobe]'))

slots.surf_air_cont = Slot(uri=DEFAULT_.surf_air_cont, name="surf_air_cont", curie=DEFAULT_.curie('surf_air_cont'),
                   model_uri=DEFAULT_.surf_air_cont, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.surf_air_cont],
                   pattern=re.compile(r'[dust|organic matter|particulate matter|volatile organic compounds|biological contaminants|radon|nutrients|biocides]'))

slots.rel_air_humidity = Slot(uri=DEFAULT_.rel_air_humidity, name="rel_air_humidity", curie=DEFAULT_.curie('rel_air_humidity'),
                   model_uri=DEFAULT_.rel_air_humidity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.rel_air_humidity],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.abs_air_humidity = Slot(uri=DEFAULT_.abs_air_humidity, name="abs_air_humidity", curie=DEFAULT_.curie('abs_air_humidity'),
                   model_uri=DEFAULT_.abs_air_humidity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.abs_air_humidity],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.surf_humidity = Slot(uri=DEFAULT_.surf_humidity, name="surf_humidity", curie=DEFAULT_.curie('surf_humidity'),
                   model_uri=DEFAULT_.surf_humidity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.surf_humidity],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.air_temp = Slot(uri=DEFAULT_.air_temp, name="air_temp", curie=DEFAULT_.curie('air_temp'),
                   model_uri=DEFAULT_.air_temp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.air_temp],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.surf_temp = Slot(uri=DEFAULT_.surf_temp, name="surf_temp", curie=DEFAULT_.curie('surf_temp'),
                   model_uri=DEFAULT_.surf_temp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.surf_temp],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.surf_moisture_ph = Slot(uri=DEFAULT_.surf_moisture_ph, name="surf_moisture_ph", curie=DEFAULT_.curie('surf_moisture_ph'),
                   model_uri=DEFAULT_.surf_moisture_ph, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.surf_moisture_ph],
                   pattern=re.compile(r'\d+[.\d+]'))

slots.build_occup_type = Slot(uri=DEFAULT_.build_occup_type, name="build_occup_type", curie=DEFAULT_.curie('build_occup_type'),
                   model_uri=DEFAULT_.build_occup_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.build_occup_type],
                   pattern=re.compile(r'[office|market|restaurant|residence|school|residential|commercial|low rise|high rise|wood framed|office|health care|school|airport|sports complex]'))

slots.surf_moisture = Slot(uri=DEFAULT_.surf_moisture, name="surf_moisture", curie=DEFAULT_.curie('surf_moisture'),
                   model_uri=DEFAULT_.surf_moisture, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.surf_moisture],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.dew_point = Slot(uri=DEFAULT_.dew_point, name="dew_point", curie=DEFAULT_.curie('dew_point'),
                   model_uri=DEFAULT_.dew_point, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.dew_point],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.indoor_space = Slot(uri=DEFAULT_.indoor_space, name="indoor_space", curie=DEFAULT_.curie('indoor_space'),
                   model_uri=DEFAULT_.indoor_space, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.indoor_space],
                   pattern=re.compile(r'[bedroom|office|bathroom|foyer|kitchen|locker room|hallway|elevator]'))

slots.indoor_surf = Slot(uri=DEFAULT_.indoor_surf, name="indoor_surf", curie=DEFAULT_.curie('indoor_surf'),
                   model_uri=DEFAULT_.indoor_surf, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.indoor_surf],
                   pattern=re.compile(r'[counter top|window|wall|cabinet|ceiling|door|shelving|vent cover]'))

slots.filter_type = Slot(uri=DEFAULT_.filter_type, name="filter_type", curie=DEFAULT_.curie('filter_type'),
                   model_uri=DEFAULT_.filter_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.filter_type],
                   pattern=re.compile(r'[particulate air filter|chemical air filter|low\-MERV pleated media|HEPA|electrostatic|gas\-phase or ultraviolet air treatments]'))

slots.heat_cool_type = Slot(uri=DEFAULT_.heat_cool_type, name="heat_cool_type", curie=DEFAULT_.curie('heat_cool_type'),
                   model_uri=DEFAULT_.heat_cool_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.heat_cool_type],
                   pattern=re.compile(r'[radiant system|heat pump|forced air system|steam forced heat|wood stove]'))

slots.substructure_type = Slot(uri=DEFAULT_.substructure_type, name="substructure_type", curie=DEFAULT_.curie('substructure_type'),
                   model_uri=DEFAULT_.substructure_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.substructure_type],
                   pattern=re.compile(r'[crawlspace|slab on grade|basement]'))

slots.building_setting = Slot(uri=DEFAULT_.building_setting, name="building_setting", curie=DEFAULT_.curie('building_setting'),
                   model_uri=DEFAULT_.building_setting, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.building_setting],
                   pattern=re.compile(r'[urban|suburban|exurban|rural]'))

slots.light_type = Slot(uri=DEFAULT_.light_type, name="light_type", curie=DEFAULT_.curie('light_type'),
                   model_uri=DEFAULT_.light_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.light_type],
                   pattern=re.compile(r'[natural light|electric light|desk lamp|flourescent lights|natural light|none]'))

slots.samp_sort_meth = Slot(uri=DEFAULT_.samp_sort_meth, name="samp_sort_meth", curie=DEFAULT_.curie('samp_sort_meth'),
                   model_uri=DEFAULT_.samp_sort_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_sort_meth])

slots.space_typ_state = Slot(uri=DEFAULT_.space_typ_state, name="space_typ_state", curie=DEFAULT_.curie('space_typ_state'),
                   model_uri=DEFAULT_.space_typ_state, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.space_typ_state],
                   pattern=re.compile(r'[typically occupied|typically unoccupied]'))

slots.typ_occup_density = Slot(uri=DEFAULT_.typ_occup_density, name="typ_occup_density", curie=DEFAULT_.curie('typ_occup_density'),
                   model_uri=DEFAULT_.typ_occup_density, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.typ_occup_density],
                   pattern=re.compile(r'\d+[.\d+]'))

slots.occup_samp = Slot(uri=DEFAULT_.occup_samp, name="occup_samp", curie=DEFAULT_.curie('occup_samp'),
                   model_uri=DEFAULT_.occup_samp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.occup_samp])

slots.occup_density_samp = Slot(uri=DEFAULT_.occup_density_samp, name="occup_density_samp", curie=DEFAULT_.curie('occup_density_samp'),
                   model_uri=DEFAULT_.occup_density_samp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.occup_density_samp],
                   pattern=re.compile(r'\d+[.\d+]'))

slots.address = Slot(uri=DEFAULT_.address, name="address", curie=DEFAULT_.curie('address'),
                   model_uri=DEFAULT_.address, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.address])

slots.adj_room = Slot(uri=DEFAULT_.adj_room, name="adj_room", curie=DEFAULT_.curie('adj_room'),
                   model_uri=DEFAULT_.adj_room, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.adj_room])

slots.aero_struc = Slot(uri=DEFAULT_.aero_struc, name="aero_struc", curie=DEFAULT_.curie('aero_struc'),
                   model_uri=DEFAULT_.aero_struc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.aero_struc],
                   pattern=re.compile(r'[plane|glider]'))

slots.amount_light = Slot(uri=DEFAULT_.amount_light, name="amount_light", curie=DEFAULT_.curie('amount_light'),
                   model_uri=DEFAULT_.amount_light, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.amount_light],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.arch_struc = Slot(uri=DEFAULT_.arch_struc, name="arch_struc", curie=DEFAULT_.curie('arch_struc'),
                   model_uri=DEFAULT_.arch_struc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.arch_struc],
                   pattern=re.compile(r'[building|shed|home]'))

slots.avg_occup = Slot(uri=DEFAULT_.avg_occup, name="avg_occup", curie=DEFAULT_.curie('avg_occup'),
                   model_uri=DEFAULT_.avg_occup, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.avg_occup],
                   pattern=re.compile(r'\d+[.\d+]'))

slots.avg_dew_point = Slot(uri=DEFAULT_.avg_dew_point, name="avg_dew_point", curie=DEFAULT_.curie('avg_dew_point'),
                   model_uri=DEFAULT_.avg_dew_point, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.avg_dew_point],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.avg_temp = Slot(uri=DEFAULT_.avg_temp, name="avg_temp", curie=DEFAULT_.curie('avg_temp'),
                   model_uri=DEFAULT_.avg_temp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.avg_temp],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.bathroom_count = Slot(uri=DEFAULT_.bathroom_count, name="bathroom_count", curie=DEFAULT_.curie('bathroom_count'),
                   model_uri=DEFAULT_.bathroom_count, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.bathroom_count])

slots.bedroom_count = Slot(uri=DEFAULT_.bedroom_count, name="bedroom_count", curie=DEFAULT_.curie('bedroom_count'),
                   model_uri=DEFAULT_.bedroom_count, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.bedroom_count])

slots.built_struc_age = Slot(uri=DEFAULT_.built_struc_age, name="built_struc_age", curie=DEFAULT_.curie('built_struc_age'),
                   model_uri=DEFAULT_.built_struc_age, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.built_struc_age],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.built_struc_set = Slot(uri=DEFAULT_.built_struc_set, name="built_struc_set", curie=DEFAULT_.curie('built_struc_set'),
                   model_uri=DEFAULT_.built_struc_set, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.built_struc_set],
                   pattern=re.compile(r'[urban|rural]'))

slots.built_struc_type = Slot(uri=DEFAULT_.built_struc_type, name="built_struc_type", curie=DEFAULT_.curie('built_struc_type'),
                   model_uri=DEFAULT_.built_struc_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.built_struc_type])

slots.ceil_area = Slot(uri=DEFAULT_.ceil_area, name="ceil_area", curie=DEFAULT_.curie('ceil_area'),
                   model_uri=DEFAULT_.ceil_area, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.ceil_area],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.ceil_cond = Slot(uri=DEFAULT_.ceil_cond, name="ceil_cond", curie=DEFAULT_.curie('ceil_cond'),
                   model_uri=DEFAULT_.ceil_cond, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ceil_cond],
                   pattern=re.compile(r'[new|visible wear|needs repair|damaged|rupture]'))

slots.ceil_finish_mat = Slot(uri=DEFAULT_.ceil_finish_mat, name="ceil_finish_mat", curie=DEFAULT_.curie('ceil_finish_mat'),
                   model_uri=DEFAULT_.ceil_finish_mat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ceil_finish_mat],
                   pattern=re.compile(r'[drywall|mineral fibre|tiles|PVC|plasterboard|metal|fiberglass|stucco|mineral wool\/calcium silicate|wood]'))

slots.ceil_water_mold = Slot(uri=DEFAULT_.ceil_water_mold, name="ceil_water_mold", curie=DEFAULT_.curie('ceil_water_mold'),
                   model_uri=DEFAULT_.ceil_water_mold, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ceil_water_mold],
                   pattern=re.compile(r'[presence of mold visible|no presence of mold visible]'))

slots.ceil_struc = Slot(uri=DEFAULT_.ceil_struc, name="ceil_struc", curie=DEFAULT_.curie('ceil_struc'),
                   model_uri=DEFAULT_.ceil_struc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ceil_struc],
                   pattern=re.compile(r'[wood frame|concrete]'))

slots.ceil_texture = Slot(uri=DEFAULT_.ceil_texture, name="ceil_texture", curie=DEFAULT_.curie('ceil_texture'),
                   model_uri=DEFAULT_.ceil_texture, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ceil_texture],
                   pattern=re.compile(r'[crows feet|crows\-foot stomp|double skip|hawk and trowel|knockdown|popcorn|orange peel|rosebud stomp|Santa\-Fe texture|skip trowel|smooth|stomp knockdown|swirl]'))

slots.ceil_thermal_mass = Slot(uri=DEFAULT_.ceil_thermal_mass, name="ceil_thermal_mass", curie=DEFAULT_.curie('ceil_thermal_mass'),
                   model_uri=DEFAULT_.ceil_thermal_mass, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.ceil_thermal_mass],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.ceil_type = Slot(uri=DEFAULT_.ceil_type, name="ceil_type", curie=DEFAULT_.curie('ceil_type'),
                   model_uri=DEFAULT_.ceil_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ceil_type],
                   pattern=re.compile(r'[cathedral|dropped|concave|barrel\-shaped|coffered|cove|stretched]'))

slots.cool_syst_id = Slot(uri=DEFAULT_.cool_syst_id, name="cool_syst_id", curie=DEFAULT_.curie('cool_syst_id'),
                   model_uri=DEFAULT_.cool_syst_id, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.cool_syst_id])

slots.date_last_rain = Slot(uri=DEFAULT_.date_last_rain, name="date_last_rain", curie=DEFAULT_.curie('date_last_rain'),
                   model_uri=DEFAULT_.date_last_rain, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.date_last_rain])

slots.build_docs = Slot(uri=DEFAULT_.build_docs, name="build_docs", curie=DEFAULT_.curie('build_docs'),
                   model_uri=DEFAULT_.build_docs, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.build_docs],
                   pattern=re.compile(r'[building information model|commissioning report|complaint logs|contract administration|cost estimate|janitorial schedules or logs|maintenance plans|schedule|sections|shop drawings|submittals|ventilation system|windows] '))

slots.door_size = Slot(uri=DEFAULT_.door_size, name="door_size", curie=DEFAULT_.curie('door_size'),
                   model_uri=DEFAULT_.door_size, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.door_size],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.door_cond = Slot(uri=DEFAULT_.door_cond, name="door_cond", curie=DEFAULT_.curie('door_cond'),
                   model_uri=DEFAULT_.door_cond, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.door_cond],
                   pattern=re.compile(r'[damaged|needs repair|new|rupture|visible wear]'))

slots.door_direct = Slot(uri=DEFAULT_.door_direct, name="door_direct", curie=DEFAULT_.curie('door_direct'),
                   model_uri=DEFAULT_.door_direct, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.door_direct],
                   pattern=re.compile(r'[inward|outward|sideways]'))

slots.door_loc = Slot(uri=DEFAULT_.door_loc, name="door_loc", curie=DEFAULT_.curie('door_loc'),
                   model_uri=DEFAULT_.door_loc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.door_loc],
                   pattern=re.compile(r'[north|south|east|west]'))

slots.door_mat = Slot(uri=DEFAULT_.door_mat, name="door_mat", curie=DEFAULT_.curie('door_mat'),
                   model_uri=DEFAULT_.door_mat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.door_mat],
                   pattern=re.compile(r'[aluminum|cellular PVC|engineered plastic|fiberboard|fiberglass|metal|thermoplastic alloy|vinyl|wood|wood\/plastic composite]'))

slots.door_move = Slot(uri=DEFAULT_.door_move, name="door_move", curie=DEFAULT_.curie('door_move'),
                   model_uri=DEFAULT_.door_move, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.door_move],
                   pattern=re.compile(r'[collapsible|folding|revolving|rolling shutter|sliding|swinging] '))

slots.door_water_mold = Slot(uri=DEFAULT_.door_water_mold, name="door_water_mold", curie=DEFAULT_.curie('door_water_mold'),
                   model_uri=DEFAULT_.door_water_mold, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.door_water_mold],
                   pattern=re.compile(r'[presence of mold visible|no presence of mold visible]'))

slots.door_type = Slot(uri=DEFAULT_.door_type, name="door_type", curie=DEFAULT_.curie('door_type'),
                   model_uri=DEFAULT_.door_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.door_type],
                   pattern=re.compile(r'[composite|metal|wooden]'))

slots.door_comp_type = Slot(uri=DEFAULT_.door_comp_type, name="door_comp_type", curie=DEFAULT_.curie('door_comp_type'),
                   model_uri=DEFAULT_.door_comp_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.door_comp_type],
                   pattern=re.compile(r'[metal covered|revolving|sliding|telescopic]'))

slots.door_type_metal = Slot(uri=DEFAULT_.door_type_metal, name="door_type_metal", curie=DEFAULT_.curie('door_type_metal'),
                   model_uri=DEFAULT_.door_type_metal, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.door_type_metal],
                   pattern=re.compile(r'[collapsible|corrugated steel|hollow|rolling shutters|steel plate]'))

slots.door_type_wood = Slot(uri=DEFAULT_.door_type_wood, name="door_type_wood", curie=DEFAULT_.curie('door_type_wood'),
                   model_uri=DEFAULT_.door_type_wood, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.door_type_wood],
                   pattern=re.compile(r'[bettened and ledged|battened|ledged and braced|battened|ledged and framed|battened|ledged, braced and frame|framed and paneled|glashed or sash|flush|louvered|wire gauged]'))

slots.drawings = Slot(uri=DEFAULT_.drawings, name="drawings", curie=DEFAULT_.curie('drawings'),
                   model_uri=DEFAULT_.drawings, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.drawings],
                   pattern=re.compile(r'[operation|as built|construction|bid|design|building navigation map|diagram|sketch]'))

slots.elevator = Slot(uri=DEFAULT_.elevator, name="elevator", curie=DEFAULT_.curie('elevator'),
                   model_uri=DEFAULT_.elevator, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.elevator])

slots.escalator = Slot(uri=DEFAULT_.escalator, name="escalator", curie=DEFAULT_.curie('escalator'),
                   model_uri=DEFAULT_.escalator, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.escalator])

slots.exp_duct = Slot(uri=DEFAULT_.exp_duct, name="exp_duct", curie=DEFAULT_.curie('exp_duct'),
                   model_uri=DEFAULT_.exp_duct, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.exp_duct],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.exp_pipe = Slot(uri=DEFAULT_.exp_pipe, name="exp_pipe", curie=DEFAULT_.curie('exp_pipe'),
                   model_uri=DEFAULT_.exp_pipe, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.exp_pipe])

slots.ext_door = Slot(uri=DEFAULT_.ext_door, name="ext_door", curie=DEFAULT_.curie('ext_door'),
                   model_uri=DEFAULT_.ext_door, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ext_door])

slots.fireplace_type = Slot(uri=DEFAULT_.fireplace_type, name="fireplace_type", curie=DEFAULT_.curie('fireplace_type'),
                   model_uri=DEFAULT_.fireplace_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.fireplace_type],
                   pattern=re.compile(r'[gas burning|wood burning]'))

slots.floor_age = Slot(uri=DEFAULT_.floor_age, name="floor_age", curie=DEFAULT_.curie('floor_age'),
                   model_uri=DEFAULT_.floor_age, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.floor_age],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.floor_area = Slot(uri=DEFAULT_.floor_area, name="floor_area", curie=DEFAULT_.curie('floor_area'),
                   model_uri=DEFAULT_.floor_area, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.floor_area],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.floor_cond = Slot(uri=DEFAULT_.floor_cond, name="floor_cond", curie=DEFAULT_.curie('floor_cond'),
                   model_uri=DEFAULT_.floor_cond, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.floor_cond],
                   pattern=re.compile(r'[new|visible wear|needs repair|damaged|rupture]'))

slots.floor_count = Slot(uri=DEFAULT_.floor_count, name="floor_count", curie=DEFAULT_.curie('floor_count'),
                   model_uri=DEFAULT_.floor_count, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.floor_count])

slots.floor_finish_mat = Slot(uri=DEFAULT_.floor_finish_mat, name="floor_finish_mat", curie=DEFAULT_.curie('floor_finish_mat'),
                   model_uri=DEFAULT_.floor_finish_mat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.floor_finish_mat],
                   pattern=re.compile(r'[tile|wood strip or parquet|carpet|rug|laminate wood|lineoleum|vinyl composition tile|sheet vinyl|stone|bamboo|cork|terrazo|concrete|none;specify unfinished|sealed|clear finish|paint]'))

slots.floor_water_mold = Slot(uri=DEFAULT_.floor_water_mold, name="floor_water_mold", curie=DEFAULT_.curie('floor_water_mold'),
                   model_uri=DEFAULT_.floor_water_mold, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.floor_water_mold],
                   pattern=re.compile(r'[mold odor|wet floor|water stains|wall discoloration|floor discoloration|ceiling discoloration|peeling paint or wallpaper|bulging walls|condensation]'))

slots.floor_struc = Slot(uri=DEFAULT_.floor_struc, name="floor_struc", curie=DEFAULT_.curie('floor_struc'),
                   model_uri=DEFAULT_.floor_struc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.floor_struc],
                   pattern=re.compile(r'[balcony|floating floor|glass floor|raised floor|sprung floor|wood\-framed|concrete]'))

slots.floor_thermal_mass = Slot(uri=DEFAULT_.floor_thermal_mass, name="floor_thermal_mass", curie=DEFAULT_.curie('floor_thermal_mass'),
                   model_uri=DEFAULT_.floor_thermal_mass, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.floor_thermal_mass],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.freq_clean = Slot(uri=DEFAULT_.freq_clean, name="freq_clean", curie=DEFAULT_.curie('freq_clean'),
                   model_uri=DEFAULT_.freq_clean, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.freq_clean])

slots.freq_cook = Slot(uri=DEFAULT_.freq_cook, name="freq_cook", curie=DEFAULT_.curie('freq_cook'),
                   model_uri=DEFAULT_.freq_cook, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.freq_cook])

slots.furniture = Slot(uri=DEFAULT_.furniture, name="furniture", curie=DEFAULT_.curie('furniture'),
                   model_uri=DEFAULT_.furniture, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.furniture],
                   pattern=re.compile(r'[cabinet|chair|desks]'))

slots.gender_restroom = Slot(uri=DEFAULT_.gender_restroom, name="gender_restroom", curie=DEFAULT_.curie('gender_restroom'),
                   model_uri=DEFAULT_.gender_restroom, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.gender_restroom],
                   pattern=re.compile(r'[male|female]'))

slots.hall_count = Slot(uri=DEFAULT_.hall_count, name="hall_count", curie=DEFAULT_.curie('hall_count'),
                   model_uri=DEFAULT_.hall_count, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.hall_count])

slots.handidness = Slot(uri=DEFAULT_.handidness, name="handidness", curie=DEFAULT_.curie('handidness'),
                   model_uri=DEFAULT_.handidness, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.handidness],
                   pattern=re.compile(r'[ambidexterity|left handedness|mixed\-handedness|right handedness]'))

slots.heat_deliv_loc = Slot(uri=DEFAULT_.heat_deliv_loc, name="heat_deliv_loc", curie=DEFAULT_.curie('heat_deliv_loc'),
                   model_uri=DEFAULT_.heat_deliv_loc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.heat_deliv_loc],
                   pattern=re.compile(r'[north|south|east|west]'))

slots.heat_system_deliv_meth = Slot(uri=DEFAULT_.heat_system_deliv_meth, name="heat_system_deliv_meth", curie=DEFAULT_.curie('heat_system_deliv_meth'),
                   model_uri=DEFAULT_.heat_system_deliv_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.heat_system_deliv_meth],
                   pattern=re.compile(r'[conductive|radiant]'))

slots.heat_system_id = Slot(uri=DEFAULT_.heat_system_id, name="heat_system_id", curie=DEFAULT_.curie('heat_system_id'),
                   model_uri=DEFAULT_.heat_system_id, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.heat_system_id])

slots.height_carper_fiber = Slot(uri=DEFAULT_.height_carper_fiber, name="height_carper_fiber", curie=DEFAULT_.curie('height_carper_fiber'),
                   model_uri=DEFAULT_.height_carper_fiber, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.height_carper_fiber],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.inside_lux = Slot(uri=DEFAULT_.inside_lux, name="inside_lux", curie=DEFAULT_.curie('inside_lux'),
                   model_uri=DEFAULT_.inside_lux, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.inside_lux],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.int_wall_cond = Slot(uri=DEFAULT_.int_wall_cond, name="int_wall_cond", curie=DEFAULT_.curie('int_wall_cond'),
                   model_uri=DEFAULT_.int_wall_cond, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.int_wall_cond],
                   pattern=re.compile(r'[new|visible wear|needs repair|damaged|rupture]'))

slots.last_clean = Slot(uri=DEFAULT_.last_clean, name="last_clean", curie=DEFAULT_.curie('last_clean'),
                   model_uri=DEFAULT_.last_clean, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.last_clean])

slots.max_occup = Slot(uri=DEFAULT_.max_occup, name="max_occup", curie=DEFAULT_.curie('max_occup'),
                   model_uri=DEFAULT_.max_occup, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.max_occup])

slots.mech_struc = Slot(uri=DEFAULT_.mech_struc, name="mech_struc", curie=DEFAULT_.curie('mech_struc'),
                   model_uri=DEFAULT_.mech_struc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.mech_struc],
                   pattern=re.compile(r'[subway|coach|carriage|elevator|escalator|boat|train|car|bus]'))

slots.number_plants = Slot(uri=DEFAULT_.number_plants, name="number_plants", curie=DEFAULT_.curie('number_plants'),
                   model_uri=DEFAULT_.number_plants, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.number_plants])

slots.number_pets = Slot(uri=DEFAULT_.number_pets, name="number_pets", curie=DEFAULT_.curie('number_pets'),
                   model_uri=DEFAULT_.number_pets, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.number_pets])

slots.number_resident = Slot(uri=DEFAULT_.number_resident, name="number_resident", curie=DEFAULT_.curie('number_resident'),
                   model_uri=DEFAULT_.number_resident, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.number_resident])

slots.occup_document = Slot(uri=DEFAULT_.occup_document, name="occup_document", curie=DEFAULT_.curie('occup_document'),
                   model_uri=DEFAULT_.occup_document, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.occup_document],
                   pattern=re.compile(r'[automated count|estimate|manual count|videos]'))

slots.ext_wall_orient = Slot(uri=DEFAULT_.ext_wall_orient, name="ext_wall_orient", curie=DEFAULT_.curie('ext_wall_orient'),
                   model_uri=DEFAULT_.ext_wall_orient, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ext_wall_orient],
                   pattern=re.compile(r'[north|south|east|west|northeast|southeast|southwest|northwest]'))

slots.ext_window_orient = Slot(uri=DEFAULT_.ext_window_orient, name="ext_window_orient", curie=DEFAULT_.curie('ext_window_orient'),
                   model_uri=DEFAULT_.ext_window_orient, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ext_window_orient],
                   pattern=re.compile(r'[north|south|east|west|northeast|southeast|southwest|northwest]'))

slots.rel_humidity_out = Slot(uri=DEFAULT_.rel_humidity_out, name="rel_humidity_out", curie=DEFAULT_.curie('rel_humidity_out'),
                   model_uri=DEFAULT_.rel_humidity_out, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.rel_humidity_out],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.pres_animal = Slot(uri=DEFAULT_.pres_animal, name="pres_animal", curie=DEFAULT_.curie('pres_animal'),
                   model_uri=DEFAULT_.pres_animal, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.pres_animal])

slots.quad_pos = Slot(uri=DEFAULT_.quad_pos, name="quad_pos", curie=DEFAULT_.curie('quad_pos'),
                   model_uri=DEFAULT_.quad_pos, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.quad_pos],
                   pattern=re.compile(r'[North side|West side|South side|East side]'))

slots.rel_samp_loc = Slot(uri=DEFAULT_.rel_samp_loc, name="rel_samp_loc", curie=DEFAULT_.curie('rel_samp_loc'),
                   model_uri=DEFAULT_.rel_samp_loc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.rel_samp_loc],
                   pattern=re.compile(r'[edge of car|center of car|under a seat]'))

slots.room_air_exch_rate = Slot(uri=DEFAULT_.room_air_exch_rate, name="room_air_exch_rate", curie=DEFAULT_.curie('room_air_exch_rate'),
                   model_uri=DEFAULT_.room_air_exch_rate, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.room_air_exch_rate],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.room_architec_element = Slot(uri=DEFAULT_.room_architec_element, name="room_architec_element", curie=DEFAULT_.curie('room_architec_element'),
                   model_uri=DEFAULT_.room_architec_element, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_architec_element])

slots.room_condt = Slot(uri=DEFAULT_.room_condt, name="room_condt", curie=DEFAULT_.curie('room_condt'),
                   model_uri=DEFAULT_.room_condt, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_condt],
                   pattern=re.compile(r'[new|visible wear|needs repair|damaged|rupture|visible signs of mold\/mildew]'))

slots.room_count = Slot(uri=DEFAULT_.room_count, name="room_count", curie=DEFAULT_.curie('room_count'),
                   model_uri=DEFAULT_.room_count, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_count])

slots.room_dim = Slot(uri=DEFAULT_.room_dim, name="room_dim", curie=DEFAULT_.curie('room_dim'),
                   model_uri=DEFAULT_.room_dim, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.room_dim])

slots.room_door_dist = Slot(uri=DEFAULT_.room_door_dist, name="room_door_dist", curie=DEFAULT_.curie('room_door_dist'),
                   model_uri=DEFAULT_.room_door_dist, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.room_door_dist])

slots.room_loc = Slot(uri=DEFAULT_.room_loc, name="room_loc", curie=DEFAULT_.curie('room_loc'),
                   model_uri=DEFAULT_.room_loc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_loc],
                   pattern=re.compile(r'[corner room|interior room|exterior wall]'))

slots.room_moist_damage_hist = Slot(uri=DEFAULT_.room_moist_damage_hist, name="room_moist_damage_hist", curie=DEFAULT_.curie('room_moist_damage_hist'),
                   model_uri=DEFAULT_.room_moist_damage_hist, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_moist_damage_hist])

slots.room_net_area = Slot(uri=DEFAULT_.room_net_area, name="room_net_area", curie=DEFAULT_.curie('room_net_area'),
                   model_uri=DEFAULT_.room_net_area, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.room_net_area])

slots.room_occup = Slot(uri=DEFAULT_.room_occup, name="room_occup", curie=DEFAULT_.curie('room_occup'),
                   model_uri=DEFAULT_.room_occup, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.room_occup])

slots.room_samp_pos = Slot(uri=DEFAULT_.room_samp_pos, name="room_samp_pos", curie=DEFAULT_.curie('room_samp_pos'),
                   model_uri=DEFAULT_.room_samp_pos, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_samp_pos],
                   pattern=re.compile(r'[north corner|south corner|west corner|east corner|northeast corner|northwest corner|southeast corner|southwest corner|center]'))

slots.room_type = Slot(uri=DEFAULT_.room_type, name="room_type", curie=DEFAULT_.curie('room_type'),
                   model_uri=DEFAULT_.room_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_type],
                   pattern=re.compile(r'[attic|bathroom|closet|conference room|elevator|examining room|hallway|kitchen|mail room|private office|open office|stairwell|,restroom|lobby|vestibule|mechanical or electrical room|data center|laboratory_wet|laboratory_dry|gymnasium|natatorium|auditorium|lockers|cafe|warehouse]'))

slots.room_vol = Slot(uri=DEFAULT_.room_vol, name="room_vol", curie=DEFAULT_.curie('room_vol'),
                   model_uri=DEFAULT_.room_vol, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.room_vol])

slots.room_window_count = Slot(uri=DEFAULT_.room_window_count, name="room_window_count", curie=DEFAULT_.curie('room_window_count'),
                   model_uri=DEFAULT_.room_window_count, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_window_count])

slots.room_connected = Slot(uri=DEFAULT_.room_connected, name="room_connected", curie=DEFAULT_.curie('room_connected'),
                   model_uri=DEFAULT_.room_connected, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_connected],
                   pattern=re.compile(r'[attic|bathroom|closet|conference room|elevator|examining room|hallway|kitchen|mail room|office|stairwell]'))

slots.room_hallway = Slot(uri=DEFAULT_.room_hallway, name="room_hallway", curie=DEFAULT_.curie('room_hallway'),
                   model_uri=DEFAULT_.room_hallway, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_hallway])

slots.room_door_share = Slot(uri=DEFAULT_.room_door_share, name="room_door_share", curie=DEFAULT_.curie('room_door_share'),
                   model_uri=DEFAULT_.room_door_share, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_door_share])

slots.room_wall_share = Slot(uri=DEFAULT_.room_wall_share, name="room_wall_share", curie=DEFAULT_.curie('room_wall_share'),
                   model_uri=DEFAULT_.room_wall_share, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_wall_share])

slots.samp_weather = Slot(uri=DEFAULT_.samp_weather, name="samp_weather", curie=DEFAULT_.curie('samp_weather'),
                   model_uri=DEFAULT_.samp_weather, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_weather],
                   pattern=re.compile(r'[clear sky|cloudy|foggy|hail|rain|snow|sleet|sunny|windy]'))

slots.samp_floor = Slot(uri=DEFAULT_.samp_floor, name="samp_floor", curie=DEFAULT_.curie('samp_floor'),
                   model_uri=DEFAULT_.samp_floor, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_floor])

slots.samp_room_id = Slot(uri=DEFAULT_.samp_room_id, name="samp_room_id", curie=DEFAULT_.curie('samp_room_id'),
                   model_uri=DEFAULT_.samp_room_id, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_room_id])

slots.samp_time_out = Slot(uri=DEFAULT_.samp_time_out, name="samp_time_out", curie=DEFAULT_.curie('samp_time_out'),
                   model_uri=DEFAULT_.samp_time_out, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_time_out],
                   pattern=re.compile(r'\d+[.\d+]'))

slots.season = Slot(uri=DEFAULT_.season, name="season", curie=DEFAULT_.curie('season'),
                   model_uri=DEFAULT_.season, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.season],
                   pattern=re.compile(r'[Spring|Summer|Fall|Winter]'))

slots.season_use = Slot(uri=DEFAULT_.season_use, name="season_use", curie=DEFAULT_.curie('season_use'),
                   model_uri=DEFAULT_.season_use, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.season_use],
                   pattern=re.compile(r'[Spring|Summer|Fall|Winter]'))

slots.shading_device_cond = Slot(uri=DEFAULT_.shading_device_cond, name="shading_device_cond", curie=DEFAULT_.curie('shading_device_cond'),
                   model_uri=DEFAULT_.shading_device_cond, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.shading_device_cond],
                   pattern=re.compile(r'[damaged|needs repair|new|rupture|visible wear]'))

slots.shading_device_loc = Slot(uri=DEFAULT_.shading_device_loc, name="shading_device_loc", curie=DEFAULT_.curie('shading_device_loc'),
                   model_uri=DEFAULT_.shading_device_loc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.shading_device_loc],
                   pattern=re.compile(r'[exterior|interior]'))

slots.shading_device_mat = Slot(uri=DEFAULT_.shading_device_mat, name="shading_device_mat", curie=DEFAULT_.curie('shading_device_mat'),
                   model_uri=DEFAULT_.shading_device_mat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.shading_device_mat])

slots.shading_device_water_mold = Slot(uri=DEFAULT_.shading_device_water_mold, name="shading_device_water_mold", curie=DEFAULT_.curie('shading_device_water_mold'),
                   model_uri=DEFAULT_.shading_device_water_mold, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.shading_device_water_mold],
                   pattern=re.compile(r'[presence of mold visible|no presence of mold visible]'))

slots.shading_device_type = Slot(uri=DEFAULT_.shading_device_type, name="shading_device_type", curie=DEFAULT_.curie('shading_device_type'),
                   model_uri=DEFAULT_.shading_device_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.shading_device_type],
                   pattern=re.compile(r'[bahama shutters|exterior roll blind|gambrel awning|hood awning|porchroller awning|sarasota shutters|slatted aluminum|solid aluminum awning|sun screen|tree|trellis|venetian awning]'))

slots.specific_humidity = Slot(uri=DEFAULT_.specific_humidity, name="specific_humidity", curie=DEFAULT_.curie('specific_humidity'),
                   model_uri=DEFAULT_.specific_humidity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.specific_humidity],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.specific = Slot(uri=DEFAULT_.specific, name="specific", curie=DEFAULT_.curie('specific'),
                   model_uri=DEFAULT_.specific, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.specific],
                   pattern=re.compile(r'[operation|as built|construction|bid|design|photos]'))

slots.temp_out = Slot(uri=DEFAULT_.temp_out, name="temp_out", curie=DEFAULT_.curie('temp_out'),
                   model_uri=DEFAULT_.temp_out, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.temp_out],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.train_line = Slot(uri=DEFAULT_.train_line, name="train_line", curie=DEFAULT_.curie('train_line'),
                   model_uri=DEFAULT_.train_line, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.train_line],
                   pattern=re.compile(r'[red|green|orange]'))

slots.train_stat_loc = Slot(uri=DEFAULT_.train_stat_loc, name="train_stat_loc", curie=DEFAULT_.curie('train_stat_loc'),
                   model_uri=DEFAULT_.train_stat_loc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.train_stat_loc],
                   pattern=re.compile(r'[south station above ground|south station underground|south station amtrak|forest hills|riverside]'))

slots.train_stop_loc = Slot(uri=DEFAULT_.train_stop_loc, name="train_stop_loc", curie=DEFAULT_.curie('train_stop_loc'),
                   model_uri=DEFAULT_.train_stop_loc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.train_stop_loc],
                   pattern=re.compile(r'[end|mid|downtown]'))

slots.vis_media = Slot(uri=DEFAULT_.vis_media, name="vis_media", curie=DEFAULT_.curie('vis_media'),
                   model_uri=DEFAULT_.vis_media, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.vis_media],
                   pattern=re.compile(r'[photos|videos|commonly of the building|site context (adjacent buildings, vegetation, terrain, streets)|interiors|equipment|3D scans]'))

slots.wall_area = Slot(uri=DEFAULT_.wall_area, name="wall_area", curie=DEFAULT_.curie('wall_area'),
                   model_uri=DEFAULT_.wall_area, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.wall_area],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.wall_const_type = Slot(uri=DEFAULT_.wall_const_type, name="wall_const_type", curie=DEFAULT_.curie('wall_const_type'),
                   model_uri=DEFAULT_.wall_const_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.wall_const_type],
                   pattern=re.compile(r'[frame construction|joisted masonry|light noncombustible|masonry noncombustible|modified fire resistive|fire resistive]'))

slots.wall_finish_mat = Slot(uri=DEFAULT_.wall_finish_mat, name="wall_finish_mat", curie=DEFAULT_.curie('wall_finish_mat'),
                   model_uri=DEFAULT_.wall_finish_mat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.wall_finish_mat],
                   pattern=re.compile(r'[plaster|gypsum plaster|veneer plaster|gypsum board|tile|terrazzo|stone facing|acoustical treatment|wood|metal|masonry]'))

slots.wall_height = Slot(uri=DEFAULT_.wall_height, name="wall_height", curie=DEFAULT_.curie('wall_height'),
                   model_uri=DEFAULT_.wall_height, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.wall_height],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.wall_loc = Slot(uri=DEFAULT_.wall_loc, name="wall_loc", curie=DEFAULT_.curie('wall_loc'),
                   model_uri=DEFAULT_.wall_loc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.wall_loc],
                   pattern=re.compile(r'[north|south|east|west]'))

slots.wall_water_mold = Slot(uri=DEFAULT_.wall_water_mold, name="wall_water_mold", curie=DEFAULT_.curie('wall_water_mold'),
                   model_uri=DEFAULT_.wall_water_mold, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.wall_water_mold],
                   pattern=re.compile(r'[presence of mold visible|no presence of mold visible]'))

slots.wall_surf_treatment = Slot(uri=DEFAULT_.wall_surf_treatment, name="wall_surf_treatment", curie=DEFAULT_.curie('wall_surf_treatment'),
                   model_uri=DEFAULT_.wall_surf_treatment, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.wall_surf_treatment],
                   pattern=re.compile(r'[painted|wall paper|no treatment|paneling|stucco|fabric]'))

slots.wall_texture = Slot(uri=DEFAULT_.wall_texture, name="wall_texture", curie=DEFAULT_.curie('wall_texture'),
                   model_uri=DEFAULT_.wall_texture, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.wall_texture],
                   pattern=re.compile(r'[crows feet|crows\-foot stomp|double skip|hawk and trowel|knockdown|popcorn|orange peel|rosebud stomp|Santa\-Fe texture|skip trowel|smooth|stomp knockdown|swirl]'))

slots.wall_thermal_mass = Slot(uri=DEFAULT_.wall_thermal_mass, name="wall_thermal_mass", curie=DEFAULT_.curie('wall_thermal_mass'),
                   model_uri=DEFAULT_.wall_thermal_mass, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.wall_thermal_mass],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.water_feat_size = Slot(uri=DEFAULT_.water_feat_size, name="water_feat_size", curie=DEFAULT_.curie('water_feat_size'),
                   model_uri=DEFAULT_.water_feat_size, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.water_feat_size],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.water_feat_type = Slot(uri=DEFAULT_.water_feat_type, name="water_feat_type", curie=DEFAULT_.curie('water_feat_type'),
                   model_uri=DEFAULT_.water_feat_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.water_feat_type],
                   pattern=re.compile(r'[fountain|pool|standing feature|stream|waterfall]'))

slots.weekday = Slot(uri=DEFAULT_.weekday, name="weekday", curie=DEFAULT_.curie('weekday'),
                   model_uri=DEFAULT_.weekday, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.weekday],
                   pattern=re.compile(r'[Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday]'))

slots.window_size = Slot(uri=DEFAULT_.window_size, name="window_size", curie=DEFAULT_.curie('window_size'),
                   model_uri=DEFAULT_.window_size, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.window_size],
                   pattern=re.compile(r'\d+[.\d+] \S+ x \d+[.\d+] \S+'))

slots.window_cond = Slot(uri=DEFAULT_.window_cond, name="window_cond", curie=DEFAULT_.curie('window_cond'),
                   model_uri=DEFAULT_.window_cond, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.window_cond],
                   pattern=re.compile(r'[damaged|needs repair|new|rupture|visible wear]'))

slots.window_cover = Slot(uri=DEFAULT_.window_cover, name="window_cover", curie=DEFAULT_.curie('window_cover'),
                   model_uri=DEFAULT_.window_cover, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.window_cover],
                   pattern=re.compile(r'[blinds|curtains|none]'))

slots.window_horiz_pos = Slot(uri=DEFAULT_.window_horiz_pos, name="window_horiz_pos", curie=DEFAULT_.curie('window_horiz_pos'),
                   model_uri=DEFAULT_.window_horiz_pos, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.window_horiz_pos],
                   pattern=re.compile(r'[left|middle|right]'))

slots.window_loc = Slot(uri=DEFAULT_.window_loc, name="window_loc", curie=DEFAULT_.curie('window_loc'),
                   model_uri=DEFAULT_.window_loc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.window_loc],
                   pattern=re.compile(r'[north|south|east|west]'))

slots.window_mat = Slot(uri=DEFAULT_.window_mat, name="window_mat", curie=DEFAULT_.curie('window_mat'),
                   model_uri=DEFAULT_.window_mat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.window_mat],
                   pattern=re.compile(r'[clad|fiberglass|metal|vinyl|wood]'))

slots.window_open_freq = Slot(uri=DEFAULT_.window_open_freq, name="window_open_freq", curie=DEFAULT_.curie('window_open_freq'),
                   model_uri=DEFAULT_.window_open_freq, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.window_open_freq])

slots.window_water_mold = Slot(uri=DEFAULT_.window_water_mold, name="window_water_mold", curie=DEFAULT_.curie('window_water_mold'),
                   model_uri=DEFAULT_.window_water_mold, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.window_water_mold],
                   pattern=re.compile(r'[presence of mold visible|no presence of mold visible]'))

slots.window_status = Slot(uri=DEFAULT_.window_status, name="window_status", curie=DEFAULT_.curie('window_status'),
                   model_uri=DEFAULT_.window_status, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.window_status],
                   pattern=re.compile(r'[closed|open]'))

slots.window_type = Slot(uri=DEFAULT_.window_type, name="window_type", curie=DEFAULT_.curie('window_type'),
                   model_uri=DEFAULT_.window_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.window_type],
                   pattern=re.compile(r'[single\-hung sash window|horizontal sash window|fixed window] '))

slots.window_vert_pos = Slot(uri=DEFAULT_.window_vert_pos, name="window_vert_pos", curie=DEFAULT_.curie('window_vert_pos'),
                   model_uri=DEFAULT_.window_vert_pos, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.window_vert_pos],
                   pattern=re.compile(r'[bottom|middle|top|low|middle|high]'))

slots.ances_data = Slot(uri=DEFAULT_.ances_data, name="ances_data", curie=DEFAULT_.curie('ances_data'),
                   model_uri=DEFAULT_.ances_data, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ances_data])

slots.biol_stat = Slot(uri=DEFAULT_.biol_stat, name="biol_stat", curie=DEFAULT_.curie('biol_stat'),
                   model_uri=DEFAULT_.biol_stat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.biol_stat],
                   pattern=re.compile(r'[wild|natural|semi\-natural|inbred line|breeder\'s line|hybrid|clonal selection|mutant]'))

slots.genetic_mod = Slot(uri=DEFAULT_.genetic_mod, name="genetic_mod", curie=DEFAULT_.curie('genetic_mod'),
                   model_uri=DEFAULT_.genetic_mod, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.genetic_mod])

slots.host_common_name = Slot(uri=DEFAULT_.host_common_name, name="host_common_name", curie=DEFAULT_.curie('host_common_name'),
                   model_uri=DEFAULT_.host_common_name, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_common_name])

slots.samp_capt_status = Slot(uri=DEFAULT_.samp_capt_status, name="samp_capt_status", curie=DEFAULT_.curie('samp_capt_status'),
                   model_uri=DEFAULT_.samp_capt_status, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_capt_status],
                   pattern=re.compile(r'[active surveillance in response to an outbreak|active surveillance not initiated by an outbreak|farm sample|market sample|other]'))

slots.samp_dis_stage = Slot(uri=DEFAULT_.samp_dis_stage, name="samp_dis_stage", curie=DEFAULT_.curie('samp_dis_stage'),
                   model_uri=DEFAULT_.samp_dis_stage, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_dis_stage])

slots.host_taxid = Slot(uri=DEFAULT_.host_taxid, name="host_taxid", curie=DEFAULT_.curie('host_taxid'),
                   model_uri=DEFAULT_.host_taxid, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_taxid])

slots.host_subject_id = Slot(uri=DEFAULT_.host_subject_id, name="host_subject_id", curie=DEFAULT_.curie('host_subject_id'),
                   model_uri=DEFAULT_.host_subject_id, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_subject_id])

slots.host_age = Slot(uri=DEFAULT_.host_age, name="host_age", curie=DEFAULT_.curie('host_age'),
                   model_uri=DEFAULT_.host_age, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_age],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.host_life_stage = Slot(uri=DEFAULT_.host_life_stage, name="host_life_stage", curie=DEFAULT_.curie('host_life_stage'),
                   model_uri=DEFAULT_.host_life_stage, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_life_stage])

slots.host_sex = Slot(uri=DEFAULT_.host_sex, name="host_sex", curie=DEFAULT_.curie('host_sex'),
                   model_uri=DEFAULT_.host_sex, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_sex],
                   pattern=re.compile(r'[male|female|neuter|hermaphrodite|not determined]'))

slots.host_disease_stat = Slot(uri=DEFAULT_.host_disease_stat, name="host_disease_stat", curie=DEFAULT_.curie('host_disease_stat'),
                   model_uri=DEFAULT_.host_disease_stat, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.host_disease_stat])

slots.host_body_habitat = Slot(uri=DEFAULT_.host_body_habitat, name="host_body_habitat", curie=DEFAULT_.curie('host_body_habitat'),
                   model_uri=DEFAULT_.host_body_habitat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_body_habitat])

slots.host_body_site = Slot(uri=DEFAULT_.host_body_site, name="host_body_site", curie=DEFAULT_.curie('host_body_site'),
                   model_uri=DEFAULT_.host_body_site, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.host_body_site],
                   pattern=re.compile(r'.* \S+:\S+'))

slots.host_body_product = Slot(uri=DEFAULT_.host_body_product, name="host_body_product", curie=DEFAULT_.curie('host_body_product'),
                   model_uri=DEFAULT_.host_body_product, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.host_body_product],
                   pattern=re.compile(r'.* \S+:\S+'))

slots.host_tot_mass = Slot(uri=DEFAULT_.host_tot_mass, name="host_tot_mass", curie=DEFAULT_.curie('host_tot_mass'),
                   model_uri=DEFAULT_.host_tot_mass, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_tot_mass],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.host_height = Slot(uri=DEFAULT_.host_height, name="host_height", curie=DEFAULT_.curie('host_height'),
                   model_uri=DEFAULT_.host_height, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_height],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.host_length = Slot(uri=DEFAULT_.host_length, name="host_length", curie=DEFAULT_.curie('host_length'),
                   model_uri=DEFAULT_.host_length, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_length],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.host_diet = Slot(uri=DEFAULT_.host_diet, name="host_diet", curie=DEFAULT_.curie('host_diet'),
                   model_uri=DEFAULT_.host_diet, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_diet])

slots.host_last_meal = Slot(uri=DEFAULT_.host_last_meal, name="host_last_meal", curie=DEFAULT_.curie('host_last_meal'),
                   model_uri=DEFAULT_.host_last_meal, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_last_meal])

slots.host_growth_cond = Slot(uri=DEFAULT_.host_growth_cond, name="host_growth_cond", curie=DEFAULT_.curie('host_growth_cond'),
                   model_uri=DEFAULT_.host_growth_cond, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_growth_cond])

slots.host_substrate = Slot(uri=DEFAULT_.host_substrate, name="host_substrate", curie=DEFAULT_.curie('host_substrate'),
                   model_uri=DEFAULT_.host_substrate, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_substrate])

slots.host_family_relationship = Slot(uri=DEFAULT_.host_family_relationship, name="host_family_relationship", curie=DEFAULT_.curie('host_family_relationship'),
                   model_uri=DEFAULT_.host_family_relationship, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_family_relationship])

slots.host_infra_specific_name = Slot(uri=DEFAULT_.host_infra_specific_name, name="host_infra_specific_name", curie=DEFAULT_.curie('host_infra_specific_name'),
                   model_uri=DEFAULT_.host_infra_specific_name, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_infra_specific_name])

slots.host_infra_specific_rank = Slot(uri=DEFAULT_.host_infra_specific_rank, name="host_infra_specific_rank", curie=DEFAULT_.curie('host_infra_specific_rank'),
                   model_uri=DEFAULT_.host_infra_specific_rank, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_infra_specific_rank])

slots.host_genotype = Slot(uri=DEFAULT_.host_genotype, name="host_genotype", curie=DEFAULT_.curie('host_genotype'),
                   model_uri=DEFAULT_.host_genotype, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_genotype])

slots.host_phenotype = Slot(uri=DEFAULT_.host_phenotype, name="host_phenotype", curie=DEFAULT_.curie('host_phenotype'),
                   model_uri=DEFAULT_.host_phenotype, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.host_phenotype],
                   pattern=re.compile(r'.* \S+:\S+'))

slots.host_body_temp = Slot(uri=DEFAULT_.host_body_temp, name="host_body_temp", curie=DEFAULT_.curie('host_body_temp'),
                   model_uri=DEFAULT_.host_body_temp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_body_temp],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.host_dry_mass = Slot(uri=DEFAULT_.host_dry_mass, name="host_dry_mass", curie=DEFAULT_.curie('host_dry_mass'),
                   model_uri=DEFAULT_.host_dry_mass, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_dry_mass],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.host_blood_press_diast = Slot(uri=DEFAULT_.host_blood_press_diast, name="host_blood_press_diast", curie=DEFAULT_.curie('host_blood_press_diast'),
                   model_uri=DEFAULT_.host_blood_press_diast, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_blood_press_diast],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.host_blood_press_syst = Slot(uri=DEFAULT_.host_blood_press_syst, name="host_blood_press_syst", curie=DEFAULT_.curie('host_blood_press_syst'),
                   model_uri=DEFAULT_.host_blood_press_syst, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_blood_press_syst],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.host_color = Slot(uri=DEFAULT_.host_color, name="host_color", curie=DEFAULT_.curie('host_color'),
                   model_uri=DEFAULT_.host_color, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_color])

slots.host_shape = Slot(uri=DEFAULT_.host_shape, name="host_shape", curie=DEFAULT_.curie('host_shape'),
                   model_uri=DEFAULT_.host_shape, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_shape])

slots.gravidity = Slot(uri=DEFAULT_.gravidity, name="gravidity", curie=DEFAULT_.curie('gravidity'),
                   model_uri=DEFAULT_.gravidity, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.gravidity])

slots.ihmc_medication_code = Slot(uri=DEFAULT_.ihmc_medication_code, name="ihmc_medication_code", curie=DEFAULT_.curie('ihmc_medication_code'),
                   model_uri=DEFAULT_.ihmc_medication_code, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ihmc_medication_code])

slots.smoker = Slot(uri=DEFAULT_.smoker, name="smoker", curie=DEFAULT_.curie('smoker'),
                   model_uri=DEFAULT_.smoker, domain=None, range=Optional[Union[dict, BooleanValue]], mappings = [MIXS.smoker],
                   pattern=re.compile(r'[true|false]'))

slots.host_hiv_stat = Slot(uri=DEFAULT_.host_hiv_stat, name="host_hiv_stat", curie=DEFAULT_.curie('host_hiv_stat'),
                   model_uri=DEFAULT_.host_hiv_stat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_hiv_stat],
                   pattern=re.compile(r'[true|false];[true|false]'))

slots.drug_usage = Slot(uri=DEFAULT_.drug_usage, name="drug_usage", curie=DEFAULT_.curie('drug_usage'),
                   model_uri=DEFAULT_.drug_usage, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.drug_usage])

slots.host_body_mass_index = Slot(uri=DEFAULT_.host_body_mass_index, name="host_body_mass_index", curie=DEFAULT_.curie('host_body_mass_index'),
                   model_uri=DEFAULT_.host_body_mass_index, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_body_mass_index],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.diet_last_six_month = Slot(uri=DEFAULT_.diet_last_six_month, name="diet_last_six_month", curie=DEFAULT_.curie('diet_last_six_month'),
                   model_uri=DEFAULT_.diet_last_six_month, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.diet_last_six_month])

slots.weight_loss_3_month = Slot(uri=DEFAULT_.weight_loss_3_month, name="weight_loss_3_month", curie=DEFAULT_.curie('weight_loss_3_month'),
                   model_uri=DEFAULT_.weight_loss_3_month, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.weight_loss_3_month],
                   pattern=re.compile(r'[true|false];\d+[.\d+] \S+'))

slots.ihmc_ethnicity = Slot(uri=DEFAULT_.ihmc_ethnicity, name="ihmc_ethnicity", curie=DEFAULT_.curie('ihmc_ethnicity'),
                   model_uri=DEFAULT_.ihmc_ethnicity, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ihmc_ethnicity])

slots.host_occupation = Slot(uri=DEFAULT_.host_occupation, name="host_occupation", curie=DEFAULT_.curie('host_occupation'),
                   model_uri=DEFAULT_.host_occupation, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_occupation])

slots.pet_farm_animal = Slot(uri=DEFAULT_.pet_farm_animal, name="pet_farm_animal", curie=DEFAULT_.curie('pet_farm_animal'),
                   model_uri=DEFAULT_.pet_farm_animal, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.pet_farm_animal])

slots.travel_out_six_month = Slot(uri=DEFAULT_.travel_out_six_month, name="travel_out_six_month", curie=DEFAULT_.curie('travel_out_six_month'),
                   model_uri=DEFAULT_.travel_out_six_month, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.travel_out_six_month])

slots.twin_sibling = Slot(uri=DEFAULT_.twin_sibling, name="twin_sibling", curie=DEFAULT_.curie('twin_sibling'),
                   model_uri=DEFAULT_.twin_sibling, domain=None, range=Optional[Union[dict, BooleanValue]], mappings = [MIXS.twin_sibling],
                   pattern=re.compile(r'[true|false]'))

slots.medic_hist_perform = Slot(uri=DEFAULT_.medic_hist_perform, name="medic_hist_perform", curie=DEFAULT_.curie('medic_hist_perform'),
                   model_uri=DEFAULT_.medic_hist_perform, domain=None, range=Optional[Union[dict, BooleanValue]], mappings = [MIXS.medic_hist_perform],
                   pattern=re.compile(r'[true|false]'))

slots.study_complt_stat = Slot(uri=DEFAULT_.study_complt_stat, name="study_complt_stat", curie=DEFAULT_.curie('study_complt_stat'),
                   model_uri=DEFAULT_.study_complt_stat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.study_complt_stat],
                   pattern=re.compile(r'[true|false];[adverse event|non\-compliance|lost to follow up|other\-specify]'))

slots.pulmonary_disord = Slot(uri=DEFAULT_.pulmonary_disord, name="pulmonary_disord", curie=DEFAULT_.curie('pulmonary_disord'),
                   model_uri=DEFAULT_.pulmonary_disord, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.pulmonary_disord])

slots.nose_throat_disord = Slot(uri=DEFAULT_.nose_throat_disord, name="nose_throat_disord", curie=DEFAULT_.curie('nose_throat_disord'),
                   model_uri=DEFAULT_.nose_throat_disord, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.nose_throat_disord])

slots.blood_blood_disord = Slot(uri=DEFAULT_.blood_blood_disord, name="blood_blood_disord", curie=DEFAULT_.curie('blood_blood_disord'),
                   model_uri=DEFAULT_.blood_blood_disord, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.blood_blood_disord])

slots.host_pulse = Slot(uri=DEFAULT_.host_pulse, name="host_pulse", curie=DEFAULT_.curie('host_pulse'),
                   model_uri=DEFAULT_.host_pulse, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_pulse],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.gestation_state = Slot(uri=DEFAULT_.gestation_state, name="gestation_state", curie=DEFAULT_.curie('gestation_state'),
                   model_uri=DEFAULT_.gestation_state, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.gestation_state])

slots.maternal_health_stat = Slot(uri=DEFAULT_.maternal_health_stat, name="maternal_health_stat", curie=DEFAULT_.curie('maternal_health_stat'),
                   model_uri=DEFAULT_.maternal_health_stat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.maternal_health_stat])

slots.foetal_health_stat = Slot(uri=DEFAULT_.foetal_health_stat, name="foetal_health_stat", curie=DEFAULT_.curie('foetal_health_stat'),
                   model_uri=DEFAULT_.foetal_health_stat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.foetal_health_stat])

slots.amniotic_fluid_color = Slot(uri=DEFAULT_.amniotic_fluid_color, name="amniotic_fluid_color", curie=DEFAULT_.curie('amniotic_fluid_color'),
                   model_uri=DEFAULT_.amniotic_fluid_color, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.amniotic_fluid_color])

slots.kidney_disord = Slot(uri=DEFAULT_.kidney_disord, name="kidney_disord", curie=DEFAULT_.curie('kidney_disord'),
                   model_uri=DEFAULT_.kidney_disord, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.kidney_disord])

slots.urogenit_tract_disor = Slot(uri=DEFAULT_.urogenit_tract_disor, name="urogenit_tract_disor", curie=DEFAULT_.curie('urogenit_tract_disor'),
                   model_uri=DEFAULT_.urogenit_tract_disor, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.urogenit_tract_disor])

slots.urine_collect_meth = Slot(uri=DEFAULT_.urine_collect_meth, name="urine_collect_meth", curie=DEFAULT_.curie('urine_collect_meth'),
                   model_uri=DEFAULT_.urine_collect_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.urine_collect_meth],
                   pattern=re.compile(r'[clean catch|catheter]'))

slots.gastrointest_disord = Slot(uri=DEFAULT_.gastrointest_disord, name="gastrointest_disord", curie=DEFAULT_.curie('gastrointest_disord'),
                   model_uri=DEFAULT_.gastrointest_disord, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.gastrointest_disord])

slots.liver_disord = Slot(uri=DEFAULT_.liver_disord, name="liver_disord", curie=DEFAULT_.curie('liver_disord'),
                   model_uri=DEFAULT_.liver_disord, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.liver_disord])

slots.special_diet = Slot(uri=DEFAULT_.special_diet, name="special_diet", curie=DEFAULT_.curie('special_diet'),
                   model_uri=DEFAULT_.special_diet, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.special_diet],
                   pattern=re.compile(r'[low carb|reduced calorie|vegetarian|other(to be specified)]'))

slots.nose_mouth_teeth_throat_disord = Slot(uri=DEFAULT_.nose_mouth_teeth_throat_disord, name="nose_mouth_teeth_throat_disord", curie=DEFAULT_.curie('nose_mouth_teeth_throat_disord'),
                   model_uri=DEFAULT_.nose_mouth_teeth_throat_disord, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.nose_mouth_teeth_throat_disord])

slots.time_last_toothbrush = Slot(uri=DEFAULT_.time_last_toothbrush, name="time_last_toothbrush", curie=DEFAULT_.curie('time_last_toothbrush'),
                   model_uri=DEFAULT_.time_last_toothbrush, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.time_last_toothbrush])

slots.dermatology_disord = Slot(uri=DEFAULT_.dermatology_disord, name="dermatology_disord", curie=DEFAULT_.curie('dermatology_disord'),
                   model_uri=DEFAULT_.dermatology_disord, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.dermatology_disord])

slots.time_since_last_wash = Slot(uri=DEFAULT_.time_since_last_wash, name="time_since_last_wash", curie=DEFAULT_.curie('time_since_last_wash'),
                   model_uri=DEFAULT_.time_since_last_wash, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.time_since_last_wash])

slots.dominant_hand = Slot(uri=DEFAULT_.dominant_hand, name="dominant_hand", curie=DEFAULT_.curie('dominant_hand'),
                   model_uri=DEFAULT_.dominant_hand, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.dominant_hand],
                   pattern=re.compile(r'[left|right|ambidextrous]'))

slots.menarche = Slot(uri=DEFAULT_.menarche, name="menarche", curie=DEFAULT_.curie('menarche'),
                   model_uri=DEFAULT_.menarche, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.menarche])

slots.sexual_act = Slot(uri=DEFAULT_.sexual_act, name="sexual_act", curie=DEFAULT_.curie('sexual_act'),
                   model_uri=DEFAULT_.sexual_act, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.sexual_act])

slots.pregnancy = Slot(uri=DEFAULT_.pregnancy, name="pregnancy", curie=DEFAULT_.curie('pregnancy'),
                   model_uri=DEFAULT_.pregnancy, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.pregnancy])

slots.douche = Slot(uri=DEFAULT_.douche, name="douche", curie=DEFAULT_.curie('douche'),
                   model_uri=DEFAULT_.douche, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.douche])

slots.birth_control = Slot(uri=DEFAULT_.birth_control, name="birth_control", curie=DEFAULT_.curie('birth_control'),
                   model_uri=DEFAULT_.birth_control, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.birth_control])

slots.menopause = Slot(uri=DEFAULT_.menopause, name="menopause", curie=DEFAULT_.curie('menopause'),
                   model_uri=DEFAULT_.menopause, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.menopause])

slots.hrt = Slot(uri=DEFAULT_.hrt, name="hrt", curie=DEFAULT_.curie('hrt'),
                   model_uri=DEFAULT_.hrt, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.hrt])

slots.hysterectomy = Slot(uri=DEFAULT_.hysterectomy, name="hysterectomy", curie=DEFAULT_.curie('hysterectomy'),
                   model_uri=DEFAULT_.hysterectomy, domain=None, range=Optional[Union[dict, BooleanValue]], mappings = [MIXS.hysterectomy],
                   pattern=re.compile(r'[true|false]'))

slots.gynecologic_disord = Slot(uri=DEFAULT_.gynecologic_disord, name="gynecologic_disord", curie=DEFAULT_.curie('gynecologic_disord'),
                   model_uri=DEFAULT_.gynecologic_disord, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.gynecologic_disord])

slots.urogenit_disord = Slot(uri=DEFAULT_.urogenit_disord, name="urogenit_disord", curie=DEFAULT_.curie('urogenit_disord'),
                   model_uri=DEFAULT_.urogenit_disord, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.urogenit_disord])

slots.hcr = Slot(uri=DEFAULT_.hcr, name="hcr", curie=DEFAULT_.curie('hcr'),
                   model_uri=DEFAULT_.hcr, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.hcr],
                   pattern=re.compile(r'[Oil Reservoir|Gas Reservoir|Oil Sand|Coalbed|Shale|Tight Oil Reservoir|Tight Gas Reservoir|other]'))

slots.hc_produced = Slot(uri=DEFAULT_.hc_produced, name="hc_produced", curie=DEFAULT_.curie('hc_produced'),
                   model_uri=DEFAULT_.hc_produced, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.hc_produced],
                   pattern=re.compile(r'[Oil|Gas\-Condensate|Gas|Bitumen|Coalbed Methane|other]'))

slots.basin = Slot(uri=DEFAULT_.basin, name="basin", curie=DEFAULT_.curie('basin'),
                   model_uri=DEFAULT_.basin, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.basin])

slots.field = Slot(uri=DEFAULT_.field, name="field", curie=DEFAULT_.curie('field'),
                   model_uri=DEFAULT_.field, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.field])

slots.reservoir = Slot(uri=DEFAULT_.reservoir, name="reservoir", curie=DEFAULT_.curie('reservoir'),
                   model_uri=DEFAULT_.reservoir, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.reservoir])

slots.hcr_temp = Slot(uri=DEFAULT_.hcr_temp, name="hcr_temp", curie=DEFAULT_.curie('hcr_temp'),
                   model_uri=DEFAULT_.hcr_temp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.hcr_temp],
                   pattern=re.compile(r'\d+[.\d+] \- \d+[.\d+] \S+'))

slots.tvdss_of_hcr_temp = Slot(uri=DEFAULT_.tvdss_of_hcr_temp, name="tvdss_of_hcr_temp", curie=DEFAULT_.curie('tvdss_of_hcr_temp'),
                   model_uri=DEFAULT_.tvdss_of_hcr_temp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tvdss_of_hcr_temp],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.hcr_pressure = Slot(uri=DEFAULT_.hcr_pressure, name="hcr_pressure", curie=DEFAULT_.curie('hcr_pressure'),
                   model_uri=DEFAULT_.hcr_pressure, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.hcr_pressure],
                   pattern=re.compile(r'\d+[.\d+] \- \d+[.\d+] \S+'))

slots.tvdss_of_hcr_pressure = Slot(uri=DEFAULT_.tvdss_of_hcr_pressure, name="tvdss_of_hcr_pressure", curie=DEFAULT_.curie('tvdss_of_hcr_pressure'),
                   model_uri=DEFAULT_.tvdss_of_hcr_pressure, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tvdss_of_hcr_pressure],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.permeability = Slot(uri=DEFAULT_.permeability, name="permeability", curie=DEFAULT_.curie('permeability'),
                   model_uri=DEFAULT_.permeability, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.permeability])

slots.porosity = Slot(uri=DEFAULT_.porosity, name="porosity", curie=DEFAULT_.curie('porosity'),
                   model_uri=DEFAULT_.porosity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.porosity],
                   pattern=re.compile(r'\d+[.\d+] \- \d+[.\d+] \S+'))

slots.lithology = Slot(uri=DEFAULT_.lithology, name="lithology", curie=DEFAULT_.curie('lithology'),
                   model_uri=DEFAULT_.lithology, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.lithology],
                   pattern=re.compile(r'[Basement|Chalk|Chert|Coal|Conglomerate|Diatomite|Dolomite|Limestone|Sandstone|Shale|Siltstone|Volcanic|other]'))

slots.depos_env = Slot(uri=DEFAULT_.depos_env, name="depos_env", curie=DEFAULT_.curie('depos_env'),
                   model_uri=DEFAULT_.depos_env, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.depos_env],
                   pattern=re.compile(r'[Continental \- Alluvial|Continental \- Aeolian|Continental \- Fluvial|Continental \- Lacustrine|Transitional \- Deltaic|Transitional \- Tidal|Transitional \- Lagoonal|Transitional \- Beach|Transitional \- Lake|Marine \- Shallow|Marine \- Deep|Marine \- Reef|Other \- Evaporite|Other \- Glacial|Other \- Volcanic|other]'))

slots.hcr_geol_age = Slot(uri=DEFAULT_.hcr_geol_age, name="hcr_geol_age", curie=DEFAULT_.curie('hcr_geol_age'),
                   model_uri=DEFAULT_.hcr_geol_age, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.hcr_geol_age],
                   pattern=re.compile(r'[Archean|Cambrian|Carboniferous|Cenozoic|Cretaceous|Devonian|Jurassic|Mesozoic|Neogene|Ordovician|Paleogene|Paleozoic|Permian|Precambrian|Proterozoic|Silurian|Triassic|other]'))

slots.owc_tvdss = Slot(uri=DEFAULT_.owc_tvdss, name="owc_tvdss", curie=DEFAULT_.curie('owc_tvdss'),
                   model_uri=DEFAULT_.owc_tvdss, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.owc_tvdss],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.hcr_fw_salinity = Slot(uri=DEFAULT_.hcr_fw_salinity, name="hcr_fw_salinity", curie=DEFAULT_.curie('hcr_fw_salinity'),
                   model_uri=DEFAULT_.hcr_fw_salinity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.hcr_fw_salinity],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.sulfate_fw = Slot(uri=DEFAULT_.sulfate_fw, name="sulfate_fw", curie=DEFAULT_.curie('sulfate_fw'),
                   model_uri=DEFAULT_.sulfate_fw, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.sulfate_fw],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.vfa_fw = Slot(uri=DEFAULT_.vfa_fw, name="vfa_fw", curie=DEFAULT_.curie('vfa_fw'),
                   model_uri=DEFAULT_.vfa_fw, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.vfa_fw],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.sr_kerog_type = Slot(uri=DEFAULT_.sr_kerog_type, name="sr_kerog_type", curie=DEFAULT_.curie('sr_kerog_type'),
                   model_uri=DEFAULT_.sr_kerog_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.sr_kerog_type],
                   pattern=re.compile(r'[Type I|Type II|Type III|Type IV|other]'))

slots.sr_lithology = Slot(uri=DEFAULT_.sr_lithology, name="sr_lithology", curie=DEFAULT_.curie('sr_lithology'),
                   model_uri=DEFAULT_.sr_lithology, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.sr_lithology],
                   pattern=re.compile(r'[Clastic|Carbonate|Coal|Biosilicieous|other]'))

slots.sr_dep_env = Slot(uri=DEFAULT_.sr_dep_env, name="sr_dep_env", curie=DEFAULT_.curie('sr_dep_env'),
                   model_uri=DEFAULT_.sr_dep_env, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.sr_dep_env],
                   pattern=re.compile(r'[Lacustine|Fluvioldeltaic|Fluviomarine|Marine|other]'))

slots.sr_geol_age = Slot(uri=DEFAULT_.sr_geol_age, name="sr_geol_age", curie=DEFAULT_.curie('sr_geol_age'),
                   model_uri=DEFAULT_.sr_geol_age, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.sr_geol_age],
                   pattern=re.compile(r'[Archean|Cambrian|Carboniferous|Cenozoic|Cretaceous|Devonian|Jurassic|Mesozoic|Neogene|Ordovician|Paleogene|Paleozoic|Permian|Precambrian|Proterozoic|Silurian|Triassic|other]'))

slots.samp_well_name = Slot(uri=DEFAULT_.samp_well_name, name="samp_well_name", curie=DEFAULT_.curie('samp_well_name'),
                   model_uri=DEFAULT_.samp_well_name, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_well_name])

slots.win = Slot(uri=DEFAULT_.win, name="win", curie=DEFAULT_.curie('win'),
                   model_uri=DEFAULT_.win, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.win])

slots.samp_type = Slot(uri=DEFAULT_.samp_type, name="samp_type", curie=DEFAULT_.curie('samp_type'),
                   model_uri=DEFAULT_.samp_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_type],
                   pattern=re.compile(r'[core|rock trimmings|drill cuttings|piping section|coupon|pigging debris|solid deposit|produced fluid|produced water|injected water|water from treatment plant|fresh water|sea water|drilling fluid|procedural blank|positive control|negative control|other]'))

slots.samp_subtype = Slot(uri=DEFAULT_.samp_subtype, name="samp_subtype", curie=DEFAULT_.curie('samp_subtype'),
                   model_uri=DEFAULT_.samp_subtype, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_subtype],
                   pattern=re.compile(r'[oil phase|water phase|biofilm|not applicable|other]'))

slots.pressure = Slot(uri=DEFAULT_.pressure, name="pressure", curie=DEFAULT_.curie('pressure'),
                   model_uri=DEFAULT_.pressure, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.pressure],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.samp_tvdss = Slot(uri=DEFAULT_.samp_tvdss, name="samp_tvdss", curie=DEFAULT_.curie('samp_tvdss'),
                   model_uri=DEFAULT_.samp_tvdss, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.samp_tvdss],
                   pattern=re.compile(r'\d+[.\d+]\-\d+[.\d+] \S+'))

slots.samp_md = Slot(uri=DEFAULT_.samp_md, name="samp_md", curie=DEFAULT_.curie('samp_md'),
                   model_uri=DEFAULT_.samp_md, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.samp_md],
                   pattern=re.compile(r'\d+[.\d+] \S+;[GL|DF|RT|KB|MSL|other]'))

slots.samp_transport_cond = Slot(uri=DEFAULT_.samp_transport_cond, name="samp_transport_cond", curie=DEFAULT_.curie('samp_transport_cond'),
                   model_uri=DEFAULT_.samp_transport_cond, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.samp_transport_cond],
                   pattern=re.compile(r'\d+[.\d+] \S+;\d+[.\d+] \S+'))

slots.organism_count_qpcr_info = Slot(uri=DEFAULT_.organism_count_qpcr_info, name="organism_count_qpcr_info", curie=DEFAULT_.curie('organism_count_qpcr_info'),
                   model_uri=DEFAULT_.organism_count_qpcr_info, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.organism_count_qpcr_info])

slots.ph = Slot(uri=DEFAULT_.ph, name="ph", curie=DEFAULT_.curie('ph'),
                   model_uri=DEFAULT_.ph, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.ph],
                   pattern=re.compile(r'\d+[.\d+]'))

slots.alkalinity = Slot(uri=DEFAULT_.alkalinity, name="alkalinity", curie=DEFAULT_.curie('alkalinity'),
                   model_uri=DEFAULT_.alkalinity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.alkalinity],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.alkalinity_method = Slot(uri=DEFAULT_.alkalinity_method, name="alkalinity_method", curie=DEFAULT_.curie('alkalinity_method'),
                   model_uri=DEFAULT_.alkalinity_method, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.alkalinity_method])

slots.sulfate = Slot(uri=DEFAULT_.sulfate, name="sulfate", curie=DEFAULT_.curie('sulfate'),
                   model_uri=DEFAULT_.sulfate, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.sulfate],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.sulfide = Slot(uri=DEFAULT_.sulfide, name="sulfide", curie=DEFAULT_.curie('sulfide'),
                   model_uri=DEFAULT_.sulfide, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.sulfide],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.tot_sulfur = Slot(uri=DEFAULT_.tot_sulfur, name="tot_sulfur", curie=DEFAULT_.curie('tot_sulfur'),
                   model_uri=DEFAULT_.tot_sulfur, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_sulfur],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.nitrate = Slot(uri=DEFAULT_.nitrate, name="nitrate", curie=DEFAULT_.curie('nitrate'),
                   model_uri=DEFAULT_.nitrate, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.nitrate],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.nitrite = Slot(uri=DEFAULT_.nitrite, name="nitrite", curie=DEFAULT_.curie('nitrite'),
                   model_uri=DEFAULT_.nitrite, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.nitrite],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.ammonium = Slot(uri=DEFAULT_.ammonium, name="ammonium", curie=DEFAULT_.curie('ammonium'),
                   model_uri=DEFAULT_.ammonium, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.ammonium],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.tot_nitro = Slot(uri=DEFAULT_.tot_nitro, name="tot_nitro", curie=DEFAULT_.curie('tot_nitro'),
                   model_uri=DEFAULT_.tot_nitro, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_nitro],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.diss_iron = Slot(uri=DEFAULT_.diss_iron, name="diss_iron", curie=DEFAULT_.curie('diss_iron'),
                   model_uri=DEFAULT_.diss_iron, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diss_iron],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.sodium = Slot(uri=DEFAULT_.sodium, name="sodium", curie=DEFAULT_.curie('sodium'),
                   model_uri=DEFAULT_.sodium, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.sodium],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.chloride = Slot(uri=DEFAULT_.chloride, name="chloride", curie=DEFAULT_.curie('chloride'),
                   model_uri=DEFAULT_.chloride, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.chloride],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.potassium = Slot(uri=DEFAULT_.potassium, name="potassium", curie=DEFAULT_.curie('potassium'),
                   model_uri=DEFAULT_.potassium, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.potassium],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.magnesium = Slot(uri=DEFAULT_.magnesium, name="magnesium", curie=DEFAULT_.curie('magnesium'),
                   model_uri=DEFAULT_.magnesium, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.magnesium],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.calcium = Slot(uri=DEFAULT_.calcium, name="calcium", curie=DEFAULT_.curie('calcium'),
                   model_uri=DEFAULT_.calcium, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.calcium],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.tot_iron = Slot(uri=DEFAULT_.tot_iron, name="tot_iron", curie=DEFAULT_.curie('tot_iron'),
                   model_uri=DEFAULT_.tot_iron, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_iron],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.diss_org_carb = Slot(uri=DEFAULT_.diss_org_carb, name="diss_org_carb", curie=DEFAULT_.curie('diss_org_carb'),
                   model_uri=DEFAULT_.diss_org_carb, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diss_org_carb],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.diss_inorg_carb = Slot(uri=DEFAULT_.diss_inorg_carb, name="diss_inorg_carb", curie=DEFAULT_.curie('diss_inorg_carb'),
                   model_uri=DEFAULT_.diss_inorg_carb, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diss_inorg_carb],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.diss_inorg_phosp = Slot(uri=DEFAULT_.diss_inorg_phosp, name="diss_inorg_phosp", curie=DEFAULT_.curie('diss_inorg_phosp'),
                   model_uri=DEFAULT_.diss_inorg_phosp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diss_inorg_phosp],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.tot_phosp = Slot(uri=DEFAULT_.tot_phosp, name="tot_phosp", curie=DEFAULT_.curie('tot_phosp'),
                   model_uri=DEFAULT_.tot_phosp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_phosp],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.suspend_solids = Slot(uri=DEFAULT_.suspend_solids, name="suspend_solids", curie=DEFAULT_.curie('suspend_solids'),
                   model_uri=DEFAULT_.suspend_solids, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.suspend_solids])

slots.density = Slot(uri=DEFAULT_.density, name="density", curie=DEFAULT_.curie('density'),
                   model_uri=DEFAULT_.density, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.density],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.diss_carb_dioxide = Slot(uri=DEFAULT_.diss_carb_dioxide, name="diss_carb_dioxide", curie=DEFAULT_.curie('diss_carb_dioxide'),
                   model_uri=DEFAULT_.diss_carb_dioxide, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diss_carb_dioxide],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.diss_oxygen_fluid = Slot(uri=DEFAULT_.diss_oxygen_fluid, name="diss_oxygen_fluid", curie=DEFAULT_.curie('diss_oxygen_fluid'),
                   model_uri=DEFAULT_.diss_oxygen_fluid, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diss_oxygen_fluid],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.vfa = Slot(uri=DEFAULT_.vfa, name="vfa", curie=DEFAULT_.curie('vfa'),
                   model_uri=DEFAULT_.vfa, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.vfa],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.benzene = Slot(uri=DEFAULT_.benzene, name="benzene", curie=DEFAULT_.curie('benzene'),
                   model_uri=DEFAULT_.benzene, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.benzene],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.toluene = Slot(uri=DEFAULT_.toluene, name="toluene", curie=DEFAULT_.curie('toluene'),
                   model_uri=DEFAULT_.toluene, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.toluene],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.ethylbenzene = Slot(uri=DEFAULT_.ethylbenzene, name="ethylbenzene", curie=DEFAULT_.curie('ethylbenzene'),
                   model_uri=DEFAULT_.ethylbenzene, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.ethylbenzene],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.xylene = Slot(uri=DEFAULT_.xylene, name="xylene", curie=DEFAULT_.curie('xylene'),
                   model_uri=DEFAULT_.xylene, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.xylene],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.api = Slot(uri=DEFAULT_.api, name="api", curie=DEFAULT_.curie('api'),
                   model_uri=DEFAULT_.api, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.api],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.tan = Slot(uri=DEFAULT_.tan, name="tan", curie=DEFAULT_.curie('tan'),
                   model_uri=DEFAULT_.tan, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tan],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.viscosity = Slot(uri=DEFAULT_.viscosity, name="viscosity", curie=DEFAULT_.curie('viscosity'),
                   model_uri=DEFAULT_.viscosity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.viscosity],
                   pattern=re.compile(r'\d+[.\d+] \S+;\d+[.\d+] \S+'))

slots.pour_point = Slot(uri=DEFAULT_.pour_point, name="pour_point", curie=DEFAULT_.curie('pour_point'),
                   model_uri=DEFAULT_.pour_point, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.pour_point],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.saturates_pc = Slot(uri=DEFAULT_.saturates_pc, name="saturates_pc", curie=DEFAULT_.curie('saturates_pc'),
                   model_uri=DEFAULT_.saturates_pc, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.saturates_pc])

slots.aromatics_pc = Slot(uri=DEFAULT_.aromatics_pc, name="aromatics_pc", curie=DEFAULT_.curie('aromatics_pc'),
                   model_uri=DEFAULT_.aromatics_pc, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.aromatics_pc])

slots.resins_pc = Slot(uri=DEFAULT_.resins_pc, name="resins_pc", curie=DEFAULT_.curie('resins_pc'),
                   model_uri=DEFAULT_.resins_pc, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.resins_pc])

slots.asphaltenes_pc = Slot(uri=DEFAULT_.asphaltenes_pc, name="asphaltenes_pc", curie=DEFAULT_.curie('asphaltenes_pc'),
                   model_uri=DEFAULT_.asphaltenes_pc, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.asphaltenes_pc])

slots.additional_info = Slot(uri=DEFAULT_.additional_info, name="additional_info", curie=DEFAULT_.curie('additional_info'),
                   model_uri=DEFAULT_.additional_info, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.additional_info])

slots.prod_start_date = Slot(uri=DEFAULT_.prod_start_date, name="prod_start_date", curie=DEFAULT_.curie('prod_start_date'),
                   model_uri=DEFAULT_.prod_start_date, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.prod_start_date])

slots.prod_rate = Slot(uri=DEFAULT_.prod_rate, name="prod_rate", curie=DEFAULT_.curie('prod_rate'),
                   model_uri=DEFAULT_.prod_rate, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.prod_rate],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.water_production_rate = Slot(uri=DEFAULT_.water_production_rate, name="water_production_rate", curie=DEFAULT_.curie('water_production_rate'),
                   model_uri=DEFAULT_.water_production_rate, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.water_production_rate],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.water_cut = Slot(uri=DEFAULT_.water_cut, name="water_cut", curie=DEFAULT_.curie('water_cut'),
                   model_uri=DEFAULT_.water_cut, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.water_cut],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.iwf = Slot(uri=DEFAULT_.iwf, name="iwf", curie=DEFAULT_.curie('iwf'),
                   model_uri=DEFAULT_.iwf, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.iwf],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.add_recov_method = Slot(uri=DEFAULT_.add_recov_method, name="add_recov_method", curie=DEFAULT_.curie('add_recov_method'),
                   model_uri=DEFAULT_.add_recov_method, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.add_recov_method])

slots.iw_bt_date_well = Slot(uri=DEFAULT_.iw_bt_date_well, name="iw_bt_date_well", curie=DEFAULT_.curie('iw_bt_date_well'),
                   model_uri=DEFAULT_.iw_bt_date_well, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.iw_bt_date_well])

slots.biocide = Slot(uri=DEFAULT_.biocide, name="biocide", curie=DEFAULT_.curie('biocide'),
                   model_uri=DEFAULT_.biocide, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.biocide])

slots.biocide_admin_method = Slot(uri=DEFAULT_.biocide_admin_method, name="biocide_admin_method", curie=DEFAULT_.curie('biocide_admin_method'),
                   model_uri=DEFAULT_.biocide_admin_method, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.biocide_admin_method])

slots.chem_treatment = Slot(uri=DEFAULT_.chem_treatment, name="chem_treatment", curie=DEFAULT_.curie('chem_treatment'),
                   model_uri=DEFAULT_.chem_treatment, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.chem_treatment])

slots.chem_treatment_method = Slot(uri=DEFAULT_.chem_treatment_method, name="chem_treatment_method", curie=DEFAULT_.curie('chem_treatment_method'),
                   model_uri=DEFAULT_.chem_treatment_method, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.chem_treatment_method])

slots.samp_loc_corr_rate = Slot(uri=DEFAULT_.samp_loc_corr_rate, name="samp_loc_corr_rate", curie=DEFAULT_.curie('samp_loc_corr_rate'),
                   model_uri=DEFAULT_.samp_loc_corr_rate, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.samp_loc_corr_rate],
                   pattern=re.compile(r'\d+[.\d+] \- \d+[.\d+] \S+'))

slots.samp_collection_point = Slot(uri=DEFAULT_.samp_collection_point, name="samp_collection_point", curie=DEFAULT_.curie('samp_collection_point'),
                   model_uri=DEFAULT_.samp_collection_point, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_collection_point],
                   pattern=re.compile(r'[well|test well|drilling rig|wellhead|separator|storage tank|other]'))

slots.samp_preserv = Slot(uri=DEFAULT_.samp_preserv, name="samp_preserv", curie=DEFAULT_.curie('samp_preserv'),
                   model_uri=DEFAULT_.samp_preserv, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.samp_preserv])

slots.alkyl_diethers = Slot(uri=DEFAULT_.alkyl_diethers, name="alkyl_diethers", curie=DEFAULT_.curie('alkyl_diethers'),
                   model_uri=DEFAULT_.alkyl_diethers, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.alkyl_diethers],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.aminopept_act = Slot(uri=DEFAULT_.aminopept_act, name="aminopept_act", curie=DEFAULT_.curie('aminopept_act'),
                   model_uri=DEFAULT_.aminopept_act, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.aminopept_act],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.bacteria_carb_prod = Slot(uri=DEFAULT_.bacteria_carb_prod, name="bacteria_carb_prod", curie=DEFAULT_.curie('bacteria_carb_prod'),
                   model_uri=DEFAULT_.bacteria_carb_prod, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.bacteria_carb_prod],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.biomass = Slot(uri=DEFAULT_.biomass, name="biomass", curie=DEFAULT_.curie('biomass'),
                   model_uri=DEFAULT_.biomass, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.biomass])

slots.bishomohopanol = Slot(uri=DEFAULT_.bishomohopanol, name="bishomohopanol", curie=DEFAULT_.curie('bishomohopanol'),
                   model_uri=DEFAULT_.bishomohopanol, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.bishomohopanol],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.bromide = Slot(uri=DEFAULT_.bromide, name="bromide", curie=DEFAULT_.curie('bromide'),
                   model_uri=DEFAULT_.bromide, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.bromide],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.carb_nitro_ratio = Slot(uri=DEFAULT_.carb_nitro_ratio, name="carb_nitro_ratio", curie=DEFAULT_.curie('carb_nitro_ratio'),
                   model_uri=DEFAULT_.carb_nitro_ratio, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.carb_nitro_ratio],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.chlorophyll = Slot(uri=DEFAULT_.chlorophyll, name="chlorophyll", curie=DEFAULT_.curie('chlorophyll'),
                   model_uri=DEFAULT_.chlorophyll, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.chlorophyll],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.diether_lipids = Slot(uri=DEFAULT_.diether_lipids, name="diether_lipids", curie=DEFAULT_.curie('diether_lipids'),
                   model_uri=DEFAULT_.diether_lipids, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diether_lipids])

slots.diss_hydrogen = Slot(uri=DEFAULT_.diss_hydrogen, name="diss_hydrogen", curie=DEFAULT_.curie('diss_hydrogen'),
                   model_uri=DEFAULT_.diss_hydrogen, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diss_hydrogen],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.diss_org_nitro = Slot(uri=DEFAULT_.diss_org_nitro, name="diss_org_nitro", curie=DEFAULT_.curie('diss_org_nitro'),
                   model_uri=DEFAULT_.diss_org_nitro, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diss_org_nitro],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.diss_oxygen = Slot(uri=DEFAULT_.diss_oxygen, name="diss_oxygen", curie=DEFAULT_.curie('diss_oxygen'),
                   model_uri=DEFAULT_.diss_oxygen, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diss_oxygen],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.glucosidase_act = Slot(uri=DEFAULT_.glucosidase_act, name="glucosidase_act", curie=DEFAULT_.curie('glucosidase_act'),
                   model_uri=DEFAULT_.glucosidase_act, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.glucosidase_act],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.mean_frict_vel = Slot(uri=DEFAULT_.mean_frict_vel, name="mean_frict_vel", curie=DEFAULT_.curie('mean_frict_vel'),
                   model_uri=DEFAULT_.mean_frict_vel, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.mean_frict_vel],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.mean_peak_frict_vel = Slot(uri=DEFAULT_.mean_peak_frict_vel, name="mean_peak_frict_vel", curie=DEFAULT_.curie('mean_peak_frict_vel'),
                   model_uri=DEFAULT_.mean_peak_frict_vel, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.mean_peak_frict_vel],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.n_alkanes = Slot(uri=DEFAULT_.n_alkanes, name="n_alkanes", curie=DEFAULT_.curie('n_alkanes'),
                   model_uri=DEFAULT_.n_alkanes, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.n_alkanes])

slots.nitro = Slot(uri=DEFAULT_.nitro, name="nitro", curie=DEFAULT_.curie('nitro'),
                   model_uri=DEFAULT_.nitro, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.nitro],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.org_carb = Slot(uri=DEFAULT_.org_carb, name="org_carb", curie=DEFAULT_.curie('org_carb'),
                   model_uri=DEFAULT_.org_carb, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.org_carb],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.org_matter = Slot(uri=DEFAULT_.org_matter, name="org_matter", curie=DEFAULT_.curie('org_matter'),
                   model_uri=DEFAULT_.org_matter, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.org_matter],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.org_nitro = Slot(uri=DEFAULT_.org_nitro, name="org_nitro", curie=DEFAULT_.curie('org_nitro'),
                   model_uri=DEFAULT_.org_nitro, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.org_nitro],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.part_org_carb = Slot(uri=DEFAULT_.part_org_carb, name="part_org_carb", curie=DEFAULT_.curie('part_org_carb'),
                   model_uri=DEFAULT_.part_org_carb, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.part_org_carb],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.petroleum_hydrocarb = Slot(uri=DEFAULT_.petroleum_hydrocarb, name="petroleum_hydrocarb", curie=DEFAULT_.curie('petroleum_hydrocarb'),
                   model_uri=DEFAULT_.petroleum_hydrocarb, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.petroleum_hydrocarb],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.phaeopigments = Slot(uri=DEFAULT_.phaeopigments, name="phaeopigments", curie=DEFAULT_.curie('phaeopigments'),
                   model_uri=DEFAULT_.phaeopigments, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.phaeopigments])

slots.phosphate = Slot(uri=DEFAULT_.phosphate, name="phosphate", curie=DEFAULT_.curie('phosphate'),
                   model_uri=DEFAULT_.phosphate, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.phosphate],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.phosplipid_fatt_acid = Slot(uri=DEFAULT_.phosplipid_fatt_acid, name="phosplipid_fatt_acid", curie=DEFAULT_.curie('phosplipid_fatt_acid'),
                   model_uri=DEFAULT_.phosplipid_fatt_acid, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.phosplipid_fatt_acid])

slots.redox_potential = Slot(uri=DEFAULT_.redox_potential, name="redox_potential", curie=DEFAULT_.curie('redox_potential'),
                   model_uri=DEFAULT_.redox_potential, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.redox_potential],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.salinity = Slot(uri=DEFAULT_.salinity, name="salinity", curie=DEFAULT_.curie('salinity'),
                   model_uri=DEFAULT_.salinity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.salinity],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.silicate = Slot(uri=DEFAULT_.silicate, name="silicate", curie=DEFAULT_.curie('silicate'),
                   model_uri=DEFAULT_.silicate, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.silicate],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.tot_carb = Slot(uri=DEFAULT_.tot_carb, name="tot_carb", curie=DEFAULT_.curie('tot_carb'),
                   model_uri=DEFAULT_.tot_carb, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_carb],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.tot_nitro_content = Slot(uri=DEFAULT_.tot_nitro_content, name="tot_nitro_content", curie=DEFAULT_.curie('tot_nitro_content'),
                   model_uri=DEFAULT_.tot_nitro_content, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_nitro_content],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.tot_org_carb = Slot(uri=DEFAULT_.tot_org_carb, name="tot_org_carb", curie=DEFAULT_.curie('tot_org_carb'),
                   model_uri=DEFAULT_.tot_org_carb, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_org_carb],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.turbidity = Slot(uri=DEFAULT_.turbidity, name="turbidity", curie=DEFAULT_.curie('turbidity'),
                   model_uri=DEFAULT_.turbidity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.turbidity],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.water_content = Slot(uri=DEFAULT_.water_content, name="water_content", curie=DEFAULT_.curie('water_content'),
                   model_uri=DEFAULT_.water_content, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.water_content],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.water_current = Slot(uri=DEFAULT_.water_current, name="water_current", curie=DEFAULT_.curie('water_current'),
                   model_uri=DEFAULT_.water_current, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.water_current],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.air_temp_regm = Slot(uri=DEFAULT_.air_temp_regm, name="air_temp_regm", curie=DEFAULT_.curie('air_temp_regm'),
                   model_uri=DEFAULT_.air_temp_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.air_temp_regm])

slots.antibiotic_regm = Slot(uri=DEFAULT_.antibiotic_regm, name="antibiotic_regm", curie=DEFAULT_.curie('antibiotic_regm'),
                   model_uri=DEFAULT_.antibiotic_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.antibiotic_regm])

slots.biotic_regm = Slot(uri=DEFAULT_.biotic_regm, name="biotic_regm", curie=DEFAULT_.curie('biotic_regm'),
                   model_uri=DEFAULT_.biotic_regm, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.biotic_regm])

slots.chem_mutagen = Slot(uri=DEFAULT_.chem_mutagen, name="chem_mutagen", curie=DEFAULT_.curie('chem_mutagen'),
                   model_uri=DEFAULT_.chem_mutagen, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.chem_mutagen])

slots.climate_environment = Slot(uri=DEFAULT_.climate_environment, name="climate_environment", curie=DEFAULT_.curie('climate_environment'),
                   model_uri=DEFAULT_.climate_environment, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.climate_environment])

slots.cult_root_med = Slot(uri=DEFAULT_.cult_root_med, name="cult_root_med", curie=DEFAULT_.curie('cult_root_med'),
                   model_uri=DEFAULT_.cult_root_med, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.cult_root_med])

slots.fertilizer_regm = Slot(uri=DEFAULT_.fertilizer_regm, name="fertilizer_regm", curie=DEFAULT_.curie('fertilizer_regm'),
                   model_uri=DEFAULT_.fertilizer_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.fertilizer_regm])

slots.fungicide_regm = Slot(uri=DEFAULT_.fungicide_regm, name="fungicide_regm", curie=DEFAULT_.curie('fungicide_regm'),
                   model_uri=DEFAULT_.fungicide_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.fungicide_regm])

slots.gaseous_environment = Slot(uri=DEFAULT_.gaseous_environment, name="gaseous_environment", curie=DEFAULT_.curie('gaseous_environment'),
                   model_uri=DEFAULT_.gaseous_environment, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.gaseous_environment])

slots.gravity = Slot(uri=DEFAULT_.gravity, name="gravity", curie=DEFAULT_.curie('gravity'),
                   model_uri=DEFAULT_.gravity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.gravity])

slots.growth_facil = Slot(uri=DEFAULT_.growth_facil, name="growth_facil", curie=DEFAULT_.curie('growth_facil'),
                   model_uri=DEFAULT_.growth_facil, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.growth_facil])

slots.growth_habit = Slot(uri=DEFAULT_.growth_habit, name="growth_habit", curie=DEFAULT_.curie('growth_habit'),
                   model_uri=DEFAULT_.growth_habit, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.growth_habit],
                   pattern=re.compile(r'[erect|semi\-erect|spreading|prostrate] '))

slots.growth_hormone_regm = Slot(uri=DEFAULT_.growth_hormone_regm, name="growth_hormone_regm", curie=DEFAULT_.curie('growth_hormone_regm'),
                   model_uri=DEFAULT_.growth_hormone_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.growth_hormone_regm])

slots.herbicide_regm = Slot(uri=DEFAULT_.herbicide_regm, name="herbicide_regm", curie=DEFAULT_.curie('herbicide_regm'),
                   model_uri=DEFAULT_.herbicide_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.herbicide_regm])

slots.host_wet_mass = Slot(uri=DEFAULT_.host_wet_mass, name="host_wet_mass", curie=DEFAULT_.curie('host_wet_mass'),
                   model_uri=DEFAULT_.host_wet_mass, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_wet_mass],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.humidity_regm = Slot(uri=DEFAULT_.humidity_regm, name="humidity_regm", curie=DEFAULT_.curie('humidity_regm'),
                   model_uri=DEFAULT_.humidity_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.humidity_regm])

slots.light_regm = Slot(uri=DEFAULT_.light_regm, name="light_regm", curie=DEFAULT_.curie('light_regm'),
                   model_uri=DEFAULT_.light_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.light_regm])

slots.mechanical_damage = Slot(uri=DEFAULT_.mechanical_damage, name="mechanical_damage", curie=DEFAULT_.curie('mechanical_damage'),
                   model_uri=DEFAULT_.mechanical_damage, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.mechanical_damage])

slots.mineral_nutr_regm = Slot(uri=DEFAULT_.mineral_nutr_regm, name="mineral_nutr_regm", curie=DEFAULT_.curie('mineral_nutr_regm'),
                   model_uri=DEFAULT_.mineral_nutr_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.mineral_nutr_regm])

slots.non_mineral_nutr_regm = Slot(uri=DEFAULT_.non_mineral_nutr_regm, name="non_mineral_nutr_regm", curie=DEFAULT_.curie('non_mineral_nutr_regm'),
                   model_uri=DEFAULT_.non_mineral_nutr_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.non_mineral_nutr_regm])

slots.ph_regm = Slot(uri=DEFAULT_.ph_regm, name="ph_regm", curie=DEFAULT_.curie('ph_regm'),
                   model_uri=DEFAULT_.ph_regm, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ph_regm])

slots.pesticide_regm = Slot(uri=DEFAULT_.pesticide_regm, name="pesticide_regm", curie=DEFAULT_.curie('pesticide_regm'),
                   model_uri=DEFAULT_.pesticide_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.pesticide_regm])

slots.plant_growth_med = Slot(uri=DEFAULT_.plant_growth_med, name="plant_growth_med", curie=DEFAULT_.curie('plant_growth_med'),
                   model_uri=DEFAULT_.plant_growth_med, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.plant_growth_med],
                   pattern=re.compile(r'.* \S+:\S+'))

slots.plant_product = Slot(uri=DEFAULT_.plant_product, name="plant_product", curie=DEFAULT_.curie('plant_product'),
                   model_uri=DEFAULT_.plant_product, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.plant_product])

slots.plant_sex = Slot(uri=DEFAULT_.plant_sex, name="plant_sex", curie=DEFAULT_.curie('plant_sex'),
                   model_uri=DEFAULT_.plant_sex, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.plant_sex],
                   pattern=re.compile(r'[Androdioecious|Androecious|Androgynous|Androgynomonoecious|Andromonoecious|Bisexual|Dichogamous|Diclinous|Dioecious|Gynodioecious|Gynoecious|Gynomonoecious|Hermaphroditic|Imperfect|Monoclinous|Monoecious|Perfect|Polygamodioecious|Polygamomonoecious|Polygamous|Protandrous|Protogynous|Subandroecious|Subdioecious|Subgynoecious|Synoecious|Trimonoecious|Trioecious|Unisexual]'))

slots.plant_struc = Slot(uri=DEFAULT_.plant_struc, name="plant_struc", curie=DEFAULT_.curie('plant_struc'),
                   model_uri=DEFAULT_.plant_struc, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.plant_struc],
                   pattern=re.compile(r'.* \S+:\S+'))

slots.radiation_regm = Slot(uri=DEFAULT_.radiation_regm, name="radiation_regm", curie=DEFAULT_.curie('radiation_regm'),
                   model_uri=DEFAULT_.radiation_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.radiation_regm])

slots.rainfall_regm = Slot(uri=DEFAULT_.rainfall_regm, name="rainfall_regm", curie=DEFAULT_.curie('rainfall_regm'),
                   model_uri=DEFAULT_.rainfall_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.rainfall_regm])

slots.root_cond = Slot(uri=DEFAULT_.root_cond, name="root_cond", curie=DEFAULT_.curie('root_cond'),
                   model_uri=DEFAULT_.root_cond, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.root_cond])

slots.root_med_carbon = Slot(uri=DEFAULT_.root_med_carbon, name="root_med_carbon", curie=DEFAULT_.curie('root_med_carbon'),
                   model_uri=DEFAULT_.root_med_carbon, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.root_med_carbon])

slots.root_med_macronutr = Slot(uri=DEFAULT_.root_med_macronutr, name="root_med_macronutr", curie=DEFAULT_.curie('root_med_macronutr'),
                   model_uri=DEFAULT_.root_med_macronutr, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.root_med_macronutr])

slots.root_med_micronutr = Slot(uri=DEFAULT_.root_med_micronutr, name="root_med_micronutr", curie=DEFAULT_.curie('root_med_micronutr'),
                   model_uri=DEFAULT_.root_med_micronutr, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.root_med_micronutr])

slots.root_med_suppl = Slot(uri=DEFAULT_.root_med_suppl, name="root_med_suppl", curie=DEFAULT_.curie('root_med_suppl'),
                   model_uri=DEFAULT_.root_med_suppl, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.root_med_suppl])

slots.root_med_ph = Slot(uri=DEFAULT_.root_med_ph, name="root_med_ph", curie=DEFAULT_.curie('root_med_ph'),
                   model_uri=DEFAULT_.root_med_ph, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.root_med_ph],
                   pattern=re.compile(r'\d+[.\d+]'))

slots.root_med_regl = Slot(uri=DEFAULT_.root_med_regl, name="root_med_regl", curie=DEFAULT_.curie('root_med_regl'),
                   model_uri=DEFAULT_.root_med_regl, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.root_med_regl])

slots.root_med_solid = Slot(uri=DEFAULT_.root_med_solid, name="root_med_solid", curie=DEFAULT_.curie('root_med_solid'),
                   model_uri=DEFAULT_.root_med_solid, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.root_med_solid])

slots.salt_regm = Slot(uri=DEFAULT_.salt_regm, name="salt_regm", curie=DEFAULT_.curie('salt_regm'),
                   model_uri=DEFAULT_.salt_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.salt_regm])

slots.season_environment = Slot(uri=DEFAULT_.season_environment, name="season_environment", curie=DEFAULT_.curie('season_environment'),
                   model_uri=DEFAULT_.season_environment, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.season_environment])

slots.standing_water_regm = Slot(uri=DEFAULT_.standing_water_regm, name="standing_water_regm", curie=DEFAULT_.curie('standing_water_regm'),
                   model_uri=DEFAULT_.standing_water_regm, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.standing_water_regm])

slots.tiss_cult_growth_med = Slot(uri=DEFAULT_.tiss_cult_growth_med, name="tiss_cult_growth_med", curie=DEFAULT_.curie('tiss_cult_growth_med'),
                   model_uri=DEFAULT_.tiss_cult_growth_med, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.tiss_cult_growth_med])

slots.water_temp_regm = Slot(uri=DEFAULT_.water_temp_regm, name="water_temp_regm", curie=DEFAULT_.curie('water_temp_regm'),
                   model_uri=DEFAULT_.water_temp_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.water_temp_regm])

slots.watering_regm = Slot(uri=DEFAULT_.watering_regm, name="watering_regm", curie=DEFAULT_.curie('watering_regm'),
                   model_uri=DEFAULT_.watering_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.watering_regm])

slots.particle_class = Slot(uri=DEFAULT_.particle_class, name="particle_class", curie=DEFAULT_.curie('particle_class'),
                   model_uri=DEFAULT_.particle_class, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.particle_class])

slots.sediment_type = Slot(uri=DEFAULT_.sediment_type, name="sediment_type", curie=DEFAULT_.curie('sediment_type'),
                   model_uri=DEFAULT_.sediment_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.sediment_type],
                   pattern=re.compile(r'[biogenous|cosmogenous|hydrogenous|lithogenous]'))

slots.tidal_stage = Slot(uri=DEFAULT_.tidal_stage, name="tidal_stage", curie=DEFAULT_.curie('tidal_stage'),
                   model_uri=DEFAULT_.tidal_stage, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.tidal_stage],
                   pattern=re.compile(r'[low tide|ebb tide|flood tide|high tide]'))

slots.tot_depth_water_col = Slot(uri=DEFAULT_.tot_depth_water_col, name="tot_depth_water_col", curie=DEFAULT_.curie('tot_depth_water_col'),
                   model_uri=DEFAULT_.tot_depth_water_col, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_depth_water_col],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.cur_land_use = Slot(uri=DEFAULT_.cur_land_use, name="cur_land_use", curie=DEFAULT_.curie('cur_land_use'),
                   model_uri=DEFAULT_.cur_land_use, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.cur_land_use],
                   pattern=re.compile(r'[cities|farmstead|industrial areas|roads\/railroads|rock|sand|gravel|mudflats|salt flats|badlands|permanent snow or ice|saline seeps|mines\/quarries|oil waste areas|small grains|row crops|vegetable crops|horticultural plants (e.g. tulips)|marshlands (grass,sedges,rushes)|tundra (mosses,lichens)|rangeland|pastureland (grasslands used for livestock grazing)|hayland|meadows (grasses,alfalfa,fescue,bromegrass,timothy)|shrub land (e.g. mesquite,sage\-brush,creosote bush,shrub oak,eucalyptus)|successional shrub land (tree saplings,hazels,sumacs,chokecherry,shrub dogwoods,blackberries)|shrub crops (blueberries,nursery ornamentals,filberts)|vine crops (grapes)|conifers (e.g. pine,spruce,fir,cypress)|hardwoods (e.g. oak,hickory,elm,aspen)|intermixed hardwood and conifers|tropical (e.g. mangrove,palms)|rainforest (evergreen forest receiving >406 cm annual rainfall)|swamp (permanent or semi\-permanent water body dominated by woody plants)|crop trees (nuts,fruit,christmas trees,nursery trees)]'))

slots.cur_vegetation = Slot(uri=DEFAULT_.cur_vegetation, name="cur_vegetation", curie=DEFAULT_.curie('cur_vegetation'),
                   model_uri=DEFAULT_.cur_vegetation, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.cur_vegetation])

slots.cur_vegetation_meth = Slot(uri=DEFAULT_.cur_vegetation_meth, name="cur_vegetation_meth", curie=DEFAULT_.curie('cur_vegetation_meth'),
                   model_uri=DEFAULT_.cur_vegetation_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.cur_vegetation_meth])

slots.previous_land_use = Slot(uri=DEFAULT_.previous_land_use, name="previous_land_use", curie=DEFAULT_.curie('previous_land_use'),
                   model_uri=DEFAULT_.previous_land_use, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.previous_land_use])

slots.previous_land_use_meth = Slot(uri=DEFAULT_.previous_land_use_meth, name="previous_land_use_meth", curie=DEFAULT_.curie('previous_land_use_meth'),
                   model_uri=DEFAULT_.previous_land_use_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.previous_land_use_meth])

slots.crop_rotation = Slot(uri=DEFAULT_.crop_rotation, name="crop_rotation", curie=DEFAULT_.curie('crop_rotation'),
                   model_uri=DEFAULT_.crop_rotation, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.crop_rotation])

slots.agrochem_addition = Slot(uri=DEFAULT_.agrochem_addition, name="agrochem_addition", curie=DEFAULT_.curie('agrochem_addition'),
                   model_uri=DEFAULT_.agrochem_addition, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.agrochem_addition])

slots.tillage = Slot(uri=DEFAULT_.tillage, name="tillage", curie=DEFAULT_.curie('tillage'),
                   model_uri=DEFAULT_.tillage, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.tillage],
                   pattern=re.compile(r'[drill|cutting disc|ridge till|strip tillage|zonal tillage|chisel|tined|mouldboard|disc plough]'))

slots.fire = Slot(uri=DEFAULT_.fire, name="fire", curie=DEFAULT_.curie('fire'),
                   model_uri=DEFAULT_.fire, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.fire])

slots.flooding = Slot(uri=DEFAULT_.flooding, name="flooding", curie=DEFAULT_.curie('flooding'),
                   model_uri=DEFAULT_.flooding, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.flooding])

slots.extreme_event = Slot(uri=DEFAULT_.extreme_event, name="extreme_event", curie=DEFAULT_.curie('extreme_event'),
                   model_uri=DEFAULT_.extreme_event, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.extreme_event])

slots.horizon = Slot(uri=DEFAULT_.horizon, name="horizon", curie=DEFAULT_.curie('horizon'),
                   model_uri=DEFAULT_.horizon, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.horizon],
                   pattern=re.compile(r'[O horizon|A horizon|E horizon|B horizon|C horizon|R layer|Permafrost]'))

slots.horizon_meth = Slot(uri=DEFAULT_.horizon_meth, name="horizon_meth", curie=DEFAULT_.curie('horizon_meth'),
                   model_uri=DEFAULT_.horizon_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.horizon_meth])

slots.sieving = Slot(uri=DEFAULT_.sieving, name="sieving", curie=DEFAULT_.curie('sieving'),
                   model_uri=DEFAULT_.sieving, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.sieving])

slots.water_content_soil_meth = Slot(uri=DEFAULT_.water_content_soil_meth, name="water_content_soil_meth", curie=DEFAULT_.curie('water_content_soil_meth'),
                   model_uri=DEFAULT_.water_content_soil_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.water_content_soil_meth])

slots.pool_dna_extracts = Slot(uri=DEFAULT_.pool_dna_extracts, name="pool_dna_extracts", curie=DEFAULT_.curie('pool_dna_extracts'),
                   model_uri=DEFAULT_.pool_dna_extracts, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.pool_dna_extracts])

slots.store_cond = Slot(uri=DEFAULT_.store_cond, name="store_cond", curie=DEFAULT_.curie('store_cond'),
                   model_uri=DEFAULT_.store_cond, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.store_cond])

slots.link_climate_info = Slot(uri=DEFAULT_.link_climate_info, name="link_climate_info", curie=DEFAULT_.curie('link_climate_info'),
                   model_uri=DEFAULT_.link_climate_info, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.link_climate_info])

slots.annual_temp = Slot(uri=DEFAULT_.annual_temp, name="annual_temp", curie=DEFAULT_.curie('annual_temp'),
                   model_uri=DEFAULT_.annual_temp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.annual_temp],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.season_temp = Slot(uri=DEFAULT_.season_temp, name="season_temp", curie=DEFAULT_.curie('season_temp'),
                   model_uri=DEFAULT_.season_temp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.season_temp],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.annual_precpt = Slot(uri=DEFAULT_.annual_precpt, name="annual_precpt", curie=DEFAULT_.curie('annual_precpt'),
                   model_uri=DEFAULT_.annual_precpt, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.annual_precpt],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.season_precpt = Slot(uri=DEFAULT_.season_precpt, name="season_precpt", curie=DEFAULT_.curie('season_precpt'),
                   model_uri=DEFAULT_.season_precpt, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.season_precpt],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.link_class_info = Slot(uri=DEFAULT_.link_class_info, name="link_class_info", curie=DEFAULT_.curie('link_class_info'),
                   model_uri=DEFAULT_.link_class_info, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.link_class_info])

slots.fao_class = Slot(uri=DEFAULT_.fao_class, name="fao_class", curie=DEFAULT_.curie('fao_class'),
                   model_uri=DEFAULT_.fao_class, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.fao_class],
                   pattern=re.compile(r'[Acrisols|Andosols|Arenosols|Cambisols|Chernozems|Ferralsols|Fluvisols|Gleysols|Greyzems|Gypsisols|Histosols|Kastanozems|Lithosols|Luvisols|Nitosols|Phaeozems|Planosols|Podzols|Podzoluvisols|Rankers|Regosols|Rendzinas|Solonchaks|Solonetz|Vertisols|Yermosols]'))

slots.local_class = Slot(uri=DEFAULT_.local_class, name="local_class", curie=DEFAULT_.curie('local_class'),
                   model_uri=DEFAULT_.local_class, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.local_class])

slots.local_class_meth = Slot(uri=DEFAULT_.local_class_meth, name="local_class_meth", curie=DEFAULT_.curie('local_class_meth'),
                   model_uri=DEFAULT_.local_class_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.local_class_meth])

slots.soil_type = Slot(uri=DEFAULT_.soil_type, name="soil_type", curie=DEFAULT_.curie('soil_type'),
                   model_uri=DEFAULT_.soil_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.soil_type])

slots.soil_type_meth = Slot(uri=DEFAULT_.soil_type_meth, name="soil_type_meth", curie=DEFAULT_.curie('soil_type_meth'),
                   model_uri=DEFAULT_.soil_type_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.soil_type_meth])

slots.slope_gradient = Slot(uri=DEFAULT_.slope_gradient, name="slope_gradient", curie=DEFAULT_.curie('slope_gradient'),
                   model_uri=DEFAULT_.slope_gradient, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.slope_gradient],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.slope_aspect = Slot(uri=DEFAULT_.slope_aspect, name="slope_aspect", curie=DEFAULT_.curie('slope_aspect'),
                   model_uri=DEFAULT_.slope_aspect, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.slope_aspect],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.profile_position = Slot(uri=DEFAULT_.profile_position, name="profile_position", curie=DEFAULT_.curie('profile_position'),
                   model_uri=DEFAULT_.profile_position, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.profile_position],
                   pattern=re.compile(r'[summit|shoulder|backslope|footslope|toeslope]'))

slots.drainage_class = Slot(uri=DEFAULT_.drainage_class, name="drainage_class", curie=DEFAULT_.curie('drainage_class'),
                   model_uri=DEFAULT_.drainage_class, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.drainage_class],
                   pattern=re.compile(r'[very poorly|poorly|somewhat poorly|moderately well|well|excessively drained]'))

slots.texture = Slot(uri=DEFAULT_.texture, name="texture", curie=DEFAULT_.curie('texture'),
                   model_uri=DEFAULT_.texture, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.texture],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.texture_meth = Slot(uri=DEFAULT_.texture_meth, name="texture_meth", curie=DEFAULT_.curie('texture_meth'),
                   model_uri=DEFAULT_.texture_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.texture_meth])

slots.ph_meth = Slot(uri=DEFAULT_.ph_meth, name="ph_meth", curie=DEFAULT_.curie('ph_meth'),
                   model_uri=DEFAULT_.ph_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ph_meth])

slots.tot_org_c_meth = Slot(uri=DEFAULT_.tot_org_c_meth, name="tot_org_c_meth", curie=DEFAULT_.curie('tot_org_c_meth'),
                   model_uri=DEFAULT_.tot_org_c_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.tot_org_c_meth])

slots.tot_nitro_content_meth = Slot(uri=DEFAULT_.tot_nitro_content_meth, name="tot_nitro_content_meth", curie=DEFAULT_.curie('tot_nitro_content_meth'),
                   model_uri=DEFAULT_.tot_nitro_content_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.tot_nitro_content_meth])

slots.microbial_biomass = Slot(uri=DEFAULT_.microbial_biomass, name="microbial_biomass", curie=DEFAULT_.curie('microbial_biomass'),
                   model_uri=DEFAULT_.microbial_biomass, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.microbial_biomass],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.microbial_biomass_meth = Slot(uri=DEFAULT_.microbial_biomass_meth, name="microbial_biomass_meth", curie=DEFAULT_.curie('microbial_biomass_meth'),
                   model_uri=DEFAULT_.microbial_biomass_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.microbial_biomass_meth])

slots.link_addit_analys = Slot(uri=DEFAULT_.link_addit_analys, name="link_addit_analys", curie=DEFAULT_.curie('link_addit_analys'),
                   model_uri=DEFAULT_.link_addit_analys, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.link_addit_analys])

slots.extreme_salinity = Slot(uri=DEFAULT_.extreme_salinity, name="extreme_salinity", curie=DEFAULT_.curie('extreme_salinity'),
                   model_uri=DEFAULT_.extreme_salinity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.extreme_salinity],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.salinity_meth = Slot(uri=DEFAULT_.salinity_meth, name="salinity_meth", curie=DEFAULT_.curie('salinity_meth'),
                   model_uri=DEFAULT_.salinity_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.salinity_meth])

slots.heavy_metals = Slot(uri=DEFAULT_.heavy_metals, name="heavy_metals", curie=DEFAULT_.curie('heavy_metals'),
                   model_uri=DEFAULT_.heavy_metals, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.heavy_metals])

slots.heavy_metals_meth = Slot(uri=DEFAULT_.heavy_metals_meth, name="heavy_metals_meth", curie=DEFAULT_.curie('heavy_metals_meth'),
                   model_uri=DEFAULT_.heavy_metals_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.heavy_metals_meth])

slots.al_sat = Slot(uri=DEFAULT_.al_sat, name="al_sat", curie=DEFAULT_.curie('al_sat'),
                   model_uri=DEFAULT_.al_sat, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.al_sat],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.al_sat_meth = Slot(uri=DEFAULT_.al_sat_meth, name="al_sat_meth", curie=DEFAULT_.curie('al_sat_meth'),
                   model_uri=DEFAULT_.al_sat_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.al_sat_meth])

slots.biochem_oxygen_dem = Slot(uri=DEFAULT_.biochem_oxygen_dem, name="biochem_oxygen_dem", curie=DEFAULT_.curie('biochem_oxygen_dem'),
                   model_uri=DEFAULT_.biochem_oxygen_dem, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.biochem_oxygen_dem],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.chem_oxygen_dem = Slot(uri=DEFAULT_.chem_oxygen_dem, name="chem_oxygen_dem", curie=DEFAULT_.curie('chem_oxygen_dem'),
                   model_uri=DEFAULT_.chem_oxygen_dem, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.chem_oxygen_dem],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.efficiency_percent = Slot(uri=DEFAULT_.efficiency_percent, name="efficiency_percent", curie=DEFAULT_.curie('efficiency_percent'),
                   model_uri=DEFAULT_.efficiency_percent, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.efficiency_percent],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.emulsions = Slot(uri=DEFAULT_.emulsions, name="emulsions", curie=DEFAULT_.curie('emulsions'),
                   model_uri=DEFAULT_.emulsions, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.emulsions])

slots.gaseous_substances = Slot(uri=DEFAULT_.gaseous_substances, name="gaseous_substances", curie=DEFAULT_.curie('gaseous_substances'),
                   model_uri=DEFAULT_.gaseous_substances, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.gaseous_substances])

slots.indust_eff_percent = Slot(uri=DEFAULT_.indust_eff_percent, name="indust_eff_percent", curie=DEFAULT_.curie('indust_eff_percent'),
                   model_uri=DEFAULT_.indust_eff_percent, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.indust_eff_percent],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.inorg_particles = Slot(uri=DEFAULT_.inorg_particles, name="inorg_particles", curie=DEFAULT_.curie('inorg_particles'),
                   model_uri=DEFAULT_.inorg_particles, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.inorg_particles])

slots.org_particles = Slot(uri=DEFAULT_.org_particles, name="org_particles", curie=DEFAULT_.curie('org_particles'),
                   model_uri=DEFAULT_.org_particles, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.org_particles])

slots.pre_treatment = Slot(uri=DEFAULT_.pre_treatment, name="pre_treatment", curie=DEFAULT_.curie('pre_treatment'),
                   model_uri=DEFAULT_.pre_treatment, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.pre_treatment])

slots.primary_treatment = Slot(uri=DEFAULT_.primary_treatment, name="primary_treatment", curie=DEFAULT_.curie('primary_treatment'),
                   model_uri=DEFAULT_.primary_treatment, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.primary_treatment])

slots.reactor_type = Slot(uri=DEFAULT_.reactor_type, name="reactor_type", curie=DEFAULT_.curie('reactor_type'),
                   model_uri=DEFAULT_.reactor_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.reactor_type])

slots.secondary_treatment = Slot(uri=DEFAULT_.secondary_treatment, name="secondary_treatment", curie=DEFAULT_.curie('secondary_treatment'),
                   model_uri=DEFAULT_.secondary_treatment, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.secondary_treatment])

slots.sewage_type = Slot(uri=DEFAULT_.sewage_type, name="sewage_type", curie=DEFAULT_.curie('sewage_type'),
                   model_uri=DEFAULT_.sewage_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.sewage_type])

slots.sludge_retent_time = Slot(uri=DEFAULT_.sludge_retent_time, name="sludge_retent_time", curie=DEFAULT_.curie('sludge_retent_time'),
                   model_uri=DEFAULT_.sludge_retent_time, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.sludge_retent_time],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.soluble_inorg_mat = Slot(uri=DEFAULT_.soluble_inorg_mat, name="soluble_inorg_mat", curie=DEFAULT_.curie('soluble_inorg_mat'),
                   model_uri=DEFAULT_.soluble_inorg_mat, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.soluble_inorg_mat])

slots.soluble_org_mat = Slot(uri=DEFAULT_.soluble_org_mat, name="soluble_org_mat", curie=DEFAULT_.curie('soluble_org_mat'),
                   model_uri=DEFAULT_.soluble_org_mat, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.soluble_org_mat])

slots.tertiary_treatment = Slot(uri=DEFAULT_.tertiary_treatment, name="tertiary_treatment", curie=DEFAULT_.curie('tertiary_treatment'),
                   model_uri=DEFAULT_.tertiary_treatment, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.tertiary_treatment])

slots.tot_phosphate = Slot(uri=DEFAULT_.tot_phosphate, name="tot_phosphate", curie=DEFAULT_.curie('tot_phosphate'),
                   model_uri=DEFAULT_.tot_phosphate, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_phosphate],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.wastewater_type = Slot(uri=DEFAULT_.wastewater_type, name="wastewater_type", curie=DEFAULT_.curie('wastewater_type'),
                   model_uri=DEFAULT_.wastewater_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.wastewater_type])

slots.atmospheric_data = Slot(uri=DEFAULT_.atmospheric_data, name="atmospheric_data", curie=DEFAULT_.curie('atmospheric_data'),
                   model_uri=DEFAULT_.atmospheric_data, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.atmospheric_data])

slots.bac_prod = Slot(uri=DEFAULT_.bac_prod, name="bac_prod", curie=DEFAULT_.curie('bac_prod'),
                   model_uri=DEFAULT_.bac_prod, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.bac_prod],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.bac_resp = Slot(uri=DEFAULT_.bac_resp, name="bac_resp", curie=DEFAULT_.curie('bac_resp'),
                   model_uri=DEFAULT_.bac_resp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.bac_resp],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.conduc = Slot(uri=DEFAULT_.conduc, name="conduc", curie=DEFAULT_.curie('conduc'),
                   model_uri=DEFAULT_.conduc, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.conduc],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.diss_inorg_nitro = Slot(uri=DEFAULT_.diss_inorg_nitro, name="diss_inorg_nitro", curie=DEFAULT_.curie('diss_inorg_nitro'),
                   model_uri=DEFAULT_.diss_inorg_nitro, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diss_inorg_nitro],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.down_par = Slot(uri=DEFAULT_.down_par, name="down_par", curie=DEFAULT_.curie('down_par'),
                   model_uri=DEFAULT_.down_par, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.down_par],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.fluor = Slot(uri=DEFAULT_.fluor, name="fluor", curie=DEFAULT_.curie('fluor'),
                   model_uri=DEFAULT_.fluor, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.fluor],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.light_intensity = Slot(uri=DEFAULT_.light_intensity, name="light_intensity", curie=DEFAULT_.curie('light_intensity'),
                   model_uri=DEFAULT_.light_intensity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.light_intensity],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.part_org_nitro = Slot(uri=DEFAULT_.part_org_nitro, name="part_org_nitro", curie=DEFAULT_.curie('part_org_nitro'),
                   model_uri=DEFAULT_.part_org_nitro, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.part_org_nitro],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.photon_flux = Slot(uri=DEFAULT_.photon_flux, name="photon_flux", curie=DEFAULT_.curie('photon_flux'),
                   model_uri=DEFAULT_.photon_flux, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.photon_flux],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.primary_prod = Slot(uri=DEFAULT_.primary_prod, name="primary_prod", curie=DEFAULT_.curie('primary_prod'),
                   model_uri=DEFAULT_.primary_prod, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.primary_prod],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.size_frac_low = Slot(uri=DEFAULT_.size_frac_low, name="size_frac_low", curie=DEFAULT_.curie('size_frac_low'),
                   model_uri=DEFAULT_.size_frac_low, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.size_frac_low],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.size_frac_up = Slot(uri=DEFAULT_.size_frac_up, name="size_frac_up", curie=DEFAULT_.curie('size_frac_up'),
                   model_uri=DEFAULT_.size_frac_up, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.size_frac_up],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.soluble_react_phosp = Slot(uri=DEFAULT_.soluble_react_phosp, name="soluble_react_phosp", curie=DEFAULT_.curie('soluble_react_phosp'),
                   model_uri=DEFAULT_.soluble_react_phosp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.soluble_react_phosp],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.suspend_part_matter = Slot(uri=DEFAULT_.suspend_part_matter, name="suspend_part_matter", curie=DEFAULT_.curie('suspend_part_matter'),
                   model_uri=DEFAULT_.suspend_part_matter, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.suspend_part_matter],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.tot_diss_nitro = Slot(uri=DEFAULT_.tot_diss_nitro, name="tot_diss_nitro", curie=DEFAULT_.curie('tot_diss_nitro'),
                   model_uri=DEFAULT_.tot_diss_nitro, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_diss_nitro],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.tot_inorg_nitro = Slot(uri=DEFAULT_.tot_inorg_nitro, name="tot_inorg_nitro", curie=DEFAULT_.curie('tot_inorg_nitro'),
                   model_uri=DEFAULT_.tot_inorg_nitro, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_inorg_nitro],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

slots.tot_part_carb = Slot(uri=DEFAULT_.tot_part_carb, name="tot_part_carb", curie=DEFAULT_.curie('tot_part_carb'),
                   model_uri=DEFAULT_.tot_part_carb, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_part_carb],
                   pattern=re.compile(r'\d+[.\d+] \S+'))

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
