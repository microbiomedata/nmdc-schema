# Slot: heating delivery locations (heat_deliv_loc)


_The location of heat delivery within the room_



URI: [MIXS:0000810](https://w3id.org/mixs/0000810)




## Inheritance

* [core_field](core_field.md)
    * **heat_deliv_loc**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [HeatDelivLocEnum](HeatDelivLocEnum.md)



## Aliases


* heating delivery locations




## Examples

| Value |
| --- |
| north |

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
name: heat_deliv_loc
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The location of heat delivery within the room
title: heating delivery locations
examples:
- value: north
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- heating delivery locations
rank: 1000
is_a: core field
slot_uri: MIXS:0000810
multivalued: false
alias: heat_deliv_loc
domain_of:
- Biosample
range: heat_deliv_loc_enum

```
</details>