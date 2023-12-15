# Slot: data_object_type


_The type of file represented by the data object._



URI: [nmdc:data_object_type](https://w3id.org/nmdc/data_object_type)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[DataObject](DataObject.md) | An object that primarily consists of symbols that represent information |  no  |







## Properties

* Range: [FileTypeEnum](FileTypeEnum.md)






## Examples

| Value |
| --- |
| FT ICR-MS Analysis Results |
| GC-MS Metabolomics Results |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: data_object_type
description: The type of file represented by the data object.
examples:
- value: FT ICR-MS Analysis Results
- value: GC-MS Metabolomics Results
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
domain: DataObject
alias: data_object_type
domain_of:
- DataObject
range: file type enum

```
</details>