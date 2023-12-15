# Slot: external_database_identifiers


_Link to corresponding identifier in external database_



URI: [nmdc:external_database_identifiers](https://w3id.org/nmdc/external_database_identifiers)




## Inheritance

* [alternative_identifiers](alternative_identifiers.md)
    * **external_database_identifiers**
        * [img_identifiers](img_identifiers.md)
        * [study_identifiers](study_identifiers.md)
        * [biosample_identifiers](biosample_identifiers.md)
        * [omics_processing_identifiers](omics_processing_identifiers.md)
        * [insdc_experiment_identifiers](insdc_experiment_identifiers.md) [ [insdc_identifiers](insdc_identifiers.md)]
        * [analysis_identifiers](analysis_identifiers.md)





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ProcessedSample](ProcessedSample.md) |  |  no  |







## Properties

* Range: [ExternalIdentifier](ExternalIdentifier.md)

* Multivalued: True

* Regex pattern: `^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$`





## Comments

* The value of this field is always a registered CURIE

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: external_database_identifiers
description: Link to corresponding identifier in external database
notes:
- had tried ranges of external identifier and string
comments:
- The value of this field is always a registered CURIE
from_schema: https://w3id.org/nmdc/nmdc
close_mappings:
- skos:closeMatch
rank: 1000
is_a: alternative_identifiers
abstract: true
multivalued: true
alias: external_database_identifiers
domain_of:
- ProcessedSample
range: external_identifier
pattern: ^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$

```
</details>