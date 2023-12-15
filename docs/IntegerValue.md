# Class: IntegerValue


_A value that is an integer_





URI: [nmdc:IntegerValue](https://w3id.org/nmdc/IntegerValue)




```mermaid
 classDiagram
    class IntegerValue
      AttributeValue <|-- IntegerValue
      
      IntegerValue : has_numeric_value
        
      IntegerValue : has_raw_value
        
      IntegerValue : was_generated_by
        
          IntegerValue --|> Activity : was_generated_by
        
      
```





## Inheritance
* [AttributeValue](AttributeValue.md)
    * **IntegerValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [has_numeric_value](has_numeric_value.md) | 0..1 <br/> [Float](Float.md) | Links a quantity value to a number | direct |
| [has_raw_value](has_raw_value.md) | 0..1 <br/> [String](String.md) | The value that was specified for an annotation in raw form, i | [AttributeValue](AttributeValue.md) |
| [was_generated_by](was_generated_by.md) | 0..1 <br/> [Activity](Activity.md) |  | [AttributeValue](AttributeValue.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nmdc:IntegerValue |
| native | nmdc:IntegerValue |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IntegerValue
description: A value that is an integer
from_schema: https://w3id.org/nmdc/nmdc
is_a: AttributeValue
slots:
- has_numeric_value

```
</details>

### Induced

<details>
```yaml
name: IntegerValue
description: A value that is an integer
from_schema: https://w3id.org/nmdc/nmdc
is_a: AttributeValue
attributes:
  has_numeric_value:
    name: has_numeric_value
    description: Links a quantity value to a number
    from_schema: https://w3id.org/nmdc/nmdc
    mappings:
    - qud:quantityValue
    - schema:value
    rank: 1000
    domain: QuantityValue
    multivalued: false
    alias: has_numeric_value
    owner: IntegerValue
    domain_of:
    - QuantityValue
    - IntegerValue
    range: float
  has_raw_value:
    name: has_raw_value
    description: The value that was specified for an annotation in raw form, i.e.
      a string. E.g. "2 cm" or "2-4 cm"
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    domain: AttributeValue
    multivalued: false
    alias: has_raw_value
    owner: IntegerValue
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
    owner: IntegerValue
    domain_of:
    - DataObject
    - AttributeValue
    - FunctionalAnnotation
    range: Activity

```
</details>