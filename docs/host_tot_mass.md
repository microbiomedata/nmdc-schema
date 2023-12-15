# Slot: host total mass (host_tot_mass)


_Total mass of the host at collection, the unit depends on host_



URI: [MIXS:0000263](https://w3id.org/mixs/0000263)




## Inheritance

* [core_field](core_field.md)
    * **host_tot_mass**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* host total mass




## Examples

| Value |
| --- |
| 2500 gram |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | kilogram, gram || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: host_tot_mass
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: kilogram, gram
  occurrence:
    tag: occurrence
    value: '1'
description: Total mass of the host at collection, the unit depends on host
title: host total mass
examples:
- value: 2500 gram
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- host total mass
rank: 1000
is_a: core field
slot_uri: MIXS:0000263
multivalued: false
alias: host_tot_mass
domain_of:
- Biosample
range: QuantityValue

```
</details>