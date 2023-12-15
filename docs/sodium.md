# Slot: sodium (sodium)


_Sodium concentration in the sample_



URI: [MIXS:0000428](https://w3id.org/mixs/0000428)




## Inheritance

* [core_field](core_field.md)
    * **sodium**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* sodium




## Examples

| Value |
| --- |
| 10.5 milligram per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | milligram per liter, parts per million || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: sodium
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: milligram per liter, parts per million
  occurrence:
    tag: occurrence
    value: '1'
description: Sodium concentration in the sample
title: sodium
examples:
- value: 10.5 milligram per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- sodium
rank: 1000
is_a: core field
slot_uri: MIXS:0000428
multivalued: false
alias: sodium
domain_of:
- Biosample
range: QuantityValue

```
</details>