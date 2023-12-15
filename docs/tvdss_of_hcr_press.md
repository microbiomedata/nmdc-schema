# Slot: depth (TVDSS) of hydrocarbon resource pressure (tvdss_of_hcr_press)


_True vertical depth subsea (TVDSS) of the hydrocarbon resource where the original pressure was measured (e.g. 1578 m)._



URI: [MIXS:0000397](https://w3id.org/mixs/0000397)




## Inheritance

* [core_field](core_field.md)
    * **tvdss_of_hcr_press**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* depth (TVDSS) of hydrocarbon resource pressure




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
name: tvdss_of_hcr_press
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
  the original pressure was measured (e.g. 1578 m).
title: depth (TVDSS) of hydrocarbon resource pressure
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- depth (TVDSS) of hydrocarbon resource pressure
rank: 1000
is_a: core field
slot_uri: MIXS:0000397
multivalued: false
alias: tvdss_of_hcr_press
domain_of:
- Biosample
range: QuantityValue

```
</details>