# Slot: contigs


_The sum of the (length*log(length)) of all contigs, times some constant.  Increase the contiguity, the score will increase_



URI: [nmdc:contigs](https://w3id.org/nmdc/contigs)




## Inheritance

* [metagenome_assembly_parameter](metagenome_assembly_parameter.md)
    * **contigs**





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
name: contigs
description: The sum of the (length*log(length)) of all contigs, times some constant.  Increase
  the contiguity, the score will increase
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
is_a: metagenome_assembly_parameter
alias: contigs
domain_of:
- MetagenomeAssembly
- MetatranscriptomeAssembly
range: float

```
</details>