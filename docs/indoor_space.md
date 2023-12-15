# Slot: indoor space (indoor_space)


_A distinguishable space within a structure, the purpose for which discrete areas of a building is used_



URI: [MIXS:0000763](https://w3id.org/mixs/0000763)




## Inheritance

* [core_field](core_field.md)
    * **indoor_space**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [IndoorSpaceEnum](IndoorSpaceEnum.md)



## Aliases


* indoor space




## Examples

| Value |
| --- |
| foyer |

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
name: indoor_space
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: A distinguishable space within a structure, the purpose for which discrete
  areas of a building is used
title: indoor space
examples:
- value: foyer
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- indoor space
rank: 1000
is_a: core field
slot_uri: MIXS:0000763
multivalued: false
alias: indoor_space
domain_of:
- Biosample
range: indoor_space_enum

```
</details>