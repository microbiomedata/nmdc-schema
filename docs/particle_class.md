# Slot: particle classification (particle_class)


_Particles are classified, based on their size, into six general categories:clay, silt, sand, gravel, cobbles, and boulders; should include amount of particle preceded by the name of the particle type; can include multiple values_



URI: [MIXS:0000206](https://w3id.org/mixs/0000206)




## Inheritance

* [core_field](core_field.md)
    * **particle_class**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* particle classification




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | particle name;measurement value || preferred_unit | micrometer || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: particle_class
annotations:
  expected_value:
    tag: expected_value
    value: particle name;measurement value
  preferred_unit:
    tag: preferred_unit
    value: micrometer
  occurrence:
    tag: occurrence
    value: m
description: Particles are classified, based on their size, into six general categories:clay,
  silt, sand, gravel, cobbles, and boulders; should include amount of particle preceded
  by the name of the particle type; can include multiple values
title: particle classification
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- particle classification
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000206
multivalued: true
alias: particle_class
domain_of:
- Biosample
range: TextValue

```
</details>