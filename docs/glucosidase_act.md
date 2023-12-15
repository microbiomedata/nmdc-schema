# Slot: glucosidase activity (glucosidase_act)


_Measurement of glucosidase activity_



URI: [MIXS:0000137](https://w3id.org/mixs/0000137)




## Inheritance

* [core_field](core_field.md)
    * **glucosidase_act**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* glucosidase activity




## Examples

| Value |
| --- |
| 5 mol per liter per hour |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | mol per liter per hour || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: glucosidase_act
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: mol per liter per hour
  occurrence:
    tag: occurrence
    value: '1'
description: Measurement of glucosidase activity
title: glucosidase activity
examples:
- value: 5 mol per liter per hour
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- glucosidase activity
rank: 1000
is_a: core field
slot_uri: MIXS:0000137
multivalued: false
alias: glucosidase_act
domain_of:
- Biosample
range: QuantityValue

```
</details>