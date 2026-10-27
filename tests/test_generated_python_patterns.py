"""The generated Python classes must not compile patterns that still hold {setting} placeholders.

linkml 1.12 gen-python fills a class's slot_usage pattern (for example Biosample_id) with the
settings of the module that defines the base slot, so a missing settings block there leaves
patterns such as ^(?:{id_nmdc_prefix}:bsm-...)$ that match no real id.
See https://github.com/microbiomedata/nmdc-schema/pull/3529.
"""

import re
from pathlib import Path

NMDC_PY = Path(__file__).resolve().parents[1] / "nmdc_schema" / "nmdc.py"

# A named {setting} placeholder inside a compiled pattern. Regex repetition such as {2} is not one.
UNFILLED = re.compile(r"re\.compile\(r?['\"][^'\"]*\{[A-Za-z_][A-Za-z0-9_]*\}")


def test_unfilled_pattern_regex_finds_a_placeholder() -> None:
    assert UNFILLED.search(
        "pattern=re.compile(r'^(?:{id_nmdc_prefix}:bsm-{id_shoulder}$)$')"
    )
    assert not UNFILLED.search(
        "pattern=re.compile(r'^(?:(nmdc):bsm-([0-9][a-z]{0,6}[0-9]))$')"
    )


def test_generated_python_compiles_no_unfilled_patterns() -> None:
    unfilled = [
        line.strip()
        for line in NMDC_PY.read_text(encoding="utf-8").splitlines()
        if UNFILLED.search(line)
    ]
    assert not unfilled, (
        f"{len(unfilled)} compiled patterns keep placeholders, e.g. {unfilled[:2]}"
    )
