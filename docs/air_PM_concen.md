# Slot: air particulate matter concentration (air_PM_concen)


_Concentration of substances that remain suspended in the air, and comprise mixtures of organic and inorganic substances (PM10 and PM2.5); can report multiple PM's by entering numeric values preceded by name of PM_



URI: [MIXS:0000108](https://w3id.org/mixs/0000108)




## Inheritance

* [core_field](core_field.md)
    * **air_PM_concen**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* air particulate matter concentration




## Examples

| Value |
| --- |
| PM2.5;10 microgram per cubic meter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | particulate matter name;measurement value || preferred_unit | micrograms per cubic meter || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: air_PM_concen
annotations:
  expected_value:
    tag: expected_value
    value: particulate matter name;measurement value
  preferred_unit:
    tag: preferred_unit
    value: micrograms per cubic meter
  occurrence:
    tag: occurrence
    value: m
description: Concentration of substances that remain suspended in the air, and comprise
  mixtures of organic and inorganic substances (PM10 and PM2.5); can report multiple
  PM's by entering numeric values preceded by name of PM
title: air particulate matter concentration
examples:
- value: PM2.5;10 microgram per cubic meter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- air particulate matter concentration
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000108
multivalued: true
alias: air_PM_concen
domain_of:
- Biosample
range: TextValue

```
</details>