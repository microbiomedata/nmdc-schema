# Slot: start_date


_The date on which any process or activity was started_



URI: [nmdc:start_date](https://w3id.org/nmdc/start_date)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[PlannedProcess](PlannedProcess.md) |  |  no  |
[Pooling](Pooling.md) | physical combination of several instances of like material |  no  |
[Extraction](Extraction.md) | A material separation in which a desired component of an input material is se... |  no  |
[LibraryPreparation](LibraryPreparation.md) |  |  no  |
[CollectingBiosamplesFromSite](CollectingBiosamplesFromSite.md) |  |  no  |
[BiosampleProcessing](BiosampleProcessing.md) | A process that takes one or more biosamples as inputs and generates one or mo... |  no  |
[SubSamplingProcess](SubSamplingProcess.md) | Separating a sample aliquot from the starting material for downstream activit... |  no  |
[MixingProcess](MixingProcess.md) | The combining of components, particles or layers into a more homogeneous stat... |  no  |
[FiltrationProcess](FiltrationProcess.md) | The process of segregation of phases; e |  no  |
[ChromatographicSeparationProcess](ChromatographicSeparationProcess.md) | The process of using a selective partitioning of the analyte or interferent b... |  no  |
[OmicsProcessing](OmicsProcessing.md) | The methods and processes used to generate omics data from a biosample or org... |  no  |







## Properties

* Range: [String](String.md)





## Comments

* We are using string representations of dates until all components of our ecosystem can handle ISO 8610 dates
* The date should be formatted as YYYY-MM-DD

## TODOs

* add date string validation pattern

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: start_date
description: The date on which any process or activity was started
todos:
- add date string validation pattern
comments:
- We are using string representations of dates until all components of our ecosystem
  can handle ISO 8610 dates
- The date should be formatted as YYYY-MM-DD
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
alias: start_date
domain_of:
- PlannedProcess
range: string

```
</details>