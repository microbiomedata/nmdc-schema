# Slot: wall texture (wall_texture)


_The feel, appearance, or consistency of a wall surface_



URI: [MIXS:0000846](https://w3id.org/mixs/0000846)




## Inheritance

* [core_field](core_field.md)
    * **wall_texture**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [WallTextureEnum](WallTextureEnum.md)



## Aliases


* wall texture




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
name: wall_texture
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The feel, appearance, or consistency of a wall surface
title: wall texture
examples:
- value: popcorn
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- wall texture
rank: 1000
is_a: core field
slot_uri: MIXS:0000846
multivalued: false
alias: wall_texture
domain_of:
- Biosample
range: wall_texture_enum

```
</details>