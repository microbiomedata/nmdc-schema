- add a minimal number of new elements.
- follow established patterns (chains or networks of classes, slots types and enums) or create new reusable patterns
- use tight ranges. minimize number of string slots.
- submit tiny PRs
    - use a bottom up approach, submitting leaf entities as early as possible
    - in addition to passing the tests, all YAML modules in each PR must compile independent with something
      like `gen-linkml` or `gen-owl`. This is not automated yet.
    - include example data files in each PR
    - emphasize example data files that instantiate a nmdc:Database and tell a cumulative story
    - add `xyz_set` collection slots as needed, but check whether their is a collection slot for a parent class first
    - minimize initial textual annotation of mappings to external resources like ontologies. add just enough for your
      own understanding and be prepared for descriptions, mappings etc to be revised
    - if mappings are provided, be aware that lexical matching (similar words) is not the same as semantic matching (
      similar meanings). mappings should be based on semantic matching and the source hierarchical context should align
      with the resulting hierarchy in the schema
- use multiple tools for browsing schema including source YAML files, SchemaView() code, documentation pages and
  diagrams. generated artifacts might have errors or limitations
    - diagramming tools should be added to Docker container
- be familar with [ChemROF](https://chemkg.github.io/chemrof/) for anythign chemistry related
- ask large-context LLMs like claude for advice by uploading a merged schema and an example data file
