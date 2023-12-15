# Slot: rooting medium micronutrients (root_med_micronutr)


_Measurement of the culture rooting medium micronutrients (Fe, Mn, Zn, B, Cu, Mo); e.g. H3BO3 (6.2¬†mg/L)._



URI: [MIXS:0000579](https://w3id.org/mixs/0000579)




## Inheritance

* [core_field](core_field.md)
    * **root_med_micronutr**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* rooting medium micronutrients




## Examples

| Value |
| --- |
| H3BO3;6.2¬†milligram per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | micronutrient name;measurement value || preferred_unit | milligram per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: root_med_micronutr
annotations:
  expected_value:
    tag: expected_value
    value: micronutrient name;measurement value
  preferred_unit:
    tag: preferred_unit
    value: milligram per liter
  occurrence:
    tag: occurrence
    value: '1'
description: Measurement of the culture rooting medium micronutrients (Fe, Mn, Zn,
  B, Cu, Mo); e.g. H3BO3 (6.2¬†mg/L).
title: rooting medium micronutrients
examples:
- value: H3BO3;6.2¬†milligram per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- rooting medium micronutrients
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000579
multivalued: false
alias: root_med_micronutr
domain_of:
- Biosample
range: TextValue

```
</details>