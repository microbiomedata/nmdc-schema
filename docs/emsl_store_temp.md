# Slot: EMSL sample storage temperature, deg. C (emsl_store_temp)


_The temperature at which the sample should be stored upon delivery to EMSL_



URI: [nmdc:emsl_store_temp](https://w3id.org/nmdc/emsl_store_temp)



<!-- no inheritance hierarchy -->







## Properties

* Range: [String](String.md)

* Recommended: True






## Examples

| Value |
| --- |
| -80 |

## Comments

* Enter a temperature in celsius. Numeric portion only.

## TODOs

* add 'see_alsos' with link to NEXUS info

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: emsl_store_temp
description: The temperature at which the sample should be stored upon delivery to
  EMSL
title: EMSL sample storage temperature, deg. C
todos:
- add 'see_alsos' with link to NEXUS info
comments:
- Enter a temperature in celsius. Numeric portion only.
examples:
- value: '-80'
from_schema: https://w3id.org/nmdc/nmdc
rank: 4
string_serialization: '{float}'
alias: emsl_store_temp
slot_group: EMSL
range: string
recommended: true

```
</details>