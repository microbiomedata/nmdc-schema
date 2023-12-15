# Slot: culture rooting medium (cult_root_med)


_Name or reference for the hydroponic or in vitro culture rooting medium; can be the name of a commonly used medium or reference to a specific medium, e.g. Murashige and Skoog medium. If the medium has not been formally published, use the rooting medium descriptors._



URI: [MIXS:0001041](https://w3id.org/mixs/0001041)




## Inheritance

* [core_field](core_field.md)
    * **cult_root_med**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* culture rooting medium




## Examples

| Value |
| --- |
| http://himedialabs.com/TD/PT158.pdf |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | name, PMID,DOI or url || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: cult_root_med
annotations:
  expected_value:
    tag: expected_value
    value: name, PMID,DOI or url
  occurrence:
    tag: occurrence
    value: '1'
description: Name or reference for the hydroponic or in vitro culture rooting medium;
  can be the name of a commonly used medium or reference to a specific medium, e.g.
  Murashige and Skoog medium. If the medium has not been formally published, use the
  rooting medium descriptors.
title: culture rooting medium
examples:
- value: http://himedialabs.com/TD/PT158.pdf
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- culture rooting medium
rank: 1000
is_a: core field
string_serialization: '{text}|{PMID}|{DOI}|{URL}'
slot_uri: MIXS:0001041
multivalued: false
alias: cult_root_med
domain_of:
- Biosample
range: TextValue

```
</details>