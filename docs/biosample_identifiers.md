# Slot: biosample_identifiers

URI: [nmdc:biosample_identifiers](https://w3id.org/nmdc/biosample_identifiers)




## Inheritance

* [alternative_identifiers](alternative_identifiers.md)
    * [external_database_identifiers](external_database_identifiers.md)
        * **biosample_identifiers**
            * [neon_biosample_identifiers](neon_biosample_identifiers.md) [ [neon_identifiers](neon_identifiers.md)]
            * [gold_biosample_identifiers](gold_biosample_identifiers.md) [ [gold_identifiers](gold_identifiers.md)]
            * [insdc_biosample_identifiers](insdc_biosample_identifiers.md) [ [insdc_identifiers](insdc_identifiers.md)]
            * [insdc_secondary_sample_identifiers](insdc_secondary_sample_identifiers.md) [ [insdc_identifiers](insdc_identifiers.md)]
            * [emsl_biosample_identifiers](emsl_biosample_identifiers.md) [ [emsl_identifiers](emsl_identifiers.md)]
            * [igsn_biosample_identifiers](igsn_biosample_identifiers.md) [ [igsn_identifiers](igsn_identifiers.md)]








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
name: biosample_identifiers
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
is_a: external_database_identifiers
abstract: true
multivalued: true
alias: biosample_identifiers
range: external_identifier
pattern: ^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$

```
</details>