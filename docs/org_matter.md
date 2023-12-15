# Slot: organic matter (org_matter)


_Concentration of organic matter_



URI: [MIXS:0000204](https://w3id.org/mixs/0000204)




## Inheritance

* [core_field](core_field.md)
    * **org_matter**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* organic matter




## Examples

| Value |
| --- |
| 1.75 milligram per cubic meter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | microgram per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: org_matter
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: microgram per liter
  occurrence:
    tag: occurrence
    value: '1'
description: Concentration of organic matter
title: organic matter
examples:
- value: 1.75 milligram per cubic meter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- organic matter
rank: 1000
is_a: core field
slot_uri: MIXS:0000204
multivalued: false
alias: org_matter
domain_of:
- Biosample
range: QuantityValue

```
</details>