"""The Runtime minter calls get_typecode_for_future_ids on an induced id pattern."""

import pytest
from linkml_runtime import SchemaView

from nmdc_schema.get_nmdc_view import ViewGetter
from nmdc_schema.id_helpers import get_typecode_for_future_ids


@pytest.fixture(scope="module")
def nmdc_view() -> SchemaView:
    return ViewGetter().get_view()


def test_named_thing_classes_have_a_future_typecode(nmdc_view: SchemaView) -> None:
    """Every concrete NamedThing descendant has a typecode for newly minted ids.

    OntologyClass and its descendants, and any class that declares id_prefixes,
    are identified by external ids rather than an NMDC typecode.
    """
    external_identifier_classes = set(nmdc_view.class_descendants("OntologyClass"))
    missing: list[str] = []
    checked = 0
    for class_name in nmdc_view.class_descendants("NamedThing"):
        class_definition = nmdc_view.get_class(class_name)
        if class_definition is None or class_definition.abstract:
            continue
        if class_name in external_identifier_classes or class_definition.id_prefixes:
            continue
        induced = nmdc_view.induced_slot("id", class_name).pattern
        assert isinstance(induced, str)
        checked += 1
        if get_typecode_for_future_ids(induced) is None:
            missing.append(str(class_name))
    assert checked > 0
    assert missing == [], (
        f"get_typecode_for_future_ids returned None for: {sorted(missing)}"
    )
