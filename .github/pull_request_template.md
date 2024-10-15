# Guidelines

## _Soft_ Schema Freeze

The `nmdc-schema` and `berkeley-schema-fy24` schemas are under a soft freeze, which means changes **should not** be made that have any downstream implications. To ensure this, all PRs created during the freeze will be closely reviewed with **every** component of the NMDC system in mind.

## Reviewers

To ensure no changes are made unexpectedly, PR creators will use this PR template to tag and notify all task coordinators. Review should be specifically requested from _all_ [Berkeley Schema Roll Out task coordinators](https://docs.google.com/document/d/1XXN1YuaBuSkxPXeiLKm5YxYzXTamBPQrzzeLhlh7PWs/edit#heading=h.u52g8v319adh) that you expect to be affected by this PR.

We expect task coordinators to review PRs and provide feedback/approval within 1 week of when they are identified as reviewers. 

PRs will **NOT** be merged until all task coordinators (or their delegates) have approved it; either here on GitHub (via "`Review changes` > `Approve`" or an equivalent comment) or verbally.

Expedition, questions, and discussion can happen at any meeting.

Delays in review & merging should be addressed in meetings or with NMDC leadership.

| If you expect the changes to<br>impact this component... | ...[request a review](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/requesting-a-pull-request-review)<br>from this person |
| -- | -- |
| Metadata<br>Schema | @mslarae13 |
| Runtime<br>Mongo database<br>Database migrations | @eecavanna,<br>who will pull in<br>@shreddd as needed |
| Postgres<br>Ingest | @naglepuff |
| Data Portal | @aclum |
| Workflows: MG & MT | @mbthornton-lbl |
| Workflows: MetaB & NOM | @corilo |
| Workflows: LipidO | @kheal |
| Workflows: MetaP | @SamuelPurvine |
| ETL code | @sujaypatil96 |
| Jupyter notebooks | @brynnz22 |

# PR Information

## What type of PR is this? (check all applicable)

- [ ] Refactor
- [ ] Feature
- [ ] Bug Fix
- [ ] Optimization
- [ ] Documentation
- [ ] Schema change: Structure and content
  - created, updated, or deleted a `class`, `slot`, or `enum`
  - changed whether a `slot` is `multivalued`
  - changed the way a `slot` is assigned to a `class`
  - changed the `permissible_values` of an `enum`
  - _etc._
- [ ] Schema change: Cleanup and preparation
  - updated the description of a `class`, `slot`, or `enum`
  - updated the `mappings` of a `class`, `slot`, or `enum` to an ontology
  - added an `enum` for _future_ use (it is not in the `range` of any `slot`)
  - _etc._
     
## Description

> _PRs should be [small and concise](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/best-practices-for-pull-requests#write-small-prs)._
>
> Aim to create small, focused pull requests that fulfill a single purpose. Smaller pull requests are easier and faster to review and merge, leave less room to introduce bugs, and provide a clearer history of changes.

- Replace this text with a description of what this PR branch contains. Please keep in mind that all reviewers will be reading this description. Example: "In this branch, I..."

## Related Issues

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
> Example: If, in this PR branch, you renamed a `slot` from `foo` to `foo_bar`, the answer to this question would be "yes," **even if** nothing in the NMDC database _currently_ uses the `foo` `slot`.
>
> More examples: `slot` or `class` name changes, changes to a `slot`'s `multivalued` state, changes to a `slot`'s `range` (e.g. string to integer), changes to `slot` assignments to `class`es, changes to an `enum`'s `permissible_values`

- [ ] Yes _(A migrator is required)_
- [ ] No
- [ ] I need help determining this

## If you answered "Yes", does this PR branch include that migrator?

- [ ] Yes
- [ ] No, this PR is incomplete and I need help writing the migrator

## Does this PR have any downstream implications?

> Examples: any change here that requires a change to workflows, workflow automation, the Mongo-to-Postgres ingest process, Jupyter notebooks, the Runtime, etc.

- [ ] Yes _(Explain below)_
- [ ] No
