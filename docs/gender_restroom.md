# Slot: gender of restroom (gender_restroom)


_The gender type of the restroom_



URI: [MIXS:0000808](https://w3id.org/mixs/0000808)




## Inheritance

* [core_field](core_field.md)
    * **gender_restroom**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [GenderRestroomEnum](GenderRestroomEnum.md)



## Aliases


* gender of restroom




## Examples

| Value |
| --- |
| male |

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
name: gender_restroom
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The gender type of the restroom
title: gender of restroom
examples:
- value: male
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- gender of restroom
rank: 1000
is_a: core field
slot_uri: MIXS:0000808
multivalued: false
alias: gender_restroom
domain_of:
- Biosample
range: gender_restroom_enum

```
</details>