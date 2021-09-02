# Change Log
Changes to the schema are documented in this file.

## Current (update before releasing)
### Added
  - slot `type` defined using `designates_type: true`
### Fixed
  - N/A
### Changed 
  - Linkml version updated to `1.0.4`
### Removed
  - N/A

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