# Slot: window location (window_loc)


_The relative location of the window within the room_



URI: [MIXS:0000852](https://w3id.org/mixs/0000852)




## Inheritance

* [core_field](core_field.md)
    * **window_loc**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [WindowLocEnum](WindowLocEnum.md)



## Aliases


* window location




## Examples

| Value |
| --- |
| west |

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
name: window_loc
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The relative location of the window within the room
title: window location
examples:
- value: west
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- window location
rank: 1000
is_a: core field
slot_uri: MIXS:0000852
multivalued: false
alias: window_loc
domain_of:
- Biosample
range: window_loc_enum

```
</details>