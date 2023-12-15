# Slot: ventilation type (ventilation_type)


_Ventilation system used in the sampled premises_



URI: [MIXS:0000756](https://w3id.org/mixs/0000756)




## Inheritance

* [core_field](core_field.md)
    * **ventilation_type**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* ventilation type




## Examples

| Value |
| --- |
| Operable windows |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | ventilation type name || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: ventilation_type
annotations:
  expected_value:
    tag: expected_value
    value: ventilation type name
  occurrence:
    tag: occurrence
    value: '1'
description: Ventilation system used in the sampled premises
title: ventilation type
examples:
- value: Operable windows
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- ventilation type
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000756
multivalued: false
alias: ventilation_type
domain_of:
- Biosample
range: TextValue

```
</details>