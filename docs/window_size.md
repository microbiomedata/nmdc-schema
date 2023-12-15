# Slot: window area/size (window_size)


_The window's length and width_



URI: [MIXS:0000224](https://w3id.org/mixs/0000224)




## Inheritance

* [core_field](core_field.md)
    * **window_size**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* window area/size




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | inch, meter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: window_size
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: inch, meter
  occurrence:
    tag: occurrence
    value: '1'
description: The window's length and width
title: window area/size
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- window area/size
rank: 1000
is_a: core field
string_serialization: '{float} {unit} x {float} {unit}'
slot_uri: MIXS:0000224
multivalued: false
alias: window_size
domain_of:
- Biosample
range: TextValue

```
</details>