# Slot: study_identifiers

URI: [nmdc:study_identifiers](https://w3id.org/nmdc/study_identifiers)




## Inheritance

* [alternative_identifiers](alternative_identifiers.md)
    * [external_database_identifiers](external_database_identifiers.md)
        * **study_identifiers**
            * [jgi_portal_study_identifiers](jgi_portal_study_identifiers.md) [ [jgi_portal_identifiers](jgi_portal_identifiers.md)]
            * [neon_study_identifiers](neon_study_identifiers.md) [ [neon_identifiers](neon_identifiers.md)]
            * [insdc_sra_ena_study_identifiers](insdc_sra_ena_study_identifiers.md) [ [insdc_identifiers](insdc_identifiers.md)]
            * [insdc_bioproject_identifiers](insdc_bioproject_identifiers.md) [ [insdc_identifiers](insdc_identifiers.md)]
            * [gold_study_identifiers](gold_study_identifiers.md) [ [gold_identifiers](gold_identifiers.md)]
            * [mgnify_project_identifiers](mgnify_project_identifiers.md) [ [mgnify_identifiers](mgnify_identifiers.md)]
            * [gnps_task_identifiers](gnps_task_identifiers.md) [ [gnps_identifiers](gnps_identifiers.md)]
            * [emsl_project_identifiers](emsl_project_identifiers.md) [ [emsl_identifiers](emsl_identifiers.md)]








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
name: study_identifiers
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
is_a: external_database_identifiers
abstract: true
multivalued: true
alias: study_identifiers
range: external_identifier
pattern: ^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$

```
</details>