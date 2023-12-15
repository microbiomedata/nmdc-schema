# Slot: organic particles (org_particles)


_Concentration of particles such as faeces, hairs, food, vomit, paper fibers, plant material, humus, etc._



URI: [MIXS:0000665](https://w3id.org/mixs/0000665)




## Inheritance

* [core_field](core_field.md)
    * **org_particles**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* organic particles




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | particle name;measurement value || preferred_unit | gram per liter || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: org_particles
annotations:
  expected_value:
    tag: expected_value
    value: particle name;measurement value
  preferred_unit:
    tag: preferred_unit
    value: gram per liter
  occurrence:
    tag: occurrence
    value: m
description: Concentration of particles such as faeces, hairs, food, vomit, paper
  fibers, plant material, humus, etc.
title: organic particles
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- organic particles
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000665
multivalued: true
alias: org_particles
domain_of:
- Biosample
range: TextValue

```
</details>