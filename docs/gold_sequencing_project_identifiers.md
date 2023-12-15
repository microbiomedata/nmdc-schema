# Slot: gold_sequencing_project_identifiers


_identifiers for corresponding sequencing project in GOLD_



URI: [nmdc:gold_sequencing_project_identifiers](https://w3id.org/nmdc/gold_sequencing_project_identifiers)




## Inheritance

* [alternative_identifiers](alternative_identifiers.md)
    * [external_database_identifiers](external_database_identifiers.md)
        * [omics_processing_identifiers](omics_processing_identifiers.md)
            * **gold_sequencing_project_identifiers** [ [gold_identifiers](gold_identifiers.md)]





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[OmicsProcessing](OmicsProcessing.md) | The methods and processes used to generate omics data from a biosample or org... |  no  |







## Properties

* Range: [ExternalIdentifier](ExternalIdentifier.md)

* Multivalued: True

* Regex pattern: `^gold:Gp[0-9]+$`






## Examples

| Value |
| --- |
| https://bioregistry.io/gold:Gp0108335 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: gold_sequencing_project_identifiers
description: identifiers for corresponding sequencing project in GOLD
examples:
- value: https://bioregistry.io/gold:Gp0108335
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
is_a: omics_processing_identifiers
mixins:
- gold_identifiers
domain: OmicsProcessing
multivalued: true
alias: gold_sequencing_project_identifiers
domain_of:
- OmicsProcessing
range: external_identifier
pattern: ^gold:Gp[0-9]+$

```
</details>