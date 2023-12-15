# Slot: nitrite_nitrogen (nitrite_nitrogen)


_Concentration of nitrite nitrogen in the sample_



URI: [nmdc:nitrite_nitrogen](https://w3id.org/nmdc/nitrite_nitrogen)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* nitrite_nitrogen
* NO2-N




## Examples

| Value |
| --- |
| 1.2 mg/kg |

## See Also

* [https://www.ornl.gov/content/bio-scales-0](https://www.ornl.gov/content/bio-scales-0)

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | mg/kg || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: nitrite_nitrogen
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: mg/kg
  occurrence:
    tag: occurrence
    value: '1'
description: Concentration of nitrite nitrogen in the sample
title: nitrite_nitrogen
examples:
- value: 1.2 mg/kg
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- https://www.ornl.gov/content/bio-scales-0
aliases:
- nitrite_nitrogen
- NO2-N
rank: 1000
alias: nitrite_nitrogen
domain_of:
- Biosample
range: QuantityValue

```
</details>