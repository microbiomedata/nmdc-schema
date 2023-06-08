<p align="center">
    <img src="images/nmdc_logo_long.jpeg" width="100" height="40"/>
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

Some optional components use the Java-based [ROBOT](http://robot.obolibrary.org/), which might be replaced with Jena arq
in the future.

See [MAINTAINERS.md](MAINTAINERS.md) for instructions on maintaining and updating the schema.

## Data downloads

The NMDC's metadata about biosamples, studies, bioinformatics workflows, etc. can be obtained from our nmdc-runtime API.
Try entering "biosample_set" or "study_set" into the `collection_name` box
at https://api.microbiomedata.org/docs#/metadata/list_from_collection_nmdcschema__collection_name__get

Or use the API programmatically! Note that some collections are large, so the responses are paged.

You can learn about the other available collections at https://microbiomedata.github.io/nmdc-schema/Database/
