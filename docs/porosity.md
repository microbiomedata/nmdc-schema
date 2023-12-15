# Slot: porosity (porosity)


_Porosity of deposited sediment is volume of voids divided by the total volume of sample_



URI: [MIXS:0000211](https://w3id.org/mixs/0000211)




## Inheritance

* [core_field](core_field.md)
    * **porosity**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* porosity




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value or range || preferred_unit | percentage || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: porosity
annotations:
  expected_value:
    tag: expected_value
    value: measurement value or range
  preferred_unit:
    tag: preferred_unit
    value: percentage
  occurrence:
    tag: occurrence
    value: '1'
description: Porosity of deposited sediment is volume of voids divided by the total
  volume of sample
title: porosity
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- porosity
rank: 1000
is_a: core field
string_serialization: '{float} - {float} {unit}'
slot_uri: MIXS:0000211
multivalued: false
alias: porosity
domain_of:
- Biosample
range: TextValue

```
</details>