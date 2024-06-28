from typing import List, Type

# TODO: Import all partials within a single `from` block.

from nmdc_schema.migrators.migrator_base import MigratorBase
from nmdc_schema.migrators.partials.migrator_from_10_2_0_to_11_0_0 import (
    migrator_from_10_2_0_to_11_0_0_part_01,
)
from nmdc_schema.migrators.partials.migrator_from_10_2_0_to_11_0_0 import (
    migrator_from_10_2_0_to_11_0_0_part_02,
)
from nmdc_schema.migrators.partials.migrator_from_10_2_0_to_11_0_0 import (
    migrator_from_10_2_0_to_11_0_0_part_03,
)
from nmdc_schema.migrators.partials.migrator_from_10_2_0_to_11_0_0 import (
    migrator_from_10_2_0_to_11_0_0_part_04,
)
from nmdc_schema.migrators.partials.migrator_from_10_2_0_to_11_0_0 import (
    migrator_from_10_2_0_to_11_0_0_part_05,
)
from nmdc_schema.migrators.partials.migrator_from_10_2_0_to_11_0_0 import (
    migrator_from_10_2_0_to_11_0_0_part_06,
)
from nmdc_schema.migrators.partials.migrator_from_10_2_0_to_11_0_0 import (
    migrator_from_10_2_0_to_11_0_0_part_07,
)
from nmdc_schema.migrators.partials.migrator_from_10_2_0_to_11_0_0 import (
    migrator_from_10_2_0_to_11_0_0_part_08,
)
from nmdc_schema.migrators.partials.migrator_from_10_2_0_to_11_0_0 import (
    migrator_from_10_2_0_to_11_0_0_part_09,
)
from nmdc_schema.migrators.partials.migrator_from_10_2_0_to_11_0_0 import (
    migrator_from_10_2_0_to_11_0_0_part_10,
)
from nmdc_schema.migrators.partials.migrator_from_10_2_0_to_11_0_0 import (
    migrator_from_10_2_0_to_11_0_0_part_11,
)
from nmdc_schema.migrators.partials.migrator_from_10_2_0_to_11_0_0 import (
    migrator_from_10_2_0_to_11_0_0_part_12,
)
from nmdc_schema.migrators.partials.migrator_from_10_2_0_to_11_0_0 import (
    migrator_from_10_2_0_to_11_0_0_part_13,
)
from nmdc_schema.migrators.partials.migrator_from_10_2_0_to_11_0_0 import (
    migrator_from_10_2_0_to_11_0_0_part_14,
)
from nmdc_schema.migrators.partials.migrator_from_10_2_0_to_11_0_0 import (
    migrator_from_10_2_0_to_11_0_0_part_15,
)
from nmdc_schema.migrators.partials.migrator_from_10_2_0_to_11_0_0 import (
    migrator_from_10_2_0_to_11_0_0_part_16,
)


def get_migrator_classes() -> List[Type[MigratorBase]]:
    r"""
    Returns a list of migrator classes in the order in which they (i.e. their `upgrade` methods)
    were designed to be run.

    >>> migrator_classes = get_migrator_classes()
    >>> type(migrator_classes) is list and len(migrator_classes) > 0  # the function returns a list
    True
    >>> from inspect import isclass
    >>> all(isclass(c) for c in migrator_classes)  # each list item is a classes
    True
    >>> all(callable(getattr(c, "upgrade")) for c in migrator_classes)  # each class has an `upgrade` method
    True
    """

    return [
        migrator_from_10_2_0_to_11_0_0_part_01.Migrator,
        migrator_from_10_2_0_to_11_0_0_part_02.Migrator,
        migrator_from_10_2_0_to_11_0_0_part_03.Migrator,
        migrator_from_10_2_0_to_11_0_0_part_04.Migrator,
        migrator_from_10_2_0_to_11_0_0_part_05.Migrator,
        migrator_from_10_2_0_to_11_0_0_part_06.Migrator,
        migrator_from_10_2_0_to_11_0_0_part_07.Migrator,
        migrator_from_10_2_0_to_11_0_0_part_08.Migrator,
        migrator_from_10_2_0_to_11_0_0_part_09.Migrator,
        migrator_from_10_2_0_to_11_0_0_part_10.Migrator,
        migrator_from_10_2_0_to_11_0_0_part_11.Migrator,
        migrator_from_10_2_0_to_11_0_0_part_12.Migrator,
        migrator_from_10_2_0_to_11_0_0_part_13.Migrator,
        migrator_from_10_2_0_to_11_0_0_part_14.Migrator,
        migrator_from_10_2_0_to_11_0_0_part_15.Migrator,
        migrator_from_10_2_0_to_11_0_0_part_16.Migrator,
    ]
