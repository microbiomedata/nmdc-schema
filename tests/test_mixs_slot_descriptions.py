"""Catch MIxS slot descriptions left broken by a yq ``sub()`` customization.

``assets/yq-for-mixs-customizations.txt`` edits imported MIxS descriptions with
``.description |= sub("<search>"; "<replacement>")``. yq's ``sub()`` treats the
search text as a regular expression, so a literal ``|`` in it is read as
alternation. The first alternative matches and is removed, and the rest of the
sentence stays behind as a fragment that starts with ``|``, for example
"... in the isotopolog. | and should be orded the same as the isotopolog."

The test reads the generated ``src/schema/mixs.yaml`` rather than the asset,
because only the generated text shows what the substitution did. It rejects
any ``|`` in a description, not only a leading one: if the upstream wording
changes, a ``sub()`` that stops matching leaves the whole sentence, pipe
included, and that should fail too. No description on ``main`` contained a
``|`` when this test was added (2026-10-01).
"""

import yaml

from tests import ROOT

MIXS_YAML = ROOT / "src" / "schema" / "mixs.yaml"


def test_no_slot_description_contains_a_pipe():
    """No imported MIxS slot description may contain ``|``, the spreadsheet value separator."""
    slots = yaml.safe_load(MIXS_YAML.read_text())["slots"]
    failures = [
        f"{name}: {slot['description']}"
        for name, slot in slots.items()
        if isinstance(slot, dict) and "|" in (slot.get("description") or "")
    ]
    assert not failures, "Descriptions containing '|':\n" + "\n".join(failures)
