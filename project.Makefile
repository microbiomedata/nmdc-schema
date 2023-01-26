## Add your own custom Makefile targets here
RUN=poetry run

SCHEMA_NAME = $(shell bash ./utils/get-value.sh name)
SOURCE_SCHEMA_PATH = $(shell bash ./utils/get-value.sh source_schema_path)

all: clean src/data/output

clean:
	rm -rf src/data/output

src/data/output:
	mkdir -p $@
	$(RUN) linkml-run-examples \
		--schema $(SOURCE_SCHEMA_PATH) \
		--input-directory src/data/valid \
		--counter-example-input-directory src/data/invalid \
		--output-directory $@ > $@/README.md

