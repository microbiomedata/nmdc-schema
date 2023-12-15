# Slot: total inorganic nitrogen (tot_inorg_nitro)


_Total inorganic nitrogen content_



URI: [MIXS:0000745](https://w3id.org/mixs/0000745)




## Inheritance

* [core_field](core_field.md)
    * **tot_inorg_nitro**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* total inorganic nitrogen




## Examples

| Value |
| --- |
| 40 microgram per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | microgram per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: tot_inorg_nitro
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: microgram per liter
  occurrence:
    tag: occurrence
    value: '1'
description: Total inorganic nitrogen content
title: total inorganic nitrogen
examples:
- value: 40 microgram per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- total inorganic nitrogen
rank: 1000
is_a: core field
slot_uri: MIXS:0000745
multivalued: false
alias: tot_inorg_nitro
domain_of:
- Biosample
range: QuantityValue

```
</details>