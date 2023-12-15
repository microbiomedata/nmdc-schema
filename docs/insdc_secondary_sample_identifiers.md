# Slot: insdc_secondary_sample_identifiers


_secondary identifiers for corresponding sample in INSDC_



URI: [nmdc:insdc_secondary_sample_identifiers](https://w3id.org/nmdc/insdc_secondary_sample_identifiers)




## Inheritance

* [alternative_identifiers](alternative_identifiers.md)
    * [external_database_identifiers](external_database_identifiers.md)
        * [biosample_identifiers](biosample_identifiers.md)
            * **insdc_secondary_sample_identifiers** [ [insdc_identifiers](insdc_identifiers.md)]








## Properties

* Range: [ExternalIdentifier](ExternalIdentifier.md)

* Multivalued: True

* Regex pattern: `^biosample:(E|D|S)RS[0-9]{6,}$`






## Examples

| Value |
| --- |
| https://bioregistry.io/insdc.sra:DRS166340 |

## Comments

* ENA redirects these to primary IDs, e.g. https://www.ebi.ac.uk/ena/browser/view/DRS166340 -> SAMD00212331
* MGnify uses these as their primary sample IDs

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: insdc_secondary_sample_identifiers
description: secondary identifiers for corresponding sample in INSDC
comments:
- ENA redirects these to primary IDs, e.g. https://www.ebi.ac.uk/ena/browser/view/DRS166340
  -> SAMD00212331
- MGnify uses these as their primary sample IDs
examples:
- value: https://bioregistry.io/insdc.sra:DRS166340
  description: I13_N_5-10 sample from Soil fungal diversity along elevational gradients
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
is_a: biosample_identifiers
mixins:
- insdc_identifiers
multivalued: true
alias: insdc_secondary_sample_identifiers
range: external_identifier
pattern: ^biosample:(E|D|S)RS[0-9]{6,}$

```
</details>