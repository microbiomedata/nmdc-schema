# Validating nmdc-schema data against the schema

## Introduction

Please see LinkML Validation documentation for general information on validation with LinkML.
It has several good examples of how to use linkml-validate in a python script or from the command line.
https://linkml.io/linkml/data/validating-data.html


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