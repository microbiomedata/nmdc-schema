# Slot: redox potential (redox_potential)


_Redox potential, measured relative to a hydrogen cell, indicating oxidation or reduction potential_



URI: [MIXS:0000182](https://w3id.org/mixs/0000182)




## Inheritance

* [core_field](core_field.md)
    * **redox_potential**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* redox potential




## Examples

| Value |
| --- |
| 300 millivolt |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | millivolt || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: redox_potential
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: millivolt
  occurrence:
    tag: occurrence
    value: '1'
description: Redox potential, measured relative to a hydrogen cell, indicating oxidation
  or reduction potential
title: redox potential
examples:
- value: 300 millivolt
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- redox potential
rank: 1000
is_a: core field
slot_uri: MIXS:0000182
multivalued: false
alias: redox_potential
domain_of:
- Biosample
range: QuantityValue

```
</details>