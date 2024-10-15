#!/bin/bash

DATABASE_NAME='interleaved'
DIRECTORY_PATH='assets/jsons-for-mongodb'

# Loop through each JSON file in the directory
for file in $DIRECTORY_PATH/*.json
do
    # Get the filename without the path and extension
    BASENAME=$(basename "$file" .json)

    # Run mongoimport for each file
    mongoimport --uri mongodb://localhost:27017/$DATABASE_NAME --collection $BASENAME --file "$file" --jsonArray
done
