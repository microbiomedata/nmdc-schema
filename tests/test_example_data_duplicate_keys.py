"""Fail on example data files that repeat a key in the same mapping.

PyYAML keeps only the last copy of a repeated key and drops the earlier ones
without a warning. In an example file that means part of the file is never
validated: a ``Database`` file with ``material_processing_set`` three times
validates only the third list, and a counter-example with a repeated slot may
pass or fail for a reason nobody intended.
"""

import collections

import pytest
import yaml

from tests import ROOT

DATA_FILES = sorted((ROOT / "src" / "data").rglob("*.yaml"))


class _DuplicateKeyLoader(yaml.SafeLoader):
    """SafeLoader that records repeated keys instead of silently keeping the last one."""

    duplicates: list[str]


def _construct_mapping(loader: _DuplicateKeyLoader, node: yaml.MappingNode, deep: bool = False) -> dict:
    counts = collections.Counter(str(loader.construct_object(key)) for key, _ in node.value)
    for key, count in counts.items():
        if count > 1:
            loader.duplicates.append(f"line {node.start_mark.line + 1}: {key!r} appears {count} times")
    return loader.construct_mapping(node, deep)


_DuplicateKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_mapping)


@pytest.mark.parametrize("path", DATA_FILES, ids=lambda p: str(p.relative_to(ROOT)))
def test_example_file_has_no_duplicate_keys(path):
    """Each mapping in an example file names each key once."""
    loader = _DuplicateKeyLoader(path.read_text())
    loader.duplicates = []
    try:
        loader.get_single_data()
    finally:
        loader.dispose()
    assert not loader.duplicates, "; ".join(loader.duplicates)
