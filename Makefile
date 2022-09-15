SRC_DIR = src
SCHEMA_DIR = $(SRC_DIR)/schema
SOURCE_FILES := $(shell find $(SCHEMA_DIR) -name '*.yaml')
DOCS_DIR = docs
#GEN_OPTS = --no-mergeimports
GEN_OPTS =
RUN=poetry run
SCHEMA_NAME = nmdc
SCHEMA_NAMES = $(patsubst $(SCHEMA_DIR)/%.yaml, %, $(SOURCE_FILES))
SCHEMA_SRC = $(SCHEMA_DIR)/$(SCHEMA_NAME).yaml
#TGTS = graphql jsonschema docs shex owl csv  python docs
TGTS = jsonschema jsonld-context python json doc

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

.PHONY: test
test: all test-data

.PHONY: test-data
test-data: test-jsonschema test-jsonschema_invalid

install:
	poetry install

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
#gen-docs: target/docs/index.md copy-src-docs make-slides
.PHONY: gen-docs
copy-src-docs:
	mkdir -p target/docs/images
	cp $(SRC_DIR)/docs/*.md target/docs/
	cp $(SRC_DIR)/docs/images/* target/docs/images/
PHONY: copy-src-docs

target/docs/%.md: $(SCHEMA_SRC) tdir-docs
	$(RUN) gen-markdown $(GEN_OPTS) --dir target/docs $<

#stage-docs: gen-docs
#	cp -pr target/docs .

gen-doc:
	mkdir -p target/doc
	echo 'long story' > target/doc/placeholder.txt
	$(RUN) gen-doc $(SCHEMA_SRC) --template-directory $(SRC_DIR)/doc-templates -d $(DOCS_DIR)
	cp $(SRC_DIR)/$(DOCS_DIR)/*.md $(DOCS_DIR)
	mkdir -p $(DOCS_DIR)/images
	cp $(SRC_DIR)/$(DOCS_DIR)/images/* $(DOCS_DIR)/images

make-slides: target/docs/schema-slides.html copy-src-slides-images
.PHONY: make-slides
copy-src-slides-images:
	mkdir -p target/docs/images
	cp $(SRC_DIR)/slides/images/* target/docs/images/
.PHONY: copy-src-slides-images
target/docs/schema-slides.html: tdir-docs 
# see here for demos https://pandoc.org/demos.html
# here the pandoc manual https://pandoc.org/MANUAL.html
	$(RUN) pandoc -s --webtex -i -t slidy src/slides/schema-slides.md -o $@

###  -- PYTHON --
# TODO: modularize imports
gen-python: $(patsubst %, target/python/%.py, $(SCHEMA_NAMES))
.PHONY: gen-python

# --no-mergeimports was causing an import error
#	gen-py-classes --no-mergeimports $(GEN_OPTS) $< > $@
	# hardcoded solution for the new src/schema/portal directory in target/python/%.py

target/python/portal:
	mkdir -p $@

# 	mkdir -p target/python/portal

target/python/%.py: $(SCHEMA_DIR)/%.yaml  tdir-python target/python/portal
	$(RUN) gen-py-classes --mergeimports $(GEN_OPTS) $< > $@

###  -- GRAPHQL --
# TODO: modularize imports. For now imports are merged.
gen-graphql:target/graphql/$(SCHEMA_NAME).graphql 
.PHONY: gen-graphql
target/graphql/%.graphql: $(SCHEMA_DIR)/%.yaml tdir-graphql
	$(RUN) gen-graphql $(GEN_OPTS) $< > $@

###  -- JSON SCHEMA --
# TODO: modularize imports. For now imports are merged.
gen-jsonschema: target/jsonschema/$(SCHEMA_NAME).schema.json
.PHONY: gen-jsonschema
target/jsonschema/%.schema.json: $(SCHEMA_DIR)/%.yaml tdir-jsonschema
	$(RUN) gen-json-schema $(GEN_OPTS) --closed -t database $< > $@

###  -- JSONLD Context --
gen-jsonld-context: target/jsonld-context/$(SCHEMA_NAME).context.jsonld
.PHONY: gen-jsonld-context
target/jsonld-context/%.context.jsonld: $(SCHEMA_DIR)/%.yaml tdir-jsonld-context
	$(RUN) gen-jsonld-context $(GEN_OPTS) $< > $@

###  -- SHEX --
# one file per module
gen-shex: $(patsubst %, target/shex/%.shex, $(SCHEMA_NAMES))
.PHONY: gen-shex
target/shex/%.shex: $(SCHEMA_DIR)/%.yaml tdir-shex
	$(RUN) gen-shex --no-mergeimports $(GEN_OPTS) $< > $@

###  -- CSV --
# one file per module
gen-csv: $(patsubst %, target/csv/%.csv, $(SCHEMA_NAMES))
.PHONY: gen-csv
target/csv/%.csv: $(SCHEMA_DIR)/%.yaml tdir-csv
	$(RUN) gen-csv $(GEN_OPTS) $< > $@

###  -- OWL --
# TODO: modularize imports. For now imports are merged.
gen-owl: target/owl/$(SCHEMA_NAME).owl.ttl
.PHONY: gen-owl
target/owl/%.owl.ttl: $(SCHEMA_DIR)/%.yaml tdir-owl
	$(RUN) gen-owl $(GEN_OPTS) $< > $@

###  -- RDF (direct mapping) --
# TODO: modularize imports. For now imports are merged.
gen-rdf: target/rdf/$(SCHEMA_NAME).ttl
.PHONY: gen-rdf
target/rdf/%.ttl: $(SCHEMA_DIR)/%.yaml tdir-rdf
	$(RUN) gen-rdf $(GEN_OPTS) $< > $@

###  -- JSON --
gen-json: target/json/$(SCHEMA_NAME).linkml.json
.PHONY: gen-json
target/json/%.linkml.json: $(SCHEMA_DIR)/%.yaml tdir-json
	$(RUN) gen-linkml $(GEN_OPTS) --format json --materialize-attributes $< > $@

# test docs locally.
docserve:
	$(RUN) mkdocs serve

gh-deploy:
# deploy documentation (note: requires documentation is in docs dir)
	$(RUN) mkdocs gh-deploy --force

###  -- PYPI TARGETS
# Use the build-package target to build a PYPI package locally
# This is useful for testing
.PHONY: clean-package build-nmdc_schema build-package deploy-pypi
clean-package:
	rm -rf dist && echo 'dist removed'
	rm -rf nmdc_schema.egg-info && echo 'egg-info removed'
	rm -f nmdc_schema/*.py
	touch nmdc_schema/__init__.py
	rm -f nmdc_schema/*.json
	rm -f nmdc_schema/*.tsv

build-nmdc_schema: clean-package
	cp src/schema/nmdc.yaml nmdc_schema/ # copy nmdc yaml file
	cp python/*.py nmdc_schema/ # copy python files
	cp jsonschema/nmdc.schema.json nmdc_schema/ # copy nmdc json schema

build-package: build-nmdc_schema
	poetry build

deploy-pypi:
# deploys package to pypi
# note: you need to be a registered PyPI user
# on the nmdc-schema PyPI repo
	poetry publish

deploy-testpypi:
# deploys package to testpypi
# note: you need to be a registered Test PyPI user
# on the nmdc-schema Test PyPI repo
	poetry config repositories.testpypi https://test.pypi.org/legacy/
	poetry publish -r testpypi

delete-poetry-env:
# delete the activated virtualenv created by poetry
	poetry env remove $(basename $(poetry env info --path))

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
	study_credit_test \
	samp_prep_db

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

.PHONY: test-jsonschema_invalid
test-jsonschema_invalid: $(foreach example, $(SCHEMA_TEST_EXAMPLES_INVALID), validate-invalid-$(example))

validate-%: test/data/%.json jsonschema/nmdc.schema.json
# util/validate_nmdc_json.py -i $< # example of validating data using the cli
	$(RUN) jsonschema -i $< $(word 2, $^)

validate-invalid-%: test/data/invalid_schemas/%.json jsonschema/nmdc.schema.json
	! $(RUN) jsonschema -i $< $(word 2, $^)

# ---

reports/slot_roster.tsv:
	poetry run python util/slot_roster.py \
		--input_paths "mixs/model/schema/mixs.yaml" \
		--input_paths "src/schema/nmdc.yaml" \
		--input_paths "https://raw.githubusercontent.com/microbiomedata/sheets_and_friends/issue-100-netlify-linkml-datastructure/artifacts/nmdc_dh.yaml" \
		--output_tsv $@

src/schema/mixs_new.yaml: reports/slot_roster.tsv
	poetry run python util/rebuild_mixs_yaml.py \
		--use_legacy "is_a" \
		--use_legacy "multivalued" \
		--use_legacy "range" \
		--output_yaml $@ \
		--legacy_see_also "https://github.com/microbiomedata/nmdc-schema/blob/issue-291-mixs-submod/util/rebuild_mixs_yaml.py" \
		--slot_roster_tsv_in $< \
		--legacy_mixs_module_in src/schema/mixs_legacy.yaml\
		--current_mixs_root_in mixs/model/schema/mixs.yaml \
		--current_nmdc_root_in src/schema/nmdc.yaml
	cp $@ src/schema/mixs.yaml

reports/slot_annotations_diffs.tsv: src/schema/mixs_new.yaml
	poetry run python util/mixs_deep_diff.py \
		--include_descriptions True \
		--shingle_size 2 \
		--slot_diff_yaml_out reports/slot_diffs.yaml \
		--anno_diff_tsv_out $@ \
		--legacy_mixs_module_in src/schema/mixs_legacy.yaml \
		--current_mixs_module_in $<

.PHONY: post_test mixs_clean

post_test: clean mixs_clean reports/slot_annotations_diffs.tsv all
	cp python/nmdc.py nmdc_schema/nmdc.py
	poetry run python biosamples_from_NMDC_api.py
	# todo add check over omics processings too?

reference_commit=dbbf2f85b676daa35af78992c2649a68457cae21
# main
# release 3_2_0 = dbbf2f85b676daa35af78992c2649a68457cae21

mixs_clean:
	rm -rf reports/slot_annotations_diffs.tsv
	rm -rf reports/slot_diffs.yaml
	rm -rf reports/slot_roster.tsv
	rm -rf src/schema/mixs*yaml
	# ensure that we are comparing against the current main
	#   not some local junk
	#   OR could compare against some other branch, commit, etc.
	curl -o src/schema/mixs.yaml https://raw.githubusercontent.com/microbiomedata/nmdc-schema/$(reference_commit)/src/schema/mixs.yaml
	curl -o src/schema/nmdc.yaml https://raw.githubusercontent.com/microbiomedata/nmdc-schema/$(reference_commit)/src/schema/nmdc.yaml
	curl -o nmdc_schema/nmdc.py https://raw.githubusercontent.com/microbiomedata/nmdc-schema/$(reference_commit)/nmdc_schema/nmdc.py
	cp src/schema/mixs.yaml src/schema/mixs_legacy.yaml

src/schema/portal/emsl.yaml:
	$(RUN) python util/integrate_dh_non_mixs_classes.py

assets/3_2_0/nmdc.schema.json:
	curl --output  $@  "https://raw.githubusercontent.com/microbiomedata/nmdc-schema/v3.2.0/jsonschema/nmdc.schema.json"

assets/4_0_0/nmdc.schema.json:
	curl --output  $@  "https://raw.githubusercontent.com/microbiomedata/nmdc-schema/v4.0.0/jsonschema/nmdc.schema.json"

assets/schema_json_diff.txt:assets/3_2_0/nmdc.schema.json assets/4_0_0/nmdc.schema.json
	- jd -o $@ --set $^
