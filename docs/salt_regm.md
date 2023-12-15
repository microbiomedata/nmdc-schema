# Slot: salt regimen (salt_regm)


_Information about treatment involving use of salts as supplement to liquid and soil growth media; should include the name of salt, amount administered, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple salt regimens_



URI: [MIXS:0000582](https://w3id.org/mixs/0000582)




## Inheritance

* [core_field](core_field.md)
    * **salt_regm**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* salt regimen




## Examples

| Value |
| --- |
| NaCl;5 gram per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | salt name;salt amount;treatment interval and duration || preferred_unit | gram, microgram, mole per liter, gram per liter || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: salt_regm
annotations:
  expected_value:
    tag: expected_value
    value: salt name;salt amount;treatment interval and duration
  preferred_unit:
    tag: preferred_unit
    value: gram, microgram, mole per liter, gram per liter
  occurrence:
    tag: occurrence
    value: m
description: Information about treatment involving use of salts as supplement to liquid
  and soil growth media; should include the name of salt, amount administered, treatment
  regimen including how many times the treatment was repeated, how long each treatment
  lasted, and the start and end time of the entire treatment; can include multiple
  salt regimens
title: salt regimen
examples:
- value: NaCl;5 gram per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- salt regimen
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit};{Rn/start_time/end_time/duration}'
slot_uri: MIXS:0000582
multivalued: true
alias: salt_regm
domain_of:
- Biosample
range: TextValue

```
</details>