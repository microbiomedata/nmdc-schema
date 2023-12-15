# Slot: oxygenation status of sample (oxy_stat_samp)


_Oxygenation status of sample_



URI: [MIXS:0000753](https://w3id.org/mixs/0000753)




## Inheritance

* [core_field](core_field.md)
    * **oxy_stat_samp**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [OxyStatSampEnum](OxyStatSampEnum.md)



## Aliases


* oxygenation status of sample




## Examples

| Value |
| --- |
| aerobic |

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
name: oxy_stat_samp
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: Oxygenation status of sample
title: oxygenation status of sample
examples:
- value: aerobic
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- oxygenation status of sample
rank: 1000
is_a: core field
slot_uri: MIXS:0000753
multivalued: false
alias: oxy_stat_samp
domain_of:
- Biosample
range: oxy_stat_samp_enum

```
</details>