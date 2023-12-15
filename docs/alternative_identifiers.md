# Slot: alternative_identifiers


_A list of alternative identifiers for the entity._



URI: [nmdc:alternative_identifiers](https://w3id.org/nmdc/alternative_identifiers)




## Inheritance

* **alternative_identifiers**
    * [external_database_identifiers](external_database_identifiers.md)





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |
[Study](Study.md) | A study summarizes the overall goal of a research initiative and outlines the... |  yes  |
[NamedThing](NamedThing.md) | a databased entity or concept/class |  no  |
[MetaboliteQuantification](MetaboliteQuantification.md) | This is used to link a metabolomics analysis workflow to a specific metabolit... |  no  |
[Pooling](Pooling.md) | physical combination of several instances of like material |  no  |
[Extraction](Extraction.md) | A material separation in which a desired component of an input material is se... |  no  |
[LibraryPreparation](LibraryPreparation.md) |  |  no  |
[FieldResearchSite](FieldResearchSite.md) | A site, outside of a laboratory, from which biosamples may be collected |  no  |
[CollectingBiosamplesFromSite](CollectingBiosamplesFromSite.md) |  |  no  |
[DataObject](DataObject.md) | An object that primarily consists of symbols that represent information |  no  |
[BiosampleProcessing](BiosampleProcessing.md) | A process that takes one or more biosamples as inputs and generates one or mo... |  no  |
[SubSamplingProcess](SubSamplingProcess.md) | Separating a sample aliquot from the starting material for downstream activit... |  no  |
[MixingProcess](MixingProcess.md) | The combining of components, particles or layers into a more homogeneous stat... |  no  |
[FiltrationProcess](FiltrationProcess.md) | The process of segregation of phases; e |  no  |
[ChromatographicSeparationProcess](ChromatographicSeparationProcess.md) | The process of using a selective partitioning of the analyte or interferent b... |  no  |
[OmicsProcessing](OmicsProcessing.md) | The methods and processes used to generate omics data from a biosample or org... |  no  |
[MaterialEntity](MaterialEntity.md) |  |  no  |
[ProcessedSample](ProcessedSample.md) |  |  no  |
[AnalyticalSample](AnalyticalSample.md) |  |  no  |
[Site](Site.md) |  |  no  |
[PlannedProcess](PlannedProcess.md) |  |  no  |
[OntologyClass](OntologyClass.md) |  |  no  |
[EnvironmentalMaterialTerm](EnvironmentalMaterialTerm.md) |  |  no  |
[ChemicalEntity](ChemicalEntity.md) | An atom or molecule that can be represented with a chemical formula |  no  |
[GeneProduct](GeneProduct.md) | A molecule encoded by a gene that has an evolved function |  no  |
[FunctionalAnnotationTerm](FunctionalAnnotationTerm.md) | Abstract grouping class for any term/descriptor that can be applied to a func... |  no  |
[Pathway](Pathway.md) | A pathway is a sequence of steps/reactions carried out by an organism or comm... |  no  |
[Reaction](Reaction.md) | An individual biochemical transformation carried out by a functional unit of ... |  no  |
[OrthologyGroup](OrthologyGroup.md) | A set of genes or gene products in which all members are orthologous |  no  |







## Properties

* Range: [Uriorcurie](Uriorcurie.md)

* Multivalued: True

* Regex pattern: `^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: alternative_identifiers
description: A list of alternative identifiers for the entity.
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
multivalued: true
alias: alternative_identifiers
domain_of:
- Biosample
- Study
- NamedThing
- MetaboliteQuantification
range: uriorcurie
pattern: ^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$

```
</details>