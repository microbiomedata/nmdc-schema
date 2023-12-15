# Slot: ecosystem_subtype


_Ecosystem subtypes represent further subdivision of Ecosystem types into more distinct subtypes. Ecosystem subtype is in position 4/5 in a GOLD path._



URI: [nmdc:ecosystem_subtype](https://w3id.org/nmdc/ecosystem_subtype)




## Inheritance

* [gold_path_field](gold_path_field.md)
    * **ecosystem_subtype**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |
[Study](Study.md) | A study summarizes the overall goal of a research initiative and outlines the... |  no  |







## Properties

* Range: [String](String.md)





## Comments

* Ecosystem Type Marine (Environmental -> Aquatic -> Marine) is further divided (for example) into Intertidal zone, Coastal, Pelagic, Intertidal zone etc. in the Ecosystem subtype category.

## See Also

* [https://gold.jgi.doe.gov/help](https://gold.jgi.doe.gov/help)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: ecosystem_subtype
description: Ecosystem subtypes represent further subdivision of Ecosystem types into
  more distinct subtypes. Ecosystem subtype is in position 4/5 in a GOLD path.
comments:
- Ecosystem Type Marine (Environmental -> Aquatic -> Marine) is further divided (for
  example) into Intertidal zone, Coastal, Pelagic, Intertidal zone etc. in the Ecosystem
  subtype category.
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- https://gold.jgi.doe.gov/help
rank: 1000
is_a: gold_path_field
alias: ecosystem_subtype
domain_of:
- Biosample
- Study
range: string

```
</details>