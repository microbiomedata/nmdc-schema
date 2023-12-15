# Slot: host shape (host_shape)


_Morphological shape of host_



URI: [MIXS:0000261](https://w3id.org/mixs/0000261)




## Inheritance

* [core_field](core_field.md)
    * **host_shape**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* host shape




## Examples

| Value |
| --- |
| round |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | shape || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: host_shape
annotations:
  expected_value:
    tag: expected_value
    value: shape
  occurrence:
    tag: occurrence
    value: '1'
description: Morphological shape of host
title: host shape
examples:
- value: round
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- host shape
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000261
multivalued: false
alias: host_shape
domain_of:
- Biosample
range: TextValue

```
</details>