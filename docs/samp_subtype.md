# Slot: sample subtype (samp_subtype)


_Name of sample sub-type. For example if "sample type" is "Produced Water" then subtype could be "Oil Phase" or "Water Phase". If "other" is specified, please propose entry in "additional info" field_



URI: [MIXS:0000999](https://w3id.org/mixs/0000999)




## Inheritance

* [core_field](core_field.md)
    * **samp_subtype**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [SampSubtypeEnum](SampSubtypeEnum.md)



## Aliases


* sample subtype




## Examples

| Value |
| --- |
| biofilm |

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
name: samp_subtype
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: Name of sample sub-type. For example if "sample type" is "Produced Water"
  then subtype could be "Oil Phase" or "Water Phase". If "other" is specified, please
  propose entry in "additional info" field
title: sample subtype
examples:
- value: biofilm
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- sample subtype
rank: 1000
is_a: core field
slot_uri: MIXS:0000999
multivalued: false
alias: samp_subtype
domain_of:
- Biosample
range: samp_subtype_enum

```
</details>