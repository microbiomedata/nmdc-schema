# Slot: corrosion rate at sample location (samp_loc_corr_rate)


_Metal corrosion rate is the speed of metal deterioration due to environmental conditions. As environmental conditions change corrosion rates change accordingly. Therefore, long term corrosion rates are generally more informative than short term rates and for that reason they are preferred during reporting. In the case of suspected MIC, corrosion rate measurements at the time of sampling might provide insights into the involvement of certain microbial community members in MIC as well as potential microbial interplays_



URI: [MIXS:0000136](https://w3id.org/mixs/0000136)




## Inheritance

* [core_field](core_field.md)
    * **samp_loc_corr_rate**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* corrosion rate at sample location




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value range || preferred_unit | millimeter per year || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: samp_loc_corr_rate
annotations:
  expected_value:
    tag: expected_value
    value: measurement value range
  preferred_unit:
    tag: preferred_unit
    value: millimeter per year
  occurrence:
    tag: occurrence
    value: '1'
description: Metal corrosion rate is the speed of metal deterioration due to environmental
  conditions. As environmental conditions change corrosion rates change accordingly.
  Therefore, long term corrosion rates are generally more informative than short term
  rates and for that reason they are preferred during reporting. In the case of suspected
  MIC, corrosion rate measurements at the time of sampling might provide insights
  into the involvement of certain microbial community members in MIC as well as potential
  microbial interplays
title: corrosion rate at sample location
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- corrosion rate at sample location
rank: 1000
is_a: core field
string_serialization: '{float} - {float} {unit}'
slot_uri: MIXS:0000136
multivalued: false
alias: samp_loc_corr_rate
domain_of:
- Biosample
range: TextValue

```
</details>