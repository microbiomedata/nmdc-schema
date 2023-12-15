# Slot: applied_roles

URI: [nmdc:applied_roles](https://w3id.org/nmdc/applied_roles)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[CreditAssociation](CreditAssociation.md) | This class supports binding associated researchers to studies |  no  |







## Properties

* Range: [CreditEnum](CreditEnum.md)

* Multivalued: True

* Required: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| display_hint | Identify all CRediT roles associated with this contributor. CRediT Information: https://info.orcid.org/credit-for-research-contribution ; CRediT: https://credit.niso.org/ |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: applied_roles
annotations:
  display_hint:
    tag: display_hint
    value: 'Identify all CRediT roles associated with this contributor. CRediT Information:
      https://info.orcid.org/credit-for-research-contribution ; CRediT: https://credit.niso.org/'
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
domain: CreditAssociation
multivalued: true
alias: applied_roles
domain_of:
- CreditAssociation
range: credit enum
required: true

```
</details>