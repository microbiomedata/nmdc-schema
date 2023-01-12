# Typecodes per class

Last generated 2023-01-12

If a class doesn't use the `id` slot, then there is no need to assign that class a typecode

Typecodes can be directly asserted for a class, or a class can inherit a typecode from one of its ancestors. This table
does not yet indicate when a typecode was inherited from an ancestor. An example of inheritance is 'acty'
for `WorkflowExecutionActivity`, which is inherited from it's ancestor `Activity`

Todo:

- Continue to add typecode to classes that are curently just inheriting general typecodes.
- Investigate which of these classes have identifiers that will actually appear on the Data Portal. Classes that are
  more behind-the-scenes (however were are going to rigorously define that) may require less deliberation.
- Automate build and deploy of this table

| class                               | uses_id | typecode |
|-------------------------------------|---------|----------|
| Activity                            | TRUE    | acty     |
| AnalyticalSample                    | TRUE    | nt       |
| Biosample                           | TRUE    | bsm      |
| BiosampleProcessing                 | TRUE    | bsmprc   |
| ChemicalEntity                      | TRUE    | nt       |
| CollectingBiosamplesFromSite        | TRUE    | nt       |
| DataObject                          | TRUE    | dobj     |
| EnvironmentalMaterialTerm           | TRUE    | nt       |
| FieldResearchSite                   | TRUE    | nt       |
| FunctionalAnnotationTerm            | TRUE    | nt       |
| GeneProduct                         | TRUE    | nt       |
| Instrument                          | TRUE    | nt       |
| MagsAnalysisActivity                | TRUE    | acty     |
| MaterialEntity                      | TRUE    | nt       |
| MaterialSample                      | TRUE    | nt       |
| MetabolomicsAnalysisActivity        | TRUE    | acty     |
| MetagenomeAnnotationActivity        | TRUE    | acty     |
| MetagenomeAssembly                  | TRUE    | acty     |
| MetaproteomicsAnalysisActivity      | TRUE    | acty     |
| MetatranscriptomeActivity           | TRUE    | acty     |
| MetatranscriptomeAnnotationActivity | TRUE    | acty     |
| MetatranscriptomeAssembly           | TRUE    | acty     |
| NamedThing                          | TRUE    | nt       |
| NomAnalysisActivity                 | TRUE    | acty     |
| OmicsProcessing                     | TRUE    | omprc    |
| OntologyClass                       | TRUE    | nt       |
| OrthologyGroup                      | TRUE    | nt       |
| Pathway                             | TRUE    | nt       |
| Person                              | TRUE    | nt       |
| PlannedProcess                      | TRUE    | nt       |
| Reaction                            | TRUE    | nt       |
| ReadBasedTaxonomyAnalysisActivity   | TRUE    | acty     |
| ReadQcAnalysisActivity              | TRUE    | acty     |
| Site                                | TRUE    | nt       |
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