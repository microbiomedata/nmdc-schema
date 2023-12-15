# Slot: collection time, GMT (collection_time)


_The time of sampling, either as an instance (single point) or interval._



URI: [nmdc:collection_time](https://w3id.org/nmdc/collection_time)



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
name: collection_time
description: The time of sampling, either as an instance (single point) or interval.
title: collection time, GMT
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
rank: 1
string_serialization: '{time, seconds optional}'
alias: collection_time
domain_of:
- Biosample
slot_group: MIxS Inspired
range: string
recommended: true

```
</details>