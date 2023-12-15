# Slot: built structure age (built_struc_age)


_The age of the built structure since construction_



URI: [MIXS:0000145](https://w3id.org/mixs/0000145)




## Inheritance

* [core_field](core_field.md)
    * **built_struc_age**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* built structure age




## Examples

| Value |
| --- |
| 15 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | value || preferred_unit | year || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: built_struc_age
annotations:
  expected_value:
    tag: expected_value
    value: value
  preferred_unit:
    tag: preferred_unit
    value: year
  occurrence:
    tag: occurrence
    value: '1'
description: The age of the built structure since construction
title: built structure age
examples:
- value: '15'
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- built structure age
rank: 1000
is_a: core field
slot_uri: MIXS:0000145
multivalued: false
alias: built_struc_age
domain_of:
- Biosample
range: QuantityValue

```
</details>