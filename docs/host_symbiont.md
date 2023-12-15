# Slot: observed host symbionts (host_symbiont)


_The taxonomic name of the organism(s) found living in mutualistic, commensalistic, or parasitic symbiosis with the specific host._



URI: [MIXS:0001298](https://w3id.org/mixs/0001298)




## Inheritance

* [core_field](core_field.md)
    * **host_symbiont**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True



## Aliases


* observed host symbionts




## Examples

| Value |
| --- |
| flukeworms |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | species name or common name || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: host_symbiont
annotations:
  expected_value:
    tag: expected_value
    value: species name or common name
  occurrence:
    tag: occurrence
    value: m
description: The taxonomic name of the organism(s) found living in mutualistic, commensalistic,
  or parasitic symbiosis with the specific host.
title: observed host symbionts
examples:
- value: flukeworms
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- observed host symbionts
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0001298
multivalued: true
alias: host_symbiont
domain_of:
- Biosample
range: string

```
</details>