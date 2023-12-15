# Slot: visual media (vis_media)


_The building visual media_



URI: [MIXS:0000840](https://w3id.org/mixs/0000840)




## Inheritance

* [core_field](core_field.md)
    * **vis_media**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [VisMediaEnum](VisMediaEnum.md)



## Aliases


* visual media




## Examples

| Value |
| --- |
| 3D scans |

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
name: vis_media
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The building visual media
title: visual media
examples:
- value: 3D scans
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- visual media
rank: 1000
is_a: core field
slot_uri: MIXS:0000840
multivalued: false
alias: vis_media
domain_of:
- Biosample
range: vis_media_enum

```
</details>