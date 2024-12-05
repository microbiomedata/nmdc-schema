from typing import List, Type

from nmdc_schema.migrators.migrator_base import MigratorBase
from nmdc_schema.migrators.partials.migrator_from_11_1_0_to_11_2_0 import (
    migrator_from_11_1_0_to_11_2_0_part_1,
    migrator_from_11_1_0_to_11_2_0_part_2,
)


def get_migrator_classes() -> List[Type[MigratorBase]]:
    r"""
    Returns a list of migrator classes in the order in which they (i.e. their `upgrade` methods)
    were designed to be run.

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
        migrator_from_11_1_0_to_11_2_0_part_1.Migrator,
        migrator_from_11_1_0_to_11_2_0_part_2.Migrator,
    ]