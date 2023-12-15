# Slot: extreme_unusual_properties/heavy metals (heavy_metals)


_Heavy metals present in the sequenced sample and their concentrations. For multiple heavy metals and concentrations, add multiple copies of this field._



URI: [MIXS:0000652](https://w3id.org/mixs/0000652)




## Inheritance

* [core_field](core_field.md)
    * **heavy_metals**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* extreme_unusual_properties/heavy metals




## Examples

| Value |
| --- |
| mercury;0.09 micrograms per gram |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | heavy metal name;measurement value unit || preferred_unit | microgram per gram || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: heavy_metals
annotations:
  expected_value:
    tag: expected_value
    value: heavy metal name;measurement value unit
  preferred_unit:
    tag: preferred_unit
    value: microgram per gram
  occurrence:
    tag: occurrence
    value: m
description: Heavy metals present in the sequenced sample and their concentrations.
  For multiple heavy metals and concentrations, add multiple copies of this field.
title: extreme_unusual_properties/heavy metals
examples:
- value: mercury;0.09 micrograms per gram
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- extreme_unusual_properties/heavy metals
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000652
multivalued: true
alias: heavy_metals
domain_of:
- Biosample
range: TextValue

```
</details>