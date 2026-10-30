"""Copy the settings each schema module needs from src/schema/nmdc.yaml into that module.

From linkml-runtime 1.12, a structured_pattern is interpolated only with the settings of the
module that defines it (https://github.com/linkml/linkml/issues/4135). Settings declared in
nmdc.yaml no longer reach patterns in the modules it imports, so those patterns keep literal
placeholders such as {id_nmdc_prefix}. This script gives each module a settings block holding
exactly the keys its interpolated patterns use, with values copied from nmdc.yaml, which stays
the single place to edit a value.

The block is written at the end of the module, after a marker comment, and is replaced on each
run. Run it after changing a setting in nmdc.yaml or a pattern in a module:

    uv run python src/scripts/sync_module_settings.py src/schema/core.yaml ...

With --check, nothing is written and the exit status is 1 if any module is out of date.
See https://github.com/microbiomedata/nmdc-schema/issues/3523.
"""

import re
import sys
from pathlib import Path

import click
import yaml

SCHEMA_DIR = Path(__file__).resolve().parents[2] / "src" / "schema"
SOURCE_SCHEMA = SCHEMA_DIR / "nmdc.yaml"

# A named {setting} placeholder. Regex repetition such as {2} or {0,6} is not one.
PLACEHOLDER = re.compile(r"\{([A-Za-z_][A-Za-z0-9_]*)\}")

MARKER = (
    "# Settings below are copied from nmdc.yaml by src/scripts/sync_module_settings.py.\n"
    "# Do not edit them here; edit nmdc.yaml and rerun the script.\n"
    "# See https://github.com/microbiomedata/nmdc-schema/issues/3523\n"
)


def used_setting_keys(node: object) -> set[str]:
    """Return the placeholder names used by interpolated structured_patterns anywhere in node.

    >>> sorted(used_setting_keys({"s": {"structured_pattern": {"syntax": "^{a}:{b}[0-9]{2}$", "interpolated": True}}}))
    ['a', 'b']
    >>> used_setting_keys({"s": {"structured_pattern": {"syntax": "^{a}$"}}})
    set()
    """
    keys: set[str] = set()
    if isinstance(node, dict):
        structured_pattern = node.get("structured_pattern")
        if (
            isinstance(structured_pattern, dict)
            and structured_pattern.get("interpolated") is True
        ):
            keys.update(PLACEHOLDER.findall(str(structured_pattern.get("syntax", ""))))
        for value in node.values():
            keys.update(used_setting_keys(value))
    elif isinstance(node, list):
        for value in node:
            keys.update(used_setting_keys(value))
    return keys


def slot_usage_index(schema_dir: Path = SCHEMA_DIR) -> dict[str, set[str]]:
    """Map each slot name to the placeholders that slot_usage patterns, in any module, use on it.

    Build it once per run and pass it to required_setting_keys, so the schema files are
    read once rather than once per module.
    """
    index: dict[str, set[str]] = {}
    for path in sorted(schema_dir.glob("*.yaml")):
        parsed = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        for class_def in (parsed.get("classes") or {}).values():
            for slot_name, usage in ((class_def or {}).get("slot_usage") or {}).items():
                keys = used_setting_keys(usage)
                if keys:
                    index.setdefault(slot_name, set()).update(keys)
    return index


def required_setting_keys(
    parsed: dict,
    schema_dir: Path = SCHEMA_DIR,
    index: dict[str, set[str]] | None = None,
) -> set[str]:
    """Return the settings a module must declare.

    That is the keys its own interpolated patterns use, plus the keys that slot_usage patterns
    in any module use on the slots it defines. linkml 1.12 gen-python builds a class-specific
    slot such as Biosample_id from slot_usage but fills its pattern with the settings of the
    module that defines the base slot (id, in basic_slots.yaml).
    See https://github.com/microbiomedata/nmdc-schema/pull/3529.
    """
    keys = used_setting_keys(parsed)
    slot_names = set(parsed.get("slots") or {})
    if not slot_names:
        return keys
    if index is None:
        index = slot_usage_index(schema_dir)
    for slot_name in slot_names:
        keys |= index.get(slot_name, set())
    return keys


def source_settings(source_schema: Path = SOURCE_SCHEMA) -> dict[str, str]:
    """Return the settings declared in the source schema as plain strings."""
    with source_schema.open(encoding="utf-8") as f:
        settings = yaml.safe_load(f).get("settings") or {}
    return {key: str(value) for key, value in settings.items()}


def strip_settings_block(text: str) -> str:
    """Remove a block previously written by this script, if present.

    >>> strip_settings_block("a: 1\\n\\n" + MARKER + "settings:\\n  x: 'y'\\n")
    'a: 1\\n'
    >>> strip_settings_block("a: 1\\n")
    'a: 1\\n'
    """
    index = text.find(MARKER)
    if index == -1:
        return text
    return text[:index].rstrip("\n") + "\n"


def settings_block(keys: set[str], settings: dict[str, str]) -> str:
    """Return the marker and a settings block for keys, quoted so YAML reads the values back unchanged."""
    missing = sorted(keys - settings.keys())
    if missing:
        raise KeyError(
            f"placeholders with no value in the source schema's settings: {', '.join(missing)}"
        )
    body = yaml.safe_dump(
        {"settings": {key: settings[key] for key in sorted(keys)}},
        default_style=None,
        sort_keys=False,
        allow_unicode=True,
        width=float("inf"),
    )
    return MARKER + body


def synced_text(
    module: Path,
    settings: dict[str, str],
    index: dict[str, set[str]] | None = None,
) -> str:
    """Return the module's text with its settings block brought up to date."""
    text = module.read_text(encoding="utf-8")
    base = strip_settings_block(text)
    parsed = yaml.safe_load(base)
    if "settings" in parsed:
        raise ValueError(
            f"{module} declares its own settings outside the generated block"
        )
    keys = required_setting_keys(parsed, module.parent, index)
    if not keys:
        return base
    return base + "\n" + settings_block(keys, settings)


@click.command()
@click.argument(
    "modules",
    nargs=-1,
    required=True,
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
)
@click.option(
    "--check", is_flag=True, help="Write nothing; exit 1 if any module is out of date."
)
@click.option(
    "--source",
    default=SOURCE_SCHEMA,
    show_default=True,
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
    help="Schema whose settings are copied.",
)
def main(modules: tuple[Path, ...], check: bool, source: Path) -> None:
    """Copy the settings each MODULE's interpolated structured_patterns use from the source schema."""
    settings = source_settings(source)
    stale = []
    indexes: dict[Path, dict[str, set[str]]] = {}
    for module in modules:
        directory = module.resolve().parent
        if directory not in indexes:
            indexes[directory] = slot_usage_index(directory)
        new_text = synced_text(module, settings, indexes[directory])
        if new_text == module.read_text(encoding="utf-8"):
            continue
        stale.append(module)
        if not check:
            module.write_text(new_text, encoding="utf-8")
            click.echo(f"updated {module}")
    if check and stale:
        click.echo("out of date: " + ", ".join(str(m) for m in stale), err=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
