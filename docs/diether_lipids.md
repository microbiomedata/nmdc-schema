# Slot: diether lipids (diether_lipids)


_Concentration of diether lipids; can include multiple types of diether lipids_



URI: [MIXS:0000178](https://w3id.org/mixs/0000178)




## Inheritance

* [core_field](core_field.md)
    * **diether_lipids**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* diether lipids




## Examples

| Value |
| --- |
| 0.2 nanogram per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | diether lipid name;measurement value || preferred_unit | nanogram per liter || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: diether_lipids
annotations:
  expected_value:
    tag: expected_value
    value: diether lipid name;measurement value
  preferred_unit:
    tag: preferred_unit
    value: nanogram per liter
  occurrence:
    tag: occurrence
    value: m
description: Concentration of diether lipids; can include multiple types of diether
  lipids
title: diether lipids
examples:
- value: 0.2 nanogram per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- diether lipids
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000178
multivalued: true
alias: diether_lipids
domain_of:
- Biosample
range: TextValue

```
</details>