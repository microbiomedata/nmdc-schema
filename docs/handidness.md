# Slot: handidness (handidness)


_The handidness of the individual sampled_



URI: [MIXS:0000809](https://w3id.org/mixs/0000809)




## Inheritance

* [core_field](core_field.md)
    * **handidness**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [HandidnessEnum](HandidnessEnum.md)



## Aliases


* handidness




## Examples

| Value |
| --- |
| right handedness |

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
name: handidness
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The handidness of the individual sampled
title: handidness
examples:
- value: right handedness
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- handidness
rank: 1000
is_a: core field
slot_uri: MIXS:0000809
multivalued: false
alias: handidness
domain_of:
- Biosample
range: handidness_enum

```
</details>