# Slot: incubation start date (start_date_inc)


_Date the incubation was started. Only relevant for incubation samples._



URI: [nmdc:start_date_inc](https://w3id.org/nmdc/start_date_inc)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [String](String.md)

* Recommended: True






## Examples

| Value |
| --- |
| 2021-04-15, 2021-04 and 2021 are all acceptable. |

## Comments

* Date should be formatted as YYYY(-MM(-DD)). Ie, 2021-04-15, 2021-04 and 2021 are all acceptable.

## See Also

* [MIXS:0000011](https://w3id.org/mixs/0000011)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: start_date_inc
description: Date the incubation was started. Only relevant for incubation samples.
title: incubation start date
notes:
- MIxS collection_date accepts (truncated) ISO8601. DH taking arbitrary precision
  date only
comments:
- Date should be formatted as YYYY(-MM(-DD)). Ie, 2021-04-15, 2021-04 and 2021 are
  all acceptable.
examples:
- value: 2021-04-15, 2021-04 and 2021 are all acceptable.
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- MIXS:0000011
rank: 4
string_serialization: '{date, arbitrary precision}'
alias: start_date_inc
domain_of:
- Biosample
slot_group: MIxS Inspired
range: string
recommended: true

```
</details>