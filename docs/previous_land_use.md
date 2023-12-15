# Slot: history/previous land use (previous_land_use)


_Previous land use and dates_



URI: [MIXS:0000315](https://w3id.org/mixs/0000315)




## Inheritance

* [core_field](core_field.md)
    * **previous_land_use**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* history/previous land use




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | land use name;date || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: previous_land_use
annotations:
  expected_value:
    tag: expected_value
    value: land use name;date
  occurrence:
    tag: occurrence
    value: '1'
description: Previous land use and dates
title: history/previous land use
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- history/previous land use
rank: 1000
is_a: core field
string_serialization: '{text};{timestamp}'
slot_uri: MIXS:0000315
multivalued: false
alias: previous_land_use
domain_of:
- Biosample
range: TextValue

```
</details>