# Slot: sample storage duration (samp_store_dur)


_Duration for which the sample was stored_



URI: [MIXS:0000116](https://w3id.org/mixs/0000116)




## Inheritance

* [core_field](core_field.md)
    * **samp_store_dur**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* sample storage duration




## Examples

| Value |
| --- |
| P1Y6M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | duration || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: samp_store_dur
annotations:
  expected_value:
    tag: expected_value
    value: duration
  occurrence:
    tag: occurrence
    value: '1'
description: Duration for which the sample was stored
title: sample storage duration
examples:
- value: P1Y6M
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- sample storage duration
rank: 1000
is_a: core field
string_serialization: '{duration}'
slot_uri: MIXS:0000116
multivalued: false
alias: samp_store_dur
domain_of:
- Biosample
range: TextValue

```
</details>