# Slot: hydrocarbon resource original pressure (hcr_pressure)


_Original pressure of the hydrocarbon resource_



URI: [MIXS:0000395](https://w3id.org/mixs/0000395)




## Inheritance

* [core_field](core_field.md)
    * **hcr_pressure**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* hydrocarbon resource original pressure




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value range || preferred_unit | atmosphere, kilopascal || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: hcr_pressure
annotations:
  expected_value:
    tag: expected_value
    value: measurement value range
  preferred_unit:
    tag: preferred_unit
    value: atmosphere, kilopascal
  occurrence:
    tag: occurrence
    value: '1'
description: Original pressure of the hydrocarbon resource
title: hydrocarbon resource original pressure
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- hydrocarbon resource original pressure
rank: 1000
is_a: core field
string_serialization: '{float} - {float} {unit}'
slot_uri: MIXS:0000395
multivalued: false
alias: hcr_pressure
domain_of:
- Biosample
range: TextValue

```
</details>