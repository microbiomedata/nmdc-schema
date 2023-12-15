# Slot: dissolved organic nitrogen (diss_org_nitro)


_Dissolved organic nitrogen concentration measured as; total dissolved nitrogen - NH4 - NO3 - NO2_



URI: [MIXS:0000162](https://w3id.org/mixs/0000162)




## Inheritance

* [core_field](core_field.md)
    * **diss_org_nitro**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* dissolved organic nitrogen




## Examples

| Value |
| --- |
| 0.05 micromole per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | microgram per liter, milligram per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: diss_org_nitro
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: microgram per liter, milligram per liter
  occurrence:
    tag: occurrence
    value: '1'
description: Dissolved organic nitrogen concentration measured as; total dissolved
  nitrogen - NH4 - NO3 - NO2
title: dissolved organic nitrogen
examples:
- value: 0.05 micromole per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- dissolved organic nitrogen
rank: 1000
is_a: core field
slot_uri: MIXS:0000162
multivalued: false
alias: diss_org_nitro
domain_of:
- Biosample
range: QuantityValue

```
</details>