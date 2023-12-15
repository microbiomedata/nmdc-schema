# Slot: EMSL Biosample Identifiers (emsl_biosample_identifiers)


_A list of identifiers for the biosample from the EMSL database.  This is used to link the biosample, as modeled by NMDC, to the biosample in the planned EMSL NEXUS database._



URI: [nmdc:emsl_biosample_identifiers](https://w3id.org/nmdc/emsl_biosample_identifiers)




## Inheritance

* [alternative_identifiers](alternative_identifiers.md)
    * [external_database_identifiers](external_database_identifiers.md)
        * [biosample_identifiers](biosample_identifiers.md)
            * **emsl_biosample_identifiers** [ [emsl_identifiers](emsl_identifiers.md)]





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [ExternalIdentifier](ExternalIdentifier.md)

* Multivalued: True

* Regex pattern: `^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$`





## TODOs

* removed "planned" once NEXUS is online
* determine real expansion for emsl prefix

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: emsl_biosample_identifiers
description: A list of identifiers for the biosample from the EMSL database.  This
  is used to link the biosample, as modeled by NMDC, to the biosample in the planned
  EMSL NEXUS database.
title: EMSL Biosample Identifiers
todos:
- removed "planned" once NEXUS is online
- determine real expansion for emsl prefix
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
is_a: biosample_identifiers
mixins:
- emsl_identifiers
multivalued: true
alias: emsl_biosample_identifiers
domain_of:
- Biosample
range: external_identifier
pattern: ^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$

```
</details>