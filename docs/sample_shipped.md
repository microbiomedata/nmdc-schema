# Slot: sample shipped amount (sample_shipped)


_The total amount or size (volume (ml), mass (g) or area (m2) ) of sample sent to EMSL._



URI: [nmdc:sample_shipped](https://w3id.org/nmdc/sample_shipped)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [String](String.md)

* Recommended: True






## Examples

| Value |
| --- |
| 15 g |
| 100 uL |
| 5 mL |

## Comments

* This field is only required when completing metadata for samples being submitted to EMSL for analyses.

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: sample_shipped
description: The total amount or size (volume (ml), mass (g) or area (m2) ) of sample
  sent to EMSL.
title: sample shipped amount
comments:
- This field is only required when completing metadata for samples being submitted
  to EMSL for analyses.
examples:
- value: 15 g
- value: 100 uL
- value: 5 mL
from_schema: https://w3id.org/nmdc/nmdc
rank: 3
string_serialization: '{float} {unit}'
alias: sample_shipped
domain_of:
- Biosample
slot_group: EMSL
range: string
recommended: true

```
</details>