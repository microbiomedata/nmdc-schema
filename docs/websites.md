# Slot: websites


_A list of websites that are associated with the entity._



URI: [nmdc:websites](https://w3id.org/nmdc/websites)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Study](Study.md) | A study summarizes the overall goal of a research initiative and outlines the... |  yes  |
[PersonValue](PersonValue.md) | An attribute value representing a person |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True

* Regex pattern: `^[Hh][Tt][Tt][Pp][Ss]?:\/\/(?!.*[Dd][Oo][Ii]\.[Oo][Rr][Gg]).*$`





## Comments

* DOIs should not be included as websites. Instead, use the associated_dois slot.

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: websites
description: A list of websites that are associated with the entity.
comments:
- DOIs should not be included as websites. Instead, use the associated_dois slot.
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
multivalued: true
alias: websites
domain_of:
- Study
- PersonValue
range: string
pattern: ^[Hh][Tt][Tt][Pp][Ss]?:\/\/(?!.*[Dd][Oo][Ii]\.[Oo][Rr][Gg]).*$

```
</details>