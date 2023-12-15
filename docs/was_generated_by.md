# Slot: was_generated_by

URI: [nmdc:was_generated_by](https://w3id.org/nmdc/was_generated_by)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[DataObject](DataObject.md) | An object that primarily consists of symbols that represent information |  no  |
[AttributeValue](AttributeValue.md) | The value for any value of a attribute for a sample |  no  |
[FunctionalAnnotation](FunctionalAnnotation.md) | An assignment of a function term (e |  yes  |
[QuantityValue](QuantityValue.md) | A simple quantity, e |  no  |
[ImageValue](ImageValue.md) | An attribute value representing an image |  no  |
[PersonValue](PersonValue.md) | An attribute value representing a person |  no  |
[TextValue](TextValue.md) | A basic string value |  no  |
[UrlValue](UrlValue.md) | A value that is a string that conforms to URL syntax |  no  |
[TimestampValue](TimestampValue.md) | A value that is a timestamp |  no  |
[IntegerValue](IntegerValue.md) | A value that is an integer |  no  |
[BooleanValue](BooleanValue.md) | A value that is a boolean |  no  |
[ControlledTermValue](ControlledTermValue.md) | A controlled term or class from an ontology |  no  |
[ControlledIdentifiedTermValue](ControlledIdentifiedTermValue.md) | A controlled term or class from an ontology, requiring the presence of term w... |  no  |
[GeolocationValue](GeolocationValue.md) | A normalized value for a location on the earth's surface |  no  |







## Properties

* Range: [Activity](Activity.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: was_generated_by
from_schema: https://w3id.org/nmdc/nmdc
mappings:
- prov:wasGeneratedBy
rank: 1000
alias: was_generated_by
domain_of:
- DataObject
- AttributeValue
- FunctionalAnnotation
range: Activity

```
</details>