# Slot: ecosystem_type


_Ecosystem types represent things having common characteristics within the Ecosystem Category. These common characteristics based grouping is still broad but specific to the characteristics of a given environment. Ecosystem type is in position 3/5 in a GOLD path._



URI: [nmdc:ecosystem_type](https://w3id.org/nmdc/ecosystem_type)




## Inheritance

* [gold_path_field](gold_path_field.md)
    * **ecosystem_type**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |
[Study](Study.md) | A study summarizes the overall goal of a research initiative and outlines the... |  no  |







## Properties

* Range: [String](String.md)





## Comments

* The Aquatic ecosystem category (for example) may have ecosystem types like Marine or Thermal springs etc. Ecosystem category Air may have Indoor air or Outdoor air as different Ecosystem Types. In the case of Host-associated samples, ecosystem type can represent Respiratory system, Digestive system, Roots etc.

## See Also

* [https://gold.jgi.doe.gov/help](https://gold.jgi.doe.gov/help)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: ecosystem_type
description: Ecosystem types represent things having common characteristics within
  the Ecosystem Category. These common characteristics based grouping is still broad
  but specific to the characteristics of a given environment. Ecosystem type is in
  position 3/5 in a GOLD path.
comments:
- The Aquatic ecosystem category (for example) may have ecosystem types like Marine
  or Thermal springs etc. Ecosystem category Air may have Indoor air or Outdoor air
  as different Ecosystem Types. In the case of Host-associated samples, ecosystem
  type can represent Respiratory system, Digestive system, Roots etc.
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- https://gold.jgi.doe.gov/help
rank: 1000
is_a: gold_path_field
alias: ecosystem_type
domain_of:
- Biosample
- Study
range: string

```
</details>