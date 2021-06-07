# National Microbiome Data Collaborative Schema

[![PyPI - License](https://img.shields.io/pypi/l/nmdc-schema)](https://github.com/microbiomedata/nmdc-schema/blob/mam-readme/LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/microbiomedata/nmdc-schema?branch=main&kill_cache=1)](https://github.com/microbiomedata/nmdc-schema/commits)
[![GitHub issues](https://img.shields.io/github/issues/microbiomedata/nmdc-schema?branch=master&kill_cache=1)](https://github.com/microbiomedata/nmdc-schema/issues)
[![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/microbiomedata/nmdc-schema?branch=main&kill_cache=1)](https://github.com/microbiomedata/nmdc-schema/issues?q=is%3Aissue+is%3Aclosed)
[![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/microbiomedata/nmdc-schema?branch=main&kill_cache=1)](https://github.com/microbiomedata/nmdc-schema/pulls)

![Deploy Documentation](https://github.com/microbiomedata/nmdc-schema/workflows/Build%20and%20Deploy%20Static%20Mkdocs%20Documentation/badge.svg?branch=main)

This repository defines a linkml  schema for managing metadata from the [National Microbiome Data Collaborative (NMDC)](https://microbiomedata.org/). The NMDC is a multi-organizational effort to enable integrated microbiome data across diverse areas in medicine, agriculture, bioenergy, and the environment. This integrated platform facilitates comprehensive discovery of and access to multidisciplinary microbiome data in order to unlock new possibilities with microbiome data science. 

Tasks managed by the repository are:

-   Generating the schema
-   Deploying the [documentation](https://microbiomedata.github.io/nmdc-metadata/) 
-   Integrating metadata from multiple environmental data repositories
    -   *was ./metadata-translation/notebooks*

## Background

The NMDC [Introduction to metadata and ontologies](https://microbiomedata.org/introduction-to-metadata-and-ontologies/) primer describes the context for this project.

## Schema

See the [slides](https://microbiomedata.github.io/nmdc-metadata/docs/schema-slides) describing the schema

-   this and other relevant docs are available at 

The [NMDC schema](./schema) is used during the [translation process](./metadata-translation/notebooks) to specify how metadata elements are related.

-   broken

![img](https://raw.githubusercontent.com/microbiomedata/nmdc-metadata/master/schema/nmdc_schema_uml.png)

-   broken, better alternatives exist

The schema is also available as:

-   [JSON-Schema](jsonschema/nmdc.schema.json)

- markdown docs
- json ld for FAIRness


-   [Protobuf](schema/nmdc.proto)
    -   fodler missing
-   [GraphQL](schema/nmdc.graphql)
    -   folder present but no graphql file
-   [OWL](schema/nmdc.owl)
    -   folder present but no owl file
-   [RDF](placeholder)
    -   folder present but no rdf file
    -   template says "(direct mapping)"
-   [ShEx](schema/nmdc.shex)
    -   folder present but no shex file

The template also promises

-   SQL DDL (TODO)
-   TSV/CSV reports

## Documentation

[Documentation](https://microbiomedata.github.io/nmdc-metadata/) for the NMDC schema can be browsed here:

- redundant links. from seperate repo.

* * *

## Under Construction! A proper README will appear soon.

What you see now comes from the template used to bootstrap this repo.

There are several other repositories that may be of interest:

-   

Template "allows you to create a project for your schema as quickly as
possible. It takes care of generating a beautiful readthedocs themed
site, as well as downstream artefacts..."

highlights from quickstart 

-   Rename the schema file in [src/schema](src/schema). Keep the `.yaml` suffix
-   Type `make install all` to build your downstream artefacts (jsonschema, owl, etc)
-   Type `make gh-deploy` to make a GitHub pages website

Minor tweak: for now you must pass in the name of your schema on the command line, e.g.

```bash
make all SCHEMA_NAME=my_awesome_schema
```

## How it works

This repo is a GitHub "template" repo. When you "Use this template" it will make a copy for your project.

Everything is orchestrated by a generic single [Makefile](Makefile). For this to work you should follow certain conventions:

-   Keep your schema in src/schema
-   Use the `.yaml` suffix for all schema files
-   Use the suggested directory layout here.

To run the Makefile you will need Python (>=3.7), and biolinkml. You can type:

```bash
make install
```

or equivalently

```bash
. environment.sh
pip install -r requirements.txt
```

You can make specific targets, e.g

```bash
make stage-jsonschema
```

Use the `all` target to make everything

Note to redeploy documentation all you need to do is:

```bash
make gh-deploy
```

That's it!

The Makefile takes care of dependencies. Downstream files are only rebuilt if source files change.

## Documentation framework

You can change the theme by editing [mkdocs.yml](mkdocs.yml)

Do not edit docs in place. They are placed in the `docs` dir by `make stage-docs`.

You can add your own docs to \`src/docs/

Note that docs are actually deployed on the gh-pages branch, but you don't need to worry about this. Just type:

```bash
make gh-deploy
```

The template site is deployed on



But this is not very interesting as it is a toy schema

## TODO

-   [ ] GitHub actions
-   [ ] Making separate modules for each import
