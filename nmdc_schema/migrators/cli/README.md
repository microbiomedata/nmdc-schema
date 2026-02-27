# CLI

This directory contains a command-line tool — and supporting files — that can be used to create a migrator.

- `create_migrator.py`: A click program that generates a migrator based upon a template and some user input 
- `migrator.py.template`: The migrator template (containing variables prefixed with `$`)
- `run_migrator.py`: A click program that runs a migrator specified by the user.  This can also be run with the make
    command `make run-migrator [migrator-name]`.
