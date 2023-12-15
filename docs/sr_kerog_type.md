# Slot: source rock kerogen type (sr_kerog_type)


_Origin of kerogen. Type I: Algal (aquatic), Type II: planktonic and soft plant material (aquatic or terrestrial), Type III: terrestrial woody/ fibrous plant material (terrestrial), Type IV: oxidized recycled woody debris (terrestrial) (additional information: https://en.wikipedia.org/wiki/Kerogen). If "other" is specified, please propose entry in "additional info" field_



URI: [MIXS:0000994](https://w3id.org/mixs/0000994)




## Inheritance

* [core_field](core_field.md)
    * **sr_kerog_type**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [SrKerogTypeEnum](SrKerogTypeEnum.md)



## Aliases


* source rock kerogen type




## Examples

| Value |
| --- |
| Type IV |

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
name: sr_kerog_type
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: 'Origin of kerogen. Type I: Algal (aquatic), Type II: planktonic and
  soft plant material (aquatic or terrestrial), Type III: terrestrial woody/ fibrous
  plant material (terrestrial), Type IV: oxidized recycled woody debris (terrestrial)
  (additional information: https://en.wikipedia.org/wiki/Kerogen). If "other" is specified,
  please propose entry in "additional info" field'
title: source rock kerogen type
examples:
- value: Type IV
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- source rock kerogen type
rank: 1000
is_a: core field
slot_uri: MIXS:0000994
multivalued: false
alias: sr_kerog_type
domain_of:
- Biosample
range: sr_kerog_type_enum

```
</details>