# Slot: host diet (host_diet)


_Type of diet depending on the host, for animals omnivore, herbivore etc., for humans high-fat, meditteranean etc.; can include multiple diet types_



URI: [MIXS:0000869](https://w3id.org/mixs/0000869)




## Inheritance

* [core_field](core_field.md)
    * **host_diet**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* host diet




## Examples

| Value |
| --- |
| herbivore |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | diet type || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: host_diet
annotations:
  expected_value:
    tag: expected_value
    value: diet type
  occurrence:
    tag: occurrence
    value: m
description: Type of diet depending on the host, for animals omnivore, herbivore etc.,
  for humans high-fat, meditteranean etc.; can include multiple diet types
title: host diet
examples:
- value: herbivore
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- host diet
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000869
multivalued: true
alias: host_diet
domain_of:
- Biosample
range: TextValue

```
</details>