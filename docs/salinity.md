# Slot: salinity (salinity)


_The total concentration of all dissolved salts in a liquid or solid sample. While salinity can be measured by a complete chemical analysis, this method is difficult and time consuming. More often, it is instead derived from the conductivity measurement. This is known as practical salinity. These derivations compare the specific conductance of the sample to a salinity standard such as seawater._



URI: [MIXS:0000183](https://w3id.org/mixs/0000183)




## Inheritance

* [core_field](core_field.md)
    * **salinity**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* salinity




## Examples

| Value |
| --- |
| 25 practical salinity unit |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | practical salinity unit, percentage || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: salinity
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: practical salinity unit, percentage
  occurrence:
    tag: occurrence
    value: '1'
description: The total concentration of all dissolved salts in a liquid or solid sample.
  While salinity can be measured by a complete chemical analysis, this method is difficult
  and time consuming. More often, it is instead derived from the conductivity measurement.
  This is known as practical salinity. These derivations compare the specific conductance
  of the sample to a salinity standard such as seawater.
title: salinity
examples:
- value: 25 practical salinity unit
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- salinity
rank: 1000
is_a: core field
slot_uri: MIXS:0000183
multivalued: false
alias: salinity
domain_of:
- Biosample
range: QuantityValue

```
</details>