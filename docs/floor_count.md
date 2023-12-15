# Slot: floor count (floor_count)


_The number of floors in the building, including basements and mechanical penthouse_



URI: [MIXS:0000225](https://w3id.org/mixs/0000225)




## Inheritance

* [core_field](core_field.md)
    * **floor_count**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* floor count




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
name: floor_count
annotations:
  expected_value:
    tag: expected_value
    value: value
  occurrence:
    tag: occurrence
    value: '1'
description: The number of floors in the building, including basements and mechanical
  penthouse
title: floor count
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- floor count
rank: 1000
is_a: core field
slot_uri: MIXS:0000225
multivalued: false
alias: floor_count
domain_of:
- Biosample
range: TextValue

```
</details>