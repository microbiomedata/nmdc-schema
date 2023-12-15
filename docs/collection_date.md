# Slot: collection date (collection_date)


_The time of sampling, either as an instance (single point in time) or interval. In case no exact time is available, the date/time can be right truncated i.e. all of these are valid times: 2008-01-23T19:23:10+00:00; 2008-01-23T19:23:10; 2008-01-23; 2008-01; 2008; Except: 2008-01; 2008 all are ISO8601 compliant_



URI: [MIXS:0000011](https://w3id.org/mixs/0000011)




## Inheritance

* [environment_field](environment_field.md)
    * **collection_date**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TimestampValue](TimestampValue.md)



## Aliases


* collection date




## Examples

| Value |
| --- |
| 2018-05-11T10:00:00+01:00; 2018-05-11 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | date and time |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: collection_date
annotations:
  expected_value:
    tag: expected_value
    value: date and time
description: 'The time of sampling, either as an instance (single point in time) or
  interval. In case no exact time is available, the date/time can be right truncated
  i.e. all of these are valid times: 2008-01-23T19:23:10+00:00; 2008-01-23T19:23:10;
  2008-01-23; 2008-01; 2008; Except: 2008-01; 2008 all are ISO8601 compliant'
title: collection date
examples:
- value: 2018-05-11T10:00:00+01:00; 2018-05-11
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- collection date
rank: 1000
is_a: environment field
slot_uri: MIXS:0000011
multivalued: false
alias: collection_date
domain_of:
- Biosample
range: TimestampValue

```
</details>