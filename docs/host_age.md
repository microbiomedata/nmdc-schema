# Slot: host age (host_age)


_Age of host at the time of sampling; relevant scale depends on species and study, e.g. Could be seconds for amoebae or centuries for trees_



URI: [MIXS:0000255](https://w3id.org/mixs/0000255)




## Inheritance

* [core_field](core_field.md)
    * **host_age**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* host age




## Examples

| Value |
| --- |
| 10 days |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | value || preferred_unit | year, day, hour || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: host_age
annotations:
  expected_value:
    tag: expected_value
    value: value
  preferred_unit:
    tag: preferred_unit
    value: year, day, hour
  occurrence:
    tag: occurrence
    value: '1'
description: Age of host at the time of sampling; relevant scale depends on species
  and study, e.g. Could be seconds for amoebae or centuries for trees
title: host age
examples:
- value: 10 days
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- host age
rank: 1000
is_a: core field
slot_uri: MIXS:0000255
multivalued: false
alias: host_age
domain_of:
- Biosample
range: QuantityValue

```
</details>