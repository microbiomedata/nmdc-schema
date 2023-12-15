# Class: Planned Process (PlannedProcess)


* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [OBI:0000011](http://purl.obolibrary.org/obo/OBI_0000011)




```mermaid
 classDiagram
    class PlannedProcess
      NamedThing <|-- PlannedProcess
      

      PlannedProcess <|-- Extraction
      PlannedProcess <|-- CollectingBiosamplesFromSite
      PlannedProcess <|-- BiosampleProcessing
      PlannedProcess <|-- SubSamplingProcess
      PlannedProcess <|-- MixingProcess
      PlannedProcess <|-- FiltrationProcess
      PlannedProcess <|-- ChromatographicSeparationProcess
      PlannedProcess <|-- OmicsProcessing
      
      
      PlannedProcess : alternative_identifiers
        
      PlannedProcess : description
        
      PlannedProcess : designated_class
        
      PlannedProcess : end_date
        
      PlannedProcess : has_input
        
          PlannedProcess --|> NamedThing : has_input
        
      PlannedProcess : has_output
        
          PlannedProcess --|> NamedThing : has_output
        
      PlannedProcess : id
        
      PlannedProcess : instrument_name
        
      PlannedProcess : name
        
      PlannedProcess : processing_institution
        
          PlannedProcess --|> processing_institution_enum : processing_institution
        
      PlannedProcess : protocol_link
        
          PlannedProcess --|> Protocol : protocol_link
        
      PlannedProcess : start_date
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * **PlannedProcess**
        * [Extraction](Extraction.md)
        * [CollectingBiosamplesFromSite](CollectingBiosamplesFromSite.md)
        * [BiosampleProcessing](BiosampleProcessing.md)
        * [SubSamplingProcess](SubSamplingProcess.md)
        * [MixingProcess](MixingProcess.md)
        * [FiltrationProcess](FiltrationProcess.md)
        * [ChromatographicSeparationProcess](ChromatographicSeparationProcess.md)
        * [OmicsProcessing](OmicsProcessing.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [designated_class](designated_class.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) |  | direct |
| [end_date](end_date.md) | 0..1 <br/> [String](String.md) | The date on which any process or activity was ended | direct |
| [has_input](has_input.md) | 0..* <br/> [NamedThing](NamedThing.md) | An input to a process | direct |
| [has_output](has_output.md) | 0..* <br/> [NamedThing](NamedThing.md) | An output biosample to a processing step | direct |
| [processing_institution](processing_institution.md) | 0..1 <br/> [ProcessingInstitutionEnum](ProcessingInstitutionEnum.md) | The organization that processed the sample | direct |
| [protocol_link](protocol_link.md) | 0..1 <br/> [Protocol](Protocol.md) |  | direct |
| [start_date](start_date.md) | 0..1 <br/> [String](String.md) | The date on which any process or activity was started | direct |
| [instrument_name](instrument_name.md) | 0..1 <br/> [String](String.md) | The name of the instrument that was used for processing the sample | direct |
| [id](id.md) | 1..1 <br/> [Uriorcurie](Uriorcurie.md) | A unique identifier for a thing | [NamedThing](NamedThing.md) |
| [name](name.md) | 0..1 <br/> [String](String.md) | A human readable label for an entity | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | a human-readable description of a thing | [NamedThing](NamedThing.md) |
| [alternative_identifiers](alternative_identifiers.md) | 0..* <br/> [Uriorcurie](Uriorcurie.md) | A list of alternative identifiers for the entity | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Database](Database.md) | [planned_process_set](planned_process_set.md) | range | [PlannedProcess](PlannedProcess.md) |
| [Pooling](Pooling.md) | [processing_institution](processing_institution.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [Pooling](Pooling.md) | [protocol_link](protocol_link.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [Pooling](Pooling.md) | [instrument_name](instrument_name.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [Extraction](Extraction.md) | [input_mass](input_mass.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [Extraction](Extraction.md) | [quality_control_report](quality_control_report.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [Extraction](Extraction.md) | [processing_institution](processing_institution.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [Extraction](Extraction.md) | [protocol_link](protocol_link.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [Extraction](Extraction.md) | [instrument_name](instrument_name.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [Solution](Solution.md) | [volume](volume.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [LibraryPreparation](LibraryPreparation.md) | [processing_institution](processing_institution.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [LibraryPreparation](LibraryPreparation.md) | [protocol_link](protocol_link.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [LibraryPreparation](LibraryPreparation.md) | [instrument_name](instrument_name.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [CollectingBiosamplesFromSite](CollectingBiosamplesFromSite.md) | [processing_institution](processing_institution.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [CollectingBiosamplesFromSite](CollectingBiosamplesFromSite.md) | [protocol_link](protocol_link.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [CollectingBiosamplesFromSite](CollectingBiosamplesFromSite.md) | [instrument_name](instrument_name.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [BiosampleProcessing](BiosampleProcessing.md) | [processing_institution](processing_institution.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [BiosampleProcessing](BiosampleProcessing.md) | [protocol_link](protocol_link.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [BiosampleProcessing](BiosampleProcessing.md) | [instrument_name](instrument_name.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [SubSamplingProcess](SubSamplingProcess.md) | [volume](volume.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [SubSamplingProcess](SubSamplingProcess.md) | [processing_institution](processing_institution.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [SubSamplingProcess](SubSamplingProcess.md) | [protocol_link](protocol_link.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [SubSamplingProcess](SubSamplingProcess.md) | [instrument_name](instrument_name.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [MixingProcess](MixingProcess.md) | [duration](duration.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [MixingProcess](MixingProcess.md) | [processing_institution](processing_institution.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [MixingProcess](MixingProcess.md) | [protocol_link](protocol_link.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [MixingProcess](MixingProcess.md) | [instrument_name](instrument_name.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [FiltrationProcess](FiltrationProcess.md) | [volume](volume.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [FiltrationProcess](FiltrationProcess.md) | [processing_institution](processing_institution.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [FiltrationProcess](FiltrationProcess.md) | [protocol_link](protocol_link.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [FiltrationProcess](FiltrationProcess.md) | [instrument_name](instrument_name.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [ChromatographicSeparationProcess](ChromatographicSeparationProcess.md) | [processing_institution](processing_institution.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [ChromatographicSeparationProcess](ChromatographicSeparationProcess.md) | [protocol_link](protocol_link.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [ChromatographicSeparationProcess](ChromatographicSeparationProcess.md) | [instrument_name](instrument_name.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [OmicsProcessing](OmicsProcessing.md) | [instrument_name](instrument_name.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [OmicsProcessing](OmicsProcessing.md) | [processing_institution](processing_institution.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [OmicsProcessing](OmicsProcessing.md) | [protocol_link](protocol_link.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [PlannedProcess](PlannedProcess.md) | [processing_institution](processing_institution.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [PlannedProcess](PlannedProcess.md) | [protocol_link](protocol_link.md) | domain | [PlannedProcess](PlannedProcess.md) |
| [PlannedProcess](PlannedProcess.md) | [instrument_name](instrument_name.md) | domain | [PlannedProcess](PlannedProcess.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | OBI:0000011 |
| native | nmdc:PlannedProcess |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PlannedProcess
title: Planned Process
from_schema: https://w3id.org/nmdc/nmdc
is_a: NamedThing
abstract: true
slots:
- designated_class
- end_date
- has_input
- has_output
- processing_institution
- protocol_link
- start_date
- instrument_name
slot_usage:
  designated_class:
    name: designated_class
    comments:
    - required on all instances in a polymorphic Database slot like planned_process_set
    domain_of:
    - PlannedProcess
class_uri: OBI:0000011

```
</details>

### Induced

<details>
```yaml
name: PlannedProcess
title: Planned Process
from_schema: https://w3id.org/nmdc/nmdc
is_a: NamedThing
abstract: true
slot_usage:
  designated_class:
    name: designated_class
    comments:
    - required on all instances in a polymorphic Database slot like planned_process_set
    domain_of:
    - PlannedProcess
attributes:
  designated_class:
    name: designated_class
    comments:
    - required on all instances in a polymorphic Database slot like planned_process_set
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    designates_type: true
    alias: designated_class
    owner: PlannedProcess
    domain_of:
    - PlannedProcess
    range: uriorcurie
  end_date:
    name: end_date
    description: The date on which any process or activity was ended
    todos:
    - add date string validation pattern
    comments:
    - We are using string representations of dates until all components of our ecosystem
      can handle ISO 8610 dates
    - The date should be formatted as YYYY-MM-DD
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    alias: end_date
    owner: PlannedProcess
    domain_of:
    - PlannedProcess
    range: string
  has_input:
    name: has_input
    description: An input to a process.
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - input
    rank: 1000
    domain: NamedThing
    multivalued: true
    alias: has_input
    owner: PlannedProcess
    domain_of:
    - BiosampleProcessing
    - OmicsProcessing
    - WorkflowExecutionActivity
    - PlannedProcess
    range: NamedThing
  has_output:
    name: has_output
    description: An output biosample to a processing step
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - output
    rank: 1000
    domain: NamedThing
    multivalued: true
    alias: has_output
    owner: PlannedProcess
    domain_of:
    - OmicsProcessing
    - WorkflowExecutionActivity
    - PlannedProcess
    range: NamedThing
  processing_institution:
    name: processing_institution
    description: The organization that processed the sample.
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    domain: PlannedProcess
    alias: processing_institution
    owner: PlannedProcess
    domain_of:
    - OmicsProcessing
    - PlannedProcess
    range: processing_institution_enum
  protocol_link:
    name: protocol_link
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    domain: PlannedProcess
    alias: protocol_link
    owner: PlannedProcess
    domain_of:
    - PlannedProcess
    range: Protocol
  start_date:
    name: start_date
    description: The date on which any process or activity was started
    todos:
    - add date string validation pattern
    comments:
    - We are using string representations of dates until all components of our ecosystem
      can handle ISO 8610 dates
    - The date should be formatted as YYYY-MM-DD
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    alias: start_date
    owner: PlannedProcess
    domain_of:
    - PlannedProcess
    range: string
  instrument_name:
    name: instrument_name
    description: The name of the instrument that was used for processing the sample.
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    domain: PlannedProcess
    alias: instrument_name
    owner: PlannedProcess
    domain_of:
    - OmicsProcessing
    - PlannedProcess
    range: string
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
    owner: PlannedProcess
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
    owner: PlannedProcess
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
    owner: PlannedProcess
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
    owner: PlannedProcess
    domain_of:
    - Biosample
    - Study
    - NamedThing
    - MetaboliteQuantification
    range: uriorcurie
    pattern: ^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$
class_uri: OBI:0000011

```
</details>