# Slot: ceiling type (ceil_type)


_The type of ceiling according to the ceiling's appearance or construction_



URI: [MIXS:0000784](https://w3id.org/mixs/0000784)




## Inheritance

* [core_field](core_field.md)
    * **ceil_type**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [CeilTypeEnum](CeilTypeEnum.md)



## Aliases


* ceiling type




## Examples

| Value |
| --- |
| coffered |

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
name: ceil_type
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The type of ceiling according to the ceiling's appearance or construction
title: ceiling type
examples:
- value: coffered
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- ceiling type
rank: 1000
is_a: core field
slot_uri: MIXS:0000784
multivalued: false
alias: ceil_type
domain_of:
- Biosample
range: ceil_type_enum

```
</details>