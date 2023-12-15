# Slot: pcr conditions (pcr_cond)


_Description of reaction conditions and components of PCR in the form of 'initial denaturation:94degC_1.5min; annealing=...'_



URI: [MIXS:0000049](https://w3id.org/mixs/0000049)




## Inheritance

* [sequencing_field](sequencing_field.md)
    * **pcr_cond**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |
[OmicsProcessing](OmicsProcessing.md) | The methods and processes used to generate omics data from a biosample or org... |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* pcr conditions




## Examples

| Value |
| --- |
| initial denaturation:94_3;annealing:50_1;elongation:72_1.5;final elongation:72_10;35 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | initial denaturation:degrees_minutes;annealing:degrees_minutes;elongation:degrees_minutes;final elongation:degrees_minutes;total cycles |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: pcr_cond
annotations:
  expected_value:
    tag: expected_value
    value: initial denaturation:degrees_minutes;annealing:degrees_minutes;elongation:degrees_minutes;final
      elongation:degrees_minutes;total cycles
description: Description of reaction conditions and components of PCR in the form
  of 'initial denaturation:94degC_1.5min; annealing=...'
title: pcr conditions
examples:
- value: initial denaturation:94_3;annealing:50_1;elongation:72_1.5;final elongation:72_10;35
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- pcr conditions
rank: 1000
is_a: sequencing field
string_serialization: initial denaturation:degrees_minutes;annealing:degrees_minutes;elongation:degrees_minutes;final
  elongation:degrees_minutes;total cycles
slot_uri: MIXS:0000049
multivalued: false
alias: pcr_cond
domain_of:
- Biosample
- OmicsProcessing
range: TextValue

```
</details>