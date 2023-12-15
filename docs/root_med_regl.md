# Slot: rooting medium regulators (root_med_regl)


_Growth regulators in the culture rooting medium such as cytokinins, auxins, gybberellins, abscisic acid; e.g. 0.5¬†mg/L NAA._



URI: [MIXS:0000581](https://w3id.org/mixs/0000581)




## Inheritance

* [core_field](core_field.md)
    * **root_med_regl**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* rooting medium regulators




## Examples

| Value |
| --- |
| abscisic acid;0.75 milligram per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | regulator name;measurement value || preferred_unit | milligram per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: root_med_regl
annotations:
  expected_value:
    tag: expected_value
    value: regulator name;measurement value
  preferred_unit:
    tag: preferred_unit
    value: milligram per liter
  occurrence:
    tag: occurrence
    value: '1'
description: Growth regulators in the culture rooting medium such as cytokinins, auxins,
  gybberellins, abscisic acid; e.g. 0.5¬†mg/L NAA.
title: rooting medium regulators
examples:
- value: abscisic acid;0.75 milligram per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- rooting medium regulators
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000581
multivalued: false
alias: root_med_regl
domain_of:
- Biosample
range: TextValue

```
</details>