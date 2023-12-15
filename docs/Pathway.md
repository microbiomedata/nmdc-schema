# Class: Pathway


_A pathway is a sequence of steps/reactions carried out by an organism or community of organisms_





URI: [nmdc:Pathway](https://w3id.org/nmdc/Pathway)




```mermaid
 classDiagram
    class Pathway
      FunctionalAnnotationTerm <|-- Pathway
      
      Pathway : alternative_identifiers
        
      Pathway : description
        
      Pathway : has_part
        
          Pathway --|> Reaction : has_part
        
      Pathway : id
        
      Pathway : name
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * [OntologyClass](OntologyClass.md)
        * [FunctionalAnnotationTerm](FunctionalAnnotationTerm.md)
            * **Pathway**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [has_part](has_part.md) | 1..* <br/> [Reaction](Reaction.md) | A pathway can be broken down to a series of reaction step | direct |
| [id](id.md) | 1..1 <br/> [Uriorcurie](Uriorcurie.md) | A unique identifier for a thing | [NamedThing](NamedThing.md) |
| [name](name.md) | 0..1 <br/> [String](String.md) | A human readable label for an entity | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | a human-readable description of a thing | [NamedThing](NamedThing.md) |
| [alternative_identifiers](alternative_identifiers.md) | 0..* <br/> [Uriorcurie](Uriorcurie.md) | A list of alternative identifiers for the entity | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Pathway](Pathway.md) | [has_part](has_part.md) | domain | [Pathway](Pathway.md) |




## Aliases


* biological process
* metabolic pathway
* signaling pathway



## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* KEGG_PATHWAY

* COG








### Schema Source


* from schema: https://w3id.org/nmdc/nmdc





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nmdc:Pathway |
| native | nmdc:Pathway |
| exact | biolink:Pathway |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Pathway
id_prefixes:
- KEGG_PATHWAY
- COG
description: A pathway is a sequence of steps/reactions carried out by an organism
  or community of organisms
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- biological process
- metabolic pathway
- signaling pathway
exact_mappings:
- biolink:Pathway
is_a: FunctionalAnnotationTerm
slots:
- has_part
slot_usage:
  has_part:
    name: has_part
    description: A pathway can be broken down to a series of reaction step
    domain_of:
    - Pathway
    range: Reaction
    required: true

```
</details>

### Induced

<details>
```yaml
name: Pathway
id_prefixes:
- KEGG_PATHWAY
- COG
description: A pathway is a sequence of steps/reactions carried out by an organism
  or community of organisms
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- biological process
- metabolic pathway
- signaling pathway
exact_mappings:
- biolink:Pathway
is_a: FunctionalAnnotationTerm
slot_usage:
  has_part:
    name: has_part
    description: A pathway can be broken down to a series of reaction step
    domain_of:
    - Pathway
    range: Reaction
    required: true
attributes:
  has_part:
    name: has_part
    description: A pathway can be broken down to a series of reaction step
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    domain: Pathway
    multivalued: true
    alias: has_part
    owner: Pathway
    domain_of:
    - Pathway
    range: Reaction
    required: true
  id:
    name: id
    description: A unique identifier for a thing. Must be either a CURIE shorthand
      for a URI or a complete URI
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    identifier: true
    alias: id
    owner: Pathway
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
    owner: Pathway
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
    owner: Pathway
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
    owner: Pathway
    domain_of:
    - Biosample
    - Study
    - NamedThing
    - MetaboliteQuantification
    range: uriorcurie
    pattern: ^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$

```
</details>