# Slot: gaseous environment (gaseous_environment)


_Use of conditions with differing gaseous environments; should include the name of gaseous compound, amount administered, treatment duration, interval and total experimental duration; can include multiple gaseous environment regimens_



URI: [MIXS:0000558](https://w3id.org/mixs/0000558)




## Inheritance

* [core_field](core_field.md)
    * **gaseous_environment**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* gaseous environment




## Examples

| Value |
| --- |
| nitric oxide;0.5 micromole per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | gaseous compound name;gaseous compound amount;treatment interval and duration || preferred_unit | micromole per liter || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: gaseous_environment
annotations:
  expected_value:
    tag: expected_value
    value: gaseous compound name;gaseous compound amount;treatment interval and duration
  preferred_unit:
    tag: preferred_unit
    value: micromole per liter
  occurrence:
    tag: occurrence
    value: m
description: Use of conditions with differing gaseous environments; should include
  the name of gaseous compound, amount administered, treatment duration, interval
  and total experimental duration; can include multiple gaseous environment regimens
title: gaseous environment
examples:
- value: nitric oxide;0.5 micromole per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- gaseous environment
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit};{Rn/start_time/end_time/duration}'
slot_uri: MIXS:0000558
multivalued: true
alias: gaseous_environment
domain_of:
- Biosample
range: TextValue

```
</details>