#!/bin/bash

# Path to the schema file
SCHEMA="../../nmdc_schema/nmdc_materialized_patterns.yaml"

# Directory containing the data files
DATA_DIR="../../src/data/valid"

# Loop over all files in the directory
for file in "$DATA_DIR"/*; do
  # Extract the class name from the filename by cutting on the first hyphen
  class_name=$(basename "$file" | cut -d'-' -f1)

  echo "$file"
  echo "$class_name"

#  # Run the linkml-validate command
#  linkml-validate --schema "$SCHEMA" --target-class "$class_name" "$file"

  # Set output filename for the RDF/TTL file
  output_ttl="${file%.yaml}.ttl"

  # Run the linkml-convert command
  linkml-convert --schema "$SCHEMA" --target-class "$class_name" --output "$output_ttl" "$file"

done
