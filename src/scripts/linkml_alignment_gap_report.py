"""Generate an explicit backend and coverage-gap report for ontology alignment work."""

from __future__ import annotations

from pathlib import Path

import click

from nmdc_schema.ontology_alignment_prototype import (
    available_tooling,
    build_schema_index,
    read_alignment_rows,
    summarize_property_like_gap,
    summarize_source_distribution,
    write_json,
)


@click.command()
@click.option("--schema", default="src/schema/nmdc.yaml", show_default=True, help="Path to the NMDC LinkML schema")
@click.option(
    "--baseline-results",
    default="/tmp/ols4_embeddings_results.tsv",
    show_default=True,
    help="Baseline semantic retrieval TSV, typically the OLS4 embeddings output from #2909",
)
@click.option(
    "--ontology-prefix",
    default="OBI",
    show_default=True,
    help="Ontology prefix to highlight in the gap analysis",
)
@click.option(
    "--summary-json",
    default="local/linkml_alignment_gap_report.json",
    show_default=True,
    help="JSON path for the gap report",
)
def cli(
    schema: str,
    baseline_results: str,
    ontology_prefix: str,
    summary_json: str,
) -> None:
    """Make retrieval and backend blind spots explicit for the current prototype."""
    schema_index = build_schema_index(schema)
    baseline_rows = read_alignment_rows(baseline_results)
    summary = {
        "tooling_available": available_tooling(),
        "baseline_source_distribution": summarize_source_distribution(baseline_rows),
        "property_like_gap_all_sources": summarize_property_like_gap(schema_index, baseline_rows, ontology_prefix=None),
        "property_like_gap_target_source": summarize_property_like_gap(schema_index, baseline_rows, ontology_prefix=ontology_prefix),
        "backend_gap_notes": [
            "OLS4 embeddings baseline is class-oriented and may miss slot->property alignments.",
            "BioPortal and other non-OLS repositories may expose additional ontology families not emphasized by the OLS4 baseline.",
            "semsql and oaklib help most after retrieval by expanding graph context, relationships, and domain/range neighborhoods.",
            "LinkML-side retrieval uses oaklib + linkml-store, with BioPortal-backed corpus harvesting available via `make alignment-linkml-store-bioportal`.",
        ],
    }
    Path(summary_json).parent.mkdir(parents=True, exist_ok=True)
    write_json(summary, summary_json)
    click.echo(f"Wrote gap report JSON: {summary_json}")


if __name__ == "__main__":
    cli()
