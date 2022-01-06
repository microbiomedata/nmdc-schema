SRC_DIR = src
SCHEMA_DIR = $(SRC_DIR)/schema
SOURCE_FILES := $(shell find $(SCHEMA_DIR) -name '*.yaml')
SCHEMA_NAMES = $(patsubst $(SCHEMA_DIR)/%.yaml, %, $(SOURCE_FILES))

SCHEMA_NAME = nmdc
SCHEMA_SRC = $(SCHEMA_DIR)/$(SCHEMA_NAME).yaml
#TGTS = graphql jsonschema docs shex owl csv  python
TGTS = jsonschema jsonld-context python docs

#GEN_OPTS = --no-mergeimports
GEN_OPTS =

all: gen stage
gen: $(patsubst %,gen-%,$(TGTS))
.PHONY: all gen stage clean clean-artifacts clean-docs t echo test install docserve gh-deploy .FORCE

clean: clean-artifacts clean-docs

clean-artifacts:
	rm -rf target/

clean-docs:
	ls docs/*.md | egrep -v 'README.md|README.markdown' | xargs rm -f # keep readme files
	rm -f docs/images/*
	rm -f docs/types/*

t:
	echo $(SCHEMA_NAMES)

echo:
	echo $(patsubst %,gen-%,$(TGTS))

test: all test-jsonschema

install:
#	. environment.sh
	pipenv install -r requirements.txt

tdir-%:
	mkdir -p target/$*

docs:
	mkdir -p $@
	mkdir -p $@/images

stage: $(patsubst %,stage-%,$(TGTS))
stage-%: gen-%
	cp -pr target/$* .


###  -- MARKDOWN DOCS AND SLIDES --
# Generate documentation ready for mkdocs
# TODO: modularize imports
gen-docs: target/docs/index.md copy-src-docs make-slides
.PHONY: gen-docs
copy-src-docs:
	mkdir -p target/docs/images
	cp $(SRC_DIR)/docs/*.md target/docs/
	cp $(SRC_DIR)/docs/images/* target/docs/images/
PHONY: copy-src-docs
target/docs/%.md: $(SCHEMA_SRC) tdir-docs
	pipenv run gen-markdown $(GEN_OPTS) --dir target/docs $<
stage-docs: gen-docs
	cp -pr target/docs .

make-slides: target/docs/schema-slides.html copy-src-slides-images
.PHONY: make-slides
copy-src-slides-images:
	mkdir -p target/docs/images
	cp $(SRC_DIR)/slides/images/* target/docs/images/
.PHONY: copy-src-slides-images
target/docs/schema-slides.html: tdir-docs 
# see here for demos https://pandoc.org/demos.html
# here the pandoc manual https://pandoc.org/MANUAL.html
	pipenv run pandoc -s --webtex -i -t slidy src/slides/schema-slides.md -o $@

###  -- PYTHON --
# TODO: modularize imports
gen-python: $(patsubst %, target/python/%.py, $(SCHEMA_NAMES))
.PHONY: gen-python
target/python/%.py: $(SCHEMA_DIR)/%.yaml  tdir-python
# --no-mergeimports was causing an import error
#	gen-py-classes --no-mergeimports $(GEN_OPTS) $< > $@
	pipenv run gen-py-classes --mergeimports $(GEN_OPTS) $< > $@

###  -- GRAPHQL --
# TODO: modularize imports. For now imports are merged.
gen-graphql:target/graphql/$(SCHEMA_NAME).graphql 
.PHONY: gen-graphql
target/graphql/%.graphql: $(SCHEMA_DIR)/%.yaml tdir-graphql
	pipenv run gen-graphql $(GEN_OPTS) $< > $@

###  -- JSON SCHEMA --
# TODO: modularize imports. For now imports are merged.
gen-jsonschema: target/jsonschema/$(SCHEMA_NAME).schema.json
.PHONY: gen-jsonschema
target/jsonschema/%.schema.json: $(SCHEMA_DIR)/%.yaml tdir-jsonschema
	pipenv run gen-json-schema $(GEN_OPTS) --closed -t database $< > $@

###  -- JSONLD Context --
gen-jsonld-context: target/jsonld-context/$(SCHEMA_NAME).context.jsonld
.PHONY: gen-jsonld-context
target/jsonld-context/%.context.jsonld: $(SCHEMA_DIR)/%.yaml tdir-jsonld-context
	pipenv run gen-jsonld-context $(GEN_OPTS) $< > $@

###  -- SHEX --
# one file per module
gen-shex: $(patsubst %, target/shex/%.shex, $(SCHEMA_NAMES))
.PHONY: gen-shex
target/shex/%.shex: $(SCHEMA_DIR)/%.yaml tdir-shex
	pipenv run gen-shex --no-mergeimports $(GEN_OPTS) $< > $@

###  -- CSV --
# one file per module
gen-csv: $(patsubst %, target/csv/%.csv, $(SCHEMA_NAMES))
.PHONY: gen-csv
target/csv/%.csv: $(SCHEMA_DIR)/%.yaml tdir-csv
	pipenv run gen-csv $(GEN_OPTS) $< > $@

###  -- OWL --
# TODO: modularize imports. For now imports are merged.
gen-owl: target/owl/$(SCHEMA_NAME).owl.ttl
.PHONY: gen-owl
target/owl/%.owl.ttl: $(SCHEMA_DIR)/%.yaml tdir-owl
	pipenv run gen-owl $(GEN_OPTS) $< > $@

###  -- RDF (direct mapping) --
# TODO: modularize imports. For now imports are merged.
gen-rdf: target/rdf/$(SCHEMA_NAME).ttl
.PHONY: gen-rdf
target/rdf/%.ttl: $(SCHEMA_DIR)/%.yaml tdir-rdf
	pipenv run gen-rdf $(GEN_OPTS) $< > $@

###  -- LINKML --
# linkml (copy)
# one file per module
gen-linkml: target/linkml/$(SCHEMA_NAME).yaml
.PHONY: gen-linkml
target/linkml/%.yaml: $(SCHEMA_DIR)/%.yaml tdir-limkml
	cp $< > $@

# test docs locally.
docserve:
	pipenv run mkdocs serve

gh-deploy:
# deploy documentation (note: requires documentation is in docs dir)
	pipenv run mkdocs gh-deploy --remote-branch gh-pages --force --theme readthedocs

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
	cp util/nmdc_data.py nmdc_schema/ # copy command-line data retrieval tool
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
	functional_annotation_set \
	study_credit_test

SCHEMA_TEST_EXAMPLES_INVALID := \
	biosample_invalid_range \
	biosample_mismatch_regex \
	biosample_missing_required_field \
	biosample_single_multi_value_mixup \
	biosample_undeclared_slot \
	study_credit_enum_mangle

# 	functional_annotation_set_invalid has invalid ID pattern but regex tests aren't applied yet? MAM 2021-06-24

.PHONY: test-jsonschema
test-jsonschema: $(foreach example, $(SCHEMA_TEST_EXAMPLES), validate-$(example))

# .PHONY: test-jsonschema
# test-jsonschema: $(foreach example, $(SCHEMA_TEST_EXAMPLES), echo $(example))

.PHONY: test-jsonschema_invalid
test-jsonschema_invalid: $(foreach example, $(SCHEMA_TEST_EXAMPLES_INVALID), validate-invalid-$(example))

validate-%: test/data/%.json jsonschema/nmdc.schema.json
# util/validate_nmdc_json.py -i $< # example of validating data using the cli
	pipenv run jsonschema -i $< $(word 2, $^)

validate-invalid-%: test/data/invalid_schemas/%.json jsonschema/nmdc.schema.json
	! pipenv run jsonschema -i $< $(word 2, $^)