# Class: OntologyClass



URI: [nmdc:OntologyClass](https://w3id.org/nmdc/OntologyClass)




```mermaid
 classDiagram
    class OntologyClass
      NamedThing <|-- OntologyClass
      

      OntologyClass <|-- EnvironmentalMaterialTerm
      OntologyClass <|-- ChemicalEntity
      OntologyClass <|-- FunctionalAnnotationTerm
      
      
      OntologyClass : alternative_identifiers
        
      OntologyClass : description
        
      OntologyClass : id
        
      OntologyClass : name
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * **OntologyClass**
        * [EnvironmentalMaterialTerm](EnvironmentalMaterialTerm.md)
        * [ChemicalEntity](ChemicalEntity.md)
        * [FunctionalAnnotationTerm](FunctionalAnnotationTerm.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [Uriorcurie](Uriorcurie.md) | A unique identifier for a thing | [NamedThing](NamedThing.md) |
| [name](name.md) | 0..1 <br/> [String](String.md) | A human readable label for an entity | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | a human-readable description of a thing | [NamedThing](NamedThing.md) |
| [alternative_identifiers](alternative_identifiers.md) | 0..* <br/> [Uriorcurie](Uriorcurie.md) | A list of alternative identifiers for the entity | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ControlledTermValue](ControlledTermValue.md) | [term](term.md) | range | [OntologyClass](OntologyClass.md) |
| [ControlledIdentifiedTermValue](ControlledIdentifiedTermValue.md) | [term](term.md) | range | [OntologyClass](OntologyClass.md) |
| [GenomeFeature](GenomeFeature.md) | [type](type.md) | range | [OntologyClass](OntologyClass.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nmdc:OntologyClass |
| native | nmdc:OntologyClass |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OntologyClass
notes:
- The identifiers for terms from external ontologies can't have their ids constrained
  to the nmdc namespace
from_schema: https://w3id.org/nmdc/nmdc
is_a: NamedThing
slot_usage:
  id:
    name: id
    domain_of:
    - Biosample
    - Study
    - NamedThing
    - Activity
    pattern: ^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$

```
</details>

### Induced

<details>
```yaml
name: OntologyClass
notes:
- The identifiers for terms from external ontologies can't have their ids constrained
  to the nmdc namespace
from_schema: https://w3id.org/nmdc/nmdc
is_a: NamedThing
slot_usage:
  id:
    name: id
    domain_of:
    - Biosample
    - Study
    - NamedThing
    - Activity
    pattern: ^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$
attributes:
  id:
    name: id
    description: A unique identifier for a thing. Must be either a CURIE shorthand
      for a URI or a complete URI
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    identifier: true
    alias: id
    owner: OntologyClass
    domain_of:
    - Biosample
    - Study
    - NamedThing
    - Activity
    range: uriorcurie
    required: true
    pattern: ^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$
  name:
    name: name
    description: A human readable label for an entity
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    alias: name
    owner: OntologyClass
    domain_of:
    - Protocol
    - QualityControlReport
    - NamedThing
    - PersonValue
    - Activity
    range: string
  description:
    name: description
    description: a human-readable description of a thing
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    slot_uri: dcterms:description
    alias: description
    owner: OntologyClass
    domain_of:
    - Study
    - NamedThing
    - ImageValue
    range: string
  alternative_identifiers:
    name: alternative_identifiers
    description: A list of alternative identifiers for the entity.
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    multivalued: true
    alias: alternative_identifiers
    owner: OntologyClass
    domain_of:
    - Biosample
    - Study
    - NamedThing
    - MetaboliteQuantification
    range: uriorcurie
    pattern: ^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$

```
</details>