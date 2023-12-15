# Class: UrlValue


_A value that is a string that conforms to URL syntax_





URI: [nmdc:UrlValue](https://w3id.org/nmdc/UrlValue)




```mermaid
 classDiagram
    class UrlValue
      AttributeValue <|-- UrlValue
      
      UrlValue : has_raw_value
        
      UrlValue : was_generated_by
        
          UrlValue --|> Activity : was_generated_by
        
      
```





## Inheritance
* [AttributeValue](AttributeValue.md)
    * **UrlValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [has_raw_value](has_raw_value.md) | 0..1 <br/> [String](String.md) | The value that was specified for an annotation in raw form, i | [AttributeValue](AttributeValue.md) |
| [was_generated_by](was_generated_by.md) | 0..1 <br/> [Activity](Activity.md) |  | [AttributeValue](AttributeValue.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nmdc:UrlValue |
| native | nmdc:UrlValue |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: UrlValue
description: A value that is a string that conforms to URL syntax
from_schema: https://w3id.org/nmdc/nmdc
is_a: AttributeValue

```
</details>

### Induced

<details>
```yaml
name: UrlValue
description: A value that is a string that conforms to URL syntax
from_schema: https://w3id.org/nmdc/nmdc
is_a: AttributeValue
attributes:
  has_raw_value:
    name: has_raw_value
    description: The value that was specified for an annotation in raw form, i.e.
      a string. E.g. "2 cm" or "2-4 cm"
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    domain: AttributeValue
    multivalued: false
    alias: has_raw_value
    owner: UrlValue
    domain_of:
    - AttributeValue
    - QuantityValue
    range: string
  was_generated_by:
    name: was_generated_by
    from_schema: https://w3id.org/nmdc/nmdc
    mappings:
    - prov:wasGeneratedBy
    rank: 1000
    alias: was_generated_by
    owner: UrlValue
    domain_of:
    - DataObject
    - AttributeValue
    - FunctionalAnnotation
    range: Activity

```
</details>