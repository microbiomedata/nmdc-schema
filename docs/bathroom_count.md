# Slot: bathroom count (bathroom_count)


_The number of bathrooms in the building_



URI: [MIXS:0000776](https://w3id.org/mixs/0000776)




## Inheritance

* [core_field](core_field.md)
    * **bathroom_count**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* bathroom count




## Examples

| Value |
| --- |
| 1 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | value || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: bathroom_count
annotations:
  expected_value:
    tag: expected_value
    value: value
  occurrence:
    tag: occurrence
    value: '1'
description: The number of bathrooms in the building
title: bathroom count
examples:
- value: '1'
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- bathroom count
rank: 1000
is_a: core field
slot_uri: MIXS:0000776
multivalued: false
alias: bathroom_count
domain_of:
- Biosample
range: TextValue

```
</details>