# Import "sub-packages" here that we want code that `import`s the `nmdc_schema` package to have access to.
#
# References:
# - https://py-pkgs.org/04-package-structure.html#the-init-file (about the `__init__.py` file)
# - https://github.com/python-poetry/poetry/issues/2270 (an issue regarding Poetry's support for sub-packages)
#
from nmdc_schema.migrators import (
    migrator_from_7_7_2_to_7_8_0,
    migrator_from_7_8_0_to_8_0_0,
    migrator_from_8_0_to_8_1,
    migrator_from_8_1_to_9_0
)
