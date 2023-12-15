# Slot: season (season)


_The season when sampling occurred. Any of the four periods into which the year is divided by the equinoxes and solstices. This field accepts terms listed under season (http://purl.obolibrary.org/obo/NCIT_C94729)._



URI: [MIXS:0000829](https://w3id.org/mixs/0000829)




## Inheritance

* [core_field](core_field.md)
    * **season**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* season




## Examples

| Value |
| --- |
| autumn [NCIT:C94733] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | NCIT:C94729 || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: season
annotations:
  expected_value:
    tag: expected_value
    value: NCIT:C94729
  occurrence:
    tag: occurrence
    value: '1'
description: The season when sampling occurred. Any of the four periods into which
  the year is divided by the equinoxes and solstices. This field accepts terms listed
  under season (http://purl.obolibrary.org/obo/NCIT_C94729).
title: season
examples:
- value: autumn [NCIT:C94733]
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- season
rank: 1000
is_a: core field
string_serialization: '{termLabel} {[termID]}'
slot_uri: MIXS:0000829
multivalued: false
alias: season
domain_of:
- Biosample
range: TextValue

```
</details>