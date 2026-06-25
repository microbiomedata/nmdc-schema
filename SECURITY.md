# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please report it responsibly.

**Do not open a public GitHub issue for security vulnerabilities.**

Instead, please use [GitHub private vulnerability reporting](https://github.com/microbiomedata/nmdc-schema/security/advisories/new) for this repository. If that is unavailable, please [email the NMDC team](https://microbiomedata.org/contact/) so they can review it privately.

## Scope

`nmdc-schema` is a schema-definition package: LinkML schema YAML, generated Pydantic and JSON Schema artifacts, and supporting Python utilities and data migrators. It is not a network service and does not handle authentication or untrusted request input. The realistic security surface is therefore:

- **Dependency vulnerabilities** in the Python and GitHub Actions dependencies (monitored by Dependabot and CodeQL).
- **Integrity of the published [`nmdc-schema` PyPI package](https://pypi.org/project/nmdc-schema/)**, which is built via PyPI trusted publishing from this repository.

## Supported Versions

Security fixes land in the latest release. Note that downstream consumers (for example `nmdc-runtime` and `nmdc-server`) pin a specific `nmdc-schema` version, so a fix in the latest release does not reach a production deployment until that consumer updates its pin. See [Releases](https://github.com/microbiomedata/nmdc-schema/releases) for the current version.

## Security Updates

Python dependencies are monitored by Dependabot, which opens pull requests to patch known vulnerabilities. CodeQL code scanning runs on the default branch and on pull requests, configured by [`.github/codeql/codeql-config.yml`](https://github.com/microbiomedata/nmdc-schema/blob/main/.github/codeql/codeql-config.yml).
