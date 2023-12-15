# Slot: sampling room ID or name (samp_room_id)


_Sampling room number. This ID should be consistent with the designations on the building floor plans_



URI: [MIXS:0000244](https://w3id.org/mixs/0000244)




## Inheritance

* [core_field](core_field.md)
    * **samp_room_id**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* sampling room ID or name




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
name: samp_room_id
annotations:
  expected_value:
    tag: expected_value
    value: value
  occurrence:
    tag: occurrence
    value: '1'
description: Sampling room number. This ID should be consistent with the designations
  on the building floor plans
title: sampling room ID or name
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- sampling room ID or name
rank: 1000
is_a: core field
slot_uri: MIXS:0000244
multivalued: false
alias: samp_room_id
domain_of:
- Biosample
range: TextValue

```
</details>