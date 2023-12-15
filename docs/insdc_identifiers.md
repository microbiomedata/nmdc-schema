# Slot: insdc_identifiers


_Any identifier covered by the International Nucleotide Sequence Database Collaboration_



URI: [nmdc:insdc_identifiers](https://w3id.org/nmdc/insdc_identifiers)



<!-- no inheritance hierarchy -->






## Mixin Usage

| mixed into | description | range | domain |
| --- | --- | --- | --- |
| [insdc_sra_ena_study_identifiers](insdc_sra_ena_study_identifiers.md) | identifiers for corresponding project in INSDC SRA / ENA | None |  |
| [insdc_bioproject_identifiers](insdc_bioproject_identifiers.md) | identifiers for corresponding project in INSDC Bioproject | None | Study, OmicsProcessing |
| [insdc_biosample_identifiers](insdc_biosample_identifiers.md) | identifiers for corresponding sample in INSDC | None | Biosample |
| [insdc_secondary_sample_identifiers](insdc_secondary_sample_identifiers.md) | secondary identifiers for corresponding sample in INSDC | None |  |
| [insdc_experiment_identifiers](insdc_experiment_identifiers.md) |  | None | OmicsProcessing |
| [insdc_analysis_identifiers](insdc_analysis_identifiers.md) |  | None |  |
| [insdc_assembly_identifiers](insdc_assembly_identifiers.md) |  | None | MetagenomeAssembly, MetatranscriptomeAssembly |



## Properties

* Range: [String](String.md)

* Mixin: True



## Aliases


* EBI identifiers
* NCBI identifiers
* DDBJ identifiers



## Comments

* note that we deliberately abstract over which of the partner databases accepted the initial submission
* the first letter of the accession indicates which partner accepted the initial submission: E for ENA, D for DDBJ, or S or N for NCBI.

## See Also

* [https://www.insdc.org/](https://www.insdc.org/)
* [https://ena-docs.readthedocs.io/en/latest/submit/general-guide/accessions.html](https://ena-docs.readthedocs.io/en/latest/submit/general-guide/accessions.html)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: insdc_identifiers
description: Any identifier covered by the International Nucleotide Sequence Database
  Collaboration
comments:
- note that we deliberately abstract over which of the partner databases accepted
  the initial submission
- 'the first letter of the accession indicates which partner accepted the initial
  submission: E for ENA, D for DDBJ, or S or N for NCBI.'
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- https://www.insdc.org/
- https://ena-docs.readthedocs.io/en/latest/submit/general-guide/accessions.html
aliases:
- EBI identifiers
- NCBI identifiers
- DDBJ identifiers
rank: 1000
mixin: true
alias: insdc_identifiers
range: string

```
</details>