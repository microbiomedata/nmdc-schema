# Slot: ctg_powsum


_Powersum of all contigs is the same as logsum except that it uses the sum of (length*(length^P)) for some power P (default P=0.25)._



URI: [nmdc:ctg_powsum](https://w3id.org/nmdc/ctg_powsum)




## Inheritance

* [metagenome_assembly_parameter](metagenome_assembly_parameter.md)
    * **ctg_powsum**





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
name: ctg_powsum
description: Powersum of all contigs is the same as logsum except that it uses the
  sum of (length*(length^P)) for some power P (default P=0.25).
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
is_a: metagenome_assembly_parameter
alias: ctg_powsum
domain_of:
- MetagenomeAssembly
- MetatranscriptomeAssembly
range: float

```
</details>