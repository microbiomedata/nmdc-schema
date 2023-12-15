# Slot: host dry mass (host_dry_mass)


_Measurement of dry mass_



URI: [MIXS:0000257](https://w3id.org/mixs/0000257)




## Inheritance

* [core_field](core_field.md)
    * **host_dry_mass**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* host dry mass




## Examples

| Value |
| --- |
| 500 gram |

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
name: host_dry_mass
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
description: Measurement of dry mass
title: host dry mass
examples:
- value: 500 gram
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- host dry mass
rank: 1000
is_a: core field
slot_uri: MIXS:0000257
multivalued: false
alias: host_dry_mass
domain_of:
- Biosample
range: QuantityValue

```
</details>