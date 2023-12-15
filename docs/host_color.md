# Slot: host color (host_color)


_The color of host_



URI: [MIXS:0000260](https://w3id.org/mixs/0000260)




## Inheritance

* [core_field](core_field.md)
    * **host_color**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* host color




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | color || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: host_color
annotations:
  expected_value:
    tag: expected_value
    value: color
  occurrence:
    tag: occurrence
    value: '1'
description: The color of host
title: host color
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- host color
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000260
multivalued: false
alias: host_color
domain_of:
- Biosample
range: TextValue

```
</details>