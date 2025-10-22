# Schema Materialization and Dematerialization Guide

This document describes the methods used in the MIxS repository to materialize and dematerialize (normalize) the LinkML schema, particularly focusing on pattern materialization and the cleanup pipeline.

## Table of Contents

- [Overview](#overview)
- [Schema Materialization Methods](#schema-materialization-methods)
- [Schema Unmaterialization/Normalization Methods](#schema-unmaterializationnormalization-methods)
- [The yq Cleanup Pipeline](#the-yq-cleanup-pipeline)
- [Complete Workflow Pipeline](#complete-workflow-pipeline)
- [Key Concepts](#key-concepts)

## Overview

The MIxS repository maintains the source schema in `src/mixs/schema/mixs.yaml` and generates several derived versions in the `contrib/` directory. These derived versions serve different purposes in the build and analysis pipeline.

**Key Philosophy:** The repository treats `structured_pattern` as the canonical source of truth and `pattern` (regex) as a derived/materialized artifact.

## Schema Materialization Methods

### Pattern Materialization with `gen-linkml`

**Location:** Makefile:164-182

**Target:** `contrib/mixs-patterns-materialized.yaml`

**Command:**

```bash
$(RUN) gen-linkml \
    --format yaml \
    --materialize-patterns \
    --no-materialize-attributes $< |
[... followed by yq cleanup pipeline ...]
```

**Purpose:**

- Expands `structured_pattern` definitions into their equivalent `pattern` (regex) forms
- Creates a version of the schema where patterns are fully materialized for downstream tools that may not understand structured patterns

**Flags:**

- `--materialize-patterns` - Expands structured_patterns into regex patterns
- `--no-materialize-attributes` - Prevents expansion of attribute inheritance (keeps the schema compact)
- `--format yaml` - Outputs in YAML format

**Input:** `contrib/mixs-normalized-minimized.yaml`

**Output:** `contrib/mixs-patterns-materialized.yaml`

## Schema Unmaterialization/Normalization Methods

The repository uses several methods to undo or prevent materialization, maintaining the structured form of the schema.

### 1. Structured Patterns Preferred

**Location:** Makefile:139-141

**Target:** `contrib/mixs_structured_patterns_preferred.yaml`

**Command:**

```bash
yq '(.slots[] | select(has("structured_pattern") and has("pattern"))) |= del(.pattern)' $< > $@
```

**Purpose:**

- Removes materialized `pattern` fields from slots that have both `structured_pattern` and `pattern`
- Ensures the structured form takes precedence over the regex form

**Input:** `src/mixs/schema/mixs.yaml`

**Output:** `contrib/mixs_structured_patterns_preferred.yaml`

**How it works:**

1. Selects all slots that have both `structured_pattern` AND `pattern` fields
2. Deletes the `pattern` field from those slots
3. Preserves `structured_pattern` as the authoritative definition

### 2. Normalized-Minimized Generation

**Location:** Makefile:143-162

**Target:** `contrib/mixs-normalized-minimized.yaml`

**Command:**

```bash
$(RUN) linkml generate linkml \
    --format yaml \
    --no-mergeimports \
    --no-materialize-attributes \
    --no-materialize-patterns $< |
[... followed by yq cleanup pipeline ...]
```

**Purpose:**

- Generates a normalized version of the schema without any materialization
- Creates a clean, canonical representation suitable for analysis and comparison

**Flags:**

- `--no-mergeimports` - Keeps imports separate rather than merging them into a single file
- `--no-materialize-attributes` - Prevents expansion of attribute inheritance
- `--no-materialize-patterns` - **Prevents expansion of structured_patterns into regex patterns**
- `--format yaml` - Outputs in YAML format

**Input:** `contrib/mixs_structured_patterns_preferred.yaml`

**Output:** `contrib/mixs-normalized-minimized.yaml`

## The yq Cleanup Pipeline

Both the `normalized-minimized` and `patterns-materialized` targets use an identical series of yq transformations to clean up and simplify the generated schema. This pipeline runs after the LinkML generation step.

### Pipeline Steps

#### Step 1: Clean up `from_schema` references

**Location:** Makefile:150, 170

```bash
yq eval '(.. | select(has("from_schema")) | .from_schema) style="" | del(.. | select(has("from_schema")).from_schema)'
```

**What it does:**

- First sets the YAML style to empty string for any `from_schema` field
- Then deletes all `from_schema` fields throughout the entire schema

**Why:**

- `from_schema` indicates which schema a component was originally defined in
- This metadata is redundant in a single consolidated output file
- Removing it reduces file size and improves readability

#### Step 2: Simplify annotations in classes

**Location:** Makefile:151, 171

```bash
yq eval '.classes[] |= select(has("annotations")).annotations |= map_values(.value)'
```

**What it does:**

- Transforms class annotations from verbose format to simple format
- Only processes classes that actually have annotations

**Format transformation:**

```yaml
# Before (verbose)
annotations:
  example_tag:
    tag: example_tag
    value: actual_value

# After (simplified)
annotations:
  example_tag: actual_value
```

#### Step 3: Simplify prefixes

**Location:** Makefile:152, 172

```bash
yq eval '.prefixes |= map_values(.prefix_reference)'
```

**What it does:**

- Flattens prefix definitions from nested structure to simple key-value pairs

**Format transformation:**

```yaml
# Before
prefixes:
  schema:
    prefix_reference: "http://schema.org/"

# After
prefixes:
  schema: "http://schema.org/"
```

#### Step 4: Simplify settings

**Location:** Makefile:153, 173

```bash
yq eval '.settings |= map_values(.setting_value)'
```

**What it does:**

- Flattens settings from nested structure to simple key-value pairs

**Format transformation:**

```yaml
# Before
settings:
  setting_name:
    setting_value: value

# After
settings:
  setting_name: value
```

#### Step 5: Simplify annotations in slots

**Location:** Makefile:154, 174

```bash
yq eval '.slots[] |= select(has("annotations")).annotations |= map_values(.value)'
```

**What it does:**

- Same transformation as Step 2, but applied to slots instead of classes
- Only processes slots that have annotations

#### Step 6: Remove redundant class names

**Location:** Makefile:155, 175

```bash
yq eval 'del(.classes.[].name)'
```

**What it does:**

- Removes the `name` field from all class definitions

**Why:**

- In LinkML YAML, classes are stored as `classes: {ClassName: {name: ClassName, ...}}`
- The `name` field duplicates the key
- The key is sufficient for identifying the class

**Format transformation:**

```yaml
# Before
classes:
  Checklist:
    name: Checklist
    description: "..."

# After
classes:
  Checklist:
    description: "..."
```

#### Step 7: Remove redundant slot_usage names

**Location:** Makefile:156, 176

```bash
yq eval 'del(.classes.[].slot_usage.[].name)'
```

**What it does:**

- Removes the `name` field from all slot_usage entries

**Why:**

- Similar to class names - the slot name is already the key
- The `name` field is redundant

**Format transformation:**

```yaml
# Before
classes:
  SomeClass:
    slot_usage:
      some_slot:
        name: some_slot
        required: true

# After
classes:
  SomeClass:
    slot_usage:
      some_slot:
        required: true
```

#### Step 8: Remove redundant enum names

**Location:** Makefile:157, 177

```bash
yq eval 'del(.enums.[].name)'
```

**What it does:**

- Removes the `name` field from all enum definitions

**Why:**

- Enum names duplicate their keys, same pattern as classes

#### Step 9: Remove redundant permissible_values text

**Location:** Makefile:158, 178

```bash
yq eval 'del(.enums.[].permissible_values.[].text)'
```

**What it does:**

- Removes the `text` field from all permissible values in enums

**Why:**

- Permissible values are stored as `{value: {text: value, ...}}`
- The `text` field duplicates the key

**Format transformation:**

```yaml
# Before
enums:
  SomeEnum:
    permissible_values:
      option1:
        text: option1
        description: "..."

# After
enums:
  SomeEnum:
    permissible_values:
      option1:
        description: "..."
```

#### Step 10: Remove most domain specifications

**Location:** Makefile:159, 179

```bash
yq eval 'del(.slots[] | select(.domain != "MixsCompliantData") | .domain)'
```

**What it does:**

- Removes `domain` field from slots UNLESS the domain is "MixsCompliantData"
- Conditional deletion based on domain value

**Why:**

- Most domain specifications can be inferred from context or slot_usage
- `MixsCompliantData` domain is semantically significant and should be preserved
- Reduces redundancy while preserving important information

#### Step 11: Remove redundant slot names

**Location:** Makefile:160, 180

```bash
yq eval 'del(.slots.[].name)'
```

**What it does:**

- Removes the `name` field from all slot definitions

**Why:**

- Same pattern as classes and enums - names duplicate keys

#### Step 12: Remove source_file metadata

**Location:** Makefile:161, 181

```bash
yq eval 'del(.source_file)'
```

**What it does:**

- Removes the `source_file` field from the schema root

**Why:**

- `source_file` tracks where the schema was originally loaded from
- This metadata is not needed in the output artifact
- Improves portability of the generated file

#### Step 13: Remove redundant subset names

**Location:** Makefile:162, 182

```bash
yq eval 'del(.subsets.[].name)'
```

**What it does:**

- Removes the `name` field from all subset definitions

**Why:**

- Same pattern - subset names duplicate their keys

### Purpose of the yq Cleanup Pipeline

The yq cleanup pipeline serves multiple critical purposes:

1. **Size Reduction**
   
   - Removes redundant information to make files significantly smaller
   - Reduces version control diff noise
   - Improves git performance and storage efficiency

2. **Readability**
   
   - Makes the YAML more human-readable by removing verbose boilerplate
   - Easier to review changes in pull requests
   - Simpler for manual inspection and debugging

3. **Normalization**
   
   - Creates a consistent, canonical format across all artifacts
   - Makes schema comparison and diffing more reliable
   - Enables better analysis of schema changes over time

4. **Portability**
   
   - Removes context-specific metadata like `from_schema` and `source_file`
   - Makes artifacts more suitable for distribution and reuse
   - Reduces coupling to specific file system paths

5. **Semantic Preservation**
   
   - Despite extensive cleanup, all semantic information is preserved
   - Only redundant syntactic elements are removed
   - The resulting schema is functionally equivalent to the input

## Complete Workflow Pipeline

The complete materialization/dematerialization pipeline follows this sequence:

```
src/mixs/schema/mixs.yaml (SOURCE)
         |
         | (yq: remove pattern when structured_pattern exists)
         v
contrib/mixs_structured_patterns_preferred.yaml
         |
         | (linkml generate linkml --no-materialize-patterns + yq cleanup)
         v
contrib/mixs-normalized-minimized.yaml (UNMATERIALIZED)
         |
         | (gen-linkml --materialize-patterns + yq cleanup)
         v
contrib/mixs-patterns-materialized.yaml (MATERIALIZED)
```

### File Descriptions

- **`src/mixs/schema/mixs.yaml`**
  
  - Source of truth
  - Hand-edited by developers
  - May contain both `structured_pattern` and `pattern` fields

- **`contrib/mixs_structured_patterns_preferred.yaml`**
  
  - First cleanup step
  - Ensures `structured_pattern` takes precedence
  - Removes materialized `pattern` when `structured_pattern` exists

- **`contrib/mixs-normalized-minimized.yaml`**
  
  - Normalized, unmaterialized version
  - Patterns remain in structured form
  - Cleaned up and simplified via yq pipeline
  - Suitable for analysis and comparison

- **`contrib/mixs-patterns-materialized.yaml`**
  
  - Fully materialized version
  - All `structured_pattern` entries expanded to `pattern` (regex)
  - Cleaned up and simplified via yq pipeline
  - Suitable for tools that don't understand structured patterns

## Key Concepts

### Structured Patterns vs. Materialized Patterns

**Structured Patterns** (`structured_pattern`):

- High-level, declarative pattern definitions
- More human-readable and maintainable
- Easier to modify and understand
- Preferred source of truth in MIxS

**Materialized Patterns** (`pattern`):

- Low-level regex patterns
- Generated from structured patterns
- Required by some validation tools
- Harder to maintain manually

### Why Both Approaches?

The repository maintains both materialized and unmaterialized versions because:

1. **Development** - Developers work with structured patterns (easier to understand and modify)
2. **Validation** - Some tools require regex patterns for validation
3. **Analysis** - Unmaterialized version is cleaner for schema analysis
4. **Compatibility** - Materialized version ensures compatibility with tools that don't support structured patterns

### Makefile Targets

To generate these artifacts, use:

```bash
# Generate all contrib artifacts (includes all versions)
make all-contrib

# Generate specific artifacts
make contrib/mixs_structured_patterns_preferred.yaml
make contrib/mixs-normalized-minimized.yaml
make contrib/mixs-patterns-materialized.yaml

# Clean all contrib artifacts
make clean-contrib
```

### Integration with Main Build

These transformations are part of the main build process:

```bash
# Full build (includes all-contrib)
make all

# Clean and rebuild
make clean all
```

The `all-contrib` target (Makefile:103) is called by the main `all` target (Makefile:101) and generates all schema transformation artifacts.

## References

- **Makefile** - Contains all transformation rules (lines 139-182 for core transformations)
- **contrib.Makefile** - Additional contrib targets for analysis tools
- **LinkML Documentation** - https://linkml.io/linkml/ for details on LinkML tools and flags
- **yq Documentation** - https://github.com/mikefarah/yq for yq syntax and capabilities
