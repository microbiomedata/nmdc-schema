# Slot: sample size sorting method (samp_sort_meth)


_Method by which samples are sorted; open face filter collecting total suspended particles, prefilter to remove particles larger than X micrometers in diameter, where common values of X would be 10 and 2.5 full size sorting in a cascade impactor._



URI: [MIXS:0000216](https://w3id.org/mixs/0000216)




## Inheritance

* [core_field](core_field.md)
    * **samp_sort_meth**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* sample size sorting method




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | description of method || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: samp_sort_meth
annotations:
  expected_value:
    tag: expected_value
    value: description of method
  occurrence:
    tag: occurrence
    value: m
description: Method by which samples are sorted; open face filter collecting total
  suspended particles, prefilter to remove particles larger than X micrometers in
  diameter, where common values of X would be 10 and 2.5 full size sorting in a cascade
  impactor.
title: sample size sorting method
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- sample size sorting method
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000216
multivalued: true
alias: samp_sort_meth
domain_of:
- Biosample
range: TextValue

```
</details>