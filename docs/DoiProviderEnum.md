# Enum: DoiProviderEnum



URI: [DoiProviderEnum](DoiProviderEnum.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| emsl | https://ror.org/04rc0xn13 |  |
| jgi | https://ror.org/04xm1d337 |  |
| kbase | https://ror.org/01znn6x10 |  |
| osti | https://ror.org/031478740 |  |
| ess_dive | https://ror.org/01t14bp54 |  |
| massive | None |  |
| gsc | None |  |
| zenodo | None |  |
| edi | https://ror.org/0330j0z60 |  |




## Slots

| Name | Description |
| ---  | --- |
| [doi_provider](doi_provider.md) | The authority, or organization, the DOI is associated with |






## See Also

* [nmdc:ProcessingInstitutionEnum](https://w3id.org/nmdc/ProcessingInstitutionEnum)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: DoiProviderEnum
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- nmdc:ProcessingInstitutionEnum
rank: 1000
permissible_values:
  emsl:
    text: emsl
    meaning: https://ror.org/04rc0xn13
    title: EMSL
    aliases:
    - Environmental Molecular Sciences Laboratory
    - EMSL
  jgi:
    text: jgi
    meaning: https://ror.org/04xm1d337
    title: JGI
    aliases:
    - Joint Genome Institute
    - JGI
  kbase:
    text: kbase
    meaning: https://ror.org/01znn6x10
    title: KBase
    aliases:
    - KBase
  osti:
    text: osti
    meaning: https://ror.org/031478740
    title: OSTI
    aliases:
    - Office of Scientific and Technical Information
    - OSTI
  ess_dive:
    text: ess_dive
    meaning: https://ror.org/01t14bp54
    title: ESS-DIVE
    aliases:
    - ESS-DIVE
    - Environmental System Science Data Infrastructure for a Virtual Ecosystem
  massive:
    text: massive
    title: MassIVE
    aliases:
    - MassIVE
    - Mass Spectrometry Virtual Environment
  gsc:
    text: gsc
    title: GSC
    aliases:
    - GSC
    - Genomic Standards Consortium
  zenodo:
    text: zenodo
    title: Zenodo
    aliases:
    - Zenodo
  edi:
    text: edi
    meaning: https://ror.org/0330j0z60
    title: EDI
    aliases:
    - EDI
    - Environmental Data Initiative

```
</details>