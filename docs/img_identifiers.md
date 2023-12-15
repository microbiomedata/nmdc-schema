# Slot: IMG Identifiers (img_identifiers)


_A list of identifiers that relate the biosample to records in the IMG database._



URI: [nmdc:img_identifiers](https://w3id.org/nmdc/img_identifiers)




## Inheritance

* [alternative_identifiers](alternative_identifiers.md)
    * [external_database_identifiers](external_database_identifiers.md)
        * **img_identifiers**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [ExternalIdentifier](ExternalIdentifier.md)

* Multivalued: True

* Regex pattern: `^img\.taxon:[a-zA-Z0-9_][a-zA-Z0-9_\/\.]*$`





## TODOs

* add is_a or mixin modeling, like other external_database_identifiers
* what class would IMG records belong to?! Are they Studies, Biosamples, or something else?

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: img_identifiers
description: A list of identifiers that relate the biosample to records in the IMG
  database.
title: IMG Identifiers
todos:
- add is_a or mixin modeling, like other external_database_identifiers
- what class would IMG records belong to?! Are they Studies, Biosamples, or something
  else?
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
is_a: external_database_identifiers
multivalued: true
alias: img_identifiers
domain_of:
- Biosample
range: external_identifier
pattern: ^img\.taxon:[a-zA-Z0-9_][a-zA-Z0-9_\/\.]*$

```
</details>