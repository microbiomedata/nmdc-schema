# Slot: viscosity (viscosity)


_A measure of oil's resistance¬†to gradual deformation by¬†shear stress¬†or¬†tensile stress (e.g. 3.5 cp; 100 ¬∞C)_



URI: [MIXS:0000126](https://w3id.org/mixs/0000126)




## Inheritance

* [core_field](core_field.md)
    * **viscosity**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* viscosity




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value;measurement value || preferred_unit | cP at degree Celsius || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: viscosity
annotations:
  expected_value:
    tag: expected_value
    value: measurement value;measurement value
  preferred_unit:
    tag: preferred_unit
    value: cP at degree Celsius
  occurrence:
    tag: occurrence
    value: '1'
description: A measure of oil's resistance¬†to gradual deformation by¬†shear stress¬†or¬†tensile
  stress (e.g. 3.5 cp; 100 ¬∞C)
title: viscosity
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- viscosity
rank: 1000
is_a: core field
string_serialization: '{float} {unit};{float} {unit}'
slot_uri: MIXS:0000126
multivalued: false
alias: viscosity
domain_of:
- Biosample
range: TextValue

```
</details>