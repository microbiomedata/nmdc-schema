# OWL Generation Experiments

This page captures a reproducible command profile for generating an OWL/Turtle
artifact tuned for OLS-oriented metadata.

## Scope

- This is an experimental generation profile for investigation and comparison.
- It is not the default release artifact pipeline.
- Use it when evaluating ontology publication options or debugging OWL output.

## Command profile

From the repository root:

```bash
poetry run linkml generate owl \
  --add-ols-annotations \
  --default-permissible-value-type "http://www.w3.org/2002/07/owl#Class" \
  --enum-iri-separator "#" \
  --format owl \
  --log_level WARNING \
  --mergeimports \
  --metadata \
  --metadata-profile ols \
  --add-root-classes \
  --no-assert-equivalent-classes \
  --metaclasses \
  --no-mixins-as-expressions \
  --no-stacktrace \
  --no-type-objects \
  --ontology-uri-suffix .owl.ttl \
  --use-native-uris \
  --useuris \
  src/schema/nmdc.yaml > local/nmdc-schema.ols.owl.ttl
```

## Notes

- Output goes to `local/` by default for experimentation.
- If this profile becomes part of the release process, move it into a dedicated Makefile target and CI validation.
- Warnings about some `equals_string` values are expected with current LinkML OWL generation behavior.
