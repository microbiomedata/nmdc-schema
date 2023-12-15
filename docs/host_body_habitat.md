# Slot: host body habitat (host_body_habitat)


_Original body habitat where the sample was obtained from_



URI: [MIXS:0000866](https://w3id.org/mixs/0000866)




## Inheritance

* [core_field](core_field.md)
    * **host_body_habitat**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* host body habitat




## Examples

| Value |
| --- |
| nasopharynx |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | free text || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: host_body_habitat
annotations:
  expected_value:
    tag: expected_value
    value: free text
  occurrence:
    tag: occurrence
    value: '1'
description: Original body habitat where the sample was obtained from
title: host body habitat
examples:
- value: nasopharynx
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- host body habitat
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000866
multivalued: false
alias: host_body_habitat
domain_of:
- Biosample
range: TextValue

```
</details>