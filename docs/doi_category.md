# Slot: doi_category


_The resource type the corresponding doi resolves to._



URI: [nmdc:doi_category](https://w3id.org/nmdc/doi_category)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Doi](Doi.md) | A centrally registered identifier symbol used to uniquely identify objects gi... |  no  |







## Properties

* Range: [DoiCategoryEnum](DoiCategoryEnum.md)

* Required: True






## Examples

| Value |
| --- |
| dataset_doi |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: doi_category
description: The resource type the corresponding doi resolves to.
examples:
- value: dataset_doi
  description: The corresponding DOI is a dataset resource type.
in_subset:
- data_portal_subset
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
domain: Doi
alias: doi_category
domain_of:
- Doi
range: DoiCategoryEnum
required: true

```
</details>