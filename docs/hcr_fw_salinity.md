# Slot: formation water salinity (hcr_fw_salinity)


_Original formation water salinity (prior to secondary recovery e.g. Waterflooding) expressed as TDS_



URI: [MIXS:0000406](https://w3id.org/mixs/0000406)




## Inheritance

* [core_field](core_field.md)
    * **hcr_fw_salinity**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* formation water salinity




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | milligram per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: hcr_fw_salinity
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: milligram per liter
  occurrence:
    tag: occurrence
    value: '1'
description: Original formation water salinity (prior to secondary recovery e.g. Waterflooding)
  expressed as TDS
title: formation water salinity
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- formation water salinity
rank: 1000
is_a: core field
slot_uri: MIXS:0000406
multivalued: false
alias: hcr_fw_salinity
domain_of:
- Biosample
range: QuantityValue

```
</details>