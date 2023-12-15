# Slot: pooling of DNA extracts (if done) (pool_dna_extracts)


_Indicate whether multiple DNA extractions were mixed. If the answer yes, the number of extracts that were pooled should be given_



URI: [MIXS:0000325](https://w3id.org/mixs/0000325)




## Inheritance

* [core_field](core_field.md)
    * **pool_dna_extracts**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* pooling of DNA extracts (if done)




## Examples

| Value |
| --- |
| yes;5 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | pooling status;number of pooled extracts || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: pool_dna_extracts
annotations:
  expected_value:
    tag: expected_value
    value: pooling status;number of pooled extracts
  occurrence:
    tag: occurrence
    value: '1'
description: Indicate whether multiple DNA extractions were mixed. If the answer yes,
  the number of extracts that were pooled should be given
title: pooling of DNA extracts (if done)
examples:
- value: yes;5
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- pooling of DNA extracts (if done)
rank: 1000
is_a: core field
string_serialization: '{boolean};{integer}'
slot_uri: MIXS:0000325
multivalued: false
alias: pool_dna_extracts
domain_of:
- Biosample
range: TextValue

```
</details>