# Slot: heating system identifier (heat_system_id)


_The heating system identifier_



URI: [MIXS:0000833](https://w3id.org/mixs/0000833)




## Inheritance

* [core_field](core_field.md)
    * **heat_system_id**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* heating system identifier




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | unique identifier || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: heat_system_id
annotations:
  expected_value:
    tag: expected_value
    value: unique identifier
  occurrence:
    tag: occurrence
    value: '1'
description: The heating system identifier
title: heating system identifier
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- heating system identifier
rank: 1000
is_a: core field
slot_uri: MIXS:0000833
multivalued: false
alias: heat_system_id
domain_of:
- Biosample
range: TextValue

```
</details>