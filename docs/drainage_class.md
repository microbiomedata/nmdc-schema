# Slot: drainage classification (drainage_class)


_Drainage classification from a standard system such as the USDA system_



URI: [MIXS:0001085](https://w3id.org/mixs/0001085)




## Inheritance

* [core_field](core_field.md)
    * **drainage_class**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [DrainageClassEnum](DrainageClassEnum.md)



## Aliases


* drainage classification




## Examples

| Value |
| --- |
| well |

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
name: drainage_class
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: Drainage classification from a standard system such as the USDA system
title: drainage classification
examples:
- value: well
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- drainage classification
rank: 1000
is_a: core field
slot_uri: MIXS:0001085
multivalued: false
alias: drainage_class
domain_of:
- Biosample
range: drainage_class_enum

```
</details>