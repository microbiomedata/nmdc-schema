# Slot: API gravity (api)


_API gravity is a measure of how heavy or light a petroleum liquid is compared to water (source: https://en.wikipedia.org/wiki/API_gravity) (e.g. 31.1¬∞ API)_



URI: [MIXS:0000157](https://w3id.org/mixs/0000157)




## Inheritance

* [core_field](core_field.md)
    * **api**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* API gravity




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | degrees API || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: api
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: degrees API
  occurrence:
    tag: occurrence
    value: '1'
description: 'API gravity is a measure of how heavy or light a petroleum liquid is
  compared to water (source: https://en.wikipedia.org/wiki/API_gravity) (e.g. 31.1¬∞
  API)'
title: API gravity
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- API gravity
rank: 1000
is_a: core field
slot_uri: MIXS:0000157
multivalued: false
alias: api
domain_of:
- Biosample
range: QuantityValue

```
</details>