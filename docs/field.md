# Slot: field name (field)


_Name of the hydrocarbon field (e.g. Albacora)_



URI: [MIXS:0000291](https://w3id.org/mixs/0000291)




## Inheritance

* [core_field](core_field.md)
    * **field**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* field name




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
name: field
annotations:
  expected_value:
    tag: expected_value
    value: name
  occurrence:
    tag: occurrence
    value: '1'
description: Name of the hydrocarbon field (e.g. Albacora)
title: field name
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- field name
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000291
multivalued: false
alias: field
domain_of:
- Biosample
range: TextValue

```
</details>