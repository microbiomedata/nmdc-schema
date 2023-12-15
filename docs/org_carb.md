# Slot: organic carbon (org_carb)


_Concentration of organic carbon_



URI: [MIXS:0000508](https://w3id.org/mixs/0000508)




## Inheritance

* [core_field](core_field.md)
    * **org_carb**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* organic carbon




## Examples

| Value |
| --- |
| 1.5 microgram per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | micromole per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: org_carb
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: micromole per liter
  occurrence:
    tag: occurrence
    value: '1'
description: Concentration of organic carbon
title: organic carbon
examples:
- value: 1.5 microgram per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- organic carbon
rank: 1000
is_a: core field
slot_uri: MIXS:0000508
multivalued: false
alias: org_carb
domain_of:
- Biosample
range: QuantityValue

```
</details>