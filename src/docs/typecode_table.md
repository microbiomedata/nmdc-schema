# Typecodes per class

Last generated 2023-01-12

If a Class doesn't use the `id` slot, then there is no need to assign that class a typecode

Typecodes can be directly asserted for a class, or a class can inherit a typecode from one of it's ancestors. This table doe not yet indicate when a typecode was inherited from an ancestor. An example of inheritance is 'acty' for `WorkflowExecutionActivity`, which is inherited from it's ancestor `Activity`



| class                               | uses_id | from_ancestor                       | typecode |
|-------------------------------------|---------|-------------------------------------|----------|
| Activity                            | True    | Activity                            | acty     |
| Agent                               | False   |                                     |          |
| AnalyticalSample                    | True    | AnalyticalSample                    |          |
| AttributeValue                      | False   |                                     |          |
| Biosample                           | True    | Biosample                           | bsm      |
| BiosampleProcessing                 | True    | BiosampleProcessing                 | bsmprc   |
| BooleanValue                        | False   |                                     |          |
| ChemicalEntity                      | True    | ChemicalEntity                      |          |
| CollectingBiosamplesFromSite        | True    | CollectingBiosamplesFromSite        |          |
| ControlledIdentifiedTermValue       | False   |                                     |          |
| ControlledTermValue                 | False   |                                     |          |
| CreditAssociation                   | False   |                                     |          |
| DataObject                          | True    | DataObject                          | dobj     |
| Database                            | False   |                                     |          |
| DissolvingActivity                  | False   |                                     |          |
| EnvironmentalMaterialTerm           | True    | EnvironmentalMaterialTerm           |          |
| FieldResearchSite                   | True    | FieldResearchSite                   |          |
| FunctionalAnnotation                | False   |                                     |          |
| FunctionalAnnotationTerm            | True    | FunctionalAnnotationTerm            |          |
| GeneProduct                         | True    | GeneProduct                         |          |
| GenomeFeature                       | False   |                                     |          |
| GeolocationValue                    | False   |                                     |          |
| ImageValue                          | False   |                                     |          |
| Instrument                          | True    | Instrument                          |          |
| IntegerValue                        | False   |                                     |          |
| LabDevice                           | False   |                                     |          |
| MagBin                              | False   |                                     |          |
| MagsAnalysisActivity                | True    | MagsAnalysisActivity                | acty     |
| MaterialContainer                   | False   |                                     |          |
| MaterialEntity                      | True    | MaterialEntity                      |          |
| MaterialSample                      | True    | MaterialSample                      |          |
| MaterialSamplingActivity            | False   |                                     |          |
| MetaboliteQuantification            | False   |                                     |          |
| MetabolomicsAnalysisActivity        | True    | MetabolomicsAnalysisActivity        | acty     |
| MetagenomeAnnotationActivity        | True    | MetagenomeAnnotationActivity        | acty     |
| MetagenomeAssembly                  | True    | MetagenomeAssembly                  | acty     |
| MetaproteomicsAnalysisActivity      | True    | MetaproteomicsAnalysisActivity      | acty     |
| MetatranscriptomeActivity           | True    | MetatranscriptomeActivity           | acty     |
| MetatranscriptomeAnnotationActivity | True    | MetatranscriptomeAnnotationActivity | acty     |
| MetatranscriptomeAssembly           | True    | MetatranscriptomeAssembly           | acty     |
| NamedThing                          | True    | NamedThing                          |          |
| NomAnalysisActivity                 | True    | NomAnalysisActivity                 | acty     |
| OmicsProcessing                     | True    | OmicsProcessing                     | omprc    |
| OntologyClass                       | True    | OntologyClass                       |          |
| OrthologyGroup                      | True    | OrthologyGroup                      |          |
| Pathway                             | True    | Pathway                             |          |
| PeptideQuantification               | False   |                                     |          |
| Person                              | True    | Person                              |          |
| PersonValue                         | False   |                                     |          |
| PlannedProcess                      | True    | PlannedProcess                      |          |
| ProteinQuantification               | False   |                                     |          |
| QuantityValue                       | False   |                                     |          |
| Reaction                            | True    | Reaction                            |          |
| ReactionActivity                    | False   |                                     |          |
| ReactionParticipant                 | False   |                                     |          |
| ReadBasedTaxonomyAnalysisActivity   | True    | ReadBasedTaxonomyAnalysisActivity   | acty     |
| ReadQcAnalysisActivity              | True    | ReadQcAnalysisActivity              | acty     |
| Site                                | True    | Site                                |          |
| Study                               | True    | Study                               | sty      |
| TextValue                           | False   |                                     |          |
| TimestampValue                      | False   |                                     |          |
| UrlValue                            | False   |                                     |          |
| WorkflowExecutionActivity           | True    | WorkflowExecutionActivity           | acty     |