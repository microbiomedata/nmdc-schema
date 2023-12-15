# Slot: light regimen (light_regm)


_Information about treatment(s) involving exposure to light, including both light intensity and quality._



URI: [MIXS:0000569](https://w3id.org/mixs/0000569)




## Inheritance

* [core_field](core_field.md)
    * **light_regm**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* light regimen




## Examples

| Value |
| --- |
| incandescant light;10 lux;450 nanometer |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | exposure type;light intensity;light quality || preferred_unit | lux; micrometer, nanometer, angstrom || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: light_regm
annotations:
  expected_value:
    tag: expected_value
    value: exposure type;light intensity;light quality
  preferred_unit:
    tag: preferred_unit
    value: lux; micrometer, nanometer, angstrom
  occurrence:
    tag: occurrence
    value: '1'
description: Information about treatment(s) involving exposure to light, including
  both light intensity and quality.
title: light regimen
examples:
- value: incandescant light;10 lux;450 nanometer
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- light regimen
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit};{float} {unit}'
slot_uri: MIXS:0000569
multivalued: false
alias: light_regm
domain_of:
- Biosample
range: TextValue

```
</details>