# Slot: plant product (plant_product)


_Substance produced by the plant, where the sample was obtained from_



URI: [MIXS:0001058](https://w3id.org/mixs/0001058)




## Inheritance

* [core_field](core_field.md)
    * **plant_product**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* plant product




## Examples

| Value |
| --- |
| xylem sap [PO:0025539] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | product name || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: plant_product
annotations:
  expected_value:
    tag: expected_value
    value: product name
  occurrence:
    tag: occurrence
    value: '1'
description: Substance produced by the plant, where the sample was obtained from
title: plant product
examples:
- value: xylem sap [PO:0025539]
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- plant product
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0001058
multivalued: false
alias: plant_product
domain_of:
- Biosample
range: TextValue

```
</details>