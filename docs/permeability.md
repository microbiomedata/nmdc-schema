# Slot: permeability (permeability)


_Measure of the ability of a hydrocarbon resource to allow fluids to pass through it. (Additional information: https://en.wikipedia.org/wiki/Permeability_(earth_sciences))_



URI: [MIXS:0000404](https://w3id.org/mixs/0000404)




## Inheritance

* [core_field](core_field.md)
    * **permeability**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* permeability




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value range || preferred_unit | mD || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: permeability
annotations:
  expected_value:
    tag: expected_value
    value: measurement value range
  preferred_unit:
    tag: preferred_unit
    value: mD
  occurrence:
    tag: occurrence
    value: '1'
description: 'Measure of the ability of a hydrocarbon resource to allow fluids to
  pass through it. (Additional information: https://en.wikipedia.org/wiki/Permeability_(earth_sciences))'
title: permeability
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- permeability
rank: 1000
is_a: core field
string_serialization: '{integer} - {integer} {unit}'
slot_uri: MIXS:0000404
multivalued: false
alias: permeability
domain_of:
- Biosample
range: TextValue

```
</details>