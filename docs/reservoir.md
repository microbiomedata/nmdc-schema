# Slot: reservoir name (reservoir)


_Name of the reservoir (e.g. Carapebus)_



URI: [MIXS:0000303](https://w3id.org/mixs/0000303)




## Inheritance

* [core_field](core_field.md)
    * **reservoir**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* reservoir name




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
name: reservoir
annotations:
  expected_value:
    tag: expected_value
    value: name
  occurrence:
    tag: occurrence
    value: '1'
description: Name of the reservoir (e.g. Carapebus)
title: reservoir name
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- reservoir name
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000303
multivalued: false
alias: reservoir
domain_of:
- Biosample
range: TextValue

```
</details>