# Slot: incubation start time, GMT (start_time_inc)


_Time the incubation was started. Only relevant for incubation samples._



URI: [nmdc:start_time_inc](https://w3id.org/nmdc/start_time_inc)



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
| 13:33 or 13:33:55 |

## Comments

* Time should be entered as HH:MM(:SS) in GMT. See here for a converter: https://www.worldtimebuddy.com/pst-to-gmt-converter

## See Also

* [MIXS:0000011](https://w3id.org/mixs/0000011)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: start_time_inc
description: Time the incubation was started. Only relevant for incubation samples.
title: incubation start time, GMT
notes:
- MIxS collection_date accepts (truncated) ISO8601. DH taking seconds optional time
  only
comments:
- 'Time should be entered as HH:MM(:SS) in GMT. See here for a converter: https://www.worldtimebuddy.com/pst-to-gmt-converter'
examples:
- value: 13:33 or 13:33:55
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- MIXS:0000011
rank: 5
string_serialization: '{time, seconds optional}'
alias: start_time_inc
domain_of:
- Biosample
slot_group: MIxS Inspired
range: string
recommended: true

```
</details>