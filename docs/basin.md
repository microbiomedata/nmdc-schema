# Slot: basin name (basin)


_Name of the basin (e.g. Campos)_



URI: [MIXS:0000290](https://w3id.org/mixs/0000290)




## Inheritance

* [core_field](core_field.md)
    * **basin**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* basin name




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | name || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: basin
annotations:
  expected_value:
    tag: expected_value
    value: name
  occurrence:
    tag: occurrence
    value: '1'
description: Name of the basin (e.g. Campos)
title: basin name
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- basin name
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000290
multivalued: false
alias: basin
domain_of:
- Biosample
range: TextValue

```
</details>