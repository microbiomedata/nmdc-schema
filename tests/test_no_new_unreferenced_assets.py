"""Guard against adding an asset with no reference found in the searched files.

A ratchet over the existing backlog, not a clean-room assertion. Every path in
``EXPECTED_UNREFERENCED`` is a file that predates this check; each group below says
why it is still there and where its retirement is tracked. A newly added asset with
no detected reference fails here instead of joining the pile.

The second assertion is the one that connects this to element deprecation: an asset
that has no detected reference and names an element in ``src/schema/deprecated.yaml``
is a priority for retirement review. Check its consumers before deciding its fate.
These candidates are listed separately so the set shrinks visibly as they are retired.

Report and rationale: ``src/scripts/report_asset_usage.py``.
Procedure: ``src/docs/asset-lifecycle.md``.
"""

from pathlib import Path

from src.scripts.report_asset_usage import find_asset_findings

REPO_ROOT = Path(__file__).resolve().parent.parent

# Inputs to the units subsystem and to one-off analyses, kept as reference data. They
# have no generator and no consumer in this repo. Retirement or relocation is tracked in
# https://github.com/microbiomedata/nmdc-schema/issues/2766 (reorganize assets/ into
# inputs/, outputs/, and reference/).
_REFERENCE_DATA = {
    "assets/blanklines.txt",
    "assets/from-sssom-dir/README.md",
    "assets/from-sssom-dir/biosample_ebs_water_packages_unclassified_taxa_sssom.tsv",
    "assets/from-sssom-dir/biosample_env_package_normalizastion.tsv",
    "assets/from-sssom-dir/per_biosample_scoped_ebs_mapping_results.tsv",
    "assets/misc/gold_seqMethod_to_nmdc_instrument_set.tsv",
    "assets/misc/linter_config_default.yaml",
    "assets/misc/neon_raw_data_file_mappings.tsv",
    "assets/misc/neon_sequencingMethod_to_nmdc_instrument_set.tsv",
    "assets/neon_mixs_env_triad_mappings/README.md",
    "assets/neon_mixs_env_triad_mappings/neon-nlcd-local-broad-mappings.tsv",
    "assets/neon_mixs_env_triad_mappings/neon-site-env_medium.tsv",
    "assets/neon_table_types.tsv",
    "assets/pref-unit-slots-claude-ucum-expanded-curated-with-has-problem.tsv",
}

# Git placeholder files. Their entire purpose is to keep an otherwise-empty directory
# tracked; requiring something to name them by path would be a category error.
_GIT_PLACEHOLDERS = {
    "assets/jsons-for-mongodb/.gitkeep",
    "assets/misc/.gitkeep",
}

# Ad-hoc MongoDB queries, run by hand against production rather than by any code here.
# Whether they belong in this repo at all is
# https://github.com/microbiomedata/nmdc-schema/issues/3068 (relocate prod-analytics
# code out of nmdc-schema).
_MANUAL_MONGO_QUERIES = {
    "assets/mongodb_queries/data_qc/biosample_part_of_study.js",
    "assets/mongodb_queries/data_qc/data_generation_has_input_biosample_or_processed_sample.js",
    "assets/mongodb_queries/data_qc/data_generation_has_output_data_objects.js",
    "assets/mongodb_queries/data_qc/data_object_was_generated_by_workflow_execution_or_data_generation.js",
    "assets/mongodb_queries/data_qc/material_processing_has_input_biosample_or_processed_sample.js",
    "assets/mongodb_queries/delete_bioscales_data_objects.js",
    "assets/mongodb_queries/delete_data_generation_has_output_ref_integrity_exceptions.js",
    "assets/mongodb_queries/find_id_nonconforming_data_objects.js",
}

# Outputs of code that has since been deleted, or examples superseded by a class rename.
# Named for retirement in https://github.com/microbiomedata/nmdc-schema/issues/2968
# (remove ncbi_postgres_nmdc_exact_term_matching.py and assets/ncbi_mappings/) and
# https://github.com/microbiomedata/nmdc-schema/issues/3330 (consolidate stray markdown).
_ORPHANED_OUTPUTS = {
    "assets/changesheet_examples/data_generation_id_inst_changesheet.tsv",
    "assets/changesheet_examples/omics_processing_id_inst_changesheet.tsv",
    "assets/misc/README_cookiecutter.md",
    "assets/misc/legacy_migration_notes.md",
    "assets/ncbi_mappings/README.md",
    "assets/ncbi_mappings/ncbi_pg_db_field_mappings.tsv",
    "assets/ncbi_mappings/ncbi_pg_db_field_mappings_filled.tsv",
    "assets/ncbi_mappings/ncbi_pg_db_fields.txt",
    "assets/mongodb_queries/data_qc/functional_annotation_agg_metagenome_metatranscriptome_annotation_id.js",
}

EXPECTED_UNREFERENCED = (
    _REFERENCE_DATA | _MANUAL_MONGO_QUERIES | _ORPHANED_OUTPUTS | _GIT_PLACEHOLDERS
)

# The subset of the above that also names an element in deprecated.yaml. These are
# retirement candidates; the search does not establish that they have no consumers.
# This set should only ever shrink.
EXPECTED_UNREFERENCED_AND_DEPRECATED = {
    "assets/mongodb_queries/data_qc/functional_annotation_agg_metagenome_metatranscriptome_annotation_id.js",
    "assets/ncbi_mappings/ncbi_pg_db_field_mappings.tsv",
    "assets/ncbi_mappings/ncbi_pg_db_field_mappings_filled.tsv",
}


def test_no_new_unreferenced_assets():
    """No file may be added to assets/ without something in the repo naming it."""
    findings = find_asset_findings(REPO_ROOT)
    actual = {finding.path for finding in findings if finding.is_unreferenced}

    unexpected = actual - EXPECTED_UNREFERENCED
    assert not unexpected, (
        f"{len(unexpected)} file(s) under assets/ have no literal reference in the "
        f"searched repository files: {sorted(unexpected)}. Document the consumer, "
        f"write it somewhere else (see the output-destination row in CONTRIBUTING.md), "
        f"or add it to EXPECTED_UNREFERENCED with a reason. "
        f"See src/docs/asset-lifecycle.md."
    )

    retired = EXPECTED_UNREFERENCED - actual
    assert not retired, (
        f"{len(retired)} allowlisted asset(s) are no longer unreferenced: "
        f"{sorted(retired)}. Remove them from EXPECTED_UNREFERENCED so the list stays "
        f"an accurate account of the backlog."
    )


def test_unreferenced_and_deprecated_set_only_shrinks():
    """Track retirement candidates that also name a deprecated element."""
    findings = find_asset_findings(REPO_ROOT)
    actual = {
        finding.path
        for finding in findings
        if finding.is_unreferenced and finding.deprecated_elements
    }

    unexpected = actual - EXPECTED_UNREFERENCED_AND_DEPRECATED
    assert not unexpected, (
        f"{len(unexpected)} unreferenced asset(s) name an element in "
        f"src/schema/deprecated.yaml: {sorted(unexpected)}. Check local and external "
        f"consumers before deciding to delete, regenerate, or retain them. If one must stay, "
        f"add it to EXPECTED_UNREFERENCED_AND_DEPRECATED with a reason. "
        f"See src/docs/schema_element_deprecation_guide.md. "
        f"If your branch did not touch assets/, the likely cause is a deprecation that "
        f"landed on main: an element moved into deprecated.yaml and one of these files "
        f"names it. Run `make report-asset-usage` to see which."
    )

    retired = EXPECTED_UNREFERENCED_AND_DEPRECATED - actual
    assert not retired, (
        f"{len(retired)} allowlisted asset(s) no longer name a deprecated element while "
        f"unreferenced: {sorted(retired)}. Remove them from "
        f"EXPECTED_UNREFERENCED_AND_DEPRECATED so the list stays an accurate account of "
        f"the remaining retirement candidates."
    )
