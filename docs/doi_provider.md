# Slot: doi_provider


_The authority, or organization, the DOI is associated with._



URI: [nmdc:doi_provider](https://w3id.org/nmdc/doi_provider)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Doi](Doi.md) | A centrally registered identifier symbol used to uniquely identify objects gi... |  no  |







## Properties

* Range: [DoiProviderEnum](DoiProviderEnum.md)






## Examples

| Value |
| --- |
| ess_dive |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: doi_provider
description: The authority, or organization, the DOI is associated with.
examples:
- value: ess_dive
  description: The corresponding DOI is associated with ESS-DIVE.
in_subset:
- data_portal_subset
from_schema: https://w3id.org/nmdc/nmdc
close_mappings:
- NCIT:C74932
rank: 1000
domain: Doi
alias: doi_provider
domain_of:
- Doi
range: DoiProviderEnum

```
</details>