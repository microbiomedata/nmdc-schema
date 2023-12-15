# Slot: insdc_experiment_identifiers

URI: [nmdc:insdc_experiment_identifiers](https://w3id.org/nmdc/insdc_experiment_identifiers)




## Inheritance

* [alternative_identifiers](alternative_identifiers.md)
    * [external_database_identifiers](external_database_identifiers.md)
        * **insdc_experiment_identifiers** [ [insdc_identifiers](insdc_identifiers.md)]





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[OmicsProcessing](OmicsProcessing.md) | The methods and processes used to generate omics data from a biosample or org... |  no  |







## Properties

* Range: [ExternalIdentifier](ExternalIdentifier.md)

* Multivalued: True

* Regex pattern: `^insdc.sra:(E|D|S)RX[0-9]{6,}$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: insdc_experiment_identifiers
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
is_a: external_database_identifiers
mixins:
- insdc_identifiers
domain: OmicsProcessing
multivalued: true
alias: insdc_experiment_identifiers
domain_of:
- OmicsProcessing
range: external_identifier
pattern: ^insdc.sra:(E|D|S)RX[0-9]{6,}$

```
</details>