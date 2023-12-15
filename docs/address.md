# Slot: address (address)


_The street name and building number where the sampling occurred._



URI: [MIXS:0000218](https://w3id.org/mixs/0000218)




## Inheritance

* [core_field](core_field.md)
    * **address**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* address




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
name: address
annotations:
  expected_value:
    tag: expected_value
    value: value
  occurrence:
    tag: occurrence
    value: '1'
description: The street name and building number where the sampling occurred.
title: address
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- address
rank: 1000
is_a: core field
string_serialization: '{integer}{text}'
slot_uri: MIXS:0000218
multivalued: false
alias: address
domain_of:
- Biosample
range: TextValue

```
</details>