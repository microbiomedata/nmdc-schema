r"""
This module contains helper functions related to schema element identifiers.
"""

import re
from typing import List, Optional


def get_typecodes_compatible_with_existing_ids(slot_pattern: str) -> List[str]:
    r"""
    Returns the typecodes, if any, that the schema says values of the specified `id` field can contain.

    :param slot_pattern: The value of the `pattern` property of the `id` slot definition

    Note: We currently use the `pattern` property of the `id` slot for two different things: (a) to specify which
          typecode we want ID generators (e.g., instances of the NMDC ID Minter) to use when generating new identifiers
          (specifically, we want them to use only the _first_ typecode that occurs in the pattern), and (b) to specify
          which typecodes we want ID validators (e.g., instance of the NMDC Runtime) to allow identifiers of instances
          of that class to contain (they can contain _any_ one of the typecodes that occurs in the pattern). This
          function returns the list for "use (b)." Eventually, we may specify the above two things using separate
          schema elements.

    >>> get_typecodes_compatible_with_existing_ids("(nmdc):foo-...")
    []
    >>> get_typecodes_compatible_with_existing_ids("^(nmdc):foo-...")
    ['foo']
    >>> get_typecodes_compatible_with_existing_ids("^(nmdc):(foo|bar)-...")
    ['foo', 'bar']
    >>> get_typecodes_compatible_with_existing_ids("^(nmdc):(foo|bar|baz)-...")
    ['foo', 'bar', 'baz']
    """
    typecodes: List[str] = []

    id_pattern = re.compile(
        r"^\^\(nmdc\):(.+?)-"
    )  # the `+?` is a lazy matcher (opposite of greedy)
    match_obj = id_pattern.match(slot_pattern)
    if match_obj is not None:
        typecode_portion = match_obj.group(1)

        # Extract the typecode from a single-typecode pattern, or extract all typecodes from a multi-typecode pattern.
        if "(" not in typecode_portion:
            typecodes = [typecode_portion]
        else:
            typecodes = typecode_portion.lstrip("(").rstrip(")").split("|")

    return typecodes


def get_typecode_for_future_ids(slot_pattern: str) -> Optional[str]:
    r"""
    Returns the typecode, if any, that schema authors want future values of the specified `id` field to contain.

    :param slot_pattern: The value of the `pattern` property of the `id` slot definition

    >>> get_typecode_for_future_ids("(nmdc):foo-...") is None
    True
    >>> get_typecode_for_future_ids("^(nmdc):foo-...")
    'foo'
    >>> get_typecode_for_future_ids("^(nmdc):(foo|bar)-...")
    'foo'
    >>> get_typecode_for_future_ids("^(nmdc):(foo|bar|baz)-...")
    'foo'
    """
    compatible_typecodes = get_typecodes_compatible_with_existing_ids(slot_pattern)
    return compatible_typecodes[0] if len(compatible_typecodes) > 0 else None
