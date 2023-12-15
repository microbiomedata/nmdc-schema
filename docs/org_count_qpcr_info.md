# Slot: organism count qPCR information (org_count_qpcr_info)


_If qpcr was used for the cell count, the target gene name, the primer sequence and the cycling conditions should also be provided. (Example: 16S rrna; FWD:ACGTAGCTATGACGT REV:GTGCTAGTCGAGTAC; initial denaturation:90C_5min; denaturation:90C_2min; annealing:52C_30 sec; elongation:72C_30 sec; 90 C for 1 min; final elongation:72C_5min; 30 cycles)_



URI: [MIXS:0000099](https://w3id.org/mixs/0000099)




## Inheritance

* [core_field](core_field.md)
    * **org_count_qpcr_info**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [String](String.md)



## Aliases


* organism count qPCR information




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | gene name;FWD:forward primer sequence;REV:reverse primer sequence;initial denaturation:degrees_minutes;denaturation:degrees_minutes;annealing:degrees_minutes;elongation:degrees_minutes;final elongation:degrees_minutes; total cycles || preferred_unit | number of cells per gram (or ml or cm^2) || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: org_count_qpcr_info
annotations:
  expected_value:
    tag: expected_value
    value: gene name;FWD:forward primer sequence;REV:reverse primer sequence;initial
      denaturation:degrees_minutes;denaturation:degrees_minutes;annealing:degrees_minutes;elongation:degrees_minutes;final
      elongation:degrees_minutes; total cycles
  preferred_unit:
    tag: preferred_unit
    value: number of cells per gram (or ml or cm^2)
  occurrence:
    tag: occurrence
    value: '1'
description: 'If qpcr was used for the cell count, the target gene name, the primer
  sequence and the cycling conditions should also be provided. (Example: 16S rrna;
  FWD:ACGTAGCTATGACGT REV:GTGCTAGTCGAGTAC; initial denaturation:90C_5min; denaturation:90C_2min;
  annealing:52C_30 sec; elongation:72C_30 sec; 90 C for 1 min; final elongation:72C_5min;
  30 cycles)'
title: organism count qPCR information
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- organism count qPCR information
rank: 1000
is_a: core field
string_serialization: '{text};FWD:{dna};REV:{dna};initial denaturation:degrees_minutes;denaturation:degrees_minutes;annealing:degrees_minutes;elongation:degrees_minutes;final
  elongation:degrees_minutes; total cycles'
slot_uri: MIXS:0000099
multivalued: false
alias: org_count_qpcr_info
domain_of:
- Biosample
range: string

```
</details>