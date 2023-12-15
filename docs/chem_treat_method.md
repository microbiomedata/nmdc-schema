# Slot: chemical treatment method (chem_treat_method)


_Method of chemical administration(dose, frequency, duration, time elapsed between administration and sampling) (e.g. 50 mg/l; twice a week; 1 hr; 0 days)_



URI: [MIXS:0000457](https://w3id.org/mixs/0000457)




## Inheritance

* [core_field](core_field.md)
    * **chem_treat_method**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [String](String.md)



## Aliases


* chemical treatment method




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value;frequency;duration;duration || preferred_unit | milligram per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: chem_treat_method
annotations:
  expected_value:
    tag: expected_value
    value: measurement value;frequency;duration;duration
  preferred_unit:
    tag: preferred_unit
    value: milligram per liter
  occurrence:
    tag: occurrence
    value: '1'
description: Method of chemical administration(dose, frequency, duration, time elapsed
  between administration and sampling) (e.g. 50 mg/l; twice a week; 1 hr; 0 days)
title: chemical treatment method
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- chemical treatment method
rank: 1000
is_a: core field
string_serialization: '{float} {unit};{Rn/start_time/end_time/duration};{duration};{duration}'
slot_uri: MIXS:0000457
multivalued: false
alias: chem_treat_method
domain_of:
- Biosample
range: string

```
</details>