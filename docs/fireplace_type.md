# Slot: fireplace type (fireplace_type)


_A firebox with chimney_



URI: [MIXS:0000802](https://w3id.org/mixs/0000802)




## Inheritance

* [core_field](core_field.md)
    * **fireplace_type**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* fireplace type




## Examples

| Value |
| --- |
| wood burning |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | enumeration || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: fireplace_type
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: A firebox with chimney
title: fireplace type
examples:
- value: wood burning
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- fireplace type
rank: 1000
is_a: core field
string_serialization: '[gas burning|wood burning]'
slot_uri: MIXS:0000802
multivalued: false
alias: fireplace_type
domain_of:
- Biosample
range: TextValue

```
</details>