from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

setup(
    name="nmdc_schema",
    url="https://github.com/microbiomedata/nmdc-schema",
    # packages=find_packages(),
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    packages=["nmdc_schema"],
    include_package_data=True,
    package_data={"nmdc_schema": ["nmdc.schema.json"]},
    # version="2021.04.13rc11",
    author="Bill Duncan",
    author_email="wdduncan@gmail.com",
    description="National Microbiome Data Collaborative (NMDC) Schema",
    # long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
    ],
    install_requires=["linkml"],
    python_requires=">=3.7",
    keywords="NMDC, schema",
)
