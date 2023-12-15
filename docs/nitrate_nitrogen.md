# Slot: nitrate_nitrogen (nitrate_nitrogen)


_Concentration of nitrate nitrogen in the sample_



URI: [nmdc:nitrate_nitrogen](https://w3id.org/nmdc/nitrate_nitrogen)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* nitrate_nitrogen
* NO3-N




## Examples

| Value |
| --- |
| 0.29 mg/kg |

## Comments

* often below some specified limit of detection

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
name: nitrate_nitrogen
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
description: Concentration of nitrate nitrogen in the sample
title: nitrate_nitrogen
comments:
- often below some specified limit of detection
examples:
- value: 0.29 mg/kg
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- https://www.ornl.gov/content/bio-scales-0
aliases:
- nitrate_nitrogen
- NO3-N
rank: 1000
alias: nitrate_nitrogen
domain_of:
- Biosample
range: QuantityValue

```
</details>