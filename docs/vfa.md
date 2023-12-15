# Slot: volatile fatty acids (vfa)


_Concentration of Volatile Fatty Acids in the sample_



URI: [MIXS:0000152](https://w3id.org/mixs/0000152)




## Inheritance

* [core_field](core_field.md)
    * **vfa**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* volatile fatty acids




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | milligram per liter, parts per million || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: vfa
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: milligram per liter, parts per million
  occurrence:
    tag: occurrence
    value: '1'
description: Concentration of Volatile Fatty Acids in the sample
title: volatile fatty acids
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- volatile fatty acids
rank: 1000
is_a: core field
slot_uri: MIXS:0000152
multivalued: false
alias: vfa
domain_of:
- Biosample
range: QuantityValue

```
</details>