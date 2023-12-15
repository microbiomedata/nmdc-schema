# Slot: alkalinity method (alkalinity_method)


_Method used for alkalinity measurement_



URI: [MIXS:0000298](https://w3id.org/mixs/0000298)




## Inheritance

* [core_field](core_field.md)
    * **alkalinity_method**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* alkalinity method




## Examples

| Value |
| --- |
| titration |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | description of method || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: alkalinity_method
annotations:
  expected_value:
    tag: expected_value
    value: description of method
  occurrence:
    tag: occurrence
    value: '1'
description: Method used for alkalinity measurement
title: alkalinity method
examples:
- value: titration
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- alkalinity method
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000298
multivalued: false
alias: alkalinity_method
domain_of:
- Biosample
range: TextValue

```
</details>