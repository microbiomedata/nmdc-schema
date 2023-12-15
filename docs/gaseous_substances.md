# Slot: gaseous substances (gaseous_substances)


_Amount or concentration of substances such as hydrogen sulfide, carbon dioxide, methane, etc.; can include multiple substances_



URI: [MIXS:0000661](https://w3id.org/mixs/0000661)




## Inheritance

* [core_field](core_field.md)
    * **gaseous_substances**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* gaseous substances




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | gaseous substance name;measurement value || preferred_unit | micromole per liter || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: gaseous_substances
annotations:
  expected_value:
    tag: expected_value
    value: gaseous substance name;measurement value
  preferred_unit:
    tag: preferred_unit
    value: micromole per liter
  occurrence:
    tag: occurrence
    value: m
description: Amount or concentration of substances such as hydrogen sulfide, carbon
  dioxide, methane, etc.; can include multiple substances
title: gaseous substances
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- gaseous substances
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000661
multivalued: true
alias: gaseous_substances
domain_of:
- Biosample
range: TextValue

```
</details>