# Slot: sample storage location (samp_store_loc)


_Location at which sample was stored, usually name of a specific freezer/room_



URI: [MIXS:0000755](https://w3id.org/mixs/0000755)




## Inheritance

* [core_field](core_field.md)
    * **samp_store_loc**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* sample storage location




## Examples

| Value |
| --- |
| Freezer no:5 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | location name || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: samp_store_loc
annotations:
  expected_value:
    tag: expected_value
    value: location name
  occurrence:
    tag: occurrence
    value: '1'
description: Location at which sample was stored, usually name of a specific freezer/room
title: sample storage location
examples:
- value: Freezer no:5
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- sample storage location
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000755
multivalued: false
alias: samp_store_loc
domain_of:
- Biosample
range: TextValue

```
</details>