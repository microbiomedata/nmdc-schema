# Slot: room moisture damage or mold history (room_moist_dam_hist)


_The history of moisture damage or mold in the past 12 months. Number of events of moisture damage or mold observed_



URI: [MIXS:0000235](https://w3id.org/mixs/0000235)




## Inheritance

* [core_field](core_field.md)
    * **room_moist_dam_hist**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [Integer](Integer.md)



## Aliases


* room moisture damage or mold history




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
name: room_moist_dam_hist
annotations:
  expected_value:
    tag: expected_value
    value: value
  occurrence:
    tag: occurrence
    value: '1'
description: The history of moisture damage or mold in the past 12 months. Number
  of events of moisture damage or mold observed
title: room moisture damage or mold history
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- room moisture damage or mold history
rank: 1000
is_a: core field
slot_uri: MIXS:0000235
multivalued: false
alias: room_moist_dam_hist
domain_of:
- Biosample
range: integer

```
</details>