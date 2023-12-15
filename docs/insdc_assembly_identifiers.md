# Slot: insdc_assembly_identifiers

URI: [nmdc:insdc_assembly_identifiers](https://w3id.org/nmdc/insdc_assembly_identifiers)




## Inheritance

* [assembly_identifiers](assembly_identifiers.md)
    * **insdc_assembly_identifiers** [ [insdc_identifiers](insdc_identifiers.md)]





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MetagenomeAssembly](MetagenomeAssembly.md) | A workflow execution activity that converts sequencing reads into an assemble... |  no  |
[MetatranscriptomeAssembly](MetatranscriptomeAssembly.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^insdc.sra:[A-Z]+[0-9]+(\.[0-9]+)?$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: insdc_assembly_identifiers
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
is_a: assembly_identifiers
mixins:
- insdc_identifiers
alias: insdc_assembly_identifiers
domain_of:
- MetagenomeAssembly
- MetatranscriptomeAssembly
range: string
pattern: ^insdc.sra:[A-Z]+[0-9]+(\.[0-9]+)?$

```
</details>