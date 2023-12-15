# Slot: organic nitrogen method (org_nitro_method)


_Method used for obtaining organic nitrogen_



URI: [nmdc:org_nitro_method](https://w3id.org/nmdc/org_nitro_method)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| https://doi.org/10.1016/0038-0717(85)90144-0 |

## Comments

* required if "org_nitro" is provided

## See Also

* [MIXS:0000338](https://w3id.org/mixs/0000338)
* [MIXS:0000205](https://w3id.org/mixs/0000205)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: org_nitro_method
description: Method used for obtaining organic nitrogen
title: organic nitrogen method
comments:
- required if "org_nitro" is provided
examples:
- value: https://doi.org/10.1016/0038-0717(85)90144-0
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- MIXS:0000338
- MIXS:0000205
rank: 14
string_serialization: '{PMID}|{DOI}|{URL}'
alias: org_nitro_method
domain_of:
- Biosample
slot_group: MIxS Inspired
range: string

```
</details>