RUN=poetry run
TIMED_RUN=time $(RUN)

JENA_APPS_DIR=/usr/local/bin

NMDC_DATA_FILE=neon_jgi_soil_metadata_2023-08-15-04-36_retyped.json # library preparation instances had ...procsm... ids

SCHEMA_FILE=../nmdc_schema/nmdc_materialized_patterns.yaml
SCHEMA_CLASS=Database

SPARQL_QUERY_FILE=extraction-input-type-counts.rq

.PHONY: sparql-all rdf-clean

sparql-all: sparql-clean validation.log sparql-results.tsv

sparql-clean:
	rm -rf validation.log nmdc-data.ttl sparql-results.tsv

validation.log: $(SCHEMA_FILE) $(NMDC_DATA_FILE) # ~ 20 sec for neon_jgi_soil_metadata_2023-08-15-04-36_retyped.json
	$(TIMED_RUN) linkml-validate \
		--target-class $(SCHEMA_CLASS) \
		--schema $^ | tee $@

nmdc-data.ttl: $(SCHEMA_FILE) $(NMDC_DATA_FILE)
	$(TIMED_RUN) linkml-convert \
		--output $@ \
		--target-class $(SCHEMA_CLASS) \
		--schema $^
	$(JENA_APPS_DIR)/riot --validate $@

sparql-results.tsv: nmdc-data.ttl $(SPARQL_QUERY_FILE)
	arq --data $(word 1,$^) --query $(word 2,$^) --results=TSV > $@

# ----

nmdc-schema-prefix-map.json: $(SCHEMA_FILE)
	$(TIMED_RUN) gen-prefix-map \
		--output $@ \
		--format json $<

neon_jgi_soil_metadata_2023-08-15-04-36_retyped.yaml: neon_jgi_soil_metadata_2023-08-15-04-36_retyped.json # non-linkml conversion if necessary
	yq -p json -o yaml -P $< > $@