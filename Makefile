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
SOURCE_SCHEMA_PATH = $(shell bash ./utils/get-value.sh source_schema_path)
SOURCE_SCHEMA_DIR = $(dir $(SOURCE_SCHEMA_PATH))
SRC = src
DEST = project
#PYMODEL = $(SRC)/$(SCHEMA_NAME)/datamodel
#PYMODEL = $(SRC)/$(SCHEMA_NAME)
PYMODEL = $(SCHEMA_NAME)
DOCDIR = docs
EXAMPLEDIR = examples


# basename of a YAML file in model/
.PHONY: all clean examples-all

# note: "help" MUST be the first target in the file,
# when the user types "make" they should get help info
help: status
	@echo ""
	@echo "make setup -- initial setup (run this first)"
	@echo "make site -- makes site locally"
	@echo "make install -- install dependencies"
	@echo "make test -- runs tests"
	@echo "make lint -- perfom linting"
	@echo "make testdoc -- builds docs and runs local test server"
	@echo "make deploy -- deploys site"
	@echo "make update -- updates linkml version"
	@echo "make help -- show this help"
	@echo ""

status: check-config
	@echo "Project: $(SCHEMA_NAME)"
	@echo "Source: $(SOURCE_SCHEMA_PATH)"

# generate products and add everything to github
setup: install gen-project gen-examples gendoc git-init-add

# install any dependencies required for building
install:
	poetry install
.PHONY: install

# ---
# Project Syncronization
# ---
#
# check we are up to date
check: cruft-check
cruft-check:
	# added cruft to poetry env and added poetry wrapper to cruft invocations
	$(RUN) cruft check
cruft-diff:
	$(RUN) cruft diff

update: update-template update-linkml
update-template:
	$(RUN) cruft update

# todo: consider pinning to template
update-linkml:
	poetry add -D linkml@latest

# EXPERIMENTAL
create-data-harmonizer:
	npm init data-harmonizer $(SOURCE_SCHEMA_PATH)

.PHONY: examples-all examples-clean
all: site
site: examples-clean gen-project gendoc \
project/nmdc_schema_generated.yaml project/nmdc_schema_merged.yaml project/nmdc_patterns_materialized.schema.json \
src/data/output
	# just can't seem to tell pyproject.toml to bundle artifacts like these
	# so reverting to copying into the module
	cp project/jsonschema/nmdc.schema.json                   $(PYMODEL)/nmdc_no_patterns.schema.json
	cp project/nmdc_patterns_materialized.schema.json        $(PYMODEL)/nmdc.schema.json
	cp project/nmdc_schema_merged.yaml                       $(PYMODEL)/nmdc_schema_merged_no_patterns.yaml
	cp project/nmdc_schema_generated.yaml                    $(PYMODEL)
	cp sssom/gold-to-mixs.sssom.tsv                          $(PYMODEL)

%.yaml: gen-project
deploy: all mkd-gh-deploy

# In future this will be done by conversion
gen-examples:
	cp src/data/examples/* $(EXAMPLEDIR)

# generates all project files

gen-project: $(PYMODEL)
	# added inclusion/exclusion parameters here, in test rule, and in project directories constant
	$(RUN) gen-project \
		--include jsonschema \
		--include python \
		--exclude excel \
		--exclude graphql \
		--exclude jsonld \
		--exclude jsonldcontext \
		--exclude markdown \
		--include owl \
		--exclude prefixmap \
		--exclude proto \
		--exclude shacl \
		--exclude shex \
		--exclude sqlddl \
		-d $(DEST) $(SOURCE_SCHEMA_PATH) && mv $(DEST)/*.py $(PYMODEL)

test: examples-clean test-schema \
project/nmdc_schema_generated.yaml project/nmdc_schema_merged.yaml project/nmdc_patterns_materialized.schema.json \
src/data/output test-python
# make test sometimes says "make: Nothing to be done for `test'."
test-schema:
	$(RUN) gen-project \
		--exclude excel \
		--exclude graphql \
		--exclude jsonld \
		--exclude jsonldcontext \
		--exclude markdown \
		--exclude prefixmap \
		--exclude proto \
		--exclude shacl \
		--exclude shex \
		--exclude sqlddl \
		--include jsonschema \
		--include owl \
		--include python \
		-d tmp $(SOURCE_SCHEMA_PATH)

test-python:
	$(RUN) python -m unittest discover

lint:
	$(RUN) linkml-lint $(SOURCE_SCHEMA_PATH) | tee assets/lint.log

check-config:
	@(grep my-datamodel about.yaml > /dev/null && printf "\n**Project not configured**:\n\n  - Remember to edit 'about.yaml'\n\n" || exit 0)

# migration of anything mentioning person is incomplete

convert-examples-to-%:
	$(patsubst %, $(RUN) linkml-convert  % -s $(SOURCE_SCHEMA_PATH) -C Person, $(shell find src/data/examples -name "*.yaml"))

examples/%.yaml: src/data/examples/%.yaml
	$(RUN) linkml-convert -s $(SOURCE_SCHEMA_PATH) -C Person $< -o $@
examples/%.json: src/data/examples/%.yaml
	$(RUN) linkml-convert -s $(SOURCE_SCHEMA_PATH) -C Person $< -o $@
examples/%.ttl: src/data/examples/%.yaml
	$(RUN) linkml-convert -P EXAMPLE=http://example.org/ -s $(SOURCE_SCHEMA_PATH) -C Person $< -o $@

# Test documentation locally
serve: mkd-serve

# Python datamodel
$(PYMODEL):
	mkdir -p $@


$(DOCDIR):
	mkdir -p $@

gendoc: $(DOCDIR)
	# added copying of images and renaming of TEMP.md
	cp $(SRC)/docs/*md $(DOCDIR) ; \
	cp -r $(SRC)/docs/images $(DOCDIR) ; \
	$(RUN) gen-doc -d $(DOCDIR) $(SOURCE_SCHEMA_PATH)
	mv $(DOCDIR)/TEMP.md $(DOCDIR)/temp.md

testdoc: gendoc serve

MKDOCS = $(RUN) mkdocs
mkd-%:
	$(MKDOCS) $*

#PROJECT_FOLDERS = sqlschema shex shacl protobuf prefixmap owl jsonschema jsonld graphql excel
PROJECT_FOLDERS = owl jsonschema
git-init-add: git-init git-add git-commit git-status
git-init:
	git init
git-add: .cruft.json
	git add \
		*.md \
		.cruft.json \
		.github \
		.gitignore \
		CODE_OF_CONDUCT.md \
		CONTRIBUTING.md \
		LICENSE \
		MAINTAINERS.md \
		Makefile \
		README.md \
		about.yaml \
		assets \
		examples \
		images \
		mkdocs.yml \
		notebooks \
		poetry.lock \
		project.Makefile \
		pyproject.toml \
		project/ \
		reports \
		src/data \
		src/doc-templates \
		src/docs \
		nmdc_schema \
		src/schema \
		sssom \
		tests \
		util \
		utils

		#		src/nmdc_schema/schema/*yaml \
		# 		src/*/datamodel/*py \

	git add $(patsubst %, project/%, $(PROJECT_FOLDERS))
git-commit:
	git commit -m 'Initial commit' -a
git-status:
	git status

# only necessary if setting up via cookiecutter
.cruft.json:
	echo "creating a stub for .cruft.json. IMPORTANT: setup via cruft not cookiecutter recommended!" ; \
	touch $@

clean:
	rm -rf $(DEST)
	rm -rf tmp
	rm -rf docs/*.md
	rm -rf docs/*.html

include project.Makefile

examples-all: examples-clean project/nmdc_schema_generated.yaml src/data/output

examples-clean:
	@echo running examples-clean
	rm -rf src/data/output project/nmdc_schema_generated.yaml

project/nmdc_schema_generated.yaml:
	@echo making project/nmdc_schema_generated.yaml
	# the need for this may be eliminated by adding mandatory pattern materialization to gen-json-schema
	$(RUN) gen-linkml \
		--output $@ \
		--materialize-patterns \
		--no-materialize-attributes \
		--format yaml $(SOURCE_SCHEMA_PATH)


project/nmdc_schema_merged.yaml:
	$(RUN) gen-linkml \
		--output $@ \
		--no-materialize-patterns \
		--no-materialize-attributes \
		--format yaml $(SOURCE_SCHEMA_PATH)


project/nmdc_patterns_materialized.schema.json: project/nmdc_schema_generated.yaml
	@echo making project/nmdc_schema_generated.yaml
	$(RUN) gen-json-schema \
		--top-class Database \
		--closed $< > $@


src/data/output: project/nmdc_schema_generated.yaml
	@echo making src/data/output
	mkdir -p $@
	$(RUN) linkml-run-examples \
		--schema $< \
		--input-directory src/data/valid \
		--counter-example-input-directory src/data/invalid \
		--output-directory $@ > $@/README.md