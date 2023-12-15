# Slot: isotope exposure/addition (isotope_exposure)


_List isotope exposure or addition applied to your sample._



URI: [nmdc:isotope_exposure](https://w3id.org/nmdc/isotope_exposure)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [String](String.md)

* Recommended: True






## Examples

| Value |
| --- |
| 13C glucose |
| H218O |

## Comments

* This is required when your experimental design includes the use of isotopically labeled compounds

## TODOs

* Can we make the H218O correctly super and subscripted?

## See Also

* [MIXS:0000751](https://w3id.org/mixs/0000751)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: isotope_exposure
description: List isotope exposure or addition applied to your sample.
title: isotope exposure/addition
todos:
- Can we make the H218O correctly super and subscripted?
comments:
- This is required when your experimental design includes the use of isotopically
  labeled compounds
examples:
- value: 13C glucose
- value: H218O
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- MIXS:0000751
rank: 16
string_serialization: '{termLabel} {[termID]}; {timestamp}'
alias: isotope_exposure
domain_of:
- Biosample
slot_group: MIxS Inspired
range: string
recommended: true

```
</details>