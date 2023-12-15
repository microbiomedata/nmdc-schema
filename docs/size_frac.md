# Slot: size fraction selected (size_frac)


_Filtering pore size used in sample preparation_



URI: [MIXS:0000017](https://w3id.org/mixs/0000017)




## Inheritance

* [nucleic_acid_sequence_source_field](nucleic_acid_sequence_source_field.md)
    * **size_frac**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* size fraction selected




## Examples

| Value |
| --- |
| 0-0.22 micrometer |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | filter size value range |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: size_frac
annotations:
  expected_value:
    tag: expected_value
    value: filter size value range
description: Filtering pore size used in sample preparation
title: size fraction selected
examples:
- value: 0-0.22 micrometer
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- size fraction selected
rank: 1000
is_a: nucleic acid sequence source field
string_serialization: '{float}-{float} {unit}'
slot_uri: MIXS:0000017
multivalued: false
alias: size_frac
domain_of:
- Biosample
range: TextValue

```
</details>