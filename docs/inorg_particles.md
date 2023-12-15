# Slot: inorganic particles (inorg_particles)


_Concentration of particles such as sand, grit, metal particles, ceramics, etc.; can include multiple particles_



URI: [MIXS:0000664](https://w3id.org/mixs/0000664)




## Inheritance

* [core_field](core_field.md)
    * **inorg_particles**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* inorganic particles




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | inorganic particle name;measurement value || preferred_unit | mole per liter, milligram per liter || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: inorg_particles
annotations:
  expected_value:
    tag: expected_value
    value: inorganic particle name;measurement value
  preferred_unit:
    tag: preferred_unit
    value: mole per liter, milligram per liter
  occurrence:
    tag: occurrence
    value: m
description: Concentration of particles such as sand, grit, metal particles, ceramics,
  etc.; can include multiple particles
title: inorganic particles
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- inorganic particles
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000664
multivalued: true
alias: inorg_particles
domain_of:
- Biosample
range: TextValue

```
</details>