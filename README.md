<div style="text-align: center;">
    <img src="https://raw.githubusercontent.com/microbiomedata/nmdc-schema/main/images/nmdc_logo_long.jpeg" width="119" height="40" alt="Long NMDC logo"/>
</div>

# National Microbiome Data Collaborative Schema

[![PyPI - License](https://img.shields.io/pypi/l/nmdc-schema)](https://github.com/microbiomedata/nmdc-schema/blob/main/LICENSE)
[![PyPI version](https://badge.fury.io/py/nmdc-schema.svg?any-param=to-cause-a-cache-miss)](https://badge.fury.io/py/nmdc-schema)

The mission of the NMDC is to build a FAIR microbiome data sharing network, through infrastructure, data standards,
and community building, that addresses pressing challenges in environmental sciences. The NMDC platform is built on
top of a unified data model (schema) that weaves together existing standards and ontologies to provide a systematic
representation of all aspects of the microbiome data life cycle.

This repository mainly defines a [LinkML](https://github.com/linkml/linkml) schema for managing metadata from
the [National Microbiome Data Collaborative (NMDC)](https://microbiomedata.org/).

## Documentation

The documentation for the NMDC schema can be found at [https://microbiomedata.github.io/nmdc-schema/](https://microbiomedata.github.io/nmdc-schema/).
This documentation is aimed at consumers of NMDC data and metadata, it describes the different data elements used to describe studies, samples,
sample processing, data generation, workflows, and downstream data objects.

The NMDC [Introduction to metadata and ontologies](https://microbiomedata.org/introduction-to-metadata-and-ontologies/)
primer provides some the context for this project.

The remainder of this page is primary for the internal maintainers and contributors to the NMDC schema

## Repository Contents Overview

Some products that are maintained, and tasks orchestrated within this repository are:

- Maintenance of LinkML YAML that specifies the NMDC Schema
    - [src/schema/nmdc.yaml](src/schema/nmdc.yaml)
    - and various other YAML schemas imported by it,
      like [prov.yaml](src/schema/prov.yaml), [annotation.yaml](src/schema/annotation.yaml), etc. all which you can find
      in the [src/schema](src/schema/) folder
- Makefile targets for converting the schema from it's native LinkML YAML format to other artifact
  like [JSON Schema](project/jsonschema/nmdc.schema.json)
- Build, deployment and distribution of the schema as a [PyPI package](https://pypi.org/project/nmdc-schema/)
- Automatic publishing of refreshed documentation upon change to the schema,
  accessible [here](https://microbiomedata.github.io/nmdc-schema/)

## Maintaining the Schema

See [DEVELOPMENT.md](DEVELOPMENT.md) for instructions on setting up a development environment.

See [MAINTAINERS.md](MAINTAINERS.md) for instructions on using that development environment to maintain the schema.

## Makefiles

Makefiles are text files people can use to tell [`make`](https://www.gnu.org/software/make/manual/make.html#Introduction) (a computer program) how it can _make_ things (or—in general—_do_ things). In the world of Makefiles, those _things_ are called _targets_.

This repo contains 2 Makefiles:
- `Makefile`, based on the generic Makefile from the [LinkML cookiecutter](https://github.com/linkml/linkml-project-cookiecutter)
- `project.Makefile`, which contains _targets_ that are specific to this project

Here's an example of using `make` in this repo:

```shell
# Deletes all files in `examples/output`.
make examples-clean
```
> The `examples-clean` _target_ is defined in the `project.Makefile`. In this repo, the `Makefile` `include`s the `project.Makefile`. As a result, `make` has access to the _targets_ defined in both files.

## Data downloads

The NMDC's metadata about biosamples, studies, bioinformatics workflows, etc. can be obtained from our nmdc-runtime API.
Try entering "biosample_set" or "study_set" into the `collection_name` box
at https://api.microbiomedata.org/docs#/metadata/list_from_collection_nmdcschema__collection_name__get

Or use the API programmatically! Note that some collections are large, so the responses are paged.

You can learn about the other available collections at https://microbiomedata.github.io/nmdc-schema/Database/
