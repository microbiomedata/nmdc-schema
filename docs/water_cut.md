# Slot: water cut (water_cut)


_Current amount of water (%) in a produced fluid stream; or the average of the combined streams_



URI: [MIXS:0000454](https://w3id.org/mixs/0000454)




## Inheritance

* [core_field](core_field.md)
    * **water_cut**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* water cut




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | percent || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: water_cut
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: percent
  occurrence:
    tag: occurrence
    value: '1'
description: Current amount of water (%) in a produced fluid stream; or the average
  of the combined streams
title: water cut
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- water cut
rank: 1000
is_a: core field
slot_uri: MIXS:0000454
multivalued: false
alias: water_cut
domain_of:
- Biosample
range: QuantityValue

```
</details>