# Slot: rooting medium organic supplements (root_med_suppl)


_Organic supplements of the culture rooting medium, such as vitamins, amino acids, organic acids, antibiotics activated charcoal; e.g. nicotinic acid (0.5¬†mg/L)._



URI: [MIXS:0000580](https://w3id.org/mixs/0000580)




## Inheritance

* [core_field](core_field.md)
    * **root_med_suppl**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* rooting medium organic supplements




## Examples

| Value |
| --- |
| nicotinic acid;0.5 milligram per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | supplement name;measurement value || preferred_unit | milligram per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: root_med_suppl
annotations:
  expected_value:
    tag: expected_value
    value: supplement name;measurement value
  preferred_unit:
    tag: preferred_unit
    value: milligram per liter
  occurrence:
    tag: occurrence
    value: '1'
description: Organic supplements of the culture rooting medium, such as vitamins,
  amino acids, organic acids, antibiotics activated charcoal; e.g. nicotinic acid
  (0.5¬†mg/L).
title: rooting medium organic supplements
examples:
- value: nicotinic acid;0.5 milligram per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- rooting medium organic supplements
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000580
multivalued: false
alias: root_med_suppl
domain_of:
- Biosample
range: TextValue

```
</details>