# Slot: shading device location (shading_device_loc)


_The location of the shading device in relation to the built structure_



URI: [MIXS:0000832](https://w3id.org/mixs/0000832)




## Inheritance

* [core_field](core_field.md)
    * **shading_device_loc**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* shading device location




## Examples

| Value |
| --- |
| exterior |

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
name: shading_device_loc
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The location of the shading device in relation to the built structure
title: shading device location
examples:
- value: exterior
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- shading device location
rank: 1000
is_a: core field
string_serialization: '[exterior|interior]'
slot_uri: MIXS:0000832
multivalued: false
alias: shading_device_loc
domain_of:
- Biosample
range: TextValue

```
</details>