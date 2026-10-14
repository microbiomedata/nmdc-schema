"""Tests for src/scripts/find_retired_element_mentions.py."""

from src.scripts.find_retired_element_mentions import (
    CHECKED_PATHS,
    build_names,
    is_skipped,
    keep_identifier_like,
    names_in_line,
    phrase_patterns,
)


def row(
    kind: str, name: str, last_tag: str = "v11.0.0", recorded: str = "", enum: str = ""
) -> dict[str, str]:
    return {
        "kind": kind,
        "enum": enum,
        "name": name,
        "last_tag": last_tag,
        "in_deprecated_yaml": recorded,
    }


def test_names_from_both_inputs_keep_the_catalog_release():
    # PersonValue is in deprecated.yaml and in the catalog. The catalog's last
    # release must survive even though deprecated.yaml is read first.
    names = build_names(
        deprecated=[("classes", "", "PersonValue")],
        catalog_rows=[
            row("classes", "PersonValue", "v11.23.0", "yes"),
            row("slots", "omics_type", "v11.0.0"),
        ],
        current=[],
        permissible_values=False,
    )
    assert names["PersonValue"] == {
        "kind": "classes",
        "last_tag": "v11.23.0",
        "in_deprecated_yaml": "yes",
    }
    assert names["omics_type"]["in_deprecated_yaml"] == ""


def test_currently_defined_element_names_are_dropped():
    names = build_names(
        deprecated=[],
        catalog_rows=[row("slots", "samp_collect_device"), row("slots", "omics_type")],
        current=[("slots", "", "samp_collect_device")],
        permissible_values=False,
    )
    assert set(names) == {"omics_type"}


def test_permissible_values_still_in_a_current_enum_are_dropped():
    # `water` was removed from one enum but another current enum still has it.
    names = build_names(
        deprecated=[],
        catalog_rows=[
            row("permissible_values", "water", enum="OldEnum"),
            row("permissible_values", "ReadQcAnalysisActivity", enum="OldEnum"),
        ],
        current=[("permissible_values", "SampleTypeEnum", "water")],
        permissible_values=True,
    )
    assert set(names) == {"ReadQcAnalysisActivity"}


def test_permissible_values_are_left_out_unless_asked_for():
    names = build_names(
        deprecated=[("permissible_values", "OldEnum", "ReadQcAnalysisActivity")],
        catalog_rows=[
            row("permissible_values", "ReadQcAnalysisActivity", enum="OldEnum")
        ],
        current=[],
        permissible_values=False,
    )
    assert names == {}


def test_phrases_match_only_as_whole_words():
    names = {"part of": {}, "Gentegra-DNA": {}, "omics_type": {}}
    phrases = phrase_patterns(names)
    assert names_in_line("counterpart of the sample", names, phrases) == set()
    assert names_in_line("Gentegra-DNAs were used", names, phrases) == set()
    assert names_in_line("is part of a study", names, phrases) == {"part of"}
    assert names_in_line("stored in Gentegra-DNA tubes", names, phrases) == {
        "Gentegra-DNA"
    }
    assert names_in_line("omics_typeX omics_type", names, phrases) == {"omics_type"}


def test_plain_words_are_left_out_by_default():
    names = {
        "soil": {},
        "part of": {},
        "omics_type": {},
        "OmicsProcessing": {},
        "Solution": {},
    }
    assert set(keep_identifier_like(names)) == {
        "omics_type",
        "OmicsProcessing",
        "Solution",
    }


def test_checked_paths_are_skipped_and_neighbors_are_not():
    assert is_skipped("src/schema/core.yaml", CHECKED_PATHS)
    assert is_skipped("nmdc_schema/migrators/partials/x.py", CHECKED_PATHS)
    assert not is_skipped("src/schema_notes.md", CHECKED_PATHS)
    assert not is_skipped(
        "assets/ncbi_mappings/ncbi_attribute_mappings.tsv", CHECKED_PATHS
    )
