# Class: FunctionalAnnotationTerm


_Abstract grouping class for any term/descriptor that can be applied to a functional unit of a genome (protein, ncRNA, complex)._




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [nmdc:FunctionalAnnotationTerm](https://w3id.org/nmdc/FunctionalAnnotationTerm)




```mermaid
 classDiagram
    class FunctionalAnnotationTerm
      OntologyClass <|-- FunctionalAnnotationTerm
      

      FunctionalAnnotationTerm <|-- Pathway
      FunctionalAnnotationTerm <|-- Reaction
      FunctionalAnnotationTerm <|-- OrthologyGroup
      
      
      FunctionalAnnotationTerm : alternative_identifiers
        
      FunctionalAnnotationTerm : description
        
      FunctionalAnnotationTerm : id
        
      FunctionalAnnotationTerm : name
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * [OntologyClass](OntologyClass.md)
        * **FunctionalAnnotationTerm**
            * [Pathway](Pathway.md)
            * [Reaction](Reaction.md)
            * [OrthologyGroup](OrthologyGroup.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [Uriorcurie](Uriorcurie.md) | A unique identifier for a thing | [NamedThing](NamedThing.md) |
| [name](name.md) | 0..1 <br/> [String](String.md) | A human readable label for an entity | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | a human-readable description of a thing | [NamedThing](NamedThing.md) |
| [alternative_identifiers](alternative_identifiers.md) | 0..* <br/> [Uriorcurie](Uriorcurie.md) | A list of alternative identifiers for the entity | [NamedThing](NamedThing.md) |







## Aliases


* function
* FunctionalAnnotation



## TODOs

* decide if this should be used for product naming

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nmdc:FunctionalAnnotationTerm |
| native | nmdc:FunctionalAnnotationTerm |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FunctionalAnnotationTerm
description: Abstract grouping class for any term/descriptor that can be applied to
  a functional unit of a genome (protein, ncRNA, complex).
todos:
- decide if this should be used for product naming
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- function
- FunctionalAnnotation
is_a: OntologyClass
abstract: true

```
</details>

### Induced

<details>
```yaml
name: FunctionalAnnotationTerm
description: Abstract grouping class for any term/descriptor that can be applied to
  a functional unit of a genome (protein, ncRNA, complex).
todos:
- decide if this should be used for product naming
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- function
- FunctionalAnnotation
is_a: OntologyClass
abstract: true
attributes:
  id:
    name: id
    description: A unique identifier for a thing. Must be either a CURIE shorthand
      for a URI or a complete URI
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    identifier: true
    alias: id
    owner: FunctionalAnnotationTerm
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
    owner: FunctionalAnnotationTerm
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
    owner: FunctionalAnnotationTerm
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
    owner: FunctionalAnnotationTerm
    domain_of:
    - Biosample
    - Study
    - NamedThing
    - MetaboliteQuantification
    range: uriorcurie
    pattern: ^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$

```
</details>