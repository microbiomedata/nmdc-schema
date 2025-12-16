# Validation-Error Summary  
*Session date: 2025-05-29*

---

## Error types observed

| # | Error kind | Schema version(s) | Affected records | Message skeleton |
|---|------------|-------------------|------------------|------------------|
| 1 | **Missing required slot** `data_category` | 11.7.0 | ≈ 160 000 (all members of `data_object_set`) | `'data_category' is a required property in /data_object_set/<idx>` |
| 2 | **Enum value not recognised** (`data_object_type`) | 11.6.1 | 2 583 | `'Direct Infusion FT-ICR MS Analysis Results' is not one of [...]` |
| – | _none_ | 11.7.0 (without `data_object_set`) | 0 | — |
| – | _none_ | 11.6.1 (without `data_object_set`) | 0 | — |

---

### 1 .  Missing `data_category` (11 .7 .0)

* Location: every element of `data_object_set`  
* Reason: slot **became required** in schema 11.7.0; export was produced before the new migrator populated the value.

### 2 .  Invalid `data_object_type` value (11 .6 .1)

* Count: 2 583 DataObjects  
* Old enum label (11.6.1): `Direct Infusion FT ICR-MS Analysis Results`  
* New enum label (data + 11.7.0): `Direct Infusion FT-ICR MS Analysis Results`  
* Reason: enumeration list was renamed between 11.6.1 and 11.7.0.

---

## Clean validation cases

* Removing `data_object_set` produces **zero errors** under **both** 11.6.1 and 11.7.0, proving every other collection is already compliant.

---

## Implications & next steps

1. **Target latest schema (11.7.0)**  
   • Run migrator `migrator_from_11_6_1_to_11_7_0` to add `data_category`.  
   • Keep existing `data_object_type` labels (they match 11.7.0).  
   • Re-validate ⇒ expected “No issues found”.

2. **Stay on old schema (11.6.1)**  
   • Either rename 2 583 enum values back to the old form **or** relax the enum list.  
   • Slot `data_category` remains optional, so no further changes needed.

3. **Hybrid / diagnostic runs** (drop `data_object_set`) are fine for quick checks but not suitable for production data releases.

---
