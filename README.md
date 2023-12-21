<p align="center">
    <img src="https://raw.githubusercontent.com/microbiomedata/nmdc-schema/main/images/nmdc_logo_long.jpeg" width="119" height="40"/>
</p>

# National Microbiome Data Collaborative Schema

[![PyPI - License](https://img.shields.io/pypi/l/nmdc-schema)](https://github.com/microbiomedata/nmdc-schema/blob/main/LICENSE)
[![PyPI version](https://badge.fury.io/py/nmdc-schema.svg)](https://badge.fury.io/py/nmdc-schema)

The NMDC is a multi-organizational effort to integrate microbiome data across diverse areas in medicine, agriculture,
bioenergy, and the environment. This integrated platform facilitates comprehensive discovery of and access to
multidisciplinary microbiome data in order to unlock new possibilities with microbiome data science.

This repository mainly defines a [LinkML](https://github.com/linkml/linkml) schema for managing metadata from
the [National Microbiome Data Collaborative (NMDC)](https://microbiomedata.org/).

## Repository Contents Overview

Some products that are maintained, and tasks orchestrated within this repository are:

- Maintenance of LinkML YAML that specifies the NMDC Schema
    - [src/schema/nmdc.yaml](src/schema/nmdc.yaml)
    - and various other YAML schemas imported by it,
      like [prov.yaml](src/schema/prov.yaml), [annotation.yaml](src/schema/annotation.yaml), etc. all which you can find
      in the [src/schema](src/schema/) folder
- Makefile targets for converting the schema from it's native LinkML YAML format to other artifact
  like [JSON Schema](project/jsonschema/nmdc.schema.json)
- Build, deployment and distribution of the schema as a PyPI package
- Automatic publishing of refreshed documentation upon change to the schema,
  accessible [here](https://microbiomedata.github.io/nmdc-schema/)

## Background

The NMDC [Introduction to metadata and ontologies](https://microbiomedata.org/introduction-to-metadata-and-ontologies/)
primer provides some the context for this project.

## Maintaining the Schema

**New system requirement: [Mike Farah's GO-based yq](https://github.com/mikefarah/yq)**

Some optional components use the Java-based [ROBOT](http://robot.obolibrary.org/) or Jena arq.
Jena riot is also a part of the MongoDB dumping, repairing and validation workflow, if the user wishes
to generate and validate RDF/TTL.

See [MAINTAINERS.md](MAINTAINERS.md) for instructions on maintaining and updating the schema.

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

## Development

This repository contains a `Dockerfile` you can use to run a container in which all the dependencies of `nmdc-schema` are present.

### Usage

You can build the container by issuing the following command in the root folder of the repo:

```shell
# Build a Docker image based upon the Dockerfile in the current folder.
docker build -t nmdc-schema .
```

Once the container has been built, you can run it with:

```shell
# Instantiate the Docker image as a container, mount the current folder within it,
# attach your terminal to the container's STDIN, STDOUT, and STDERR streams,
# run `bash` within the container, and delete the container as soon as `bash` stops running.
docker run --name nmdc-schema --rm -it -v "$(pwd):/src" nmdc-schema /bin/bash
```

Then, inside the Docker container, you can run whatever shell commands you want:

```shell
poetry install
make squeaky-clean
poetry shell
# etc.
```

Alternatively, once the container has been built, you can run a specific shell command in it:

```shell
docker run --name nmdc-schema --rm -it -v "$(pwd):/src" nmdc-schema /bin/bash -c "hostname; whoami"
```

#### mkdocs

In case you want to test the `mkdocs`, you can run the container with its port `8000` mapped to a localhost port (e.g. `18000`):

```shell
docker run --name nmdc-schema --rm -it -v "$(pwd):/src" -p "18000:8000" nmdc-schema /bin/bash
```

Then, inside the Docker container:

```shell
# Start the mkdocs server, binding the server to host "0.0.0.0" (i.e. allowing requests to come from any host) instead of "localhost" (default).
$ poetry run mkdocs serve --dev-addr 0.0.0.0:8000
```

Finally, on your computer, visit the documentation website at http://localhost:18000/nmdc-schema/
