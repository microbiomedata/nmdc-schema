# Slot: sample collection point (samp_collect_point)


_Sampling point on the asset were sample was collected (e.g. Wellhead, storage tank, separator, etc). If "other" is specified, please propose entry in "additional info" field_



URI: [MIXS:0001015](https://w3id.org/mixs/0001015)




## Inheritance

* [core_field](core_field.md)
    * **samp_collect_point**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [SampCollectPointEnum](SampCollectPointEnum.md)



## Aliases


* sample collection point




## Examples

| Value |
| --- |
| well |

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
name: samp_collect_point
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: Sampling point on the asset were sample was collected (e.g. Wellhead,
  storage tank, separator, etc). If "other" is specified, please propose entry in
  "additional info" field
title: sample collection point
examples:
- value: well
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- sample collection point
rank: 1000
is_a: core field
slot_uri: MIXS:0001015
multivalued: false
alias: samp_collect_point
domain_of:
- Biosample
range: samp_collect_point_enum

```
</details>