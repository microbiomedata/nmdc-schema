# Slot: ceiling texture (ceil_texture)


_The feel, appearance, or consistency of a ceiling surface_



URI: [MIXS:0000783](https://w3id.org/mixs/0000783)




## Inheritance

* [core_field](core_field.md)
    * **ceil_texture**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [CeilTextureEnum](CeilTextureEnum.md)



## Aliases


* ceiling texture




## Examples

| Value |
| --- |
| popcorn |

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
name: ceil_texture
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The feel, appearance, or consistency of a ceiling surface
title: ceiling texture
examples:
- value: popcorn
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- ceiling texture
rank: 1000
is_a: core field
slot_uri: MIXS:0000783
multivalued: false
alias: ceil_texture
domain_of:
- Biosample
range: ceil_texture_enum

```
</details>