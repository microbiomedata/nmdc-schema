# Slot: fluorescence (fluor)


_Raw or converted fluorescence of water_



URI: [MIXS:0000704](https://w3id.org/mixs/0000704)




## Inheritance

* [core_field](core_field.md)
    * **fluor**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* fluorescence




## Examples

| Value |
| --- |
| 2.5 volts |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | milligram chlorophyll a per cubic meter, volts || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: fluor
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: milligram chlorophyll a per cubic meter, volts
  occurrence:
    tag: occurrence
    value: '1'
description: Raw or converted fluorescence of water
title: fluorescence
examples:
- value: 2.5 volts
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- fluorescence
rank: 1000
is_a: core field
slot_uri: MIXS:0000704
multivalued: false
alias: fluor
domain_of:
- Biosample
range: QuantityValue

```
</details>