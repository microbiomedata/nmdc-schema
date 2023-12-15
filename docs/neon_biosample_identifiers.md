# Slot: neon_biosample_identifiers

URI: [nmdc:neon_biosample_identifiers](https://w3id.org/nmdc/neon_biosample_identifiers)




## Inheritance

* [alternative_identifiers](alternative_identifiers.md)
    * [external_database_identifiers](external_database_identifiers.md)
        * [biosample_identifiers](biosample_identifiers.md)
            * **neon_biosample_identifiers** [ [neon_identifiers](neon_identifiers.md)]





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
name: neon_biosample_identifiers
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
is_a: biosample_identifiers
mixins:
- neon_identifiers
multivalued: true
alias: neon_biosample_identifiers
domain_of:
- Biosample
range: external_identifier
pattern: ^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$

```
</details>