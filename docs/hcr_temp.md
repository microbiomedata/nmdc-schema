# Slot: hydrocarbon resource original temperature (hcr_temp)


_Original temperature of the hydrocarbon resource_



URI: [MIXS:0000393](https://w3id.org/mixs/0000393)




## Inheritance

* [core_field](core_field.md)
    * **hcr_temp**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* hydrocarbon resource original temperature




## Examples

| Value |
| --- |
| 150-295 degree Celsius |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value range || preferred_unit | degree Celsius || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: hcr_temp
annotations:
  expected_value:
    tag: expected_value
    value: measurement value range
  preferred_unit:
    tag: preferred_unit
    value: degree Celsius
  occurrence:
    tag: occurrence
    value: '1'
description: Original temperature of the hydrocarbon resource
title: hydrocarbon resource original temperature
examples:
- value: 150-295 degree Celsius
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- hydrocarbon resource original temperature
rank: 1000
is_a: core field
string_serialization: '{float} - {float} {unit}'
slot_uri: MIXS:0000393
multivalued: false
alias: hcr_temp
domain_of:
- Biosample
range: TextValue

```
</details>