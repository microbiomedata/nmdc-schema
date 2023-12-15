# Slot: sample material processing (samp_mat_process)


_A brief description of any processing applied to the sample during or after retrieving the sample from environment, or a link to the relevant protocol(s) performed._



URI: [MIXS:0000016](https://w3id.org/mixs/0000016)




## Inheritance

* [nucleic_acid_sequence_source_field](nucleic_acid_sequence_source_field.md)
    * **samp_mat_process**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [ControlledTermValue](ControlledTermValue.md)



## Aliases


* sample material processing




## Examples

| Value |
| --- |
| filtering of seawater, storing samples in ethanol |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | text |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: samp_mat_process
annotations:
  expected_value:
    tag: expected_value
    value: text
description: A brief description of any processing applied to the sample during or
  after retrieving the sample from environment, or a link to the relevant protocol(s)
  performed.
title: sample material processing
examples:
- value: filtering of seawater, storing samples in ethanol
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- sample material processing
rank: 1000
is_a: nucleic acid sequence source field
string_serialization: '{text}'
slot_uri: MIXS:0000016
multivalued: false
alias: samp_mat_process
domain_of:
- Biosample
range: ControlledTermValue

```
</details>