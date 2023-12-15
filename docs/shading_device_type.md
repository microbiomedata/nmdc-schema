# Slot: shading device type (shading_device_type)


_The type of shading device_



URI: [MIXS:0000835](https://w3id.org/mixs/0000835)




## Inheritance

* [core_field](core_field.md)
    * **shading_device_type**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [ShadingDeviceTypeEnum](ShadingDeviceTypeEnum.md)



## Aliases


* shading device type




## Examples

| Value |
| --- |
| slatted aluminum awning |

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
name: shading_device_type
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The type of shading device
title: shading device type
examples:
- value: slatted aluminum awning
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- shading device type
rank: 1000
is_a: core field
slot_uri: MIXS:0000835
multivalued: false
alias: shading_device_type
domain_of:
- Biosample
range: shading_device_type_enum

```
</details>