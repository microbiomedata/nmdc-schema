from nmdc_schema.ontology_alignment_prototype import (
    SchemaElementRecord,
    MetadataResolution,
    OlsEntityMetadata,
    classify_alignment,
    compose_ontology_term_search_text,
    compose_subject_query_text,
    enrich_review_rows,
    harvest_oaklib_ontology_terms,
    lexical_profile,
    linkml_store_available,
    match_type,
    normalize_text,
    oaklib_available,
    OntologyTermRecord,
    parse_quota_option,
    read_unique_subjects,
    resolve_entity_metadata,
    review_flags,
    shortlist_alignment_rows,
    structural_support,
    SubjectQueryRecord,
    summarize_property_like_gap,
    summarize_review_rows,
    summarize_source_distribution,
    summarize_backend_overlap,
)


def test_normalize_text_splits_camel_case_and_underscores():
    assert normalize_text("LibraryPreparation_Kit") == "library preparation kit"


def test_lexical_profile_detects_strong_lexical_match():
    profile = lexical_profile("ProcessedSample", "processed specimen")
    assert profile.lexical_score >= 0.45
    assert profile.containment > 0


def test_lexical_profile_detects_weak_lexical_match():
    profile = lexical_profile("FunctionalAnnotation", "employment status")
    assert profile.lexical_score < 0.45


def test_classify_alignment_flags_semantic_only_hits():
    classification = classify_alignment(
        semantic_confidence=0.93,
        lexical_score_value=0.21,
        semantic_threshold=0.90,
        lexical_threshold=0.45,
    )
    assert classification == "strong_semantic_weak_lexical"


def test_match_type_slot_to_class():
    assert match_type("slot", "class") == "slot->class"


def test_structural_support_for_scalar_slot_to_class_is_false():
    record = SchemaElementRecord(
        subject_id="nmdc:test_slot",
        subject_label="test_slot",
        subject_category="slot",
        subject_description="",
        element_name="test_slot",
        range_name="string",
        range_kind="scalar",
        owners=("Study",),
        owner_mapping_sources=tuple(),
        range_mapping_sources=tuple(),
        existing_mappings=tuple(),
        existing_mapping_sources=tuple(),
        expected_alignment_type="property_like",
    )
    metadata = OlsEntityMetadata(
        object_id="OBI:0000066",
        object_source="OBI",
        object_kind="class",
        iri="http://purl.obolibrary.org/obo/OBI_0000066",
        description="investigation",
    )
    supported, reason = structural_support(record, metadata)
    assert supported is False
    assert reason == "slot_class_scalar_mismatch"


def test_structural_support_for_enum_backed_slot_to_class_is_true():
    record = SchemaElementRecord(
        subject_id="nmdc:test_slot",
        subject_label="test_slot",
        subject_category="slot",
        subject_description="",
        element_name="test_slot",
        range_name="InstrumentModelEnum",
        range_kind="enum",
        owners=("DataGeneration",),
        owner_mapping_sources=("OBI",),
        range_mapping_sources=tuple(),
        existing_mappings=tuple(),
        existing_mapping_sources=tuple(),
        expected_alignment_type="class_filler",
    )
    metadata = OlsEntityMetadata(
        object_id="OBI:0002630",
        object_source="OBI",
        object_kind="class",
        iri="http://purl.obolibrary.org/obo/OBI_0002630",
        description="instrument model term",
    )
    supported, reason = structural_support(record, metadata)
    assert supported is True
    assert reason == "slot_class_range_fit"


def test_structural_support_for_pv_without_source_overlap_is_false():
    record = SchemaElementRecord(
        subject_id="nmdc:test_enum.value",
        subject_label="value",
        subject_category="permissible_value",
        subject_description="",
        element_name="value",
        range_name="",
        range_kind="none",
        owners=("TestEnum",),
        owner_mapping_sources=tuple(),
        range_mapping_sources=tuple(),
        existing_mappings=tuple(),
        existing_mapping_sources=tuple(),
        expected_alignment_type="class_like",
    )
    metadata = OlsEntityMetadata(
        object_id="OBI:0000366",
        object_source="OBI",
        object_kind="class",
        iri="http://purl.obolibrary.org/obo/OBI_0000366",
        description="metabolite profiling assay",
    )
    supported, reason = structural_support(record, metadata)
    assert supported is False
    assert reason == "pv_source_mismatch"


def test_shortlist_prefers_structurally_supported_rows():
    rows = [
        {
            "subject_id": "nmdc:a",
            "object_id": "X:1",
            "structural_bucket": "strong_semantic_strong_lexical",
            "semantic_confidence": 0.99,
            "lexical_score": 0.90,
        },
        {
            "subject_id": "nmdc:b",
            "object_id": "X:2",
            "structural_bucket": "strong_semantic_weak_lexical_structurally_supported",
            "semantic_confidence": 0.91,
            "lexical_score": 0.10,
        },
    ]
    shortlisted = shortlist_alignment_rows(rows, top_n=1)
    assert shortlisted[0]["subject_id"] == "nmdc:b"


def test_shortlist_respects_match_type_quotas():
    rows = [
        {
            "subject_id": "nmdc:a",
            "object_id": "X:1",
            "match_type": "pv->class",
            "structural_bucket": "strong_semantic_strong_lexical",
            "semantic_confidence": 0.99,
            "lexical_score": 0.90,
        },
        {
            "subject_id": "nmdc:b",
            "object_id": "X:2",
            "match_type": "pv->class",
            "structural_bucket": "strong_semantic_strong_lexical",
            "semantic_confidence": 0.98,
            "lexical_score": 0.85,
        },
        {
            "subject_id": "nmdc:c",
            "object_id": "X:3",
            "match_type": "slot->class",
            "structural_bucket": "strong_semantic_strong_lexical",
            "semantic_confidence": 0.90,
            "lexical_score": 0.60,
        },
    ]
    shortlisted = shortlist_alignment_rows(rows, top_n=3, match_type_quotas={"pv->class": 1})
    assert len(shortlisted) == 2
    assert sum(1 for row in shortlisted if row["match_type"] == "pv->class") == 1
    assert sum(1 for row in shortlisted if row["match_type"] == "slot->class") == 1


def test_enrich_review_rows_without_metadata_leaves_rows_unchanged():
    rows = [{"subject_id": "nmdc:a", "object_id": "OBI:1", "object_source": "OBI"}]
    enriched = enrich_review_rows(rows, metadata_backend="none")
    assert enriched == rows


def test_review_flags_capture_semantic_rescue_and_slot_shape():
    row = {
        "structural_bucket": "strong_semantic_weak_lexical_structurally_supported",
        "match_type": "slot->class",
        "schema_expected_alignment_type": "property_like",
        "lexical_score": 0.1,
        "object_description": "definition",
        "object_synonyms": "alias one|alias two",
        "object_is_obsolete": False,
    }
    flags = review_flags(row)
    assert "semantic_rescue" in flags
    assert "slot_to_class" in flags
    assert "property_like_slot" in flags
    assert "very_weak_lexical" in flags
    assert "has_definition" in flags
    assert "has_synonyms" in flags


def test_summarize_review_rows_counts_flags():
    rows = [
        {
            "structural_bucket": "strong_semantic_weak_lexical_structurally_supported",
            "object_source": "OBI",
            "match_type": "slot->class",
            "review_flags": "semantic_rescue|slot_to_class",
        },
        {
            "structural_bucket": "strong_semantic_strong_lexical",
            "object_source": "MI",
            "match_type": "class->class",
            "review_flags": "has_definition",
        },
    ]
    summary = summarize_review_rows(rows)
    assert summary["total_rows"] == 2
    assert summary["by_review_flag"]["semantic_rescue"] == 1
    assert summary["by_object_source"]["OBI"] == 1


def test_parse_quota_option():
    assert parse_quota_option("slot->class=10,pv->class=15") == {
        "slot->class": 10,
        "pv->class": 15,
    }


def test_oaklib_available_returns_boolean():
    assert isinstance(oaklib_available(), bool)


def test_linkml_store_available_returns_boolean():
    assert isinstance(linkml_store_available(), bool)


def test_resolve_entity_metadata_uses_requested_backend_when_available():
    resolution = resolve_entity_metadata("OBI:0000366", "OBI", backend="oaklib")
    assert isinstance(resolution, MetadataResolution)
    assert resolution.requested_backend == "oaklib"
    if oaklib_available():
        assert resolution.resolved_backend == "oaklib"
    else:
        assert resolution.resolved_backend == "ols4_fallback"


def test_summarize_review_rows_counts_metadata_backend():
    rows = [
        {
            "structural_bucket": "strong_semantic_weak_lexical_structurally_supported",
            "object_source": "OBI",
            "match_type": "slot->class",
            "metadata_backend_resolved": "ols4",
            "review_flags": "semantic_rescue",
        }
    ]
    summary = summarize_review_rows(rows)
    assert summary["by_metadata_backend"]["ols4"] == 1


def test_compose_subject_query_text_includes_label_description_and_category():
    subject = SubjectQueryRecord(
        subject_id="nmdc:instrument_used",
        subject_label="instrument used",
        subject_category="slot",
        subject_description="The instrument used in data generation",
    )
    query_text = compose_subject_query_text(subject)
    assert "instrument used" in query_text
    assert "data generation" in query_text
    assert "schema element type: slot" in query_text


def test_compose_ontology_term_search_text_includes_synonyms_and_definition():
    text = compose_ontology_term_search_text(
        OntologyTermRecord(
            object_id="OBI:0000366",
            object_label="metabolite profiling assay",
            object_source="OBI",
            object_kind="class",
            object_description="An assay for metabolites",
            object_synonyms=("metabolite profiling assay",),
        )
    )
    assert "metabolite" in text.lower()


def test_read_unique_subjects_preserves_first_seen_order(tmp_path):
    path = tmp_path / "alignment.tsv"
    path.write_text(
        "\t".join(
            [
                "subject_id",
                "subject_label",
                "subject_category",
                "subject_description",
                "object_id",
                "object_label",
                "object_source",
                "predicate_id",
                "mapping_justification",
                "confidence",
                "comment",
            ]
        )
        + "\n"
        + "\n".join(
            [
                "\t".join(["nmdc:A", "Alpha", "class", "first", "OBI:1", "One", "OBI", "skos:closeMatch", "x", "0.9", ""]),
                "\t".join(["nmdc:A", "Alpha", "class", "first", "OBI:2", "Two", "OBI", "skos:closeMatch", "x", "0.8", ""]),
                "\t".join(["nmdc:B", "Beta", "slot", "second", "OBI:3", "Three", "OBI", "skos:closeMatch", "x", "0.7", ""]),
            ]
        )
        + "\n"
    )
    subjects = read_unique_subjects(path)
    assert [subject.subject_id for subject in subjects] == ["nmdc:A", "nmdc:B"]


def test_summarize_backend_overlap_counts_top1_and_topk_matches():
    reference_rows = [
        {"subject_id": "nmdc:A", "object_id": "OBI:1", "object_source": "OBI", "confidence": 0.95},
        {"subject_id": "nmdc:A", "object_id": "OBI:2", "object_source": "OBI", "confidence": 0.91},
        {"subject_id": "nmdc:B", "object_id": "OBI:3", "object_source": "OBI", "confidence": 0.96},
    ]
    candidate_rows = [
        {"subject_id": "nmdc:A", "object_id": "OBI:1", "object_source": "OBI", "confidence": 0.93},
        {"subject_id": "nmdc:A", "object_id": "OBI:7", "object_source": "OBI", "confidence": 0.90},
        {"subject_id": "nmdc:B", "object_id": "OBI:8", "object_source": "OBI", "confidence": 0.94},
    ]
    summary = summarize_backend_overlap(reference_rows, candidate_rows, object_source="OBI", top_k=2)
    assert summary["subjects_compared"] == 2
    assert summary["subjects_with_any_top_k_overlap"] == 1
    assert summary["subjects_with_top1_overlap"] == 1


def test_summarize_source_distribution_counts_rows_and_subjects():
    rows = [
        {"subject_id": "nmdc:A", "object_source": "OBI"},
        {"subject_id": "nmdc:B", "object_source": "OBI"},
        {"subject_id": "nmdc:A", "object_source": "OBI"},
        {"subject_id": "nmdc:C", "object_source": "ENVO"},
    ]
    summary = summarize_source_distribution(rows, top_n=2)
    assert summary["distinct_sources"] == 2
    assert summary["top_sources"][0]["object_source"] == "OBI"
    assert summary["top_sources"][0]["row_count"] == 3
    assert summary["top_sources"][0]["subject_count"] == 2


def test_summarize_property_like_gap_counts_property_like_slot_hits():
    schema_index = {
        "nmdc:slot_a": SchemaElementRecord(
            subject_id="nmdc:slot_a",
            subject_label="slot_a",
            subject_category="slot",
            subject_description="",
            element_name="slot_a",
            range_name="string",
            range_kind="scalar",
            owners=("Study",),
            owner_mapping_sources=tuple(),
            range_mapping_sources=tuple(),
            existing_mappings=tuple(),
            existing_mapping_sources=tuple(),
            expected_alignment_type="property_like",
        ),
        "nmdc:slot_b": SchemaElementRecord(
            subject_id="nmdc:slot_b",
            subject_label="slot_b",
            subject_category="slot",
            subject_description="",
            element_name="slot_b",
            range_name="InstrumentEnum",
            range_kind="enum",
            owners=("Study",),
            owner_mapping_sources=tuple(),
            range_mapping_sources=tuple(),
            existing_mappings=tuple(),
            existing_mapping_sources=tuple(),
            expected_alignment_type="class_filler",
        ),
    }
    baseline_rows = [
        {"subject_id": "nmdc:slot_a", "subject_category": "slot", "object_source": "OBI"},
        {"subject_id": "nmdc:slot_b", "subject_category": "slot", "object_source": "OBI"},
    ]
    summary = summarize_property_like_gap(schema_index, baseline_rows, ontology_prefix="OBI")
    assert summary["property_like_slot_subjects"] == 1
    assert summary["class_filler_slot_subjects"] == 1
    assert summary["property_like_slots_with_retrieval_hits"] == 1
    assert summary["class_filler_slots_with_retrieval_hits"] == 1
