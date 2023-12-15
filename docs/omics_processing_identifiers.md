# Slot: omics_processing_identifiers

URI: [nmdc:omics_processing_identifiers](https://w3id.org/nmdc/omics_processing_identifiers)




## Inheritance

* [alternative_identifiers](alternative_identifiers.md)
    * [external_database_identifiers](external_database_identifiers.md)
        * **omics_processing_identifiers**
            * [gold_sequencing_project_identifiers](gold_sequencing_project_identifiers.md) [ [gold_identifiers](gold_identifiers.md)]








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
name: omics_processing_identifiers
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
is_a: external_database_identifiers
abstract: true
multivalued: true
alias: omics_processing_identifiers
range: external_identifier
pattern: ^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$

```
</details>