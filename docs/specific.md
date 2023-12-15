# Slot: specifications (specific)


_The building specifications. If design is chosen, indicate phase: conceptual, schematic, design development, construction documents_



URI: [MIXS:0000836](https://w3id.org/mixs/0000836)




## Inheritance

* [core_field](core_field.md)
    * **specific**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [SpecificEnum](SpecificEnum.md)



## Aliases


* specifications




## Examples

| Value |
| --- |
| construction |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | enumeration || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: specific
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: 'The building specifications. If design is chosen, indicate phase: conceptual,
  schematic, design development, construction documents'
title: specifications
examples:
- value: construction
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- specifications
rank: 1000
is_a: core field
slot_uri: MIXS:0000836
multivalued: false
alias: specific
domain_of:
- Biosample
range: specific_enum

```
</details>