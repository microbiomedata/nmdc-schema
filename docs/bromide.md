# Slot: bromide (bromide)


_Concentration of bromide_



URI: [MIXS:0000176](https://w3id.org/mixs/0000176)




## Inheritance

* [core_field](core_field.md)
    * **bromide**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* bromide




## Examples

| Value |
| --- |
| 0.05 parts per million |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | parts per million || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: bromide
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: parts per million
  occurrence:
    tag: occurrence
    value: '1'
description: Concentration of bromide
title: bromide
examples:
- value: 0.05 parts per million
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- bromide
rank: 1000
is_a: core field
slot_uri: MIXS:0000176
multivalued: false
alias: bromide
domain_of:
- Biosample
range: QuantityValue

```
</details>