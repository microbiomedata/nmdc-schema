# Slot: heating system delivery method (heat_sys_deliv_meth)


_The method by which the heat is delivered through the system_



URI: [MIXS:0000812](https://w3id.org/mixs/0000812)




## Inheritance

* [core_field](core_field.md)
    * **heat_sys_deliv_meth**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [String](String.md)



## Aliases


* heating system delivery method




## Examples

| Value |
| --- |
| radiant |

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
name: heat_sys_deliv_meth
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The method by which the heat is delivered through the system
title: heating system delivery method
examples:
- value: radiant
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- heating system delivery method
rank: 1000
is_a: core field
string_serialization: '[conductive|radiant]'
slot_uri: MIXS:0000812
multivalued: false
alias: heat_sys_deliv_meth
domain_of:
- Biosample
range: string

```
</details>