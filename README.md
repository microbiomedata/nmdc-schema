# National Microbiome Data Collaborative Schema

[![PyPI - License](https://img.shields.io/pypi/l/nmdc-schema)](https://github.com/microbiomedata/nmdc-schema/blob/mam-readme/LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/microbiomedata/nmdc-schema?branch=main&kill_cache=1)](https://github.com/microbiomedata/nmdc-schema/commits)
[![GitHub issues](https://img.shields.io/github/issues/microbiomedata/nmdc-schema?branch=master&kill_cache=1)](https://github.com/microbiomedata/nmdc-schema/issues)
[![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/microbiomedata/nmdc-schema?branch=main&kill_cache=1)](https://github.com/microbiomedata/nmdc-schema/issues?q=is%3Aissue+is%3Aclosed)
[![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/microbiomedata/nmdc-schema?branch=main&kill_cache=1)](https://github.com/microbiomedata/nmdc-schema/pulls)

![Deploy Documentation](https://github.com/microbiomedata/nmdc-schema/workflows/Build%20and%20Deploy%20Static%20Mkdocs%20Documentation/badge.svg?branch=main)

This repository defines a [linkml](https://github.com/linkml/linkml) schema for managing metadata from the [National Microbiome Data Collaborative (NMDC)](https://microbiomedata.org/). The NMDC is a multi-organizational effort to integrate microbiome data across diverse areas in medicine, agriculture, bioenergy, and the environment. This integrated platform facilitates comprehensive discovery of and access to multidisciplinary microbiome data in order to unlock new possibilities with microbiome data science. 

Tasks managed by the repository are:

-   Generating the schema
-   Converting the schema from it's native LinkML/YAML format into other artifacts
    -   [JSON-Schema](jsonschema/nmdc.schema.json)
-   Deploying the schema as a PyPI package
-   Deploying the [documentation](https://microbiomedata.github.io/nmdc-metadata/) 

## Background

The NMDC [Introduction to metadata and ontologies](https://microbiomedata.org/introduction-to-metadata-and-ontologies/) primer provides some the context for this project.

See also [these slides](https://microbiomedata.github.io/nmdc-metadata/docs/schema-slides) describing the schema

## Collections within the schema

_If some colelctions are reported to contain 0 documents, it could be that the MongoDB is being repopulated based on new data or a new schema._


| Collection   Name                    | Documents | Avg. Document Size | Total Document Size | Notes                                                                |
|--------------------------------------|----------:|-------------------:|--------------------:|----------------------------------------------------------------------|
| activity_set                         | 0         |                    | 0.0 B               |                                                                      |
| biosample_set                        | 716       | 1.2 KB             | 835.1 KB            |                                                                      |
| capabilities                         | 9         | 120.1 B            | 1.1 KB              |                                                                      |
| data_object_set                      | 12,455    | 294.0 B            | 3.5 MB              |                                                                      |
| date_created                         | 0         |                    | 0.0 B               |                                                                      |
| etl_software_version                 | 0         |                    | 0.0 B               |                                                                      |
| functional_annotation_set            | 0         |                    | 0.0 B               |                                                                      |
| genome_feature_set                   | 0         |                    | 0.0 B               |                                                                      |
| ids                                  | 12        | 29.0 B             | 348.0 B             |                                                                      |
| mags_activity_set                    | 114       | 5.2 KB             | 597.7 KB            |                                                                      |
| metabolomics_analysis_activity_set   | 209       | 72.6 KB            | 14.8 MB             |                                                                      |
| metagenome_annotation_activity_set   | 156       | 649.0 B            | 98.9 KB             |                                                                      |
| metagenome_assembly_set              | 403       | 1.1 KB             | 427.2 KB            |                                                                      |
| metaproteomics_analysis_activity_set | 33        | 3.6 MB             | 120.1 MB            |                                                                      |
| nmdc_schema_version                  | 0         |                    | 0.0 B               |                                                                      |
| nom_analysis_activity_set            | 788       | 431.0 B            | 331.7 KB            |                                                                      |
| notes                                | 0         |                    | 0.0 B               |                                                                      |
| object_types                         | 1         | 141.0 B            | 141.0 B             |                                                                      |
| objects                              | 2         | 412.0 B            | 824.0 B             |                                                                      |
| omics_processing_set                 | 2,716     | 478.5 B            | 1.2 MB              |                                                                      |
| operations                           | 4         | 585.0 B            | 2.3 KB              |                                                                      |
| raw.functional_annotation_set        | 0         |                    | 0.0 B               | "raw" means this collection hasn't been run through any   validation |
| read_QC_analysis_activity_set        | 405       | 611.9 B            | 242.0 KB            |                                                                      |
| read_based_analysis_activity_set     | 274       | 904.0 B            | 241.9 KB            |                                                                      |
| sites                                | 1         | 187.0 B            | 187.0 B             |                                                                      |
| study_set                            | 8         | 1.2 KB             | 9.6 KB              |                                                                      |
| triggers                             | 1         | 146.0 B            | 146.0 B             |                                                                      |
| users                                | 1         | 124.0 B            | 124.0 B             |                                                                      |
| workflows                            | 9         | 161.3 B            | 1.4 KB              |                                                                      |
