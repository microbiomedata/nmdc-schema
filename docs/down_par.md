# Slot: downward PAR (down_par)


_Visible waveband radiance and irradiance measurements in the water column_



URI: [MIXS:0000703](https://w3id.org/mixs/0000703)




## Inheritance

* [core_field](core_field.md)
    * **down_par**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* downward PAR




## Examples

| Value |
| --- |
| 28.71 microEinstein per square meter per second |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | microEinstein per square meter per second, microEinstein per square centimeter per second || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: down_par
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: microEinstein per square meter per second, microEinstein per square centimeter
      per second
  occurrence:
    tag: occurrence
    value: '1'
description: Visible waveband radiance and irradiance measurements in the water column
title: downward PAR
examples:
- value: 28.71 microEinstein per square meter per second
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- downward PAR
rank: 1000
is_a: core field
slot_uri: MIXS:0000703
multivalued: false
alias: down_par
domain_of:
- Biosample
range: QuantityValue

```
</details>