# Slot: suspended particulate matter (suspend_part_matter)


_Concentration of suspended particulate matter_



URI: [MIXS:0000741](https://w3id.org/mixs/0000741)




## Inheritance

* [core_field](core_field.md)
    * **suspend_part_matter**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* suspended particulate matter




## Examples

| Value |
| --- |
| 0.5 milligram per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | milligram per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: suspend_part_matter
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: milligram per liter
  occurrence:
    tag: occurrence
    value: '1'
description: Concentration of suspended particulate matter
title: suspended particulate matter
examples:
- value: 0.5 milligram per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- suspended particulate matter
rank: 1000
is_a: core field
slot_uri: MIXS:0000741
multivalued: false
alias: suspend_part_matter
domain_of:
- Biosample
range: QuantityValue

```
</details>