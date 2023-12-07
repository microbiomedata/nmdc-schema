# Contributing to NMDC-schema

:+1: First of all: Thank you for taking the time to contribute!

The following is a set of guidelines for contributing to nmdc-schema. This guide
is aimed primarily at the core NMDC schema developers, although anyone is welcome
to contribute.

## Table Of Contents

- [Code of Conduct](#code-of-conduct)
- [Guidelines for Contributions and Requests](#contributions)
    * [Reporting issues](#reporting-issues)
    * [Making pull requests](#pull-requests)
- [Best practices](#best-practices)

<a id="code-of-conduct"></a>

## Code of Conduct

The nmdc-schema team strives to create a
welcoming environment for editors, users and other contributors.

Please carefully read our [Code of Conduct](CODE_OF_CONDUCT.md).

<a id="contributions"></a>

## Guidelines for Contributions and Requests

<a id="reporting-issues"></a>

### Reporting issues with the schema

Please use the [Issue Tracker](https://github.com/microbiomedata/nmdc-schema/issues/) for reporting problems with the schema. 

Please review GitHub's overview article,
["Tracking Your Work with Issues"][[about-issues]].

### Pull Requests

See [Pull Requests](https://github.com/microbiomedata/nmdc-schema/pulls/) for all pull requests.

Please review GitHub's article, ["About Pull Requests"][about-pulls],
and make your changes on a [new branch][about-branches].

We recommend also reading [GitHub Pull Requests: 10 Tips to Know](https://blog.mergify.com/github-pull-requests-10-tips-to-know/)

## Best Practices

While anyone is welcome to make issues or pull requests in this repository, it is expected that the core schema team become
familiar with the schema, the basics of the LinkML framework, and NMDC Best Practices.

### GitHub Best Practice

(Note: these best practices apply to most development in NMDC; these guidelines may later be moved somewhere central)

- Read ["About Issues"][[about-issues]] and ["About Pull Requests"][[about-pulls]]
- Issues should be focused and actionable
- Complex issues should be broken down into simpler issues where possible
- Pull Requests (PRs) should be atomic and aim to close a single issue
- Long running PRs should be avoided where possible
- PRs should reference issues following standard conventions (e.g. “fixes #123”)
- Schema developers should always be working on a single issue at any one time
- Never work on the main branch, always work on an issue/feature branch
- Core developers can work on branches off origin rather than forks
- Always create a PR on a branch to maximize transparency of what you are doing
- When a PR includes a breaking change, include a migration
- PRs should be reviewed and merged in a timely fashion by the nmdc-schema technical leads
- PRs that do not pass GitHub actions should never be merged
- In the case of git conflicts, the contributor should try and resolve the conflict
- If a PR fails a GitHub action check, the contributor should try and resolve the issue in a timely fashion

### Understanding LinkML

Core developers should read the material on the [LinkML site](https://linkml.io/linkml), in particular:

- [Overview](https://linkml.io/linkml/intro/overview.html)
- [Tutorial](https://linkml.io/linkml/intro/tutorial.html)
- [Schemas](https://linkml.io/linkml/schemas/index.html)
- [FAQ](https://linkml.io/linkml/faq/index.html)

### Modeling Best Practice

- Follow Naming conventions
    - Standard LinkML naming conventions should be followed (UpperCamelCase for classes and enums, snake_case for slots)
    - Know how to use the LinkML linter to check style and conventions
    - The names for classes should be nouns or noun-phrases: Person, SequenceAlignment, Annotation, SequenceTrimming
    - Spell out abbreviations and short forms, except where this goes against convention (e.g. do not spell out DNA)
    - Elements that are imported from outside (e.g. MIxS) need not follow the same naming conventions
    - Multivalued slots should be named as plurals
    - Older elements may be "grandfathered in" - modifying them to match naming conventions may be too expensive
- Document model elements
    - All model elements should have documentation (descriptions) and other textual annotations (e.g. comments, notes)
    - Textual annotations on classes, slots and enumerations should be written with minimal jargon, clear grammar and no misspellings
- Include examples and counter-examples (intentionally invalid examples)
    - Rationale: these serve as documentation and unit tests
    - All elements of the nmdc-schema must be illustrated with valid and invalid data examples in src/data. New schema elements will not be merged into the main branch until examples are provided
    - Invalid example data files should be invalid for one single reason, which should be reflected in the filename. It should be possible to render the invalid example files valid by addressing that single fault.
- Use enums for categorical values
    - Rationale: Open-ended string ranges encourage multiple values to represent the same entity, like “water”, “H2O” and “HOH”
    - Any slot whose values could be constrained to a finite set should use an Enum
    - Non-categorical values, e.g. descriptive fields like `name` or `description` fall outside of this.
- Reuse
    - Existing scheme elements should be reused where appropriate, rather than making duplicative elements
    - More specific classes can be created by refinining classes using inheritance (`is_a`)
- Place new classes under existing upper level classes
    - __Note__: this is partially aspirational until we have a stable upper level structure in place
    - Most new classes should be refinement of existing classes
    - Follow the naming conventions of the parent class
    - Descriptions of child classes may reference parent classes in a genus-differentia definition structure (e.g. "A workflow execution activity that...")
    - Inheritance should be monotonic: `slot_usage` should refine rather than override

### Testing Changes Locally

While all PRs will be automatically checked using GitHub actions, core developers should understand how to run tests locally, as well as
how to deploy a test version of the schema documentation. This requires some basic Python installation (e.g poetry)

 - Contributors should be comfortable running makefile targets, like `squeaky-clean`, `all`, `test`
 - Anyone who is involved in writing migrations or otherwise checking data from MongoDB against the schema should be comfortable running make `make-rdf`.
 - The main [Makefile](Makefile) should in general not be edited. Instead, edits should be made to [project.Makefile](project.Makefile) (advanced contributors only)

### Making Releases

TODO: Add to this section later

[about-branches]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches
[about-issues]: https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues
[about-pulls]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests


