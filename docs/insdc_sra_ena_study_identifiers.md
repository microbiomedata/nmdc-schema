# Slot: insdc_sra_ena_study_identifiers


_identifiers for corresponding project in INSDC SRA / ENA_



URI: [nmdc:insdc_sra_ena_study_identifiers](https://w3id.org/nmdc/insdc_sra_ena_study_identifiers)




## Inheritance

* [alternative_identifiers](alternative_identifiers.md)
    * [external_database_identifiers](external_database_identifiers.md)
        * [study_identifiers](study_identifiers.md)
            * **insdc_sra_ena_study_identifiers** [ [insdc_identifiers](insdc_identifiers.md)]








## Properties

* Range: [ExternalIdentifier](ExternalIdentifier.md)

* Multivalued: True

* Regex pattern: `^insdc.sra:(E|D|S)RP[0-9]{6,}$`



## Aliases


* EBI ENA study identifiers
* NCBI SRA identifiers
* DDBJ SRA identifiers




## Examples

| Value |
| --- |
| https://bioregistry.io/insdc.sra:SRP121659 |

## See Also

* [https://github.com/bioregistry/bioregistry/issues/109](https://github.com/bioregistry/bioregistry/issues/109)
* [https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=studies](https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=studies)
* [https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=studies](https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=studies)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: insdc_sra_ena_study_identifiers
description: identifiers for corresponding project in INSDC SRA / ENA
examples:
- value: https://bioregistry.io/insdc.sra:SRP121659
  description: Avena fatua rhizosphere microbial communities - H1_Rhizo_Litter_2 metatranscriptome
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- https://github.com/bioregistry/bioregistry/issues/109
- https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=studies
- https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=studies
aliases:
- EBI ENA study identifiers
- NCBI SRA identifiers
- DDBJ SRA identifiers
rank: 1000
is_a: study_identifiers
mixins:
- insdc_identifiers
multivalued: true
alias: insdc_sra_ena_study_identifiers
range: external_identifier
pattern: ^insdc.sra:(E|D|S)RP[0-9]{6,}$

```
</details>