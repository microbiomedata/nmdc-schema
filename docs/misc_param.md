# Slot: miscellaneous parameter (misc_param)


_Any other measurement performed or parameter collected, that is not listed here_



URI: [MIXS:0000752](https://w3id.org/mixs/0000752)




## Inheritance

* [core_field](core_field.md)
    * **misc_param**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* miscellaneous parameter




## Examples

| Value |
| --- |
| Bicarbonate ion concentration;2075 micromole per kilogram |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | parameter name;measurement value || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: misc_param
annotations:
  expected_value:
    tag: expected_value
    value: parameter name;measurement value
  occurrence:
    tag: occurrence
    value: m
description: Any other measurement performed or parameter collected, that is not listed
  here
title: miscellaneous parameter
examples:
- value: Bicarbonate ion concentration;2075 micromole per kilogram
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- miscellaneous parameter
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000752
multivalued: true
alias: misc_param
domain_of:
- Biosample
range: TextValue

```
</details>