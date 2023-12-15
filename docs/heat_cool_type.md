# Slot: heating and cooling system type (heat_cool_type)


_Methods of conditioning or heating a room or building_



URI: [MIXS:0000766](https://w3id.org/mixs/0000766)




## Inheritance

* [core_field](core_field.md)
    * **heat_cool_type**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [HeatCoolTypeEnum](HeatCoolTypeEnum.md)

* Multivalued: True



## Aliases


* heating and cooling system type




## Examples

| Value |
| --- |
| heat pump |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | enumeration || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: heat_cool_type
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: m
description: Methods of conditioning or heating a room or building
title: heating and cooling system type
examples:
- value: heat pump
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- heating and cooling system type
rank: 1000
is_a: core field
slot_uri: MIXS:0000766
multivalued: true
alias: heat_cool_type
domain_of:
- Biosample
range: heat_cool_type_enum

```
</details>