# Slot: emulsions (emulsions)


_Amount or concentration of substances such as paints, adhesives, mayonnaise, hair colorants, emulsified oils, etc.; can include multiple emulsion types_



URI: [MIXS:0000660](https://w3id.org/mixs/0000660)




## Inheritance

* [core_field](core_field.md)
    * **emulsions**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* emulsions




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | emulsion name;measurement value || preferred_unit | gram per liter || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: emulsions
annotations:
  expected_value:
    tag: expected_value
    value: emulsion name;measurement value
  preferred_unit:
    tag: preferred_unit
    value: gram per liter
  occurrence:
    tag: occurrence
    value: m
description: Amount or concentration of substances such as paints, adhesives, mayonnaise,
  hair colorants, emulsified oils, etc.; can include multiple emulsion types
title: emulsions
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- emulsions
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000660
multivalued: true
alias: emulsions
domain_of:
- Biosample
range: TextValue

```
</details>