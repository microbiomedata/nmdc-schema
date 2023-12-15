# Slot: duration


_The elapsed time of an activity._



URI: [nmdc:duration](https://w3id.org/nmdc/duration)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MixingProcess](MixingProcess.md) | The combining of components, particles or layers into a more homogeneous stat... |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)






## Examples

| Value |
| --- |
| JsonObj(has_numeric_value=2, has_unit='hours') |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: duration
description: The elapsed time of an activity.
examples:
- value: JsonObj(has_numeric_value=2, has_unit='hours')
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
domain: PlannedProcess
alias: duration
domain_of:
- MixingProcess
range: QuantityValue

```
</details>