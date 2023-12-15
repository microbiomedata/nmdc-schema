# Slot: total acid number (tan)


_Total Acid Number¬†(TAN) is a measurement of acidity that is determined by the amount of¬†potassium hydroxide¬†in milligrams that is needed to neutralize the acids in one gram of oil.¬†It is an important quality measurement of¬†crude oil. (source: https://en.wikipedia.org/wiki/Total_acid_number)_



URI: [MIXS:0000120](https://w3id.org/mixs/0000120)




## Inheritance

* [core_field](core_field.md)
    * **tan**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* total acid number




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | milligram per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: tan
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: milligram per liter
  occurrence:
    tag: occurrence
    value: '1'
description: 'Total Acid Number¬†(TAN) is a measurement of acidity that is determined
  by the amount of¬†potassium hydroxide¬†in milligrams that is needed to neutralize
  the acids in one gram of oil.¬†It is an important quality measurement of¬†crude
  oil. (source: https://en.wikipedia.org/wiki/Total_acid_number)'
title: total acid number
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- total acid number
rank: 1000
is_a: core field
slot_uri: MIXS:0000120
multivalued: false
alias: tan
domain_of:
- Biosample
range: QuantityValue

```
</details>