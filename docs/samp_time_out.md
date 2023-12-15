# Slot: sampling time outside (samp_time_out)


_The recent and long term history of outside sampling_



URI: [MIXS:0000196](https://w3id.org/mixs/0000196)




## Inheritance

* [core_field](core_field.md)
    * **samp_time_out**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* sampling time outside




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | time || preferred_unit | hour || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: samp_time_out
annotations:
  expected_value:
    tag: expected_value
    value: time
  preferred_unit:
    tag: preferred_unit
    value: hour
  occurrence:
    tag: occurrence
    value: '1'
description: The recent and long term history of outside sampling
title: sampling time outside
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- sampling time outside
rank: 1000
is_a: core field
slot_uri: MIXS:0000196
multivalued: false
alias: samp_time_out
domain_of:
- Biosample
range: TextValue

```
</details>