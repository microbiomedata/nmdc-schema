# Slot: exterior door count (ext_door)


_The number of exterior doors in the built structure_



URI: [MIXS:0000170](https://w3id.org/mixs/0000170)




## Inheritance

* [core_field](core_field.md)
    * **ext_door**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* exterior door count




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | value || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: ext_door
annotations:
  expected_value:
    tag: expected_value
    value: value
  occurrence:
    tag: occurrence
    value: '1'
description: The number of exterior doors in the built structure
title: exterior door count
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- exterior door count
rank: 1000
is_a: core field
slot_uri: MIXS:0000170
multivalued: false
alias: ext_door
domain_of:
- Biosample
range: TextValue

```
</details>