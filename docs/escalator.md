# Slot: escalator count (escalator)


_The number of escalators within the built structure_



URI: [MIXS:0000800](https://w3id.org/mixs/0000800)




## Inheritance

* [core_field](core_field.md)
    * **escalator**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* escalator count




## Examples

| Value |
| --- |
| 4 |

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
name: escalator
annotations:
  expected_value:
    tag: expected_value
    value: value
  occurrence:
    tag: occurrence
    value: '1'
description: The number of escalators within the built structure
title: escalator count
examples:
- value: '4'
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- escalator count
rank: 1000
is_a: core field
slot_uri: MIXS:0000800
multivalued: false
alias: escalator
domain_of:
- Biosample
range: TextValue

```
</details>