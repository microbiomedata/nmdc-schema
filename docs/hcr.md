# Slot: hydrocarbon resource type (hcr)


_Main Hydrocarbon Resource type. The term "Hydrocarbon Resource" HCR defined as a natural environmental feature containing large amounts of hydrocarbons at high concentrations potentially suitable for commercial exploitation. This term should not be confused with the Hydrocarbon Occurrence term which also includes hydrocarbon-rich environments with currently limited commercial interest such as seeps, outcrops, gas hydrates etc. If "other" is specified, please propose entry in "additional info" field_



URI: [MIXS:0000988](https://w3id.org/mixs/0000988)




## Inheritance

* [core_field](core_field.md)
    * **hcr**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [HcrEnum](HcrEnum.md)



## Aliases


* hydrocarbon resource type




## Examples

| Value |
| --- |
| Oil Sand |

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
name: hcr
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: Main Hydrocarbon Resource type. The term "Hydrocarbon Resource" HCR defined
  as a natural environmental feature containing large amounts of hydrocarbons at high
  concentrations potentially suitable for commercial exploitation. This term should
  not be confused with the Hydrocarbon Occurrence term which also includes hydrocarbon-rich
  environments with currently limited commercial interest such as seeps, outcrops,
  gas hydrates etc. If "other" is specified, please propose entry in "additional info"
  field
title: hydrocarbon resource type
examples:
- value: Oil Sand
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- hydrocarbon resource type
rank: 1000
is_a: core field
slot_uri: MIXS:0000988
multivalued: false
alias: hcr
domain_of:
- Biosample
range: hcr_enum

```
</details>