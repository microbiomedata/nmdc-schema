# Slot: sample type (samp_type)


_The type of material from which the sample was obtained. For the Hydrocarbon package, samples include types like core, rock trimmings, drill cuttings, piping section, coupon, pigging debris, solid deposit, produced fluid, produced water, injected water, swabs, etc. For the Food Package, samples are usually categorized as food, body products or tissues, or environmental material. This field accepts terms listed under environmental specimen (http://purl.obolibrary.org/obo/GENEPIO_0001246)._



URI: [MIXS:0000998](https://w3id.org/mixs/0000998)




## Inheritance

* [core_field](core_field.md)
    * **samp_type**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* sample type




## Examples

| Value |
| --- |
| built environment sample [GENEPIO:0001248] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | GENEPIO:0001246 || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: samp_type
annotations:
  expected_value:
    tag: expected_value
    value: GENEPIO:0001246
  occurrence:
    tag: occurrence
    value: '1'
description: The type of material from which the sample was obtained. For the Hydrocarbon
  package, samples include types like core, rock trimmings, drill cuttings, piping
  section, coupon, pigging debris, solid deposit, produced fluid, produced water,
  injected water, swabs, etc. For the Food Package, samples are usually categorized
  as food, body products or tissues, or environmental material. This field accepts
  terms listed under environmental specimen (http://purl.obolibrary.org/obo/GENEPIO_0001246).
title: sample type
examples:
- value: built environment sample [GENEPIO:0001248]
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- sample type
rank: 1000
is_a: core field
string_serialization: '{termLabel} {[termID]}'
slot_uri: MIXS:0000998
multivalued: false
alias: samp_type
domain_of:
- Biosample
range: TextValue

```
</details>