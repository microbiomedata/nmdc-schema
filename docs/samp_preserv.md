# Slot: preservative added to sample (samp_preserv)


_Preservative added to the sample (e.g. Rnalater, alcohol, formaldehyde, etc.). Where appropriate include volume added (e.g. Rnalater; 2 ml)_



URI: [MIXS:0000463](https://w3id.org/mixs/0000463)




## Inheritance

* [core_field](core_field.md)
    * **samp_preserv**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* preservative added to sample




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | name;measurement value || preferred_unit | milliliter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: samp_preserv
annotations:
  expected_value:
    tag: expected_value
    value: name;measurement value
  preferred_unit:
    tag: preferred_unit
    value: milliliter
  occurrence:
    tag: occurrence
    value: '1'
description: Preservative added to the sample (e.g. Rnalater, alcohol, formaldehyde,
  etc.). Where appropriate include volume added (e.g. Rnalater; 2 ml)
title: preservative added to sample
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- preservative added to sample
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000463
multivalued: false
alias: samp_preserv
domain_of:
- Biosample
range: TextValue

```
</details>