# Class: TimestampValue


_A value that is a timestamp. The range should be ISO-8601_





URI: [nmdc:TimestampValue](https://w3id.org/nmdc/TimestampValue)




```mermaid
 classDiagram
    class TimestampValue
      AttributeValue <|-- TimestampValue
      
      TimestampValue : has_raw_value
        
      TimestampValue : was_generated_by
        
          TimestampValue --|> Activity : was_generated_by
        
      
```





## Inheritance
* [AttributeValue](AttributeValue.md)
    * **TimestampValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [has_raw_value](has_raw_value.md) | 0..1 <br/> [String](String.md) | The value that was specified for an annotation in raw form, i | [AttributeValue](AttributeValue.md) |
| [was_generated_by](was_generated_by.md) | 0..1 <br/> [Activity](Activity.md) |  | [AttributeValue](AttributeValue.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Biosample](Biosample.md) | [collection_date](collection_date.md) | range | [TimestampValue](TimestampValue.md) |
| [Biosample](Biosample.md) | [date_last_rain](date_last_rain.md) | range | [TimestampValue](TimestampValue.md) |
| [Biosample](Biosample.md) | [iw_bt_date_well](iw_bt_date_well.md) | range | [TimestampValue](TimestampValue.md) |
| [Biosample](Biosample.md) | [last_clean](last_clean.md) | range | [TimestampValue](TimestampValue.md) |
| [Biosample](Biosample.md) | [prod_start_date](prod_start_date.md) | range | [TimestampValue](TimestampValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nmdc:TimestampValue |
| native | nmdc:TimestampValue |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TimestampValue
description: A value that is a timestamp. The range should be ISO-8601
notes:
- 'removed the following slots: year, month, day'
from_schema: https://w3id.org/nmdc/nmdc
is_a: AttributeValue

```
</details>

### Induced

<details>
```yaml
name: TimestampValue
description: A value that is a timestamp. The range should be ISO-8601
notes:
- 'removed the following slots: year, month, day'
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
    owner: TimestampValue
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
    owner: TimestampValue
    domain_of:
    - DataObject
    - AttributeValue
    - FunctionalAnnotation
    range: Activity

```
</details>