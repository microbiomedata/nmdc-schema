# Slot: room window count (room_window_count)


_Number of windows in the room_



URI: [MIXS:0000237](https://w3id.org/mixs/0000237)




## Inheritance

* [core_field](core_field.md)
    * **room_window_count**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [Integer](Integer.md)



## Aliases


* room window count




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | value || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: room_window_count
annotations:
  expected_value:
    tag: expected_value
    value: value
  occurrence:
    tag: occurrence
    value: '1'
description: Number of windows in the room
title: room window count
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- room window count
rank: 1000
is_a: core field
slot_uri: MIXS:0000237
multivalued: false
alias: room_window_count
domain_of:
- Biosample
range: integer

```
</details>