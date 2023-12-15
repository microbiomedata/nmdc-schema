# Slot: herbicide regimen (herbicide_regm)


_Information about treatment involving use of herbicides; information about treatment involving use of growth hormones; should include the name of herbicide, amount administered, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple regimens_



URI: [MIXS:0000561](https://w3id.org/mixs/0000561)




## Inheritance

* [core_field](core_field.md)
    * **herbicide_regm**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* herbicide regimen




## Examples

| Value |
| --- |
| atrazine;10 milligram per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | herbicide name;herbicide amount;treatment interval and duration || preferred_unit | gram, mole per liter, milligram per liter || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: herbicide_regm
annotations:
  expected_value:
    tag: expected_value
    value: herbicide name;herbicide amount;treatment interval and duration
  preferred_unit:
    tag: preferred_unit
    value: gram, mole per liter, milligram per liter
  occurrence:
    tag: occurrence
    value: m
description: Information about treatment involving use of herbicides; information
  about treatment involving use of growth hormones; should include the name of herbicide,
  amount administered, treatment regimen including how many times the treatment was
  repeated, how long each treatment lasted, and the start and end time of the entire
  treatment; can include multiple regimens
title: herbicide regimen
examples:
- value: atrazine;10 milligram per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- herbicide regimen
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit};{Rn/start_time/end_time/duration}'
slot_uri: MIXS:0000561
multivalued: true
alias: herbicide_regm
domain_of:
- Biosample
range: TextValue

```
</details>