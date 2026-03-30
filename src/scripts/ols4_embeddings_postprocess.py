"""Post-process OLS4 embeddings results with schema-aware diagnostics."""

from __future__ import annotations

from pathlib import Path

import click

from nmdc_schema.ontology_alignment_prototype import (
    build_schema_index,
    enrich_alignment_rows,
    parse_csv_option,
    read_alignment_rows,
    summarize_alignment_rows,
    write_json,
    write_tsv,
)


@click.command()
@click.option("--schema", default="src/schema/nmdc.yaml", show_default=True, help="Path to LinkML schema YAML")
@click.option(
    "--semantic-results",
    required=True,
    help="TSV of semantic candidates, e.g. ols4_embeddings_results.tsv",
)
@click.option(
    "--output",
    "-o",
    default="local/ols4_embeddings_enriched.tsv",
    show_default=True,
    help="Output TSV path for enriched candidate rows",
)
@click.option(
    "--summary-json",
    default="local/ols4_embeddings_summary.json",
    show_default=True,
    help="Summary JSON path",
)
@click.option(
    "--semantic-threshold",
    default=0.90,
    show_default=True,
    help="Threshold for strong semantic confidence",
)
@click.option(
    "--lexical-threshold",
    default=0.45,
    show_default=True,
    help="Threshold below which lexical similarity is treated as weak",
)
@click.option(
    "--allowed-ontologies",
    default="",
    help="Comma-separated ontology prefixes to keep, e.g. OBI,ENVO,CHMO",
)
@click.option(
    "--excluded-ontologies",
    default="",
    help="Comma-separated ontology prefixes to exclude",
)
@click.option(
    "--subject-categories",
    default="",
    help="Comma-separated subject categories to keep: class,slot,enum,permissible_value",
)
@click.option(
    "--resolve-ols-metadata/--skip-ols-metadata",
    default=False,
    show_default=True,
    help="Resolve per-hit OLS metadata to distinguish classes from properties",
)
def cli(
    schema: str,
    semantic_results: str,
    output: str,
    summary_json: str,
    semantic_threshold: float,
    lexical_threshold: float,
    allowed_ontologies: str,
    excluded_ontologies: str,
    subject_categories: str,
    resolve_ols_metadata: bool,
) -> None:
    """Enrich OLS4 semantic hits with schema context and lexical diagnostics."""
    schema_index = build_schema_index(schema)
    semantic_rows = read_alignment_rows(semantic_results)
    enriched = enrich_alignment_rows(
        rows=semantic_rows,
        schema_index=schema_index,
        semantic_threshold=semantic_threshold,
        lexical_threshold=lexical_threshold,
        allowed_ontologies=parse_csv_option(allowed_ontologies),
        excluded_ontologies=parse_csv_option(excluded_ontologies),
        allowed_subject_categories={item.lower() for item in parse_csv_option(subject_categories)},
        resolve_ols_metadata=resolve_ols_metadata,
    )

    Path(output).parent.mkdir(parents=True, exist_ok=True)
    Path(summary_json).parent.mkdir(parents=True, exist_ok=True)
    write_tsv(enriched, output)

    summary = summarize_alignment_rows(enriched)
    summary["schema_elements_indexed"] = len(schema_index)
    write_json(summary, summary_json)

    click.echo(f"Indexed schema elements: {len(schema_index)}")
    click.echo(f"Semantic candidates analyzed: {len(enriched)}")
    click.echo(f"Wrote enriched TSV: {output}")
    click.echo(f"Wrote summary JSON: {summary_json}")


if __name__ == "__main__":
    cli()
