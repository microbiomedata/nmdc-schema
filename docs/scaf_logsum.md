# Slot: scaf_logsum


_The sum of the (length*log(length)) of all scaffolds, times some constant.  Increase the contiguity, the score will increase_



URI: [nmdc:scaf_logsum](https://w3id.org/nmdc/scaf_logsum)




## Inheritance

* [metagenome_assembly_parameter](metagenome_assembly_parameter.md)
    * **scaf_logsum**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MetagenomeAssembly](MetagenomeAssembly.md) | A workflow execution activity that converts sequencing reads into an assemble... |  no  |
[MetatranscriptomeAssembly](MetatranscriptomeAssembly.md) |  |  no  |







## Properties

* Range: [Float](Float.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: scaf_logsum
description: The sum of the (length*log(length)) of all scaffolds, times some constant.  Increase
  the contiguity, the score will increase
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
is_a: metagenome_assembly_parameter
alias: scaf_logsum
domain_of:
- MetagenomeAssembly
- MetatranscriptomeAssembly
range: float

```
</details>