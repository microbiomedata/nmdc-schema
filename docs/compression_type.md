# Slot: compression_type


_If provided, specifies the compression type_



URI: [nmdc:compression_type](https://w3id.org/nmdc/compression_type)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[DataObject](DataObject.md) | An object that primarily consists of symbols that represent information |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| gzip |

## TODOs

* consider setting the range to an enum

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: compression_type
description: If provided, specifies the compression type
todos:
- consider setting the range to an enum
examples:
- value: gzip
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
alias: compression_type
domain_of:
- DataObject
range: string

```
</details>