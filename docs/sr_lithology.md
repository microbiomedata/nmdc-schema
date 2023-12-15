# Slot: source rock lithology (sr_lithology)


_Lithology of source rock (https://en.wikipedia.org/wiki/Source_rock). If "other" is specified, please propose entry in "additional info" field_



URI: [MIXS:0000995](https://w3id.org/mixs/0000995)




## Inheritance

* [core_field](core_field.md)
    * **sr_lithology**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [SrLithologyEnum](SrLithologyEnum.md)



## Aliases


* source rock lithology




## Examples

| Value |
| --- |
| Coal |

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
name: sr_lithology
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: Lithology of source rock (https://en.wikipedia.org/wiki/Source_rock).
  If "other" is specified, please propose entry in "additional info" field
title: source rock lithology
examples:
- value: Coal
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- source rock lithology
rank: 1000
is_a: core field
slot_uri: MIXS:0000995
multivalued: false
alias: sr_lithology
domain_of:
- Biosample
range: sr_lithology_enum

```
</details>