# Slot: filter method (filter_method)


_Type of filter used or how the sample was filtered_



URI: [nmdc:filter_method](https://w3id.org/nmdc/filter_method)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [String](String.md)

* Recommended: True






## Examples

| Value |
| --- |
| C18 |
| Basix PES, 13-100-106 FisherSci |

## Comments

* describe the filter or provide a catalog number and manufacturer

## See Also

* [MIXS:0000765](https://w3id.org/mixs/0000765)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: filter_method
description: Type of filter used or how the sample was filtered
title: filter method
comments:
- describe the filter or provide a catalog number and manufacturer
examples:
- value: C18
- value: Basix PES, 13-100-106 FisherSci
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- MIXS:0000765
rank: 6
string_serialization: '{text}'
alias: filter_method
domain_of:
- Biosample
slot_group: MIxS Inspired
range: string
recommended: true

```
</details>