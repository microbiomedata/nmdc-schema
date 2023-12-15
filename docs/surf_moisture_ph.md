# Slot: surface moisture pH (surf_moisture_ph)


_ph measurement of surface_



URI: [MIXS:0000760](https://w3id.org/mixs/0000760)




## Inheritance

* [core_field](core_field.md)
    * **surf_moisture_ph**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [Double](Double.md)



## Aliases


* surface moisture pH




## Examples

| Value |
| --- |
| 7 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: surf_moisture_ph
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  occurrence:
    tag: occurrence
    value: '1'
description: ph measurement of surface
title: surface moisture pH
examples:
- value: '7'
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- surface moisture pH
rank: 1000
is_a: core field
slot_uri: MIXS:0000760
multivalued: false
alias: surf_moisture_ph
domain_of:
- Biosample
range: double

```
</details>