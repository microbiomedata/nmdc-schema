from nmdc_schema.ontology_registry_counts import summarize_registry_differences


def test_summarize_registry_differences_distinguishes_ols_overall_and_embeddings():
    summary = summarize_registry_differences(
        ols_overall={"count": 4, "prefixes": ["A", "B", "C", "D"]},
        ols_embeddings_corpus={"count": 2, "prefixes": ["A", "B"]},
        obo_foundry_registry={"count": 3, "prefixes": ["A", "C", "X"]},
        bioportal_registry={"count": 10, "prefixes": ["A", "Q"]},
        semsql_registry={"count": 5, "prefixes": ["A", "S"]},
    )
    assert summary["ols_overall_count"] == 4
    assert summary["ols_embeddings_corpus_count"] == 2
    assert summary["ols_overall_not_in_embeddings"] == ["C", "D"]
    assert summary["ols_embeddings_not_in_ols_overall"] == []
    assert summary["obo_missing_from_ols_embeddings"] == ["C", "X"]
    assert summary["bioportal_count"] == 10
    assert summary["semantic_sql_count"] == 5
