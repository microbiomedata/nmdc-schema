# Slot: history/agrochemical additions (agrochem_addition)


_Addition of fertilizers, pesticides, etc. - amount and time of applications_



URI: [MIXS:0000639](https://w3id.org/mixs/0000639)




## Inheritance

* [core_field](core_field.md)
    * **agrochem_addition**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* history/agrochemical additions




## Examples

| Value |
| --- |
| roundup;5 milligram per liter;2018-06-21 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | agrochemical name;agrochemical amount;timestamp || preferred_unit | gram, mole per liter, milligram per liter || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: agrochem_addition
annotations:
  expected_value:
    tag: expected_value
    value: agrochemical name;agrochemical amount;timestamp
  preferred_unit:
    tag: preferred_unit
    value: gram, mole per liter, milligram per liter
  occurrence:
    tag: occurrence
    value: m
description: Addition of fertilizers, pesticides, etc. - amount and time of applications
title: history/agrochemical additions
examples:
- value: roundup;5 milligram per liter;2018-06-21
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- history/agrochemical additions
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit};{timestamp}'
slot_uri: MIXS:0000639
multivalued: true
alias: agrochem_addition
domain_of:
- Biosample
range: TextValue

```
</details>