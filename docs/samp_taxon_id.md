# Slot: Taxonomy ID of DNA sample (samp_taxon_id)


_NCBI taxon id of the sample.  Maybe be a single taxon or mixed taxa sample. Use 'synthetic metagenome’ for mock community/positive controls, or 'blank sample' for negative controls._



URI: [MIXS:0001320](https://w3id.org/mixs/0001320)




## Inheritance

* [investigation_field](investigation_field.md)
    * **samp_taxon_id**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [ControlledIdentifiedTermValue](ControlledIdentifiedTermValue.md)



## Aliases


* Taxonomy ID of DNA sample



## Comments

* coal metagenome [NCBITaxon:1260732] would be a reasonable has_raw_value

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | Taxonomy ID |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: samp_taxon_id
annotations:
  expected_value:
    tag: expected_value
    value: Taxonomy ID
description: NCBI taxon id of the sample.  Maybe be a single taxon or mixed taxa sample.
  Use 'synthetic metagenome’ for mock community/positive controls, or 'blank sample'
  for negative controls.
title: Taxonomy ID of DNA sample
comments:
- coal metagenome [NCBITaxon:1260732] would be a reasonable has_raw_value
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- Taxonomy ID of DNA sample
rank: 1000
is_a: investigation field
slot_uri: MIXS:0001320
multivalued: false
alias: samp_taxon_id
domain_of:
- Biosample
range: ControlledIdentifiedTermValue

```
</details>