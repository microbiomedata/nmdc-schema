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

.PHONY: all clean examples-clean install site site-clean site-copy squeaky-clean test test-python test-with-examples

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
	@echo ""

cookiecutter-help: status
	@echo ""
	@echo "make setup -- initial setup (run this first)"
	@echo "make site -- makes site locally"
	@echo "make install -- install dependencies"
	@echo "make test -- runs tests"
	@echo "make lint -- perfom linting"
	@echo "make testdoc -- builds docs and runs local test server"
	@echo "make deploy -- deploys site"
	@echo "make update -- updates linkml version"
	@echo "make cookiecutter-help -- show this help"
	@echo ""

status: check-config
	@echo "Project: $(SCHEMA_NAME)"
	@echo "Source: $(SOURCE_SCHEMA_PATH)"

# generate products and add everything to github
setup: install gen-project gendoc git-init-add

# install any dependencies required for building
install:
	poetry install


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
site: clean site-clean gen-project gendoc migration-doctests nmdc_schema/gold-to-mixs.sssom.tsv

%.yaml: gen-project

# was deploy: all mkd-gh-deploy
deploy: gendoc mkd-gh-deploy

gen-project: $(PYMODEL) src/schema/mixs.yaml
	$(RUN) gen-project \
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
		-d $(DEST) $(SOURCE_SCHEMA_PATH) && mv $(DEST)/*.py $(PYMODEL)
		cp project/jsonschema/nmdc.schema.json  $(PYMODEL)


test: examples-clean site test-python examples/output
only-test: examples-clean test-python examples/output

test-schema:
	$(RUN) gen-project \
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
		-d tmp $(SOURCE_SCHEMA_PATH)

test-python:
	$(RUN) python -m unittest discover
	$(RUN) python -m doctest nmdc_schema/nmdc_data.py

lint:
	$(RUN) linkml-lint $(SOURCE_SCHEMA_PATH) > local/lint.log

check-config:
	@(grep my-datamodel about.yaml > /dev/null && printf "\n**Project not configured**:\n\n - Remember to edit 'about.yaml'\n\n" || exit 0)

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
	$(RUN) gen-doc -d $(DOCDIR) --template-directory $(SRC)/$(TEMPLATEDIR) $(SOURCE_SCHEMA_PATH)
	mkdir -p $(DOCDIR)/javascripts
	$(RUN) cp $(SRC)/scripts/*.js $(DOCDIR)/javascripts/

testdoc: gendoc serve

MKDOCS = $(RUN) mkdocs
mkd-%:
	$(MKDOCS) $*

PROJECT_FOLDERS = jsonldcontext jsonschema owl python rdf
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
		RELEASE_NOTES_v7.7.2_to_v7.7.7.md \
		about.yaml \
		assets \
		images \
		mkdocs.yml \
		nmdc_schema \
		notebooks \
		poetry.lock \
		project.Makefile \
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

# custom
site-clean: clean
	rm -rf nmdc_schema/*.json
	rm -rf nmdc_schema/*.tsv
	rm -rf nmdc_schema/*.yaml

squeaky-clean: clean examples-clean rdf-clean shuttle-clean site-clean # does not include mixs-yaml-clean
	rm -rf local/biosample_slots_ranges_report.tsv

nmdc_schema/nmdc_materialized_patterns.yaml:
	$(RUN) gen-linkml \
		--format yaml \
		--materialize-patterns \
		--no-materialize-attributes \
		--output $@ $(SOURCE_SCHEMA_PATH)

nmdc_schema/nmdc_materialized_patterns.schema.json: nmdc_schema/nmdc_materialized_patterns.yaml
	$(RUN) gen-json-schema \
		--closed \
		--include-range-class-descendants \
		--top-class Database $< > $@

# todo this target makes a lot of prerequisites if necessary, but they aren't part of the copying prpocess
# the sssom/ files should be double checked too... they're probably not all SSSSOM files
nmdc_schema/gold-to-mixs.sssom.tsv: sssom/gold-to-mixs.sssom.tsv nmdc_schema/nmdc_materialized_patterns.schema.json \
nmdc_schema/nmdc_materialized_patterns.yaml
	# just can't seem to tell pyproject.toml to bundle artifacts like these
	#   so reverting to copying into the module
	cp $< $@


