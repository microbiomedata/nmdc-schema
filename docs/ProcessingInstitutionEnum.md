# Enum: ProcessingInstitutionEnum



URI: [ProcessingInstitutionEnum](ProcessingInstitutionEnum.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| UCSD | https://ror.org/0168r3w48 |  |
| JGI | https://ror.org/04xm1d337 |  |
| EMSL | https://ror.org/04rc0xn13 |  |
| Battelle | https://ror.org/01h5tnr73 |  |
| ANL | https://ror.org/05gvnxz63 |  |
| UCD_Genome_Center | https://genomecenter.ucdavis.edu/ |  |




## Slots

| Name | Description |
| ---  | --- |
| [processing_institution](processing_institution.md) | The organization that processed the sample |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: processing_institution_enum
notes:
- use ROR meanings like https://ror.org/0168r3w48 for UCSD
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
permissible_values:
  UCSD:
    text: UCSD
    meaning: https://ror.org/0168r3w48
    title: University of California, San Diego
  JGI:
    text: JGI
    meaning: https://ror.org/04xm1d337
    title: Joint Genome Institute
  EMSL:
    text: EMSL
    meaning: https://ror.org/04rc0xn13
    title: Environmental Molecular Sciences Laboratory
    aliases:
    - Environmental Molecular Science Laboratory
    - Environmental Molecular Sciences Lab
  Battelle:
    text: Battelle
    meaning: https://ror.org/01h5tnr73
    title: Battelle Memorial Institute
  ANL:
    text: ANL
    meaning: https://ror.org/05gvnxz63
    title: Argonne National Laboratory
  UCD_Genome_Center:
    text: UCD_Genome_Center
    meaning: https://genomecenter.ucdavis.edu/
    title: University of California, Davis Genome Center

```
</details>