# Slot: filter type (filter_type)


_A device which removes solid particulates or airborne molecular contaminants_



URI: [MIXS:0000765](https://w3id.org/mixs/0000765)




## Inheritance

* [core_field](core_field.md)
    * **filter_type**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [FilterTypeEnum](FilterTypeEnum.md)

* Multivalued: True



## Aliases


* filter type




## Examples

| Value |
| --- |
| HEPA |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | enumeration || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: filter_type
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: m
description: A device which removes solid particulates or airborne molecular contaminants
title: filter type
examples:
- value: HEPA
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- filter type
rank: 1000
is_a: core field
slot_uri: MIXS:0000765
multivalued: true
alias: filter_type
domain_of:
- Biosample
range: filter_type_enum

```
</details>