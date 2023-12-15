# Slot: train line (train_line)


_The subway line name_



URI: [MIXS:0000837](https://w3id.org/mixs/0000837)




## Inheritance

* [core_field](core_field.md)
    * **train_line**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TrainLineEnum](TrainLineEnum.md)



## Aliases


* train line




## Examples

| Value |
| --- |
| red |

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
name: train_line
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The subway line name
title: train line
examples:
- value: red
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- train line
rank: 1000
is_a: core field
slot_uri: MIXS:0000837
multivalued: false
alias: train_line
domain_of:
- Biosample
range: train_line_enum

```
</details>