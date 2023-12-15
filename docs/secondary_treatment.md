# Slot: secondary treatment (secondary_treatment)


_The process for substantially degrading the biological content of the sewage_



URI: [MIXS:0000351](https://w3id.org/mixs/0000351)




## Inheritance

* [core_field](core_field.md)
    * **secondary_treatment**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* secondary treatment




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | secondary treatment type || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: secondary_treatment
annotations:
  expected_value:
    tag: expected_value
    value: secondary treatment type
  occurrence:
    tag: occurrence
    value: '1'
description: The process for substantially degrading the biological content of the
  sewage
title: secondary treatment
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- secondary treatment
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000351
multivalued: false
alias: secondary_treatment
domain_of:
- Biosample
range: TextValue

```
</details>