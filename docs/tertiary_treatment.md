# Slot: tertiary treatment (tertiary_treatment)


_The process providing a final treatment stage to raise the effluent quality before it is discharged to the receiving environment_



URI: [MIXS:0000352](https://w3id.org/mixs/0000352)




## Inheritance

* [core_field](core_field.md)
    * **tertiary_treatment**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* tertiary treatment




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | tertiary treatment type || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: tertiary_treatment
annotations:
  expected_value:
    tag: expected_value
    value: tertiary treatment type
  occurrence:
    tag: occurrence
    value: '1'
description: The process providing a final treatment stage to raise the effluent quality
  before it is discharged to the receiving environment
title: tertiary treatment
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- tertiary treatment
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000352
multivalued: false
alias: tertiary_treatment
domain_of:
- Biosample
range: TextValue

```
</details>