# Slot: current vegetation (cur_vegetation)


_Vegetation classification from one or more standard classification systems, or agricultural crop_



URI: [MIXS:0000312](https://w3id.org/mixs/0000312)




## Inheritance

* [core_field](core_field.md)
    * **cur_vegetation**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FieldResearchSite](FieldResearchSite.md) | A site, outside of a laboratory, from which biosamples may be collected |  no  |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* current vegetation




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | current vegetation type || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: cur_vegetation
annotations:
  expected_value:
    tag: expected_value
    value: current vegetation type
  occurrence:
    tag: occurrence
    value: '1'
description: Vegetation classification from one or more standard classification systems,
  or agricultural crop
title: current vegetation
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- current vegetation
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000312
multivalued: false
alias: cur_vegetation
domain_of:
- FieldResearchSite
- Biosample
range: TextValue

```
</details>