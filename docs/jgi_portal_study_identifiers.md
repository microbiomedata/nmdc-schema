# Slot: JGI Portal Study identifiers (jgi_portal_study_identifiers)


_Identifiers that link a NMDC study to a website hosting raw and analyzed data for a JGI proposal.  The suffix of the curie can used to query the GOLD API and is interoperable with an award DOI from OSTI and a GOLD study identifier._



URI: [nmdc:jgi_portal_study_identifiers](https://w3id.org/nmdc/jgi_portal_study_identifiers)




## Inheritance

* [alternative_identifiers](alternative_identifiers.md)
    * [external_database_identifiers](external_database_identifiers.md)
        * [study_identifiers](study_identifiers.md)
            * **jgi_portal_study_identifiers** [ [jgi_portal_identifiers](jgi_portal_identifiers.md)]





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Study](Study.md) | A study summarizes the overall goal of a research initiative and outlines the... |  no  |







## Properties

* Range: [ExternalIdentifier](ExternalIdentifier.md)

* Multivalued: True

* Regex pattern: `^jgi.proposal:\d+$`






## Examples

| Value |
| --- |
| jgi.proposal:507130 |

## Comments

* Could this could be considered a related identifier?
* Curie suffix is the Site Award Number from an OSTI award page
* Site Award Number 507130 == award doi doi:10.46936/10.25585/60000017 -- GOLD study identifier gold:Gs0154044
* bioregistry.io/jgi.proposal:507130 ==https://genome.jgi.doe.gov/portal/BioDefcarcycling/BioDefcarcycling.info.html

## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* jgi.proposal








### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: jgi_portal_study_identifiers
id_prefixes:
- jgi.proposal
description: Identifiers that link a NMDC study to a website hosting raw and analyzed
  data for a JGI proposal.  The suffix of the curie can used to query the GOLD API
  and is interoperable with an award DOI from OSTI and a GOLD study identifier.
title: JGI Portal Study identifiers
comments:
- Could this could be considered a related identifier?
- Curie suffix is the Site Award Number from an OSTI award page
- Site Award Number 507130 == award doi doi:10.46936/10.25585/60000017 -- GOLD study
  identifier gold:Gs0154044
- bioregistry.io/jgi.proposal:507130 ==https://genome.jgi.doe.gov/portal/BioDefcarcycling/BioDefcarcycling.info.html
examples:
- value: jgi.proposal:507130
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
is_a: study_identifiers
mixins:
- jgi_portal_identifiers
domain: Study
multivalued: true
alias: jgi_portal_study_identifiers
domain_of:
- Study
range: external_identifier
pattern: ^jgi.proposal:\d+$

```
</details>