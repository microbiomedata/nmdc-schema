# Slot: nitrate (nitrate)


_Concentration of nitrate in the sample_



URI: [MIXS:0000425](https://w3id.org/mixs/0000425)




## Inheritance

* [core_field](core_field.md)
    * **nitrate**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* nitrate




## Examples

| Value |
| --- |
| 65 micromole per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | micromole per liter, milligram per liter, parts per million || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: nitrate
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: micromole per liter, milligram per liter, parts per million
  occurrence:
    tag: occurrence
    value: '1'
description: Concentration of nitrate in the sample
title: nitrate
examples:
- value: 65 micromole per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- nitrate
rank: 1000
is_a: core field
slot_uri: MIXS:0000425
multivalued: false
alias: nitrate
domain_of:
- Biosample
range: QuantityValue

```
</details>