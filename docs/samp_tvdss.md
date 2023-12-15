# Slot: sample true vertical depth subsea (samp_tvdss)


_Depth of the sample i.e. The vertical distance between the sea level and the sampled position in the subsurface. Depth can be reported as an interval for subsurface samples e.g. 1325.75-1362.25 m_



URI: [MIXS:0000409](https://w3id.org/mixs/0000409)




## Inheritance

* [core_field](core_field.md)
    * **samp_tvdss**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* sample true vertical depth subsea




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value or measurement value range || preferred_unit | meter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: samp_tvdss
annotations:
  expected_value:
    tag: expected_value
    value: measurement value or measurement value range
  preferred_unit:
    tag: preferred_unit
    value: meter
  occurrence:
    tag: occurrence
    value: '1'
description: Depth of the sample i.e. The vertical distance between the sea level
  and the sampled position in the subsurface. Depth can be reported as an interval
  for subsurface samples e.g. 1325.75-1362.25 m
title: sample true vertical depth subsea
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- sample true vertical depth subsea
rank: 1000
is_a: core field
string_serialization: '{float}-{float} {unit}'
slot_uri: MIXS:0000409
multivalued: false
alias: samp_tvdss
domain_of:
- Biosample
range: TextValue

```
</details>