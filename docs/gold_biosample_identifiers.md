# Slot: gold_biosample_identifiers


_identifiers for corresponding sample in GOLD_



URI: [nmdc:gold_biosample_identifiers](https://w3id.org/nmdc/gold_biosample_identifiers)




## Inheritance

* [alternative_identifiers](alternative_identifiers.md)
    * [external_database_identifiers](external_database_identifiers.md)
        * [biosample_identifiers](biosample_identifiers.md)
            * **gold_biosample_identifiers** [ [gold_identifiers](gold_identifiers.md)]





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [ExternalIdentifier](ExternalIdentifier.md)

* Multivalued: True

* Regex pattern: `^gold:Gb[0-9]+$`






## Examples

| Value |
| --- |
| https://bioregistry.io/gold:Gb0312930 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: gold_biosample_identifiers
description: identifiers for corresponding sample in GOLD
examples:
- value: https://bioregistry.io/gold:Gb0312930
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
is_a: biosample_identifiers
mixins:
- gold_identifiers
multivalued: true
alias: gold_biosample_identifiers
domain_of:
- Biosample
range: external_identifier
pattern: ^gold:Gb[0-9]+$

```
</details>