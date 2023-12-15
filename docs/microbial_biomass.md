# Slot: microbial biomass (microbial_biomass)


_The part of the organic matter in the soil that constitutes living microorganisms smaller than 5-10 micrometer. If you keep this, you would need to have correction factors used for conversion to the final units_



URI: [MIXS:0000650](https://w3id.org/mixs/0000650)




## Inheritance

* [core_field](core_field.md)
    * **microbial_biomass**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* microbial biomass




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | ton, kilogram, gram per kilogram soil || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: microbial_biomass
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: ton, kilogram, gram per kilogram soil
  occurrence:
    tag: occurrence
    value: '1'
description: The part of the organic matter in the soil that constitutes living microorganisms
  smaller than 5-10 micrometer. If you keep this, you would need to have correction
  factors used for conversion to the final units
title: microbial biomass
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- microbial biomass
rank: 1000
is_a: core field
slot_uri: MIXS:0000650
multivalued: false
alias: microbial_biomass
domain_of:
- Biosample
range: QuantityValue

```
</details>