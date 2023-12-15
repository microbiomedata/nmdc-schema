# Slot: term


_pointer to an ontology class_



URI: [nmdc:term](https://w3id.org/nmdc/term)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ControlledTermValue](ControlledTermValue.md) | A controlled term or class from an ontology |  no  |
[ControlledIdentifiedTermValue](ControlledIdentifiedTermValue.md) | A controlled term or class from an ontology, requiring the presence of term w... |  yes  |







## Properties

* Range: [OntologyClass](OntologyClass.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: term
description: pointer to an ontology class
notes:
- 'removed ''slot_uri: rdf:type'''
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
domain: ControlledTermValue
alias: term
domain_of:
- ControlledTermValue
range: OntologyClass
inlined: true

```
</details>