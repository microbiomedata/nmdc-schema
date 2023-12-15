# Slot: surface moisture (surf_moisture)


_Water held on a surface_



URI: [MIXS:0000128](https://w3id.org/mixs/0000128)




## Inheritance

* [core_field](core_field.md)
    * **surf_moisture**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* surface moisture




## Examples

| Value |
| --- |
| 0.01 gram per square meter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | parts per million, gram per cubic meter, gram per square meter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: surf_moisture
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: parts per million, gram per cubic meter, gram per square meter
  occurrence:
    tag: occurrence
    value: '1'
description: Water held on a surface
title: surface moisture
examples:
- value: 0.01 gram per square meter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- surface moisture
rank: 1000
is_a: core field
slot_uri: MIXS:0000128
multivalued: false
alias: surf_moisture
domain_of:
- Biosample
range: QuantityValue

```
</details>