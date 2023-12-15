# Slot: insdc_analysis_identifiers

URI: [nmdc:insdc_analysis_identifiers](https://w3id.org/nmdc/insdc_analysis_identifiers)




## Inheritance

* [alternative_identifiers](alternative_identifiers.md)
    * [external_database_identifiers](external_database_identifiers.md)
        * [analysis_identifiers](analysis_identifiers.md)
            * **insdc_analysis_identifiers** [ [insdc_identifiers](insdc_identifiers.md)]








## Properties

* Range: [ExternalIdentifier](ExternalIdentifier.md)

* Multivalued: True

* Regex pattern: `^insdc.sra:(E|D|S)RR[0-9]{6,}$`






## Examples

| Value |
| --- |
| https://www.ebi.ac.uk/metagenomics/runs/DRR218479 |
| https://www.ebi.ac.uk/ena/browser/view/ERR436051 |

## Comments

* in INSDC this is a run but it corresponds to a GOLD analysis

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: insdc_analysis_identifiers
comments:
- in INSDC this is a run but it corresponds to a GOLD analysis
examples:
- value: https://www.ebi.ac.uk/metagenomics/runs/DRR218479
  description: Illumina MiSeq paired end sequencing of SAMD00212331
- value: https://www.ebi.ac.uk/ena/browser/view/ERR436051
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
is_a: analysis_identifiers
mixins:
- insdc_identifiers
multivalued: true
alias: insdc_analysis_identifiers
range: external_identifier
pattern: ^insdc.sra:(E|D|S)RR[0-9]{6,}$

```
</details>