## NMDC community principles for contributing to the schema

### Meeting style

- Meetings should follow an agenda with small, clear, post-meeting deliverables in mind.
- All meeting attendees should be treated with respect. We especially want to hear diverse input.
- Therefore, the meeting agenda should include ample time for active checkins from all attendees.
- All attendees have a voice in the functionality that the schema needs to support, but those with greater
  experience with object-oriented or semantic data modelling will take the lead regarding how the schema
  implements data storage.
- All team members are encouraged to learn about LinkML data modeling, by attending LinkML meetings, posting in LinkML
  Slack channels, self study though LinkML tutorials, or reaching out to their favorite person who does daily LinkML
  modeling
- Attendees can contribute in any way, but greater weight will be put on diagrams, and even greater weight on
  examples checked into the nmdc-schema repo, even if they are not fully functional

### GitHub policies
- Anyone with an idea for improving the schema can [start a new GitHub issue]([url](https://github.com/microbiomedata/nmdc-schema/issues))
- Issue titles should indicate either
  - an observable problem
  - a proposed solution
- GitHub issue titles and comments should use terminology from the nmdc-schema and the [LinkML metamodel]([url](https://linkml.io/linkml-model/latest/docs/)).
  Temptation to use pet names for entites in the nmdc-schema may indicate the need to add more aliases.
- A branch should be opened as soon after the creation of an issue as possible.
  Branch names are ideally brief and include the issue number and a few keywords from the issue title.
  The issue creation page has a development section on the far right, which can be used to link the issue
  to an existing branch, or to create a new branch. The auto-created branch names are based on the entire
  issue title, so it may be challenging to follow all of these guidelines perfectly.
- A pull request should be made as soon as new content is commited to the branch. It's OK to start the PR in draft mode.
- Issue creators, branch contributors and PR reviewers should work togther from the beginning to optimize
  the current and future impact of the branch on the schema.
- Issues, branches and PRs should be small and should ahve a short lifecycle so that new content can be merged on a rolling basis.
  

### Default modelling style

- All of our modeling and example data should be as clear as possible. Textual annotation on classes,
  slots and enumerations should be written with minimal jargon, clear grammar and no misspellings
- If it is necessary to retain external content **as-is**, like `description`s, they should be attributed using
  the appropriate LinkML metaslots, and we should also strive to provide clarification in appropriate metaslots
- The structural definitions of elements should agree with the textual description (and vice versa)
- The schema should contain a minimal number of slots, classes, etc. Elements that have a general suffix, like "speed"
  and a very specific prefix like "lc_pumping_" are suggestive of suboptimal modelling.
- People adding new modeling bear the responsibility of re-using existing elements or demonstrating to the team how
  their proposed alternative modeling is in general superior
- Adding modeling that that doesn't informing downstream analyses or searching in the (DataPortal or though an API)
  is an anti-pattern.
- See also `src/docs/prefixes_curies_ids_mappings_etc.md`

## To Do

- We need more documentation about browsing, searching and editing the schema via the GitHub web interface and/or
  IDEs like PyCharm or VisualStudio code.
