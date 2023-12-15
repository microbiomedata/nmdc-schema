# Slot: longitude


_longitude_



URI: [wgs84:long](http://www.w3.org/2003/01/geo/wgs84_pos#long)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[GeolocationValue](GeolocationValue.md) | A normalized value for a location on the earth's surface |  yes  |







## Properties

* Range: [DecimalDegree](DecimalDegree.md)






## Examples

| Value |
| --- |
| 150.168149 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: longitude
description: longitude
examples:
- value: '150.168149'
from_schema: https://w3id.org/nmdc/nmdc
mappings:
- schema:longitude
rank: 1000
domain: GeolocationValue
slot_uri: wgs84:long
alias: longitude
domain_of:
- GeolocationValue
range: decimal degree

```
</details>