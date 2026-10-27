"""Each schema module must carry the settings its interpolated structured_patterns use.

linkml-runtime 1.12 interpolates a structured_pattern only with the settings of the module that
defines it (https://github.com/linkml/linkml/issues/4135), so settings declared only in nmdc.yaml
leave literal placeholders such as {id_nmdc_prefix} in every other module's patterns. The copies
are written by src/scripts/sync_module_settings.py; nmdc.yaml stays the one place to edit a value.
See https://github.com/microbiomedata/nmdc-schema/issues/3523.

The checks resolve each module with PatternResolver on that module alone, which reads only the
module's own settings on linkml-runtime 1.11 and 1.12 alike, so they fail on the old layout even
though the locked runtime still merges settings across imports.
"""

from pathlib import Path

import pytest
import yaml
from click.testing import CliRunner
from linkml_runtime import SchemaView
from linkml_runtime.utils.pattern import PatternResolver

from src.scripts.sync_module_settings import (
    MARKER,
    PLACEHOLDER,
    main,
    settings_block,
    source_settings,
    strip_settings_block,
    synced_text,
    required_setting_keys,
    slot_usage_index,
    used_setting_keys,
)

SCHEMA_DIR = Path(__file__).resolve().parent.parent / "src" / "schema"
SOURCE_SCHEMA = SCHEMA_DIR / "nmdc.yaml"


def _load(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def _interpolated_syntaxes(node: object) -> list[str]:
    found = []
    if isinstance(node, dict):
        structured_pattern = node.get("structured_pattern")
        if (
            isinstance(structured_pattern, dict)
            and structured_pattern.get("interpolated") is True
        ):
            found.append(str(structured_pattern["syntax"]))
        for value in node.values():
            found.extend(_interpolated_syntaxes(value))
    elif isinstance(node, list):
        for value in node:
            found.extend(_interpolated_syntaxes(value))
    return found


# Built once for the session instead of once per module.
SLOT_USAGE_INDEX = slot_usage_index(SCHEMA_DIR)

MODULES_WITH_PATTERNS = sorted(
    path.name
    for path in SCHEMA_DIR.glob("*.yaml")
    if path.name != SOURCE_SCHEMA.name
    and required_setting_keys(_load(path), SCHEMA_DIR, SLOT_USAGE_INDEX)
)

# Every module but nmdc.yaml, so a block left behind after a module's last placeholder is
# removed is still found as stale.
ALL_MODULES = sorted(
    path.name for path in SCHEMA_DIR.glob("*.yaml") if path.name != SOURCE_SCHEMA.name
)


def test_modules_with_interpolated_patterns_are_found() -> None:
    """Guard against the parametrized tests below silently checking nothing."""
    assert {
        "core.yaml",
        "basic_classes.yaml",
        "mixs.yaml",
        "workflow_execution_activity.yaml",
    } <= set(MODULES_WITH_PATTERNS)


@pytest.mark.parametrize("module_name", MODULES_WITH_PATTERNS)
def test_module_declares_every_setting_its_patterns_use(module_name: str) -> None:
    module = _load(SCHEMA_DIR / module_name)
    declared = set((module.get("settings") or {}).keys())
    missing = sorted(
        required_setting_keys(module, SCHEMA_DIR, SLOT_USAGE_INDEX) - declared
    )
    assert not missing, f"{module_name} uses settings it does not declare: {missing}"


@pytest.mark.parametrize("module_name", ALL_MODULES)
def test_module_declares_no_unused_settings(module_name: str) -> None:
    module = _load(SCHEMA_DIR / module_name)
    declared = set((module.get("settings") or {}).keys())
    extra = sorted(
        declared - required_setting_keys(module, SCHEMA_DIR, SLOT_USAGE_INDEX)
    )
    assert not extra, (
        f"{module_name} declares settings none of its patterns use: {extra}"
    )


@pytest.mark.parametrize("module_name", MODULES_WITH_PATTERNS)
def test_module_setting_values_match_nmdc_yaml(module_name: str) -> None:
    source = source_settings(SOURCE_SCHEMA)
    declared = _load(SCHEMA_DIR / module_name).get("settings") or {}
    drifted = sorted(
        key for key, value in declared.items() if str(value) != source.get(key)
    )
    assert not drifted, (
        f"{module_name} settings differ from nmdc.yaml for {drifted}; rerun sync_module_settings.py"
    )


@pytest.mark.parametrize("module_name", MODULES_WITH_PATTERNS)
def test_module_patterns_resolve_with_only_its_own_settings(module_name: str) -> None:
    """The linkml 1.12 rule: a pattern sees only its own module's settings."""
    resolver = PatternResolver(SchemaView(str(SCHEMA_DIR / module_name)))
    unresolved = [
        syntax
        for syntax in _interpolated_syntaxes(_load(SCHEMA_DIR / module_name))
        if PLACEHOLDER.search(resolver.resolve(syntax))
    ]
    assert not unresolved, (
        f"{module_name}: {len(unresolved)} patterns keep placeholders, e.g. {unresolved[:3]}"
    )


def test_nmdc_yaml_patterns_resolve_with_its_own_settings() -> None:
    resolver = PatternResolver(SchemaView(str(SOURCE_SCHEMA)))
    unresolved = [
        syntax
        for syntax in _interpolated_syntaxes(_load(SOURCE_SCHEMA))
        if PLACEHOLDER.search(resolver.resolve(syntax))
    ]
    assert not unresolved


def test_settings_copies_are_up_to_date() -> None:
    """The same check as `sync_module_settings.py --check` over every module."""
    result = CliRunner().invoke(
        main, ["--check", *(str(SCHEMA_DIR / name) for name in ALL_MODULES)]
    )
    assert result.exit_code == 0, result.output


def test_settings_block_is_the_last_thing_in_each_module() -> None:
    """The script replaces everything after the marker, so nothing hand-written may follow it."""
    for module_name in MODULES_WITH_PATTERNS:
        text = (SCHEMA_DIR / module_name).read_text(encoding="utf-8")
        assert text.count(MARKER) == 1, module_name
        tail = text[text.index(MARKER) + len(MARKER) :]
        assert set(yaml.safe_load(tail).keys()) == {"settings"}, module_name


# Unit tests for src/scripts/sync_module_settings.py


@pytest.fixture
def module_file(tmp_path: Path) -> Path:
    path = tmp_path / "module.yaml"
    path.write_text(
        "id: https://example.org/module\n"
        "name: module\n"
        "slots:\n"
        "  id:\n"
        "    structured_pattern:\n"
        "      syntax: '{id_nmdc_prefix}:x-{id_shoulder}-[0-9]{2}$'\n"
        "      interpolated: true\n"
        "  code:\n"
        "    structured_pattern:\n"
        "      syntax: '^{not_interpolated}$'\n",
        encoding="utf-8",
    )
    return path


def test_used_setting_keys_ignores_quantifiers_and_uninterpolated_patterns(
    module_file: Path,
) -> None:
    assert used_setting_keys(_load(module_file)) == {"id_nmdc_prefix", "id_shoulder"}


def test_sync_adds_only_the_keys_used(module_file: Path) -> None:
    settings = {"id_nmdc_prefix": "^(nmdc)", "id_shoulder": "([0-9])", "unused": "x"}
    parsed = yaml.safe_load(synced_text(module_file, settings))
    assert parsed["settings"] == {"id_nmdc_prefix": "^(nmdc)", "id_shoulder": "([0-9])"}


def test_sync_keeps_the_rest_of_the_file_byte_for_byte(module_file: Path) -> None:
    original = module_file.read_text(encoding="utf-8")
    new_text = synced_text(module_file, {"id_nmdc_prefix": "a", "id_shoulder": "b"})
    assert new_text.startswith(original)


def test_sync_is_idempotent(module_file: Path) -> None:
    settings = {"id_nmdc_prefix": "a", "id_shoulder": "b"}
    module_file.write_text(synced_text(module_file, settings), encoding="utf-8")
    assert synced_text(module_file, settings) == module_file.read_text(encoding="utf-8")


def test_sync_replaces_a_stale_value(module_file: Path) -> None:
    module_file.write_text(
        synced_text(module_file, {"id_nmdc_prefix": "old", "id_shoulder": "b"}),
        encoding="utf-8",
    )
    parsed = yaml.safe_load(
        synced_text(module_file, {"id_nmdc_prefix": "new", "id_shoulder": "b"})
    )
    assert parsed["settings"]["id_nmdc_prefix"] == "new"


def test_sync_removes_the_block_when_no_pattern_needs_it(tmp_path: Path) -> None:
    path = tmp_path / "plain.yaml"
    path.write_text(
        "id: https://example.org/plain\nname: plain\n\n"
        + MARKER
        + "settings:\n  x: 'y'\n",
        encoding="utf-8",
    )
    assert (
        synced_text(path, {"x": "y"}) == "id: https://example.org/plain\nname: plain\n"
    )


def test_check_finds_a_block_left_after_the_last_placeholder_is_removed(
    tmp_path: Path,
) -> None:
    path = tmp_path / "plain.yaml"
    path.write_text(
        "id: https://example.org/plain\nname: plain\n\n"
        + MARKER
        + "settings:\n  x: 'y'\n",
        encoding="utf-8",
    )
    source = tmp_path / "source.yaml"
    source.write_text(
        "id: https://example.org/s\nname: s\nsettings:\n  x: 'y'\n", encoding="utf-8"
    )
    result = CliRunner().invoke(main, ["--check", "--source", str(source), str(path)])
    assert result.exit_code == 1


def test_sync_rejects_a_placeholder_with_no_value(module_file: Path) -> None:
    with pytest.raises(KeyError, match="id_shoulder"):
        synced_text(module_file, {"id_nmdc_prefix": "a"})


def test_sync_refuses_hand_written_settings(tmp_path: Path) -> None:
    path = tmp_path / "own.yaml"
    path.write_text(
        "id: https://example.org/own\nname: own\nsettings:\n  a: b\n"
        "slots:\n  s:\n    structured_pattern:\n      syntax: '{a}'\n      interpolated: true\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="declares its own settings"):
        synced_text(path, {"a": "b"})


def test_every_nmdc_setting_value_survives_the_round_trip() -> None:
    """Backslashes, quotes, colons and leading ^ in nmdc.yaml values must read back unchanged."""
    settings = source_settings(SOURCE_SCHEMA)
    block = settings_block(set(settings), settings)
    assert yaml.safe_load(block.removeprefix(MARKER))["settings"] == settings


def test_strip_settings_block_without_a_block_is_a_no_op(module_file: Path) -> None:
    text = module_file.read_text(encoding="utf-8")
    assert strip_settings_block(text) == text


def test_cli_check_reports_and_writes_nothing(
    module_file: Path, tmp_path: Path
) -> None:
    source = tmp_path / "source.yaml"
    source.write_text(
        "id: https://example.org/s\nname: s\nsettings:\n  id_nmdc_prefix: a\n  id_shoulder: b\n",
        encoding="utf-8",
    )
    before = module_file.read_text(encoding="utf-8")
    result = CliRunner().invoke(
        main, ["--check", "--source", str(source), str(module_file)]
    )
    assert result.exit_code == 1
    assert module_file.read_text(encoding="utf-8") == before

    result = CliRunner().invoke(main, ["--source", str(source), str(module_file)])
    assert result.exit_code == 0
    result = CliRunner().invoke(
        main, ["--check", "--source", str(source), str(module_file)]
    )
    assert result.exit_code == 0, result.output


def test_module_gets_the_settings_slot_usage_patterns_use_on_its_slots(
    tmp_path: Path,
) -> None:
    """gen-python fills a slot_usage pattern with the settings of the module defining the slot."""
    (tmp_path / "slots.yaml").write_text(
        "slots:\n  id: {}\n  other: {}\n", encoding="utf-8"
    )
    (tmp_path / "classes.yaml").write_text(
        "classes:\n"
        "  Thing:\n"
        "    slot_usage:\n"
        "      id:\n"
        "        structured_pattern:\n"
        "          syntax: '{prefix}:thing-[0-9]+'\n"
        "          interpolated: true\n",
        encoding="utf-8",
    )
    slots_module = yaml.safe_load((tmp_path / "slots.yaml").read_text(encoding="utf-8"))
    assert used_setting_keys(slots_module) == set()
    assert required_setting_keys(slots_module, tmp_path) == {"prefix"}
    # A module whose slots have no such slot_usage needs nothing.
    assert required_setting_keys({"slots": {"other": {}}}, tmp_path) == set()
