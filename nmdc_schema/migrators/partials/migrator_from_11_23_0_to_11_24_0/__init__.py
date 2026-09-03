from typing import List, Type

from nmdc_schema.migrators.migrator_base import MigratorBase
from nmdc_schema.migrators.partials.migrator_from_11_23_0_to_11_24_0 import (
    migrator_from_11_23_0_to_11_24_0_part_1,
    migrator_from_11_23_0_to_11_24_0_part_2,
    migrator_from_11_23_0_to_11_24_0_part_3,
    migrator_from_11_23_0_to_11_24_0_part_4,
)


def get_migrator_classes() -> List[Type[MigratorBase]]:
    r"""
    Returns a list of migrator classes in the order in which they (i.e. their `upgrade` methods)
    were designed to be run.

    Part 1 removes `principal_investigator` (copying it onto DataGeneration
    `has_credit_associations` first). Part 2 standardizes remaining
    `PersonValue.orcid` values, including those copied in part 1. Part 3 copies
    `has_raw_value` onto missing `PersonValue.name` so name can be required.
    Part 4 removes the deprecated `collection_date_inc` slot from Biosample; it
    is independent of parts 1 through 3.

    >>> migrator_classes = get_migrator_classes()
    >>> type(migrator_classes) is list and len(migrator_classes) > 0  # the function returns a list
    True
    >>> from inspect import isclass
    >>> all(isclass(c) for c in migrator_classes)  # each list item is a class
    True
    >>> all(callable(getattr(c, "upgrade")) for c in migrator_classes)  # each class has an `upgrade` method
    True
    """

    return [
        migrator_from_11_23_0_to_11_24_0_part_1.Migrator,
        migrator_from_11_23_0_to_11_24_0_part_2.Migrator,
        migrator_from_11_23_0_to_11_24_0_part_3.Migrator,
        migrator_from_11_23_0_to_11_24_0_part_4.Migrator,
    ]
