from nmdc_schema.ontology_alignment_prototype import (
    OlsEntityMetadata,
    SchemaElementRecord,
    classify_alignment,
    enrich_review_rows,
    lexical_profile,
    match_type,
    normalize_text,
    shortlist_alignment_rows,
    structural_support,
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


def test_enrich_review_rows_without_metadata_leaves_rows_unchanged():
    rows = [{"subject_id": "nmdc:a", "object_id": "OBI:1", "object_source": "OBI"}]
    enriched = enrich_review_rows(rows, resolve_ols_metadata=False)
    assert enriched == rows
