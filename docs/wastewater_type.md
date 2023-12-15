# Slot: wastewater type (wastewater_type)


_The origin of wastewater such as human waste, rainfall, storm drains, etc._



URI: [MIXS:0000353](https://w3id.org/mixs/0000353)




## Inheritance

* [core_field](core_field.md)
    * **wastewater_type**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* wastewater type




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | wastewater type name || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: wastewater_type
annotations:
  expected_value:
    tag: expected_value
    value: wastewater type name
  occurrence:
    tag: occurrence
    value: '1'
description: The origin of wastewater such as human waste, rainfall, storm drains,
  etc.
title: wastewater type
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- wastewater type
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000353
multivalued: false
alias: wastewater_type
domain_of:
- Biosample
range: TextValue

```
</details>