# Slot: chimera check software (chimera_check)


_Tool(s) used for chimera checking, including version number and parameters, to discover and remove chimeric sequences. A chimeric sequence is comprised of two or more phylogenetically distinct parent sequences._



URI: [MIXS:0000052](https://w3id.org/mixs/0000052)




## Inheritance

* [sequencing_field](sequencing_field.md)
    * **chimera_check**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |
[OmicsProcessing](OmicsProcessing.md) | The methods and processes used to generate omics data from a biosample or org... |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* chimera check software




## Examples

| Value |
| --- |
| uchime;v4.1;default parameters |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | name and version of software, parameters used |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: chimera_check
annotations:
  expected_value:
    tag: expected_value
    value: name and version of software, parameters used
description: Tool(s) used for chimera checking, including version number and parameters,
  to discover and remove chimeric sequences. A chimeric sequence is comprised of two
  or more phylogenetically distinct parent sequences.
title: chimera check software
examples:
- value: uchime;v4.1;default parameters
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- chimera check software
rank: 1000
is_a: sequencing field
string_serialization: '{software};{version};{parameters}'
slot_uri: MIXS:0000052
multivalued: false
alias: chimera_check
domain_of:
- Biosample
- OmicsProcessing
range: TextValue

```
</details>