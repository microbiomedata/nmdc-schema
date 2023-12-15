# Slot: biocide administration method (biocide_admin_method)


_Method of biocide administration (dose, frequency, duration, time elapsed between last biociding and sampling) (e.g. 150 mg/l; weekly; 4 hr; 3 days)_



URI: [MIXS:0000456](https://w3id.org/mixs/0000456)




## Inheritance

* [core_field](core_field.md)
    * **biocide_admin_method**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* biocide administration method




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
name: biocide_admin_method
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
description: Method of biocide administration (dose, frequency, duration, time elapsed
  between last biociding and sampling) (e.g. 150 mg/l; weekly; 4 hr; 3 days)
title: biocide administration method
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- biocide administration method
rank: 1000
is_a: core field
string_serialization: '{float} {unit};{Rn/start_time/end_time/duration};{duration}'
slot_uri: MIXS:0000456
multivalued: false
alias: biocide_admin_method
domain_of:
- Biosample
range: TextValue

```
</details>