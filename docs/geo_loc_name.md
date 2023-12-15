# Slot: geographic location (country and/or sea,region) (geo_loc_name)


_The geographical origin of the sample as defined by the country or sea name followed by specific region name. Country or sea names should be chosen from the INSDC country list (http://insdc.org/country.html), or the GAZ ontology (http://purl.bioontology.org/ontology/GAZ)_



URI: [MIXS:0000010](https://w3id.org/mixs/0000010)




## Inheritance

* [environment_field](environment_field.md)
    * **geo_loc_name**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FieldResearchSite](FieldResearchSite.md) | A site, outside of a laboratory, from which biosamples may be collected |  no  |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* geographic location (country and/or sea,region)




## Examples

| Value |
| --- |
| USA: Maryland, Bethesda |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | country or sea name (INSDC or GAZ): region(GAZ), specific location name |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: geo_loc_name
annotations:
  expected_value:
    tag: expected_value
    value: 'country or sea name (INSDC or GAZ): region(GAZ), specific location name'
description: The geographical origin of the sample as defined by the country or sea
  name followed by specific region name. Country or sea names should be chosen from
  the INSDC country list (http://insdc.org/country.html), or the GAZ ontology (http://purl.bioontology.org/ontology/GAZ)
title: geographic location (country and/or sea,region)
examples:
- value: 'USA: Maryland, Bethesda'
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- geographic location (country and/or sea,region)
rank: 1000
is_a: environment field
string_serialization: '{term}: {term}, {text}'
slot_uri: MIXS:0000010
multivalued: false
alias: geo_loc_name
domain_of:
- FieldResearchSite
- Biosample
range: TextValue

```
</details>