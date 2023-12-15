# Slot: volatile organic compounds (volatile_org_comp)


_Concentration of carbon-based chemicals that easily evaporate at room temperature; can report multiple volatile organic compounds by entering numeric values preceded by name of compound_



URI: [MIXS:0000115](https://w3id.org/mixs/0000115)




## Inheritance

* [core_field](core_field.md)
    * **volatile_org_comp**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* volatile organic compounds




## Examples

| Value |
| --- |
| formaldehyde;500 nanogram per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | volatile organic compound name;measurement value || preferred_unit | microgram per cubic meter, parts per million, nanogram per liter || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: volatile_org_comp
annotations:
  expected_value:
    tag: expected_value
    value: volatile organic compound name;measurement value
  preferred_unit:
    tag: preferred_unit
    value: microgram per cubic meter, parts per million, nanogram per liter
  occurrence:
    tag: occurrence
    value: m
description: Concentration of carbon-based chemicals that easily evaporate at room
  temperature; can report multiple volatile organic compounds by entering numeric
  values preceded by name of compound
title: volatile organic compounds
examples:
- value: formaldehyde;500 nanogram per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- volatile organic compounds
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000115
multivalued: true
alias: volatile_org_comp
domain_of:
- Biosample
range: TextValue

```
</details>