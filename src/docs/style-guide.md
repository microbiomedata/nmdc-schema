- add a minimal number of new [elements](https://linkml.io/linkml-model/latest/docs/Definition/).
    - all new elements should be use-case justified (informing workflows, searching via the data portal, etc.)
    - development of [process](https://microbiomedata.github.io/berkeley-schema-fy24/PlannedProcess/) classes should
      emphasize clarity in the inputs and outputs
- follow established patterns (chains or networks of classes, slots types and enums) or create new reusable patterns
- use tight ranges. minimize number of string slots.
- submit tiny PRs
    - use a bottom up approach, submitting leaf entities as early as possible
    - include example data files in each PR
    - run `linkml-validate` on individual example data files as they are developed. don't wait for
      the `linkml-run-examples` phase at the end of `make test`
    - in addition to passing the tests, all YAML modules in each PR must compile independent with something
      like `gen-linkml` or `gen-owl`. This is not automated yet.
    - emphasize example data files that instantiate a `nmdc:Database` and tell a cumulative story
    - add `xyz_set` collection slots as needed, but check whether there is a collection slot for a parent class first
    - minimize initial textual annotation of mappings to external resources like ontologies. add just enough for your
      own understanding and be prepared for descriptions, mappings etc. to be revised
    - any textual annotations provided must agree 100% with the structural/logical modelling
    - if mappings are provided, be aware that lexical matching (similar words) is not as important as semantic
      matching (similar meanings). the resulting hierarchy in the schema should align with the source hierarchical
      context
- use multiple tools for browsing schema including source YAML files, SchemaView() code, documentation pages and
  diagrams. generated artifacts might have errors or limitations
    - diagramming tools should be added to Docker container
- be familiar with [ChemROF](https://chemkg.github.io/chemrof/) for anything chemistry related
- ask large-context LLMs like claude for advice by uploading a merged schema and an example data file
