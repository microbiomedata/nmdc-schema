# Slot: host sex (host_sex)


_Gender or physical sex of the host._



URI: [MIXS:0000811](https://w3id.org/mixs/0000811)




## Inheritance

* [core_field](core_field.md)
    * **host_sex**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [HostSexEnum](HostSexEnum.md)



## Aliases


* host sex




## Examples

| Value |
| --- |
| non-binary |

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
name: host_sex
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: Gender or physical sex of the host.
title: host sex
examples:
- value: non-binary
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- host sex
rank: 1000
is_a: core field
slot_uri: MIXS:0000811
multivalued: false
alias: host_sex
domain_of:
- Biosample
range: host_sex_enum

```
</details>