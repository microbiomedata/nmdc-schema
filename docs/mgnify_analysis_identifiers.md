# Slot: mgnify_analysis_identifiers

URI: [nmdc:mgnify_analysis_identifiers](https://w3id.org/nmdc/mgnify_analysis_identifiers)




## Inheritance

* [alternative_identifiers](alternative_identifiers.md)
    * [external_database_identifiers](external_database_identifiers.md)
        * [analysis_identifiers](analysis_identifiers.md)
            * **mgnify_analysis_identifiers** [ [mgnify_identifiers](mgnify_identifiers.md)]








## Properties

* Range: [ExternalIdentifier](ExternalIdentifier.md)

* Multivalued: True

* Regex pattern: `^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$`






## Examples

| Value |
| --- |
| https://www.ebi.ac.uk/metagenomics/analyses/MGYA00002270 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: mgnify_analysis_identifiers
notes:
- 'removed pattern: "^mgnify:MGYA[0-9]+$" ## TODO https://github.com/bioregistry/bioregistry/issues/109'
examples:
- value: https://www.ebi.ac.uk/metagenomics/analyses/MGYA00002270
  description: combined analyses (taxonomic, functional) of sample ERS438107
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
is_a: analysis_identifiers
mixins:
- mgnify_identifiers
multivalued: true
alias: mgnify_analysis_identifiers
range: external_identifier
pattern: ^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$

```
</details>