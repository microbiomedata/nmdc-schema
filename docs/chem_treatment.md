# Slot: chemical treatment (chem_treatment)


_List of chemical compounds administered upstream the sampling location where sampling occurred (e.g. Glycols, H2S scavenger, corrosion and scale inhibitors, demulsifiers, and other production chemicals etc.). The commercial name of the product and name of the supplier should be provided. The date of administration should also be included_



URI: [MIXS:0001012](https://w3id.org/mixs/0001012)




## Inheritance

* [core_field](core_field.md)
    * **chem_treatment**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* chemical treatment




## Examples

| Value |
| --- |
| ACCENT 1125;DOW;2010-11-17 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | name;name;timestamp || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: chem_treatment
annotations:
  expected_value:
    tag: expected_value
    value: name;name;timestamp
  occurrence:
    tag: occurrence
    value: '1'
description: List of chemical compounds administered upstream the sampling location
  where sampling occurred (e.g. Glycols, H2S scavenger, corrosion and scale inhibitors,
  demulsifiers, and other production chemicals etc.). The commercial name of the product
  and name of the supplier should be provided. The date of administration should also
  be included
title: chemical treatment
examples:
- value: ACCENT 1125;DOW;2010-11-17
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- chemical treatment
rank: 1000
is_a: core field
string_serialization: '{text};{text};{timestamp}'
slot_uri: MIXS:0001012
multivalued: false
alias: chem_treatment
domain_of:
- Biosample
range: TextValue

```
</details>