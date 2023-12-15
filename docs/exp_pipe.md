# Slot: exposed pipes (exp_pipe)


_The number of exposed pipes in the room_



URI: [MIXS:0000220](https://w3id.org/mixs/0000220)




## Inheritance

* [core_field](core_field.md)
    * **exp_pipe**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* exposed pipes




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: exp_pipe
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  occurrence:
    tag: occurrence
    value: '1'
description: The number of exposed pipes in the room
title: exposed pipes
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- exposed pipes
rank: 1000
is_a: core field
slot_uri: MIXS:0000220
multivalued: false
alias: exp_pipe
domain_of:
- Biosample
range: QuantityValue

```
</details>