## Add your own custom Makefile targets here
RUN=poetry run

SCHEMA_NAME = $(shell bash ./utils/get-value.sh name)
SOURCE_SCHEMA_PATH = $(shell bash ./utils/get-value.sh source_schema_path)

#examples-all: examples-clean src/data/output
#
#examples-clean:
#	rm -rf src/data/output project/nmdc_schema_generated.yaml
#
#project/nmdc_schema_generated.yaml: $(SOURCE_SCHEMA_PATH)
#	# the need for this may be eliminated by adding mandatory pattern materialization to gen-json-schema
#	$(RUN) gen-linkml \
#		--output $@ \
#		--materialize-patterns \
#		--no-materialize-attributes \
#		--format yaml $<
#
#src/data/output: project/nmdc_schema_generated.yaml
#	mkdir -p $@
#	$(RUN) linkml-run-examples \
#		--schema $< \
#		--input-directory src/data/valid \
#		--counter-example-input-directory src/data/invalid \
#		--output-directory $@ > $@/README.md
#

assets/MIxS_6_term_updates_MIxS6_Core-_Final_clean.tsv:
	curl -L "https://docs.google.com/spreadsheets/d/1QDeeUcDqXes69Y2RjU2aWgOpCVWo5OVsBX9MKmMqi_o/export?gid=178015749&format=tsv" > $@

assets/MIxS_6_term_updates_MIxS6_packages_-_Final_clean.tsv:
	curl -L "https://docs.google.com/spreadsheets/d/1QDeeUcDqXes69Y2RjU2aWgOpCVWo5OVsBX9MKmMqi_o/export?gid=750683809&format=tsv" > $@

