# Slot: reactor type (reactor_type)


_Anaerobic digesters can be designed and engineered to operate using a number of different process configurations, as batch or continuous, mesophilic, high solid or low solid, and single stage or multistage_



URI: [MIXS:0000350](https://w3id.org/mixs/0000350)




## Inheritance

* [core_field](core_field.md)
    * **reactor_type**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* reactor type




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | reactor type name || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: reactor_type
annotations:
  expected_value:
    tag: expected_value
    value: reactor type name
  occurrence:
    tag: occurrence
    value: '1'
description: Anaerobic digesters can be designed and engineered to operate using a
  number of different process configurations, as batch or continuous, mesophilic,
  high solid or low solid, and single stage or multistage
title: reactor type
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- reactor type
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000350
multivalued: false
alias: reactor_type
domain_of:
- Biosample
range: TextValue

```
</details>