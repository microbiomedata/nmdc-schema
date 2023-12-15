# Slot: composite design/sieving (sieving)


_Collection design of pooled samples and/or sieve size and amount of sample sieved_



URI: [MIXS:0000322](https://w3id.org/mixs/0000322)




## Inheritance

* [core_field](core_field.md)
    * **sieving**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* composite design/sieving




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | design name and/or size;amount || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: sieving
annotations:
  expected_value:
    tag: expected_value
    value: design name and/or size;amount
  occurrence:
    tag: occurrence
    value: '1'
description: Collection design of pooled samples and/or sieve size and amount of sample
  sieved
title: composite design/sieving
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- composite design/sieving
rank: 1000
is_a: core field
string_serialization: '{{text}|{float} {unit}};{float} {unit}'
slot_uri: MIXS:0000322
multivalued: false
alias: sieving
domain_of:
- Biosample
range: TextValue

```
</details>