#!/usr/bin/env python3
"""
Script to run a specific migrator against a MongoDB database using PyMongo.

Usage:
    python run_migrator.py migrator_from_11_9_1_to_11_10_0 [commit|rollback] [--host localhost] [--port 27022] [--database nmdc]
    
Arguments:
    migrator_name - Name of the migrator to run
    action - Either 'commit' to save changes or 'rollback' to discard them (default: rollback)
    
Environment variables (loaded from .env file if present):
    MONGO_HOST - MongoDB host (default: localhost)
    MONGO_PORT - MongoDB port (default: 27022)
    MONGO_DB - MongoDB database name (default: nmdc)
    MONGO_USERNAME - MongoDB username
    MONGO_PASSWORD - MongoDB password
    MONGO_AUTH_DB - Authentication database name
"""
import importlib

import click
import sys
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from nmdc_schema.migrators.adapters.mongo_adapter import MongoAdapter

# TODO: Is this script somewhat redundant with nmdc_schema/migration_recursion.py? Can they be
#       consolidated?

# Load environment variables from .env file if it exists
load_dotenv()


@click.command()
@click.argument("migrator", required=True)
@click.argument("action", required=False, default="rollback", type=click.Choice(["commit", "rollback"]))
@click.option("--host", default=lambda: os.getenv("MONGO_HOST", "localhost"), help="MongoDB host (default: from MONGO_HOST env var or localhost)")
@click.option("--port", default=lambda: int(os.getenv("MONGO_PORT", "27022")), type=int, help="MongoDB port (default: from MONGO_PORT env var or 27022)")
@click.option("--database", default=lambda: os.getenv("MONGO_DB", "nmdc"), help="MongoDB database name (default: from MONGO_DB env var or nmdc)")
@click.option("--auth-db", default=lambda: os.getenv("MONGO_AUTH_DB"), help="Authentication database name (default: from MONGO_AUTH_DB env var)")
@click.option("--username", default=lambda: os.getenv("MONGO_USERNAME"), help="MongoDB username (default: from MONGO_USERNAME env var)")
@click.option("--password", default=lambda: os.getenv("MONGO_PASSWORD"), help="MongoDB password (default: from MONGO_PASSWORD env var)")
def run_migrator(migrator, action, host, port, database, auth_db, username, password):
    """Run a specific migrator against MongoDB using PyMongo.
    
    MIGRATOR should the fully qualified module name for module containing a Migrator class
    ACTION should be either 'commit' to save changes or 'rollback' to discard changes (default: rollback).
    """
    
    # Construct MongoDB connection string for PyMongo
    if username and password:
        connection_string = f"mongodb://{username}:{password}@{host}:{port}/"
        params = []
        if auth_db:
            params.append(f"authSource={auth_db}")
        # Add replica set and direct connection for Docker environments
        params.append("replicaSet=rs0")
        params.append("directConnection=true")
        if params:
            connection_string += "?" + "&".join(params)
    else:
        connection_string = f"mongodb://{host}:{port}/?replicaSet=rs0&directConnection=true"
    
    commit_changes = action == "commit"
    
    click.echo(f"Running migrator: {migrator}")
    click.echo(f"Action: {action.upper()} (changes will {'be saved' if commit_changes else 'be discarded'})")
    click.echo(f"MongoDB connection: {host}:{port}/{database}")
    
    # Get the migrator class
    migrator_module = importlib.import_module(migrator)
    migrator_class = getattr(migrator_module, "Migrator")
    
    # Connect to MongoDB using PyMongo
    try:
        client = MongoClient(connection_string)
        # Test the connection
        client.admin.command('ping')
        db = client[database]
    except Exception as e:
        click.echo(f"Error: Could not connect to MongoDB: {e}", err=True)
        sys.exit(1)
    
    # Create adapter and migrator
    try:
        adapter = MongoAdapter(database=db)
        migrator = migrator_class(adapter=adapter)
        
        # Run the migration
        migrator.upgrade(commit_changes=commit_changes)
        click.echo("Migration completed successfully!")
        
    except Exception as e:
        click.echo(f"Migration failed: {e}", err=True)
        raise
    finally:
        if 'client' in locals():
            client.close()


if __name__ == "__main__":
    run_migrator()