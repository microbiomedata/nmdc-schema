# Slot: organism count (organism_count)


_Total cell count of any organism (or group of organisms) per gram, volume or area of sample, should include name of organism followed by count. The method that was used for the enumeration (e.g. qPCR, atp, mpn, etc.) Should also be provided. (example: total prokaryotes; 3.5e7 cells per ml; qpcr)_



URI: [MIXS:0000103](https://w3id.org/mixs/0000103)




## Inheritance

* [core_field](core_field.md)
    * **organism_count**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)

* Multivalued: True



## Aliases


* organism count




## Examples

| Value |
| --- |
| total prokaryotes;3.5e7 cells per milliliter;qPCR |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | organism name;measurement value;enumeration || preferred_unit | number of cells per cubic meter, number of cells per milliliter, number of cells per cubic centimeter || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: organism_count
annotations:
  expected_value:
    tag: expected_value
    value: organism name;measurement value;enumeration
  preferred_unit:
    tag: preferred_unit
    value: number of cells per cubic meter, number of cells per milliliter, number
      of cells per cubic centimeter
  occurrence:
    tag: occurrence
    value: m
description: 'Total cell count of any organism (or group of organisms) per gram, volume
  or area of sample, should include name of organism followed by count. The method
  that was used for the enumeration (e.g. qPCR, atp, mpn, etc.) Should also be provided.
  (example: total prokaryotes; 3.5e7 cells per ml; qpcr)'
title: organism count
examples:
- value: total prokaryotes;3.5e7 cells per milliliter;qPCR
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- organism count
rank: 1000
is_a: core field
slot_uri: MIXS:0000103
multivalued: true
alias: organism_count
domain_of:
- Biosample
range: QuantityValue

```
</details>