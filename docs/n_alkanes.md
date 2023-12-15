# Slot: n-alkanes (n_alkanes)


_Concentration of n-alkanes; can include multiple n-alkanes_



URI: [MIXS:0000503](https://w3id.org/mixs/0000503)




## Inheritance

* [core_field](core_field.md)
    * **n_alkanes**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* n-alkanes




## Examples

| Value |
| --- |
| n-hexadecane;100 milligram per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | n-alkane name;measurement value || preferred_unit | micromole per liter || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: n_alkanes
annotations:
  expected_value:
    tag: expected_value
    value: n-alkane name;measurement value
  preferred_unit:
    tag: preferred_unit
    value: micromole per liter
  occurrence:
    tag: occurrence
    value: m
description: Concentration of n-alkanes; can include multiple n-alkanes
title: n-alkanes
examples:
- value: n-hexadecane;100 milligram per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- n-alkanes
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000503
multivalued: true
alias: n_alkanes
domain_of:
- Biosample
range: TextValue

```
</details>