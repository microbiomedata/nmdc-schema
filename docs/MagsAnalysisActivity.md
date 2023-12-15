# Class: Metagenome-Assembled Genome analysis activity (MagsAnalysisActivity)


_A workflow execution activity that uses computational binning tools to group assembled contigs into genomes_





URI: [nmdc:MagsAnalysisActivity](https://w3id.org/nmdc/MagsAnalysisActivity)




```mermaid
 classDiagram
    class MagsAnalysisActivity
      WorkflowExecutionActivity <|-- MagsAnalysisActivity
      
      MagsAnalysisActivity : binned_contig_num
        
      MagsAnalysisActivity : ended_at_time
        
      MagsAnalysisActivity : execution_resource
        
      MagsAnalysisActivity : git_url
        
      MagsAnalysisActivity : has_input
        
          MagsAnalysisActivity --|> NamedThing : has_input
        
      MagsAnalysisActivity : has_output
        
          MagsAnalysisActivity --|> NamedThing : has_output
        
      MagsAnalysisActivity : id
        
      MagsAnalysisActivity : input_contig_num
        
      MagsAnalysisActivity : low_depth_contig_num
        
      MagsAnalysisActivity : mags_list
        
          MagsAnalysisActivity --|> MagBin : mags_list
        
      MagsAnalysisActivity : name
        
      MagsAnalysisActivity : part_of
        
          MagsAnalysisActivity --|> NamedThing : part_of
        
      MagsAnalysisActivity : started_at_time
        
      MagsAnalysisActivity : too_short_contig_num
        
      MagsAnalysisActivity : type
        
      MagsAnalysisActivity : unbinned_contig_num
        
      MagsAnalysisActivity : used
        
      MagsAnalysisActivity : version
        
      MagsAnalysisActivity : was_informed_by
        
          MagsAnalysisActivity --|> Activity : was_informed_by
        
      
```





## Inheritance
* [Activity](Activity.md)
    * [WorkflowExecutionActivity](WorkflowExecutionActivity.md)
        * **MagsAnalysisActivity**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [type](type.md) | 1..1 <br/> [String](String.md) | An optional string that specifies the type object | direct |
| [input_contig_num](input_contig_num.md) | 0..1 <br/> [Integer](Integer.md) |  | direct |
| [binned_contig_num](binned_contig_num.md) | 0..1 <br/> [Integer](Integer.md) |  | direct |
| [too_short_contig_num](too_short_contig_num.md) | 0..1 <br/> [Integer](Integer.md) |  | direct |
| [low_depth_contig_num](low_depth_contig_num.md) | 0..1 <br/> [Integer](Integer.md) |  | direct |
| [unbinned_contig_num](unbinned_contig_num.md) | 0..1 <br/> [Integer](Integer.md) |  | direct |
| [mags_list](mags_list.md) | 0..* <br/> [MagBin](MagBin.md) |  | direct |
| [execution_resource](execution_resource.md) | 1..1 <br/> [String](String.md) |  | [WorkflowExecutionActivity](WorkflowExecutionActivity.md) |
| [git_url](git_url.md) | 1..1 <br/> [String](String.md) |  | [WorkflowExecutionActivity](WorkflowExecutionActivity.md) |
| [has_input](has_input.md) | 1..* <br/> [NamedThing](NamedThing.md) | An input to a process | [WorkflowExecutionActivity](WorkflowExecutionActivity.md) |
| [has_output](has_output.md) | 1..* <br/> [NamedThing](NamedThing.md) | An output biosample to a processing step | [WorkflowExecutionActivity](WorkflowExecutionActivity.md) |
| [part_of](part_of.md) | 0..* <br/> [NamedThing](NamedThing.md) | Links a resource to another resource that either logically or physically incl... | [WorkflowExecutionActivity](WorkflowExecutionActivity.md) |
| [version](version.md) | 0..1 <br/> [String](String.md) |  | [WorkflowExecutionActivity](WorkflowExecutionActivity.md) |
| [id](id.md) | 1..1 <br/> [Uriorcurie](Uriorcurie.md) | A unique identifier for a thing | [Activity](Activity.md) |
| [name](name.md) | 0..1 <br/> [String](String.md) | A human readable label for an entity | [Activity](Activity.md) |
| [started_at_time](started_at_time.md) | 1..1 <br/> [String](String.md) |  | [Activity](Activity.md) |
| [ended_at_time](ended_at_time.md) | 1..1 <br/> [String](String.md) |  | [Activity](Activity.md) |
| [was_informed_by](was_informed_by.md) | 0..1 <br/> [Activity](Activity.md) |  | [Activity](Activity.md) |
| [used](used.md) | 0..1 <br/> [String](String.md) |  | [Activity](Activity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Database](Database.md) | [mags_activity_set](mags_activity_set.md) | range | [MagsAnalysisActivity](MagsAnalysisActivity.md) |
| [MagsAnalysisActivity](MagsAnalysisActivity.md) | [mags_list](mags_list.md) | domain | [MagsAnalysisActivity](MagsAnalysisActivity.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nmdc:MagsAnalysisActivity |
| native | nmdc:MagsAnalysisActivity |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MagsAnalysisActivity
description: A workflow execution activity that uses computational binning tools to
  group assembled contigs into genomes
title: Metagenome-Assembled Genome analysis activity
in_subset:
- workflow subset
from_schema: https://w3id.org/nmdc/nmdc
is_a: WorkflowExecutionActivity
slots:
- type
- input_contig_num
- binned_contig_num
- too_short_contig_num
- low_depth_contig_num
- unbinned_contig_num
- mags_list
slot_usage:
  id:
    name: id
    domain_of:
    - Biosample
    - Study
    - NamedThing
    - Activity
    required: true
    structured_pattern:
      syntax: '{id_nmdc_prefix}:wfmag-{id_shoulder}-{id_blade}{id_version}{id_locus}'
      interpolated: true

```
</details>

### Induced

<details>
```yaml
name: MagsAnalysisActivity
description: A workflow execution activity that uses computational binning tools to
  group assembled contigs into genomes
title: Metagenome-Assembled Genome analysis activity
in_subset:
- workflow subset
from_schema: https://w3id.org/nmdc/nmdc
is_a: WorkflowExecutionActivity
slot_usage:
  id:
    name: id
    domain_of:
    - Biosample
    - Study
    - NamedThing
    - Activity
    required: true
    structured_pattern:
      syntax: '{id_nmdc_prefix}:wfmag-{id_shoulder}-{id_blade}{id_version}{id_locus}'
      interpolated: true
attributes:
  type:
    name: type
    description: An optional string that specifies the type object.  This is used
      to allow for searches for different kinds of objects.
    deprecated: Due to confusion about what values are used for this slot, it is best
      not to use this slot. See https://github.com/microbiomedata/nmdc-schema/issues/248.
      MAM removed designates_type and rdf:type slot uri 2022-11-30
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    alias: type
    owner: MagsAnalysisActivity
    domain_of:
    - DataObject
    - Biosample
    - Study
    - OmicsProcessing
    - CreditAssociation
    - WorkflowExecutionActivity
    - MetagenomeAssembly
    - MetagenomeAnnotationActivity
    - MetatranscriptomeAnnotationActivity
    - MetatranscriptomeActivity
    - MagsAnalysisActivity
    - ReadQcAnalysisActivity
    - ReadBasedTaxonomyAnalysisActivity
    - MagBin
    - GenomeFeature
    range: string
    required: true
  input_contig_num:
    name: input_contig_num
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    alias: input_contig_num
    owner: MagsAnalysisActivity
    domain_of:
    - MagsAnalysisActivity
    range: integer
  binned_contig_num:
    name: binned_contig_num
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    alias: binned_contig_num
    owner: MagsAnalysisActivity
    domain_of:
    - MagsAnalysisActivity
    range: integer
  too_short_contig_num:
    name: too_short_contig_num
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    alias: too_short_contig_num
    owner: MagsAnalysisActivity
    domain_of:
    - MagsAnalysisActivity
    range: integer
  low_depth_contig_num:
    name: low_depth_contig_num
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    alias: low_depth_contig_num
    owner: MagsAnalysisActivity
    domain_of:
    - MagsAnalysisActivity
    range: integer
  unbinned_contig_num:
    name: unbinned_contig_num
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    alias: unbinned_contig_num
    owner: MagsAnalysisActivity
    domain_of:
    - MagsAnalysisActivity
    range: integer
  mags_list:
    name: mags_list
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    domain: MagsAnalysisActivity
    multivalued: true
    alias: mags_list
    owner: MagsAnalysisActivity
    domain_of:
    - MagsAnalysisActivity
    range: MagBin
  execution_resource:
    name: execution_resource
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    domain: Activity
    alias: execution_resource
    owner: MagsAnalysisActivity
    domain_of:
    - WorkflowExecutionActivity
    range: string
    required: true
  git_url:
    name: git_url
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    alias: git_url
    owner: MagsAnalysisActivity
    domain_of:
    - WorkflowExecutionActivity
    range: string
    required: true
  has_input:
    name: has_input
    description: An input to a process.
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    domain: NamedThing
    multivalued: true
    alias: has_input
    owner: MagsAnalysisActivity
    domain_of:
    - BiosampleProcessing
    - OmicsProcessing
    - WorkflowExecutionActivity
    - PlannedProcess
    range: NamedThing
    required: true
  has_output:
    name: has_output
    description: An output biosample to a processing step
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    domain: NamedThing
    multivalued: true
    alias: has_output
    owner: MagsAnalysisActivity
    domain_of:
    - OmicsProcessing
    - WorkflowExecutionActivity
    - PlannedProcess
    range: NamedThing
    required: true
  part_of:
    name: part_of
    description: Links a resource to another resource that either logically or physically
      includes it.
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - is part of
    rank: 1000
    domain: NamedThing
    slot_uri: dcterms:isPartOf
    multivalued: true
    alias: part_of
    owner: MagsAnalysisActivity
    domain_of:
    - FieldResearchSite
    - Biosample
    - Study
    - OmicsProcessing
    - WorkflowExecutionActivity
    range: NamedThing
  version:
    name: version
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    domain: Activity
    alias: version
    owner: MagsAnalysisActivity
    domain_of:
    - WorkflowExecutionActivity
    - ReadQcAnalysisActivity
    range: string
  id:
    name: id
    description: A unique identifier for a thing. Must be either a CURIE shorthand
      for a URI or a complete URI
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    identifier: true
    alias: id
    owner: MagsAnalysisActivity
    domain_of:
    - Biosample
    - Study
    - NamedThing
    - Activity
    range: uriorcurie
    required: true
    pattern: ^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$
    structured_pattern:
      syntax: '{id_nmdc_prefix}:wfmag-{id_shoulder}-{id_blade}{id_version}{id_locus}'
      interpolated: true
  name:
    name: name
    description: A human readable label for an entity
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    alias: name
    owner: MagsAnalysisActivity
    domain_of:
    - Protocol
    - QualityControlReport
    - NamedThing
    - PersonValue
    - Activity
    range: string
  started_at_time:
    name: started_at_time
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    domain: Activity
    alias: started_at_time
    owner: MagsAnalysisActivity
    domain_of:
    - Activity
    range: string
    required: true
    pattern: ^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$
  ended_at_time:
    name: ended_at_time
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    domain: Activity
    alias: ended_at_time
    owner: MagsAnalysisActivity
    domain_of:
    - Activity
    range: string
    required: true
    pattern: ^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$
  was_informed_by:
    name: was_informed_by
    from_schema: https://w3id.org/nmdc/nmdc
    mappings:
    - prov:wasInformedBy
    rank: 1000
    domain: Activity
    alias: was_informed_by
    owner: MagsAnalysisActivity
    domain_of:
    - Activity
    range: Activity
  used:
    name: used
    from_schema: https://w3id.org/nmdc/nmdc
    mappings:
    - prov:used
    rank: 1000
    domain: Activity
    alias: used
    owner: MagsAnalysisActivity
    domain_of:
    - Activity
    range: string

```
</details>