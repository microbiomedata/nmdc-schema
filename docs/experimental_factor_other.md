# Slot: experimental factor- other (experimental_factor_other)


_Other details about your sample that you feel can't be accurately represented in the available columns._



URI: [nmdc:experimental_factor_other](https://w3id.org/nmdc/experimental_factor_other)



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
| experimental treatment: value |

## Comments

* This slot accepts open-ended text about your sample.
* We recommend using key:value pairs.
* Provided pairs will be considered for inclusion as future slots/terms in this data collection template.

## See Also

* [MIXS:0000008](https://w3id.org/mixs/0000008)
* [MIXS:0000300](https://w3id.org/mixs/0000300)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: experimental_factor_other
description: Other details about your sample that you feel can't be accurately represented
  in the available columns.
title: experimental factor- other
comments:
- This slot accepts open-ended text about your sample.
- We recommend using key:value pairs.
- Provided pairs will be considered for inclusion as future slots/terms in this data
  collection template.
examples:
- value: 'experimental treatment: value'
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- MIXS:0000008
- MIXS:0000300
rank: 7
string_serialization: '{text}'
alias: experimental_factor_other
domain_of:
- Biosample
slot_group: MIxS Inspired
range: string
recommended: true

```
</details>