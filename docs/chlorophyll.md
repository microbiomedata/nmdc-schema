# Slot: chlorophyll (chlorophyll)


_Concentration of chlorophyll_



URI: [MIXS:0000177](https://w3id.org/mixs/0000177)




## Inheritance

* [core_field](core_field.md)
    * **chlorophyll**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* chlorophyll




## Examples

| Value |
| --- |
| 5 milligram per cubic meter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | milligram per cubic meter, microgram per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: chlorophyll
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: milligram per cubic meter, microgram per liter
  occurrence:
    tag: occurrence
    value: '1'
description: Concentration of chlorophyll
title: chlorophyll
examples:
- value: 5 milligram per cubic meter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- chlorophyll
rank: 1000
is_a: core field
slot_uri: MIXS:0000177
multivalued: false
alias: chlorophyll
domain_of:
- Biosample
range: QuantityValue

```
</details>