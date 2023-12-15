# Slot: chloride (chloride)


_Concentration of chloride in the sample_



URI: [MIXS:0000429](https://w3id.org/mixs/0000429)




## Inheritance

* [core_field](core_field.md)
    * **chloride**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* chloride




## Examples

| Value |
| --- |
| 5000 milligram per liter |

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
name: chloride
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
description: Concentration of chloride in the sample
title: chloride
examples:
- value: 5000 milligram per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- chloride
rank: 1000
is_a: core field
slot_uri: MIXS:0000429
multivalued: false
alias: chloride
domain_of:
- Biosample
range: QuantityValue

```
</details>