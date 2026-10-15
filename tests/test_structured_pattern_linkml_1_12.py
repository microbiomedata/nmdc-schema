"""Check the schema against how linkml-runtime 1.12 resolves structured patterns.

linkml-runtime 1.12 (https://github.com/linkml/linkml/pull/3832) changed four things, and the
repo still locks 1.11, so these tests compute the 1.12 result themselves instead of relying on
whichever runtime is installed:

1. A structured_pattern is interpolated with the settings of its own module only
   (https://github.com/linkml/linkml/issues/4135). Covered in test_module_settings.py.
2. Unless partial_match is true, the resolved pattern is wrapped as ^(?:...)$, so a value must
   match the whole pattern (https://github.com/linkml/linkml/issues/4134).
3. induced_slot rebuilds pattern from structured_pattern and ignores an asserted pattern.
4. A placeholder in a structured_pattern without interpolated: true is escaped and kept as
   literal text. Covered in test_structured_patterns_interpolated.py.
"""

import re
from pathlib import Path

import pytest
import yaml
from linkml_runtime import SchemaView
from linkml_runtime.linkml_model.meta import SchemaDefinition, Setting, SlotDefinition
from linkml_runtime.utils.pattern import PatternResolver

from nmdc_schema.get_nmdc_view import ViewGetter
from nmdc_schema.id_helpers import get_compatible_typecodes

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_DIR = ROOT / "src" / "schema"
VALID_DATA_DIR = ROOT / "src" / "data" / "valid"
PLACEHOLDER = re.compile(r"\{[A-Za-z_][A-Za-z0-9_]*\}")


def _load(path: Path) -> object:
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def _walk(node: object, path: str = ""):
    """Yield (path, dict) for every mapping in node."""
    if isinstance(node, dict):
        yield path, node
        for key, value in node.items():
            yield from _walk(value, f"{path}/{key}")
    elif isinstance(node, list):
        for index, value in enumerate(node):
            yield from _walk(value, f"{path}[{index}]")


@pytest.fixture(scope="module")
def source_view() -> SchemaView:
    return SchemaView(str(SCHEMA_DIR / "nmdc.yaml"))


@pytest.fixture(scope="module")
def resolvers(source_view: SchemaView) -> dict[str, PatternResolver]:
    """One resolver per module, each seeing only that module's settings, as linkml 1.12 does."""
    return {
        str(schema.id): PatternResolver(SchemaView(schema))
        for schema in source_view.all_schema()
    }


def _apply_1_12_rules(
    definition: SlotDefinition, schema_id: str, resolvers: dict[str, PatternResolver]
) -> str | None:
    """Resolve one asserted definition the way linkml-runtime 1.12's SchemaView.resolve_pattern does (v1.12.1)."""
    structured_pattern = definition.structured_pattern
    if structured_pattern is None:
        return definition.pattern
    pattern = structured_pattern.syntax
    if structured_pattern.interpolated:
        pattern = resolvers[schema_id].resolve(pattern)
    if not structured_pattern.partial_match:
        pattern = f"^(?:{pattern})$"
    return pattern


def resolve_like_linkml_1_12(
    view: SchemaView,
    slot_name: str,
    class_name: str,
    resolvers: dict[str, PatternResolver],
) -> str | None:
    """Return the pattern linkml-runtime 1.12 would give the induced slot, without needing 1.12 installed.

    The rule that matters here: a pattern is resolved with the settings of the module that asserted
    it, so a slot_usage or attribute uses its class's module and a slot definition uses its own.
    The nearest assertion wins: the class and then its ancestors (slot_usage or attributes), then the
    slot and its ancestors. test_emulation_agrees_with_installed_runtime checks this against the
    real induced_slot whenever linkml-runtime 1.12 or later is installed.
    """
    for ancestor in view.class_ancestors(class_name, reflexive=True, mixins=True):
        owning_class = view.get_class(ancestor)
        for asserted in (
            owning_class.slot_usage.get(slot_name),
            owning_class.attributes.get(slot_name),
        ):
            if asserted is not None and (
                asserted.structured_pattern is not None or asserted.pattern
            ):
                return _apply_1_12_rules(
                    asserted, str(owning_class.from_schema), resolvers
                )
    for ancestor in view.slot_ancestors(slot_name, reflexive=True):
        slot = view.get_slot(ancestor, attributes=False)
        if slot is not None and (slot.structured_pattern is not None or slot.pattern):
            return _apply_1_12_rules(slot, str(slot.from_schema), resolvers)
    return None


def test_no_slot_asserts_both_pattern_and_structured_pattern() -> None:
    """1.12's induced_slot replaces an asserted pattern with the resolved structured_pattern."""
    both = [
        f"{module.name}{path}"
        for module in sorted(SCHEMA_DIR.glob("*.yaml"))
        for path, node in _walk(_load(module))
        if "pattern" in node and isinstance(node.get("structured_pattern"), dict)
    ]
    assert not both, (
        "pattern and structured_pattern on the same element:\n" + "\n".join(both)
    )


def test_partial_match_is_only_ever_true() -> None:
    """partial_match: false is the default; spelling it out hides which patterns are deliberately partial."""
    values = {
        node["structured_pattern"]["partial_match"]
        for module in SCHEMA_DIR.glob("*.yaml")
        for _, node in _walk(_load(module))
        if isinstance(node.get("structured_pattern"), dict)
        and "partial_match" in node["structured_pattern"]
    }
    assert values <= {True}


def test_resolver_matches_the_documented_1_12_behavior() -> None:
    """Pin the emulation itself, so a mistake in it cannot make every check below pass."""
    schema = SchemaDefinition(
        id="m", name="m", settings={"p": Setting(setting_key="p", setting_value="nmdc")}
    )
    resolvers = {"m": PatternResolver(SchemaView(schema))}
    full = SlotDefinition(
        "s", structured_pattern={"syntax": "^{p}:x$", "interpolated": True}
    )
    partial = SlotDefinition(
        "s",
        structured_pattern={
            "syntax": "{p}",
            "interpolated": True,
            "partial_match": True,
        },
    )
    asserted = SlotDefinition("s", pattern="^a$")
    assert _apply_1_12_rules(full, "m", resolvers) == "^(?:^nmdc:x$)$"
    assert _apply_1_12_rules(partial, "m", resolvers) == "nmdc"
    assert _apply_1_12_rules(asserted, "m", resolvers) == "^a$"


def _string_patterns_by_class(
    view: SchemaView, resolvers: dict[str, PatternResolver]
) -> dict[str, dict[str, re.Pattern]]:
    """For each class, the 1.12 pattern of every slot whose range is a type (patterns on class ranges are ignored)."""
    type_names = set(view.all_types())
    result: dict[str, dict[str, re.Pattern]] = {}
    for class_name in view.all_classes():
        for slot_name in view.class_slots(class_name):
            if view.induced_slot(slot_name, class_name).range not in type_names:
                continue
            pattern = resolve_like_linkml_1_12(view, slot_name, class_name, resolvers)
            if pattern:
                result.setdefault(class_name, {})[slot_name] = re.compile(pattern)
    return result


def test_no_resolved_pattern_keeps_a_placeholder(
    source_view: SchemaView, resolvers: dict[str, PatternResolver]
) -> None:
    leftovers = sorted(
        f"{class_name}.{slot_name}: {pattern.pattern}"
        for class_name, slots in _string_patterns_by_class(
            source_view, resolvers
        ).items()
        for slot_name, pattern in slots.items()
        if PLACEHOLDER.search(pattern.pattern)
    )
    assert not leftovers, (
        f"{len(leftovers)} patterns keep placeholders under linkml 1.12, e.g. {leftovers[:5]}"
    )


def test_every_class_id_pattern_resolves(
    source_view: SchemaView, resolvers: dict[str, PatternResolver]
) -> None:
    """Report per class; the source schema has 57 classes with an id slot."""
    unresolved = sorted(
        class_name
        for class_name, slots in _string_patterns_by_class(
            source_view, resolvers
        ).items()
        if "id" in slots and PLACEHOLDER.search(slots["id"].pattern)
    )
    assert not unresolved, (
        f"id pattern keeps placeholders under linkml 1.12 for {unresolved}"
    )


def test_valid_examples_match_the_anchored_1_12_patterns(
    source_view: SchemaView, resolvers: dict[str, PatternResolver]
) -> None:
    """Valid example data must still match once patterns are anchored at both ends."""
    patterns = _string_patterns_by_class(source_view, resolvers)
    checked = 0
    failures = []
    for data_file in sorted(VALID_DATA_DIR.glob("*.yaml")):
        for path, node in _walk(_load(data_file)):
            class_name = str(node.get("type", "")).removeprefix("nmdc:")
            for slot_name, pattern in patterns.get(class_name, {}).items():
                values = node.get(slot_name)
                for value in values if isinstance(values, list) else [values]:
                    if not isinstance(value, str):
                        continue
                    checked += 1
                    if not pattern.search(value):
                        failures.append(
                            f"{data_file.name}{path}.{slot_name} = {value!r} !~ {pattern.pattern}"
                        )
    assert checked > 500, f"only {checked} values checked; is the type lookup broken?"
    assert not failures, (
        f"{len(failures)} valid values fail under linkml 1.12:\n"
        + "\n".join(failures[:20])
    )


@pytest.fixture(scope="module")
def materialized_view() -> SchemaView:
    return ViewGetter().get_view()


def test_typecodes_are_the_same_for_wrapped_and_unwrapped_id_patterns(
    materialized_view: SchemaView,
) -> None:
    """id_helpers must read every class's id pattern the same way before and after 1.12's wrapping."""
    checked = 0
    for class_name in materialized_view.all_classes():
        if "id" not in materialized_view.class_slots(class_name):
            continue
        pattern = materialized_view.induced_slot("id", class_name).pattern
        if not pattern:
            continue
        if pattern.startswith("^(?:") and pattern.endswith(")$"):
            pattern = pattern[len("^(?:") : -len(")$")]
        # From 11.25.0 our own patterns carry no anchors, so the inner pattern may not start
        # with ^ (https://github.com/microbiomedata/nmdc-schema/issues/3539). Compare the
        # wrapped form with the plain anchored form 11.24.x shipped.
        anchored = pattern if pattern.startswith("^") else f"^{pattern}"
        unwrapped = get_compatible_typecodes(anchored)
        if not unwrapped:
            continue
        checked += 1
        assert get_compatible_typecodes(f"^(?:{pattern})$") == unwrapped, class_name
    assert checked > 30


def test_materialized_artifact_patterns_have_no_placeholders() -> None:
    materialized = _load(ROOT / "nmdc_schema" / "nmdc_materialized_patterns.yaml")
    leftovers = [
        path
        for path, node in _walk(materialized)
        if isinstance(node.get("pattern"), str) and PLACEHOLDER.search(node["pattern"])
    ]
    assert not leftovers, leftovers[:10]


def test_emulation_agrees_with_installed_runtime(
    source_view: SchemaView, resolvers: dict[str, PatternResolver]
) -> None:
    """With linkml-runtime 1.12 or later installed, the emulation must equal the real induced pattern."""
    if not hasattr(SchemaView, "resolve_pattern"):
        pytest.skip(
            "installed linkml-runtime predates 1.12; nothing to compare against"
        )
    disagreements = []
    for class_name in source_view.all_classes():
        for slot_name in source_view.class_slots(class_name):
            expected = source_view.induced_slot(slot_name, class_name).pattern
            emulated = resolve_like_linkml_1_12(
                source_view, slot_name, class_name, resolvers
            )
            if emulated != expected:
                disagreements.append(
                    f"{class_name}.{slot_name}: emulated {emulated!r}, runtime {expected!r}"
                )
    assert not disagreements, f"{len(disagreements)} disagreements:\n" + "\n".join(
        disagreements[:20]
    )
