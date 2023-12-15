# Slot: type


_An optional string that specifies the type object.  This is used to allow for searches for different kinds of objects._



URI: [nmdc:type](https://w3id.org/nmdc/type)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[DataObject](DataObject.md) | An object that primarily consists of symbols that represent information |  no  |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |
[Study](Study.md) | A study summarizes the overall goal of a research initiative and outlines the... |  no  |
[OmicsProcessing](OmicsProcessing.md) | The methods and processes used to generate omics data from a biosample or org... |  no  |
[CreditAssociation](CreditAssociation.md) | This class supports binding associated researchers to studies |  no  |
[WorkflowExecutionActivity](WorkflowExecutionActivity.md) | Represents an instance of an execution of a particular workflow |  yes  |
[MetagenomeAssembly](MetagenomeAssembly.md) | A workflow execution activity that converts sequencing reads into an assemble... |  no  |
[MetagenomeAnnotationActivity](MetagenomeAnnotationActivity.md) | A workflow execution activity that provides functional and structural annotat... |  no  |
[MetatranscriptomeAnnotationActivity](MetatranscriptomeAnnotationActivity.md) |  |  no  |
[MetatranscriptomeActivity](MetatranscriptomeActivity.md) | A metatranscriptome activity that e |  no  |
[MagsAnalysisActivity](MagsAnalysisActivity.md) | A workflow execution activity that uses computational binning tools to group ... |  no  |
[ReadQcAnalysisActivity](ReadQcAnalysisActivity.md) | A workflow execution activity that performs quality control on raw Illumina r... |  no  |
[ReadBasedTaxonomyAnalysisActivity](ReadBasedTaxonomyAnalysisActivity.md) | A workflow execution activity that performs taxonomy classification using seq... |  no  |
[MagBin](MagBin.md) |  |  no  |
[GenomeFeature](GenomeFeature.md) | A feature localized to an interval along a genome |  yes  |
[MetatranscriptomeAssembly](MetatranscriptomeAssembly.md) |  |  no  |
[MetagenomeSequencingActivity](MetagenomeSequencingActivity.md) | Initial sequencing activity that precedes any analysis |  no  |
[MetabolomicsAnalysisActivity](MetabolomicsAnalysisActivity.md) |  |  no  |
[MetaproteomicsAnalysisActivity](MetaproteomicsAnalysisActivity.md) |  |  no  |
[NomAnalysisActivity](NomAnalysisActivity.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| nmdc:Biosample |
| nmdc:Study |

## See Also

* [https://github.com/microbiomedata/nmdc-schema/issues/1233](https://github.com/microbiomedata/nmdc-schema/issues/1233)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: type
description: An optional string that specifies the type object.  This is used to allow
  for searches for different kinds of objects.
deprecated: Due to confusion about what values are used for this slot, it is best
  not to use this slot. See https://github.com/microbiomedata/nmdc-schema/issues/248.
  MAM removed designates_type and rdf:type slot uri 2022-11-30
examples:
- value: nmdc:Biosample
- value: nmdc:Study
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- https://github.com/microbiomedata/nmdc-schema/issues/1233
rank: 1000
alias: type
domain_of:
- DataObject
- Biosample
- Study
- OmicsProcessing
- CreditAssociation
- WorkflowExecutionActivity
- MetagenomeAssembly
- MetagenomeAnnotationActivity
- MetatranscriptomeAnnotationActivity
- MetatranscriptomeActivity
- MagsAnalysisActivity
- ReadQcAnalysisActivity
- ReadBasedTaxonomyAnalysisActivity
- MagBin
- GenomeFeature
range: string

```
</details>