# Slot: lime buffer capacity (after 5 day incubation) (lbceq)


_lime buffer capacity, determined at equilibrium after 5 day incubation_



URI: [nmdc:lbceq](https://w3id.org/nmdc/lbceq)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* lbceq
* lime buffer capacity (at 5-day equilibrium)




## Examples

| Value |
| --- |
| 1575 mg/kg |

## Comments

* This is the mass of lime, in mg, needed to raise the pH of one kg of soil by one pH unit

## See Also

* [https://www.ornl.gov/content/bio-scales-0](https://www.ornl.gov/content/bio-scales-0)

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | ppm CaCO3/pH || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: lbceq
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: ppm CaCO3/pH
  occurrence:
    tag: occurrence
    value: '1'
description: lime buffer capacity, determined at equilibrium after 5 day incubation
title: lime buffer capacity (after 5 day incubation)
comments:
- This is the mass of lime, in mg, needed to raise the pH of one kg of soil by one
  pH unit
examples:
- value: 1575 mg/kg
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- https://www.ornl.gov/content/bio-scales-0
aliases:
- lbceq
- lime buffer capacity (at 5-day equilibrium)
rank: 1000
alias: lbceq
domain_of:
- Biosample
range: QuantityValue

```
</details>