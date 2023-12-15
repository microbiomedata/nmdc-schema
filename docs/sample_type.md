# Slot: sample type (sample_type)


_Type of sample being submitted_



URI: [nmdc:sample_type](https://w3id.org/nmdc/sample_type)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [SampleTypeEnum](SampleTypeEnum.md)

* Recommended: True






## Examples

| Value |
| --- |
| water extracted soil |

## Comments

* This can vary from 'environmental package' if the sample is an extraction.

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: sample_type
description: Type of sample being submitted
title: sample type
comments:
- This can vary from 'environmental package' if the sample is an extraction.
examples:
- value: water extracted soil
from_schema: https://w3id.org/nmdc/nmdc
rank: 2
alias: sample_type
domain_of:
- Biosample
slot_group: EMSL
range: sample_type_enum
recommended: true

```
</details>