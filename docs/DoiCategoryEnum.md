# Enum: DoiCategoryEnum



URI: [DoiCategoryEnum](DoiCategoryEnum.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| award_doi | None | A type of DOI that resolves to a funding authority |
| dataset_doi | None | A type of DOI that resolves to generated data |
| publication_doi | None | A type of DOI that resolves to a publication |
| data_management_plan_doi | None | A type of DOI that resolves to a data management plan |




## Slots

| Name | Description |
| ---  | --- |
| [doi_category](doi_category.md) | The resource type the corresponding doi resolves to |






## Comments

* See especially the resourceTypeGeneral section of the DataCite PDF, on pp48-53 as of 2023-07-19

## See Also

* [https://schema.datacite.org/meta/kernel-4.4/doc/DataCite-MetadataKernel_v4.4.pdf](https://schema.datacite.org/meta/kernel-4.4/doc/DataCite-MetadataKernel_v4.4.pdf)
* [https://api.crossref.org/types](https://api.crossref.org/types)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: DoiCategoryEnum
comments:
- See especially the resourceTypeGeneral section of the DataCite PDF, on pp48-53 as
  of 2023-07-19
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- https://schema.datacite.org/meta/kernel-4.4/doc/DataCite-MetadataKernel_v4.4.pdf
- https://api.crossref.org/types
rank: 1000
permissible_values:
  award_doi:
    text: award_doi
    description: A type of DOI that resolves to a funding authority.
  dataset_doi:
    text: dataset_doi
    description: A type of DOI that resolves to generated data.
  publication_doi:
    text: publication_doi
    description: A type of DOI that resolves to a publication.
  data_management_plan_doi:
    text: data_management_plan_doi
    description: A type of DOI that resolves to a data management plan.

```
</details>