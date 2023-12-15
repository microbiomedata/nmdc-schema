# Class: OrthologyGroup


_A set of genes or gene products in which all members are orthologous_





URI: [nmdc:OrthologyGroup](https://w3id.org/nmdc/OrthologyGroup)




```mermaid
 classDiagram
    class OrthologyGroup
      FunctionalAnnotationTerm <|-- OrthologyGroup
      
      OrthologyGroup : alternative_identifiers
        
      OrthologyGroup : description
        
      OrthologyGroup : id
        
      OrthologyGroup : name
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * [OntologyClass](OntologyClass.md)
        * [FunctionalAnnotationTerm](FunctionalAnnotationTerm.md)
            * **OrthologyGroup**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [Uriorcurie](Uriorcurie.md) | A unique identifier for a thing | [NamedThing](NamedThing.md) |
| [name](name.md) | 0..1 <br/> [String](String.md) | A human readable label for an entity | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | a human-readable description of a thing | [NamedThing](NamedThing.md) |
| [alternative_identifiers](alternative_identifiers.md) | 0..* <br/> [Uriorcurie](Uriorcurie.md) | A list of alternative identifiers for the entity | [NamedThing](NamedThing.md) |









## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* CATH

* EGGNOG

* KEGG.ORTHOLOGY

* PANTHER.FAMILY

* PFAM

* SUPFAM

* TIGRFAM








### Schema Source


* from schema: https://w3id.org/nmdc/nmdc





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nmdc:OrthologyGroup |
| native | nmdc:OrthologyGroup |
| exact | biolink:GeneFamily |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OrthologyGroup
id_prefixes:
- CATH
- EGGNOG
- KEGG.ORTHOLOGY
- PANTHER.FAMILY
- PFAM
- SUPFAM
- TIGRFAM
description: A set of genes or gene products in which all members are orthologous
notes:
- KEGG.ORTHOLOGY prefix is used for KO numbers
from_schema: https://w3id.org/nmdc/nmdc
exact_mappings:
- biolink:GeneFamily
is_a: FunctionalAnnotationTerm

```
</details>

### Induced

<details>
```yaml
name: OrthologyGroup
id_prefixes:
- CATH
- EGGNOG
- KEGG.ORTHOLOGY
- PANTHER.FAMILY
- PFAM
- SUPFAM
- TIGRFAM
description: A set of genes or gene products in which all members are orthologous
notes:
- KEGG.ORTHOLOGY prefix is used for KO numbers
from_schema: https://w3id.org/nmdc/nmdc
exact_mappings:
- biolink:GeneFamily
is_a: FunctionalAnnotationTerm
attributes:
  id:
    name: id
    description: A unique identifier for a thing. Must be either a CURIE shorthand
      for a URI or a complete URI
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    identifier: true
    alias: id
    owner: OrthologyGroup
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
    owner: OrthologyGroup
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
    owner: OrthologyGroup
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
    owner: OrthologyGroup
    domain_of:
    - Biosample
    - Study
    - NamedThing
    - MetaboliteQuantification
    range: uriorcurie
    pattern: ^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$

```
</details>