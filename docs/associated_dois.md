# Slot: associated_dois


_A list of DOIs associated with a resource, such as a list of DOIS associated with a Study._



URI: [nmdc:associated_dois](https://w3id.org/nmdc/associated_dois)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Study](Study.md) | A study summarizes the overall goal of a research initiative and outlines the... |  no  |







## Properties

* Range: [Doi](Doi.md)

* Multivalued: True



## Aliases


* Associated DOIs
* Associated digital object identifiers




## Examples

| Value |
| --- |
| [{'doi': 'doi:10.46936/intm.proj.2021.60141/60000423', 'doi_provider': 'emsl', 'doi_category': 'award_doi'}, {'doi': 'doi:10.1101/2022.12.12.520098', 'doi_category': 'publication_doi'}, {'doi': 'doi:10.48321/D1Z60Q', 'doi_category': 'data_management_plan_doi', 'doi_provider': 'gsc'}] |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: associated_dois
description: A list of DOIs associated with a resource, such as a list of DOIS associated
  with a Study.
examples:
- value: '[{''doi'': ''doi:10.46936/intm.proj.2021.60141/60000423'', ''doi_provider'':
    ''emsl'', ''doi_category'': ''award_doi''}, {''doi'': ''doi:10.1101/2022.12.12.520098'',
    ''doi_category'': ''publication_doi''}, {''doi'': ''doi:10.48321/D1Z60Q'', ''doi_category'':
    ''data_management_plan_doi'', ''doi_provider'': ''gsc''}]'
  description: Provides a list of two DOIs; specifically, an EMSL award DOI and a
    publication DOI.
in_subset:
- data_portal_subset
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- Associated DOIs
- Associated digital object identifiers
rank: 1000
domain: Study
multivalued: true
alias: associated_dois
domain_of:
- Study
range: Doi
inlined: true
inlined_as_list: true

```
</details>