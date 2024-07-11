# Validating data against the nmdc-schema

The nmdc-schema's preferred on-disk data serializations are YAML, closely followed by JSON. Preferred databases
are MongDB and any RDF triplestore.

The nmdc-schema Makefiles use the `linkml-validate` and `linkml-run-examples` CLIs for build-time validation of data
file,
both of which build upon JSON Schema validation. `linkml-validate` can even validate against TSV,
as long as the schema classes that are instantiated can reasonably be expressed in a table.
Programmers can learn more about the internals of these tools at https://linkml.io/linkml/data/validating-data.html

We can conceive of validating a data file at two levels

1. The file should be syntactically correct
2. The file should conform to the NMDC schema

## Syntactically correct YAML or JSON

All tools, libraries, or scripts generating NMDC data SHOULD instantiate Python data classes from the nmdc-schema PyPI
package.
It is strongly discouraged to generate Python dicts or JSON by any method other than object instantiation, even using
high-quality, standard JSON libraries. That practice may generate valid data files when first tested but is likely to
degrade
over time. That degradation can be difficult to debug.

Mike Farrah's [yq](https://mikefarah.gitbook.io/yq/v/v3.x/commands/validate)
is a system dependency for the nmdc-schema. It can be used to validate legacy YAML and JSON data.
If malformed YAML or JSON is presented to `linkml-validate`, the error messages may not be as helpful as the messages
from `yq` or some other syntactical validator.

## What to do if the data do not validate

Start by reflecting on whether your data may be ahead of what the schema can currently account for.

1. The data are reasonable, but the schema needs to be extended or modified to account for it
2. The schema really does provide support for your data, but you are just not adhering to it

For 1, you can make PR on the schema yaml. If you aren't comfortable editing LinkML YAML,
then you can get help from one of the schema developers. We recommend filing a new ticket explaining the issue.
Please include your error messages.

For 2, we suggest taking a minimal example approach. `linkml-validate` is very good at identifying schema violations
in small, syntactically valid data files. Debugging can be aided in pulling out single data instances
and first verifying that they are syntactically valid YAML or JSON. If you don't want to use yq, then you could paste
one instance into a website like https://jsonlint.com/.
A common issue in multi-instance files is using incorrect syntax for grouping the instances into a YAML or JSON array.
Using a small subsample of your data and an online linter as above can aide in debugging this.

## Expectations of NMDC data producers

It is expected that data producers or transformers take the upfront initiative to validate their data.

Currently, not all providers of information to NMDC provide JSON - for
example, GOLD is provided as database dumps, and an ETL process
transforms this into JSON. In the future, we would like to move towards a
situation where all information is provided as JSON.
