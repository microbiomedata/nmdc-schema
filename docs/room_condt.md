# Slot: room condition (room_condt)


_The condition of the room at the time of sampling_



URI: [MIXS:0000822](https://w3id.org/mixs/0000822)




## Inheritance

* [core_field](core_field.md)
    * **room_condt**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [RoomCondtEnum](RoomCondtEnum.md)



## Aliases


* room condition




## Examples

| Value |
| --- |
| new |

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
name: room_condt
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The condition of the room at the time of sampling
title: room condition
examples:
- value: new
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- room condition
rank: 1000
is_a: core field
slot_uri: MIXS:0000822
multivalued: false
alias: room_condt
domain_of:
- Biosample
range: room_condt_enum

```
</details>