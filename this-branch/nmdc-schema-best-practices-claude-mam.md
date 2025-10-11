# NMDC-Schema Best Practices Guide

## Code Style and Organization

1. **Python Style Guidelines**
    - Follow PEP8 conventions and Black formatting
    - Use snake_case for variables/functions, PascalCase for classes
    - Type annotations required for all parameters and returns
    - Organize imports: stdlib first, third-party next, local modules last
    - Docstrings use triple double quotes with examples
    - Use specific exception handling with descriptive messages
    - Use pathlib for file operations instead of os.path
    - Write verbose, descriptive variable and function names
    - Use None return values to indicate absence of a result

2. **File Organization**
    - Use underscores to delimit file names
    - Use hyphens to delimit CLI alias names
    - Input and output files should use hyphens as delimiters
    - Output should go in assets directory unless it's very large or likely to change independently of the schema
    - Source schema files should be in src/schema/
    - Custom documentation goes in src/docs/

3. **Repository Structure**
    - Organize scripts by functionality
    - Maintain clear separations between tools, utilities, and core code
    - Use consistent file and directory naming
    - Place tools in appropriate locations (src/scripts for utilities)

## Schema Development

1. **Naming Conventions**
    - Standard LinkML naming conventions should be followed (UpperCamelCase for classes and enums, snake_case for slots)
    - Know how to use the LinkML linter to check style and conventions
    - Names for classes should be nouns or noun-phrases: Person, SequenceAlignment, Annotation
    - Spell out abbreviations and short forms, except for common terms (e.g. DNA)
    - Elements imported from outside need not follow the same naming conventions
    - Multivalued slots should be named as plurals
    - Older elements may be "grandfathered in"

2. **Class and Slot Design**
    - Document all model elements with descriptions and textual annotations
    - Include examples and counter-examples for all schema elements
    - Use enums for categorical values (finite sets)
    - Reuse existing schema elements where appropriate
    - Place new classes under existing upper level classes
    - Follow ID patterning conventions
    - Use abstract classes to define shared behavior and attributes
    - Provide class_uri definitions for proper RDF representation
    - Define clear hierarchies with is_a relationships
    - Include aliases for alternative terms to aid discoverability

3. **ID and Naming Patterns**
    - Follow consistent ID patterns for each class type
    - Use structured_pattern syntax for defining ID patterns with typecodes
    - Specify clear naming formats in documentation
    - Identifiers should be permanent, unique, resolvable, and opaque
    - Use CURIEs (prefixed identifiers) following W3C specification
    - Register all prefixes with at least one standard identifier prefix system

4. **Slot Definitions**
    - Document slot usage with description and notes
    - Use structured patterns for slot values when appropriate
    - Restrict values to appropriate ranges and types
    - Document required slots explicitly
    - Multivalued slots with class ranges must be inlined as lists when they lack identifiers

5. **Schema Structural Integrity**
    - All classes must assert a class_uri
    - Classes must use the type slot for consistent typing
    - Inherited slots should not be reiterated in child classes
    - JSON Schema artifacts must compile with fastjsonschema
    - Follow proper inheritance patterns without duplication
    - Use consistent URI patterns for classes
    - Maintain proper type handling across the schema

6. **Deprecation Practices**
    - Follow the two-step deprecation process
    - Include replacements with deprecated_element_has_exact_replacement
    - Document deprecation with dates and issue references
    - Move deprecated elements to deprecated.yaml file

7. **Enum Usage**
    - Create enums for categorical values
    - Include descriptions and meanings (ontology references) for enum values
    - Use aliases to support alternative terms

8. **Schema Integration**
    - Integrate with external resources (MIxS, EnvO, CHEBI)
    - Document mappings to external ontologies
    - Enforce prefix definitions for all CURIEs
    - Create utilities for identifier validation

## Development Practices

1. **CLI Development**
    - Scripts should have click CLIs
    - CLI parameters/options should be written with hyphens
    - CLI parameters/options should use consistent names
    - CLI entry points should be named 'main' or 'cli' unless there's a compelling reason otherwise
    - Use click and click_log for consistent CLI interfaces
    - Include help text for all parameters
    - Use proper validation callbacks for parameters
    - Follow CLI naming conventions (kebab-case for options)

2. **Makefile Standards**
    - Makefile targets should make use of $< for input and $@ for output
    - Scripts/aliases should be illustrated in a Makefile
    - The main Makefile should not be edited - make changes to project.Makefile instead
    - Use Make for generating artifacts and running tests
    - Define clear targets for common operations (clean, build, test)

3. **Function Design**
    - Write small, focused functions that do one thing well
    - Use descriptive parameter names
    - Provide default values for optional parameters
    - Return appropriate values or None when appropriate
    - Make transformation functions pure and self-contained
    - Document input and output expectations
    - Include examples for each transformation

4. **Class Design**
    - Create utility classes for common operations
    - Use clear class and method names that describe their purpose
    - Implement proper encapsulation with appropriate access modifiers
    - Create a clear inheritance hierarchy
    - Use class variables for version information
    - Implement standard interfaces across classes
    - Document inheritance relationships

5. **Error Handling and Validation**
    - Validate inputs at function boundaries
    - Use Click's validation capabilities for CLI parameters
    - Include validation examples in docstrings
    - Log important operations at appropriate log levels
    - Document error conditions and edge cases
    - Include descriptive error messages
    - Validate inputs before processing
    - Implement clear error messages for validation issues
    - Use proper logging for script operations
    - Handle API errors gracefully with informative messages

6. **Documentation**
    - Include docstrings with examples
    - Document classes with tooltips and annotations
    - Reference issues in code comments and documentation
    - Use TODO markers for future enhancements
    - Document the purpose and intent of schema elements
    - Explain relationships between classes and their hierarchies
    - Document identifier patterns and URI/CURIE usage
    - Include thorough comments in workflow files

7. **Testing Practices**
    - Write comprehensive unit tests for adapters/migrators
    - Use setUp and tearDown methods to prepare and clean test environments
    - Document test execution instructions
    - Structure tests with clear Setup/Execute/Validate phases
    - Test both successful operations and error cases
    - Include doctests for core functionality
    - Write test cases for edge cases
    - Use assertions to validate function behavior
    - Organize tests by schema feature or requirement
    - Use clear test names that describe what's being tested
    - Provide meaningful error messages that describe the failure
    - Run tests across multiple Python versions

8. **Resource Management**
    - Use context managers for file operations
    - Handle cleanup of resources properly
    - Use proper streaming for large files
    - Define constants for common file paths and URLs
    - Use pathlib for platform-independent file operations
    - Implement proper cleanup and resource handling
    - Define clear paths for output files

## Migration and Schema Evolution

1. **Migration Patterns**
    - Create consistent version-to-version migration classes
    - Document the purpose of each migration clearly
    - Implement the upgrade method consistently for all migrators
    - Break complex migrations into smaller, focused methods
    - Use descriptive method names for migration operations
    - Organize migrations by version pairs
    - Separate migration logic into transformation functions
    - Use helper methods for common operations
    - Keep migrations isolated and independent

2. **Version Management**
    - Follow semantic versioning principles
    - Major version for breaking changes
    - Minor version for new functionality
    - Patch version for non-functional changes
    - Maintain clear version identification
    - Document version transitions
    - Use consistent version number format
    - Create upgrade paths between adjacent versions
    - Use poetry-dynamic-versioning for version management

3. **Release Process**
    - Generate artifacts before release
    - Update version using semantic versioning
    - Create GitHub releases with proper documentation
    - Maintain changelog with clear descriptions
    - Automate PyPI publishing via GitHub Actions
    - Use make commands to generate artifacts
    - Run tests before publishing

4. **Adapter Pattern**
    - Use the adapter pattern to abstract database operations
    - Define clear interfaces for adapters with abstract methods
    - Implement specific adapters for different storage backends
    - Use callbacks for extensible behavior

5. **Callback Systems**
    - Use callback functions for extensibility
    - Document callback parameters and usage
    - Make callbacks optional with sensible defaults
    - Provide clear interfaces for callback registration

6. **Database Interaction**
    - Abstract database operations behind interfaces
    - Design for different backend support (MongoDB, Dictionary)
    - Implement CRUD operations consistently
    - Document collection and field naming conventions

## Collaboration and GitHub Practices

1. **GitHub Workflow**
    - Issues should be focused and actionable
    - Complex issues should be broken down into simpler issues
    - PRs should be atomic and aim to close a single issue
    - Never work on the main branch
    - Always create PR on a branch for transparency
    - Include migrations for breaking changes
    - PRs should reference issues following standard conventions
    - Test changes via CI/CD before merging
    - Always run the test suite on PRs

2. **Change Management**
    - Submit issues before making changes
    - Create branches with issue numbers
    - Create pull requests that reference issues
    - Delete branches after merging
    - Document breaking changes clearly
    - Create issues for broken documentation links

3. **Documentation Updates**
    - Custom documentation goes in src/docs/
    - Documentation is auto-deployed via GitHub workflows
    - Don't manually edit the docs directory
    - Maintain comprehensive developer documentation
    - Create FAQs for common development tasks
    - Document schema evolution and design decisions
    - Provide migration guides between versions
    - Check documentation links for breakage

4. **CI/CD Practices**
    - Use GitHub Actions for automated testing and deployment
    - Maintain separate workflows for testing, publishing, and documentation
    - Test on multiple Python versions
    - Generate documentation automatically
    - Publish to PyPI automatically on release
    - Deploy documentation when merging to main
    - Check dependencies for vulnerabilities
    - Use environment isolation (Poetry) for reproducible builds
    - Run all tests and validations before merging PRs

5. **Dependency Management**
    - Use Poetry for dependency management
    - Specify exact versions for core dependencies
    - Use ranges for compatible dependencies
    - Lock dependencies for reproducible builds
    - Use compatible extras for optional features
    - Check dependencies during CI process
    - Maintain Python version compatibility

## Data Validation and Schema Interaction

1. **Validation Standards**
    - Validate data using LinkML tools
    - Data producers should validate their data
    - Use Python data classes from nmdc-schema package instead of generating dicts/JSON manually
    - JSON Schema must be compatible with multiple validation libraries
    - Schema definitions must be properly materialized
    - Schema must support proper validation with key libraries
    - Check documents against schema before submission

2. **Schema Access and Manipulation**
    - Use LinkML's SchemaView for programmatic schema access
    - Apply ordered iteration over schema elements
    - Access induced classes and slots properly
    - Check relationships between schema elements
    - Use SchemaView for programmatic access to schema
    - Abstract common schema operations into reusable functions
    - Handle schema variants appropriately

3. **Resource Access Patterns**
    - Schema resources should be accessible through standardized getter methods
    - Schema views should be properly initialized
    - Access YAML and JSON representations consistently
    - Provide proper type conversions (bytes, strings, dictionaries)
    - Use package resources rather than file paths

4. **Schema Analysis and Validation Tools**
    - Create tools to identify unused schema elements
    - Implement pattern linting for schema quality
    - Build reports for subset usage and element coverage
    - Create utilities to scrutinize schema elements
    - Run validation during CI process

5. **API Client Development**
    - Design clean API interfaces with proper error handling
    - Implement pagination handling for large result sets
    - Use request parameters for filtering data
    - Provide clear documentation for API methods
    - Handle authentication and headers consistently

6. **Reporting and Analysis**
    - Build utilities for analyzing schema usage
    - Create tools for reporting relationships between elements
    - Implement validation reports for schema coverage
    - Design scripts for data extraction and transformation
    - Generate reports for schema compliance

7. **RDF and Semantic Web**
    - Generate RDF/OWL representations of the schema
    - Validate RDF for consistency
    - Use established ontology design patterns
    - Maintain SPARQL query examples
    - Test RDF serializations and transformations

## From `pyproject.toml`

1. Package Metadata and Configuration:
   - Provide detailed package metadata including description, documentation URL, homepage, keywords
   - Include license information explicitly
   - Specify repository URL for source code access
   - List all authors with contact information
   - Add appropriate classifiers for package categorization
   - Specify Python version compatibility with proper version specifiers
2. Dependency Management:
   - Pin exact versions for critical dependencies (e.g., linkml = "1.8.5")
   - Use compatible version ranges for stable dependencies (e.g., "^4")
   - Separate development dependencies from runtime dependencies
   - Add explanatory comments for dependencies that need context
   - Group dependencies by purpose (e.g., dev dependencies vs. main)
   - Identify dependencies that might need to move between groups
3. Package Structure:
   - Define explicit package includes with clear structure
   - Include subpackages with proper "from" specifications
   - Maintain nested package structure while keeping appropriate organization
4. Version Management:
   - Use poetry-dynamic-versioning for automated version management
   - Define substitution patterns for version updates
   - Specify version format style (pep440)
   - Include comments explaining how to properly use the versioning system
5. CLI Script Organization:
   - Register all CLI scripts in the poetry.scripts section
   - Use consistent naming conventions for script entry points
   - Map script names to their implementation functions
   - Provide descriptive comments for scripts that need explanation
6. Build System Configuration:
   - Specify build-system requirements explicitly
   - Configure the appropriate build backend
   - Include necessary build plugins

## Discussions summaries by ChatGPT

This document synthesizes proposals, decisions, and areas of dissent from all 24 discussions in the `nmdc-schema` GitHub
repository as of the current export.

## Chemical Entities and Molecular Data Modeling

- Use `ChemicalEntity` for solvents and reagents in `MaterialProcessing`.
- Avoid using `ChemicalEntity` for inferred compounds (metabolites, peptides); introduce a `MolecularData` class
  instead.
- Add support for identifiers like CAS, ChEBI, InChI, RefMet, and UniProt via normalization APIs.
- Apply node normalizer to populate MongoDB instances robustly.

## Integration of ReDU Metadata

- Map ReDU fields (e.g., YearOfAnalysis, SampleExtractionMethod) to structured NMDC schema classes.
- Recognize that ReDU's metadata is less complete and mostly optional compared to NMDC.
- Consider aliasing or mapping to ReDU fields for interoperability.

## Metaproteomics Schema Simplification

- Remove `PeptideQuantification` and `ProteinQuantification` classes and unused slots.
- Add `razor_protein` slot to `MetaproteomicsAnalysis` class.
- Align .tsv and MongoDB outputs to only include useful summary data.

## Sample Type and Environmental Metadata

- Use `sample_type` or `env_package` as required or derived fields.
- Automate population of `sample_type` from ENVO-based environmental triads.
- Harmonize use of `env_package` and `sample_type`, potentially both as enums.

## Schema Hygiene and Redundancy Cleanup

- Remove `core_field`, `environment_field`, etc. from `Biosample` unless used structurally.
- Use LinkML's `is_grouping_slot` or `slot_group` for logical grouping.

## EMSL Identifier Policy

- Remove unresolved EMSL identifiers and deprecated prefixes from MongoDB.
- Use `my_emsl:` formatted IDs where resolvable identifiers are needed.
- Retain some internal IDs for EMSL internal use, even if not resolvable externally.

## Submission Schema Split

- Move submission-only slots (e.g., `rna_volume`, `dna_absorb1`) to the `submission-schema` repo.
- Preserve mappings needed for JGI metadata templates and APIs.
- Coordinate slot definitions in TSV (`slots.tsv`, `classes.tsv`) for submission-specific usage.

## Instrument Metadata Representation

- Use structured `vendor` and `model` enums for instrument metadata instead of `instrument_name`.
- Preserve `instrument_name` for cases where 1:1 mapping to vendor/model breaks down.

## Typecode and Identifier Minting

- Document preferred typecodes for minting identifiers using LinkML metadata.
- Use `deprecated_element_has_exact_replacement` for typecode transitions.
- Recognize tension between human-readable and machine-resilient IDs.

## Lat/Lon Uncertainty Representation

- Consider adding `lat_uncertainty` and `lon_uncertainty` slots to Biosample.
- Weigh added precision vs complexity and limited data availability.

## Clarifying Data Linking Semantics

- `sample_linkage` does not always imply a GUID; design must support non-GUID values.
- Be explicit about linkage semantics and value formats.

## Slot Grouping Exhaustiveness

- When introducing new grouping subsets, ensure they are exhaustive or document gaps.
- Improve documentation for grouped slots (like sequencing fields).

## Unit and Term Mapping Guidance

- Ensure valid unit mappings (e.g., volume) use UCUM where appropriate.
- Create example term mappings for slots like `volume`, `temperature`, etc.

## Validation Example Best Practices

- Every class should have at least one valid and one invalid example file in `src/data`.
- Invalid examples must clearly explain which constraint is being violated.
- Avoid vague or empty invalid example files.

## Permissible Values and Descriptions

- Each enum value should include a `description` and/or `meaning`.
- Revisit and improve enum documentation across the schema.

## Modular Schema Maintenance

- Schema contributors should ensure each YAML module builds independently.
- Avoid circular imports between modules.
- LinkML linter should be run routinely before merges.

## Naming and Reusability

- Use descriptive names; avoid tautological slot or class descriptions.
- Encourage reuse of recently added slots and structures across modules.
