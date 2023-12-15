# Slot: id


_A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_



URI: [nmdc:id](https://w3id.org/nmdc/id)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |
[Study](Study.md) | A study summarizes the overall goal of a research initiative and outlines the... |  yes  |
[NamedThing](NamedThing.md) | a databased entity or concept/class |  no  |
[Activity](Activity.md) | Something that occurs over a period of time and acts upon or with entities; i... |  yes  |
[Pooling](Pooling.md) | physical combination of several instances of like material |  yes  |
[Extraction](Extraction.md) | A material separation in which a desired component of an input material is se... |  yes  |
[LibraryPreparation](LibraryPreparation.md) |  |  yes  |
[FieldResearchSite](FieldResearchSite.md) | A site, outside of a laboratory, from which biosamples may be collected |  yes  |
[CollectingBiosamplesFromSite](CollectingBiosamplesFromSite.md) |  |  yes  |
[DataObject](DataObject.md) | An object that primarily consists of symbols that represent information |  yes  |
[BiosampleProcessing](BiosampleProcessing.md) | A process that takes one or more biosamples as inputs and generates one or mo... |  yes  |
[SubSamplingProcess](SubSamplingProcess.md) | Separating a sample aliquot from the starting material for downstream activit... |  no  |
[MixingProcess](MixingProcess.md) | The combining of components, particles or layers into a more homogeneous stat... |  no  |
[FiltrationProcess](FiltrationProcess.md) | The process of segregation of phases; e |  no  |
[ChromatographicSeparationProcess](ChromatographicSeparationProcess.md) | The process of using a selective partitioning of the analyte or interferent b... |  no  |
[OmicsProcessing](OmicsProcessing.md) | The methods and processes used to generate omics data from a biosample or org... |  yes  |
[WorkflowExecutionActivity](WorkflowExecutionActivity.md) | Represents an instance of an execution of a particular workflow |  yes  |
[MetagenomeAssembly](MetagenomeAssembly.md) | A workflow execution activity that converts sequencing reads into an assemble... |  yes  |
[MetatranscriptomeAssembly](MetatranscriptomeAssembly.md) |  |  yes  |
[MetagenomeAnnotationActivity](MetagenomeAnnotationActivity.md) | A workflow execution activity that provides functional and structural annotat... |  yes  |
[MetatranscriptomeAnnotationActivity](MetatranscriptomeAnnotationActivity.md) |  |  yes  |
[MetatranscriptomeActivity](MetatranscriptomeActivity.md) | A metatranscriptome activity that e |  yes  |
[MagsAnalysisActivity](MagsAnalysisActivity.md) | A workflow execution activity that uses computational binning tools to group ... |  yes  |
[MetagenomeSequencingActivity](MetagenomeSequencingActivity.md) | Initial sequencing activity that precedes any analysis |  yes  |
[ReadQcAnalysisActivity](ReadQcAnalysisActivity.md) | A workflow execution activity that performs quality control on raw Illumina r... |  yes  |
[ReadBasedTaxonomyAnalysisActivity](ReadBasedTaxonomyAnalysisActivity.md) | A workflow execution activity that performs taxonomy classification using seq... |  yes  |
[MetabolomicsAnalysisActivity](MetabolomicsAnalysisActivity.md) |  |  yes  |
[MetaproteomicsAnalysisActivity](MetaproteomicsAnalysisActivity.md) |  |  yes  |
[NomAnalysisActivity](NomAnalysisActivity.md) |  |  yes  |
[MaterialEntity](MaterialEntity.md) |  |  no  |
[ProcessedSample](ProcessedSample.md) |  |  yes  |
[AnalyticalSample](AnalyticalSample.md) |  |  yes  |
[Site](Site.md) |  |  yes  |
[PlannedProcess](PlannedProcess.md) |  |  no  |
[OntologyClass](OntologyClass.md) |  |  yes  |
[EnvironmentalMaterialTerm](EnvironmentalMaterialTerm.md) |  |  no  |
[ChemicalEntity](ChemicalEntity.md) | An atom or molecule that can be represented with a chemical formula |  no  |
[GeneProduct](GeneProduct.md) | A molecule encoded by a gene that has an evolved function |  no  |
[FunctionalAnnotationTerm](FunctionalAnnotationTerm.md) | Abstract grouping class for any term/descriptor that can be applied to a func... |  no  |
[Pathway](Pathway.md) | A pathway is a sequence of steps/reactions carried out by an organism or comm... |  no  |
[Reaction](Reaction.md) | An individual biochemical transformation carried out by a functional unit of ... |  no  |
[OrthologyGroup](OrthologyGroup.md) | A set of genes or gene products in which all members are orthologous |  no  |







## Properties

* Range: [Uriorcurie](Uriorcurie.md)

* Required: True

* Regex pattern: `^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$`






## Examples

| Value |
| --- |
| nmdc:mgmag-00-x012.1_7_c1 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: id
description: A unique identifier for a thing. Must be either a CURIE shorthand for
  a URI or a complete URI
notes:
- 'abstracted pattern: prefix:typecode-authshoulder-blade(.version)?(_seqsuffix)?'
- a minimum length of 3 characters is suggested for typecodes, but 1 or 2 characters
  will be accepted
- typecodes must correspond 1:1 to a class in the NMDC schema. this will be checked
  via per-class id slot usage assertions
- minting authority shoulders should probably be enumerated and checked in the pattern
examples:
- value: nmdc:mgmag-00-x012.1_7_c1
  description: https://github.com/microbiomedata/nmdc-schema/pull/499#discussion_r1018499248
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
identifier: true
alias: id
domain_of:
- Biosample
- Study
- NamedThing
- Activity
range: uriorcurie
required: true
pattern: ^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$

```
</details>