# Slot: bulk electrical conductivity (bulk_elect_conductivity)


_Electrical conductivity is a measure of the ability to carry electric current, which is mostly dictated by the chemistry of and amount of water._



URI: [nmdc:bulk_elect_conductivity](https://w3id.org/nmdc/bulk_elect_conductivity)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)






## Examples

| Value |
| --- |
| JsonObj(has_raw_value='0.017 mS/cm', has_numeric_value=0.017, has_unit='mS/cm') |

## Comments

* Provide the value output of the field instrument.

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: bulk_elect_conductivity
description: Electrical conductivity is a measure of the ability to carry electric
  current, which is mostly dictated by the chemistry of and amount of water.
title: bulk electrical conductivity
comments:
- Provide the value output of the field instrument.
examples:
- value: JsonObj(has_raw_value='0.017 mS/cm', has_numeric_value=0.017, has_unit='mS/cm')
  description: The conductivity measurement was 0.017 millisiemens per centimeter.
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
alias: bulk_elect_conductivity
domain_of:
- Biosample
range: QuantityValue

```
</details>