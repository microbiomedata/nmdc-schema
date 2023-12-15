# Slot: phaeopigments (phaeopigments)


_Concentration of phaeopigments; can include multiple phaeopigments_



URI: [MIXS:0000180](https://w3id.org/mixs/0000180)




## Inheritance

* [core_field](core_field.md)
    * **phaeopigments**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* phaeopigments




## Examples

| Value |
| --- |
| 2.5 milligram per cubic meter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | phaeopigment name;measurement value || preferred_unit | milligram per cubic meter || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: phaeopigments
annotations:
  expected_value:
    tag: expected_value
    value: phaeopigment name;measurement value
  preferred_unit:
    tag: preferred_unit
    value: milligram per cubic meter
  occurrence:
    tag: occurrence
    value: m
description: Concentration of phaeopigments; can include multiple phaeopigments
title: phaeopigments
examples:
- value: 2.5 milligram per cubic meter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- phaeopigments
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000180
multivalued: true
alias: phaeopigments
domain_of:
- Biosample
range: TextValue

```
</details>