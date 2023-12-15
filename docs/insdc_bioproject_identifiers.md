# Slot: insdc_bioproject_identifiers


_identifiers for corresponding project in INSDC Bioproject_



URI: [nmdc:insdc_bioproject_identifiers](https://w3id.org/nmdc/insdc_bioproject_identifiers)




## Inheritance

* [alternative_identifiers](alternative_identifiers.md)
    * [external_database_identifiers](external_database_identifiers.md)
        * [study_identifiers](study_identifiers.md)
            * **insdc_bioproject_identifiers** [ [insdc_identifiers](insdc_identifiers.md)]





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Study](Study.md) | A study summarizes the overall goal of a research initiative and outlines the... |  yes  |
[OmicsProcessing](OmicsProcessing.md) | The methods and processes used to generate omics data from a biosample or org... |  no  |







## Properties

* Range: [ExternalIdentifier](ExternalIdentifier.md)

* Multivalued: True

* Regex pattern: `^bioproject:PRJ[DEN][A-Z][0-9]+$`



## Aliases


* NCBI bioproject identifiers
* DDBJ bioproject identifiers




## Examples

| Value |
| --- |
| https://bioregistry.io/bioproject:PRJNA366857 |

## Comments

* these are distinct IDs from INSDC SRA/ENA project identifiers, but are usually(?) one to one

## See Also

* [https://www.ncbi.nlm.nih.gov/bioproject/](https://www.ncbi.nlm.nih.gov/bioproject/)
* [https://www.ddbj.nig.ac.jp/bioproject/index-e.html](https://www.ddbj.nig.ac.jp/bioproject/index-e.html)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: insdc_bioproject_identifiers
description: identifiers for corresponding project in INSDC Bioproject
comments:
- these are distinct IDs from INSDC SRA/ENA project identifiers, but are usually(?)
  one to one
examples:
- value: https://bioregistry.io/bioproject:PRJNA366857
  description: Avena fatua rhizosphere microbial communities - H1_Rhizo_Litter_2 metatranscriptome
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- https://www.ncbi.nlm.nih.gov/bioproject/
- https://www.ddbj.nig.ac.jp/bioproject/index-e.html
aliases:
- NCBI bioproject identifiers
- DDBJ bioproject identifiers
rank: 1000
is_a: study_identifiers
mixins:
- insdc_identifiers
multivalued: true
alias: insdc_bioproject_identifiers
domain_of:
- Study
- OmicsProcessing
range: external_identifier
pattern: ^bioproject:PRJ[DEN][A-Z][0-9]+$

```
</details>