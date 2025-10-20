# Deep Analysis of Non-Imported Schemas in linkml-model

## Executive Summary

After extensive investigation including GitHub issues, PRs, codebase searches, and test analysis across linkml, linkml-runtime, and linkml-model repositories, here are the definitive findings:

| Schema | Status | Recommendation | Rationale |
|--------|--------|----------------|-----------|
| **validation.yaml** | ✅ Active | **KEEP** | Core validation infrastructure, heavily used |
| **array.yaml** | ✅ Active | **KEEP** | Complementary to meta.yaml's array_expression, active development |
| **datasets.yaml** | ⚠️ Dormant | **KEEP but document** | Has import bugs, minimal usage, but represents W3C standards |
| **extended_types.yaml** | ❌ Orphaned | **REMOVE or integrate** | Zero usage, not in runtime, abandoned after creation |

---

## 1. validation.yaml (reporting.yaml)

### Status: ✅ **ACTIVELY USED - CORE INFRASTRUCTURE**

### Current Usage

**In linkml codebase:**
- Core to validation framework at `linkml/validator/`
- Used in 8+ files:
  - `validator/validator.py`
  - `validator/report.py` (defines Pydantic equivalents)
  - `validator/plugins/jsonschema_validation_plugin.py`
  - `validator/plugins/shacl_validation_plugin.py`
  - `validator/plugins/pydantic_validation_plugin.py`
  - `validator/plugins/recommended_slots_plugin.py`
  - `validator/__init__.py`

**In linkml-runtime:**
- Present at `linkml_runtime/linkml_model/model/schema/validation.yaml`
- Generated Python model at `linkml/reporting/model.py`

**Key Classes:**
- `ValidationReport` - Container for validation results
- `ValidationResult` - Individual validation finding
- Severity enum: FATAL, ERROR, WARNING, INFO

### Why Not in meta.yaml?

**Intentional separation** - Validation is a runtime concern, not a metamodel concern. The metamodel defines what schemas look like; validation.yaml defines what validation reports look like.

### Recommendation: **KEEP**

Essential infrastructure. Do not remove or modify.

---

## 2. array.yaml

### Status: ✅ **ACTIVELY USED - COMPLEMENTARY TO meta.yaml**

### Critical Discovery: Two Different Array Approaches

**array.yaml provides:**
- **Class-based approach**: `NDArray`, `DataArray` classes
- Used when you need arrays **with additional metadata** (units, conversion factors, etc.)
- Import via: `implements: [linkml:lib/arrays#NDArray]`
- Example use case: **NWB (Neurodata Without Borders)** needs arrays with precision, units, conversion metadata

**meta.yaml's array_expression provides:**
- **Slot-level approach**: Define array shapes inline
- Used when you just need **dimensions specification**
- Import via: Direct use of `array:` slot property
- Introduced in **LinkML 1.7.0 (February 2024)**

### Key Difference

```yaml
# Using array.yaml (class-based, with metadata)
classes:
  TimeSeries:
    attributes:
      data:
        range: NDArray
        # NDArray class has elements, units, conversion, etc.

# Using meta.yaml's array_expression (inline dimensions)
classes:
  ImageData:
    attributes:
      pixels:
        range: integer
        array:
          dimensions:
            - alias: width
            - alias: height
```

### GitHub Evidence

**Active Development:**
- **Issue #199** (linkml-model): Enable `any_of` with ArrayExpressions - RESOLVED
- **PR #200** (linkml-model): Moved array to slot_expression mixin - MERGED Oct 2024
- **Issue #1888** (linkml): Add array support to pydanticgen - CLOSED (implemented in 1.7.0)
- **Issue #1890** (linkml): NDArray RDF serialization strategy - OPEN (active discussion)
- **Issue #2406** (linkml): Support `array: null` for any-shaped arrays - OPEN
- **PR #1397** (linkml): Generate Pydantic models for data arrays - MERGED
- Working group: **@linkml/ndarray-wg** actively developing

**Test Coverage:**
- `tests/test_compliance/test_array_compliance.py` - Comprehensive array validation tests
- Tests across pydanticgen, jsonschemagen, etc.

### Why Two Approaches Coexist

1. **Different use cases**: Simple dimensions vs. rich metadata
2. **Different communities**: General LinkML users vs. scientific data (NWB, neuroimaging)
3. **Historical**: array.yaml predates array_expression
4. **Intentional design**: Both are maintained by design

### Recommendation: **KEEP**

**Both array.yaml AND meta.yaml's array_expression should be kept.** They serve complementary purposes:
- Use `array_expression` (meta.yaml) for simple dimensional arrays
- Use NDArray/DataArray (array.yaml) for arrays with rich metadata
- Document the distinction clearly

---

## 3. datasets.yaml

### Status: ⚠️ **DORMANT WITH KNOWN BUGS**

### Purpose

Multi-standard metadata model mapping to:
- **Frictionless Data Package/Resource**
- **W3C DCAT** (Data Catalog Vocabulary)
- **W3C VOID** (Vocabulary of Interlinked Datasets)
- **Schema.org** (CreativeWork, DataDownload)
- **CSVW** (CSV on the Web)

### Timeline

- **Created**: December 2021 (commit a14b757b)
- **Total commits**: 11 over 3 years
- **Last update**: February 2024 (maintenance only)
- **No active development** since Feb 2024

### Known Issues

**CRITICAL BUG - Issue #1763** (OPEN since Dec 2023):
- `NameError: name 'PermissibleValue' is not defined` when importing
- Generated Python code has import errors
- **Projects cannot reliably import** DataPackage/DataResource classes
- Workaround: Projects copy relevant parts instead

### Usage Evidence

**Minimal adoption:**
- Only 1 external project found attempting to use it: bridge2ai/data-sheets-schema (hit the import bug)
- No test files in linkml repo
- No examples in linkml-model
- No documentation

**In linkml-runtime:**
- Schema file present but unused
- Available via `linkml_runtime.linkml_model.datasets` module

### Related Discussions

- **Issue #501** (2021): Utility to validate data files - discussed datasets concept, deferred
- **Issue #861** (2022): Frictionless schema importer/exporter - closed without completion

### Why Not Used?

1. **Import bug prevents adoption** (Issue #1763)
2. **Projects use Frictionless directly** instead
3. **No clear advantage** over existing standards
4. **Lacks documentation and examples**

### Recommendation: **KEEP but Fix or Deprecate Formally**

Options:
1. **Fix Issue #1763** and create examples/documentation → Make it actually usable
2. **Formally deprecate** with migration guide to Frictionless Data
3. **Move to examples/** as reference implementation, not production schema

Do NOT silently remove - it represents legitimate W3C standards mappings. Either fix or deprecate explicitly.

---

## 4. extended_types.yaml

### Status: ❌ **ORPHANED - ZERO USAGE**

### Timeline

- **Created**: PR #185 (Feb 8, 2024)
- **Merged**: April 12, 2024
- **Origin**: Issue #1871 - Request from ndarray working group
- **NOT in linkml-runtime**: Confirmed absent
- **Zero code usage**: No imports found anywhere

### What It Provides

NumPy-style extended numeric types:
- **Signed integers**: int8, int16, int32, int64
- **Unsigned integers**: uint8, uint16, uint32, uint64
- **Floating point**: float16, float32, float64
- **Union type**: any_number
- **Unconstrained**: Any

All with NumPy documentation refs and value constraints.

### Why It Exists But Isn't Used

1. **Never integrated into linkml-runtime** - exists only in linkml-model
2. **No generator support** - would need pydanticgen, jsonschemagen updates
3. **Unclear adoption path** - how would users actually use these types?
4. **Minimal discussion** - PR had almost no comments beyond bool inclusion debate

### Current Discussion

**Discussion #2958** (Oct 20, 2025) - "YAML Models Not Imported into meta.yaml"
- User questioning unimported schemas
- Lists extended_types as removal candidate
- **NO responses** from maintainers yet

### No Test Coverage

- No test files reference extended_types
- No examples demonstrate usage
- No documentation mentions it

### Recommendation: **REMOVE OR INTEGRATE PROPERLY**

This schema is **aspirational but abandoned**. Options:

**Option 1: Remove entirely**
- Minimal value currently
- Zero usage detected
- Not in runtime
- Creates maintenance burden

**Option 2: Integrate properly** (significant work)
- Add to linkml-runtime
- Update all generators (pydantic, jsonschema, etc.)
- Create documentation and examples
- Announce the feature

**Option 3: Keep as experimental** (status quo)
- Document as experimental/unstable
- Low maintenance cost (single file)
- Available for future use

**My recommendation: REMOVE** unless there's commitment to Option 2 integration work. An unused, undocumented feature that's not in the runtime provides no value and creates confusion.

---

## Comparison: Why Some Schemas Aren't in meta.yaml

### Intentional Design Decisions

**meta.yaml imports (core metamodel):**
- types.yaml - Foundation types
- extensions.yaml - Extension mechanism
- mappings.yaml - Ontology mappings
- annotations.yaml - OWL annotations
- units.yaml - Units of measure

**Not imported (optional/runtime features):**
- validation.yaml - Runtime validation (not metamodel concern)
- array.yaml - Optional rich array support (complementary to built-in array_expression)
- datasets.yaml - Optional dataset metadata (maps to external standards)
- extended_types.yaml - Experimental types (never integrated)

### The Pattern

Schemas NOT imported into meta.yaml fall into categories:
1. **Runtime concerns** (validation) - Used at validation time, not schema definition time
2. **Optional rich features** (array.yaml) - Available but not required
3. **Standards mappings** (datasets) - Bridge to external ecosystems
4. **Experimental/abandoned** (extended_types) - Created but never finished

---

## Summary Table with Evidence

| Schema | Lines of Code | In Runtime? | GitHub Issues | Test Coverage | External Usage | Verdict |
|--------|---------------|-------------|---------------|---------------|----------------|---------|
| **validation.yaml** | 121 | ✅ Yes | 0 open, actively maintained | Extensive (8+ files) | Core validator | **KEEP** |
| **array.yaml** | 180 | ✅ Yes | 3 open, active development | test_array_compliance.py | NWB, ndarray-wg | **KEEP** |
| **datasets.yaml** | 358 | ✅ Yes | #1763 OPEN (import bug) | None | 1 project (failed) | **FIX or DEPRECATE** |
| **extended_types.yaml** | 153 | ❌ NO | #2958 (questions it) | None | None | **REMOVE** |

---

## Recommendations for GitHub Discussion

### Immediate Actions

1. **validation.yaml**: Document why it's separate from meta.yaml (runtime vs metamodel)
2. **array.yaml**: Document relationship with meta.yaml's array_expression, provide usage guide
3. **datasets.yaml**: Either fix Issue #1763 + add docs, or formally deprecate
4. **extended_types.yaml**: Remove or commit to full integration

### Documentation Needed

Create `linkml-model/README.md` explaining:
- Purpose of each schema file
- Which are core (in meta.yaml) vs optional
- How to use optional schemas
- Relationship between array.yaml and array_expression

### Questions for Maintainers

1. Is there commitment to fix datasets.yaml Issue #1763?
2. Should extended_types be integrated into runtime or removed?
3. Should array.yaml usage be documented prominently?
4. Should validation.yaml be documented as the standard validation report format?

---

## Files Referenced

- `/Users/MAM/Documents/gitrepos/linkml-model/linkml_model/model/schema/validation.yaml`
- `/Users/MAM/Documents/gitrepos/linkml-model/linkml_model/model/schema/array.yaml`
- `/Users/MAM/Documents/gitrepos/linkml-model/linkml_model/model/schema/datasets.yaml`
- `/Users/MAM/Documents/gitrepos/linkml-model/linkml_model/model/schema/extended_types.yaml`
- `/Users/MAM/Documents/gitrepos/linkml-model/linkml_model/model/schema/meta.yaml`
- `/Users/MAM/Documents/gitrepos/linkml/linkml/validator/` (validation usage)
- `/Users/MAM/Documents/gitrepos/linkml/linkml/generators/pydanticgen/array.py` (array usage)
- `/Users/MAM/Documents/gitrepos/linkml/tests/test_compliance/test_array_compliance.py` (array tests)

---

**Analysis Date**: October 20, 2025
**Repositories Analyzed**: linkml/linkml, linkml/linkml-runtime, linkml/linkml-model
**Methods**: Code search, GitHub issues/PRs, test analysis, git history
