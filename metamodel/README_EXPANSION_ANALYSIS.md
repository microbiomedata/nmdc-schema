# LinkML Schema Expansion Analysis Documentation

This directory contains comprehensive documentation of how and why LinkML schemas expand during loading, processing, and serialization. This analysis is based on deep investigation of the LinkML runtime source code.

## Quick Navigation

### For Different Reading Levels

**I want a quick answer (5 minutes)**
- → Read: EXPANSION_QUICK_REFERENCE.md
- → Look for: Your question in the FAQ section

**I want to understand the mechanism (30 minutes)**
- → Read: EXPANSION_QUICK_REFERENCE.md
- → Then: LINKML_EXPANSION_MECHANISMS.md Parts 1-3
- → Then: NMDC_EXPANSION_EXAMPLES.md (relevant examples)

**I want the complete picture (2 hours)**
- → Read: LINKML_EXPANSION_MECHANISMS.md (all 9 parts)
- → Reference: EXPANSION_QUICK_REFERENCE.md for decision trees
- → Study: NMDC_EXPANSION_EXAMPLES.md for each mechanism
- → Understand: EXPANSION_RESEARCH_SUMMARY.md for methodology and findings

**I'm debugging a specific expansion issue**
- → Start: EXPANSION_QUICK_REFERENCE.md "Common Expansion Questions" section
- → Find: Your issue in NMDC_EXPANSION_EXAMPLES.md
- → Reference: Code locations in LINKML_EXPANSION_MECHANISMS.md Part 8

## Document Overview

### 1. EXPANSION_QUICK_REFERENCE.md (7 KB)
**The most useful document for daily work**

Fast lookup guide organized by:
- When does something expand? (with Python decision algorithm)
- Metaslot expansion (field injection)
- Key field duplication pattern
- The serialization pipeline (visual diagram)
- Which metaslots are computed
- The yq cleanup pipeline
- FAQ with 7 common questions
- Performance implications

**Best for:** Quick answers, decision trees, FAQ lookups

### 2. LINKML_EXPANSION_MECHANISMS.md (17 KB)
**The comprehensive technical reference**

Complete analysis in 9 parts:
1. ExpandedDict/SimpleDict serialization mechanism
2. Metaslot injection during schema processing
3. Keyed dictionary fields and expansion patterns
4. Configuration flags and annotations
5. All expansion patterns beyond pattern materialization
6. The yq cleanup pipeline and its role
7. Prediction matrix for all expansion types
8. Complete code locations reference table
9. Key insights for predicting expansions

**Best for:** Deep understanding, code tracing, explaining why something happens

### 3. NMDC_EXPANSION_EXAMPLES.md (12 KB)
**Concrete examples from NMDC schema**

10 detailed worked examples:
1. Prefixes (ExpandedDict serialization)
2. Annotations (ExpandedDict → Simplified)
3. Slot induction and metaslot addition
4. Permissible values (key duplication + ExpandedDict)
5. Attributes with inlined_as_list
6. from_schema tracking during imports
7. Settings simplification
8. Class induction with field propagation
9. SimpleDict vs ExpandedDict (design decisions)
10. Read-only computed fields issue

**Best for:** Learning by example, understanding your specific schema case

### 4. EXPANSION_RESEARCH_SUMMARY.md (9 KB)
**Research methodology and high-level findings**

Contains:
- Overview of all 4 documents
- Research methodology and scope
- Critical code locations table
- 7 key findings with code proof
- How to use this documentation
- Next steps for NMDC schema team
- Research completeness checklist

**Best for:** Understanding research scope, methodology, and next steps

## Core Concepts

### Three Types of Expansions

1. **ExpandedDict Serialization**
   - Internal: dict for O(1) lookup
   - External: list in YAML (YAML has no dict syntax)
   - Example: `prefixes: {schema: Prefix(...)}` → `prefixes: [{prefix_prefix: schema, ...}]`

2. **Metaslot Injection**
   - Computed fields added during schema processing
   - Examples: `owner`, `domain_of`, `from_schema`, `alias`
   - NOT user-editable, re-computed on every load

3. **Key Field Duplication**
   - Key appears as both dict key and object field
   - Intentional: for self-contained object storage
   - Examples: Prefix, LocalName, Setting, PermissibleValue

### Three Mechanisms That Cause Expansions

1. **Internal Storage vs External Format**
   - Dicts stored internally for efficiency
   - Lists in YAML for portability
   - Conversion happens in YAMLRoot._default() (yamlutils.py:69-78)

2. **Computed Schema Metadata**
   - induced_slot() infers schema relationships
   - Adds owner, domain_of, propagates properties
   - Always recalculated, never stored (except in dump)

3. **Metamodel Class Design**
   - Prefix, LocalName, Setting have multiple fields
   - Stored as keyed dicts for lookup
   - Expand to lists on serialization

## The Serialization Pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│ User creates/edits YAML schema (source form - compact)          │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│ SchemaView.load() reads YAML                                    │
│ - _normalize_inlined_as_dict() converts lists to dicts          │
│ - Internal: dicts for fast lookup                               │
│ - load_import() adds from_schema tracking                       │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│ Schema processing (gen-linkml, SchemaView methods)              │
│ - induced_slot() adds owner, domain_of, alias                  │
│ - Pattern materialization (structured_pattern → pattern)        │
│ - Attribute materialization (if requested)                      │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│ YAMLDumper.dumps() serializes to YAML                           │
│ - YAMLRoot._default() converts dicts to lists                   │
│ - remove_empty_items() cleans up None/empty values             │
│ - Output: YAML with expanded forms (ExpandedDict)              │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│ yq cleanup pipeline reverses expansions                         │
│ - Simplify annotations: list → key-value                       │
│ - Simplify prefixes: remove prefix_prefix field                │
│ - Remove from_schema, owner, domain_of metadata                │
│ - Remove redundant name fields                                 │
│ Output: YAML artifact (simplified form - back to compact)       │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│ Final schema artifact (cleaned, ready for distribution)         │
└─────────────────────────────────────────────────────────────────┘
```

## Code Locations Quick Reference

| Mechanism | File | Function | Lines |
|-----------|------|----------|-------|
| **Dict→List** | yamlutils.py | YAMLRoot._default() | 69-78 |
| **List→Dict** | yamlutils.py | _normalize_inlined_as_dict() | 98-209 |
| **Slot induction** | schemaview.py | induced_slot() | 1471-1579 |
| **Metaslot: owner** | schemaview.py | induced_slot() | 1542 |
| **Metaslot: domain_of** | schemaview.py | induced_slot() | 1577-1578 |
| **Metaslot: from_schema** | schemaview.py | load_import() | 407-410 |
| **SimpleDict detect** | referencevalidator.py | _slot_as_simple_dict_value_slot() | 1000-1013 |
| **Collection form** | referencevalidator.py | infer_slot_collection_form() | 481-503 |
| **Keyed dicts** | meta.py | Various __post_init__ | Multiple |
| **Cleanup** | Makefile | yq pipeline | 143-182 |

## Key Findings

### Finding 1: Expansions Are Not Bugs
ExpandedDict serialization is fundamental LinkML design, not an error. It's how LinkML represents collections that need both fast lookup (dict) and YAML compatibility (list).

### Finding 2: Computed Fields Should Not Be Trusted
Fields like `owner`, `domain_of`, `from_schema` are re-computed on every schema load. Don't edit them in source schema - they'll be overwritten.

### Finding 3: The yq Pipeline Assumes Expansions Happen
The cleanup pipeline exists because expansions ARE expected. It doesn't prevent them - it reverses them for the final artifact.

### Finding 4: SimpleDict Is An Optimization
When a class has exactly 1 non-identifier field, it gets SimpleDict (more compact) instead of ExpandedDict. This is an intentional optimization.

### Finding 5: No Hidden Configuration
There is no secret flag controlling all expansions. They follow from:
- `inlined` and `inlined_as_list` properties
- Range class field count
- "expanded" annotation
- That's it.

### Finding 6: Key Duplication Is Intentional
Classes like Prefix have the key field twice (as dict key and field) for self-contained object storage. This is not redundancy - it's necessary for proper serialization.

### Finding 7: Read-Only Is Problematic
Marking computed fields as read-only causes issues in induction. Better to document them as computed without marking read-only.

## How to Use This Documentation

### Understanding a Specific Expansion

1. Identify what expanded (e.g., "my prefixes became a list")
2. Open EXPANSION_QUICK_REFERENCE.md
3. Find "Common Expansion Questions" section
4. Look for your specific case (e.g., "Why does `prefixes: {schema: "..."}` become a list?")
5. Read the explanation and code reference
6. If you need deeper understanding, go to LINKML_EXPANSION_MECHANISMS.md Part 1

### Predicting If Something Will Expand

1. Open EXPANSION_QUICK_REFERENCE.md
2. Go to "When Does Something Expand?" section
3. Use the decision tree algorithm
4. Apply to your specific slot/class
5. Reference NMDC_EXPANSION_EXAMPLES.md for similar examples

### Debugging an Expansion Issue

1. Identify which type of expansion (ExpandedDict, metaslot, key dup)
2. Find code location from reference table
3. Trace through code using LINKML_EXPANSION_MECHANISMS.md
4. Compare with similar example in NMDC_EXPANSION_EXAMPLES.md
5. Determine if expansion is expected or needs fixing

### Modifying Cleanup Logic

1. Review current pipeline: SCHEMA_MATERIALIZATION_GUIDE.md
2. Check corresponding Makefile rules: Makefile 143-182
3. Study before/after patterns: NMDC_EXPANSION_EXAMPLES.md
4. Test on known examples
5. Update documentation if behavior changes

## Related Documents in This Directory

This analysis complements:
- **SCHEMA_MATERIALIZATION_GUIDE.md** - Pattern materialization and cleanup pipeline
- **extract_schema_keys.py** - Tool to identify metamodel vs application keys
- **compare_linkml_schemas.py** - Tool to compare schema versions
- **metaslot_analysis_contradictions.md** - Earlier analysis and corrections

## Research Scope

### Covered in This Analysis
- ExpandedDict and SimpleDict serialization mechanisms
- All metaslot injection points
- Key field duplication patterns
- Configuration flags (inlined, inlined_as_list, expanded annotation)
- Complete yq cleanup pipeline
- Code locations for all mechanisms
- Concrete NMDC examples

### Not Covered (Out of Scope)
- Pydantic model generation details
- JSON Schema generation
- OWL/RDF generation
- Specific tool integrations
- Historical evolution of LinkML

## Contact / Questions

If this analysis is unclear:
1. Check the relevant document for your level of understanding
2. Read the example most similar to your case
3. Trace the code location provided
4. Refer to EXPANSION_RESEARCH_SUMMARY.md for research methodology

## Document Sizes

- EXPANSION_QUICK_REFERENCE.md: 7 KB (10 min read)
- LINKML_EXPANSION_MECHANISMS.md: 17 KB (45 min read)
- NMDC_EXPANSION_EXAMPLES.md: 12 KB (30 min read)
- EXPANSION_RESEARCH_SUMMARY.md: 9 KB (20 min read)
- **Total: 45 KB (105 minutes of reading)**

## Version Information

- **Created:** October 21, 2025
- **Analyzed:** LinkML runtime version 1.9.3
- **Python version:** 3.11
- **NMDC Schema:** Branch 2663-dont-assert-read-only-slots
- **Analysis depth:** Complete source code examination with code location references
