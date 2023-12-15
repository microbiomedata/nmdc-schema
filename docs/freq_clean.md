# Slot: frequency of cleaning (freq_clean)


_The number of times the sample location is cleaned. Frequency of cleaning might be on a Daily basis, Weekly, Monthly, Quarterly or Annually._



URI: [MIXS:0000226](https://w3id.org/mixs/0000226)




## Inheritance

* [core_field](core_field.md)
    * **freq_clean**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* frequency of cleaning




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | enumeration or {text} || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: freq_clean
annotations:
  expected_value:
    tag: expected_value
    value: enumeration or {text}
  occurrence:
    tag: occurrence
    value: '1'
description: The number of times the sample location is cleaned. Frequency of cleaning
  might be on a Daily basis, Weekly, Monthly, Quarterly or Annually.
title: frequency of cleaning
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- frequency of cleaning
rank: 1000
is_a: core field
slot_uri: MIXS:0000226
multivalued: false
alias: freq_clean
domain_of:
- Biosample
range: QuantityValue

```
</details>