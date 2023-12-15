# Slot: gravidity (gravidity)


_Whether or not subject is gravid, and if yes date due or date post-conception, specifying which is used_



URI: [MIXS:0000875](https://w3id.org/mixs/0000875)




## Inheritance

* [core_field](core_field.md)
    * **gravidity**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* gravidity




## Examples

| Value |
| --- |
| yes;due date:2018-05-11 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | gravidity status;timestamp || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: gravidity
annotations:
  expected_value:
    tag: expected_value
    value: gravidity status;timestamp
  occurrence:
    tag: occurrence
    value: '1'
description: Whether or not subject is gravid, and if yes date due or date post-conception,
  specifying which is used
title: gravidity
examples:
- value: yes;due date:2018-05-11
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- gravidity
rank: 1000
is_a: core field
string_serialization: '{boolean};{timestamp}'
slot_uri: MIXS:0000875
multivalued: false
alias: gravidity
domain_of:
- Biosample
range: TextValue

```
</details>