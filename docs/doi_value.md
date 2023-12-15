# Slot: doi_value


_A digital object identifier, which is intended to persistantly identify some resource on the web._



URI: [nmdc:doi_value](https://w3id.org/nmdc/doi_value)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Doi](Doi.md) | A centrally registered identifier symbol used to uniquely identify objects gi... |  no  |







## Properties

* Range: [Uriorcurie](Uriorcurie.md)

* Required: True

* Regex pattern: `^doi:10.\d{2,9}/.*$`



## Aliases


* DOI
* digital object identifier




## Examples

| Value |
| --- |
| doi:10.46936/10.25585/60000880 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: doi_value
description: A digital object identifier, which is intended to persistantly identify
  some resource on the web.
examples:
- value: doi:10.46936/10.25585/60000880
  description: The DOI links to an electronic document.
in_subset:
- data_portal_subset
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- DOI
- digital object identifier
exact_mappings:
- OBI:0002110
narrow_mappings:
- edam.data:1188
rank: 1000
domain: Doi
alias: doi_value
domain_of:
- Doi
range: uriorcurie
required: true
pattern: ^doi:10.\d{2,9}/.*$

```
</details>