# Slot: petroleum hydrocarbon (petroleum_hydrocarb)


_Concentration of petroleum hydrocarbon_



URI: [MIXS:0000516](https://w3id.org/mixs/0000516)




## Inheritance

* [core_field](core_field.md)
    * **petroleum_hydrocarb**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* petroleum hydrocarbon




## Examples

| Value |
| --- |
| 0.05 micromole per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | micromole per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: petroleum_hydrocarb
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: micromole per liter
  occurrence:
    tag: occurrence
    value: '1'
description: Concentration of petroleum hydrocarbon
title: petroleum hydrocarbon
examples:
- value: 0.05 micromole per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- petroleum hydrocarbon
rank: 1000
is_a: core field
slot_uri: MIXS:0000516
multivalued: false
alias: petroleum_hydrocarb
domain_of:
- Biosample
range: QuantityValue

```
</details>