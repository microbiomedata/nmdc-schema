# Slot: latitude


_latitude_



URI: [wgs84:lat](http://www.w3.org/2003/01/geo/wgs84_pos#lat)



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
| -33.460524 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: latitude
description: latitude
examples:
- value: '-33.460524'
from_schema: https://w3id.org/nmdc/nmdc
mappings:
- schema:latitude
rank: 1000
domain: GeolocationValue
slot_uri: wgs84:lat
alias: latitude
domain_of:
- GeolocationValue
range: decimal degree

```
</details>