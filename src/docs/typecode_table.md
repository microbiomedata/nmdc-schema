# Typecodes per class

Last generated 2023-01-12

If a Class doesn't use the `id` slot, then there is no need to assign that class a typecode

Typecodes can be directly asserted for a class, or a class can inherit a typecode from one of it's ancestors. This table doe not yet indicate when a typecode was inherited from an ancestor. An example of inheritance is 'acty' for `WorkflowExecutionActivity`, which is inherited from it's ancestor `Activity`

| class                               | uses_id | typecode |
|-------------------------------------|---------|----------|
| Activity                            | TRUE    | acty     |
| AnalyticalSample                    | TRUE    |          |
| Biosample                           | TRUE    | bsm      |
| BiosampleProcessing                 | TRUE    | bsmprc   |
| ChemicalEntity                      | TRUE    |          |
| CollectingBiosamplesFromSite        | TRUE    |          |
| DataObject                          | TRUE    | dobj     |
| EnvironmentalMaterialTerm           | TRUE    |          |
| FieldResearchSite                   | TRUE    |          |
| FunctionalAnnotationTerm            | TRUE    |          |
| GeneProduct                         | TRUE    |          |
| Instrument                          | TRUE    |          |
| MagsAnalysisActivity                | TRUE    | acty     |
| MaterialEntity                      | TRUE    |          |
| MaterialSample                      | TRUE    |          |
| MetabolomicsAnalysisActivity        | TRUE    | acty     |
| MetagenomeAnnotationActivity        | TRUE    | acty     |
| MetagenomeAssembly                  | TRUE    | acty     |
| MetaproteomicsAnalysisActivity      | TRUE    | acty     |
| MetatranscriptomeActivity           | TRUE    | acty     |
| MetatranscriptomeAnnotationActivity | TRUE    | acty     |
| MetatranscriptomeAssembly           | TRUE    | acty     |
| NamedThing                          | TRUE    |          |
| NomAnalysisActivity                 | TRUE    | acty     |
| OmicsProcessing                     | TRUE    | omprc    |
| OntologyClass                       | TRUE    |          |
| OrthologyGroup                      | TRUE    |          |
| Pathway                             | TRUE    |          |
| Person                              | TRUE    |          |
| PlannedProcess                      | TRUE    |          |
| Reaction                            | TRUE    |          |
| ReadBasedTaxonomyAnalysisActivity   | TRUE    | acty     |
| ReadQcAnalysisActivity              | TRUE    | acty     |
| Site                                | TRUE    |          |
| Study                               | TRUE    | sty      |
| WorkflowExecutionActivity           | TRUE    | acty     |
| Agent                               | FALSE   |          |
| AttributeValue                      | FALSE   |          |
| BooleanValue                        | FALSE   |          |
| ControlledIdentifiedTermValue       | FALSE   |          |
| ControlledTermValue                 | FALSE   |          |
| CreditAssociation                   | FALSE   |          |
| Database                            | FALSE   |          |
| DissolvingActivity                  | FALSE   |          |
| FunctionalAnnotation                | FALSE   |          |
| GenomeFeature                       | FALSE   |          |
| GeolocationValue                    | FALSE   |          |
| ImageValue                          | FALSE   |          |
| IntegerValue                        | FALSE   |          |
| LabDevice                           | FALSE   |          |
| MagBin                              | FALSE   |          |
| MaterialContainer                   | FALSE   |          |
| MaterialSamplingActivity            | FALSE   |          |
| MetaboliteQuantification            | FALSE   |          |
| PeptideQuantification               | FALSE   |          |
| PersonValue                         | FALSE   |          |
| ProteinQuantification               | FALSE   |          |
| QuantityValue                       | FALSE   |          |
| ReactionActivity                    | FALSE   |          |
| ReactionParticipant                 | FALSE   |          |
| TextValue                           | FALSE   |          |
| TimestampValue                      | FALSE   |          |
| UrlValue                            | FALSE   |          |