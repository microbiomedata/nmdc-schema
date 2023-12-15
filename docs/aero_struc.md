# Slot: aerospace structure (aero_struc)


_Aerospace structures typically consist of thin plates with stiffeners for the external surfaces, bulkheads and frames to support the shape and fasteners such as welds, rivets, screws and bolts to hold the components together_



URI: [MIXS:0000773](https://w3id.org/mixs/0000773)




## Inheritance

* [core_field](core_field.md)
    * **aero_struc**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* aerospace structure




## Examples

| Value |
| --- |
| plane |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | enumeration || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: aero_struc
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: Aerospace structures typically consist of thin plates with stiffeners
  for the external surfaces, bulkheads and frames to support the shape and fasteners
  such as welds, rivets, screws and bolts to hold the components together
title: aerospace structure
examples:
- value: plane
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- aerospace structure
rank: 1000
is_a: core field
string_serialization: '[plane|glider]'
slot_uri: MIXS:0000773
multivalued: false
alias: aero_struc
domain_of:
- Biosample
range: TextValue

```
</details>