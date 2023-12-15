# Slot: host substrate (host_substrate)


_The growth substrate of the host._



URI: [MIXS:0000252](https://w3id.org/mixs/0000252)




## Inheritance

* [core_field](core_field.md)
    * **host_substrate**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* host substrate




## Examples

| Value |
| --- |
| rock |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | substrate name || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: host_substrate
annotations:
  expected_value:
    tag: expected_value
    value: substrate name
  occurrence:
    tag: occurrence
    value: '1'
description: The growth substrate of the host.
title: host substrate
examples:
- value: rock
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- host substrate
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000252
multivalued: false
alias: host_substrate
domain_of:
- Biosample
range: TextValue

```
</details>