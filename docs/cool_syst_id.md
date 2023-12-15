# Slot: cooling system identifier (cool_syst_id)


_The cooling system identifier_



URI: [MIXS:0000785](https://w3id.org/mixs/0000785)




## Inheritance

* [core_field](core_field.md)
    * **cool_syst_id**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* cooling system identifier




## Examples

| Value |
| --- |
| 12345 |

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
name: cool_syst_id
annotations:
  expected_value:
    tag: expected_value
    value: unique identifier
  occurrence:
    tag: occurrence
    value: '1'
description: The cooling system identifier
title: cooling system identifier
examples:
- value: '12345'
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- cooling system identifier
rank: 1000
is_a: core field
slot_uri: MIXS:0000785
multivalued: false
alias: cool_syst_id
domain_of:
- Biosample
range: TextValue

```
</details>