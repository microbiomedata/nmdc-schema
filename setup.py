from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

setup(
    name="nmdc_schema",
    url="https://github.com/microbiomedata/nmdc-schema",
    # set version manually when testing
    # version="2021.04.16a1",
    # use use_scm_version when version is set by github release action
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    packages=["nmdc_schema"],  # set package manually
    package_data={
        "nmdc_schema": ["nmdc.schema.json", "gold-to-mixs.sssom.tsv", "*.yaml"]
    },
    author="Bill Duncan",
    author_email="wdduncan@gmail.com",
    license="CC0 1.0 Universal",
    description="Schema resources for the National Microbiome Data Collaborative (NMDC)",
    entry_points={
        "console_scripts": [
            "validate-nmdc-json=nmdc_schema.validate_nmdc_json:cli",
            "fetch-nmdc-schema=nmdc_schema.nmdc_data:get_nmdc_jsonschema",
            "nmdc-version=nmdc_schema.nmdc_version:cli",
            "nmdc-data=nmdc_schema.nmdc_data:cli",
        ]
    },
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3 :: Only",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
    ],
    install_requires=["linkml"],
    python_requires=">=3.7",
    keywords="NMDC, schema",
)
