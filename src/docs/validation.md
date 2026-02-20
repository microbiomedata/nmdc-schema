# Validating nmdc-schema data against the NMDC Schema

## Introduction

Please see LinkML Validation documentation for general information on validation with LinkML.
It has several good examples of how to use linkml-validate in a python script or from the command line.
https://linkml.io/linkml/data/validating-data.html

## Validating from the command line

The `linkml validate` CLI command can be used to validate a YAML data file against the NMDC schema.
The `--target-class` option specifies the class that the top-level object in the data file should conform to.

Validating a valid file (no output means success):

```bash
linkml validate \
  --schema nmdc_schema/nmdc_materialized_patterns.yaml \
  --target-class Biosample \
  src/data/valid/Biosample-minimal.yaml
```

Validating a file that contains a schema violation (output shows the error):

```bash
linkml validate \
  --schema nmdc_schema/nmdc_materialized_patterns.yaml \
  --target-class Biosample \
  src/data/invalid/Biosample-minimal-invalid-type.yaml
```

Note: `nmdc_schema/nmdc_materialized_patterns.yaml` is the pre-built schema artifact used for validation.
If you have not already built the schema, you can use `src/schema/nmdc.yaml` as the `--schema` value instead,
though this requires all schema imports to be resolvable.

## Validating from Python

Using the examples in src/docs/examples, we can validate the data against the schema in python:

```python
from linkml.validator import validate

instance = {
    "id": "nmdc:bsm-99-dtTMNb",
    "associated_studies": ["nmdc:study-00-abc123"],
    "env_broad_scale": {
        "has_raw_value": "ENVO:00002030",
        "term": {
            "id": "ENVO:00002030"
        }
    },
    "env_local_scale": {
        "has_raw_value": "ENVO:00002169",
        "term": {
            "id": "ENVO:00002169"
        }
    },
    "env_medium": {
        "has_raw_value": "ENVO:00005792",
        "term": {
            "id": "ENVO:00005792"
        }
    },
    "type": "nmdc:Biosample",
    "analysis_type": [
        "amplicon sequencing assay",
        "metagenomics"
    ]
}

report = validate(instance, "nmdc.yaml", "Biosample")

if not report.results:
    print('The instance is valid!')
else:
    for result in report.results:
        print(result.message)
```