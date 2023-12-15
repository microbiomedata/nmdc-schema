# Slot: storage conditions (store_cond)


_Explain how and for how long the soil sample was stored before DNA extraction (fresh/frozen/other)._



URI: [MIXS:0000327](https://w3id.org/mixs/0000327)




## Inheritance

* [core_field](core_field.md)
    * **store_cond**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* storage conditions




## Examples

| Value |
| --- |
| -20 degree Celsius freezer;P2Y10D |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | storage condition type;duration || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: store_cond
annotations:
  expected_value:
    tag: expected_value
    value: storage condition type;duration
  occurrence:
    tag: occurrence
    value: '1'
description: Explain how and for how long the soil sample was stored before DNA extraction
  (fresh/frozen/other).
title: storage conditions
examples:
- value: -20 degree Celsius freezer;P2Y10D
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- storage conditions
rank: 1000
is_a: core field
string_serialization: '{text};{duration}'
slot_uri: MIXS:0000327
multivalued: false
alias: store_cond
domain_of:
- Biosample
range: TextValue

```
</details>