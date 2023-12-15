# Slot: history/crop rotation (crop_rotation)


_Whether or not crop is rotated, and if yes, rotation schedule_



URI: [MIXS:0000318](https://w3id.org/mixs/0000318)




## Inheritance

* [core_field](core_field.md)
    * **crop_rotation**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* history/crop rotation




## Examples

| Value |
| --- |
| yes;R2/2017-01-01/2018-12-31/P6M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | crop rotation status;schedule || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: crop_rotation
annotations:
  expected_value:
    tag: expected_value
    value: crop rotation status;schedule
  occurrence:
    tag: occurrence
    value: '1'
description: Whether or not crop is rotated, and if yes, rotation schedule
title: history/crop rotation
examples:
- value: yes;R2/2017-01-01/2018-12-31/P6M
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- history/crop rotation
rank: 1000
is_a: core field
string_serialization: '{boolean};{Rn/start_time/end_time/duration}'
slot_uri: MIXS:0000318
multivalued: false
alias: crop_rotation
domain_of:
- Biosample
range: TextValue

```
</details>