# Slot: depth (TVDSS) of hydrocarbon resource temperature (tvdss_of_hcr_temp)


_True vertical depth subsea (TVDSS) of the hydrocarbon resource where the original temperature was measured (e.g. 1345 m)._



URI: [MIXS:0000394](https://w3id.org/mixs/0000394)




## Inheritance

* [core_field](core_field.md)
    * **tvdss_of_hcr_temp**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* depth (TVDSS) of hydrocarbon resource temperature




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | meter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: tvdss_of_hcr_temp
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: meter
  occurrence:
    tag: occurrence
    value: '1'
description: True vertical depth subsea (TVDSS) of the hydrocarbon resource where
  the original temperature was measured (e.g. 1345 m).
title: depth (TVDSS) of hydrocarbon resource temperature
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- depth (TVDSS) of hydrocarbon resource temperature
rank: 1000
is_a: core field
slot_uri: MIXS:0000394
multivalued: false
alias: tvdss_of_hcr_temp
domain_of:
- Biosample
range: QuantityValue

```
</details>