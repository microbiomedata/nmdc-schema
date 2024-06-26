# Guidelines

## _Light_ Schema Freeze
The nmdc-schema and berkeley-schema are under a light freeze this means changes **should not** be made that have any down stream implications. To ensure this, PRs need to be closely reviewed with **every** component of the NMDC in mind.

## Reviewers
To ensure no changes are made unexpectedly, ALL berkeley-schema refacror roll out task coordinators should be listed as reviewrs for ALL PRs. See [squad proposal](https://docs.google.com/document/d/1XXN1YuaBuSkxPXeiLKm5YxYzXTamBPQrzzeLhlh7PWs/edit#heading=h.u52g8v319adh) for list of names

PRs should NOT be merged until they have been approved by all task coordinators.

# PR Informtion
## What type of PR is this? (check all applicable)

- [ ] Refactor
- [ ] Feature
- [ ] Bug Fix
- [ ] Optimization
- [ ] Documentation Update
- [ ] Content change
    - slot or Class name
  - slot multiplicity changes (from a single value to a list or vice versa)
  - slot movement from one Class to another
  - creating a new slot/Class
  - Enum value changes
- [ ] Informitive change
  - descriptions of slots, classes, or enums
  - removal of unused, commented, or invalid code
  - updated mappings of terms, classes, or slots to ontologies
  - added an additional Enum to accommodate new or future metadata.
- [ ] changes to ANY files in /src/schema
     


## Description 
_PRs should be small and concise_

Delete this task and provide a describion of what this PR is accomplishing

## Related Tickets & Documents
_All pull requests should relate to or close an issue, please include them below._

- Related Issue #
- Closes #

## Added/updated tests?

- [ ] Yes
- [ ] No, and this is why: _please replace this line with details on why tests
      have not been included_
- [ ] I need help with writing tests

## Will this change to the schema result in any invalid data?

- [ ] Yes _Migration Required_
- [ ] No 
- [ ] Unsure

## Migration Required?
_**Ideally**, no additional migrations will be performed with the schema soft freeze_

- [ ] Yes
- [ ] No
- [ ] Unsure

Migrations are required if the change results in any existing data being no longer valid. This includes 1) slot or Class name changes 2) slot multiplicity changes (from a single value to a list or vice versa) 3) slot movement from one Class to another 4) Enum value changes.

## Downstream implications

_**Ideally** no schema changes will be performed that have down stream implications._

_If your change **does** results in downstream changes, provide a justification/need for this change_ >-

_Examples of downstream changes include any change that requires an update or change to workflows, workflow automation, Postgres ingest, Jupyter notebooks, runtime, & more_

- Change this text to NONE if no downstream implication

## [optional] Are there any post deployment tasks we need to perform?

Add 







