# Slot: rooting medium carbon (root_med_carbon)


_Source of organic carbon in the culture rooting medium; e.g. sucrose._



URI: [MIXS:0000577](https://w3id.org/mixs/0000577)




## Inheritance

* [core_field](core_field.md)
    * **root_med_carbon**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* rooting medium carbon




## Examples

| Value |
| --- |
| sucrose |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | carbon source name;measurement value || preferred_unit | milligram per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: root_med_carbon
annotations:
  expected_value:
    tag: expected_value
    value: carbon source name;measurement value
  preferred_unit:
    tag: preferred_unit
    value: milligram per liter
  occurrence:
    tag: occurrence
    value: '1'
description: Source of organic carbon in the culture rooting medium; e.g. sucrose.
title: rooting medium carbon
examples:
- value: sucrose
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- rooting medium carbon
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000577
multivalued: false
alias: root_med_carbon
domain_of:
- Biosample
range: TextValue

```
</details>