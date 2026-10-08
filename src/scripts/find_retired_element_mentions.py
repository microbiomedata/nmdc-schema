"""Find mentions of retired schema element names in files that no build or test checks.

Retired names come from two places: the definitions in ``src/schema/deprecated.yaml``
and the catalog written by ``schema_element_history.py`` (elements some release defined
and the current schema does not). A name the current schema still defines is dropped, so
a slot retired from one module and redefined in another is not reported. With
``--permissible-values``, a value that any current enum still has is dropped too.

By default the scan covers tracked files outside the paths that something already
checks: schema sources (linted), example data (validated), the ``nmdc_schema`` package
(generated files and frozen migrators), and tests. Matches are whole-word and
case-sensitive. A match is a lead, not a defect: changelogs, aliases and history notes
may mention a retired name on purpose.

Names that are ordinary lowercase words or phrases (``soil``, ``part of``) are not scanned
by default, because early schema versions used many of them and they match ordinary text.
Pass ``--plain-words`` to include them. Permissible values are not scanned by default for
the same reason. Pass ``--permissible-values`` to include them.

Usage:
    poetry run python src/scripts/find_retired_element_mentions.py \\
        --catalog assets/schema_element_history/retired_elements.tsv -o local/retired_mentions.tsv
"""

from __future__ import annotations

import csv
import logging
import re
import subprocess
import sys
from collections import Counter
from collections.abc import Iterable
from pathlib import Path

import click

sys.path.insert(0, str(Path(__file__).parent))
from schema_element_history import (  # noqa: E402
    DEPRECATED,
    Key,
    blobs_at,
    current_inventory,
    inventory_of_blob,
)

logger = logging.getLogger(__name__)

IDENTIFIER_LIKE = re.compile(r"^[A-Za-z0-9]*(_|[a-z0-9][A-Z]|^[A-Z])")
WORD = re.compile(r"[A-Za-z0-9_]+")
LOCK_FILES = ("poetry.lock", "uv.lock")
CHECKED_PATHS = ("src/schema", "src/data", "nmdc_schema", "tests", ".github")


def build_names(
    deprecated: Iterable[Key],
    catalog_rows: Iterable[dict[str, str]],
    current: Iterable[Key],
    permissible_values: bool,
) -> dict[str, dict[str, str]]:
    """Return retired names mapped to their kind, last release and deprecated.yaml status.

    A name is dropped when the current schema defines it as an element, or, when
    permissible values are included, as a value of any current enum.
    """
    current = set(current)
    active = {name for kind, _, name in current if kind != "permissible_values"}
    if permissible_values:
        active |= {name for kind, _, name in current if kind == "permissible_values"}
    names: dict[str, dict[str, str]] = {}

    def add(name: str, kind: str, last_tag: str, recorded: str) -> None:
        entry = names.setdefault(
            name, {"kind": kind, "last_tag": "", "in_deprecated_yaml": ""}
        )
        if kind not in entry["kind"].split(","):
            entry["kind"] = f"{entry['kind']},{kind}"
        if last_tag and not entry["last_tag"]:
            entry["last_tag"] = last_tag
        if recorded:
            entry["in_deprecated_yaml"] = "yes"

    for kind, _, name in deprecated:
        if kind != "permissible_values" or permissible_values:
            add(name, kind, "", "yes")
    for row in catalog_rows:
        if row["kind"] != "permissible_values" or permissible_values:
            add(row["name"], row["kind"], row["last_tag"], row["in_deprecated_yaml"])
    return {name: info for name, info in names.items() if name not in active}


def keep_identifier_like(names: dict[str, dict[str, str]]) -> dict[str, dict[str, str]]:
    """Drop names that are ordinary lowercase words or phrases."""
    return {
        name: info
        for name, info in names.items()
        if IDENTIFIER_LIKE.match(name) and " " not in name
    }


def phrase_patterns(names: Iterable[str]) -> dict[str, re.Pattern[str]]:
    """Return a whole-word pattern for each name that is not a single word, such as `part of`."""
    return {
        name: re.compile(rf"(?<![A-Za-z0-9_]){re.escape(name)}(?![A-Za-z0-9_])")
        for name in names
        if not WORD.fullmatch(name)
    }


def names_in_line(
    line: str, names: dict[str, dict[str, str]], phrases: dict[str, re.Pattern[str]]
) -> set[str]:
    """Return the retired names that appear in a line as whole words."""
    found = {token for token in WORD.findall(line) if token in names}
    found |= {name for name, pattern in phrases.items() if pattern.search(line)}
    return found


def is_skipped(path: str, skipped: tuple[str, ...]) -> bool:
    """Return True when a path is one of the skipped paths or inside one."""
    return any(path == p or path.startswith(f"{p}/") for p in skipped)


def retired_names(
    catalog: Path | None, ref: str, permissible_values: bool
) -> dict[str, dict[str, str]]:
    """Read deprecated.yaml and the catalog at ref and return the retired names."""
    deprecated: set[Key] = set()
    for path, blob in blobs_at(ref, built=False):
        if path == DEPRECATED:
            deprecated |= inventory_of_blob(blob)
    rows: list[dict[str, str]] = []
    if catalog:
        with catalog.open() as fh:
            rows = list(csv.DictReader(fh, delimiter="\t"))
    return build_names(deprecated, rows, current_inventory(ref), permissible_values)


def tracked_text_files(ref: str, skipped: tuple[str, ...]) -> list[tuple[str, str]]:
    """Return (path, text) for every tracked text file at ref outside the skipped paths."""
    listing = subprocess.run(
        ["git", "ls-tree", "-r", ref], check=True, capture_output=True, text=True
    ).stdout
    entries = []
    for line in listing.splitlines():
        meta, path = line.split("\t", 1)
        mode, kind, blob = meta.split()
        if kind != "blob" or mode == "120000" or is_skipped(path, skipped):
            continue
        entries.append((path, blob))
    batch = subprocess.run(
        ["git", "cat-file", "--batch"],
        input="".join(f"{blob}\n" for _, blob in entries).encode(),
        check=True,
        capture_output=True,
    ).stdout
    files = []
    offset = 0
    for path, _ in entries:
        header_end = batch.index(b"\n", offset)
        size = int(batch[offset:header_end].split()[2])
        content = batch[header_end + 1 : header_end + 1 + size]
        offset = header_end + 1 + size + 1
        if b"\0" in content[:8000]:
            continue
        files.append((path, content.decode("utf-8", errors="replace")))
    return files


@click.command()
@click.option(
    "--catalog",
    type=click.Path(exists=True, path_type=Path),
    help="TSV from schema_element_history.py.",
)
@click.option("--ref", default="HEAD", show_default=True, help="The revision to scan.")
@click.option(
    "--output",
    "-o",
    type=click.Path(path_type=Path),
    required=True,
    help="TSV file to write.",
)
@click.option(
    "--include-checked",
    is_flag=True,
    help="Also scan schema sources, example data, the package and tests.",
)
@click.option(
    "--permissible-values",
    is_flag=True,
    help="Also scan for retired permissible values.",
)
@click.option(
    "--plain-words",
    is_flag=True,
    help="Also scan for retired names that are ordinary lowercase words or phrases, such as 'soil' or 'part of'.",
)
def main(
    catalog: Path | None,
    ref: str,
    output: Path,
    include_checked: bool,
    permissible_values: bool,
    plain_words: bool,
) -> None:
    """Write one row per retired name per matching line."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    names = retired_names(catalog, ref, permissible_values)
    if not plain_words:
        names = keep_identifier_like(names)
    logger.info("%d retired names", len(names))
    phrases = phrase_patterns(names)
    skipped = () if include_checked else CHECKED_PATHS
    skipped += (DEPRECATED, "assets/schema_element_history", *LOCK_FILES)
    rows = []
    for path, text in tracked_text_files(ref, skipped):
        for number, line in enumerate(text.splitlines(), start=1):
            for name in sorted(names_in_line(line, names, phrases)):
                info = names[name]
                rows.append(
                    {
                        "path": path,
                        "line": number,
                        "name": name,
                        "kind": info["kind"],
                        "last_tag": info["last_tag"],
                        "in_deprecated_yaml": info["in_deprecated_yaml"],
                        "text": line.strip()[:200],
                    }
                )
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "path",
                "line",
                "name",
                "kind",
                "last_tag",
                "in_deprecated_yaml",
                "text",
            ],
            delimiter="\t",
        )
        writer.writeheader()
        writer.writerows(rows)
    lines = {(row["path"], row["line"]) for row in rows}
    logger.info(
        "%d matching lines in %d files", len(lines), len({row["path"] for row in rows})
    )
    for where, count in Counter(
        "/".join(path.split("/")[:2]) for path, _ in lines
    ).most_common(20):
        logger.info("  %6d  %s", count, where)
    for name, count in Counter(row["name"] for row in rows).most_common(20):
        logger.info("  %6d  %s", count, name)


if __name__ == "__main__":
    main()
