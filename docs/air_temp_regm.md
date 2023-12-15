# Slot: air temperature regimen (air_temp_regm)


_Information about treatment involving an exposure to varying temperatures; should include the temperature, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include different temperature regimens_



URI: [MIXS:0000551](https://w3id.org/mixs/0000551)




## Inheritance

* [core_field](core_field.md)
    * **air_temp_regm**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* air temperature regimen




## Examples

| Value |
| --- |
| 25 degree Celsius;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | temperature value;treatment interval and duration || preferred_unit | meter || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: air_temp_regm
annotations:
  expected_value:
    tag: expected_value
    value: temperature value;treatment interval and duration
  preferred_unit:
    tag: preferred_unit
    value: meter
  occurrence:
    tag: occurrence
    value: m
description: Information about treatment involving an exposure to varying temperatures;
  should include the temperature, treatment regimen including how many times the treatment
  was repeated, how long each treatment lasted, and the start and end time of the
  entire treatment; can include different temperature regimens
title: air temperature regimen
examples:
- value: 25 degree Celsius;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- air temperature regimen
rank: 1000
is_a: core field
string_serialization: '{float} {unit};{Rn/start_time/end_time/duration}'
slot_uri: MIXS:0000551
multivalued: true
alias: air_temp_regm
domain_of:
- Biosample
range: TextValue

```
</details>