# Slot: soil type (soil_type)


_Description of the soil type or classification. This field accepts terms under soil (http://purl.obolibrary.org/obo/ENVO_00001998).  Multiple terms can be separated by pipes._



URI: [MIXS:0000332](https://w3id.org/mixs/0000332)




## Inheritance

* [core_field](core_field.md)
    * **soil_type**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FieldResearchSite](FieldResearchSite.md) | A site, outside of a laboratory, from which biosamples may be collected |  no  |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* soil type




## Examples

| Value |
| --- |
| plinthosol [ENVO:00002250] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | ENVO_00001998 || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: soil_type
annotations:
  expected_value:
    tag: expected_value
    value: ENVO_00001998
  occurrence:
    tag: occurrence
    value: '1'
description: Description of the soil type or classification. This field accepts terms
  under soil (http://purl.obolibrary.org/obo/ENVO_00001998).  Multiple terms can be
  separated by pipes.
title: soil type
examples:
- value: plinthosol [ENVO:00002250]
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- soil type
rank: 1000
is_a: core field
string_serialization: '{termLabel} {[termID]}'
slot_uri: MIXS:0000332
multivalued: false
alias: soil_type
domain_of:
- FieldResearchSite
- Biosample
range: TextValue

```
</details>