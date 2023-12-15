# Slot: secondary and tertiary recovery methods and start date (add_recov_method)


_Additional (i.e. Secondary, tertiary, etc.) recovery methods deployed for increase of hydrocarbon recovery from resource and start date for each one of them. If "other" is specified, please propose entry in "additional info" field_



URI: [MIXS:0001009](https://w3id.org/mixs/0001009)




## Inheritance

* [core_field](core_field.md)
    * **add_recov_method**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* secondary and tertiary recovery methods and start date




## Examples

| Value |
| --- |
| Polymer Addition;2018-06-21T14:30Z |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | enumeration;timestamp || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: add_recov_method
annotations:
  expected_value:
    tag: expected_value
    value: enumeration;timestamp
  occurrence:
    tag: occurrence
    value: '1'
description: Additional (i.e. Secondary, tertiary, etc.) recovery methods deployed
  for increase of hydrocarbon recovery from resource and start date for each one of
  them. If "other" is specified, please propose entry in "additional info" field
title: secondary and tertiary recovery methods and start date
examples:
- value: Polymer Addition;2018-06-21T14:30Z
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- secondary and tertiary recovery methods and start date
rank: 1000
is_a: core field
slot_uri: MIXS:0001009
multivalued: false
alias: add_recov_method
domain_of:
- Biosample
range: TextValue

```
</details>