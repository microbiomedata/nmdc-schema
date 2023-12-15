# Slot: insdc_biosample_identifiers


_identifiers for corresponding sample in INSDC_



URI: [nmdc:insdc_biosample_identifiers](https://w3id.org/nmdc/insdc_biosample_identifiers)




## Inheritance

* [alternative_identifiers](alternative_identifiers.md)
    * [external_database_identifiers](external_database_identifiers.md)
        * [biosample_identifiers](biosample_identifiers.md)
            * **insdc_biosample_identifiers** [ [insdc_identifiers](insdc_identifiers.md)]





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [ExternalIdentifier](ExternalIdentifier.md)

* Multivalued: True

* Regex pattern: `^biosample:SAM[NED]([A-Z])?[0-9]+$`



## Aliases


* EBI biosample identifiers
* NCBI biosample identifiers
* DDBJ biosample identifiers




## Examples

| Value |
| --- |
| https://bioregistry.io/biosample:SAMEA5989477 |
| https://bioregistry.io/biosample:SAMD00212331 |

## See Also

* [https://github.com/bioregistry/bioregistry/issues/108](https://github.com/bioregistry/bioregistry/issues/108)
* [https://www.ebi.ac.uk/biosamples/](https://www.ebi.ac.uk/biosamples/)
* [https://www.ncbi.nlm.nih.gov/biosample](https://www.ncbi.nlm.nih.gov/biosample)
* [https://www.ddbj.nig.ac.jp/biosample/index-e.html](https://www.ddbj.nig.ac.jp/biosample/index-e.html)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: insdc_biosample_identifiers
description: identifiers for corresponding sample in INSDC
examples:
- value: https://bioregistry.io/biosample:SAMEA5989477
- value: https://bioregistry.io/biosample:SAMD00212331
  description: I13_N_5-10 sample from Soil fungal diversity along elevational gradients
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- https://github.com/bioregistry/bioregistry/issues/108
- https://www.ebi.ac.uk/biosamples/
- https://www.ncbi.nlm.nih.gov/biosample
- https://www.ddbj.nig.ac.jp/biosample/index-e.html
aliases:
- EBI biosample identifiers
- NCBI biosample identifiers
- DDBJ biosample identifiers
rank: 1000
is_a: biosample_identifiers
mixins:
- insdc_identifiers
multivalued: true
alias: insdc_biosample_identifiers
domain_of:
- Biosample
range: external_identifier
pattern: ^biosample:SAM[NED]([A-Z])?[0-9]+$

```
</details>