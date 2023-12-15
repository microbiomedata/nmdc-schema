# Slot: funding_sources


_A list of organizations, along with the award numbers, that underwrite financial support for projects of  a particular type. Typically, they process applications and award funds to the chosen qualified  applicants._



URI: [nmdc:funding_sources](https://w3id.org/nmdc/funding_sources)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Study](Study.md) | A study summarizes the overall goal of a research initiative and outlines the... |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| National Sciences Foundation Dimensions of Biodiversity (award no. 1342701) |
| U.S. Department of Energy, Office of Science, Office of Biological and Environmental Research  (BER) under contract DE-AC05-00OR2275 |

## Comments

* Include only the name of the funding organization and the award or contract number.

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: funding_sources
description: A list of organizations, along with the award numbers, that underwrite
  financial support for projects of  a particular type. Typically, they process applications
  and award funds to the chosen qualified  applicants.
comments:
- Include only the name of the funding organization and the award or contract number.
examples:
- value: National Sciences Foundation Dimensions of Biodiversity (award no. 1342701)
- value: U.S. Department of Energy, Office of Science, Office of Biological and Environmental
    Research  (BER) under contract DE-AC05-00OR2275
from_schema: https://w3id.org/nmdc/nmdc
close_mappings:
- NCIT:C39409
rank: 1000
multivalued: true
alias: funding_sources
domain_of:
- Study
range: string

```
</details>