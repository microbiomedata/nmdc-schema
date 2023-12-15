# Slot: biocide administration (biocide)


_List of biocides (commercial name of product and supplier) and date of administration_



URI: [MIXS:0001011](https://w3id.org/mixs/0001011)




## Inheritance

* [core_field](core_field.md)
    * **biocide**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* biocide administration




## Examples

| Value |
| --- |
| ALPHA 1427;Baker Hughes;2008-01-23 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | name;name;timestamp || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: biocide
annotations:
  expected_value:
    tag: expected_value
    value: name;name;timestamp
  occurrence:
    tag: occurrence
    value: '1'
description: List of biocides (commercial name of product and supplier) and date of
  administration
title: biocide administration
examples:
- value: ALPHA 1427;Baker Hughes;2008-01-23
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- biocide administration
rank: 1000
is_a: core field
string_serialization: '{text};{text};{timestamp}'
slot_uri: MIXS:0001011
multivalued: false
alias: biocide
domain_of:
- Biosample
range: TextValue

```
</details>