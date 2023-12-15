# Slot: tissue culture growth media (tiss_cult_growth_med)


_Description of plant tissue culture growth media used_



URI: [MIXS:0001070](https://w3id.org/mixs/0001070)




## Inheritance

* [core_field](core_field.md)
    * **tiss_cult_growth_med**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* tissue culture growth media




## Examples

| Value |
| --- |
| https://link.springer.com/content/pdf/10.1007/BF02796489.pdf |

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
name: tiss_cult_growth_med
annotations:
  expected_value:
    tag: expected_value
    value: PMID,DOI,url or free text
  occurrence:
    tag: occurrence
    value: '1'
description: Description of plant tissue culture growth media used
title: tissue culture growth media
examples:
- value: https://link.springer.com/content/pdf/10.1007/BF02796489.pdf
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- tissue culture growth media
rank: 1000
is_a: core field
string_serialization: '{PMID}|{DOI}|{URL}|{text}'
slot_uri: MIXS:0001070
multivalued: false
alias: tiss_cult_growth_med
domain_of:
- Biosample
range: TextValue

```
</details>