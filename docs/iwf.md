# Slot: injection water fraction (iwf)


_Proportion of the produced fluids derived from injected water at the time of sampling. (e.g. 87%)_



URI: [MIXS:0000455](https://w3id.org/mixs/0000455)




## Inheritance

* [core_field](core_field.md)
    * **iwf**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* injection water fraction




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | percent || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: iwf
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: percent
  occurrence:
    tag: occurrence
    value: '1'
description: Proportion of the produced fluids derived from injected water at the
  time of sampling. (e.g. 87%)
title: injection water fraction
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- injection water fraction
rank: 1000
is_a: core field
slot_uri: MIXS:0000455
multivalued: false
alias: iwf
domain_of:
- Biosample
range: QuantityValue

```
</details>