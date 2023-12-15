# Slot: geographic location (latitude and longitude) (lat_lon)


_The geographical origin of the sample as defined by latitude and longitude. The values should be reported in decimal degrees and in WGS84 system_



URI: [MIXS:0000009](https://w3id.org/mixs/0000009)




## Inheritance

* [environment_field](environment_field.md)
    * **lat_lon**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FieldResearchSite](FieldResearchSite.md) | A site, outside of a laboratory, from which biosamples may be collected |  no  |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [GeolocationValue](GeolocationValue.md)



## Aliases


* geographic location (latitude and longitude)




## Examples

| Value |
| --- |
| 50.586825 6.408977 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | decimal degrees,  limit to 8 decimal points |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: lat_lon
annotations:
  expected_value:
    tag: expected_value
    value: decimal degrees,  limit to 8 decimal points
description: The geographical origin of the sample as defined by latitude and longitude.
  The values should be reported in decimal degrees and in WGS84 system
title: geographic location (latitude and longitude)
examples:
- value: 50.586825 6.408977
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- geographic location (latitude and longitude)
rank: 1000
is_a: environment field
string_serialization: '{float} {float}'
slot_uri: MIXS:0000009
multivalued: false
alias: lat_lon
domain_of:
- FieldResearchSite
- Biosample
range: GeolocationValue

```
</details>