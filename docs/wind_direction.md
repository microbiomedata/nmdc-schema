# Slot: wind direction (wind_direction)


_Wind direction is the direction from which a wind originates_



URI: [MIXS:0000757](https://w3id.org/mixs/0000757)




## Inheritance

* [core_field](core_field.md)
    * **wind_direction**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* wind direction




## Examples

| Value |
| --- |
| Northwest |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | wind direction name || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: wind_direction
annotations:
  expected_value:
    tag: expected_value
    value: wind direction name
  occurrence:
    tag: occurrence
    value: '1'
description: Wind direction is the direction from which a wind originates
title: wind direction
examples:
- value: Northwest
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- wind direction
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000757
multivalued: false
alias: wind_direction
domain_of:
- Biosample
range: TextValue

```
</details>