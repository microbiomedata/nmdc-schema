"""Generate a small review-oriented shortlist from enriched alignment rows."""

from __future__ import annotations

from pathlib import Path

import click

from nmdc_schema.ontology_alignment_prototype import (
    enrich_review_rows,
    parse_quota_option,
    read_alignment_rows,
    shortlist_alignment_rows,
    summarize_review_rows,
    write_json,
    write_tsv,
)


@click.command()
@click.option(
    "--enriched-results",
    required=True,
    help="TSV from linkml_embeddings_alignment_prototype.py or similar enriched output",
)
@click.option(
    "--output",
    "-o",
    default="local/linkml_alignment_review.tsv",
    show_default=True,
    help="Review TSV path",
)
@click.option(
    "--summary-json",
    default="local/linkml_alignment_review_summary.json",
    show_default=True,
    help="Review summary JSON path",
)
@click.option(
    "--top-n",
    default=50,
    show_default=True,
    help="Number of shortlisted rows to keep",
)
@click.option(
    "--preferred-buckets",
    default="strong_semantic_weak_lexical_structurally_supported,strong_semantic_strong_lexical",
    show_default=True,
    help="Comma-separated structural buckets to prioritize in shortlist order",
)
@click.option(
    "--max-per-subject",
    default=3,
    show_default=True,
    help="Maximum shortlisted rows per NMDC subject",
)
@click.option(
    "--match-type-quotas",
    default="slot->class=15,class->class=10,pv->class=15,enum->class=10",
    show_default=True,
    help="Comma-separated quotas per match type to keep the shortlist informative",
)
@click.option(
    "--resolve-review-metadata/--skip-review-metadata",
    default=True,
    show_default=True,
    help="Fetch richer metadata only for shortlisted rows",
)
def cli(
    enriched_results: str,
    output: str,
    summary_json: str,
    top_n: int,
    preferred_buckets: str,
    max_per_subject: int,
    match_type_quotas: str,
    resolve_review_metadata: bool,
) -> None:
    """Build a human-review shortlist from enriched alignment rows."""
    rows = read_alignment_rows(enriched_results)
    shortlist = shortlist_alignment_rows(
        rows,
        top_n=top_n,
        preferred_buckets=tuple(item.strip() for item in preferred_buckets.split(",") if item.strip()),
        max_per_subject=max_per_subject,
        match_type_quotas=parse_quota_option(match_type_quotas),
    )
    review_rows = enrich_review_rows(shortlist, resolve_ols_metadata=resolve_review_metadata)

    Path(output).parent.mkdir(parents=True, exist_ok=True)
    Path(summary_json).parent.mkdir(parents=True, exist_ok=True)
    write_tsv(review_rows, output)
    write_json(summarize_review_rows(review_rows), summary_json)

    click.echo(f"Shortlisted rows: {len(review_rows)}")
    click.echo(f"Wrote review TSV: {output}")
    click.echo(f"Wrote review summary JSON: {summary_json}")


if __name__ == "__main__":
    cli()
