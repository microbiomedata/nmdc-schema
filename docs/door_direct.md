# Slot: door direction of opening (door_direct)


_The direction the door opens_



URI: [MIXS:0000789](https://w3id.org/mixs/0000789)




## Inheritance

* [core_field](core_field.md)
    * **door_direct**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [DoorDirectEnum](DoorDirectEnum.md)



## Aliases


* door direction of opening




## Examples

| Value |
| --- |
| inward |

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
name: door_direct
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The direction the door opens
title: door direction of opening
examples:
- value: inward
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- door direction of opening
rank: 1000
is_a: core field
slot_uri: MIXS:0000789
multivalued: false
alias: door_direct
domain_of:
- Biosample
range: door_direct_enum

```
</details>