# Slot: door condition (door_cond)


_The phsical condition of the door_



URI: [MIXS:0000788](https://w3id.org/mixs/0000788)




## Inheritance

* [core_field](core_field.md)
    * **door_cond**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [DoorCondEnum](DoorCondEnum.md)



## Aliases


* door condition




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
name: door_cond
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The phsical condition of the door
title: door condition
examples:
- value: new
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- door condition
rank: 1000
is_a: core field
slot_uri: MIXS:0000788
multivalued: false
alias: door_cond
domain_of:
- Biosample
range: door_cond_enum

```
</details>