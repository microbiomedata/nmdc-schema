# Slot: part_of


_Links a resource to another resource that either logically or physically includes it._



URI: [dcterms:isPartOf](http://purl.org/dc/terms/isPartOf)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FieldResearchSite](FieldResearchSite.md) | A site, outside of a laboratory, from which biosamples may be collected |  no  |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |
[Study](Study.md) | A study summarizes the overall goal of a research initiative and outlines the... |  yes  |
[OmicsProcessing](OmicsProcessing.md) | The methods and processes used to generate omics data from a biosample or org... |  yes  |
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







## Properties

* Range: [NamedThing](NamedThing.md)

* Multivalued: True



## Aliases


* is part of



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: part_of
description: Links a resource to another resource that either logically or physically
  includes it.
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- is part of
rank: 1000
domain: NamedThing
slot_uri: dcterms:isPartOf
multivalued: true
alias: part_of
domain_of:
- FieldResearchSite
- Biosample
- Study
- OmicsProcessing
- WorkflowExecutionActivity
range: NamedThing

```
</details>