# Slot: furniture (furniture)


_The types of furniture present in the sampled room_



URI: [MIXS:0000807](https://w3id.org/mixs/0000807)




## Inheritance

* [core_field](core_field.md)
    * **furniture**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [FurnitureEnum](FurnitureEnum.md)



## Aliases


* furniture




## Examples

| Value |
| --- |
| chair |

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
name: furniture
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The types of furniture present in the sampled room
title: furniture
examples:
- value: chair
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- furniture
rank: 1000
is_a: core field
slot_uri: MIXS:0000807
multivalued: false
alias: furniture
domain_of:
- Biosample
range: furniture_enum

```
</details>