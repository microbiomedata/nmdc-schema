# Slot: scaf_n90


_Given a set of scaffolds, each with its own length, the N90 count is defined as the smallest number of scaffolds whose length sum makes up 90% of genome size._



URI: [nmdc:scaf_n90](https://w3id.org/nmdc/scaf_n90)




## Inheritance

* [metagenome_assembly_parameter](metagenome_assembly_parameter.md)
    * **scaf_n90**





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
name: scaf_n90
description: Given a set of scaffolds, each with its own length, the N90 count is
  defined as the smallest number of scaffolds whose length sum makes up 90% of genome
  size.
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
is_a: metagenome_assembly_parameter
alias: scaf_n90
domain_of:
- MetagenomeAssembly
- MetatranscriptomeAssembly
range: float

```
</details>