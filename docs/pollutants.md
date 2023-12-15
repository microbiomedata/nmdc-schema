# Slot: pollutants (pollutants)


_Pollutant types and, amount or concentrations measured at the time of sampling; can report multiple pollutants by entering numeric values preceded by name of pollutant_



URI: [MIXS:0000107](https://w3id.org/mixs/0000107)




## Inheritance

* [core_field](core_field.md)
    * **pollutants**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* pollutants




## Examples

| Value |
| --- |
| lead;0.15 microgram per cubic meter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | pollutant name;measurement value || preferred_unit | gram, mole per liter, milligram per liter, microgram per cubic meter || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: pollutants
annotations:
  expected_value:
    tag: expected_value
    value: pollutant name;measurement value
  preferred_unit:
    tag: preferred_unit
    value: gram, mole per liter, milligram per liter, microgram per cubic meter
  occurrence:
    tag: occurrence
    value: m
description: Pollutant types and, amount or concentrations measured at the time of
  sampling; can report multiple pollutants by entering numeric values preceded by
  name of pollutant
title: pollutants
examples:
- value: lead;0.15 microgram per cubic meter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- pollutants
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000107
multivalued: true
alias: pollutants
domain_of:
- Biosample
range: TextValue

```
</details>