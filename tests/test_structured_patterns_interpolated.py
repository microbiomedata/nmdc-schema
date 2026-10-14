"""Every structured_pattern whose syntax uses {setting} placeholders must set interpolated: true.

linkml 1.11 expanded the placeholders even without the flag, but linkml 1.12.0rc2 leaves them
as literal text, so the generated pattern can never match a valid id.
"""
import re
from pathlib import Path

import yaml

SCHEMA_DIR = Path(__file__).resolve().parent.parent / "src" / "schema"

# A named {setting} placeholder. Regex repetition such as {2} or {0,6} is not one.
PLACEHOLDER = re.compile(r"\{[A-Za-z_][A-Za-z0-9_]*\}")


def _uninterpolated(node: object, path: str) -> list[str]:
    found = []
    if isinstance(node, dict):
        structured_pattern = node.get("structured_pattern")
        if isinstance(structured_pattern, dict):
            syntax = str(structured_pattern.get("syntax", ""))
            if PLACEHOLDER.search(syntax) and structured_pattern.get("interpolated") is not True:
                found.append(f"{path}: {syntax}")
        for key, value in node.items():
            found.extend(_uninterpolated(value, f"{path}/{key}"))
    elif isinstance(node, list):
        for index, value in enumerate(node):
            found.extend(_uninterpolated(value, f"{path}[{index}]"))
    return found


def test_structured_patterns_with_placeholders_are_interpolated() -> None:
    problems = []
    for schema_file in sorted(SCHEMA_DIR.glob("*.yaml")):
        with schema_file.open(encoding="utf-8") as f:
            problems.extend(_uninterpolated(yaml.safe_load(f), schema_file.name))
    assert not problems, "structured_pattern with {placeholders} but no interpolated: true:\n" + "\n".join(problems)


def test_regex_repetition_is_not_a_placeholder() -> None:
    assert _uninterpolated({"structured_pattern": {"syntax": "^[0-9]{2}$"}}, "x") == []
    assert _uninterpolated({"structured_pattern": {"syntax": "^[a-z]{0,6}$"}}, "x") == []
    assert _uninterpolated({"structured_pattern": {"syntax": "^{id_shoulder}$"}}, "x") == ["x: ^{id_shoulder}$"]
