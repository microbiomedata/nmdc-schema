# Slot: host last meal (host_last_meal)


_Content of last meal and time since feeding; can include multiple values_



URI: [MIXS:0000870](https://w3id.org/mixs/0000870)




## Inheritance

* [core_field](core_field.md)
    * **host_last_meal**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* host last meal




## Examples

| Value |
| --- |
| corn feed;P2H |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | content;duration || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: host_last_meal
annotations:
  expected_value:
    tag: expected_value
    value: content;duration
  occurrence:
    tag: occurrence
    value: m
description: Content of last meal and time since feeding; can include multiple values
title: host last meal
examples:
- value: corn feed;P2H
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- host last meal
rank: 1000
is_a: core field
string_serialization: '{text};{duration}'
slot_uri: MIXS:0000870
multivalued: true
alias: host_last_meal
domain_of:
- Biosample
range: TextValue

```
</details>