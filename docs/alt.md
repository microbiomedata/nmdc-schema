# Slot: altitude (alt)


_Altitude is a term used to identify heights of objects such as airplanes, space shuttles, rockets, atmospheric balloons and heights of places such as atmospheric layers and clouds. It is used to measure the height of an object which is above the earth's surface. In this context, the altitude measurement is the vertical distance between the earth's surface above sea level and the sampled position in the air_



URI: [MIXS:0000094](https://w3id.org/mixs/0000094)




## Inheritance

* [environment_field](environment_field.md)
    * **alt**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* altitude




## Examples

| Value |
| --- |
| 100 meter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: alt
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
description: Altitude is a term used to identify heights of objects such as airplanes,
  space shuttles, rockets, atmospheric balloons and heights of places such as atmospheric
  layers and clouds. It is used to measure the height of an object which is above
  the earth's surface. In this context, the altitude measurement is the vertical distance
  between the earth's surface above sea level and the sampled position in the air
title: altitude
examples:
- value: 100 meter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- altitude
rank: 1000
is_a: environment field
slot_uri: MIXS:0000094
multivalued: false
alias: alt
domain_of:
- Biosample
range: QuantityValue

```
</details>