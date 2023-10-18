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
- See also src/docs/prefixes_curies_ids_mappings_etc.md

## To Do

- We need more documentation about browsing, searching and editing the schema via the GitHub web interface and/or
  IDEs like PyCharm or VisualStudio code.