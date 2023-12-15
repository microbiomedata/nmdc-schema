# Slot: average daily occupancy (avg_occup)


_Daily average occupancy of room. Indicate the number of person(s) daily occupying the sampling room._



URI: [MIXS:0000775](https://w3id.org/mixs/0000775)




## Inheritance

* [core_field](core_field.md)
    * **avg_occup**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* average daily occupancy




## Examples

| Value |
| --- |
| 2 |

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
name: avg_occup
annotations:
  expected_value:
    tag: expected_value
    value: value
  occurrence:
    tag: occurrence
    value: '1'
description: Daily average occupancy of room. Indicate the number of person(s) daily
  occupying the sampling room.
title: average daily occupancy
examples:
- value: '2'
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- average daily occupancy
rank: 1000
is_a: core field
slot_uri: MIXS:0000775
multivalued: false
alias: avg_occup
domain_of:
- Biosample
range: TextValue

```
</details>