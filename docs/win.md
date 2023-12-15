# Slot: well identification number (win)


_A unique identifier of a well or wellbore. This is part of the Global Framework for Well Identification initiative which is compiled by the Professional Petroleum Data Management Association (PPDM) in an effort to improve well identification systems. (Supporting information: https://ppdm.org/ and http://dl.ppdm.org/dl/690)_



URI: [MIXS:0000297](https://w3id.org/mixs/0000297)




## Inheritance

* [core_field](core_field.md)
    * **win**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* well identification number




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | text || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: win
annotations:
  expected_value:
    tag: expected_value
    value: text
  occurrence:
    tag: occurrence
    value: '1'
description: 'A unique identifier of a well or wellbore. This is part of the Global
  Framework for Well Identification initiative which is compiled by the Professional
  Petroleum Data Management Association (PPDM) in an effort to improve well identification
  systems. (Supporting information: https://ppdm.org/ and http://dl.ppdm.org/dl/690)'
title: well identification number
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- well identification number
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000297
multivalued: false
alias: win
domain_of:
- Biosample
range: TextValue

```
</details>