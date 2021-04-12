from setuptools import setup, find_packages

# with open("requirements/main.in") as f:
#     install_requires = f.read().splitlines()

# with open("requirements/dev.in") as f:
#     dev_requires = f.read().splitlines()

with open("README.md") as f:
    long_description = f.read()

setup(
    name="nmdc_schema",
    url="https://github.com/microbiomedata/nmdc-schema",
    packages=find_packages(),
    # packages=["python", "jsonschema"],
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    author="Bill Duncan",
    author_email="wdduncan@gmail.com",
    description="National Microbiome Data Collaborative (NMDC) Schema",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
    ],
    # install_requires=install_requires,
    # extras_require={
    #     "dev": dev_requires,
    # },
    python_requires=">=3.7",
    keywords="NMDC, schema",
)
