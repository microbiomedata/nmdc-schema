# Slot: scaf_n50


_Given a set of scaffolds, each with its own length, the N50 count is defined as the smallest number of scaffolds whose length sum makes up half of genome size._



URI: [nmdc:scaf_n50](https://w3id.org/nmdc/scaf_n50)




## Inheritance

* [metagenome_assembly_parameter](metagenome_assembly_parameter.md)
    * **scaf_n50**





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
name: scaf_n50
description: Given a set of scaffolds, each with its own length, the N50 count is
  defined as the smallest number of scaffolds whose length sum makes up half of genome
  size.
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
is_a: metagenome_assembly_parameter
alias: scaf_n50
domain_of:
- MetagenomeAssembly
- MetatranscriptomeAssembly
range: float

```
</details>