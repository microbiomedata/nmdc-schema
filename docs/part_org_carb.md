# Slot: particulate organic carbon (part_org_carb)


_Concentration of particulate organic carbon_



URI: [MIXS:0000515](https://w3id.org/mixs/0000515)




## Inheritance

* [core_field](core_field.md)
    * **part_org_carb**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* particulate organic carbon




## Examples

| Value |
| --- |
| 1.92 micromole per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | microgram per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: part_org_carb
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: microgram per liter
  occurrence:
    tag: occurrence
    value: '1'
description: Concentration of particulate organic carbon
title: particulate organic carbon
examples:
- value: 1.92 micromole per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- particulate organic carbon
rank: 1000
is_a: core field
slot_uri: MIXS:0000515
multivalued: false
alias: part_org_carb
domain_of:
- Biosample
range: QuantityValue

```
</details>