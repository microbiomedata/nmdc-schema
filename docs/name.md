# Slot: name


_A human readable label for an entity_



URI: [nmdc:name](https://w3id.org/nmdc/name)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Protocol](Protocol.md) |  |  no  |
[QualityControlReport](QualityControlReport.md) |  |  no  |
[NamedThing](NamedThing.md) | a databased entity or concept/class |  no  |
[PersonValue](PersonValue.md) | An attribute value representing a person |  yes  |
[Activity](Activity.md) | Something that occurs over a period of time and acts upon or with entities; i... |  no  |
[Pooling](Pooling.md) | physical combination of several instances of like material |  no  |
[Extraction](Extraction.md) | A material separation in which a desired component of an input material is se... |  no  |
[LibraryPreparation](LibraryPreparation.md) |  |  no  |
[FieldResearchSite](FieldResearchSite.md) | A site, outside of a laboratory, from which biosamples may be collected |  no  |
[CollectingBiosamplesFromSite](CollectingBiosamplesFromSite.md) |  |  no  |
[DataObject](DataObject.md) | An object that primarily consists of symbols that represent information |  yes  |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |
[Study](Study.md) | A study summarizes the overall goal of a research initiative and outlines the... |  yes  |
[BiosampleProcessing](BiosampleProcessing.md) | A process that takes one or more biosamples as inputs and generates one or mo... |  no  |
[SubSamplingProcess](SubSamplingProcess.md) | Separating a sample aliquot from the starting material for downstream activit... |  no  |
[MixingProcess](MixingProcess.md) | The combining of components, particles or layers into a more homogeneous stat... |  no  |
[FiltrationProcess](FiltrationProcess.md) | The process of segregation of phases; e |  no  |
[ChromatographicSeparationProcess](ChromatographicSeparationProcess.md) | The process of using a selective partitioning of the analyte or interferent b... |  no  |
[OmicsProcessing](OmicsProcessing.md) | The methods and processes used to generate omics data from a biosample or org... |  no  |
[WorkflowExecutionActivity](WorkflowExecutionActivity.md) | Represents an instance of an execution of a particular workflow |  no  |
[MetagenomeAssembly](MetagenomeAssembly.md) | A workflow execution activity that converts sequencing reads into an assemble... |  no  |
[MetatranscriptomeAssembly](MetatranscriptomeAssembly.md) |  |  no  |
[MetagenomeAnnotationActivity](MetagenomeAnnotationActivity.md) | A workflow execution activity that provides functional and structural annotat... |  no  |
[MetatranscriptomeAnnotationActivity](MetatranscriptomeAnnotationActivity.md) |  |  no  |
[MetatranscriptomeActivity](MetatranscriptomeActivity.md) | A metatranscriptome activity that e |  no  |
[MagsAnalysisActivity](MagsAnalysisActivity.md) | A workflow execution activity that uses computational binning tools to group ... |  no  |
[MetagenomeSequencingActivity](MetagenomeSequencingActivity.md) | Initial sequencing activity that precedes any analysis |  no  |
[ReadQcAnalysisActivity](ReadQcAnalysisActivity.md) | A workflow execution activity that performs quality control on raw Illumina r... |  no  |
[ReadBasedTaxonomyAnalysisActivity](ReadBasedTaxonomyAnalysisActivity.md) | A workflow execution activity that performs taxonomy classification using seq... |  no  |
[MetabolomicsAnalysisActivity](MetabolomicsAnalysisActivity.md) |  |  no  |
[MetaproteomicsAnalysisActivity](MetaproteomicsAnalysisActivity.md) |  |  no  |
[NomAnalysisActivity](NomAnalysisActivity.md) |  |  no  |
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

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: name
description: A human readable label for an entity
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
alias: name
domain_of:
- Protocol
- QualityControlReport
- NamedThing
- PersonValue
- Activity
range: string

```
</details>