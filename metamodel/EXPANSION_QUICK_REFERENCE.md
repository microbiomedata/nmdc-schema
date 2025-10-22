# LinkML Expansion Quick Reference Guide

## When Does Something Expand?

### Collection Expansion (ExpandedDict)

**When:** A slot is stored as dict internally, but serialized as list during dump.

**Why:** yamlutils.py lines 69-78 convert internal dicts to lists (YAML has no ordered dict syntax)

**Affected Elements:**
- Any SlotDefinition with `inlined: true`, `multivalued: true`, `inlined_as_list: false`
- Range class must have 2+ non-identifier fields (else SimpleDict applies)

**Examples in LinkML metamodel:**
```
prefixes: {prefix_prefix → Prefix} → List of Prefix objects
annotations: {tag → Annotation} → List of Annotation objects
extensions: {tag → Extension} → List of Extension objects
permissible_values: {text → PermissibleValue} → List of PermissibleValue objects
local_names: {local_name_source → LocalName} → List of LocalName objects
settings: {setting_key → Setting} → List of Setting objects
alt_descriptions: {source → AltDescription} → List of AltDescription objects
```

### How to Predict If Something Will Be ExpandedDict

```
if slot.multivalued and slot.inlined and not slot.inlined_as_list:
    range_class = get_range(slot)
    non_pk_fields = [f for f in range_class.attributes if not f.identifier and not f.key]

    if "expanded" in slot.annotations and slot.annotations["expanded"].value:
        → EXPANDEDDICT (forced by annotation)
    elif len(non_pk_fields) == 1:
        → SIMPLEDICT (special case: only one meaningful field)
    else:
        → EXPANDEDDICT (default for multi-field objects)
```

## Metaslot Expansion (Field Injection)

### Always Added During Slot Induction

| Field | Source | Line | Example |
|-------|--------|------|---------|
| `owner` | induced_slot() | schemaview.py:1542 | `owner: my_class` |
| `domain_of` | induced_slot() | schemaview.py:1577-1578 | `domain_of: [class_a, class_b]` |
| `alias` | induced_slot() | schemaview.py:1574 | `alias: my_slot` |

### From Schema Addition

**When:** During schema loading or slot retrieval

**Lines:** schemaview.py:407-410 (load_import), schemaview.py:723-724 (get_slot)

**Pattern:**
```python
# In load_import
e.from_schema = schema.id

# In get_slot for attributes
slot.from_schema = class.from_schema
slot.owner = class.name
```

## Key Field Duplication Pattern

### Classes with Key Duplication

These metamodel classes store the key BOTH as dict key AND as field:

```
Class        Key Field              Other Fields                Internal Form
------       ---------              -----------                 ----------------
Prefix       prefix_prefix          prefix_reference            {key: Prefix(...)}
LocalName    local_name_source      local_name_value            {key: LocalName(...)}
Setting      setting_key            setting_value               {key: Setting(...)}
Annotation   tag                    value, description, etc.    {key: Annotation(...)}
Extension    tag                    value, description, etc.    {key: Extension(...)}
PermValue    text                   description, meaning, etc.  {key: PermissibleValue(...)}
AltDescr     source                 description                 {key: AltDescription(...)}
```

### Why Double Storage?

1. **Efficient lookup** - Dict keys for O(1) access
2. **Self-contained objects** - Each object carries its own identifier
3. **Round-tripping** - Can serialize and deserialize without context

## The Serialization Pipeline

```
User edits YAML (compact form)
    ↓
SchemaView loads (converts list to internal dict)
    ↓
Processing/induction (adds computed metaslots)
    ↓
YAMLRoot._default() dumps (converts internal dict back to list)
    ↓
Output YAML (expanded form with list syntax)
    ↓
yq cleanup pipeline (converts list back to simplified form)
    ↓
Final artifact (compact form again)
```

## Which Metaslots Are "Computed"?

These should NOT be edited in source schema (they're recalculated on load):

| Metaslot | Purpose | Set By | Can Edit? |
|----------|---------|--------|-----------|
| `owner` | Which class owns slot | induced_slot() | No - computed |
| `domain_of` | All classes using slot | induced_slot() | No - computed |
| `from_schema` | Which import this came from | load_import() | No - computed |
| `alias` | Normalized slot name | induced_slot() | Yes - but usually derived |

## The yq Cleanup Pipeline (What Gets Removed)

```bash
# Step 1: Remove from_schema metadata
del(.. | select(has("from_schema")).from_schema)

# Step 2: Simplify annotations (expansions → key-value)
.classes[] |= select(has("annotations")).annotations |= map_values(.value)

# Step 3: Simplify prefixes (dict → values)
.prefixes |= map_values(.prefix_reference)

# Step 4: Simplify settings
.settings |= map_values(.setting_value)

# Step 5: Same annotation simplification for slots
.slots[] |= select(has("annotations")).annotations |= map_values(.value)

# Step 6-13: Remove redundant name fields
del(.classes.[].name)
del(.classes.[].slot_usage.[].name)
del(.enums.[].name)
del(.enums.[].permissible_values.[].text)
del(.slots.[].name)
del(.subsets.[].name)
```

## Common Expansion Questions

### Q: Why does `prefixes: {schema: "..."}` become a list?

**A:** Because internally, SchemaView stores it as `{schema: Prefix(...)}` dict for fast lookup. When dumping to YAML, the dict is converted to a list (YAML limitation). The yq cleanup step converts it back.

### Q: When I call `induced_slot()`, why do I get extra fields?

**A:** Because induced_slot() at schemaview.py:1542 and 1577-1578 adds:
- `owner` - The class that owns the slot
- `domain_of` - All classes using the slot
These are computed fields, not from the original schema.

### Q: Why does every class get `from_schema` after loading?

**A:** Because load_import() at schemaview.py:407-410 adds it to track which imported file each element came from. It's metadata for provenance tracking.

### Q: What's the difference between `inlined` and `inlined_as_list`?

**A:**
```
inlined: false  → Values are URIs/CURIEs only, not full objects
inlined: true, inlined_as_list: true  → Full objects in list form
inlined: true, inlined_as_list: false → Full objects in dict form (ExpandedDict)
```

### Q: Why does the "name" field appear in classes and slots?

**A:** Because classes and slots are stored in dicts: `{class_name: {name: class_name, ...}}`. The name is duplicated as a field for self-contained storage. The yq pipeline removes this redundancy.

### Q: Can I mark computed fields as read-only?

**A:** Yes, but LinkML handles this inconsistently. The current branch (2663-dont-assert-read-only-slots) suggests there are issues with read-only assertions on computed fields. It's safer to not mark `owner`, `domain_of`, and `from_schema` as read-only if they're generated by induction.

## Testing Expansions

### See the Internal Dict Form
```python
from linkml_runtime.utils.schemaview import SchemaView
sv = SchemaView('schema.yaml')
# Prefixes are stored as dict internally
print(sv.schema.prefixes)  # {prefix_name: Prefix(...), ...}
```

### See the Expanded List Form
```python
import yaml
from linkml_runtime.utils.yamlutils import root_representer
# After dumping, check the serialized form
yaml.dump(sv.schema)  # Shows list form for prefixes
```

### See the Simplified Form
```bash
# Run through yq pipeline
yq eval '.prefixes |= map_values(.prefix_reference)' input.yaml
```

## Performance Implications

1. **Internal dict storage** is fast for lookups by key
2. **List serialization** adds slight overhead on dump (dict→list conversion)
3. **yq cleanup** is relatively slow for large schemas (but only done once at build time)
4. **Reload** is fast (list→dict conversion happens in __post_init__)

## Files to Understand

| File | Purpose | Key Lines |
|------|---------|-----------|
| yamlutils.py | Serialization control | 69-78 (dict→list) |
| schemaview.py | Schema processing | 407-410, 723-724 (from_schema), 1471-1579 (induction) |
| referencevalidator.py | Collection form detection | 481-503 (ExpandedDict decision) |
| meta.py | Metamodel class definitions | 194, 379, 392, 394, 571, 587-615, 896 |
| formatutils.py | remove_empty_items() | 123-186 (cleanup logic) |
| Makefile | Cleanup pipeline | 143-182 |

## Summary Table

| Expansion Type | Trigger | Reversal | Metafile Reference |
|---|---|---|---|
| **ExpandedDict** | inlined: true, multivalued: true, 2+ fields | yq map_values | Part 1, yamlutils.py:69-78 |
| **Metaslot injection** | induced_slot() call or SchemaView load | Remove with yq | Part 2, schemaview.py:407-410, 1542, 1577 |
| **Key duplication** | Class definition in metamodel | Already present, can't remove | Part 3, meta.py |
| **from_schema tracking** | load_import() or get_slot() | yq delete | Part 2, schemaview.py:407-410 |
| **Computed metaslots** | Slot induction | Don't rely on them persisting | Part 2 table |
