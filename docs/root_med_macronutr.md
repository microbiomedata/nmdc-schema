# Slot: rooting medium macronutrients (root_med_macronutr)


_Measurement of the culture rooting medium macronutrients (N,P, K, Ca, Mg, S); e.g. KH2PO4 (170¬†mg/L)._



URI: [MIXS:0000578](https://w3id.org/mixs/0000578)




## Inheritance

* [core_field](core_field.md)
    * **root_med_macronutr**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* rooting medium macronutrients




## Examples

| Value |
| --- |
| KH2PO4;170¬†milligram per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | macronutrient name;measurement value || preferred_unit | milligram per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: root_med_macronutr
annotations:
  expected_value:
    tag: expected_value
    value: macronutrient name;measurement value
  preferred_unit:
    tag: preferred_unit
    value: milligram per liter
  occurrence:
    tag: occurrence
    value: '1'
description: Measurement of the culture rooting medium macronutrients (N,P, K, Ca,
  Mg, S); e.g. KH2PO4 (170¬†mg/L).
title: rooting medium macronutrients
examples:
- value: KH2PO4;170¬†milligram per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- rooting medium macronutrients
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000578
multivalued: false
alias: root_med_macronutr
domain_of:
- Biosample
range: TextValue

```
</details>