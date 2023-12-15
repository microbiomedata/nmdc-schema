# Enum: BiosampleCategoryEnum




_Funding-based, sample location-based, or experimental method-based defined categories_



URI: [BiosampleCategoryEnum](BiosampleCategoryEnum.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| LTER | https://lternet.edu/ |  |
| SIP | None |  |
| SFA | https://science.osti.gov/ber/funding-opportunities/laboratory-scientific-focus-area-guidance | Science Focus Area projects funded through the Department of Energy Office of... |
| FICUS | https://jgi.doe.gov/user-programs/program-info/ficus-overview |  |
| NEON | https://www.neonscience.org |  |




## Slots

| Name | Description |
| ---  | --- |
| [biosample_categories](biosample_categories.md) |  |




## Aliases


* category tag



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: BiosampleCategoryEnum
description: Funding-based, sample location-based, or experimental method-based defined
  categories
notes:
- Currently, these values can associated with biosamples via the biosample_categories
  slot
- They might also be applicable to other classes
- They are intended to enable metadata search and or filtering, for example in the
  NMDC data portal, https://data.microbiomedata.org/
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- category tag
rank: 1000
permissible_values:
  LTER:
    text: LTER
    meaning: https://lternet.edu/
    title: National Science Foundation's Long Term Ecological Research Network
  SIP:
    text: SIP
  SFA:
    text: SFA
    description: Science Focus Area projects funded through the Department of Energy
      Office of Science Biological and Environmental Research Program
    meaning: https://science.osti.gov/ber/funding-opportunities/laboratory-scientific-focus-area-guidance
    title: Department of Energy Office of Science Biological and Environmental Research
      Program Laboratory Science Focus Areas
  FICUS:
    text: FICUS
    meaning: https://jgi.doe.gov/user-programs/program-info/ficus-overview
    title: Facilities Integrating Collaborations for User Science
  NEON:
    text: NEON
    meaning: https://www.neonscience.org
    title: National Science Foundation's National Ecological Observatory Network

```
</details>