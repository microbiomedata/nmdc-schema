RUN=poetry run

PHONY: validate
SCHEMA_YAML = well_plate_schema.yaml
SCHEMA_JSON = $(subst .yaml,.schema.json,$(SCHEMA_YAML))


validate: \
well_plate_schema.yaml \
well_plate_valid_plate.yaml \
well_plate_invalid_plate.yaml \
well_plate_valid_tube.yaml \
well_plate_invalid_tube.yaml

	$(RUN) linkml-validate \
		--target-class Database \
		--schema $< $(word 2,$^)

	$(RUN) gen-json-schema \
		--top-class Database \
		--closed $< > $(SCHEMA_JSON)

	$(RUN) check-jsonschema --schemafile $(SCHEMA_JSON) $(word 2,$^)

	! $(RUN) check-jsonschema --schemafile $(SCHEMA_JSON) $(word 3,$^)

	$(RUN) check-jsonschema --schemafile $(SCHEMA_JSON) $(word 4,$^)


#	! $(RUN) check-jsonschema --schemafile $(SCHEMA_JSON) $(word 5,$^)