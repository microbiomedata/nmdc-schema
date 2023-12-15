# Slot: biotic regimen (biotic_regm)


_Information about treatment(s) involving use of biotic factors, such as bacteria, viruses or fungi._



URI: [MIXS:0001038](https://w3id.org/mixs/0001038)




## Inheritance

* [core_field](core_field.md)
    * **biotic_regm**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* biotic regimen




## Examples

| Value |
| --- |
| sample inoculated with Rhizobium spp. Culture |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | free text || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: biotic_regm
annotations:
  expected_value:
    tag: expected_value
    value: free text
  occurrence:
    tag: occurrence
    value: '1'
description: Information about treatment(s) involving use of biotic factors, such
  as bacteria, viruses or fungi.
title: biotic regimen
examples:
- value: sample inoculated with Rhizobium spp. Culture
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- biotic regimen
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0001038
multivalued: false
alias: biotic_regm
domain_of:
- Biosample
range: TextValue

```
</details>