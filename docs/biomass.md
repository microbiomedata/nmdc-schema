# Slot: biomass (biomass)


_Amount of biomass; should include the name for the part of biomass measured, e.g. Microbial, total. Can include multiple measurements_



URI: [MIXS:0000174](https://w3id.org/mixs/0000174)




## Inheritance

* [core_field](core_field.md)
    * **biomass**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* biomass




## Examples

| Value |
| --- |
| total;20 gram |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | biomass type;measurement value || preferred_unit | ton, kilogram, gram || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: biomass
annotations:
  expected_value:
    tag: expected_value
    value: biomass type;measurement value
  preferred_unit:
    tag: preferred_unit
    value: ton, kilogram, gram
  occurrence:
    tag: occurrence
    value: m
description: Amount of biomass; should include the name for the part of biomass measured,
  e.g. Microbial, total. Can include multiple measurements
title: biomass
examples:
- value: total;20 gram
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- biomass
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000174
multivalued: true
alias: biomass
domain_of:
- Biosample
range: TextValue

```
</details>