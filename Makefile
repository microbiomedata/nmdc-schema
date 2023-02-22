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
#PYMODEL = $(SRC)/$(SCHEMA_NAME)/datamodel
#PYMODEL = $(SRC)/$(SCHEMA_NAME)
PYMODEL = $(SCHEMA_NAME)
EXAMPLEDIR = examples

.PHONY: all clean combined-extras examples-clean site test

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
# Project Synchronization
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

all: site
site_prep:
	rm -rf src/schema/mixs.yaml \
src/schema/mixs.yaml.bak \
src/schema/nmdc.yaml.bak

site: site_prep src/schema/mixs.yaml src/schema/mixs.yaml gen-project gendoc # may change files in nmdc_schema/ or project/. uncommitted changes are not tolerated by mkd-gh-deploy

%.yaml: gen-project

# was deploy: all mkd-gh-deploy
deploy: gendoc mkd-gh-deploy

# In future this will be done by conversion
gen-examples:
	cp src/data/examples/* $(EXAMPLEDIR)

gen-project: $(PYMODEL)
	# added inclusion/exclusion parameters here, in test rule, and in project directories constant
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
		-d $(DEST) $(SOURCE_SCHEMA_PATH) && mv $(DEST)/*.py $(PYMODEL)

test: combined-extras test-schema test-python

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
	$(RUN) linkml-lint $(SOURCE_SCHEMA_PATH) | tee assets/misc/lint.log

check-config:
	@(grep my-datamodel about.yaml > /dev/null && printf "\n**Project not configured**:\n\n - Remember to edit 'about.yaml'\n\n" || exit 0)

convert-examples-to-%:
	$(patsubst %, $(RUN) linkml-convert % -s $(SOURCE_SCHEMA_PATH) -C Person, $(shell find src/data/examples -name "*.yaml"))

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
	#mv $(DOCDIR)/TEMP.md $(DOCDIR)/temp.md

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
		nmdc_schema \
		notebooks \
		poetry.lock \
		project.Makefile \
		project/ \
		pyproject.toml \
		reports \
		src/ \
		sssom \
		tests \
		util \
		utils

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

examples-clean: clean
	@echo running examples-clean
	rm -rf src/data/output project/nmdc_*.yaml


project/nmdc_schema_merged.yaml:
	$(RUN) gen-linkml \
		--format yaml \
		--no-materialize-attributes \
		--no-materialize-patterns \
		--output $@ $(SOURCE_SCHEMA_PATH)

project/nmdc_materialized_patterns.yaml:
	$(RUN) gen-linkml \
		--format yaml \
		--materialize-patterns \
		--no-materialize-attributes \
		--output $@ $(SOURCE_SCHEMA_PATH)

project/nmdc_materialized_patterns.schema.json: project/nmdc_materialized_patterns.yaml
	$(RUN) gen-json-schema \
		--closed \
		--top-class Database $< > $@

src/data/output: project/nmdc_materialized_patterns.yaml
	@echo making src/data/output
	mkdir -p $@
	$(RUN) linkml-run-examples \
		--counter-example-input-directory src/data/invalid \
		--input-directory src/data/valid \
		--output-directory $@ \
		--schema $< > $@/README.md

#		--input-formats json \
#		--input-formats yaml \

combined-extras: examples-clean gen-project gendoc \
project/nmdc_schema_merged.yaml project/nmdc_materialized_patterns.yaml project/nmdc_materialized_patterns.schema.json \
src/data/output
	# just can't seem to tell pyproject.toml to bundle artifacts like these
	#   so reverting to copying into the module
	cp project/jsonschema/nmdc.schema.json                   $(PYMODEL)
	cp project/nmdc_materialized_patterns.schema.json        $(PYMODEL)
	cp project/nmdc_materialized_patterns.yaml               $(PYMODEL)
	cp project/nmdc_schema_merged.yaml                       $(PYMODEL)
	cp sssom/gold-to-mixs.sssom.tsv                          $(PYMODEL)

