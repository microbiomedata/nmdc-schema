#!/usr/bin/env python3
"""Block Claude from writing to build output dirs or generated artifacts."""

import json
import sys
from pathlib import PurePosixPath

data = json.load(sys.stdin)
tool = data.get("tool_name", "")
inputs = data.get("tool_input", {})

if tool not in ("Write", "Edit"):
    sys.exit(0)

path = inputs.get("file_path", "")
parts = PurePosixPath(path).parts

# Block writing .md files to docs/ (should be src/docs/)
if "docs" in parts and "src" not in parts and path.endswith(".md"):
    print("BLOCKED: docs/ is a build output directory wiped by 'make clean'.")
    print("Hand-written documentation belongs in src/docs/ instead.")
    print("See: https://github.com/microbiomedata/nmdc-schema/issues/2962")
    sys.exit(2)

# Block editing generated artifacts in nmdc_schema/
GENERATED = {
    "nmdc.py", "nmdc_pydantic.py", "nmdc.schema.json",
    "nmdc_materialized_patterns.yaml",
    "nmdc_materialized_patterns.json",
    "nmdc_materialized_patterns.schema.json",
}
if "nmdc_schema" in parts and PurePosixPath(path).name in GENERATED:
    print(f"BLOCKED: {PurePosixPath(path).name} is a generated artifact — do not edit directly.")
    print("Edit the schema source in src/schema/ and run 'make all' to regenerate.")
    sys.exit(2)
