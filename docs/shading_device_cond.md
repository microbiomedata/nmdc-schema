# Slot: shading device condition (shading_device_cond)


_The physical condition of the shading device at the time of sampling_



URI: [MIXS:0000831](https://w3id.org/mixs/0000831)




## Inheritance

* [core_field](core_field.md)
    * **shading_device_cond**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [ShadingDeviceCondEnum](ShadingDeviceCondEnum.md)



## Aliases


* shading device condition




## Examples

| Value |
| --- |
| new |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | enumeration || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: shading_device_cond
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The physical condition of the shading device at the time of sampling
title: shading device condition
examples:
- value: new
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- shading device condition
rank: 1000
is_a: core field
slot_uri: MIXS:0000831
multivalued: false
alias: shading_device_cond
domain_of:
- Biosample
range: shading_device_cond_enum

```
</details>