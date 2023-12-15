# Slot: oil water contact depth (owc_tvdss)


_Depth of the original oil water contact (OWC) zone (average) (m TVDSS)_



URI: [MIXS:0000405](https://w3id.org/mixs/0000405)




## Inheritance

* [core_field](core_field.md)
    * **owc_tvdss**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* oil water contact depth




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | meter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: owc_tvdss
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: meter
  occurrence:
    tag: occurrence
    value: '1'
description: Depth of the original oil water contact (OWC) zone (average) (m TVDSS)
title: oil water contact depth
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- oil water contact depth
rank: 1000
is_a: core field
slot_uri: MIXS:0000405
multivalued: false
alias: owc_tvdss
domain_of:
- Biosample
range: QuantityValue

```
</details>