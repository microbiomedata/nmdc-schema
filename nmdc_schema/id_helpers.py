r"""
This module contains helper functions related to schema element identifiers.
"""

import re
from typing import List, Optional

from nmdc_schema.get_nmdc_view import ViewGetter


def get_compatible_typecodes(slot_pattern: str) -> List[str]:
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

    >>> get_compatible_typecodes("(nmdc):foo-...")
    []
    >>> get_compatible_typecodes("^(nmdc):foo-...")
    ['foo']
    >>> get_compatible_typecodes("^(nmdc):(foo|bar)-...")
    ['foo', 'bar']
    >>> get_compatible_typecodes("^(nmdc):(foo|bar|baz)-...")
    ['foo', 'bar', 'baz']
    """
    typecodes: List[str] = []

    # Make a regular expression that can be used to extract the typecode portion of a slot pattern.
    #
    # Examples:
    # - "^(nmdc):foo-..."           → "foo"
    # - "^(nmdc):(foo|bar|baz)-..." → "(foo|bar|baz)"
    #
    # Note: The `+?` is a lazy matcher (opposite of greedy). If we did a greedy match here, the capture group would
    #       consume all but the final hyphen in the slot pattern. By doing a lazy match, we prevent the capture
    #       group from consuming any hyphens at all.
    #
    id_pattern = re.compile(r"^\^\(nmdc\):(.+?)-")

    # Use the regular expression to extract the typecode portion of the specified slot pattern.
    match_obj = id_pattern.match(slot_pattern)
    if match_obj is not None:
        typecode_portion = match_obj.group(1)

        # Extract the typecode from a single-typecode pattern, or extract all typecodes from a multi-typecode pattern.
        if "(" not in typecode_portion:
            # Example: "foo" → ["foo"]
            typecodes = [typecode_portion]
        else:
            # Example: "(foo|bar|baz)" → ["foo", "bar", "baz"]
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
    compatible_typecodes = get_compatible_typecodes(slot_pattern)
    return compatible_typecodes[0] if len(compatible_typecodes) > 0 else None


def get_class_name_to_typecode_map() -> dict[str, list[str]]:
    r"""
    Returns a dictionary in which each key is the name of a schema class and each value is a list of all the typecodes
    compatible with the `id` slot of that class.

    >>> d = get_class_name_to_typecode_map()
    >>> isinstance(d, dict)  # returns a dict
    True
    >>> all(isinstance(k, str) for k in d.keys())  # all dict keys are strings
    True
    >>> all(isinstance(v, list) for v in d.values())  # all dict values are lists
    True
    >>> "NamedThing" in d  # schema class lacking an `id` field compatible with any typecodes
    True
    >>> d["NamedThing"]
    []
    >>> "Biosample" in d  # schema class having an `id` field compatible with one typecode
    True
    >>> d["Biosample"]
    ['bsm']
    >>> "MassSpectrometry" in d  # schema class having an `id` field compatible with multiple typecodes
    True
    >>> sorted(d["MassSpectrometry"])
    ['dgms', 'omprc']
    """

    # Make a dictionary in which each key is the name of a schema class and each value is the definition of that class.
    view_getter = ViewGetter()
    schema_view = view_getter.get_view()
    class_definitions_by_class_name = schema_view.all_classes()

    # Make a dictionary in which each key is the name of a schema class and each value is a list of all the typecodes
    # compatible with the `id` slot of that class.
    class_name_to_typecodes_map = dict()
    for class_name, class_definition in class_definitions_by_class_name.items():

        # Ensure this class name appears in the resulting dictionary, regardless of whether its `id` slot is compatible
        # with any typecodes. That way, all class names end up in the resulting dictionary.
        if class_name not in class_name_to_typecodes_map:
            class_name_to_typecodes_map[class_name] = list()

        # Determine whether the `id` slot of this class is compatible with any typecodes and, if it is, add them to the
        # list.
        slot_definitions_for_class = schema_view.class_induced_slots(class_name)
        for slot_definition in slot_definitions_for_class:
            if slot_definition.name == "id":
                if slot_definition.pattern is not None:
                    compatible_typecodes = get_compatible_typecodes(slot_definition.pattern)
                    class_name_to_typecodes_map[class_name].extend(compatible_typecodes)

    return class_name_to_typecodes_map
