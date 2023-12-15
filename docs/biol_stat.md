# Slot: biological status (biol_stat)


_The level of genome modification._



URI: [MIXS:0000858](https://w3id.org/mixs/0000858)




## Inheritance

* [core_field](core_field.md)
    * **biol_stat**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [BiolStatEnum](BiolStatEnum.md)



## Aliases


* biological status




## Examples

| Value |
| --- |
| natural |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | enumeration || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: biol_stat
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The level of genome modification.
title: biological status
examples:
- value: natural
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- biological status
rank: 1000
is_a: core field
slot_uri: MIXS:0000858
multivalued: false
alias: biol_stat
domain_of:
- Biosample
range: biol_stat_enum

```
</details>