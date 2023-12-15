# Slot: elevation (elev)


_Elevation of the sampling site is its height above a fixed reference point, most commonly the mean sea level. Elevation is mainly used when referring to points on the earth's surface, while altitude is used for points above the surface, such as an aircraft in flight or a spacecraft in orbit._



URI: [MIXS:0000093](https://w3id.org/mixs/0000093)




## Inheritance

* [environment_field](environment_field.md)
    * **elev**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FieldResearchSite](FieldResearchSite.md) | A site, outside of a laboratory, from which biosamples may be collected |  no  |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* elevation




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
name: elev
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
description: Elevation of the sampling site is its height above a fixed reference
  point, most commonly the mean sea level. Elevation is mainly used when referring
  to points on the earth's surface, while altitude is used for points above the surface,
  such as an aircraft in flight or a spacecraft in orbit.
title: elevation
examples:
- value: 100 meter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- elevation
rank: 1000
is_a: environment field
slot_uri: MIXS:0000093
multivalued: false
alias: elev
domain_of:
- FieldResearchSite
- Biosample
range: QuantityValue

```
</details>