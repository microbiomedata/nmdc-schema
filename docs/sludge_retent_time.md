# Slot: sludge retention time (sludge_retent_time)


_The time activated sludge remains in reactor_



URI: [MIXS:0000669](https://w3id.org/mixs/0000669)




## Inheritance

* [core_field](core_field.md)
    * **sludge_retent_time**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* sludge retention time




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | hours || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: sludge_retent_time
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: hours
  occurrence:
    tag: occurrence
    value: '1'
description: The time activated sludge remains in reactor
title: sludge retention time
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- sludge retention time
rank: 1000
is_a: core field
slot_uri: MIXS:0000669
multivalued: false
alias: sludge_retent_time
domain_of:
- Biosample
range: QuantityValue

```
</details>