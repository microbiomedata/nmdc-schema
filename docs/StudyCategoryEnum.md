# Enum: StudyCategoryEnum



URI: [StudyCategoryEnum](StudyCategoryEnum.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| research_study | None | A detailed examination, analysis, or critical inspection of a hypothesis-driv... |
| consortium | None | A group formed to undertake a venture that is beyond the capabilities of the ... |




## Slots

| Name | Description |
| ---  | --- |
| [study_category](study_category.md) | The type of research initiative |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: StudyCategoryEnum
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
permissible_values:
  research_study:
    text: research_study
    description: A detailed examination, analysis, or critical inspection of a hypothesis-driven
      experiment.
    exact_mappings:
    - SIO:001066
    - NCIT:C63536
    - ISA:Study
    close_mappings:
    - OBI:0000355
  consortium:
    text: consortium
    description: A group formed to undertake a venture that is beyond the capabilities
      of the individual members. Each member of the  consortium brings a high level
      of expertise in a specific area to ensure the successful completion of the project.
    comments:
    - A consortium has collections of data, those data do not come from a hypothesis-driven
      experiment.
    exact_mappings:
    - NCIT:C61538

```
</details>