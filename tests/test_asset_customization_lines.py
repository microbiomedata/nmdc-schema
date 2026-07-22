"""Guard the MIxS customization asset against shell-quoting breaks.

``makefiles/mixs.Makefile`` applies each active line of
``assets/yq-for-mixs-customizations.txt`` with ``eval yq -i $line $@``. An
active line is single-quote-wrapped (``'<yq expression>'``). Any literal single
quote inside that wrapper (for example an apostrophe in ``MIxS's``) closes the
quote early, so ``eval`` mangles the command. The Makefile loop's exit status is
the last iteration's, so a mid-file failure is otherwise swallowed and the
customization is silently dropped while ``make src/schema/mixs.yaml`` still
reports success. This test catches such lines before a regeneration would lose
them.

``shlex.split`` models POSIX-shell word splitting, which is what ``eval`` does
to the line. A well-formed active line tokenizes to exactly ``yq``, ``-i``, one
expression token, and the target path; a broken quote either raises or splits
the expression across extra tokens.
"""

import shlex

from tests import ROOT

ASSET = ROOT / "assets" / "yq-for-mixs-customizations.txt"


def test_active_customization_lines_survive_shell_eval():
    """Every active (``^'``) customization line must tokenize as the Makefile expects."""
    failures = []
    for lineno, raw in enumerate(ASSET.read_text().splitlines(), start=1):
        if not raw.startswith("'"):
            continue  # commented/blank line; the Makefile's `grep "^'"` skips it
        command = f"yq -i {raw} target.yaml"
        try:
            tokens = shlex.split(command)
        except ValueError as err:
            failures.append(f"line {lineno}: unparseable under `eval` ({err}): {raw}")
            continue
        # yq, -i, <one single expression token>, target.yaml
        if len(tokens) != 4:
            failures.append(
                f"line {lineno}: tokenizes into {len(tokens)} words, expected 4 "
                f"(an interior quote is splitting the expression): {raw}"
            )

    assert not failures, "Customization lines that break `eval yq`:\n" + "\n".join(failures)
