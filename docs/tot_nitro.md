# Slot: total nitrogen concentration (tot_nitro)


_Total nitrogen concentration of water samples, calculated by: total nitrogen = total dissolved nitrogen + particulate nitrogen. Can also be measured without filtering, reported as nitrogen_



URI: [MIXS:0000102](https://w3id.org/mixs/0000102)




## Inheritance

* [core_field](core_field.md)
    * **tot_nitro**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* total nitrogen concentration




## Examples

| Value |
| --- |
| 50 micromole per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | microgram per liter, micromole per liter, milligram per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: tot_nitro
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: microgram per liter, micromole per liter, milligram per liter
  occurrence:
    tag: occurrence
    value: '1'
description: 'Total nitrogen concentration of water samples, calculated by: total
  nitrogen = total dissolved nitrogen + particulate nitrogen. Can also be measured
  without filtering, reported as nitrogen'
title: total nitrogen concentration
examples:
- value: 50 micromole per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- total nitrogen concentration
rank: 1000
is_a: core field
slot_uri: MIXS:0000102
multivalued: false
alias: tot_nitro
domain_of:
- Biosample
range: QuantityValue

```
</details>