# Slot: designated_class

URI: [nmdc:designated_class](https://w3id.org/nmdc/designated_class)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[PlannedProcess](PlannedProcess.md) |  |  yes  |
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

* Range: [Uriorcurie](Uriorcurie.md)





## See Also

* [https://github.com/microbiomedata/nmdc-schema/issues/1048](https://github.com/microbiomedata/nmdc-schema/issues/1048)
* [https://github.com/microbiomedata/nmdc-schema/issues/1233](https://github.com/microbiomedata/nmdc-schema/issues/1233)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: designated_class
notes:
- MAM prefers to use this functionality in a `type` class and to eliminate '...type...'
  from the names of any NMDC-owned elements
- this would be required on all instances in a polymorphic Database slot, like planned_process_set
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- https://github.com/microbiomedata/nmdc-schema/issues/1048
- https://github.com/microbiomedata/nmdc-schema/issues/1233
rank: 1000
designates_type: true
alias: designated_class
domain_of:
- PlannedProcess
range: uriorcurie

```
</details>