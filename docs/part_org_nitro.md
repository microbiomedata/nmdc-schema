# Slot: particulate organic nitrogen (part_org_nitro)


_Concentration of particulate organic nitrogen_



URI: [MIXS:0000719](https://w3id.org/mixs/0000719)




## Inheritance

* [core_field](core_field.md)
    * **part_org_nitro**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* particulate organic nitrogen




## Examples

| Value |
| --- |
| 0.3 micromole per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | microgram per liter, micromole per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: part_org_nitro
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: microgram per liter, micromole per liter
  occurrence:
    tag: occurrence
    value: '1'
description: Concentration of particulate organic nitrogen
title: particulate organic nitrogen
examples:
- value: 0.3 micromole per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- particulate organic nitrogen
rank: 1000
is_a: core field
slot_uri: MIXS:0000719
multivalued: false
alias: part_org_nitro
domain_of:
- Biosample
range: QuantityValue

```
</details>