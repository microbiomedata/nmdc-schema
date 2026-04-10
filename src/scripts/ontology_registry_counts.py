"""Count ontology registries and extract prefixes across major ontology sources."""

from __future__ import annotations

import csv
import json
import os
from pathlib import Path

import click

from nmdc_schema.ontology_registry_counts import (
    fetch_bioportal_registry,
    fetch_obo_foundry_registry,
    fetch_ols_overall_registry,
    fetch_semsql_registry,
    read_ols_embeddings_corpus,
    summarize_registry_differences,
)


def write_json(data: dict, output_path: str | Path) -> None:
    Path(output_path).write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")


def write_tsv(rows: list[dict[str, str]], output_path: str | Path) -> None:
    if not rows:
        Path(output_path).write_text("")
        return
    fieldnames = list(rows[0].keys())
    with Path(output_path).open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


@click.command()
@click.option(
    "--ols-embeddings-results",
    default="/tmp/ols4_embeddings_results.tsv",
    show_default=True,
    help="OLS-derived semantic results TSV used to define the current embeddings corpus",
)
@click.option(
    "--include-bioportal/--skip-bioportal",
    default=True,
    show_default=True,
    help="Include BioPortal counts and acronyms using BIOPORTAL_API_KEY from the environment",
)
@click.option(
    "--output-json",
    default="local/ontology_registry_counts.json",
    show_default=True,
    help="JSON summary output path",
)
@click.option(
    "--output-prefixes-tsv",
    default="local/ontology_registry_prefixes.tsv",
    show_default=True,
    help="TSV path for per-source prefixes/acronyms",
)
def cli(
    ols_embeddings_results: str,
    include_bioportal: bool,
    output_json: str,
    output_prefixes_tsv: str,
) -> None:
    """Count ontology registries and emit reproducible counts plus prefix lists."""
    ols_overall = fetch_ols_overall_registry()
    ols_embeddings_corpus = read_ols_embeddings_corpus(ols_embeddings_results)
    obo_foundry_registry = fetch_obo_foundry_registry()
    semsql_registry = fetch_semsql_registry()
    bioportal_registry = None
    if include_bioportal:
        if os.environ.get("BIOPORTAL_API_KEY"):
            bioportal_registry = fetch_bioportal_registry()
        else:
            click.echo("WARNING: BIOPORTAL_API_KEY not set; skipping BioPortal registry.", err=True)

    summary = {
        "ols_overall": ols_overall,
        "ols_embeddings_corpus": ols_embeddings_corpus,
        "obo_foundry_registry": obo_foundry_registry,
        "semantic_sql_registry": semsql_registry,
        "bioportal": bioportal_registry,
        "comparisons": summarize_registry_differences(
            ols_overall=ols_overall,
            ols_embeddings_corpus=ols_embeddings_corpus,
            obo_foundry_registry=obo_foundry_registry,
            bioportal_registry=bioportal_registry,
            semsql_registry=semsql_registry,
        ),
    }

    prefix_rows: list[dict[str, str]] = []
    for source_key, payload in [
        ("ols_overall", ols_overall),
        ("ols_embeddings_corpus", ols_embeddings_corpus),
        ("obo_foundry_registry", obo_foundry_registry),
        ("semantic_sql_registry", semsql_registry),
        ("bioportal", bioportal_registry),
    ]:
        if not payload:
            continue
        for prefix in payload["prefixes"]:
            prefix_rows.append({"source_name": source_key, "prefix": prefix})

    Path(output_json).parent.mkdir(parents=True, exist_ok=True)
    Path(output_prefixes_tsv).parent.mkdir(parents=True, exist_ok=True)
    write_json(summary, output_json)
    write_tsv(prefix_rows, output_prefixes_tsv)

    click.echo(f"OLS overall count: {ols_overall['count']}")
    click.echo(f"OLS embeddings corpus count: {ols_embeddings_corpus['count']}")
    click.echo(f"OBO Foundry registry count: {obo_foundry_registry['count']}")
    click.echo(f"semantic-sql registry count: {semsql_registry['count']}")
    if bioportal_registry:
        click.echo(f"BioPortal count: {bioportal_registry['count']}")
    click.echo(f"Wrote summary JSON: {output_json}")
    click.echo(f"Wrote prefixes TSV: {output_prefixes_tsv}")


if __name__ == "__main__":
    cli()
