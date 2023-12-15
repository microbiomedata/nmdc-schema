# Slot: IGSN Biosample Identifiers (igsn_biosample_identifiers)


_A list of identifiers for the biosample from the IGSN database._



URI: [nmdc:igsn_biosample_identifiers](https://w3id.org/nmdc/igsn_biosample_identifiers)




## Inheritance

* [alternative_identifiers](alternative_identifiers.md)
    * [external_database_identifiers](external_database_identifiers.md)
        * [biosample_identifiers](biosample_identifiers.md)
            * **igsn_biosample_identifiers** [ [igsn_identifiers](igsn_identifiers.md)]





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [ExternalIdentifier](ExternalIdentifier.md)

* Multivalued: True

* Regex pattern: `^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: igsn_biosample_identifiers
description: A list of identifiers for the biosample from the IGSN database.
title: IGSN Biosample Identifiers
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
is_a: biosample_identifiers
mixins:
- igsn_identifiers
multivalued: true
alias: igsn_biosample_identifiers
domain_of:
- Biosample
range: external_identifier
pattern: ^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$

```
</details>