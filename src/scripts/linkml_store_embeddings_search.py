"""Run a LinkML-side semantic retrieval experiment with oaklib + linkml-store."""

from __future__ import annotations

from pathlib import Path

import click

from nmdc_schema.ontology_alignment_prototype import (
    available_tooling,
    build_schema_index,
    enrich_alignment_rows,
    harvest_bioportal_ontology_terms,
    parse_csv_option,
    read_alignment_rows,
    read_unique_subjects,
    run_linkml_store_semantic_search,
    summarize_alignment_rows,
    summarize_backend_overlap,
    write_json,
    write_tsv,
    harvest_oaklib_ontology_terms,
)


@click.command()
@click.option(
    "--ols4-results",
    default="/tmp/ols4_embeddings_results.tsv",
    show_default=True,
    help="Baseline OLS4 embeddings TSV used to derive the NMDC query set and compare overlap",
)
@click.option(
    "--corpus-source",
    type=click.Choice(["oaklib", "bioportal"], case_sensitive=False),
    default="oaklib",
    show_default=True,
    help="Source used to harvest the ontology corpus before local linkml-store indexing",
)
@click.option(
    "--ontology-prefix",
    default="OBI",
    show_default=True,
    help="Ontology prefix used for oaklib harvests and overlap summaries",
)
@click.option(
    "--adapter-handle",
    default="sqlite:obo:obi",
    show_default=True,
    help="oaklib adapter handle for the local ontology source",
)
@click.option(
    "--bioportal-acronyms",
    default="",
    help="Optional comma-separated BioPortal ontology acronyms to harvest directly from BioPortal",
)
@click.option(
    "--bioportal-page-size",
    default=250,
    show_default=True,
    help="Page size used when harvesting classes from BioPortal",
)
@click.option(
    "--bioportal-include-views/--bioportal-skip-views",
    default=False,
    show_default=True,
    help="Whether to include ontology views when harvesting from BioPortal",
)
@click.option(
    "--bioportal-include-imports/--bioportal-exclude-imports",
    default=False,
    show_default=True,
    help="Whether to keep imported classes from other ontologies when harvesting from BioPortal",
)
@click.option(
    "--subject-categories",
    default="",
    help="Optional comma-separated subject categories to keep from the baseline query set",
)
@click.option(
    "--restrict-to-baseline-source-hits/--all-baseline-subjects",
    default=True,
    show_default=True,
    help="When enabled, only query NMDC subjects that had baseline OLS4 hits in the target ontology",
)
@click.option("--max-subjects", type=int, default=None, help="Optional maximum number of baseline subjects to query")
@click.option("--max-ontology-terms", type=int, default=None, help="Optional maximum number of local ontology terms to index")
@click.option("--top-k", default=20, show_default=True, help="Number of semantic hits to keep per NMDC subject")
@click.option(
    "--corpus-batch-size",
    default=250,
    show_default=True,
    help="Number of ontology terms to embed per linkml-store batch when building the local index",
)
@click.option(
    "--embedding-model-name",
    default="text-embedding-3-small",
    show_default=True,
    help="Embedding model name passed through linkml-store's LLMIndexer",
)
@click.option(
    "--cache-db",
    default="local/linkml-store-embeddings.db",
    show_default=True,
    help="DuckDB/SQLite cache used by linkml-store's LLM indexer",
)
@click.option(
    "--cache-collection",
    default="",
    help="Optional cache collection name; defaults to a name derived from ontology prefix and model",
)
@click.option(
    "--output",
    "-o",
    default="local/linkml_store_embeddings_obi.tsv",
    show_default=True,
    help="Output TSV path for LinkML-side semantic retrieval results",
)
@click.option(
    "--summary-json",
    default="local/linkml_store_embeddings_obi_summary.json",
    show_default=True,
    help="Summary JSON path",
)
@click.option(
    "--schema-path",
    default="nmdc_schema/nmdc_materialized_patterns.yaml",
    show_default=True,
    help="Schema path used for structural enrichment of LinkML-side retrieval results",
)
@click.option(
    "--semantic-threshold",
    default=0.90,
    show_default=True,
    help="Semantic threshold used for semantic-vs-lexical classification",
)
@click.option(
    "--lexical-threshold",
    default=0.45,
    show_default=True,
    help="Lexical threshold used for semantic-vs-lexical classification",
)
@click.option(
    "--enriched-output",
    default="",
    help="Optional TSV path for structurally enriched retrieval rows",
)
@click.option(
    "--enriched-summary-json",
    default="",
    help="Optional JSON path for the enriched retrieval summary",
)
def cli(
    ols4_results: str,
    corpus_source: str,
    ontology_prefix: str,
    adapter_handle: str,
    bioportal_acronyms: str,
    bioportal_page_size: int,
    bioportal_include_views: bool,
    bioportal_include_imports: bool,
    subject_categories: str,
    restrict_to_baseline_source_hits: bool,
    max_subjects: int | None,
    max_ontology_terms: int | None,
    top_k: int,
    corpus_batch_size: int,
    embedding_model_name: str,
    cache_db: str,
    cache_collection: str,
    output: str,
    summary_json: str,
    schema_path: str,
    semantic_threshold: float,
    lexical_threshold: float,
    enriched_output: str,
    enriched_summary_json: str,
) -> None:
    """Compare a local LinkML-side semantic retrieval run against the OLS4 baseline query set."""
    allowed_subject_categories = {item.lower() for item in parse_csv_option(subject_categories)}
    baseline_rows = read_alignment_rows(ols4_results)
    schema_index = build_schema_index(schema_path)
    ontology_prefixes = (
        [prefix.strip().upper() for prefix in bioportal_acronyms.split(",") if prefix.strip()]
        if bioportal_acronyms
        else [ontology_prefix.upper()]
    )
    if corpus_source.lower() == "oaklib":
        ontology_prefixes = [ontology_prefix.upper()]
    subjects = read_unique_subjects(
        ols4_results,
        allowed_subject_categories=allowed_subject_categories,
        schema_index=schema_index,
    )
    if restrict_to_baseline_source_hits:
        eligible_subject_ids = {
            row.get("subject_id", "")
            for row in baseline_rows
            if (row.get("object_source") or "").upper() in set(ontology_prefixes)
        }
        subjects = [subject for subject in subjects if subject.subject_id in eligible_subject_ids]
    if max_subjects is not None:
        subjects = subjects[:max_subjects]
    if corpus_source.lower() == "bioportal":
        ontology_terms = harvest_bioportal_ontology_terms(
            ontology_acronyms=ontology_prefixes,
            max_terms=max_ontology_terms,
            page_size=bioportal_page_size,
            include_views=bioportal_include_views,
            include_imported_terms=bioportal_include_imports,
        )
    else:
        ontology_terms = harvest_oaklib_ontology_terms(
            adapter_handle=adapter_handle,
            ontology_prefix=ontology_prefix,
            max_terms=max_ontology_terms,
        )
    derived_cache_collection = cache_collection or f"{'_'.join(prefix.lower() for prefix in ontology_prefixes)}_{embedding_model_name.replace('-', '_')}"
    rows = run_linkml_store_semantic_search(
        subjects=subjects,
        ontology_terms=ontology_terms,
        top_k=top_k,
        embedding_model_name=embedding_model_name,
        cache_db_path=cache_db,
        cache_collection_name=derived_cache_collection,
        corpus_batch_size=corpus_batch_size,
    )

    Path(output).parent.mkdir(parents=True, exist_ok=True)
    Path(summary_json).parent.mkdir(parents=True, exist_ok=True)
    write_tsv(rows, output)

    summary = {
        "retrieval_backend": "linkml_store_llm",
        "corpus_source": corpus_source.lower(),
        "embedding_model_name": embedding_model_name,
        "ontology_prefixes": ontology_prefixes,
        "adapter_handle": adapter_handle,
        "restrict_to_baseline_source_hits": restrict_to_baseline_source_hits,
        "subjects_queried": len(subjects),
        "ontology_terms_indexed": len(ontology_terms),
        "top_k": top_k,
        "corpus_batch_size": corpus_batch_size,
        "rows_written": len(rows),
        "tooling_available": available_tooling(),
        "overlap_vs_ols4_by_source": {
            source: summarize_backend_overlap(
                reference_rows=baseline_rows,
                candidate_rows=rows,
                object_source=source,
                top_k=top_k,
            )
            for source in ontology_prefixes
        },
    }
    write_json(summary, summary_json)

    if enriched_output or enriched_summary_json:
        enriched_rows = enrich_alignment_rows(
            rows=rows,
            schema_index=schema_index,
            semantic_threshold=semantic_threshold,
            lexical_threshold=lexical_threshold,
            resolve_ols_metadata=False,
        )
        if enriched_output:
            write_tsv(enriched_rows, enriched_output)
        if enriched_summary_json:
            write_json(summarize_alignment_rows(enriched_rows), enriched_summary_json)

    click.echo(f"Subjects queried: {len(subjects)}")
    click.echo(f"Ontology terms indexed: {len(ontology_terms)}")
    click.echo(f"Rows written: {len(rows)}")
    click.echo(f"Wrote retrieval TSV: {output}")
    click.echo(f"Wrote summary JSON: {summary_json}")
    if enriched_output:
        click.echo(f"Wrote enriched TSV: {enriched_output}")
    if enriched_summary_json:
        click.echo(f"Wrote enriched summary JSON: {enriched_summary_json}")


if __name__ == "__main__":
    cli()
