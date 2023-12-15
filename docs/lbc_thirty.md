# Slot: lime buffer capacity (at 30 minutes) (lbc_thirty)


_lime buffer capacity, determined after 30 minute incubation_



URI: [nmdc:lbc_thirty](https://w3id.org/nmdc/lbc_thirty)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* lbc_thirty
* lbc30
* lime buffer capacity (at 30 minutes)




## Examples

| Value |
| --- |
| 543 mg/kg |

## Comments

* This is the mass of lime, in mg, needed to raise the pH of one kg of soil by one pH unit

## See Also

* [https://www.ornl.gov/content/bio-scales-0](https://www.ornl.gov/content/bio-scales-0)
* [https://secure.caes.uga.edu/extension/publications/files/pdf/C%20874_5.PDF](https://secure.caes.uga.edu/extension/publications/files/pdf/C%20874_5.PDF)

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
name: lbc_thirty
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
description: lime buffer capacity, determined after 30 minute incubation
title: lime buffer capacity (at 30 minutes)
comments:
- This is the mass of lime, in mg, needed to raise the pH of one kg of soil by one
  pH unit
examples:
- value: 543 mg/kg
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- https://www.ornl.gov/content/bio-scales-0
- https://secure.caes.uga.edu/extension/publications/files/pdf/C%20874_5.PDF
aliases:
- lbc_thirty
- lbc30
- lime buffer capacity (at 30 minutes)
rank: 1000
alias: lbc_thirty
domain_of:
- Biosample
range: QuantityValue

```
</details>