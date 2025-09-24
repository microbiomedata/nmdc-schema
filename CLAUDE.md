# Poetry Entry Point Diagnostics

## Diagnostic Commands for Poetry Entry Point Issues

When `poetry run <command>` says "Command not found" but the package is installed:

### 1. Check if package is installed
```bash
poetry show | grep <package-name>
```

### 2. Check if script exists in venv
```bash
ls -la .venv/bin/ | grep <command-name>
```

### 3. Check if entry points are registered
```bash
poetry run python -c "import pkg_resources; [print(f'{ep.name}: {ep.module_name}:{ep.attrs[0]}') for ep in pkg_resources.iter_entry_points('console_scripts') if '<command>' in ep.name]"
```

### 4. Verify entry points in package metadata
```bash
find .venv/lib/python*/site-packages/<package>*.dist-info/ -name "entry_points.txt" -exec cat {} \;
```

## Solutions (in order of preference)

### 1. Force reinstall specific package
```bash
poetry run pip uninstall <package-name> -y && poetry install
```

### 2. Force reinstall all dependencies
```bash
poetry install --force
```

### 3. Rebuild entire environment
```bash
poetry env remove
poetry install
```

## Prevention

- Run `poetry check` periodically to catch configuration issues
- Avoid mixing `pip install` and `poetry install` in the same environment
- Consider using `poetry shell` instead of `poetry run` for interactive work

## Test Commands

Essential commands that should work in this project:
- `poetry run do_shuttle --help` (from sheets-and-friends)
- `poetry run gen-linkml --help` (from linkml)
- `poetry run gen-pydantic --help` (from linkml)

If any of these fail with "Command not found", use the diagnostic steps above.