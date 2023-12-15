# Slot: soluble inorganic material (soluble_inorg_mat)


_Concentration of substances such as ammonia, road-salt, sea-salt, cyanide, hydrogen sulfide, thiocyanates, thiosulfates, etc._



URI: [MIXS:0000672](https://w3id.org/mixs/0000672)




## Inheritance

* [core_field](core_field.md)
    * **soluble_inorg_mat**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* soluble inorganic material




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | soluble inorganic material name;measurement value || preferred_unit | gram, microgram, mole per liter, gram per liter, parts per million || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: soluble_inorg_mat
annotations:
  expected_value:
    tag: expected_value
    value: soluble inorganic material name;measurement value
  preferred_unit:
    tag: preferred_unit
    value: gram, microgram, mole per liter, gram per liter, parts per million
  occurrence:
    tag: occurrence
    value: m
description: Concentration of substances such as ammonia, road-salt, sea-salt, cyanide,
  hydrogen sulfide, thiocyanates, thiosulfates, etc.
title: soluble inorganic material
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- soluble inorganic material
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000672
multivalued: true
alias: soluble_inorg_mat
domain_of:
- Biosample
range: TextValue

```
</details>