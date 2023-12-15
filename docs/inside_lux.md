# Slot: inside lux light (inside_lux)


_The recorded value at sampling time (power density)_



URI: [MIXS:0000168](https://w3id.org/mixs/0000168)




## Inheritance

* [core_field](core_field.md)
    * **inside_lux**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* inside lux light




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | kilowatt per square metre || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: inside_lux
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: kilowatt per square metre
  occurrence:
    tag: occurrence
    value: '1'
description: The recorded value at sampling time (power density)
title: inside lux light
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- inside lux light
rank: 1000
is_a: core field
slot_uri: MIXS:0000168
multivalued: false
alias: inside_lux
domain_of:
- Biosample
range: QuantityValue

```
</details>