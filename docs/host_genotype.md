# Slot: host genotype (host_genotype)


_Observed genotype_



URI: [MIXS:0000365](https://w3id.org/mixs/0000365)




## Inheritance

* [core_field](core_field.md)
    * **host_genotype**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* host genotype




## Examples

| Value |
| --- |
| C57BL/6 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | genotype || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: host_genotype
annotations:
  expected_value:
    tag: expected_value
    value: genotype
  occurrence:
    tag: occurrence
    value: '1'
description: Observed genotype
title: host genotype
examples:
- value: C57BL/6
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- host genotype
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000365
multivalued: false
alias: host_genotype
domain_of:
- Biosample
range: TextValue

```
</details>