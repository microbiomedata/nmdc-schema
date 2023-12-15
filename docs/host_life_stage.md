# Slot: host life stage (host_life_stage)


_Description of life stage of host_



URI: [MIXS:0000251](https://w3id.org/mixs/0000251)




## Inheritance

* [core_field](core_field.md)
    * **host_life_stage**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* host life stage




## Examples

| Value |
| --- |
| adult |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | stage || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: host_life_stage
annotations:
  expected_value:
    tag: expected_value
    value: stage
  occurrence:
    tag: occurrence
    value: '1'
description: Description of life stage of host
title: host life stage
examples:
- value: adult
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- host life stage
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000251
multivalued: false
alias: host_life_stage
domain_of:
- Biosample
range: TextValue

```
</details>