# Slot: sampling day weather (samp_weather)


_The weather on the sampling day_



URI: [MIXS:0000827](https://w3id.org/mixs/0000827)




## Inheritance

* [core_field](core_field.md)
    * **samp_weather**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [SampWeatherEnum](SampWeatherEnum.md)



## Aliases


* sampling day weather




## Examples

| Value |
| --- |
| foggy |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | enumeration || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: samp_weather
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The weather on the sampling day
title: sampling day weather
examples:
- value: foggy
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- sampling day weather
rank: 1000
is_a: core field
slot_uri: MIXS:0000827
multivalued: false
alias: samp_weather
domain_of:
- Biosample
range: samp_weather_enum

```
</details>