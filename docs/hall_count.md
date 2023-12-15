# Slot: hallway/corridor count (hall_count)


_The total count of hallways and cooridors in the built structure_



URI: [MIXS:0000228](https://w3id.org/mixs/0000228)




## Inheritance

* [core_field](core_field.md)
    * **hall_count**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* hallway/corridor count




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
name: hall_count
annotations:
  expected_value:
    tag: expected_value
    value: value
  occurrence:
    tag: occurrence
    value: '1'
description: The total count of hallways and cooridors in the built structure
title: hallway/corridor count
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- hallway/corridor count
rank: 1000
is_a: core field
slot_uri: MIXS:0000228
multivalued: false
alias: hall_count
domain_of:
- Biosample
range: TextValue

```
</details>