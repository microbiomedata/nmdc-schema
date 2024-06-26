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
_If your change **does** results in downstream changes, provide a justification/need for this change_
  - Examples of downstream changes include any change that requires an update or change to workflows, workflow automation, Postgres ingest, Jupyter notebooks, runtime, & more

Change this text to NONE if no downstream implication

## [optional] Are there any post deployment tasks we need to perform?







