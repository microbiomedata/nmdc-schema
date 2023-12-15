# Slot: sample disease stage (samp_dis_stage)


_Stage of the disease at the time of sample collection, e.g. inoculation, penetration, infection, growth and reproduction, dissemination of pathogen._



URI: [MIXS:0000249](https://w3id.org/mixs/0000249)




## Inheritance

* [core_field](core_field.md)
    * **samp_dis_stage**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [SampDisStageEnum](SampDisStageEnum.md)



## Aliases


* sample disease stage




## Examples

| Value |
| --- |
| infection |

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
name: samp_dis_stage
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: Stage of the disease at the time of sample collection, e.g. inoculation,
  penetration, infection, growth and reproduction, dissemination of pathogen.
title: sample disease stage
examples:
- value: infection
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- sample disease stage
rank: 1000
is_a: core field
slot_uri: MIXS:0000249
multivalued: false
alias: samp_dis_stage
domain_of:
- Biosample
range: samp_dis_stage_enum

```
</details>