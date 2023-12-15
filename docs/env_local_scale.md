# Slot: local environmental context (env_local_scale)


_Report the entity or entities which are in the sample or specimen’s local vicinity and which you believe have significant causal influences on your sample or specimen. We recommend using EnvO terms which are of smaller spatial grain than your entry for env_broad_scale. Terms, such as anatomical sites, from other OBO Library ontologies which interoperate with EnvO (e.g. UBERON) are accepted in this field. EnvO documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS._



URI: [MIXS:0000013](https://w3id.org/mixs/0000013)




## Inheritance

* [environment_field](environment_field.md)
    * **env_local_scale**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [ControlledIdentifiedTermValue](ControlledIdentifiedTermValue.md)



## Aliases


* local environmental context




## Examples

| Value |
| --- |
| litter layer [ENVO:01000338]; Annotating a pooled sample taken from various vegetation layers in a forest consider: canopy [ENVO:00000047]|herb and fern layer [ENVO:01000337]|litter layer [ENVO:01000338]|understory [01000335]|shrub layer [ENVO:01000336]. |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | Environmental entities having causal influences upon the entity at time of sampling. |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: env_local_scale
annotations:
  expected_value:
    tag: expected_value
    value: Environmental entities having causal influences upon the entity at time
      of sampling.
description: 'Report the entity or entities which are in the sample or specimen’s
  local vicinity and which you believe have significant causal influences on your
  sample or specimen. We recommend using EnvO terms which are of smaller spatial grain
  than your entry for env_broad_scale. Terms, such as anatomical sites, from other
  OBO Library ontologies which interoperate with EnvO (e.g. UBERON) are accepted in
  this field. EnvO documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS.'
title: local environmental context
examples:
- value: 'litter layer [ENVO:01000338]; Annotating a pooled sample taken from various
    vegetation layers in a forest consider: canopy [ENVO:00000047]|herb and fern layer
    [ENVO:01000337]|litter layer [ENVO:01000338]|understory [01000335]|shrub layer
    [ENVO:01000336].'
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- local environmental context
rank: 1000
is_a: environment field
string_serialization: '{termLabel} {[termID]}'
slot_uri: MIXS:0000013
multivalued: false
alias: env_local_scale
domain_of:
- Biosample
range: ControlledIdentifiedTermValue

```
</details>