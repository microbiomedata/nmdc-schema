# Slot: GNPS task identifiers (gnps_task_identifiers)


_identifiers that link a NMDC study to a web-based report about metabolomics analysis progress and results_



URI: [nmdc:gnps_task_identifiers](https://w3id.org/nmdc/gnps_task_identifiers)




## Inheritance

* [alternative_identifiers](alternative_identifiers.md)
    * [external_database_identifiers](external_database_identifiers.md)
        * [study_identifiers](study_identifiers.md)
            * **gnps_task_identifiers** [ [gnps_identifiers](gnps_identifiers.md)]





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Study](Study.md) | A study summarizes the overall goal of a research initiative and outlines the... |  no  |







## Properties

* Range: [ExternalIdentifier](ExternalIdentifier.md)

* Multivalued: True

* Regex pattern: `^gnps\.task:[a-f0-9]+$`






## Examples

| Value |
| --- |
| gnps.task:4b848c342a4f4abc871bdf8a09a60807 |

## Comments

* this could be considered a related identifier, as the metabolomics progress and results aren't a study per se
* this identifier was registered with bioregistry but not identifiers.org

## See Also

* [https://microbiomedata.github.io/nmdc-schema/MetabolomicsAnalysisActivity/](https://microbiomedata.github.io/nmdc-schema/MetabolomicsAnalysisActivity/)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: gnps_task_identifiers
description: identifiers that link a NMDC study to a web-based report about metabolomics
  analysis progress and results
title: GNPS task identifiers
comments:
- this could be considered a related identifier, as the metabolomics progress and
  results aren't a study per se
- this identifier was registered with bioregistry but not identifiers.org
examples:
- value: gnps.task:4b848c342a4f4abc871bdf8a09a60807
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- https://microbiomedata.github.io/nmdc-schema/MetabolomicsAnalysisActivity/
rank: 1000
is_a: study_identifiers
mixins:
- gnps_identifiers
domain: Study
multivalued: true
alias: gnps_task_identifiers
domain_of:
- Study
range: external_identifier
pattern: ^gnps\.task:[a-f0-9]+$

```
</details>