# Change Log
Changes to the schema are documented in this file.

## Current (updates before releasing)
### Added
  - N/A
### Fixed
  - N/A
### Changed 
  - N/A
### Removed
  - N/A

## [2021.10.13rc2](https://github.com/microbiomedata/nmdc-schema/releases/tag/2021.10.13rc2)
### Added
  - command line utility `fetch-nmdc-schema` for downloading the jsonschema
### Fixed
  - `nmdc-version` command line utility (#183)
### Changed 
  - N/A
### Removed
  - N/A

## [2021.10.13rc1](https://github.com/microbiomedata/nmdc-schema/releases/tag/2021.10.13rc1)
### Added
  - N/A
### Fixed
  - N/A
### Changed 
  - N/A
### Removed
  - regex patterns for `has function` slot on class `function annotation` (#178)

## [2021.10.12rc2](https://github.com/microbiomedata/nmdc-schema/releases/tag/2021.10.12rc2)
### Added
  - `part of` slot for `workflow execution activity` (#176)
### Fixed
  - N/A
### Changed 
  - N/A
### Removed
  - N/A

## [2021.10.12rc1](https://github.com/microbiomedata/nmdc-schema/releases/tag/2021.10.12rc1)
### Added
  - N/A
### Fixed
  - descriptions are inherited in induced slots (#174)
### Changed 
  - N/A
### Removed
  - N/A

## [2021.09.30rc3](https://github.com/microbiomedata/nmdc-schema/releases/tag/2021.09.30rc3)
### Added
  - N/A
### Fixed
  - N/A
### Changed 
  - re-added `part of` constraint to `slot_usage` section of `biosample` (#163)
### Removed
  - N/A

## [2021.09.30rc2](https://github.com/microbiomedata/nmdc-schema/releases/tag/2021.09.30rc2)
### Added
  - N/A
### Fixed
  - N/A
### Changed 
  - removed `part of` from `slot_usage` section of `biosample` (#163)
### Removed
  - N/A

## [2021.09.30rc1](https://github.com/microbiomedata/nmdc-schema/releases/tag/2021.09.30rc1)
### Added
  - `part of` to slot section of `biosample` (#163)
### Fixed
  - N/A
### Changed 
  - N/A
### Removed
  - N/A

## [2021.09.28rc2](https://github.com/microbiomedata/nmdc-schema/releases/tag/2021.09.28rc2)
### Added
  - `websites` slot to `person value`
### Fixed
  - N/A
### Changed 
  - `has output` is not required for `omics processing`
### Removed
  - N/A

## [2021.09.28rc1](https://github.com/microbiomedata/nmdc-schema/releases/tag/2021.09.28rc1)
### Added
  - `relevant protocols` and `funding sources` slots
  - `ess dive datasets` slot
  - amplicon slots to omics processing (#139)
  - `alternate emails` slot
### Fixed
  - N/A
### Changed 
  - `email` slot is single valued.
### Removed
  - N/A

## [2021.09.21rc1](https://github.com/microbiomedata/nmdc-schema/releases/tag/2021.09.21rc1)
### Added
  - `CreditAssociation` class and related slots. Abstracts the roles borne by people within a strudy.
  - `email` slot in `core.yaml`. Motivation = people (`person value`) associated with studies, but not constrained to that domain (cf. #100).
      - `email` made multivalued and assigned schema.org URI
  - slot `type` defined using `designates_type: true`
  - `name` slot added to `person value`. Noted that `has raw value` could be deprecated in the future.
  - All `yaml` files are included in the package data (#153)
### Fixed
  - added `name` and `title` to `mixs.yaml` (#126)
### Changed 
  - Linkml version updated to `1.0.4`
  - `alternate identifiers` to `alternative identifiers` (#125)
### Removed
  - `alternate identifiers` slot (#125)

## [2021.07.01rc1](https://github.com/microbiomedata/nmdc-schema/releases/tag/2021.07.01rc1)
### Added
  - `metatranscriptome activity` class and `metatranscriptome activity set`
### Fixed
  - N/A
### Changed 
  - N/A
### Removed
  - N/A

## [2021.06.24rc1](https://github.com/microbiomedata/nmdc-schema/releases/tag/2021.06.24rc1)
### Added
  - `depth2` and `subsurface_depth2` slots added to biosamples (cf. issue 80).
### Fixed
  - N/A
### Changed 
  - N/A
### Removed
  - N/A

## [2021.06.23rc1](https://github.com/microbiomedata/nmdc-schema/releases/tag/2021.06.23rc1)
### Added
  - `alternative identifiers` slot added to biosamples (cf. issue 75).
### Fixed
  - N/A
### Changed 
  - N/A
### Removed
  - N/A

## [2021.06.17rc1](https://github.com/microbiomedata/nmdc-schema/releases/tag/2021.06.16rc1)
### Added
  - `profile image url` to hold the url pointing an image of the investigator (cf. issue 19)
  - description for `orcid` slot.
### Fixed
  - N/A
### Changed 
  - `principal investigator name` to simply be `principal investigator`.
### Removed
  - N/A

## [2021.06.16rc1](https://github.com/microbiomedata/nmdc-schema/releases/tag/2021.06.16rc1)
### Added
  - `title` slot as attribute of `nmdc:study` (cf. issue 51)
  - `objective` slot as attribute of `nmdc:study` (cf. issue 51)
  - `alternative titles` slot as attribute of `nmdc:study` (cf. issue 51)
  - `alternative dscriptiions` slot as attribute of `nmdc:study` (cf. issue 51)
  - `alternative names` slot as attribute of `nmdc:study` (cf. issue 51)
  - `keywords` slot as attribute of `nmdc:study` (cf. issue 51)
  - `websites` slot as attribute of `nmdc:study` (cf. issue 51)
  - `publications` slot as attribute of `nmdc:study` (cf. issue 51)
  - `skos` prefix to `core` and mapping for `alternative names` to `skos:altLabel`
  - `samp_mat_process` slot as attribute of `nmdc:biosample` (cf. issue 67)
### Fixed
  - N/A
### Changed 
  - N/A
### Removed
  - N/A

## [2021.06.10rc1](https://github.com/microbiomedata/nmdc-schema/releases/tag/2021.06.10rc1)
### Added
  - `abstract` slot for use with `study` (cf. issue 60)
### Fixed
  - N/A
### Changed
  - N/A
### Removed
  - N/A

## [2021.06.01rc2](https://github.com/microbiomedata/nmdc-schema/releases/tag/2021.06.01rc2)
### Added
  - N/A
### Fixed
  - N/A
### Changed
  - `part of`, `has input`, `has output` slots are required for `omics processing` objects (cf. issue 50)
  - `name`, `description` slots required for `data object` objects (cf. issue 50)
  - `git url`, `has input`, `has output`, `was informed by`, `execution resource`, `type` slots required for `workflow execution activity` objects (cf. issue 50)
### Removed
  - N/A

## [2021.06.01rc1](https://github.com/microbiomedata/nmdc-schema/releases/tag/2021.06.01rc1)
### Added
  - N/A
### Fixed
  - N/A
### Changed
  - MIxS triad properties required for biosamples (cf. issue 45)
  - `started at time` and `ended at time` properties required for workflow execution activities (cf. issue 44)
### Removed
  - N/A

## [2021.04.28rc1](https://github.com/microbiomedata/nmdc-schema/releases/tag/2021.04.28rc1)
### Added
  - New class: metatranscriptome assembly
  - New class: metatranscriptome annotation activity
### Fixed
  - N/A
### Changed
  - Updated `part of` slot to biosample to relate biosamples to the studies for which they were collected.
### Removed
  - N/A

## [2021.04.22rc1](https://github.com/microbiomedata/nmdc-schema/releases/tag/2021.04.22rc1)
### Added
  - Example data to test validation
### Fixed
  - N/A
### Changed
  - Updated `part of` slot to biosample to relate biosamples to the studies for which they were collected.
### Removed
  - N/A

## [2021.04.16rc1](https://github.com/microbiomedata/nmdc-schema/releases/tag/2021.04.16rc1)
### Added
  - N/A
### Fixed
  - N/A
### Changed
  - Enhance command-line nmdc-version tool to get metamodel version.
### Removed
  - N/A

## [2021.04.15rc3](https://github.com/microbiomedata/nmdc-schema/releases/tag/2021.04.15rc3)
### Added
  - `nmdc.yaml` to package data files
### Fixed
  - N/A
### Changed
  - N/A
### Removed
  - N/A

## [2021.04.15rc2](https://github.com/microbiomedata/nmdc-schema/releases/tag/2021.04.15rc2)
### Added
  - `nmdc-version` command-line tool to find out the nmdc schema version
### Fixed
  - N/A
### Changed
  - N/A
### Removed
  - N/A
  
## [20210414](https://github.com/microbiomedata/nmdc-schema/releases/tag/20210414)
### Added
  - SSSOM mapping file for mapping GOLD to MIxS
### Fixed
  - N/A
### Changed
  - Update `python-publish.yml`
### Removed
  - N/A

## [2021.04.15rc1](https://github.com/microbiomedata/nmdc-schema/releases/tag/2021.04.15rc1)
### Added
  - Command-line json validation tool validate-nmdc-json
### Fixed
  - N/A
### Changed
  - N/A
### Removed
  - N/A

## [2021.04.14](https://github.com/microbiomedata/nmdc-schema/releases/tag/2021.04.14)
### Added
  - N/A
### Fixed
  - N/A
### Changed
  - Update `python-publish.yml`
### Removed
  - N/A
 
## [2021.04.14rc2](https://github.com/microbiomedata/nmdc-schema/releases/tag/2021.04.14rc2)
### Added
  - SSSOM file to package
### Fixed
  - N/A
### Changed
  - N/A
### Removed
  - N/A

## [2021.04.14rc1](https://github.com/microbiomedata/nmdc-schema/releases/tag/2021.04.14rc1)
### Added
  - N/A
### Fixed
  - N/A
### Changed
  - Update `python-publish.yml`
### Removed
  - N/A
