# Slot: total phosphorus (tot_phosp)


_Total phosphorus concentration in the sample, calculated by: total phosphorus = total dissolved phosphorus + particulate phosphorus_



URI: [MIXS:0000117](https://w3id.org/mixs/0000117)




## Inheritance

* [core_field](core_field.md)
    * **tot_phosp**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* total phosphorus




## Examples

| Value |
| --- |
| 0.03 milligram per liter |

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
name: tot_phosp
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
description: 'Total phosphorus concentration in the sample, calculated by: total phosphorus
  = total dissolved phosphorus + particulate phosphorus'
title: total phosphorus
examples:
- value: 0.03 milligram per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- total phosphorus
rank: 1000
is_a: core field
slot_uri: MIXS:0000117
multivalued: false
alias: tot_phosp
domain_of:
- Biosample
range: QuantityValue

```
</details>