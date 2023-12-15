# Slot: replicate number (replicate_number)


_If sending biological replicates, indicate the rep number here._



URI: [nmdc:replicate_number](https://w3id.org/nmdc/replicate_number)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [String](String.md)

* Recommended: True





## Comments

* This will guide staff in ensuring your samples are blocked & randomized correctly

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: replicate_number
description: If sending biological replicates, indicate the rep number here.
title: replicate number
comments:
- This will guide staff in ensuring your samples are blocked & randomized correctly
from_schema: https://w3id.org/nmdc/nmdc
rank: 6
string_serialization: '{integer}'
alias: replicate_number
domain_of:
- Biosample
slot_group: EMSL
range: string
recommended: true

```
</details>