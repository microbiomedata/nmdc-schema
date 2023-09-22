#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A simple script to show how to retrieve the jsonschema from the nmdc-schema library.
"""
if __name__ == "__main__":
    from nmdc_schema.validate_nmdc_json import get_nmdc_schema
    from pprint import pprint

    jsonschema = get_nmdc_schema()
    pprint(jsonschema)
