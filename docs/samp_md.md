# Slot: sample measured depth (samp_md)


_In non deviated well, measured depth is equal to the true vertical depth, TVD (TVD=TVDSS plus the reference or datum it refers to). In deviated wells, the MD is the length of trajectory of the borehole measured from the same reference or datum. Common datums used are ground level (GL), drilling rig floor (DF), rotary table (RT), kelly bushing (KB) and mean sea level (MSL). If "other" is specified, please propose entry in "additional info" field_



URI: [MIXS:0000413](https://w3id.org/mixs/0000413)




## Inheritance

* [core_field](core_field.md)
    * **samp_md**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* sample measured depth




## Examples

| Value |
| --- |
| 1534 meter;MSL |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value;enumeration || preferred_unit | meter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: samp_md
annotations:
  expected_value:
    tag: expected_value
    value: measurement value;enumeration
  preferred_unit:
    tag: preferred_unit
    value: meter
  occurrence:
    tag: occurrence
    value: '1'
description: In non deviated well, measured depth is equal to the true vertical depth,
  TVD (TVD=TVDSS plus the reference or datum it refers to). In deviated wells, the
  MD is the length of trajectory of the borehole measured from the same reference
  or datum. Common datums used are ground level (GL), drilling rig floor (DF), rotary
  table (RT), kelly bushing (KB) and mean sea level (MSL). If "other" is specified,
  please propose entry in "additional info" field
title: sample measured depth
examples:
- value: 1534 meter;MSL
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- sample measured depth
rank: 1000
is_a: core field
slot_uri: MIXS:0000413
multivalued: false
alias: samp_md
domain_of:
- Biosample
range: QuantityValue

```
</details>