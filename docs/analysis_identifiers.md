# Slot: analysis_identifiers

URI: [nmdc:analysis_identifiers](https://w3id.org/nmdc/analysis_identifiers)




## Inheritance

* [alternative_identifiers](alternative_identifiers.md)
    * [external_database_identifiers](external_database_identifiers.md)
        * **analysis_identifiers**
            * [gold_analysis_project_identifiers](gold_analysis_project_identifiers.md) [ [gold_identifiers](gold_identifiers.md)]
            * [insdc_analysis_identifiers](insdc_analysis_identifiers.md) [ [insdc_identifiers](insdc_identifiers.md)]
            * [mgnify_analysis_identifiers](mgnify_analysis_identifiers.md) [ [mgnify_identifiers](mgnify_identifiers.md)]








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
name: analysis_identifiers
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
is_a: external_database_identifiers
abstract: true
multivalued: true
alias: analysis_identifiers
range: external_identifier
pattern: ^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$

```
</details>