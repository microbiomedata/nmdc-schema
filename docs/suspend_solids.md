# Slot: suspended solids (suspend_solids)


_Concentration of substances including a wide variety of material, such as silt, decaying plant and animal matter; can include multiple substances_



URI: [MIXS:0000150](https://w3id.org/mixs/0000150)




## Inheritance

* [core_field](core_field.md)
    * **suspend_solids**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* suspended solids




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | suspended solid name;measurement value || preferred_unit | gram, microgram, milligram per liter, mole per liter, gram per liter, part per million || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: suspend_solids
annotations:
  expected_value:
    tag: expected_value
    value: suspended solid name;measurement value
  preferred_unit:
    tag: preferred_unit
    value: gram, microgram, milligram per liter, mole per liter, gram per liter, part
      per million
  occurrence:
    tag: occurrence
    value: m
description: Concentration of substances including a wide variety of material, such
  as silt, decaying plant and animal matter; can include multiple substances
title: suspended solids
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- suspended solids
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000150
multivalued: true
alias: suspend_solids
domain_of:
- Biosample
range: TextValue

```
</details>