# Slot: total organic carbon (tot_org_carb)


_Definition for soil: total organic carbon content of the soil, definition otherwise: total organic carbon content_



URI: [MIXS:0000533](https://w3id.org/mixs/0000533)




## Inheritance

* [core_field](core_field.md)
    * **tot_org_carb**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* total organic carbon




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | gram Carbon per kilogram sample material || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: tot_org_carb
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: gram Carbon per kilogram sample material
  occurrence:
    tag: occurrence
    value: '1'
description: 'Definition for soil: total organic carbon content of the soil, definition
  otherwise: total organic carbon content'
title: total organic carbon
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- total organic carbon
rank: 1000
is_a: core field
slot_uri: MIXS:0000533
multivalued: false
alias: tot_org_carb
domain_of:
- Biosample
range: QuantityValue

```
</details>