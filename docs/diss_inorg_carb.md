# Slot: dissolved inorganic carbon (diss_inorg_carb)


_Dissolved inorganic carbon concentration in the sample, typically measured after filtering the sample using a 0.45 micrometer filter_



URI: [MIXS:0000434](https://w3id.org/mixs/0000434)




## Inheritance

* [core_field](core_field.md)
    * **diss_inorg_carb**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* dissolved inorganic carbon




## Examples

| Value |
| --- |
| 2059 micromole per kilogram |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | microgram per liter, milligram per liter, parts per million || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: diss_inorg_carb
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: microgram per liter, milligram per liter, parts per million
  occurrence:
    tag: occurrence
    value: '1'
description: Dissolved inorganic carbon concentration in the sample, typically measured
  after filtering the sample using a 0.45 micrometer filter
title: dissolved inorganic carbon
examples:
- value: 2059 micromole per kilogram
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- dissolved inorganic carbon
rank: 1000
is_a: core field
slot_uri: MIXS:0000434
multivalued: false
alias: diss_inorg_carb
domain_of:
- Biosample
range: QuantityValue

```
</details>