## NMDC community principles for contributing to the schema

### Meeting style

- Meetings should follow an agenda with small, clear, post-meeting deliverables in mind.
- All meeting attendees should be treated with respect. We especially want to hear diverse input.
- Therefore, the meeting agenda should include ample time for active check-ins from all attendees.
- All attendees have a voice in the functionality that the schema needs to support, but those with greater
  experience with object-oriented or semantic data modeling will take the lead regarding how the schema
  implements data storage.
- All team members are encouraged to amplify their voices by increasing their LinkML skills.
  That could include attending the
  [LinkML Developer's Meeting](https://docs.google.com/document/d/1OOgBRPYVwcD0hbKc79EOKP750vVCLEKAtbztSMQdC7A/edit#heading=h.6sqkx1xhumse),
  [The LinkML Community Meeting](https://docs.google.com/document/d/1MStpDyh9LOZYJTjLtnpOsNYc3HaeU-bz0CHAI9xOjfQ/edit#heading=h.6sqkx1xhumse)
  reading the [LInkML Documenation](https://linkml.io/linkml/),
  or working though [LinkML tutorials](https://linkml.io/linkml/intro/tutorial.html).
- Attendees can contribute in any way, but greater weight will be put on diagrams, and even greater weight on
  examples checked into the nmdc-schema repo, even if they are not fully functional

### Default modeling style

- All of our modeling and example data should be as clear as possible. Textual annotation on classes,
  slots and enumerations should be written with minimal jargon, clear grammar and no misspellings
- If it is necessary to retain external content **as-is**, like `description`s, they should be attributed using
  the appropriate LinkML meta-slots, and we should also strive to provide clarification in appropriate meta-slots
- The structural definitions of elements should agree with the textual description (and vice versa)
- Parsimony: The schema should contain a minimal number of slots, classes, etc. Elements that have a general suffix, like "speed"
  and a very specific prefix like "lc_pumping_" are suggestive of suboptimal modeling.
- People adding new modeling bear the responsibility of re-using existing elements or demonstrating to the team how
  their proposed alternative modeling is in general superior
- Modeling that informs downstream analyses or supports searching (DataPortal or through an API) will be prioritized.
  Requests for modeling that might be useful in the future should be left as separate issues, possibly with code branches.
  is an anti-pattern.
- LinkML provides micro-crediting metaslots. They should be used to micro-=credit contributors
  - https://linkml.io/linkml-model/latest/docs/contributors/
  - https://linkml.io/linkml-model/latest/docs/created_by/
  - https://linkml.io/linkml-model/latest/docs/created_on/
  - https://linkml.io/linkml-model/latest/docs/modified_by/
  - https://linkml.io/linkml-model/latest/docs/last_updated_on/
- See also `src/docs/prefixes_curies_ids_mappings_etc.md`

## To Do

- We need more documentation about browsing, searching and editing the schema via the GitHub web interface and/or
  IDEs like PyCharm or VisualStudio code.
