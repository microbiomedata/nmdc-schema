# Slot: sample well name (samp_well_name)


_Name of the well (e.g. BXA1123) where sample was taken_



URI: [MIXS:0000296](https://w3id.org/mixs/0000296)




## Inheritance

* [core_field](core_field.md)
    * **samp_well_name**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* sample well name




## Examples

| Value |
| --- |
|  |

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
name: samp_well_name
annotations:
  expected_value:
    tag: expected_value
    value: name
  occurrence:
    tag: occurrence
    value: '1'
description: Name of the well (e.g. BXA1123) where sample was taken
title: sample well name
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- sample well name
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000296
multivalued: false
alias: samp_well_name
domain_of:
- Biosample
range: TextValue

```
</details>