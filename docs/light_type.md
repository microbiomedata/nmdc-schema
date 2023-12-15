# Slot: light type (light_type)


_Application of light to achieve some practical or aesthetic effect. Lighting includes the use of both artificial light sources such as lamps and light fixtures, as well as natural illumination by capturing daylight. Can also include absence of light_



URI: [MIXS:0000769](https://w3id.org/mixs/0000769)




## Inheritance

* [core_field](core_field.md)
    * **light_type**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [LightTypeEnum](LightTypeEnum.md)

* Multivalued: True



## Aliases


* light type




## Examples

| Value |
| --- |
| desk lamp |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | enumeration || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: light_type
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: m
description: Application of light to achieve some practical or aesthetic effect. Lighting
  includes the use of both artificial light sources such as lamps and light fixtures,
  as well as natural illumination by capturing daylight. Can also include absence
  of light
title: light type
examples:
- value: desk lamp
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- light type
rank: 1000
is_a: core field
slot_uri: MIXS:0000769
multivalued: true
alias: light_type
domain_of:
- Biosample
range: light_type_enum

```
</details>