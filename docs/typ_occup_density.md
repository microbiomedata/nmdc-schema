# Slot: typical occupant density (typ_occup_density)


_Customary or normal density of occupants_



URI: [MIXS:0000771](https://w3id.org/mixs/0000771)




## Inheritance

* [core_field](core_field.md)
    * **typ_occup_density**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [Double](Double.md)



## Aliases


* typical occupant density




## Examples

| Value |
| --- |
| 25 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: typ_occup_density
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  occurrence:
    tag: occurrence
    value: '1'
description: Customary or normal density of occupants
title: typical occupant density
examples:
- value: '25'
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- typical occupant density
rank: 1000
is_a: core field
slot_uri: MIXS:0000771
multivalued: false
alias: typ_occup_density
domain_of:
- Biosample
range: double

```
</details>