# Slot: room count (room_count)


_The total count of rooms in the built structure including all room types_



URI: [MIXS:0000234](https://w3id.org/mixs/0000234)




## Inheritance

* [core_field](core_field.md)
    * **room_count**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* room count




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
name: room_count
annotations:
  expected_value:
    tag: expected_value
    value: value
  occurrence:
    tag: occurrence
    value: '1'
description: The total count of rooms in the built structure including all room types
title: room count
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- room count
rank: 1000
is_a: core field
slot_uri: MIXS:0000234
multivalued: false
alias: room_count
domain_of:
- Biosample
range: TextValue

```
</details>