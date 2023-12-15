# Slot: depth (depth)


_The vertical distance below local surface, e.g. for sediment or soil samples depth is measured from sediment or soil surface, respectively. Depth can be reported as an interval for subsurface samples._



URI: [MIXS:0000018](https://w3id.org/mixs/0000018)




## Inheritance

* [environment_field](environment_field.md)
    * **depth**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* depth




## Examples

| Value |
| --- |
| 10 meter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: depth
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
description: The vertical distance below local surface, e.g. for sediment or soil
  samples depth is measured from sediment or soil surface, respectively. Depth can
  be reported as an interval for subsurface samples.
title: depth
examples:
- value: 10 meter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- depth
rank: 1000
is_a: environment field
slot_uri: MIXS:0000018
multivalued: false
alias: depth
domain_of:
- Biosample
range: QuantityValue

```
</details>