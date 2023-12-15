# Slot: atmospheric data (atmospheric_data)


_Measurement of atmospheric data; can include multiple data_



URI: [MIXS:0001097](https://w3id.org/mixs/0001097)




## Inheritance

* [core_field](core_field.md)
    * **atmospheric_data**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* atmospheric data




## Examples

| Value |
| --- |
| wind speed;9 knots |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | atmospheric data name;measurement value || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: atmospheric_data
annotations:
  expected_value:
    tag: expected_value
    value: atmospheric data name;measurement value
  occurrence:
    tag: occurrence
    value: m
description: Measurement of atmospheric data; can include multiple data
title: atmospheric data
examples:
- value: wind speed;9 knots
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- atmospheric data
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0001097
multivalued: true
alias: atmospheric_data
domain_of:
- Biosample
range: TextValue

```
</details>