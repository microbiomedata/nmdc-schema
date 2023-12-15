# Slot: window covering (window_cover)


_The type of window covering_



URI: [MIXS:0000850](https://w3id.org/mixs/0000850)




## Inheritance

* [core_field](core_field.md)
    * **window_cover**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [WindowCoverEnum](WindowCoverEnum.md)



## Aliases


* window covering




## Examples

| Value |
| --- |
| curtains |

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
name: window_cover
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The type of window covering
title: window covering
examples:
- value: curtains
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- window covering
rank: 1000
is_a: core field
slot_uri: MIXS:0000850
multivalued: false
alias: window_cover
domain_of:
- Biosample
range: window_cover_enum

```
</details>