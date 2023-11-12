# Import "sub-packages" here that we want code that `import`s the `nmdc_schema` package to have access to.
#
# References:
# - https://py-pkgs.org/04-package-structure.html#the-init-file (about the `__init__.py` file)
# - https://github.com/python-poetry/poetry/issues/2270 (an issue regarding Poetry's support for sub-packages)
#
from nmdc_schema import migrators
