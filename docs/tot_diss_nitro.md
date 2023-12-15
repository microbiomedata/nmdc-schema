# Slot: total dissolved nitrogen (tot_diss_nitro)


_Total dissolved nitrogen concentration, reported as nitrogen, measured by: total dissolved nitrogen = NH4 + NO3NO2 + dissolved organic nitrogen_



URI: [MIXS:0000744](https://w3id.org/mixs/0000744)




## Inheritance

* [core_field](core_field.md)
    * **tot_diss_nitro**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* total dissolved nitrogen




## Examples

| Value |
| --- |
| 40 microgram per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | microgram per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: tot_diss_nitro
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: microgram per liter
  occurrence:
    tag: occurrence
    value: '1'
description: 'Total dissolved nitrogen concentration, reported as nitrogen, measured
  by: total dissolved nitrogen = NH4 + NO3NO2 + dissolved organic nitrogen'
title: total dissolved nitrogen
examples:
- value: 40 microgram per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- total dissolved nitrogen
rank: 1000
is_a: core field
slot_uri: MIXS:0000744
multivalued: false
alias: tot_diss_nitro
domain_of:
- Biosample
range: QuantityValue

```
</details>