#!/usr/bin/env python3
"""
Check self-containment of LinkML schema files.

This script runs `linkml generate linkml --format yaml` on all YAML files in src/schema/
to check if they are self-contained (can be processed independently).

Files that are currently self-contained should fail if they become non-self-contained
(to prevent backsliding), while files that are currently not self-contained should
show warnings but not fail the test.
"""

import subprocess
import sys
import os
import tempfile
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

# Files that should be self-contained (currently passing)
SELF_CONTAINED_FILES = {
    "src/schema/attribute_values.yaml",
    "src/schema/basic_slots.yaml", 
    "src/schema/external_identifiers.yaml",
    "src/schema/mixs.yaml",
    "src/schema/nmdc_subsets.yaml",
    "src/schema/nmdc_types.yaml",
    "src/schema/nmdc.yaml",
    "src/schema/portal_emsl.yaml",
    "src/schema/portal_enums.yaml",
    "src/schema/portal_jgi_metagenomics.yaml",
    "src/schema/portal_jgi_metatranscriptomics.yaml",
    "src/schema/portal_mixs_inspired.yaml",
    "src/schema/portal_sample_id.yaml"
}

def run_linkml_generate(file_path):
    """
    Run linkml generate on a file and return (success, stderr).
    
    Args:
        file_path: Path to the YAML file to process
        
    Returns:
        tuple: (bool success, str stderr)
    """
    try:
        result = subprocess.run(
            ["poetry", "run", "linkml", "generate", "linkml", "--format", "yaml", file_path],
            capture_output=True,
            text=True,
            check=False
        )
        return result.returncode == 0, result.stderr
    except subprocess.SubprocessError as e:
        return False, f"Subprocess error: {e}"

def main():
    """Main function to check schema self-containment."""
    logging.info("Generating linkml YAML files for all schema files...")
    
    # Find all YAML files in src/schema/
    schema_dir = Path("src/schema")
    if not schema_dir.exists():
        logging.error(f"Error: {schema_dir} directory not found")
        sys.exit(1)
    
    yaml_files = sorted(schema_dir.glob("*.yaml"))
    if not yaml_files:
        logging.error(f"No YAML files found in {schema_dir}")
        sys.exit(1)
    
    exit_code = 0
    
    for file_path in yaml_files:
        file_path_str = str(file_path)
        
        success, stderr = run_linkml_generate(file_path_str)
        
        if not success:
            if file_path_str in SELF_CONTAINED_FILES:
                logging.error(f"ERROR: {file_path_str} is no longer self-contained (backsliding detected)")
                exit_code = 1
            else:
                logging.warning(f"warning: {file_path_str} is not self-contained")
    
    sys.exit(exit_code)

if __name__ == "__main__":
    main()