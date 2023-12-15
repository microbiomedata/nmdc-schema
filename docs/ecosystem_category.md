# Slot: ecosystem_category


_Ecosystem categories represent divisions within the ecosystem based on specific characteristics of the environment from where an organism or sample is isolated. Ecosystem category is in position 2/5 in a GOLD path._



URI: [nmdc:ecosystem_category](https://w3id.org/nmdc/ecosystem_category)




## Inheritance

* [gold_path_field](gold_path_field.md)
    * **ecosystem_category**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |
[Study](Study.md) | A study summarizes the overall goal of a research initiative and outlines the... |  no  |







## Properties

* Range: [String](String.md)





## Comments

* The Environmental ecosystem (for example) is divided into Air, Aquatic and Terrestrial. Ecosystem categories for Host-associated samples can be individual hosts or phyla and for engineered samples it may be manipulated environments like bioreactors, solid waste etc.

## See Also

* [https://gold.jgi.doe.gov/help](https://gold.jgi.doe.gov/help)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: ecosystem_category
description: Ecosystem categories represent divisions within the ecosystem based on
  specific characteristics of the environment from where an organism or sample is
  isolated. Ecosystem category is in position 2/5 in a GOLD path.
comments:
- The Environmental ecosystem (for example) is divided into Air, Aquatic and Terrestrial.
  Ecosystem categories for Host-associated samples can be individual hosts or phyla
  and for engineered samples it may be manipulated environments like bioreactors,
  solid waste etc.
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- https://gold.jgi.doe.gov/help
rank: 1000
is_a: gold_path_field
alias: ecosystem_category
domain_of:
- Biosample
- Study
range: string

```
</details>