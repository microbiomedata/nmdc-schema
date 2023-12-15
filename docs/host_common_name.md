# Slot: host common name (host_common_name)


_Common name of the host._



URI: [MIXS:0000248](https://w3id.org/mixs/0000248)




## Inheritance

* [core_field](core_field.md)
    * **host_common_name**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* host common name




## Examples

| Value |
| --- |
| human |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | common name || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: host_common_name
annotations:
  expected_value:
    tag: expected_value
    value: common name
  occurrence:
    tag: occurrence
    value: '1'
description: Common name of the host.
title: host common name
examples:
- value: human
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- host common name
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000248
multivalued: false
alias: host_common_name
domain_of:
- Biosample
range: TextValue

```
</details>