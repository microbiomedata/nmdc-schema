#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# nmdc_schema/assets/mongodb_queries/referential_integrity_check.py
"""
This module contains the MongoDB queries for checking referential integrity.
"""
import click
import logging
import os
from pymongo import MongoClient

@click.group()
@click.argument("mongo_uri", type=str)
@click.pass_context
def cli(ctx, mongo_uri):
    ctx.ensure_object(dict)
    ctx.obj["MONGO_URI"] = mongo_uri

@cli.command()
@click.pass_context
def referential_integrity(ctx):
    """
    Check referential integrity of slots in the MongoDB database using the queries in
    in nmdb_schema/assets/mongodb_queries/data_qc.

    Check for referential integrity of the following slots:
        - part_of
        - has_input
        - has_output
        - was_informed_by
        - metagenome_annotation_id

    Write a report to a file.
    """
    logging.basicConfig(level=logging.INFO)

    mongo_uri = ctx.obj["MONGO_URI"]
    client = MongoClient(mongo_uri, directConnection=True)
    try:
        db = client["nmdc"]
        # iterate over query files
        query_dir = os.path.join(os.path.dirname(__file__), "data_qc")
        for query_file in os.listdir(query_dir):
            if query_file.endswith(".js"):
                query_name = os.path.splitext(query_file)[0]
                logging.info(f"Running query: {query_name}")
                with open(os.path.join(query_dir, query_file), "r") as f:
                    query = f.read()
                result = db.command("aggregate", query, explain=True)
                logging.info(f"Result: {result}")
    finally:
        client.close()
    client.close()


if __name__ == "__main__":
    cli(obj={})