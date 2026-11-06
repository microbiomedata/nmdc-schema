"""Our structured patterns leave anchoring to linkml.

From linkml-runtime 1.12, a structured_pattern whose partial_match is not true is wrapped as
^(?:...)$ when it is resolved. A syntax that also carries its own ^ and $ comes out doubled, for
example ^(?:^(nmdc):sty-...$)$. So our syntax values carry no anchors, and linkml adds them.
See https://github.com/microbiomedata/nmdc-schema/issues/3539.

mixs.yaml is generated from MIxS, which anchors its own patterns. The MIxS pipeline strips those
anchors from patterns that linkml wraps (assets/yq-for-mixs-dematerialize.yq), and the checks
below cover mixs.yaml too. See https://github.com/microbiomedata/nmdc-schema/issues/3579.
"""

import re
from importlib.metadata import version
from pathlib import Path

import pytest

import yaml
from linkml_runtime import SchemaView

SCHEMA_DIR = Path(__file__).resolve().parent.parent / "src" / "schema"

# Structured patterns that keep their own anchors, with the reason.
KEEP_ANCHORS = {
    # submission-schema imports this slot and re-resolves its structured pattern with
    # linkml-runtime 1.9.5, which ignores partial_match and adds no anchors. Without its own
    # anchors the slot would accept any text containing a PMID, DOI or URL. Drop it from this
    # list once submission-schema builds with linkml 1.12.
    ("nmdc.yaml", "/slots/salinity_meth"),
}


def _structured_patterns(node: object, path: str = ""):
    """Yield (path, structured_pattern) for every structured_pattern in node."""
    if isinstance(node, dict):
        pattern = node.get("structured_pattern")
        if isinstance(pattern, dict):
            yield path, pattern
        for key, value in node.items():
            yield from _structured_patterns(value, f"{path}/{key}")
    elif isinstance(node, list):
        for index, value in enumerate(node):
            yield from _structured_patterns(value, f"{path}[{index}]")


def _anchored_syntaxes(schema_dir: Path) -> list[tuple[str, str, str]]:
    found = []
    for module in sorted(schema_dir.glob("*.yaml")):
        with module.open(encoding="utf-8") as f:
            document = yaml.safe_load(f)
        for path, pattern in _structured_patterns(document):
            if pattern.get("partial_match") is True:
                continue
            if (module.name, path) in KEEP_ANCHORS:
                continue
            syntax = pattern.get("syntax", "")
            # An anchor at either end, or one on either side of a top-level `|`, is ours to
            # drop: linkml's ^(?:...)$ wrapper already anchors every alternative.
            if (
                syntax.startswith("^")
                or syntax.endswith("$")
                or re.search(r"(?<!\\)\$\||\|\^", syntax)
            ):
                found.append((module.name, path, syntax))
    return found


def test_structured_pattern_syntax_has_no_anchors_of_its_own() -> None:
    anchored = _anchored_syntaxes(SCHEMA_DIR)
    assert not anchored, f"{len(anchored)} structured patterns carry their own ^ or $, e.g. {anchored[:3]}"


def test_settings_used_in_patterns_have_no_anchors() -> None:
    with (SCHEMA_DIR / "nmdc.yaml").open(encoding="utf-8") as f:
        settings = yaml.safe_load(f)["settings"]
    for key in ("id_nmdc_prefix", "id_locus"):
        value = settings[key]
        assert not value.startswith("^") and not value.endswith("$"), f"{key}: {value}"


def test_anchor_check_finds_an_anchored_syntax(tmp_path: Path) -> None:
    (tmp_path / "m.yaml").write_text(
        "slots:\n"
        "  s:\n"
        "    structured_pattern:\n"
        "      syntax: '^{id_nmdc_prefix}:x$'\n"
        "      interpolated: true\n"
        "  t:\n"
        "    structured_pattern:\n"
        "      syntax: '^y'\n"
        "      partial_match: true\n",
        encoding="utf-8",
    )
    assert _anchored_syntaxes(tmp_path) == [("m.yaml", "/slots/s", "^{id_nmdc_prefix}:x$")]


@pytest.mark.skipif(
    tuple(int(part) for part in version("linkml-runtime").split(".")[:2]) < (1, 12),
    reason="linkml-runtime older than 1.12 does not wrap resolved patterns",
)
def test_nmdc_id_patterns_are_wrapped_once() -> None:
    view = SchemaView(str(SCHEMA_DIR / "nmdc.yaml"))
    checked = 0
    for class_name in view.all_classes():
        if "id" not in view.class_slots(class_name):
            continue
        pattern = view.induced_slot("id", class_name).pattern
        if pattern is None or "(nmdc)" not in pattern:
            continue
        checked += 1
        assert pattern.startswith("^(?:(nmdc):") and not pattern.endswith("$)$"), f"{class_name}: {pattern}"
    assert checked > 0


def _doubled_resolved_patterns(view: SchemaView) -> list[tuple[str, str]]:
    """Return (element, pattern) for every resolved pattern that carries a second pair of anchors.

    Resolves the patterns of every slot, slot_usage, attribute and type, imports included, which is
    what linkml generate linkml --materialize-patterns writes to nmdc_materialized_patterns.yaml.
    """
    definitions = [(f"slots/{name}", slot) for name, slot in view.all_slots().items()]
    for class_name, class_def in view.all_classes().items():
        for kind in ("slot_usage", "attributes"):
            for slot_name, slot in (getattr(class_def, kind) or {}).items():
                definitions.append((f"classes/{class_name}/{kind}/{slot_name}", slot))
    definitions += [
        (f"types/{name}", type_def) for name, type_def in view.all_types().items()
    ]
    doubled = []
    for element, definition in definitions:
        if definition.structured_pattern is None:
            continue
        pattern = view.resolve_pattern(definition)
        if pattern.startswith("^(?:^") or pattern.endswith("$)$"):
            doubled.append((element, pattern))
    return doubled


@pytest.mark.skipif(
    tuple(int(part) for part in version("linkml-runtime").split(".")[:2]) < (1, 12),
    reason="linkml-runtime older than 1.12 does not wrap resolved patterns",
)
def test_resolved_patterns_are_anchored_once() -> None:
    exempt = {f"slots/{path.rsplit('/', 1)[-1]}" for _, path in KEEP_ANCHORS}
    doubled = [
        found
        for found in _doubled_resolved_patterns(
            SchemaView(str(SCHEMA_DIR / "nmdc.yaml"))
        )
        if found[0] not in exempt
    ]
    assert not doubled, (
        f"{len(doubled)} resolved patterns are anchored twice, e.g. {doubled[:3]}"
    )


@pytest.mark.skipif(
    tuple(int(part) for part in version("linkml-runtime").split(".")[:2]) < (1, 12),
    reason="linkml-runtime older than 1.12 does not wrap resolved patterns",
)
def test_doubled_anchor_check_finds_an_imported_pattern(tmp_path: Path) -> None:
    (tmp_path / "imported.yaml").write_text(
        "id: https://example.org/imported\n"
        "name: imported\n"
        "imports:\n"
        "  - linkml:types\n"
        "prefixes:\n"
        "  linkml: https://w3id.org/linkml/\n"
        "default_range: string\n"
        "slots:\n"
        "  doubled:\n"
        "    structured_pattern:\n"
        "      syntax: '^(a|b)$'\n"
        "  partial:\n"
        "    structured_pattern:\n"
        "      syntax: '^c$'\n"
        "      partial_match: true\n",
        encoding="utf-8",
    )
    (tmp_path / "main.yaml").write_text(
        "id: https://example.org/main\n"
        "name: main\n"
        "imports:\n"
        "  - imported\n"
        "prefixes:\n"
        "  linkml: https://w3id.org/linkml/\n"
        "slots:\n"
        "  single:\n"
        "    structured_pattern:\n"
        "      syntax: '(d|e)'\n",
        encoding="utf-8",
    )
    doubled = _doubled_resolved_patterns(SchemaView(str(tmp_path / "main.yaml")))
    assert doubled == [("slots/doubled", "^(?:^(a|b)$)$")]
