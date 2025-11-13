MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help
.DELETE_ON_ERROR:
.SUFFIXES:
.SECONDARY:

RUN = poetry run
# get values from about.yaml file
# replaced sh with bash esp for linux
SCHEMA_NAME = $(shell bash ./utils/get-value.sh name)
DOCDIR = docs
SOURCE_SCHEMA_PATH = $(shell bash ./utils/get-value.sh source_schema_path)
SOURCE_SCHEMA_DIR = $(dir $(SOURCE_SCHEMA_PATH))
SRC = src
DEST = project
PYMODEL = $(SCHEMA_NAME)
EXAMPLEDIR = examples
TEMPLATEDIR = doc-templates

.PHONY: all clean examples-clean install site site-clean site-copy squeaky-clean test test-python test-with-examples linkml-lint


# note: "help" MUST be the first target in the file,
# when the user types "make" they should get help info

help: status
	@echo ""
	@echo "This project requires that dependencies are loaded into a poetry environment with 'poetry install'"
	@echo "Most typical usage: 'make squeaky-clean all test'"
	@echo "Documentation publication is handled by a GitHub merge action"
	@echo "  but users can generate a local documentation site with 'make testdoc'"
	@echo "Please excuse the currently verbose logging mode"
	@echo "make help -- show this help"
	@echo "make linkml-lint -- run LinkML schema linting (non-failing warnings)"
	@echo ""

status: check-config
	@echo "Project: $(SCHEMA_NAME)"
	@echo "Source: $(SOURCE_SCHEMA_PATH)"

# generate products and add everything to github
setup: install gen-project gendoc git-init-add

# install any dependencies required for building
install:
	poetry install

# Update to latest LinkML version
update-linkml:
	poetry add -D linkml@latest

prefixmaps:
	@mkdir -p $(DEST)/prefixmap
	$(RUN) linkml generate prefix-map nmdc_schema/nmdc_materialized_patterns.yaml > $(DEST)/prefixmap/nmdc-prefix-map.json

pydantic:
	@mkdir -p $(DEST)/pydantic
	$(RUN) linkml generate pydantic nmdc_schema/nmdc_materialized_patterns.yaml > $(DEST)/pydantic/nmdc-pydantic.py

# Note: `all` builds the project (site, docs, etc.) but doesn't run quality checks
all: site
site: clean site-clean gen-project gendoc \
nmdc_schema/gold-to-mixs.sssom.tsv \
nmdc_schema/nmdc_materialized_patterns.schema.json \
nmdc_schema/nmdc_materialized_patterns.yaml \
nmdc_schema/nmdc_materialized_patterns.json \
migration-doctests \
prefixmaps \
pydantic

%.yaml: gen-project

# was deploy: all mkd-gh-deploy
deploy: gendoc mkd-gh-deploy

gen-project: $(PYMODEL) prefixmaps pydantic # depends on src/schema/mixs.yaml # can be nuked with mixs-yaml-clean
	$(RUN) linkml generate project \
		--exclude excel \
		--exclude graphql \
		--exclude jsonld \
		--exclude markdown \
		--exclude proto \
		--exclude shacl \
		--exclude shex \
		--exclude sqlddl \
		--include jsonldcontext \
		--include jsonschema \
		--include owl \
		--include python \
		--include rdf \
		--config-file gen-project-config.yaml \
		-d $(DEST) $(SOURCE_SCHEMA_PATH) && mv $(DEST)/*.py $(PYMODEL) && cp $(DEST)/pydantic/*.py $(PYMODEL)/nmdc-pydantic.py
		cp project/jsonschema/nmdc.schema.json  $(PYMODEL)


test: examples-clean site test-python migration-doctests examples/output gen-linkml-schema-files linkml-lint
test-no-lint: examples-clean site test-python migration-doctests examples/output gen-linkml-schema-files
tests: squeaky-clean all test  # simply for convenience to wrap convention of running these three targets to test locally.

test-python:
	$(RUN) pytest tests/
	$(RUN) python -m doctest nmdc_schema/nmdc_data.py
	$(RUN) python -m doctest nmdc_schema/id_helpers.py
	$(RUN) python -m doctest src/scripts/make_typecode_to_class_map.py

linkml-lint:
	@mkdir -p local
	$(RUN) linkml lint -f tsv $(SOURCE_SCHEMA_PATH) 2>&1 | tee local/lint.tsv || true

.PHONY: check-dependencies
check-dependencies:
	$(RUN) deptry nmdc_schema --known-first-party nmdc_schema

check-config:
	@(grep my-datamodel about.yaml > /dev/null && printf "\n**Project not configured**:\n\n - Remember to edit 'about.yaml'\n\n" || exit 0)

# Test documentation locally
serve: mkd-serve

# Python datamodel
$(PYMODEL):
	mkdir -p $@

$(DOCDIR):
	mkdir -p $@

# Compile static Markdown files, images, and JavaScript scripts, into a documentation website.
#
# Then, use `refscan graph` to generate a pair of diagrams within the website's file tree.
# One of the diagrams is a graph showing all the _inter-collection_ relationships the schema says can exist,
# and the other diagram is a graph showing all the _inter-class_ relationships the schema says can exist.
#
# Note: Using `refgraph` in this way requires the `nmdc_schema/nmdc_materialized_patterns.yaml`
#       file to already have been generated. That dependency is currently not reflected in
#       the dependency list of this `make` target.
#
gendoc: $(DOCDIR) prefixmaps
	# Copy all documentation files to the documentation directory
	cp -rf $(SRC)/docs/* $(DOCDIR)
	# Use `make_typecode_to_class_map.py` to make a Markdown page that can be used to map a typecode to a schema class.
	$(RUN) python src/scripts/make_typecode_to_class_map.py > $(DOCDIR)/typecode-to-class-map.md
	# Generate documentation using the linkml generate doc command
	$(RUN) linkml generate doc -d $(DOCDIR) --template-directory $(SRC)/$(TEMPLATEDIR) --include src/schema/deprecated.yaml $(SOURCE_SCHEMA_PATH)
	# Create directory for JavaScript files and copy them
	# Added copying of prefixmaps output
	cp -f $(DEST)/prefixmap/nmdc-prefix-map.json $(DOCDIR)
	mkdir -p $(DOCDIR)/javascripts
	$(RUN) cp $(SRC)/scripts/*.js $(DOCDIR)/javascripts/
	# Use `refscan graph` to generate diagrams within the website's file tree.
	mkdir -p $(DOCDIR)/visualizations
	$(RUN) refscan graph --schema nmdc_schema/nmdc_materialized_patterns.yaml --subject collection --graph $(DOCDIR)/visualizations/collection-graph.html
	$(RUN) refscan graph --schema nmdc_schema/nmdc_materialized_patterns.yaml --subject class      --graph $(DOCDIR)/visualizations/class-graph.html

testdoc: gendoc serve

MKDOCS = $(RUN) mkdocs
mkd-%:
	$(MKDOCS) $*

PROJECT_FOLDERS = jsonldcontext jsonschema owl python rdf
git-init-add: git-init git-add git-commit git-status
git-init:
	git init
git-add:
	git add \
		*.md \
		.github \
		.gitignore \
		CODE_OF_CONDUCT.md \
		CONTRIBUTING.md \
		LICENSE \
		MAINTAINERS.md \
		Makefile \
		README.md \
		RELEASE_NOTES_v7.7.2_to_v7.7.7.md \
		about.yaml \
		assets \
		images \
		mkdocs.yml \
		nmdc_schema \
		notebooks \
		poetry.lock \
		project/ \
		pyproject.toml \
		src/ \
		tests \
		utils
	git add $(patsubst %, project/%, $(PROJECT_FOLDERS))

git-commit:
	git commit -m 'Initial commit' -a

git-status:
	git status

clean:
	rm -rf $(DEST)
	rm -rf tmp
	rm -rf docs/*.md
	rm -rf docs/*.html

###########################################################
# Schema Release Tracking
###########################################################

REPO  := microbiomedata/nmdc-schema
FILE  := nmdc_schema/nmdc_materialized_patterns.yaml
LATEST_RELEASE_TAG_FILE := local/latest_release_tag.txt
LATEST_TAG_SCHEMA_FILE   := local/nmdc_schema_last_release.yaml

# Get the tag that belongs to the latest (non-prerelease) GitHub release
LATEST_TAG = $(shell curl -fsSL https://api.github.com/repos/$(REPO)/releases/latest | jq -r '.tag_name')
LATEST_TAG_SCHEMA_URL := https://raw.githubusercontent.com/$(REPO)/$(LATEST_TAG)/$(FILE)

.PHONY: $(LATEST_TAG_SCHEMA_FILE) examples-clean

# Rule to fetch the schema file if local/nmdc_schema_last_release.yaml does not exist OR if there is a new release
$(LATEST_TAG_SCHEMA_FILE): $(LATEST_RELEASE_TAG_FILE)
	@echo "Checking for schema updates..."
	@if [ ! -f $@ ]; then \
		echo "Schema file does not exist. Creating it..."; \
		curl -fsSL $(LATEST_TAG_SCHEMA_URL) -o $@; \
		echo "$(LATEST_TAG)" > $(LATEST_RELEASE_TAG_FILE); \
	elif [ "$$(cat $(LATEST_RELEASE_TAG_FILE))" != "$(LATEST_TAG)" ]; then \
		echo "New release detected ($(LATEST_TAG)). Downloading schema..."; \
		curl -fsSL $(LATEST_TAG_SCHEMA_URL) -o $@; \
		echo "$(LATEST_TAG)" > $(LATEST_RELEASE_TAG_FILE); \
	else \
		echo "Local copy of schema is already up to date with release $(LATEST_TAG)."; \
	fi

# Rule to store the latest release tag locally
$(LATEST_RELEASE_TAG_FILE):
	@if [ -f $(LATEST_TAG_SCHEMA_FILE) ]; then \
	echo "ERROR: Tag file is missing. Recreating release tag and removing local schema file..."; \
		rm -f $(LATEST_TAG_SCHEMA_FILE); \
	fi
	@echo "Creating release tag file..."
	@curl -fsSL $(LATEST_TAG_SCHEMA_URL) -o $(LATEST_TAG_SCHEMA_FILE)
	@echo "$(LATEST_TAG)" > $@
	@echo "Release tag file created with tag: $(LATEST_TAG)"

###########################################################
# Example Data Validation
###########################################################

examples-clean:
	rm -rf examples/output

examples/output: nmdc_schema/nmdc_materialized_patterns.yaml
	mkdir -p $@
	$(RUN) linkml examples \
		--schema $< \
		--input-directory src/data/valid \
		--counter-example-input-directory src/data/invalid \
		--output-directory $@ > $@/README.md

examples/output/Biosample-exhaustive-pretty-sorted.yaml: src/data/valid/Database-interleaved.yaml
	$(RUN) pretty-sort-yaml \
		-i $< \
		-o $@

###########################################################
# Schema Analysis and Reporting
###########################################################

local/usage_template.tsv: nmdc_schema/nmdc_materialized_patterns.yaml
	mkdir -p $(@D) # create parent directory
	$(RUN) linkml2schemasheets-template \
		--source-path $< \
		--output-path $@ \
		--debug-report-path $@.debug.txt \
		--log-file $@.log.txt \
		--report-style exhaustive

local/biosample-slot-range-type-report.tsv: src/schema/nmdc.yaml
	$(RUN) slot-range-type-reporter \
		--schema $< \
		--output $@ \
		--schema-class Biosample

local/biosamples-per-study.txt:
	$(RUN) report-biosamples-per-study \
		--api-server api \
		--max-page-size 10000 > $@

local/gold-study-ids.json:
	curl -X 'GET' \
		--output $@ \
		'https://api.microbiomedata.org/nmdcschema/study_set?max_page_size=999&projection=id%2Cgold_study_identifiers' \
		-H 'accept: application/json'

local/nmdc-no-use-native-uris.owl.ttl: src/schema/nmdc.yaml
	$(RUN) linkml generate owl --no-use-native-uris $< > $@

local/nmdc_materialized.ttl: src/schema/nmdc.yaml
	$(RUN) schema-view-relation-graph \
		--schema $< \
		--output $@

local/Database-interleaved-class-count.tsv: src/data/valid/Database-interleaved.yaml
	cat $< | grep ' type: ' | sed 's/.*type: //' | sort | uniq -c | awk '{ OFS="\t"; $$1=$$1; print $$0 }' > $@

local/class_instantiation_counts.tsv: local/usage_template.tsv local/Database-interleaved-class-count.tsv
	$(RUN) class-instantiation-counts \
		--schemasheets-input $(word 1,$^) \
		--counts-input $(word 2,$^) \
		--output $@

###########################################################
# Asset Generation
###########################################################

assets/check_examples_class_coverage.txt:
	$(RUN) check-examples-class-coverage \
		--source_directory src/data/valid \
		--schema_file src/schema/nmdc.yaml > $@

assets/schema_pattern_linting.txt:
	$(RUN) schema-pattern-linting \
 		--schema-file src/schema/nmdc.yaml > $@

assets/enum_pv_result.tsv: src/schema/nmdc.yaml assets/enum_pv_template.tsv
	$(RUN) linkml2sheets \
		--output $@ \
		--schema $< $(word 2,$^)

assets/mentions-of-ids-analysis.txt: src/schema/nmdc.yaml
	$(RUN) analyze-mentions-of-ids \
		--schema-file $< 1> $@ 2> $@.log

assets/usages-report.txt: src/schema/nmdc.yaml
	$(RUN) report-usages \
		--schema-file $< > $@

assets/element-scrutiny.tsv: nmdc_schema/nmdc_materialized_patterns.yaml
	$(RUN)  scrutinize-elements \
		--schema-file $< \
		--output-file assets/element-scrutiny.tsv

# NCBI mapping process
assets/ncbi_mappings/ncbi_attribute_mappings.tsv:
	$(RUN) nmdc-ncbi-mapping create-unmapped-ncbi-mapping-file \
		--tsv-output $@

assets/ncbi_mappings/ncbi_attribute_mappings_filled.tsv: assets/ncbi_mappings/ncbi_attribute_mappings.tsv
	$(RUN) nmdc-ncbi-mapping exact-term-matching \
		--tsv-input $< \
		--tsv-output $@
	$(RUN) nmdc-ncbi-mapping ignore-import-schema-slots $@

# EXPERIMENTAL
assets/partial-imports-graph.pdf: src/schema/nmdc.yaml
	$(RUN) python src/scripts/experimental/partial_imports_graph.py # needs networkx and plotly

###########################################################
# JSON Collection Generation
###########################################################

.PHONY: generate-json-collections

generate-json-collections: src/data/valid/Database-interleaved.yaml
	$(RUN) database-to-json-list-files \
		--yaml-input $< \
		--output-dir assets/jsons-for-mongodb

src/data/valid/Database-interleaved-new.yaml: src/schema/nmdc.yaml
	$(RUN) interleave-yaml \
		--directory-path src/data/valid \
		--output-file $@ \
		--schema-file $<

###########################################################
# Utility Targets
###########################################################

.PHONY: filtered-status

filtered-status:
	git status | grep -v 'project/' | grep -v 'nmdc_schema/.*yaml' | grep -v 'nmdc_schema/.*json' | \
		grep -v 'nmdc.py' | grep -v 'examples/output/'

# Include specialized makefiles
include makefiles/mixs.Makefile
include makefiles/data-validation.Makefile
include makefiles/migrators.Makefile

# custom
site-clean: clean
	rm -rf nmdc_schema/*.json
	rm -rf nmdc_schema/*.tsv
	rm -rf nmdc_schema/*.yaml


squeaky-clean: clean examples-clean rdf-clean shuttle-clean site-clean # does not include mixs-yaml-clean
	rm -rf $(PYMODEL)/nmdc.py
	rm -rf $(PYMODEL)/nmdc-pydantic.py
	mkdir project
	rm -rf local/biosample_slots_ranges_report.tsv

nmdc_schema/nmdc_materialized_patterns.yaml:
	$(RUN) linkml generate linkml \
		--format yaml \
		--materialize-patterns \
		--no-materialize-attributes \
		--output $@ $(SOURCE_SCHEMA_PATH)

nmdc_schema/nmdc_materialized_patterns.schema.json: nmdc_schema/nmdc_materialized_patterns.yaml
	$(RUN) linkml generate json-schema \
		--closed \
		--include-range-class-descendants \
		--top-class Database $< > $@

nmdc_schema/nmdc_materialized_patterns.json: nmdc_schema/nmdc_materialized_patterns.yaml
	yq -o json < $< > $@

# the sssom/ files should be double checked too... they're probably not all SSSSOM files
nmdc_schema/gold-to-mixs.sssom.tsv: sssom/gold-to-mixs.sssom.tsv
	# just can't seem to tell pyproject.toml to bundle artifacts like these
	#   so reverting to copying into the module
	cp $< $@


nmdc_schema/nmdc_schema_merged.yaml: project/nmdc_schema_merged.yaml
	cp $< $@

####

.PHONY: check-invalids-for-single-failure

# 		echo "Running command: $$cmd"; \

check-invalids-for-single-failure:
	for file in src/data/invalid/*.yaml; do \
		echo "$$file:"; \
		target_class=$$(basename $$file | cut -d'-' -f1); \
		cmd="poetry run linkml validate --schema nmdc_schema/nmdc_materialized_patterns.yaml --target-class $$target_class $$file"; \
		output=$$($$cmd 2>&1 || true); \
		echo "$$output" | sort | uniq; \
	done

# Generate linkml yaml for all schema files
.PHONY: gen-linkml-schema-files
gen-linkml-schema-files:
