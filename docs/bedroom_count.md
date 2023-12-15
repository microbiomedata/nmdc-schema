# Slot: bedroom count (bedroom_count)


_The number of bedrooms in the building_



URI: [MIXS:0000777](https://w3id.org/mixs/0000777)




## Inheritance

* [core_field](core_field.md)
    * **bedroom_count**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* bedroom count




## Examples

| Value |
| --- |
| 2 |

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
name: bedroom_count
annotations:
  expected_value:
    tag: expected_value
    value: value
  occurrence:
    tag: occurrence
    value: '1'
description: The number of bedrooms in the building
title: bedroom count
examples:
- value: '2'
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- bedroom count
rank: 1000
is_a: core field
slot_uri: MIXS:0000777
multivalued: false
alias: bedroom_count
domain_of:
- Biosample
range: TextValue

```
</details>