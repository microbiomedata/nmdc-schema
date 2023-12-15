# Slot: has_input


_An input to a process._



URI: [nmdc:has_input](https://w3id.org/nmdc/has_input)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BiosampleProcessing](BiosampleProcessing.md) | A process that takes one or more biosamples as inputs and generates one or mo... |  yes  |
[OmicsProcessing](OmicsProcessing.md) | The methods and processes used to generate omics data from a biosample or org... |  yes  |
[WorkflowExecutionActivity](WorkflowExecutionActivity.md) | Represents an instance of an execution of a particular workflow |  yes  |
[PlannedProcess](PlannedProcess.md) |  |  no  |
[Pooling](Pooling.md) | physical combination of several instances of like material |  yes  |
[Extraction](Extraction.md) | A material separation in which a desired component of an input material is se... |  yes  |
[LibraryPreparation](LibraryPreparation.md) |  |  yes  |
[CollectingBiosamplesFromSite](CollectingBiosamplesFromSite.md) |  |  yes  |
[SubSamplingProcess](SubSamplingProcess.md) | Separating a sample aliquot from the starting material for downstream activit... |  yes  |
[MixingProcess](MixingProcess.md) | The combining of components, particles or layers into a more homogeneous stat... |  yes  |
[FiltrationProcess](FiltrationProcess.md) | The process of segregation of phases; e |  no  |
[ChromatographicSeparationProcess](ChromatographicSeparationProcess.md) | The process of using a selective partitioning of the analyte or interferent b... |  yes  |
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







## Properties

* Range: [NamedThing](NamedThing.md)

* Multivalued: True



## Aliases


* input



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: has_input
description: An input to a process.
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- input
rank: 1000
domain: NamedThing
multivalued: true
alias: has_input
domain_of:
- BiosampleProcessing
- OmicsProcessing
- WorkflowExecutionActivity
- PlannedProcess
range: NamedThing

```
</details>