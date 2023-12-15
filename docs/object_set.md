# Slot: object_set


_Applies to a property that links a database object to a set of objects. This is necessary in a json document to provide context for a list, and to allow for a single json object that combines multiple object types_



URI: [nmdc:object_set](https://w3id.org/nmdc/object_set)



<!-- no inheritance hierarchy -->






## Mixin Usage

| mixed into | description | range | domain |
| --- | --- | --- | --- |
| [planned_process_set](planned_process_set.md) | This property links a database object to the set of planned processes within ... | PlannedProcess | Database |
| [biosample_set](biosample_set.md) | This property links a database object to the set of samples within it | Biosample | Database |
| [study_set](study_set.md) | This property links a database object to the set of studies within it | Study | Database |
| [field_research_site_set](field_research_site_set.md) |  | FieldResearchSite | Database |
| [collecting_biosamples_from_site_set](collecting_biosamples_from_site_set.md) |  | CollectingBiosamplesFromSite | Database |
| [data_object_set](data_object_set.md) | This property links a database object to the set of data objects within it | DataObject | Database |
| [genome_feature_set](genome_feature_set.md) | This property links a database object to the set of all features | GenomeFeature | Database |
| [functional_annotation_set](functional_annotation_set.md) | This property links a database object to the set of all functional annotation... | FunctionalAnnotation | Database |
| [activity_set](activity_set.md) | This property links a database object to the set of workflow activities | WorkflowExecutionActivity | Database |
| [mags_activity_set](mags_activity_set.md) | This property links a database object to the set of MAGs analysis activities | MagsAnalysisActivity | Database |
| [metabolomics_analysis_activity_set](metabolomics_analysis_activity_set.md) | This property links a database object to the set of metabolomics analysis act... | MetabolomicsAnalysisActivity | Database |
| [metaproteomics_analysis_activity_set](metaproteomics_analysis_activity_set.md) | This property links a database object to the set of metaproteomics analysis a... | MetaproteomicsAnalysisActivity | Database |
| [metagenome_annotation_activity_set](metagenome_annotation_activity_set.md) | This property links a database object to the set of metagenome annotation act... | MetagenomeAnnotationActivity | Database |
| [metagenome_assembly_set](metagenome_assembly_set.md) | This property links a database object to the set of metagenome assembly activ... | MetagenomeAssembly | Database |
| [metagenome_sequencing_activity_set](metagenome_sequencing_activity_set.md) | This property links a database object to the set of metagenome sequencing act... | MetagenomeSequencingActivity | Database |
| [metatranscriptome_activity_set](metatranscriptome_activity_set.md) | This property links a database object to the set of metatranscriptome analysi... | MetatranscriptomeActivity | Database |
| [read_qc_analysis_activity_set](read_qc_analysis_activity_set.md) | This property links a database object to the set of read QC analysis activiti... | ReadQcAnalysisActivity | Database |
| [read_based_taxonomy_analysis_activity_set](read_based_taxonomy_analysis_activity_set.md) | This property links a database object to the set of read based analysis activ... | ReadBasedTaxonomyAnalysisActivity | Database |
| [nom_analysis_activity_set](nom_analysis_activity_set.md) | This property links a database object to the set of natural organic matter (N... | NomAnalysisActivity | Database |
| [omics_processing_set](omics_processing_set.md) | This property links a database object to the set of omics processings within ... | OmicsProcessing | Database |
| [pooling_set](pooling_set.md) |  | Pooling | Database |
| [processed_sample_set](processed_sample_set.md) | This property links a database object to the set of processed samples within ... | ProcessedSample | Database |
| [extraction_set](extraction_set.md) | This property links a database object to the set of extractions within it | Extraction | Database |
| [library_preparation_set](library_preparation_set.md) | This property links a database object to the set of DNA extractions within it | LibraryPreparation | Database |



## Properties

* Range: [String](String.md)

* Multivalued: True

* Mixin: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: object_set
description: Applies to a property that links a database object to a set of objects.
  This is necessary in a json document to provide context for a list, and to allow
  for a single json object that combines multiple object types
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
mixin: true
domain: Database
multivalued: true
alias: object_set
range: string
inlined_as_list: true

```
</details>