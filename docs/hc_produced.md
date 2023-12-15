# Slot: hydrocarbon type produced (hc_produced)


_Main hydrocarbon type produced from resource (i.e. Oil, gas, condensate, etc). If "other" is specified, please propose entry in "additional info" field_



URI: [MIXS:0000989](https://w3id.org/mixs/0000989)




## Inheritance

* [core_field](core_field.md)
    * **hc_produced**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [HcProducedEnum](HcProducedEnum.md)



## Aliases


* hydrocarbon type produced




## Examples

| Value |
| --- |
| Gas |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | enumeration || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: hc_produced
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: Main hydrocarbon type produced from resource (i.e. Oil, gas, condensate,
  etc). If "other" is specified, please propose entry in "additional info" field
title: hydrocarbon type produced
examples:
- value: Gas
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- hydrocarbon type produced
rank: 1000
is_a: core field
slot_uri: MIXS:0000989
multivalued: false
alias: hc_produced
domain_of:
- Biosample
range: hc_produced_enum

```
</details>