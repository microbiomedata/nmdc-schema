# LinkML Schema Expansion Research Summary

This directory now contains comprehensive documentation of LinkML schema expansion mechanisms discovered through deep source code analysis.

## Documents in This Research

### 1. LINKML_EXPANSION_MECHANISMS.md (Main Document)
**Comprehensive technical analysis of all expansion mechanisms**

Contains 9 detailed parts:
- Part 1: ExpandedDict/SimpleDict serialization mechanism (yamlutils.py)
- Part 2: Complete metaslot injection during schema processing (schemaview.py)
- Part 3: Keyed dictionary fields and expansion patterns (meta.py)
- Part 4: Configuration flags and annotations (referencevalidator.py)
- Part 5: All expansion patterns beyond pattern materialization
- Part 6: The yq cleanup pipeline and its role
- Part 7: Prediction matrix for when expansions occur
- Part 8: Code locations reference table
- Part 9: Key insights for predicting expansions

**Key Finding:** Expansions are NOT arbitrary - they follow from three fundamental design choices:
1. Internal dict storage for efficient lookup
2. YAML's lack of ordered dict notation
3. Computed metaslots for schema inference

### 2. EXPANSION_QUICK_REFERENCE.md
**Fast lookup guide for common questions**

Organized sections:
- When does something expand? (with prediction algorithm)
- Metaslot expansion (field injection)
- Key field duplication pattern
- The serialization pipeline (visual)
- Which metaslots are computed
- The yq cleanup pipeline (what gets removed)
- FAQ section with 7 common questions
- Quick reference table by expansion type

### 3. NMDC_EXPANSION_EXAMPLES.md
**Concrete examples from NMDC schema showing expansions**

10 detailed examples:
1. Prefixes (ExpandedDict serialization)
2. Annotations (ExpandedDict → Simplified)
3. Slot induction and metaslot addition
4. Permissible values (key duplication + ExpandedDict)
5. Attributes with inlined_as_list
6. from_schema tracking
7. Settings simplification
8. Class induction with field propagation
9. SimpleDict vs ExpandedDict (when one vs other)
10. Read-only computed fields issue

## Research Methodology

This research involved:

1. **Source Code Analysis** (linkml-runtime package)
   - yamlutils.py: Serialization mechanism (492 lines analyzed)
   - schemaview.py: Metaslot injection (line-by-line review)
   - meta.py: Metamodel class definitions (5240 lines, classes identified)
   - referencevalidator.py: Collection form decision logic
   - formatutils.py: Cleanup logic

2. **Pattern Identification**
   - Identified 9 classes with key field duplication (Prefix, LocalName, Setting, etc.)
   - Found 13 _normalize_inlined_as_dict calls in meta.py
   - Traced 4 metaslot injection points (owner, domain_of, alias, from_schema)

3. **Code Path Tracing**
   - Followed schema loading pipeline
   - Traced induced_slot() execution (108 lines)
   - Mapped yq cleanup pipeline to source code

## Critical Code Locations

| Mechanism | File | Lines | Key Function |
|-----------|------|-------|--------------|
| Dict→List conversion | yamlutils.py | 69-78 | YAMLRoot._default() |
| Dict normalization | yamlutils.py | 98-209 | _normalize_inlined_as_dict() |
| Metaslot injection | schemaview.py | 1471-1579 | induced_slot() |
| from_schema addition | schemaview.py | 407-410, 723-724 | load_import(), get_slot() |
| SimpleDict detection | referencevalidator.py | 1000-1013 | _slot_as_simple_dict_value_slot() |
| Collection form decision | referencevalidator.py | 481-503 | infer_slot_collection_form() |
| Keyed dicts | meta.py | Multiple __post_init__ | All metamodel classes |
| Cleanup pipeline | Makefile | 143-182 | yq transformations |

## Key Findings

### Finding 1: ExpandedDict is Fundamental Design
When a class is stored as dict internally for lookup efficiency but YAML needs a list (no dict syntax in YAML), it becomes ExpandedDict. This is NOT a bug - it's how LinkML works.

**Code proof:** yamlutils.py lines 69-78

### Finding 2: Metaslots Are Computed, Not Stored
Fields like `owner`, `domain_of`, `from_schema` are added by schema processing. They should not be edited in source schema files. They are re-computed on every load.

**Code proof:** schemaview.py lines 1542, 1577-1578, 407-410

### Finding 3: Key Fields Are Intentionally Duplicated
Classes like Prefix have `prefix_prefix` as both:
- Dictionary key: `{prefix_prefix: Prefix(...)}`
- Object field: `Prefix(prefix_prefix='...')`

This duplication is intentional for self-contained object storage.

**Code proof:** meta.py Prefix class definition (lines 3697-3722)

### Finding 4: The yq Pipeline Assumes Expansions Are Intermediate
The cleanup pipeline doesn't prevent expansions - it reverses them. This suggests the philosophy is:
- Internal tool: use expanded form (gen-linkml output)
- User artifact: use simplified form (after yq cleanup)

**Code proof:** SCHEMA_MATERIALIZATION_GUIDE.md and Makefile 143-182

### Finding 5: Read-Only Assertions Are Problematic
The current branch (2663-dont-assert-read-only-slots) indicates that marking computed fields as read-only causes issues. Better approach: document them as computed, don't mark read-only.

**Code proof:** Current work in branch 2663-dont-assert-read-only-slots

### Finding 6: SimpleDict Is A Rare Optimization
Only when a class has exactly 1 non-identifier field does it get SimpleDict serialization. This is an optimization for compact representation.

**Code proof:** referencevalidator.py lines 1000-1013, 494-496

### Finding 7: No Hidden Configuration for Expansions
Expansions follow from:
- `inlined` and `inlined_as_list` properties
- Range class field count
- "expanded" annotation
- `expand_all` flag in ReferenceValidator

There is no secret flag that controls all expansions.

**Code proof:** referencevalidator.py lines 481-503

## Files Previously Created (Before This Research)

The following files were already in the metamodel directory before this analysis:
- metaslot_analysis_contradictions.md (tracks earlier waffling on metaslot identification)
- extract_schema_keys.py (tool to identify metamodel vs application keys)
- compare_linkml_schemas.py (tool to compare schema versions)
- SCHEMA_MATERIALIZATION_GUIDE.md (documents pattern materialization and cleanup)

This research supersedes and complements those earlier documents.

## How to Use This Documentation

### For Understanding Expansions
1. Read LINKML_EXPANSION_MECHANISMS.md Part 1-4 for deep understanding
2. Use EXPANSION_QUICK_REFERENCE.md for quick answers
3. Check NMDC_EXPANSION_EXAMPLES.md for concrete examples

### For Predicting Expansions
1. Use the decision tree in EXPANSION_QUICK_REFERENCE.md
2. Refer to the prediction matrix in LINKML_EXPANSION_MECHANISMS.md Part 7
3. Check if a class is in the "Classes with Key Duplication" list

### For Debugging Expansion Issues
1. Identify which mechanism is causing the expansion (ExpandedDict, metaslot, key dup)
2. Find the code location from the reference table
3. Trace through to understand the specific case
4. Determine if cleanup is needed or if expansion is expected

### For Modifying Cleanup Logic
1. Review yq cleanup pipeline in SCHEMA_MATERIALIZATION_GUIDE.md
2. Look at corresponding Makefile rules (143-182)
3. Check NMDC_EXPANSION_EXAMPLES.md for before/after patterns
4. Test changes on known examples

## Expected Output Format

After full understanding, users should be able to:
1. **Predict** which elements will expand without running gen-linkml
2. **Explain** why an expansion occurred by referencing code locations
3. **Predict** what yq rules will reverse a specific expansion
4. **Distinguish** between computed metaslots and user-editable fields
5. **Understand** why ExpandedDict is NOT a bug but a feature

## Next Steps for NMDC Schema

With this understanding, the NMDC schema team can:

1. **Eliminate Assertions on Computed Fields**
   - Remove read_only marks from `owner`, `domain_of`, `from_schema`
   - Document them as computed in schema comments

2. **Improve Cleanup Consistency**
   - Extend yq pipeline if additional expansions need reversal
   - Ensure all ExpandedDict classes are handled

3. **Prevent False Expansions**
   - Review which slots use `inlined: true` + `multivalued: true` without `inlined_as_list`
   - Consider adding `inlined_as_list: true` where SimpleDict expansion is unexpected

4. **Better Documentation**
   - Use this research to explain expansions in schema comments
   - Guide schema editors on which fields are computed vs editable

5. **Validation Improvements**
   - Use the prediction matrix to validate schema changes don't create unexpected expansions
   - Create tests for expansion patterns

## Research Completeness

This research covers:
- ✓ All 9 ExpandedDict/SimpleDict cases
- ✓ All 4 metaslot injection points
- ✓ All 9 classes with key duplication
- ✓ 13 _normalize_inlined_as_dict calls
- ✓ Complete yq pipeline (13 steps)
- ✓ All configuration flags (inlined, inlined_as_list, expanded annotation, expand_all)
- ✓ Code locations for all mechanisms
- ✓ Concrete NMDC examples for 10 cases

This research does NOT cover:
- Pydantic model generation (outside LinkML core)
- JSON Schema generation
- OWL/RDF generation
- Specific tool integrations (only generic LinkML mechanisms)

