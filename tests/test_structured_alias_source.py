"""Require every hand-written structured alias to name its origin in ``source``.

In the LinkML StructuredAlias metamodel, ``source`` is where an alias comes
from and ``contexts`` is where it applies. This schema records origins, so
each alias needs a ``source`` and none should use ``contexts`` for that.
See CLAUDE.md ("structured_aliases") and
https://github.com/microbiomedata/nmdc-schema/issues/3454

Like tests/test_attribution_metaslots.py, this reads the src/schema/*.yaml
source files rather than the generated artifact. That includes
src/schema/mixs.yaml: it is generated, but its structured aliases are written
by NMDC in assets/yq-for-mixs-customizations.txt, so fix them there and
regenerate.
"""

from collections.abc import Iterator
from pathlib import Path

import yaml

# (file, literal_form) pairs known to use contexts. Don't add to this set.
GRANDFATHERED: set[tuple[str, str]] = set()


def structured_aliases(node: object, path: str = "") -> Iterator[tuple[str, object]]:
    """Yield (location, alias) for every structured alias at any depth."""
    if isinstance(node, dict):
        for key, value in node.items():
            location = f"{path}/{key}"
            if key == "structured_aliases" and isinstance(value, list):
                for alias in value:
                    yield location, alias
            yield from structured_aliases(value, location)
    elif isinstance(node, list):
        for item in node:
            yield from structured_aliases(item, path)


def test_structured_aliases_name_their_source() -> None:
    repository_root = Path(__file__).resolve().parents[1]
    problems = []
    still_grandfathered = set()
    for schema_path in sorted((repository_root / "src" / "schema").glob("*.yaml")):
        with schema_path.open(encoding="utf-8") as source_file:
            schema = yaml.safe_load(source_file)
        for location, alias in structured_aliases(schema):
            label = alias.get("literal_form") if isinstance(alias, dict) else alias
            where = f"{schema_path.relative_to(repository_root)}{location}: {label!r}"
            found = []
            if not isinstance(alias, dict) or not alias.get("source"):
                found.append(f"{where} has no source")
            if isinstance(alias, dict) and "contexts" in alias:
                found.append(f"{where} uses contexts; put its origin in source")
            if found and (schema_path.name, label) in GRANDFATHERED:
                still_grandfathered.add((schema_path.name, label))
            else:
                problems.extend(found)

    assert not problems, (
        "Each structured alias needs a source (where it comes from), not contexts.\n"
        + "\n".join(problems)
    )
    assert still_grandfathered == GRANDFATHERED, (
        f"Remove fixed entries from GRANDFATHERED: {sorted(GRANDFATHERED - still_grandfathered)}"
    )
