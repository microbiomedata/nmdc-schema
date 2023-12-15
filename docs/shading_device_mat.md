# Slot: shading device material (shading_device_mat)


_The material the shading device is composed of_



URI: [MIXS:0000245](https://w3id.org/mixs/0000245)




## Inheritance

* [core_field](core_field.md)
    * **shading_device_mat**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* shading device material




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | material name || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: shading_device_mat
annotations:
  expected_value:
    tag: expected_value
    value: material name
  occurrence:
    tag: occurrence
    value: '1'
description: The material the shading device is composed of
title: shading device material
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- shading device material
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000245
multivalued: false
alias: shading_device_mat
domain_of:
- Biosample
range: TextValue

```
</details>