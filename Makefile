SRC_DIR = src
SCHEMA_DIR = $(SRC_DIR)/schema
SOURCE_FILES := $(shell find $(SCHEMA_DIR) -name '*.yaml')
SCHEMA_NAMES = $(patsubst $(SCHEMA_DIR)/%.yaml, %, $(SOURCE_FILES))

SCHEMA_NAME = nmdc
SCHEMA_SRC = $(SCHEMA_DIR)/$(SCHEMA_NAME).yaml
TGTS = graphql jsonschema docs shex owl csv graphql python

#GEN_OPTS = --no-mergeimports
GEN_OPTS = 

all: gen stage
gen: $(patsubst %,gen-%,$(TGTS))
clean:
	rm -rf target/
	rm -f docs/*.md

t:
	echo $(SCHEMA_NAMES)

echo:
	echo $(patsubst %,gen-%,$(TGTS))

test: all test-jsonschema

install:
	. environment.sh
	pip install -r requirements.txt

tdir-%:
	mkdir -p target/$*
docs:
	mkdir $@

stage: $(patsubst %,stage-%,$(TGTS))
stage-%: gen-%
	cp -pr target/$* .


###  -- MARKDOWN DOCS --
# Generate documentation ready for mkdocs
# TODO: modularize imports
gen-docs: target/docs/index.md copy-src-docs
.PHONY: gen-docs
copy-src-docs:
	cp $(SRC_DIR)/docs/*md target/docs/
target/docs/%.md: $(SCHEMA_SRC) tdir-docs
	gen-markdown $(GEN_OPTS) --dir target/docs $<
stage-docs: gen-docs
	cp -pr target/docs .

###  -- MARKDOWN DOCS --
# TODO: modularize imports
gen-python: $(patsubst %, target/python/%.py, $(SCHEMA_NAMES))
.PHONY: gen-python
target/python/%.py: $(SCHEMA_DIR)/%.yaml  tdir-python
# --no-mergeimports was causing an import error
#	gen-py-classes --no-mergeimports $(GEN_OPTS) $< > $@
	gen-py-classes --mergeimports $(GEN_OPTS) $< > $@

###  -- MARKDOWN DOCS --
# TODO: modularize imports. For now imports are merged.
gen-graphql:target/graphql/$(SCHEMA_NAME).graphql 
target/graphql/%.graphql: $(SCHEMA_DIR)/%.yaml tdir-graphql
	gen-graphql $(GEN_OPTS) $< > $@

###  -- JSON schema --
# TODO: modularize imports. For now imports are merged.
gen-jsonschema: target/jsonschema/$(SCHEMA_NAME).schema.json
target/jsonschema/%.schema.json: $(SCHEMA_DIR)/%.yaml tdir-jsonschema
	gen-json-schema $(GEN_OPTS) -t database $< > $@

# This is temporary fix to apply additionalProperties: false gloabally
# see: https://github.com/linkml/linkml/issues/106
	jq '. += {"additionalProperties": false}' $@ > $@.tmp && mv $@.tmp $@

###  -- Shex --
# one file per module
gen-shex: $(patsubst %, target/shex/%.shex, $(SCHEMA_NAMES))
target/shex/%.shex: $(SCHEMA_DIR)/%.yaml tdir-shex
	gen-shex --no-mergeimports $(GEN_OPTS) $< > $@

###  -- CSV --
# one file per module
gen-csv: $(patsubst %, target/csv/%.csv, $(SCHEMA_NAMES))
target/csv/%.csv: $(SCHEMA_DIR)/%.yaml tdir-csv
	gen-csv $(GEN_OPTS) $< > $@

###  -- OWL --
# TODO: modularize imports. For now imports are merged.
gen-owl: target/owl/$(SCHEMA_NAME).owl.ttl
.PHONY: gen-owl
target/owl/%.owl.ttl: $(SCHEMA_DIR)/%.yaml tdir-owl
	gen-owl $(GEN_OPTS) $< > $@

###  -- RDF (direct mapping) --
# TODO: modularize imports. For now imports are merged.
gen-rdf: target/rdf/$(SCHEMA_NAME).ttl
target/rdf/%.ttl: $(SCHEMA_DIR)/%.yaml tdir-rdf
	gen-rdf $(GEN_OPTS) $< > $@

###  -- LinkML --
# linkml (copy)
# one file per module
gen-linkml: target/linkml/$(SCHEMA_NAME).yaml
target/linkml/%.yaml: $(SCHEMA_DIR)/%.yaml tdir-limkml
	cp $< > $@

# test docs locally.
docserve:
	mkdocs serve

gh-deploy:
# deploy documentation (note: requires documentation is in docs dir)
	mkdocs gh-deploy --remote-branch gh-pages --force --theme readthedocs

###  -- PYPI TARGETS
# Use the build-package target to build a PYPI package locally
# This is usefule for testing
.PHONY: clean-package build-package deploy-pypi
clean-package:
	rm -rf dist && echo 'dist removed'
	rm -rf nmdc_schema.egg-info && echo 'egg-info removed'
	rm -f nmdc_schema/*.py
	rm -f nmdc_schema/*.json
	rm -f nmdc_schema/*.tsv

build-package: clean-package
	cp src/schema/nmdc.yaml nmdc_schema/ # copy nmdc yaml file
	cp python/*.py nmdc_schema/ # copy python files
	cp jsonschema/nmdc.schema.json nmdc_schema/ # copy nmdc json schema
	cp sssom/gold-to-mixs.sssom.tsv nmdc_schema/ # copy sssom mapping
	cp util/validate_nmdc_json.py nmdc_schema/ # copy command-line validation tool
	cp util/nmdc_version.py nmdc_schema/ # copy command-line version tool
	python setup.py bdist_wheel sdist

deploy-pypi:
# deploys package to pypi
# note: you need to have a pypi account
# properly configured .pypirc file
	twine upload dist/* --verbose

deploy-testpypi:
# deploys package to testpypi
# note: you need to have a testpypi account 
# or properly configured .pypirc file
	twine upload -r testpypi dist/* --verbose

##  -- TEST/VALIDATE JSONSCHEMA

# datasets used test/validate the schema
SCHEMA_TEST_EXAMPLES := \
	biosample_test \
	gold_project_test \
	img_mg_annotation_objects \
	nmdc_example_database \
	MAGs_activity \
	mg_assembly_activities_test \
	mg_assembly_data_objects_test \
	nmdc_example_database \
	study_test \
	functional_annotation_set

SCHEMA_TEST_EXAMPLES_INVALID := \
	invalid_study_test

# 	functional_annotation_set_invalid has invalid ID pattern but regex tests aren't applied yet? MAM 2021-06-24

.PHONY: test-jsonschema
test-jsonschema: $(foreach example, $(SCHEMA_TEST_EXAMPLES), validate-$(example))

# .PHONY: test-jsonschema
# test-jsonschema: $(foreach example, $(SCHEMA_TEST_EXAMPLES), echo $(example))

.PHONY: test-jsonschema_invalid
test-jsonschema_invalid: $(foreach example, $(SCHEMA_TEST_EXAMPLES_INVALID), validate-invalid-$(example))

validate-%: test/data/%.json jsonschema/nmdc.schema.json
# util/validate_nmdc_json.py -i $< # example of validating data using the cli
	jsonschema -i $< $(word 2, $^)

validate-invalid-%: test/data/%.json jsonschema/nmdc.schema.json
	@echo $(word 2, $^)
	! jsonschema -i $< $(word 2, $^)
