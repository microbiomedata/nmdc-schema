"""List schema elements that some release defined and the current schema does not.

At each release tag, an element counts as defined if any schema source file defines it
(every YAML file under the source directory the tag used, except ``deprecated.yaml``)
or a built schema file shipped with the tag defines it
(``nmdc_schema/nmdc_materialized_patterns.yaml`` or ``nmdc_schema/nmdc_schema_merged.yaml``).
Reading both protects against tags where one of them was partial.

For each element that the current source does not define, the script reports the last
tag that defined it, the first later tag that did not, and the commit on the first-parent
line of ``main`` after which the source stopped defining it. The PR number, the merge
subject and the subjects of the PR's commits that touched the element's definition line
are included as evidence. They are not a disposition: a renamed or moved element looks
the same as a deleted one until someone reads the commits.

Elements are identified by kind and name, and permissible values by enum and value, so
removing a value from one enum does not retire that spelling elsewhere.

Usage:
    poetry run python src/scripts/schema_element_history.py -o local/retired_elements.tsv
"""

from __future__ import annotations

import csv
import logging
import re
import subprocess
from collections import defaultdict
from functools import lru_cache
from pathlib import Path

import click
import linkml_runtime
import yaml

logger = logging.getLogger(__name__)

Key = tuple[str, str, str]

KINDS = ("classes", "slots", "enums", "types", "subsets")
BUILT_FILES = (
    "nmdc_schema/nmdc_materialized_patterns.yaml",
    "nmdc_schema/nmdc_schema_merged.yaml",
)
SOURCE_DIRS = ("src/schema", "src/nmdc_schema/src")
DEPRECATED = "src/schema/deprecated.yaml"
PR_NUMBER = re.compile(r"Merge pull request #(\d+)|\(#(\d+)\)$")


def normalize(name: str) -> str:
    """Return a name lowercased with underscores, hyphens and spaces removed, to spot case-only renames."""
    return re.sub(r"[_\s-]", "", name).lower()


def git(*args: str) -> str:
    """Run a git command in the current repository and return stdout."""
    return subprocess.run(
        ["git", *args], check=True, capture_output=True, text=True
    ).stdout


@lru_cache(maxsize=None)
def inventory_of_blob(blob: str) -> frozenset[Key]:
    """Return (kind, enum, name) for every element and permissible value in one YAML blob."""
    try:
        doc = yaml.safe_load(git("cat-file", "blob", blob))
    except yaml.YAMLError as err:
        logger.warning("could not parse blob %s: %s", blob, err)
        return frozenset()
    if not isinstance(doc, dict):
        return frozenset()
    found = set()
    for kind in KINDS:
        section = doc.get(kind)
        if not isinstance(section, dict):
            continue
        for name, body in section.items():
            found.add((kind, "", str(name)))
            if kind == "enums" and isinstance(body, dict):
                for value in body.get("permissible_values") or {}:
                    found.add(("permissible_values", str(name), str(value)))
    return frozenset(found)


@lru_cache(maxsize=None)
def blobs_at(ref: str, built: bool) -> list[tuple[str, str]]:
    """Return (path, blob) for the schema files at a ref: source files, plus built files when asked."""
    listing = git(
        "ls-tree", "-r", ref, "--", *SOURCE_DIRS, *(BUILT_FILES if built else ())
    )
    blobs = []
    for line in listing.splitlines():
        meta, path = line.split("\t", 1)
        if path.endswith(".yaml"):
            blobs.append((path, meta.split()[2]))
    return blobs


@lru_cache(maxsize=None)
def defined_at(ref: str, built: bool) -> frozenset[Key]:
    """Return everything the schema files at a ref define, not counting deprecated.yaml."""
    found: set[Key] = set()
    for path, blob in blobs_at(ref, built):
        if not path.endswith("deprecated.yaml"):
            found |= inventory_of_blob(blob)
    return frozenset(found)


def linkml_type_names() -> frozenset[str]:
    """Return the names of the types defined by linkml:types, read from the installed linkml_runtime."""
    types_yaml = (
        Path(linkml_runtime.__file__).parent
        / "linkml_model"
        / "model"
        / "schema"
        / "types.yaml"
    )
    return frozenset(yaml.safe_load(types_yaml.read_text())["types"])


def combine_current(
    source: frozenset[Key], built: frozenset[Key], imported_types: frozenset[str]
) -> set[Key]:
    """Return the source inventory plus the built file's types that come from linkml:types.

    Only imported LinkML types are taken from the built file. An NMDC-defined type that was
    removed from the source but survives in a stale built file is not counted as current.
    """
    return set(source) | {
        key for key in built if key[0] == "types" and key[2] in imported_types
    }


def current_inventory(ref: str) -> set[Key]:
    """Return what REF defines now.

    Built files are regenerated only at release, so they can still hold an element that a
    merged PR removed from the source. Source files are used, plus the types that the built
    files import from linkml:types, which no source file defines.
    """
    return combine_current(
        defined_at(ref, built=False), defined_at(ref, built=True), linkml_type_names()
    )


def removal_commits(keys: set[Key], last: str, gone: str) -> dict[Key, str]:
    """Return, for each key, the first-parent commit after which the source no longer defined it."""
    commits = git("rev-list", "--first-parent", "--reverse", gone, f"^{last}").split()
    pending = {key for key in keys if key in defined_at(last, built=False)}
    found = {}
    for sha in commits:
        if not pending:
            break
        now = defined_at(sha, built=False)
        for key in [key for key in pending if key not in now]:
            found[key] = sha
            pending.discard(key)
    return found


def touching_subjects(name: str, sha: str) -> list[str]:
    """Return subjects of the commits a merge brought in that added or removed a definition line for name."""
    parents = git("rev-list", "--parents", "-n", "1", sha).split()[1:]
    if len(parents) < 2:
        return []
    pattern = rf"^[[:space:]]+{re.escape(name)}:[[:space:]]*$"
    out = git(
        "log",
        "--format=%s",
        "-G",
        pattern,
        f"{parents[0]}..{parents[1]}",
        "--",
        *SOURCE_DIRS,
    )
    return [line for line in out.splitlines() if line]


@click.command()
@click.option(
    "--ref",
    default="origin/main",
    show_default=True,
    help="The revision treated as the current schema.",
)
@click.option(
    "--output",
    "-o",
    type=click.Path(path_type=Path),
    required=True,
    help="TSV file to write.",
)
def main(ref: str, output: Path) -> None:
    """Write a TSV of elements defined at some release tag but not at REF."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    tags = [
        t
        for t in git("tag", "--sort=creatordate", "--merged", ref).split()
        if blobs_at(t, built=True)
    ]
    seen: dict[Key, list[str]] = defaultdict(list)
    for tag in tags:
        found = defined_at(tag, built=True)
        for key in found:
            seen[key].append(tag)
        logger.info("%s\t%d", tag, len(found))
    current = current_inventory(ref)
    recorded: set[Key] = set()
    for path, blob in blobs_at(ref, built=False):
        if path == DEPRECATED:
            recorded |= inventory_of_blob(blob)
    order = {tag: i for i, tag in enumerate(tags)}

    retired: dict[Key, tuple[str, str]] = {}
    for key, present in seen.items():
        if key not in current:
            last = present[-1]
            retired[key] = (
                last,
                tags[order[last] + 1] if order[last] + 1 < len(tags) else ref,
            )
    # The search for the removing commit starts at the last tag whose source still defined
    # the element. That can be earlier than the last tag that defined it at all, because
    # built files are regenerated only at release.
    by_interval: dict[tuple[str, str], set[Key]] = defaultdict(set)
    for key, (last, gone) in retired.items():
        in_source = [t for t in seen[key] if key in defined_at(t, built=False)]
        start = in_source[-1] if in_source else last
        if start != last:
            gone = tags[order[start] + 1]
        by_interval[(start, gone)].add(key)
    commit_of: dict[Key, str] = {}
    for (last, gone), keys in sorted(
        by_interval.items(), key=lambda item: order[item[0][0]]
    ):
        commit_of |= removal_commits(keys, last, gone)
        logger.info(
            "%s..%s: %d retired, %d attributed",
            last,
            gone,
            len(keys),
            sum(k in commit_of for k in keys),
        )

    by_normal: dict[str, list[str]] = defaultdict(list)
    enums_with_value: dict[str, list[str]] = defaultdict(list)
    for kind, enum, name in sorted(current):
        if kind == "permissible_values":
            enums_with_value[name].append(enum)
        else:
            by_normal[normalize(name)].append(f"{kind}:{name}")

    rows = []
    for key in sorted(retired):
        kind, enum, name = key
        last, gone = retired[key]
        present = seen[key]
        sha = commit_of.get(key, "")
        subject = git("log", "-1", "--format=%s", sha).strip() if sha else ""
        pr = PR_NUMBER.search(subject)
        subjects = (
            touching_subjects(name, sha) if sha and kind != "permissible_values" else []
        )
        rows.append(
            {
                "kind": kind,
                "enum": enum,
                "name": name,
                "first_tag": present[0],
                "last_tag": last,
                "first_tag_without": gone,
                "absent_at_tags_between": " ".join(
                    t for t in tags[order[present[0]] : order[last]] if t not in present
                ),
                "same_name_ignoring_case_now": " ".join(
                    by_normal.get(normalize(name), [])
                )
                if kind != "permissible_values"
                else "",
                "value_now_in_enums": " ".join(enums_with_value.get(name, []))
                if kind == "permissible_values"
                else "",
                "in_deprecated_yaml": "yes" if key in recorded else "",
                "removed_by_commit": sha[:9],
                "pr": (pr.group(1) or pr.group(2)) if pr else "",
                "merge_subject": subject,
                "commit_subjects": " | ".join(subjects),
            }
        )
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="") as fh:
        writer = csv.DictWriter(
            fh, fieldnames=list(rows[0]) if rows else ["kind"], delimiter="\t"
        )
        writer.writeheader()
        writer.writerows(rows)
    logger.info("wrote %d rows to %s", len(rows), output)


if __name__ == "__main__":
    main()
