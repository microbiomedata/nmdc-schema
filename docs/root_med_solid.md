# Slot: rooting medium solidifier (root_med_solid)


_Specification of the solidifying agent in the culture rooting medium; e.g. agar._



URI: [MIXS:0001063](https://w3id.org/mixs/0001063)




## Inheritance

* [core_field](core_field.md)
    * **root_med_solid**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* rooting medium solidifier




## Examples

| Value |
| --- |
| agar |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | name || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: root_med_solid
annotations:
  expected_value:
    tag: expected_value
    value: name
  occurrence:
    tag: occurrence
    value: '1'
description: Specification of the solidifying agent in the culture rooting medium;
  e.g. agar.
title: rooting medium solidifier
examples:
- value: agar
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- rooting medium solidifier
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0001063
multivalued: false
alias: root_med_solid
domain_of:
- Biosample
range: TextValue

```
</details>