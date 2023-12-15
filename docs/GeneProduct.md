# Class: GeneProduct


_A molecule encoded by a gene that has an evolved function_





URI: [nmdc:GeneProduct](https://w3id.org/nmdc/GeneProduct)




```mermaid
 classDiagram
    class GeneProduct
      NamedThing <|-- GeneProduct
      
      GeneProduct : alternative_identifiers
        
      GeneProduct : description
        
      GeneProduct : id
        
      GeneProduct : name
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * **GeneProduct**



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
| [PeptideQuantification](PeptideQuantification.md) | [all_proteins](all_proteins.md) | range | [GeneProduct](GeneProduct.md) |
| [PeptideQuantification](PeptideQuantification.md) | [best_protein](best_protein.md) | range | [GeneProduct](GeneProduct.md) |
| [ProteinQuantification](ProteinQuantification.md) | [all_proteins](all_proteins.md) | range | [GeneProduct](GeneProduct.md) |
| [ProteinQuantification](ProteinQuantification.md) | [best_protein](best_protein.md) | range | [GeneProduct](GeneProduct.md) |
| [GenomeFeature](GenomeFeature.md) | [encodes](encodes.md) | range | [GeneProduct](GeneProduct.md) |
| [FunctionalAnnotation](FunctionalAnnotation.md) | [subject](subject.md) | range | [GeneProduct](GeneProduct.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* PR

* UniProtKB

* gtpo








### Schema Source


* from schema: https://w3id.org/nmdc/nmdc





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nmdc:GeneProduct |
| native | nmdc:GeneProduct |
| exact | biolink:GeneProduct |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GeneProduct
id_prefixes:
- PR
- UniProtKB
- gtpo
description: A molecule encoded by a gene that has an evolved function
notes:
- we may include a more general gene product class in future to allow for ncRNA annotation
from_schema: https://w3id.org/nmdc/nmdc
exact_mappings:
- biolink:GeneProduct
is_a: NamedThing

```
</details>

### Induced

<details>
```yaml
name: GeneProduct
id_prefixes:
- PR
- UniProtKB
- gtpo
description: A molecule encoded by a gene that has an evolved function
notes:
- we may include a more general gene product class in future to allow for ncRNA annotation
from_schema: https://w3id.org/nmdc/nmdc
exact_mappings:
- biolink:GeneProduct
is_a: NamedThing
attributes:
  id:
    name: id
    description: A unique identifier for a thing. Must be either a CURIE shorthand
      for a URI or a complete URI
    notes:
    - 'abstracted pattern: prefix:typecode-authshoulder-blade(.version)?(_seqsuffix)?'
    - a minimum length of 3 characters is suggested for typecodes, but 1 or 2 characters
      will be accepted
    - typecodes must correspond 1:1 to a class in the NMDC schema. this will be checked
      via per-class id slot usage assertions
    - minting authority shoulders should probably be enumerated and checked in the
      pattern
    examples:
    - value: nmdc:mgmag-00-x012.1_7_c1
      description: https://github.com/microbiomedata/nmdc-schema/pull/499#discussion_r1018499248
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    identifier: true
    alias: id
    owner: GeneProduct
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
    owner: GeneProduct
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
    owner: GeneProduct
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
    owner: GeneProduct
    domain_of:
    - Biosample
    - Study
    - NamedThing
    - MetaboliteQuantification
    range: uriorcurie
    pattern: ^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$

```
</details>