# NMDC Schema Validation & Migration Report  
### _Work session: 2025-05-29_

---

## 1. Background  

| Item | Value |
|------|-------|
| Source database | NMDC production API (`https://api.microbiomedata.org`) |
| Export script   | `pure-export` (max 200 000 docs/collection) |
| Initial schema in repo | **11.7.0** (`nmdc_schema/nmdc_materialized_patterns.yaml`) |
| Validation tool | `linkml-validate` (via Poetry venv) |
| Host            | `mark-NUC10i7FNH` (Ubuntu 22.04, yq v4.44.5 from Snap) |

The first validation run failed because every member of `data_object_set`
was missing the **required** slot **`data_category`** (added in schema 11.7.0).

```
[ERROR] … 'data_category' is a required property in /data_object_set/0  
[ERROR] … 'data_category' is a required property in /data_object_set/1  
…
```

No other kinds of *ERROR* messages were present.

---

## 2. Quick experiment (“hybrid check”)

1. **Removed** the entire `data_object_set` key  
   ```bash
   yq e 'del(.data_object_set)' \
       local/mongo_as_nmdc_database_rdf_safe.yaml \
     | cat > local/mongo_as_nmdc_database_rdf_safe_NO_DOBJ.yaml
   ```
   *Size dropped from 481 MB → 468 MB.*

2. **Validated** the trimmed file against **schema 11.6.1** (≈ 15 min).  
   Purpose: confirm that `data_category` is the only breaking change.

---

## 3. Long-term solutions considered

| Option | Description | Pros | Cons |
|--------|-------------|------|------|
| **A** | Add legal `data_category`, keep schema 11.7.0 | Current, future-proof | Requires migration step |
| **B** | Stay on schema 11.6.1 | No data change | Stuck on deprecated model |
| **C** | Fork 11.7.0 and make `data_category` optional | No data change | Private dialect; maintenance burden |
| **D** | Hybrid (remove collection) | Quick inspection only | Loses entire collection; unusable downstream |

---

## 4. Recommended path – **Option A**  
Use existing migrator **`migrator_from_11_6_1_to_11_7_0.py`** which populates
`data_category` automatically.

### 4.1 One-time migration procedure

```bash
# 1 – duplicate original YAML
cp local/mongo_as_unvalidated_nmdc_database.yaml \
   local/mongo_as_unvalidated_nmdc_database_PREMIG.yaml

# 2 – pretend dump is 11.6.1 so the migrator will run
yq e '.schema_version = "11.6.1"' \
    local/mongo_as_unvalidated_nmdc_database_PREMIG.yaml \
  | cat > local/mongo_as_unvalidated_nmdc_database_11_6_1.yaml

# 3 – run migration-recursion
time poetry run migration-recursion \
     --input-path  local/mongo_as_unvalidated_nmdc_database_11_6_1.yaml \
     --schema-path nmdc_schema/nmdc_materialized_patterns.yaml \
     --output-path local/mongo_as_nmdc_database_rdf_safe_FIXED.yaml \
     --migrators   nmdc_schema.migrators.migrator_from_11_6_1_to_11_7_0
```

### 4.2 Final validation (schema 11.7.0)

```bash
time poetry run linkml-validate \
     --schema nmdc_schema/nmdc_materialized_patterns.yaml \
     local/mongo_as_nmdc_database_rdf_safe_FIXED.yaml \
  > local/mongo_as_nmdc_database_validation_FIXED_11_7_0.log
```

Success criterion: **zero** `ERROR` lines.

### 4.3 Pipeline integration  

After confirming success, simply let `migration-recursion` run with its default
migrator set; no manual header tweaking will be necessary.

---

## 5. Appendix  

### 5.1 Top-level keys in original dump
```
biosample_set
calibration_set
configuration_set
data_generation_set
data_object_set
field_research_site_set
instrument_set
manifest_set
material_processing_set
processed_sample_set
study_set
workflow_execution_set
```

### 5.2 File size comparison

| File | Size |
|------|------|
| `mongo_as_unvalidated_nmdc_database.yaml` | 481 MB |
| `mongo_as_nmdc_database_rdf_safe.yaml` | 482 MB |
| `mongo_as_nmdc_database_rdf_safe_NO_DOBJ.yaml` | 468 MB |
| `mongo_as_nmdc_database_rdf_safe_FIXED.yaml` (target) | ≈ 482 MB |

### 5.3 Helpful snippets
```bash
# list distinct error messages
grep '^\[ERROR]' validation.log | sed 's/^\[[^]]*\] *//' | sort | uniq -c

# verify key absence
yq e 'has("data_object_set")' mongo_as_nmdc_database_rdf_safe_NO_DOBJ.yaml
```

---

_Compiled by: Mark Miller_  
_Date: 2025-05-29_
