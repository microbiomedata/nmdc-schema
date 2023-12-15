# Slot: rooting medium pH (root_med_ph)


_pH measurement of the culture rooting medium; e.g. 5.5._



URI: [MIXS:0001062](https://w3id.org/mixs/0001062)




## Inheritance

* [core_field](core_field.md)
    * **root_med_ph**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* rooting medium pH




## Examples

| Value |
| --- |
| 7.5 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: root_med_ph
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  occurrence:
    tag: occurrence
    value: '1'
description: pH measurement of the culture rooting medium; e.g. 5.5.
title: rooting medium pH
examples:
- value: '7.5'
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- rooting medium pH
rank: 1000
is_a: core field
slot_uri: MIXS:0001062
multivalued: false
alias: root_med_ph
domain_of:
- Biosample
range: QuantityValue

```
</details>