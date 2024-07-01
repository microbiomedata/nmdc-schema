# Guidelines

## _Soft_ Schema Freeze

The `nmdc-schema` and `berkeley-schema-fy24` schemas are under a light freeze, which means changes **should not** be made that have any downstream implications. To ensure this, all PRs created creating during the freeze will be closely reviewed with **every** component of the NMDC system in mind.

## Reviewers

To ensure no changes are made unexpectedly, PR creators will request reviews from _all_ [Berkeley Schema Roll Out task coordinators](https://docs.google.com/document/d/1XXN1YuaBuSkxPXeiLKm5YxYzXTamBPQrzzeLhlh7PWs/edit#heading=h.u52g8v319adh).

We expect task coordinators to review PRs and provide feedback/approval within 1 week of when they are identified as reviewers. Expedition, questions, and discussion can happen at any meeting.

PRs should **NOT** be merged until they have been approved by all task coordinators.

# PR Information

## What type of PR is this? (check all applicable)

- [ ] Refactor
- [ ] Feature
- [ ] Bug Fix
- [ ] Optimization
- [ ] Documentation
- [ ] Schema change: Content
  - slot or class name
  - slot multiplicity changes (from a single value to a list or vice versa)
  - slot movement from one class to another
  - creating a new slot/Class
  - Enum value changes
- [ ] Schema change: Cleanup
  - descriptions of slots, classes, or enums
  - removal of unused, commented, or invalid code
  - updated mappings of terms, classes, or slots to ontologies
  - added an additional Enum to accommodate new or future metadata
- [ ] Changes to any files or directories in `src/schema`
     
## Description

> _PRs should be [small and concise](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/best-practices-for-pull-requests#write-small-prs)._
>
> Aim to create small, focused pull requests that fulfill a single purpose. Smaller pull requests are easier and faster to review and merge, leave less room to introduce bugs, and provide a clearer history of changes.

- Replace this text with a description of what this PR branch contains. Please keep in mind that all reviewers will be reading this description. Example: "In this branch, I..."

## Related Tickets & Documents

> All PRs should relate to or fix an issue(s). Please identify the issue(s) below.

- Related Issue(s): #
- Fixes: #

## Did you add/update any tests?

- [ ] Yes
- [ ] No _(Add a justification below)_
- [ ] I need help with writing tests

## Could this schema change make it so any valid data becomes invalid?

> This is a question about what the schema allows. It is not a question about what happens to exists in the NMDC database right now.
> 
> Example: If, in this PR branch, you renamed a slot named `foo` to `foo_bar`, the answer to this question would be "yes," **even if** nothing in the NMDC database _currently_ uses the `foo` slot.
>
> More examples: slot or class name changes, slot multiplicity changes (e.g. string versus list), slot movement from one class to another, some kinds of enum value changes.

- [ ] Yes _(A migrator is required)_
- [ ] No
- [ ] I need help determining this

## If you answered "Yes", does this PR branch include that migrator?

- [ ] Yes
- [ ] No, this PR is incomplete and I need help writing the migrator

## Does this PR have any downstream implications?

> **Ideally**, no schema changes will be performed that have downstream implications.
>
> Examples of downstream changes: any change that requires a change to workflows, workflow automation, the Mongo-to-Postgres ingest process, Jupyter notebooks, the Runtime, etc.

- [ ] Yes _(Add a justification below)_
- [ ] No
