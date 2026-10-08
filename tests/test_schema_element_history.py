"""Tests for src/scripts/schema_element_history.py."""

from src.scripts.schema_element_history import (
    combine_current,
    linkml_type_names,
    normalize,
)


def test_combine_current_keeps_imported_linkml_types():
    source = frozenset({("slots", "", "depth")})
    built = frozenset({("slots", "", "depth"), ("types", "", "string")})
    assert combine_current(source, built, frozenset({"string"})) == {
        ("slots", "", "depth"),
        ("types", "", "string"),
    }


def test_combine_current_ignores_removed_custom_type_in_stale_built_file():
    # decimal_degree was removed from the source, but a built file regenerated
    # only at release still has it. It must not count as current.
    source = frozenset({("slots", "", "depth")})
    built = frozenset(
        {
            ("slots", "", "depth"),
            ("types", "", "decimal_degree"),
            ("types", "", "string"),
        }
    )
    current = combine_current(source, built, frozenset({"string"}))
    assert ("types", "", "decimal_degree") not in current
    assert ("types", "", "string") in current


def test_combine_current_ignores_other_built_kinds():
    source = frozenset()
    built = frozenset({("slots", "", "collection_date_inc")})
    assert combine_current(source, built, frozenset({"string"})) == set()


def test_linkml_type_names_are_the_linkml_types():
    names = linkml_type_names()
    assert {"string", "integer", "uriorcurie"} <= names
    assert "decimal_degree" not in names


def test_normalize_matches_case_and_underscore_renames():
    assert normalize("arch_struc_enum") == normalize("ArchStrucEnum")
    assert normalize("decimal degree") == normalize("decimal_degree")
