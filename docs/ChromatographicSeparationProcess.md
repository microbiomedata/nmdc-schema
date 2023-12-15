# Class: ChromatographicSeparationProcess


_The process of using a selective partitioning of the analyte or interferent between two immiscible phases._





URI: [nmdc:ChromatographicSeparationProcess](https://w3id.org/nmdc/ChromatographicSeparationProcess)




```mermaid
 classDiagram
    class ChromatographicSeparationProcess
      PlannedProcess <|-- ChromatographicSeparationProcess
      
      ChromatographicSeparationProcess : alternative_identifiers
        
      ChromatographicSeparationProcess : description
        
      ChromatographicSeparationProcess : designated_class
        
      ChromatographicSeparationProcess : end_date
        
      ChromatographicSeparationProcess : has_input
        
          ChromatographicSeparationProcess --|> NamedThing : has_input
        
      ChromatographicSeparationProcess : has_output
        
          ChromatographicSeparationProcess --|> NamedThing : has_output
        
      ChromatographicSeparationProcess : id
        
      ChromatographicSeparationProcess : instrument_name
        
      ChromatographicSeparationProcess : name
        
      ChromatographicSeparationProcess : ordered_mobile_phases
        
          ChromatographicSeparationProcess --|> Solution : ordered_mobile_phases
        
      ChromatographicSeparationProcess : processing_institution
        
          ChromatographicSeparationProcess --|> processing_institution_enum : processing_institution
        
      ChromatographicSeparationProcess : protocol_link
        
          ChromatographicSeparationProcess --|> Protocol : protocol_link
        
      ChromatographicSeparationProcess : start_date
        
      ChromatographicSeparationProcess : stationary_phase
        
          ChromatographicSeparationProcess --|> StationaryPhaseEnum : stationary_phase
        
      ChromatographicSeparationProcess : temperature
        
          ChromatographicSeparationProcess --|> QuantityValue : temperature
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * [PlannedProcess](PlannedProcess.md)
        * **ChromatographicSeparationProcess**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [ordered_mobile_phases](ordered_mobile_phases.md) | 0..* <br/> [Solution](Solution.md) | The solution(s) that moves through a chromatography column | direct |
| [stationary_phase](stationary_phase.md) | 0..1 <br/> [StationaryPhaseEnum](StationaryPhaseEnum.md) | The material the stationary phase is comprised of used in chromatography | direct |
| [temperature](temperature.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The value of a temperature measurement or temperature used in a process | direct |
| [designated_class](designated_class.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) |  | [PlannedProcess](PlannedProcess.md) |
| [end_date](end_date.md) | 0..1 <br/> [String](String.md) | The date on which any process or activity was ended | [PlannedProcess](PlannedProcess.md) |
| [has_input](has_input.md) | 0..* <br/> [NamedThing](NamedThing.md) | An input to a process | [PlannedProcess](PlannedProcess.md) |
| [has_output](has_output.md) | 0..* <br/> [NamedThing](NamedThing.md) | An output biosample to a processing step | [PlannedProcess](PlannedProcess.md) |
| [processing_institution](processing_institution.md) | 0..1 <br/> [ProcessingInstitutionEnum](ProcessingInstitutionEnum.md) | The organization that processed the sample | [PlannedProcess](PlannedProcess.md) |
| [protocol_link](protocol_link.md) | 0..1 <br/> [Protocol](Protocol.md) |  | [PlannedProcess](PlannedProcess.md) |
| [start_date](start_date.md) | 0..1 <br/> [String](String.md) | The date on which any process or activity was started | [PlannedProcess](PlannedProcess.md) |
| [instrument_name](instrument_name.md) | 0..1 <br/> [String](String.md) | The name of the instrument that was used for processing the sample | [PlannedProcess](PlannedProcess.md) |
| [id](id.md) | 1..1 <br/> [Uriorcurie](Uriorcurie.md) | A unique identifier for a thing | [NamedThing](NamedThing.md) |
| [name](name.md) | 0..1 <br/> [String](String.md) | A human readable label for an entity | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | a human-readable description of a thing | [NamedThing](NamedThing.md) |
| [alternative_identifiers](alternative_identifiers.md) | 0..* <br/> [Uriorcurie](Uriorcurie.md) | A list of alternative identifiers for the entity | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ChromatographicSeparationProcess](ChromatographicSeparationProcess.md) | [ordered_mobile_phases](ordered_mobile_phases.md) | domain | [ChromatographicSeparationProcess](ChromatographicSeparationProcess.md) |
| [ChromatographicSeparationProcess](ChromatographicSeparationProcess.md) | [stationary_phase](stationary_phase.md) | domain | [ChromatographicSeparationProcess](ChromatographicSeparationProcess.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nmdc:ChromatographicSeparationProcess |
| native | nmdc:ChromatographicSeparationProcess |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ChromatographicSeparationProcess
description: The process of using a selective partitioning of the analyte or interferent
  between two immiscible phases.
from_schema: https://w3id.org/nmdc/nmdc
contributors:
- ORCID:0009-0001-1555-1601
- ORCID:0000-0002-1368-8217
is_a: PlannedProcess
slots:
- ordered_mobile_phases
- stationary_phase
- temperature
slot_usage:
  has_input:
    name: has_input
    domain_of:
    - BiosampleProcessing
    - OmicsProcessing
    - WorkflowExecutionActivity
    - PlannedProcess
    any_of:
    - range: Biosample
    - range: ProcessedSample

```
</details>

### Induced

<details>
```yaml
name: ChromatographicSeparationProcess
description: The process of using a selective partitioning of the analyte or interferent
  between two immiscible phases.
from_schema: https://w3id.org/nmdc/nmdc
contributors:
- ORCID:0009-0001-1555-1601
- ORCID:0000-0002-1368-8217
is_a: PlannedProcess
slot_usage:
  has_input:
    name: has_input
    domain_of:
    - BiosampleProcessing
    - OmicsProcessing
    - WorkflowExecutionActivity
    - PlannedProcess
    any_of:
    - range: Biosample
    - range: ProcessedSample
attributes:
  ordered_mobile_phases:
    name: ordered_mobile_phases
    description: The solution(s) that moves through a chromatography column.
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    domain: ChromatographicSeparationProcess
    multivalued: true
    list_elements_ordered: true
    alias: ordered_mobile_phases
    owner: ChromatographicSeparationProcess
    domain_of:
    - ChromatographicSeparationProcess
    range: Solution
    inlined: true
    inlined_as_list: true
  stationary_phase:
    name: stationary_phase
    description: The material the stationary phase is comprised of used in chromatography.
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    domain: ChromatographicSeparationProcess
    alias: stationary_phase
    owner: ChromatographicSeparationProcess
    domain_of:
    - ChromatographicSeparationProcess
    range: StationaryPhaseEnum
  temperature:
    name: temperature
    description: The value of a temperature measurement or temperature used in a process.
    notes:
    - Not to be confused with the MIXS:0000113
    from_schema: https://w3id.org/nmdc/nmdc
    contributors:
    - ORCID:0009-0001-1555-1601
    - ORCID:0000-0002-8683-0050
    rank: 1000
    alias: temperature
    owner: ChromatographicSeparationProcess
    domain_of:
    - SubSamplingProcess
    - ChromatographicSeparationProcess
    range: QuantityValue
  designated_class:
    name: designated_class
    comments:
    - required on all instances in a polymorphic Database slot like planned_process_set
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    designates_type: true
    alias: designated_class
    owner: ChromatographicSeparationProcess
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
    owner: ChromatographicSeparationProcess
    domain_of:
    - PlannedProcess
    range: string
  has_input:
    name: has_input
    description: An input to a process.
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    domain: NamedThing
    multivalued: true
    alias: has_input
    owner: ChromatographicSeparationProcess
    domain_of:
    - BiosampleProcessing
    - OmicsProcessing
    - WorkflowExecutionActivity
    - PlannedProcess
    range: NamedThing
    any_of:
    - range: Biosample
    - range: ProcessedSample
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
    owner: ChromatographicSeparationProcess
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
    owner: ChromatographicSeparationProcess
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
    owner: ChromatographicSeparationProcess
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
    owner: ChromatographicSeparationProcess
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
    owner: ChromatographicSeparationProcess
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
    owner: ChromatographicSeparationProcess
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
    owner: ChromatographicSeparationProcess
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
    owner: ChromatographicSeparationProcess
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
    owner: ChromatographicSeparationProcess
    domain_of:
    - Biosample
    - Study
    - NamedThing
    - MetaboliteQuantification
    range: uriorcurie
    pattern: ^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$

```
</details>