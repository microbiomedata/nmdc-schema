# Slot: number of residents (number_resident)


_The number of individuals currently occupying in the sampling location_



URI: [MIXS:0000232](https://w3id.org/mixs/0000232)




## Inheritance

* [core_field](core_field.md)
    * **number_resident**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* number of residents




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: number_resident
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  occurrence:
    tag: occurrence
    value: '1'
description: The number of individuals currently occupying in the sampling location
title: number of residents
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- number of residents
rank: 1000
is_a: core field
slot_uri: MIXS:0000232
multivalued: false
alias: number_resident
domain_of:
- Biosample
range: QuantityValue

```
</details>