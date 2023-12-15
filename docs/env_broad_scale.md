# Slot: broad-scale environmental context (env_broad_scale)


_Report the major environmental system the sample or specimen came from. The system(s) identified should have a coarse spatial grain, to provide the general environmental context of where the sampling was done (e.g. in the desert or a rainforest). We recommend using subclasses of EnvO’s biome class:  http://purl.obolibrary.org/obo/ENVO_00000428. EnvO documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS_



URI: [MIXS:0000012](https://w3id.org/mixs/0000012)




## Inheritance

* [environment_field](environment_field.md)
    * **env_broad_scale**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [ControlledIdentifiedTermValue](ControlledIdentifiedTermValue.md)



## Aliases


* broad-scale environmental context




## Examples

| Value |
| --- |
| oceanic epipelagic zone biome [ENVO:01000033] for annotating a water sample from the photic zone in middle of the Atlantic Ocean |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | The major environment type(s) where the sample was collected. Recommend subclasses of biome [ENVO:00000428]. Multiple terms can be separated by one or more pipes. |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: env_broad_scale
annotations:
  expected_value:
    tag: expected_value
    value: The major environment type(s) where the sample was collected. Recommend
      subclasses of biome [ENVO:00000428]. Multiple terms can be separated by one
      or more pipes.
description: 'Report the major environmental system the sample or specimen came from.
  The system(s) identified should have a coarse spatial grain, to provide the general
  environmental context of where the sampling was done (e.g. in the desert or a rainforest).
  We recommend using subclasses of EnvO’s biome class:  http://purl.obolibrary.org/obo/ENVO_00000428.
  EnvO documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS'
title: broad-scale environmental context
examples:
- value: oceanic epipelagic zone biome [ENVO:01000033] for annotating a water sample
    from the photic zone in middle of the Atlantic Ocean
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- broad-scale environmental context
rank: 1000
is_a: environment field
string_serialization: '{termLabel} {[termID]}'
slot_uri: MIXS:0000012
multivalued: false
alias: env_broad_scale
domain_of:
- Biosample
range: ControlledIdentifiedTermValue

```
</details>