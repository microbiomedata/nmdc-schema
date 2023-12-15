# Slot: total iron (tot_iron)


_Concentration of total iron in the sample_



URI: [MIXS:0000105](https://w3id.org/mixs/0000105)




## Inheritance

* [core_field](core_field.md)
    * **tot_iron**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* total iron




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | milligram per liter, milligram per kilogram || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: tot_iron
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: milligram per liter, milligram per kilogram
  occurrence:
    tag: occurrence
    value: '1'
description: Concentration of total iron in the sample
title: total iron
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- total iron
rank: 1000
is_a: core field
slot_uri: MIXS:0000105
multivalued: false
alias: tot_iron
domain_of:
- Biosample
range: QuantityValue

```
</details>