# Slot: shading device signs of water/mold (shad_dev_water_mold)


_Signs of the presence of mold or mildew on the shading device_



URI: [MIXS:0000834](https://w3id.org/mixs/0000834)




## Inheritance

* [core_field](core_field.md)
    * **shad_dev_water_mold**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [String](String.md)



## Aliases


* shading device signs of water/mold




## Examples

| Value |
| --- |
| no presence of mold visible |

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
name: shad_dev_water_mold
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: Signs of the presence of mold or mildew on the shading device
title: shading device signs of water/mold
examples:
- value: no presence of mold visible
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- shading device signs of water/mold
rank: 1000
is_a: core field
string_serialization: '[presence of mold visible|no presence of mold visible]'
slot_uri: MIXS:0000834
multivalued: false
alias: shad_dev_water_mold
domain_of:
- Biosample
range: string

```
</details>