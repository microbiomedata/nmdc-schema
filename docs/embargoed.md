# Slot: embargoed


_If true, the data are embargoed and not available for public access._



URI: [nmdc:embargoed](https://w3id.org/nmdc/embargoed)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [Boolean](Boolean.md)

* Recommended: True





## TODOs

* make this required?
* first apply to Biosample
* try to apply to all Biosamples in a particular nmdc-server SubmissionMetadata?
* applying to a Study may not be granular enough

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: embargoed
description: If true, the data are embargoed and not available for public access.
todos:
- make this required?
- first apply to Biosample
- try to apply to all Biosamples in a particular nmdc-server SubmissionMetadata?
- applying to a Study may not be granular enough
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
alias: embargoed
domain_of:
- Biosample
range: boolean
recommended: true

```
</details>