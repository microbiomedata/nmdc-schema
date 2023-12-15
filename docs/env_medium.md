# Slot: environmental medium (env_medium)


_Report the environmental material(s) immediately surrounding the sample or specimen at the time of sampling. We recommend using subclasses of 'environmental material' (http://purl.obolibrary.org/obo/ENVO_00010483). EnvO documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS . Terms from other OBO ontologies are permissible as long as they reference mass/volume nouns (e.g. air, water, blood) and not discrete, countable entities (e.g. a tree, a leaf, a table top)._



URI: [MIXS:0000014](https://w3id.org/mixs/0000014)




## Inheritance

* [environment_field](environment_field.md)
    * **env_medium**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [ControlledIdentifiedTermValue](ControlledIdentifiedTermValue.md)



## Aliases


* environmental medium




## Examples

| Value |
| --- |
| soil [ENVO:00001998]; Annotating a fish swimming in the upper 100 m of the Atlantic Ocean, consider: ocean water [ENVO:00002151]. Example: Annotating a duck on a pond consider: pond water [ENVO:00002228]|air [ENVO_00002005] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | The material displaced by the entity at time of sampling. Recommend subclasses of environmental material [ENVO:00010483]. |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: env_medium
annotations:
  expected_value:
    tag: expected_value
    value: The material displaced by the entity at time of sampling. Recommend subclasses
      of environmental material [ENVO:00010483].
description: 'Report the environmental material(s) immediately surrounding the sample
  or specimen at the time of sampling. We recommend using subclasses of ''environmental
  material'' (http://purl.obolibrary.org/obo/ENVO_00010483). EnvO documentation about
  how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS
  . Terms from other OBO ontologies are permissible as long as they reference mass/volume
  nouns (e.g. air, water, blood) and not discrete, countable entities (e.g. a tree,
  a leaf, a table top).'
title: environmental medium
examples:
- value: 'soil [ENVO:00001998]; Annotating a fish swimming in the upper 100 m of the
    Atlantic Ocean, consider: ocean water [ENVO:00002151]. Example: Annotating a duck
    on a pond consider: pond water [ENVO:00002228]|air [ENVO_00002005]'
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- environmental medium
rank: 1000
is_a: environment field
string_serialization: '{termLabel} {[termID]}'
slot_uri: MIXS:0000014
multivalued: false
alias: env_medium
domain_of:
- Biosample
range: ControlledIdentifiedTermValue

```
</details>