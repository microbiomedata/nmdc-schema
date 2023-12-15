# Slot: genetic modification (genetic_mod)


_Genetic modifications of the genome of an organism, which may occur naturally by spontaneous mutation, or be introduced by some experimental means, e.g. specification of a transgene or the gene knocked-out or details of transient transfection_



URI: [MIXS:0000859](https://w3id.org/mixs/0000859)




## Inheritance

* [core_field](core_field.md)
    * **genetic_mod**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* genetic modification




## Examples

| Value |
| --- |
| aox1A transgenic |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | PMID,DOI,url or free text || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: genetic_mod
annotations:
  expected_value:
    tag: expected_value
    value: PMID,DOI,url or free text
  occurrence:
    tag: occurrence
    value: '1'
description: Genetic modifications of the genome of an organism, which may occur naturally
  by spontaneous mutation, or be introduced by some experimental means, e.g. specification
  of a transgene or the gene knocked-out or details of transient transfection
title: genetic modification
examples:
- value: aox1A transgenic
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- genetic modification
rank: 1000
is_a: core field
string_serialization: '{PMID}|{DOI}|{URL}|{text}'
slot_uri: MIXS:0000859
multivalued: false
alias: genetic_mod
domain_of:
- Biosample
range: TextValue

```
</details>