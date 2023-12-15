# Slot: sample capture status (samp_capt_status)


_Reason for the sample_



URI: [MIXS:0000860](https://w3id.org/mixs/0000860)




## Inheritance

* [core_field](core_field.md)
    * **samp_capt_status**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [SampCaptStatusEnum](SampCaptStatusEnum.md)



## Aliases


* sample capture status




## Examples

| Value |
| --- |
| farm sample |

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
name: samp_capt_status
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: Reason for the sample
title: sample capture status
examples:
- value: farm sample
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- sample capture status
rank: 1000
is_a: core field
slot_uri: MIXS:0000860
multivalued: false
alias: samp_capt_status
domain_of:
- Biosample
range: samp_capt_status_enum

```
</details>