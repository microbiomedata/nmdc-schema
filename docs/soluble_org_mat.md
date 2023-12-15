# Slot: soluble organic material (soluble_org_mat)


_Concentration of substances such as urea, fruit sugars, soluble proteins, drugs, pharmaceuticals, etc._



URI: [MIXS:0000673](https://w3id.org/mixs/0000673)




## Inheritance

* [core_field](core_field.md)
    * **soluble_org_mat**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* soluble organic material




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | soluble organic material name;measurement value || preferred_unit | gram, microgram, mole per liter, gram per liter, parts per million || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: soluble_org_mat
annotations:
  expected_value:
    tag: expected_value
    value: soluble organic material name;measurement value
  preferred_unit:
    tag: preferred_unit
    value: gram, microgram, mole per liter, gram per liter, parts per million
  occurrence:
    tag: occurrence
    value: m
description: Concentration of substances such as urea, fruit sugars, soluble proteins,
  drugs, pharmaceuticals, etc.
title: soluble organic material
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- soluble organic material
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000673
multivalued: true
alias: soluble_org_mat
domain_of:
- Biosample
range: TextValue

```
</details>