# Slot: other treatments (other_treatment)


_Other treatments applied to your samples that are not applicable to the provided fields_



URI: [nmdc:other_treatment](https://w3id.org/nmdc/other_treatment)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [String](String.md)

* Recommended: True





## Comments

* This is an open text field to provide any treatments that cannot be captured in the provided slots.

## See Also

* [MIXS:0000300](https://w3id.org/mixs/0000300)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: other_treatment
description: Other treatments applied to your samples that are not applicable to the
  provided fields
title: other treatments
notes:
- Values entered here will be used to determine potential new slots.
comments:
- This is an open text field to provide any treatments that cannot be captured in
  the provided slots.
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- MIXS:0000300
rank: 15
string_serialization: '{text}'
alias: other_treatment
domain_of:
- Biosample
slot_group: MIxS Inspired
range: string
recommended: true

```
</details>