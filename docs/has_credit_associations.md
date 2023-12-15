# Slot: has_credit_associations


_This slot links a study to a credit association.  The credit association will be linked to a person value and to a CRediT Contributor Roles term. Overall semantics: person should get credit X for their participation in the study_



URI: [prov:qualifiedAssociation](http://www.w3.org/ns/prov#qualifiedAssociation)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Study](Study.md) | A study summarizes the overall goal of a research initiative and outlines the... |  no  |







## Properties

* Range: [CreditAssociation](CreditAssociation.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| display_hint | Other researchers associated with this study. |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: has_credit_associations
annotations:
  display_hint:
    tag: display_hint
    value: Other researchers associated with this study.
description: 'This slot links a study to a credit association.  The credit association
  will be linked to a person value and to a CRediT Contributor Roles term. Overall
  semantics: person should get credit X for their participation in the study'
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
domain: Study
slot_uri: prov:qualifiedAssociation
multivalued: true
alias: has_credit_associations
domain_of:
- Study
range: CreditAssociation
inlined: true
inlined_as_list: true

```
</details>