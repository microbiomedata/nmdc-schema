# Slot: photon flux (photon_flux)


_Measurement of photon flux_



URI: [MIXS:0000725](https://w3id.org/mixs/0000725)




## Inheritance

* [core_field](core_field.md)
    * **photon_flux**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* photon flux




## Examples

| Value |
| --- |
| 3.926 micromole photons per second per square meter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | number of photons per second per unit area || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: photon_flux
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: number of photons per second per unit area
  occurrence:
    tag: occurrence
    value: '1'
description: Measurement of photon flux
title: photon flux
examples:
- value: 3.926 micromole photons per second per square meter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- photon flux
rank: 1000
is_a: core field
slot_uri: MIXS:0000725
multivalued: false
alias: photon_flux
domain_of:
- Biosample
range: QuantityValue

```
</details>