# Slot: dissolved inorganic nitrogen (diss_inorg_nitro)


_Concentration of dissolved inorganic nitrogen_



URI: [MIXS:0000698](https://w3id.org/mixs/0000698)




## Inheritance

* [core_field](core_field.md)
    * **diss_inorg_nitro**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* dissolved inorganic nitrogen




## Examples

| Value |
| --- |
| 761 micromole per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | microgram per liter, micromole per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: diss_inorg_nitro
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: microgram per liter, micromole per liter
  occurrence:
    tag: occurrence
    value: '1'
description: Concentration of dissolved inorganic nitrogen
title: dissolved inorganic nitrogen
examples:
- value: 761 micromole per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- dissolved inorganic nitrogen
rank: 1000
is_a: core field
slot_uri: MIXS:0000698
multivalued: false
alias: diss_inorg_nitro
domain_of:
- Biosample
range: QuantityValue

```
</details>