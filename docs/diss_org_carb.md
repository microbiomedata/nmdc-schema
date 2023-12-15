# Slot: dissolved organic carbon (diss_org_carb)


_Concentration of dissolved organic carbon in the sample, liquid portion of the sample, or aqueous phase of the fluid_



URI: [MIXS:0000433](https://w3id.org/mixs/0000433)




## Inheritance

* [core_field](core_field.md)
    * **diss_org_carb**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* dissolved organic carbon




## Examples

| Value |
| --- |
| 197 micromole per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | micromole per liter, milligram per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: diss_org_carb
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: micromole per liter, milligram per liter
  occurrence:
    tag: occurrence
    value: '1'
description: Concentration of dissolved organic carbon in the sample, liquid portion
  of the sample, or aqueous phase of the fluid
title: dissolved organic carbon
examples:
- value: 197 micromole per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- dissolved organic carbon
rank: 1000
is_a: core field
slot_uri: MIXS:0000433
multivalued: false
alias: diss_org_carb
domain_of:
- Biosample
range: QuantityValue

```
</details>