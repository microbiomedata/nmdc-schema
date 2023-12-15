# Slot: phospholipid fatty acid (phosplipid_fatt_acid)


_Concentration of phospholipid fatty acids; can include multiple values_



URI: [MIXS:0000181](https://w3id.org/mixs/0000181)




## Inheritance

* [core_field](core_field.md)
    * **phosplipid_fatt_acid**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* phospholipid fatty acid




## Examples

| Value |
| --- |
| 2.98 milligram per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | phospholipid fatty acid name;measurement value || preferred_unit | mole per gram, mole per liter || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: phosplipid_fatt_acid
annotations:
  expected_value:
    tag: expected_value
    value: phospholipid fatty acid name;measurement value
  preferred_unit:
    tag: preferred_unit
    value: mole per gram, mole per liter
  occurrence:
    tag: occurrence
    value: m
description: Concentration of phospholipid fatty acids; can include multiple values
title: phospholipid fatty acid
examples:
- value: 2.98 milligram per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- phospholipid fatty acid
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000181
multivalued: true
alias: phosplipid_fatt_acid
domain_of:
- Biosample
range: TextValue

```
</details>